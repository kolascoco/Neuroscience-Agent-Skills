#!/usr/bin/env python3
"""Tests for validate_analysis_config.py.

Run: python3 -m unittest discover -s scripts -p 'test_*.py' -v
Standard library only; no third-party test runner.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "validate_analysis_config.py"


def declared(position, name, consumes):
    """One well-formed entry for config.json's instruments array."""
    return {
        "stage": name,
        "position": position,
        "consumes": consumes,
        "name": name,
        "version": "1.0.0",
        "install_source": "pypi",
        "parameters": {},
    }


def observed(name, validated_at, status="PASS", consumes=None):
    """One well-formed entry for gate_status.json's instrument_status array."""
    return {
        "stage": name,
        "status": status,
        "validated_at": validated_at,
        "runtime_s": 1.5,
        "output_shape": "[64, 1000]",
        "input_ref": "sources[0]" if consumes is None else consumes,
    }


def config_with(instruments):
    return {
        "analysis_id": "H-2026-001",
        "status": "draft",
        "sources": [],
        "frozen_decisions": {},
        "compute_gates": {},
        "required_outputs": [],
        "interpretation": "unfrozen",
        "instruments": instruments,
        "family": {"family_id": None, "parent_analysis": None, "varies": []},
    }


def run(config, gate_status=None, write_gate_status=True):
    """Run the validator against a temp config, returning the CompletedProcess."""
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        config_path = base / "config.json"
        config_path.write_text(json.dumps(config), encoding="utf-8")
        if write_gate_status:
            payload = {"instrument_status": gate_status or []}
            (base / "gate_status.json").write_text(
                json.dumps(payload), encoding="utf-8"
            )
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(config_path)],
            capture_output=True,
            text=True,
        )


DECLARED_CHAIN = [
    declared(0, "filter", None),
    declared(1, "ica", "filter"),
    declared(2, "epoch", "ica"),
]

OBSERVED_CHAIN = [
    observed("filter", "2026-08-19T10:00:00+00:00"),
    observed("ica", "2026-08-19T11:00:00+00:00", consumes="filter"),
    observed("epoch", "2026-08-19T12:00:00+00:00", consumes="ica"),
]


class TestSchema(unittest.TestCase):
    def test_missing_instruments_key_names_the_fix(self):
        config = config_with([])
        del config["instruments"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("instruments", result.stderr)

    def test_empty_chain_passes(self):
        result = run(config_with([]))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_wellformed_chain_passes(self):
        result = run(config_with(DECLARED_CHAIN), OBSERVED_CHAIN)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_declared_missing_key_fails(self):
        broken = [dict(DECLARED_CHAIN[0])]
        del broken[0]["install_source"]
        result = run(config_with(broken), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("install_source", result.stderr)

    def test_observed_missing_key_fails(self):
        broken = [dict(OBSERVED_CHAIN[0])]
        del broken[0]["output_shape"]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("output_shape", result.stderr)

    def test_invalid_status_fails(self):
        broken = [observed("filter", "2026-08-19T10:00:00+00:00", status="OK")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("status", result.stderr)

    def test_unparseable_validated_at_fails(self):
        broken = [observed("filter", "yesterday")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)


class TestTwoFileAgreement(unittest.TestCase):
    def test_missing_gate_status_file_names_the_fix(self):
        result = run(
            config_with([DECLARED_CHAIN[0]]), write_gate_status=False
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gate_status.json", result.stderr)

    def test_declared_stage_without_observed_entry_fails(self):
        result = run(config_with(DECLARED_CHAIN), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ica", result.stderr)

    def test_observed_entry_without_declared_stage_fails(self):
        extra = OBSERVED_CHAIN + [observed("ghost", "2026-08-19T13:00:00+00:00")]
        result = run(config_with(DECLARED_CHAIN), extra)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ghost", result.stderr)


class TestChainShape(unittest.TestCase):
    def test_duplicate_position_fails(self):
        broken = [declared(0, "filter", None), declared(0, "ica", "filter")]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)

    def test_gap_in_positions_fails(self):
        broken = [declared(0, "filter", None), declared(2, "ica", "filter")]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)

    def test_consumes_unknown_stage_fails(self):
        broken = [declared(0, "filter", None), declared(1, "ica", "nonexistent")]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nonexistent", result.stderr)

    def test_first_stage_with_consumes_fails(self):
        broken = [declared(0, "filter", "ghost")]
        result = run(config_with(broken), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)

    def test_later_stage_without_consumes_fails(self):
        broken = [declared(0, "filter", None), declared(1, "ica", None)]
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)

    def test_cycle_fails(self):
        broken = [
            declared(0, "filter", None),
            declared(1, "ica", "epoch"),
            declared(2, "epoch", "ica"),
        ]
        result = run(config_with(broken), OBSERVED_CHAIN)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cycle", result.stderr.lower())


class TestCascade(unittest.TestCase):
    def test_downstream_validated_before_upstream_is_stale(self):
        broken = [
            observed("filter", "2026-08-19T14:00:00+00:00"),
            observed("ica", "2026-08-19T11:00:00+00:00", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("STALE", result.stderr)

    def test_pass_downstream_of_pending_fails(self):
        broken = [
            observed("filter", "2026-08-19T10:00:00+00:00", status="PENDING"),
            observed("ica", "2026-08-19T11:00:00+00:00", status="PASS", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("PENDING", result.stderr)

    def test_pending_downstream_of_pass_is_allowed(self):
        ok = [
            observed("filter", "2026-08-19T10:00:00+00:00", status="PASS"),
            observed("ica", "2026-08-19T11:00:00+00:00", status="PENDING", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), ok)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("INCOMPLETE", result.stdout)


class TestFamily(unittest.TestCase):
    def test_missing_family_key_fails(self):
        config = config_with([])
        del config["family"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("family", result.stderr)

    def test_parent_without_family_id_fails(self):
        config = config_with([])
        config["family"] = {
            "family_id": None,
            "parent_analysis": "F007",
            "varies": ["threshold"],
        }
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("family_id", result.stderr)

    def test_wellformed_family_passes(self):
        config = config_with([])
        config["family"] = {
            "family_id": "memory_performance",
            "parent_analysis": "F007",
            "varies": ["exclusion_threshold", "tmax"],
        }
        result = run(config)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
