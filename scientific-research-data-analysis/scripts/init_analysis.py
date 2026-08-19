#!/usr/bin/env python3
"""Create a minimal scientific analysis scaffold."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "analysis_id",
        help="Analysis id, for example F031_theta_load_contrast",
    )
    parser.add_argument("--root", type=Path, default=Path("analyses"))
    parser.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Defaults to --root's parent directory",
    )
    parser.add_argument("--title", default="")
    args = parser.parse_args()
    project_root = args.project_root if args.project_root is not None else args.root.parent

    root = args.root / args.analysis_id
    if root.exists():
        raise SystemExit(f"analysis id already exists: {root}")
    prefix = args.analysis_id.split("_")[0]
    clashes = sorted(
        sibling.name
        for sibling in args.root.glob(f"{prefix}_*")
        if sibling.is_dir()
    )
    if clashes:
        raise SystemExit(
            f"analysis id prefix {prefix!r} is already taken by: "
            f"{', '.join(clashes)}; a variant takes its own id and records "
            "parent_analysis in config.json"
        )
    # root does not exist (checked above), so none of the files below can
    # already exist either; the mkdir/write calls need no exist_ok or
    # if-not-exists guards.
    for name in ("code", "results", "tests"):
        (root / name).mkdir(parents=True)

    title = args.title or args.analysis_id
    plan = root / "plan.md"
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
                "instruments": [],
                "family": {
                    "family_id": None,
                    "parent_analysis": None,
                    "varies": [],
                },
                "interpretation": "unfrozen",
            },
            indent=2,
        )
        + "\n",
        encoding="ascii",
    )

    gate_status = root / "gate_status.json"
    gate_status.write_text(
        json.dumps({"gates": {}, "instrument_status": []}, indent=2) + "\n",
        encoding="ascii",
    )

    log = root / "log.md"
    log.write_text(f"# {args.analysis_id} Execution Log\n\n", encoding="ascii")

    # ideas.md lives at the project root, not inside this analysis folder, so
    # it legitimately survives across many init_analysis.py runs — keep the
    # existence guard so a later analysis does not clobber earlier entries.
    ideas = project_root / "ideas.md"
    if not ideas.exists():
        ideas.write_text(
            "\n".join(
                [
                    "# Project Ideas",
                    "",
                    "Ranked candidate directions not in any current plan.",
                    "Written while discussing results, during analysis, at data",
                    "audit, and at theory update. Read when an analysis stalls,",
                    "when a method is dropped, and at every theory update.",
                    "",
                    "Status: open | in progress | done (<analysis-id>) |",
                    "dropped (<reason>). An idea is never silently deleted.",
                    "",
                    "| Rank | Idea | Rationale | Rough cost | Status |",
                    "|---|---|---|---|---|",
                    "",
                ]
            ),
            encoding="ascii",
        )

    print(root)


if __name__ == "__main__":
    main()
