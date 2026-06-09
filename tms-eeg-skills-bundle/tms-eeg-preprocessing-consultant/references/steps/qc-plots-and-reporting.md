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

Report the analysis reference and the stage at which it was applied. Average reference, REST, and mastoid/linked-ear references change TEP topography and GMFA/LMFP, so much cross-study amplitude variation reflects reference choice rather than physiology. Select LMFP ROI channels only after the final full-channel reference.

Report the retained data rank after every rank-reducing step (bad-channel interpolation, SOUND, SSP-SIR, ICA). Undocumented rank loss inflates channel correlations and distorts source/topography estimates.

State the baseline-correction window and verify it does not overlap residual pulse/decay artifact; a contaminated baseline biases every downstream amplitude and latency.

Apply identical preprocessing to active and sham/control conditions: same artifact windows, same component-rejection criteria, same projections, and the same retained rank. Condition-specific cleaning is a hidden confound in active-vs-sham contrasts. Where trial counts differ after rejection, match them or report the imbalance, since averaged-trial count and SNR affect TEP/GMFA amplitude.

## Method Options

Raw overlays, epoch images, component reports, evoked butterfly plots, topomaps, spectra, GMFA/LMFP, reference mode, and trial-count tables.

## Learning Mode Explanation

QC is not decoration; it is the evidence that a preprocessing choice did not create the result.

## Code-Engineer Notes

Use MNE report/plotting APIs if available; otherwise save clear static figures.

## QC Checks

Include pulse windows, artifact residuals, component decisions, retained trials, condition balance, the analysis reference and its stage, the retained rank after each rank-reducing step, and the baseline-correction window.

## Failure Modes

Only plotting final averages, no artifact-window report, no trial counts, missing reference mode for feature calculation, undocumented rank loss, baseline overlapping residual artifact, condition-specific preprocessing in active-vs-sham contrasts, unmatched/unreported trial counts across conditions, and missing code/config provenance.

## Sources

All pipeline cards.
