---
type: repo-card
id: tmseegpy
title: tmseegpy
source_url: https://github.com/LazyCyborg/tmseegpy
context7: preferred
github_fallback: https://github.com/LazyCyborg/tmseegpy
tags:
  - repo:tmseegpy
  - ecosystem:python
  - pipeline:mne
  - pipeline:tesa-inspired
---

## Role In The Skill

Python-oriented TMS-EEG preprocessing reference, useful for TESA-like concepts in a Python/MNE-adjacent workflow.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

Workflow ideas for TMS artifact handling, ICA-oriented cleaning, muscle/noise attenuation, TEP metrics, and possibly PCIst-adjacent functionality after verification.

## Workflow Concepts

Use as a bridge between TMS-specific preprocessing logic and Python code generation.

## Important Assumptions

Verify current package state and APIs before writing runnable code.

## Useful Source Areas To Inspect

README, examples, preprocessing modules, artifact routines, metric utilities, and tests if present.

## Failure Modes

Assuming feature parity with TESA, relying on stale function names, and using toolbox defaults without dataset-specific QC.

## Related Cards

`pipelines/conservative-mne-python.md`; `pipelines/tesa-inspired-two-pass-ica.md`.
