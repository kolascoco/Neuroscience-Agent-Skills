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

Remove stereotyped artifacts such as ocular and non-stimulus-locked muscle/background EMG while preserving neural signal. Auditory/somatosensory-related components should usually be flagged, modeled, contrasted, or subtracted with appropriate control conditions rather than removed by default.

## When To Apply

After gross pulse handling, bad-channel marking, bad-trial inspection, and enough preprocessing to make the decomposition stable. Mark bad channels before ICA and exclude them from decomposition; do not let noisy/dead channels define ICA components. Repair marked channels after ICA with SOUND, interpolation, or another documented channel-repair method when montage/geometry support it.

In SOUND/SSP-SIR-style TESA workflows, place the main physiological ICA for blinks, eye movements, ocular artifacts, and non-stimulus-locked/background muscle before SOUND and SSP-SIR. Do not use ICA to remove TMS-evoked muscle artifacts or components with clear TMS-stimulus-locked activity; those components can contain genuine TEP signal or overlap with it. Use pulse-window interpolation, projection/SSP-SIR, trial rejection, or target adjustment for TMS-evoked muscle. Use any later ICA pass only for residual non-stimulus-locked stereotyped artifacts after SOUND/SSP-SIR, with explicit before/after QC. TESA-style workflows may use two ICA passes, but the artifact target of each pass must be stated.

Do not treat broad analysis filtering as a prerequisite for ICA. If filtering is needed only to improve ICA stability, use a separate ICA-training copy or a clearly documented detrending/high-pass strategy, then apply the learned component rejection to the intended analysis data when supported by the software workflow.

## Inputs Needed

Sufficient trials, channel count, bad-channel mask before ICA, ICA-training data policy, filtering/detrending policy, component plots, and rejection criteria.

## Decision Rules

The ICA pass that precedes SOUND/SSP-SIR is for ocular, blink, eye-movement, and non-stimulus-locked/background-muscle artifact only — never for TMS-evoked muscle or stimulus-locked components. Handle those with pulse-window interpolation, projection/SSP-SIR, trial rejection, or target adjustment.

Do not reject components by label alone. Require topography, time course, spectrum, and condition-aware QC. Do not remove components with clear TMS-stimulus-locked activity unless there is a protocol-specific, documented artifact model and sensitivity analysis; ordinary ICA rejection of such components risks spoiling genuine TEP components.

Do not remove auditory/somatosensory-related components by default. If the question specifically requires sensory-response correction, prefer proper experimental contrasts or modeled subtraction, for example subtracting an auditory ERP/control response where the design supports it, and report the assumptions.

## Method Options

Manual ICA review, automated component suggestions plus human verification, two-pass ICA, or alternative cleaning when ICA is unstable. For TMS-evoked muscle, prefer projection/SSP-SIR or explicit artifact-window handling over ICA component rejection. For auditory/sensory confounds, prefer masking, sham/control contrasts, rest-vs-task contrasts, or ERP subtraction when justified by the design.

## Learning Mode Explanation

ICA can help separate artifacts, but it can also remove real evoked activity if used carelessly. TMS-stimulus-locked components are especially dangerous to reject because true TEPs are also stimulus locked.

## Code-Engineer Notes

Use `recipes/run_ica_with_qc.md`; verify MNE or TESA/tmseegpy APIs.

## QC Checks

Component maps, explained variance, bad-channel exclusion log, before/after TEPs, retained components, and active/sham or sensory-control differences.

## Failure Modes

Too few data points, rank issues, fitting ICA with bad channels included, interpolating channels before ICA in a way that creates dependent channels, overcleaning, residual artifacts, irreproducible manual decisions, default removal of auditory/sensory components that should be controlled by design/contrast, removing TMS-stimulus-locked or TMS-evoked muscle components as if they were ordinary ICA artifacts, and letting early ICA-preparation filters distort the final TEP waveform.

## Sources

TESA repo card; overcleaning artifact card.
