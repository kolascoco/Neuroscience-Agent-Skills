#!/usr/bin/env python3
"""Validate a generic frozen scientific analysis config."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "analysis_id",
    "status",
    "sources",
    "frozen_decisions",
    "compute_gates",
    "required_outputs",
    "interpretation",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path)
    parser.add_argument("--check-files", action="store_true")
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

    print("PASS")


if __name__ == "__main__":
    main()
