---
type: paper-card
id: rogasch-designing-comparing-cleaning
title: Designing and comparing cleaning pipelines for TMS-EEG
year:
authors: Rogasch et al.
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/nigel-c-rogasch-designing-and-comparing-cleaning.pdf
doi:
tags:
  - pipeline:tesa-inspired
  - caution:overcleaning
  - step:qc
use_for:
  - pipeline comparison
  - cleaning rationale
confidence: seed-card
---

## Why This Matters For The Agent

Local source for comparing preprocessing choices and explaining tradeoffs.

## Key Methods

Compares cleaning approaches head-to-head (e.g., FastICA, SOUND without ICA, and a model-based detrending approach), using single-step manipulation so that the effect of one choice can be isolated rather than confounded in an end-to-end comparison. FastICA and SOUND tend to converge for late-window TEPs but differ in early windows (~0–50 ms); model-based detrending can diverge more broadly. Varying the decay-suppression method alone changes both early TEP amplitude and topography. Notes that ICA's statistical-independence assumption is weakened by the time-locked nature of TMS-evoked activity, and that concatenating conditions for ICA is valid only when they share the same non-neural noise structure.

## Practical Recommendations

Use for pipeline comparison answers and cautions about methodological choices. When reporting or comparing results, specify which decay-suppression method was used. For ICA: keep retained PCA components fewer than the number of trials, do not let the initial pass contain TMS-evoked muscle transients, and run a sensitivity check (vary rejected-component count by ±2 and inspect TEP stability).

## Agent Rules Extracted

Pipeline choices should be justified by artifact profile, target, and analysis goal. If a user reports unusual early TEP morphology, ask which decay-suppression method was used — it is a primary source of inter-pipeline divergence.

## Claims To Avoid

Do not rank pipelines universally without dataset context.

## Questions This Source Helps Answer

How should different TMS-EEG cleaning pipelines be compared?

## Related Cards

`artifacts/overcleaning-and-ica-risk.md`; `pipelines/tesa-inspired-two-pass-ica.md`.
