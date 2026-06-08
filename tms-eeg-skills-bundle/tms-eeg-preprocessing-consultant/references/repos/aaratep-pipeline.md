---
type: repo-card
id: aaratep-pipeline
title: AARATEP Pipeline
source_url: https://github.com/chriscline/AARATEPPipeline
context7: preferred
github_fallback: https://github.com/chriscline/AARATEPPipeline
tags:
  - repo:aaratep
  - ecosystem:matlab
  - ecosystem:eeglab
  - pipeline:artist-aaratep
---

## Role In The Skill

Reference repository for automated TMS-EEG preprocessing using advanced artifact removal and staged EEGLAB/TESA-compatible processing.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

The staged automated workflow: epoching, artifact interpolation, downsampling, baseline correction, high-pass filtering, bad-channel identification, early eye-related IC rejection, SOUND, decay component removal, further interpolation, line-noise filtering, ICA, ICLabel plus TMS-specific component rules, low-pass filtering, and average rereferencing.

This order is a repo-specific implementation cue. Do not generalize the early/mid high-pass position into ordinary advisor code unless the user asks to reproduce AARATEP. General TMS-EEG advice should prefer late analysis filtering after pulse and major artifact handling.

## Workflow Concepts

Automation can make TMS-EEG preprocessing more reproducible, but the resulting decisions must be logged and reviewed.

## Important Assumptions

The README states the code assumes EEGLAB plus ICLabel and TESA extensions. It is MATLAB-based and should not be described as Python/MNE code.

## Useful Source Areas To Inspect

README, `c_TMSEEG_Preprocess_AARATEPPipeline.m`, `Common/`, preparation helpers, and release notes.

## Failure Modes

Dependency mismatch, stale function signatures, unreviewed automated rejection, and applying pipeline defaults to incompatible protocols.

## Related Cards

`pipelines/automated-artist-aaratep.md`; `steps/automated-artifact-rejection.md`; `papers/cline-2021-aaratep.md`.
