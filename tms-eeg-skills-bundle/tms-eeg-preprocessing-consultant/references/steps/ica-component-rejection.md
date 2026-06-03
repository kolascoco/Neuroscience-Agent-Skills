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

After gross pulse handling and suitable filtering. TESA-style workflows may use two ICA passes.

## Inputs Needed

Sufficient trials, channel count, filtering policy, component plots, and rejection criteria.

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

Too few data points, rank issues, overcleaning, residual artifacts, and irreproducible manual decisions.

## Sources

TESA repo card; overcleaning artifact card.
