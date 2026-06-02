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

Canonical MATLAB/EEGLAB reference for TMS-EEG preprocessing and TEP analysis logic. TESA is the preferred MATLAB target when users ask for EEGLAB `.set` workflows, `pop_tesa_*` functions, FastICA, TMS pulse interpolation, SOUND, SSP-SIR, or TEP peak/ROI analysis.

## Software Lookup Policy

1. If Context7 is available, resolve/query `/nigelrogasch/tesa` for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

Conceptual workflow ordering, artifact categories, TMS-specific cleaning rationale, and TEP/GMFA analysis ideas. For MATLAB code, reuse verified TESA function families rather than generic pseudocode.

## Workflow Concepts

Core workflow concepts:

- pulse detection/fixing when needed: `tesa_findpulse`, `tesa_fixevent`
- pulse artifact blanking/interpolation: `tesa_removedata` / `pop_tesa_removedata`, `tesa_interpdata` / `pop_tesa_interpdata`
- dimensionality and ICA: `tesa_pcacompress` / `pop_tesa_pcacompress`, `tesa_fastica` / `pop_tesa_fastica`, `tesa_compplot` / `pop_tesa_compplot`, `tesa_compselect`
- filtering: `tesa_filtbutter` or project/EEGLAB filter helpers after pulse handling
- model/source-based cleaning: `tesa_sound` / `pop_tesa_sound`, `tesa_sspsir` / `pop_tesa_sspsir`
- TEP analysis: `tesa_tepextract`, `tesa_peakanalysis`, `tesa_peakoutput`, `pop_tesa_plot`

## Important Assumptions

TESA is MATLAB/EEGLAB-based and requires EEGLAB. The repository README describes TESA as an EEGLAB extension for cleaning and analysing TMS-EEG data in MATLAB. Python answers should be described as TESA-inspired unless using a verified Python implementation.

The local Science Factory lesson script uses MATLAB R2024b, EEGLAB 2024.1, TESA 1.1.1, and FastICA; those are teaching-script facts, not universal requirements.

## Useful Source Areas To Inspect

README, release page, `pop_tesa_*` wrappers, non-`pop_` TESA functions, `pipeline_repository`, `pop_tesa_removedata.m`, `pop_tesa_interpdata.m`, `pop_tesa_fastica.m`, `pop_tesa_sound.m`, `pop_tesa_sspsir.m`, and TEP extraction/peak-analysis functions.

## Failure Modes

Translating MATLAB routines into Python without verifying equivalent behavior; treating TESA-style order as universal; applying high-pass filters to short epochs; using project-specific helper functions as if they were TESA functions; failing to compare cleaned data against minimally preprocessed data.

## Related Cards

`pipelines/tesa-inspired-two-pass-ica.md`; `recipes/tesa_matlab_preprocessing.md`; `guidelines/matlab-tesa-lesson-pipeline.md`; `steps/ica-component-rejection.md`.
