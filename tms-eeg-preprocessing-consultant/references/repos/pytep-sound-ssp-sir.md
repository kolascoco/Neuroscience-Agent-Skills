---
type: repo-card
id: pytep-sound-ssp-sir
title: PyTEP-SOUND-SSP-SIR
source_url: https://github.com/MarcioCamposJr/PyTEP-SOUND-SSP-SIR
context7: preferred
github_fallback: https://github.com/MarcioCamposJr/PyTEP-SOUND-SSP-SIR
tags:
  - repo:pytep-sound-ssp-sir
  - ecosystem:python
  - pipeline:sound-ssp-sir
---

## Role In The Skill

Reference implementation/source for TMS-EEG workflows using SOUND and SSP-SIR style cleaning.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

Method ordering, assumptions around SOUND/SSP-SIR, QC expectations, and code structure after API verification.

## Workflow Concepts

Model/projection-based cleaning can complement or substitute parts of ICA-heavy workflows when assumptions are satisfied.

## Important Assumptions

Geometry, rank, and projection assumptions must be explicit.

## Useful Source Areas To Inspect

README, notebooks/scripts, SOUND implementation, SSP-SIR implementation, parameter examples.

## Failure Modes

Using model-based cleaning without required geometry; rank loss; treating projection outputs as artifact-free.

## Related Cards

`pipelines/sound-ssp-sir-enhanced.md`; `steps/sound-cleaning.md`; `steps/ssp-sir-cleaning.md`.
