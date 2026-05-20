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

Evoked data, channel picks, ROI channel list for LMFP, time windows, and condition labels.

## Decision Rules

GMFA is global scalp dispersion, not target-specific excitability. LMFP depends strongly on ROI/channel definition.

## Method Options

Compute standard deviation across selected channels over time; compute LMFP over predefined ROI channels.

## Learning Mode Explanation

GMFA/LMFP reduce complex TEPs to time courses, useful for comparison but not mechanistically specific by themselves.

## Code-Engineer Notes

Use `recipes/compute_teps_gmfa_lmfp.md`; label channels and windows clearly.

## QC Checks

Plot TEPs with GMFA/LMFP, verify channel picks, compare active/sham, and report time windows.

## Failure Modes

Including bad/non-EEG channels, changing ROI after seeing results, and direct excitability claims.

## Sources

Conservative MNE pipeline card; interpretation caveat from MVP architecture.
