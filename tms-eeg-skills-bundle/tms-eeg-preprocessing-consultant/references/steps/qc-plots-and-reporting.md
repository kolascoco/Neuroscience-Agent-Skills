---
type: step-card
id: qc-plots-and-reporting
title: QC Plots And Reporting
tags:
  - step:qc
applies_to:
  - conservative-mne-python
  - tesa-inspired-two-pass-ica
  - sound-ssp-sir-enhanced
  - itep-early-response-analysis
load_with:
  - recipes/qc_report.md
---

## Purpose

Make preprocessing decisions auditable and catch residual artifacts before interpretation.

## When To Apply

At every major stage and in final reporting.

## Inputs Needed

Raw/cleaned data, events, artifact windows, bad channels, ICA/projection decisions, trial rejection logs, and condition labels.

## Decision Rules

Every substantive cleaning step should have a before/after plot or numeric summary.

## Method Options

Raw overlays, epoch images, component reports, evoked butterfly plots, topomaps, spectra, GMFA/LMFP, reference mode, and trial-count tables.

## Learning Mode Explanation

QC is not decoration; it is the evidence that a preprocessing choice did not create the result.

## Code-Engineer Notes

Use MNE report/plotting APIs if available; otherwise save clear static figures.

## QC Checks

Include pulse windows, artifact residuals, component decisions, retained trials, and condition balance.

## Failure Modes

Only plotting final averages, no artifact-window report, no trial counts, missing reference mode for feature calculation, and missing code/config provenance.

## Sources

All pipeline cards.
