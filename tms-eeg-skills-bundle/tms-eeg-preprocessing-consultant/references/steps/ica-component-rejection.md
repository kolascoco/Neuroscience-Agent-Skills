---
type: step-card
id: ica-component-rejection
title: ICA Component Rejection
tags:
  - step:ica
  - caution:overcleaning
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
load_with:
  - artifacts/overcleaning-and-ica-risk.md
---

## Purpose

Remove stereotyped artifacts such as ocular, muscle, auditory/sensory-related, and residual TMS components while preserving neural signal.

## When To Apply

After gross pulse handling, bad-channel/bad-trial inspection, and enough preprocessing to make the decomposition stable. TESA-style workflows may use two ICA passes.

Do not treat broad analysis filtering as a prerequisite for ICA. If filtering is needed only to improve ICA stability, use a separate ICA-training copy or a clearly documented detrending/high-pass strategy, then apply the learned component rejection to the intended analysis data when supported by the software workflow.

## Inputs Needed

Sufficient trials, channel count, ICA-training data policy, filtering/detrending policy, component plots, and rejection criteria.

## Decision Rules

Do not reject components by label alone. Require topography, time course, spectrum, and condition-aware QC.

## Method Options

Manual ICA review, automated component suggestions plus human verification, two-pass ICA, or alternative cleaning when ICA is unstable.

## Learning Mode Explanation

ICA can help separate artifacts, but it can also remove real evoked activity if used carelessly.

## Code-Engineer Notes

Use `recipes/run_ica_with_qc.md`; verify MNE or TESA/tmseegpy APIs.

## QC Checks

Component maps, explained variance, before/after TEPs, retained components, and active/sham differences.

## Failure Modes

Too few data points, rank issues, overcleaning, residual artifacts, irreproducible manual decisions, and letting early ICA-preparation filters distort the final TEP waveform.

## Sources

TESA repo card; overcleaning artifact card.
