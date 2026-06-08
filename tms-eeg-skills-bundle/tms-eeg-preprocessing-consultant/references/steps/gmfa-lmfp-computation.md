---
type: step-card
id: gmfa-lmfp-computation
title: GMFA And LMFP Computation
tags:
  - metric:gmfa
  - metric:lmfp
applies_to:
  - conservative-mne-python
  - sound-ssp-sir-enhanced
load_with:
  - steps/tep-averaging.md
---

## Purpose

Summarize global or local field power across channels/ROIs after preprocessing.

## When To Apply

After cleaned evoked responses are computed.

## Inputs Needed

Evoked data, full-channel reference mode, channel picks, ROI channel list for LMFP, time windows, and condition labels.

## Decision Rules

GMFA is global scalp dispersion, not target-specific excitability. LMFP depends strongly on ROI/channel definition and reference choice.

Apply the chosen EEG reference before feature calculation and before selecting ROI channels. Usually use common average reference (CAR) or a justified surface Laplacian/CSD transform. Never apply CAR after picking only the LMFP ROI, because close ROI channels will reference against each other and can artificially reduce the local field estimate.

## Method Options

Compute standard deviation across selected channels over time; compute LMFP over predefined ROI channels after full-channel re-referencing.

## Learning Mode Explanation

GMFA/LMFP reduce complex TEPs to time courses, useful for comparison but not mechanistically specific by themselves. Re-referencing changes the spatial distribution used for these metrics, so it is part of the feature definition rather than a cosmetic preprocessing step.

## Code-Engineer Notes

Use `recipes/compute_teps_gmfa_lmfp.md`; label reference mode, channels, ROI, and windows clearly.

## QC Checks

Plot TEPs with GMFA/LMFP, verify channel picks, compare active/sham, report time windows, and check sensitivity to reference choice when conclusions depend on LMFP.

## Failure Modes

Including bad/non-EEG channels, changing ROI after seeing results, applying CAR only within the ROI, unreported reference changes, and direct excitability claims.

## Sources

Conservative MNE pipeline card; interpretation caveat from MVP architecture.
