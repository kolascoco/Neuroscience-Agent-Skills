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


def declared(position, name, consumes, tier="Required"):
    """One well-formed entry for config.json's instruments array."""
    return {
        "stage": name,
        "position": position,
        "consumes": consumes,
        "name": name,
        "version": "1.0.0",
        "install_source": "pypi",
        "parameters": {},
        "tier": tier,
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


def pending(name, consumes=None):
    """A freshly-frozen PENDING entry: no run has happened yet, so
    validated_at/runtime_s/output_shape are null rather than invented."""
    return {
        "stage": name,
        "status": "PENDING",
        "validated_at": None,
        "runtime_s": None,
        "output_shape": None,
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


def run_raw(config_path, extra_args=None):
    """Run the validator directly against an already-written config path."""
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(config_path), *(extra_args or [])],
        capture_output=True,
        text=True,
    )


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
        # C3/I1: pinned to the actual migration message, not just any
        # stderr containing the substring "instruments" (a bare KeyError
        # traceback from `config["instruments"]` would also match a looser
        # assertion, and stays green even if REQUIRED_TOP_LEVEL is mutated
        # to drop "instruments").
        config = config_with([])
        del config["instruments"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('add "instruments": []', result.stderr)
        self.assertIn("gate_status.json", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_empty_chain_passes(self):
        result = run(config_with([]))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_wellformed_chain_passes(self):
        result = run(config_with(DECLARED_CHAIN), OBSERVED_CHAIN)
        self.assertEqual(result.returncode, 0, result.stderr)
        # I5: the leading token is never bare "PASS" — it names what the
        # script actually checked, with the chain state spelled out
        # separately in the same line.
        self.assertIn("CONFIG VALID", result.stdout)
        self.assertIn("instrument chain: PASS", result.stdout)

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

    def test_duplicate_stage_name_in_declared_fails(self):
        # C2.1: two declared entries name the same stage. Positions are
        # distinct (0, 1) so this exercises the duplicate-stage check in
        # isolation from the duplicate-position check.
        broken = [
            declared(0, "filter", None),
            declared(1, "filter", "filter"),
        ]
        result = run(
            config_with(broken),
            [OBSERVED_CHAIN[0], observed("filter2", "2026-08-19T11:00:00+00:00")],
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate", result.stderr.lower())
        self.assertIn("filter", result.stderr)

    def test_instruments_not_list_fails(self):
        # C2.4
        config = config_with("not-a-list")
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("instruments", result.stderr)
        self.assertIn("list", result.stderr)

    def test_declared_missing_tier_fails(self):
        # I4: tier is mandatory ("Every instrument carries one tier,
        # recorded with it") but had nowhere to be recorded; it must now
        # be a required declared key like any other.
        broken = dict(DECLARED_CHAIN[0])
        del broken["tier"]
        result = run(config_with([broken]), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tier", result.stderr)

    def test_declared_invalid_tier_fails(self):
        broken = dict(DECLARED_CHAIN[0])
        broken["tier"] = "Primary"
        result = run(config_with([broken]), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("tier", result.stderr)
        self.assertIn("Primary", result.stderr)

    def test_declared_each_allowed_tier_passes(self):
        for tier in ("Required", "Shadow", "Diagnostic", "Fallback"):
            with self.subTest(tier=tier):
                entry = declared(0, "filter", None, tier=tier)
                result = run(config_with([entry]), [OBSERVED_CHAIN[0]])
                self.assertEqual(result.returncode, 0, result.stderr)


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

    def test_agreement_mismatch_reports_both_directions(self):
        # M2: a missing observed entry AND an extra observed entry in the
        # same run must both be reported, not just whichever direction the
        # code happens to check first.
        decl = [declared(0, "a", None), declared(1, "b", "a")]
        obs = [
            observed("a", "2026-08-19T09:00:00+00:00"),
            observed("zzz", "2026-08-19T09:00:00+00:00"),
        ]
        result = run(config_with(decl), obs)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("b", result.stderr)
        self.assertIn("zzz", result.stderr)

    def test_gate_status_override_is_honored(self):
        # C2.2: --gate-status pointed at a file in a different directory
        # from config.json must actually be read. If the flag is ignored
        # and the code always looks beside config.json, this fails because
        # no gate_status.json exists there.
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            config_dir = base / "cfgdir"
            config_dir.mkdir()
            other_dir = base / "otherdir"
            other_dir.mkdir()
            config_path = config_dir / "config.json"
            config_path.write_text(
                json.dumps(config_with([DECLARED_CHAIN[0]])), encoding="utf-8"
            )
            gate_path = other_dir / "custom_gate_status.json"
            gate_path.write_text(
                json.dumps({"instrument_status": [OBSERVED_CHAIN[0]]}),
                encoding="utf-8",
            )
            result = run_raw(config_path, ["--gate-status", str(gate_path)])
            self.assertEqual(result.returncode, 0, result.stderr)


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

    def test_fork_consumes_same_predecessor_fails(self):
        # I2: two stages consuming the same predecessor is not a linear
        # chain. This is the exact escape reported: c(2) consumes a(0),
        # bypassing b(1), and c's validated_at predates b's, but nothing
        # upstream of c (a) is actually stale relative to c.
        broken = [
            declared(0, "a", None),
            declared(1, "b", "a"),
            declared(2, "c", "a"),
        ]
        obs = [
            observed("a", "2026-08-19T09:00:00+00:00"),
            observed("b", "2026-08-19T20:00:00+00:00", consumes="a"),
            observed("c", "2026-08-19T11:00:00+00:00", consumes="a"),
        ]
        result = run(config_with(broken), obs)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)
        self.assertIn("c", result.stderr)

    def test_skip_a_position_fails(self):
        # I2: d(3) skips its immediate predecessor c(2) and instead names
        # b(1). The chain is required to be strictly linear: stage[i] must
        # consume stage[i-1].
        broken = [
            declared(0, "a", None),
            declared(1, "b", "a"),
            declared(2, "c", "b"),
            declared(3, "d", "b"),
        ]
        obs = [
            observed("a", "2026-08-19T09:00:00+00:00"),
            observed("b", "2026-08-19T10:00:00+00:00", consumes="a"),
            observed("c", "2026-08-19T11:00:00+00:00", consumes="b"),
            observed("d", "2026-08-19T12:00:00+00:00", consumes="b"),
        ]
        result = run(config_with(broken), obs)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("consumes", result.stderr)
        self.assertIn("d", result.stderr)

    def test_position_wrong_type_fails(self):
        # I3.a: a string position compared against an int position must not
        # raise a bare TypeError from sorted(); a mix of types is needed to
        # actually trigger the unguarded comparison.
        broken = [declared(0, "filter", None), dict(declared(1, "ica", "filter"))]
        broken[1]["position"] = "1"
        result = run(config_with(broken), OBSERVED_CHAIN[:2])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_position_bool_rejected(self):
        # M1: bool is a subclass of int, and [False, True] == [0, 1], so a
        # naive contiguity check silently accepts position: false/true.
        broken = [dict(declared(0, "filter", None))]
        broken[0]["position"] = False
        result = run(config_with(broken), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("position", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_non_hashable_stage_fails(self):
        # I3.b: a list used as a dict key raises TypeError: unhashable type
        # unless guarded.
        broken = [dict(declared(0, "filter", None))]
        broken[0]["stage"] = ["filter"]
        result = run(config_with(broken), [OBSERVED_CHAIN[0]])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stage", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


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

    def test_all_fail_chain_reports_failed_not_incomplete(self):
        # M8: an all-FAIL chain is not merely "not finished" — it failed.
        # I5: the line must not lead with "PASS" next to a failed chain —
        # a reader (or the Adversary) scanning for "PASS" must not read
        # this line as a passing chain.
        broken = [observed("filter", "2026-08-19T10:00:00+00:00", status="FAIL")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("CONFIG VALID", result.stdout)
        self.assertIn("FAILED", result.stdout)
        self.assertNotIn("INCOMPLETE", result.stdout)
        self.assertFalse(result.stdout.startswith("PASS"))


class TestPendingObservedState(unittest.TestCase):
    """C1: a PENDING entry describes a stage that has not run yet. The
    declared chain is frozen at config-freeze time (SKILL.md step 4), long
    before any stage runs (step 6), so a freshly-frozen all-PENDING chain
    is the single most common state of gate_status.json — it must be the
    easy, passing path, not a failure with no documented remedy."""

    def test_freshly_frozen_all_pending_chain_passes(self):
        obs = [pending("filter"), pending("ica", consumes="filter")]
        result = run(config_with(DECLARED_CHAIN[:2]), obs)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("CONFIG VALID", result.stdout)
        # I5: distinct, non-alarming wording for the legitimate PENDING
        # case, separate from a partially-worked-through INCOMPLETE chain.
        self.assertIn("instrument chain: PENDING", result.stdout)
        self.assertNotIn("INCOMPLETE", result.stdout)

    def test_pending_may_omit_run_keys_entirely(self):
        # "may omit or null" — omission, not just an explicit null, must
        # also be accepted for a PENDING entry.
        obs_entry = {
            "stage": "filter",
            "status": "PENDING",
            "input_ref": "sources[0]",
        }
        result = run(config_with([DECLARED_CHAIN[0]]), [obs_entry])
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_pass_entry_with_null_validated_at_fails(self):
        # Any status other than PENDING requires all three run keys,
        # present and non-null — inventing a validated_at for a run that
        # never happened is exactly the failure this schema prevents.
        broken = dict(observed("filter", "2026-08-19T10:00:00+00:00"))
        broken["validated_at"] = None
        result = run(config_with([DECLARED_CHAIN[0]]), [broken])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)
        self.assertIn("PASS", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_pending_excluded_from_staleness_comparison_not_crashed(self):
        # The upstream stage has genuinely run (PASS, real validated_at);
        # the downstream stage is still PENDING with no validated_at at
        # all. Comparing "is downstream stale relative to upstream" makes
        # no sense when downstream has no run to date — it must be
        # excluded from that comparison rather than crashing it.
        obs = [
            observed("filter", "2026-08-19T10:00:00+00:00", status="PASS"),
            pending("ica", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), obs)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("Traceback", result.stderr)


class TestValidatedAtDiscipline(unittest.TestCase):
    """C1: validated_at must carry a UTC offset; naive/date-only rejected
    with a named error instead of crashing the comparison downstream."""

    def test_naive_validated_at_rejected(self):
        broken = [observed("filter", "2026-08-19T10:00:00")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)
        self.assertIn("UTC offset", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_date_only_validated_at_rejected(self):
        broken = [observed("filter", "2026-08-19")]
        result = run(config_with([DECLARED_CHAIN[0]]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_mixed_naive_and_aware_validated_at_rejected_not_crashed(self):
        # This is the exact repro from C1: one aware timestamp, one naive.
        # Before the fix this raised TypeError: can't compare offset-naive
        # and offset-aware datetimes at the staleness comparison.
        broken = [
            observed("filter", "2026-08-19T10:00:00+00:00"),
            observed("ica", "2026-08-19T11:00:00", consumes="filter"),
        ]
        result = run(config_with(DECLARED_CHAIN[:2]), broken)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("validated_at", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_z_suffixed_validated_at_accepted(self):
        # "Z" is the most common UTC spelling, but datetime.fromisoformat
        # only accepts it directly on Python 3.11+. It must be normalized
        # so this input is accepted on every supported interpreter.
        accepted = [observed("filter", "2026-08-19T10:00:00Z")]
        result = run(config_with([DECLARED_CHAIN[0]]), accepted)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("Traceback", result.stderr)


class TestAdversarialInputs(unittest.TestCase):
    """I3: malformed/adversarial input produces a named diagnosis, not a
    raw traceback."""

    def test_gate_status_top_level_array_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            config_path = base / "config.json"
            config_path.write_text(
                json.dumps(config_with([DECLARED_CHAIN[0]])), encoding="utf-8"
            )
            (base / "gate_status.json").write_text(
                json.dumps([1, 2, 3]), encoding="utf-8"
            )
            result = run_raw(config_path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("gate_status.json", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_malformed_config_json_names_the_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            config_path = base / "config.json"
            config_path.write_text("{not valid json", encoding="utf-8")
            (base / "gate_status.json").write_text(
                json.dumps({"instrument_status": []}), encoding="utf-8"
            )
            result = run_raw(config_path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(str(config_path), result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_malformed_gate_status_json_names_the_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            config_path = base / "config.json"
            config_path.write_text(
                json.dumps(config_with([DECLARED_CHAIN[0]])), encoding="utf-8"
            )
            gate_path = base / "gate_status.json"
            gate_path.write_text("{not valid json", encoding="utf-8")
            result = run_raw(config_path)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(str(gate_path), result.stderr)
            self.assertNotIn("Traceback", result.stderr)


class TestFamily(unittest.TestCase):
    def test_missing_family_key_fails(self):
        # C3/I1: pinned to the migration message, not a bare substring that
        # a KeyError traceback would also satisfy.
        config = config_with([])
        del config["family"]
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('add "family"', result.stderr)
        self.assertNotIn("Traceback", result.stderr)

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

    def test_family_varies_not_list_fails(self):
        # C2.3
        config = config_with([])
        config["family"] = {
            "family_id": None,
            "parent_analysis": None,
            "varies": "not-a-list",
        }
        result = run(config)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("varies", result.stderr)


if __name__ == "__main__":
    unittest.main()
