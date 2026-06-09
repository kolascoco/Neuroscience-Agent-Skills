---
type: artifact-card
id: overcleaning-and-ica-risk
title: Overcleaning And ICA Risk
tags:
  - caution:overcleaning
  - step:ica
---

## What It Is

Loss or distortion of real evoked activity due to aggressive component rejection, projection, filtering, or interpolation.

## Why It Matters

TMS-EEG preprocessing can create plausible-looking waveforms while removing condition-relevant signal. Systematic comparisons indicate that ICA-using pipelines tend to produce smaller TEP amplitudes across all peaks, including early (N15/P30) and late (N100/P180) components, not only in windows adjacent to artifact. This points to a global suppressive effect of ICA-based cleaning that is not restricted to artifact-contaminated latencies.

## Detection Clues

Large pre/post changes in TEP morphology, removed components with evoked timing, rank loss, and condition-specific cleaning effects. Note that varying a single decay-suppression method (FastICA vs. SOUND vs. model-based detrending) can change both early TEP amplitude and topography even when late windows converge (Rogasch et al. 2022); systematic topography shifts compromise source interpretation.

## Mitigation Options

Transparent component decisions, before/after plots (compare topographies, not only amplitudes), conservative thresholds, sensitivity checks (vary rejected-component count and SSP-SIR projection count), and explicit retained-rank reporting.

## Pipeline Implications

Every cleaning step needs QC and a record of decisions. When comparing results across studies, account for the systematic ICA amplitude-suppression effect before attributing amplitude differences to physiology.

## Interpretation Caveats

Null results after heavy cleaning may reflect preprocessing suppression rather than absence of cortical response; large early responses in ICA-light pipelines may reflect residual artifact. Amplitude comparisons across studies with different cleaning strategies are not straightforward.

## Sources

`papers/methodological-choices-matter.md` (systematic pipeline comparison); `papers/rogasch-designing-comparing-cleaning.md`; `papers/atti-2024-ica-accuracy.md`; `papers/rogasch-2014-ica-artifacts-network-properties.md`.
