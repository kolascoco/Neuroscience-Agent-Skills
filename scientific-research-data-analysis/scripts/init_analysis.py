#!/usr/bin/env python3
"""Create a minimal scientific analysis scaffold."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("analysis_id", help="Analysis id, for example H-2026-032")
    parser.add_argument("--root", type=Path, default=Path("analyses"))
    parser.add_argument("--title", default="")
    args = parser.parse_args()

    root = args.root / args.analysis_id
    for name in ("code", "results", "tests", "audits"):
        (root / name).mkdir(parents=True, exist_ok=True)

    title = args.title or args.analysis_id
    plan = root / "plan.md"
    if not plan.exists():
        plan.write_text(
            "\n".join(
                [
                    f"# {title} Frozen Plan",
                    "",
                    "## Purpose",
                    "",
                    "## Frozen Decisions",
                    "",
                    "## Data Contract",
                    "",
                    "## Statistical Plan",
                    "",
                    "## Controls",
                    "",
                    "## Outputs",
                    "",
                    "## Interpretation Limits",
                    "",
                ]
            ),
            encoding="ascii",
        )

    config = root / "config.json"
    if not config.exists():
        config.write_text(
            json.dumps(
                {
                    "analysis_id": args.analysis_id,
                    "created_utc": datetime.now(timezone.utc).isoformat(),
                    "status": "draft",
                    "sources": [],
                    "frozen_decisions": {},
                    "compute_gates": {},
                    "required_outputs": [],
                    "interpretation": "unfrozen",
                },
                indent=2,
            )
            + "\n",
            encoding="ascii",
        )

    log = root / "log.md"
    if not log.exists():
        log.write_text(f"# {args.analysis_id} Execution Log\n\n", encoding="ascii")

    print(root)


if __name__ == "__main__":
    main()
