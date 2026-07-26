#!/usr/bin/env python3
"""Write a SHA-256 manifest for a scientific analysis result folder."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Analysis root or results folder")
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--analysis-id", default="")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output or root / "result_manifest.json"
    output = output.resolve()
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.resolve() == output:
            continue
        files.append(
            {
                "path": str(path.relative_to(root)),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    manifest = {
        "schema": "scientific-analysis-result-manifest-v1",
        "analysis_id": args.analysis_id or root.name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "files": files,
    }
    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="ascii")
    print(f"wrote {output} with {len(files)} files")


if __name__ == "__main__":
    main()
