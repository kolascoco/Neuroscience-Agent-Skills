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

ALLOWED_TIERS = {"Required", "Shadow", "Diagnostic", "Fallback"}

DECLARED_KEYS = {
    "stage",
    "position",
    "consumes",
    "name",
    "version",
    "install_source",
    "parameters",
    "tier",
}

# Always required on every observed entry, regardless of status.
OBSERVED_KEYS_ALWAYS = {"stage", "status", "input_ref"}

# Required (and non-null) only once a stage has actually run. A PENDING
# stage describes a run that has not happened yet, so these three may be
# omitted or null: inventing a validated_at/runtime_s/output_shape for a
# run that never occurred is exactly the failure this schema exists to
# prevent (C1).
OBSERVED_KEYS_RUN = {"validated_at", "runtime_s", "output_shape"}

OBSERVED_KEYS = OBSERVED_KEYS_ALWAYS | OBSERVED_KEYS_RUN


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_time(value: str, label: str) -> datetime:
    # datetime.fromisoformat only accepts a trailing "Z" on Python 3.11+;
    # normalize it to an explicit offset so the same input parses the same
    # way on every supported interpreter version.
    normalized = value
    if isinstance(value, str) and value.endswith("Z"):
        normalized = value[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except (TypeError, ValueError):
        raise SystemExit(f"{label} validated_at is not ISO-8601: {value!r}")
    if parsed.tzinfo is None:
        raise SystemExit(
            f"{label} validated_at must include a UTC offset (e.g. +00:00), "
            f"got {value!r}"
        )
    return parsed


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
        stage_value = record["stage"]
        if not isinstance(stage_value, str):
            raise SystemExit(
                f"{label} stage must be a string, got {stage_value!r}"
            )
        if stage_value in by_stage:
            raise SystemExit(f"{kind} has duplicate stage name: {stage_value}")
        by_stage[stage_value] = record
    return by_stage


def check_observed_entries(records, kind="instrument_status"):
    """Type-check the observed array and index it by stage name.

    Unlike `check_entries`, the required-keys check here is conditional on
    `status`: a PENDING entry describes a stage that has not run, so
    `validated_at`, `runtime_s`, and `output_shape` may be omitted or null.
    Any other status requires all three, present and non-null (C1).
    """
    if not isinstance(records, list):
        raise SystemExit(f"{kind} must be a list")
    by_stage = {}
    for index, record in enumerate(records):
        label = f"{kind}[{index}]"
        if not isinstance(record, dict):
            raise SystemExit(f"{label} must be an object")
        missing = sorted(OBSERVED_KEYS_ALWAYS - set(record))
        if missing:
            raise SystemExit(f"{label} missing keys: {', '.join(missing)}")
        stage_value = record["stage"]
        if not isinstance(stage_value, str):
            raise SystemExit(
                f"{label} stage must be a string, got {stage_value!r}"
            )
        if stage_value in by_stage:
            raise SystemExit(f"{kind} has duplicate stage name: {stage_value}")
        status_value = record["status"]
        if status_value != "PENDING":
            unset = sorted(
                key
                for key in OBSERVED_KEYS_RUN
                if record.get(key) is None
            )
            if unset:
                raise SystemExit(
                    f"{label} status is {status_value!r}, which requires "
                    f"non-null {', '.join(unset)} (a stage that has run "
                    "carries all three; PENDING may omit or null them)"
                )
        by_stage[stage_value] = record
    return by_stage


def validate_instruments(declared: object, observed: object) -> None:
    """Validate the declared chain and its observed status. Raises SystemExit."""
    declared_by_stage = check_entries(declared, DECLARED_KEYS, "instruments")
    observed_by_stage = check_observed_entries(observed, "instrument_status")

    if not declared_by_stage:
        if observed_by_stage:
            raise SystemExit(
                "instrument_status records stages that config.json does not "
                f"declare: {', '.join(sorted(observed_by_stage))}"
            )
        return

    unobserved = sorted(set(declared_by_stage) - set(observed_by_stage))
    undeclared = sorted(set(observed_by_stage) - set(declared_by_stage))
    if unobserved or undeclared:
        parts = []
        if unobserved:
            parts.append(
                "declared stages have no instrument_status entry in "
                f"gate_status.json: {', '.join(unobserved)}"
            )
        if undeclared:
            parts.append(
                "instrument_status records stages that config.json does not "
                f"declare: {', '.join(undeclared)}"
            )
        raise SystemExit("; ".join(parts))

    for stage_name, record in observed_by_stage.items():
        if record["status"] not in ALLOWED_STATUS:
            raise SystemExit(
                f"instrument_status[{stage_name}] status must be one of "
                f"{sorted(ALLOWED_STATUS)}, got {record['status']!r}"
            )
        # A PENDING stage may carry a null validated_at (no run has
        # happened yet); check_observed_entries already guaranteed every
        # other status has a non-null value here, so only parse when one
        # is actually present.
        validated_at = record.get("validated_at")
        if validated_at is not None:
            parse_time(validated_at, f"instrument_status[{stage_name}]")

    for record in declared:
        position = record["position"]
        if isinstance(position, bool) or not isinstance(position, int):
            raise SystemExit(
                f"stage {record['stage']!r} position must be an integer, "
                f"got {position!r}"
            )
        tier = record["tier"]
        if tier not in ALLOWED_TIERS:
            raise SystemExit(
                f"stage {record['stage']!r} tier must be one of "
                f"{sorted(ALLOWED_TIERS)}, got {tier!r}"
            )

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
        if declared_by_stage[upstream_name]["position"] != record["position"] - 1:
            raise SystemExit(
                f"stage {record['stage']} consumes {upstream_name} at position "
                f"{declared_by_stage[upstream_name]['position']}, but the chain "
                f"is linear: consumes must name the immediate predecessor at "
                f"position {record['position'] - 1}"
            )

    for record in ordered:
        upstream_name = record["consumes"]
        if upstream_name is None:
            continue
        own = observed_by_stage[record["stage"]]
        up = observed_by_stage[upstream_name]
        own_validated_at = own.get("validated_at")
        up_validated_at = up.get("validated_at")
        # A PENDING stage (own or upstream) may have no validated_at at
        # all: it describes a run that has not happened, so it is
        # excluded from the staleness comparison rather than crashing it
        # (C1). The PASS-requires-upstream-PASS check below still applies
        # unconditionally: it needs only the two statuses, not a time.
        if own_validated_at is not None and up_validated_at is not None:
            if parse_time(own_validated_at, record["stage"]) < parse_time(
                up_validated_at, upstream_name
            ):
                raise SystemExit(
                    f"stage {record['stage']} is STALE: validated at "
                    f"{own_validated_at} but upstream {upstream_name} was "
                    f"validated later at {up_validated_at}"
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

    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{args.config} is not valid JSON: {exc}")

    missing = sorted(REQUIRED_TOP_LEVEL - set(config))
    if missing:
        remedies = []
        if "instruments" in missing:
            remedies.append(
                'add "instruments": [] to config.json and create '
                'gate_status.json containing {"instrument_status": []}'
            )
        if "family" in missing:
            remedies.append(
                'add "family": {"family_id": null, "parent_analysis": null, '
                '"varies": []} to config.json'
            )
        detail = f"; {'; '.join(remedies)}" if remedies else ""
        raise SystemExit(
            f"missing required config keys: {', '.join(missing)}{detail}"
        )
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
        try:
            gate_status = json.loads(gate_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{gate_path} is not valid JSON: {exc}")
        if not isinstance(gate_status, dict):
            raise SystemExit(
                f"{gate_path} must contain a JSON object at the top level, "
                f"got {type(gate_status).__name__}"
            )
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

    # I5: the leading word reports what this script actually checked — the
    # config's schema and chain arithmetic — never the scientific validity
    # of the chain itself. A reader (or an Adversary) grepping for "PASS"
    # must not mistake schema validity for a passing instrument chain: a
    # FAILED chain and a schema-valid config both exit 0, so the chain
    # state is spelled out, unmistakably, in the same line.
    if declared:
        states = {record["status"] for record in observed}
        if states == {"PASS"}:
            chain = "PASS"
        elif "FAIL" in states:
            chain = "FAILED"
        elif "STALE" in states:
            chain = "STALE"
        elif states == {"PENDING"}:
            # A freshly frozen chain that has not run yet is the expected,
            # common state (C1) — distinct from INCOMPLETE, which covers a
            # chain partway through validation.
            chain = "PENDING"
        else:
            chain = "INCOMPLETE"
        print(
            f"CONFIG VALID -- instrument chain: {chain} "
            f"({len(declared)} stages)"
        )
    else:
        print("CONFIG VALID -- no instruments recorded")


if __name__ == "__main__":
    main()
