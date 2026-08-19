#!/usr/bin/env python3
"""Validate a generic frozen scientific analysis config."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "analysis_id",
    "status",
    "sources",
    "frozen_decisions",
    "compute_gates",
    "required_outputs",
    "interpretation",
    "instruments",
    "family",
}

ALLOWED_STATUS = {"PASS", "PENDING", "FAIL", "STALE"}

DECLARED_KEYS = {
    "stage",
    "position",
    "consumes",
    "name",
    "version",
    "install_source",
    "parameters",
}

OBSERVED_KEYS = {
    "stage",
    "status",
    "validated_at",
    "runtime_s",
    "output_shape",
    "input_ref",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_time(value: str, label: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError):
        raise SystemExit(f"{label} validated_at is not ISO-8601: {value!r}")


def check_entries(records, required, kind):
    """Type-check one array and index it by stage name."""
    if not isinstance(records, list):
        raise SystemExit(f"{kind} must be a list")
    by_stage = {}
    for index, record in enumerate(records):
        label = f"{kind}[{index}]"
        if not isinstance(record, dict):
            raise SystemExit(f"{label} must be an object")
        missing = sorted(required - set(record))
        if missing:
            raise SystemExit(f"{label} missing keys: {', '.join(missing)}")
        if record["stage"] in by_stage:
            raise SystemExit(f"{kind} has duplicate stage name: {record['stage']}")
        by_stage[record["stage"]] = record
    return by_stage


def validate_instruments(declared: object, observed: object) -> None:
    """Validate the declared chain and its observed status. Raises SystemExit."""
    declared_by_stage = check_entries(declared, DECLARED_KEYS, "instruments")
    observed_by_stage = check_entries(
        observed, OBSERVED_KEYS, "instrument_status"
    )

    if not declared_by_stage:
        if observed_by_stage:
            raise SystemExit(
                "instrument_status records stages that config.json does not "
                f"declare: {', '.join(sorted(observed_by_stage))}"
            )
        return

    unobserved = sorted(set(declared_by_stage) - set(observed_by_stage))
    if unobserved:
        raise SystemExit(
            "declared stages have no instrument_status entry in "
            f"gate_status.json: {', '.join(unobserved)}"
        )
    undeclared = sorted(set(observed_by_stage) - set(declared_by_stage))
    if undeclared:
        raise SystemExit(
            "instrument_status records stages that config.json does not "
            f"declare: {', '.join(undeclared)}"
        )

    for stage_name, record in observed_by_stage.items():
        if record["status"] not in ALLOWED_STATUS:
            raise SystemExit(
                f"instrument_status[{stage_name}] status must be one of "
                f"{sorted(ALLOWED_STATUS)}, got {record['status']!r}"
            )
        parse_time(record["validated_at"], f"instrument_status[{stage_name}]")

    positions = sorted(record["position"] for record in declared)
    if positions != list(range(len(declared))):
        raise SystemExit(
            f"instrument position values must be contiguous from 0, got {positions}"
        )

    ordered = sorted(declared, key=lambda record: record["position"])
    for record in ordered:
        upstream_name = record["consumes"]
        if record["position"] == 0:
            if upstream_name is not None:
                raise SystemExit(
                    f"first stage {record['stage']} must have consumes: null"
                )
            continue
        if upstream_name is None:
            raise SystemExit(
                f"stage {record['stage']} must name an upstream stage in consumes"
            )
        if upstream_name not in declared_by_stage:
            raise SystemExit(
                f"stage {record['stage']} consumes unknown stage: {upstream_name}"
            )
        if declared_by_stage[upstream_name]["position"] >= record["position"]:
            raise SystemExit(
                f"cycle: stage {record['stage']} consumes {upstream_name}, "
                "which is not upstream of it"
            )

    for record in ordered:
        upstream_name = record["consumes"]
        if upstream_name is None:
            continue
        own = observed_by_stage[record["stage"]]
        up = observed_by_stage[upstream_name]
        if parse_time(own["validated_at"], record["stage"]) < parse_time(
            up["validated_at"], upstream_name
        ):
            raise SystemExit(
                f"stage {record['stage']} is STALE: validated at "
                f"{own['validated_at']} but upstream {upstream_name} was "
                f"validated later at {up['validated_at']}"
            )
        if own["status"] == "PASS" and up["status"] != "PASS":
            raise SystemExit(
                f"stage {record['stage']} cannot be PASS while upstream "
                f"{upstream_name} is {up['status']}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--check-files", action="store_true")
    parser.add_argument("--gate-status", type=Path, default=None)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_TOP_LEVEL - set(config))
    if missing:
        raise SystemExit(f"missing required config keys: {', '.join(missing)}")
    if not isinstance(config["sources"], list):
        raise SystemExit("sources must be a list")
    if not isinstance(config["frozen_decisions"], dict):
        raise SystemExit("frozen_decisions must be an object")
    if not isinstance(config["required_outputs"], list):
        raise SystemExit("required_outputs must be a list")

    declared = config["instruments"]
    gate_path = args.gate_status or args.config.parent / "gate_status.json"
    if not isinstance(declared, list):
        raise SystemExit("instruments must be a list")
    if declared and not gate_path.is_file():
        raise SystemExit(
            f"gate_status.json not found at {gate_path}; create it containing "
            '{"instrument_status": []} and record one entry per declared stage'
        )
    if gate_path.is_file():
        gate_status = json.loads(gate_path.read_text(encoding="utf-8"))
        observed = gate_status.get("instrument_status", [])
    else:
        observed = []
    validate_instruments(declared, observed)

    family = config["family"]
    if not isinstance(family, dict):
        raise SystemExit("family must be an object")
    missing = sorted({"family_id", "parent_analysis", "varies"} - set(family))
    if missing:
        raise SystemExit(f"family missing keys: {', '.join(missing)}")
    if not isinstance(family["varies"], list):
        raise SystemExit("family.varies must be a list")
    if family["parent_analysis"] and not family["family_id"]:
        raise SystemExit(
            "family.parent_analysis is set without family_id; a variant shares "
            "its parent's family_id"
        )

    if args.check_files:
        base = args.config.parent
        for index, record in enumerate(config["sources"]):
            if not isinstance(record, dict) or "path" not in record:
                raise SystemExit(f"sources[{index}] must contain path")
            path = Path(record["path"])
            if not path.is_absolute():
                path = base / path
            if not path.is_file():
                raise SystemExit(f"source missing: {path}")
            expected = record.get("sha256")
            if expected and sha256(path) != expected:
                raise SystemExit(f"source hash mismatch: {path}")

    if declared:
        states = {record["status"] for record in observed}
        chain = "PASS" if states == {"PASS"} else "INCOMPLETE"
        print(f"PASS (instrument chain: {chain}, {len(declared)} stages)")
    else:
        print("PASS (no instruments recorded)")


if __name__ == "__main__":
    main()
