---
type: repo-card
id: tesa
title: TESA
source_url: https://github.com/nigelrogasch/TESA
context7: preferred
github_fallback: https://github.com/nigelrogasch/TESA
tags:
  - repo:tesa
  - ecosystem:matlab
  - ecosystem:eeglab
  - pipeline:tesa-inspired
---

## Role In The Skill

Canonical MATLAB/EEGLAB reference for TMS-EEG preprocessing and TEP analysis logic.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

Conceptual workflow ordering, artifact categories, TMS-specific cleaning rationale, and TEP/GMFA analysis ideas.

## Workflow Concepts

Pulse handling, artifact cleaning, ICA/component review, TEP analysis, and careful QC.

## Important Assumptions

TESA is MATLAB/EEGLAB-based. Python answers should be described as TESA-inspired unless using a verified Python implementation.

## Useful Source Areas To Inspect

README, tutorial scripts, function docs, examples, and artifact-removal routines.

## Failure Modes

Translating MATLAB routines into Python without verifying equivalent behavior; treating TESA-style order as universal.

## Related Cards

`pipelines/tesa-inspired-two-pass-ica.md`; `steps/ica-component-rejection.md`.
