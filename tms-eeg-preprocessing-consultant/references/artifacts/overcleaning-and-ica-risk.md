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

TMS-EEG preprocessing can create plausible-looking waveforms while removing condition-relevant signal.

## Detection Clues

Large pre/post changes in TEP morphology, removed components with evoked timing, rank loss, and condition-specific cleaning effects.

## Mitigation Options

Transparent component decisions, before/after plots, conservative thresholds, sensitivity checks, and retained-rank reporting.

## Pipeline Implications

Every cleaning step needs QC and a record of decisions.

## Interpretation Caveats

Null results after heavy cleaning may reflect preprocessing choices; positive results may reflect residual artifacts.

## Sources

TESA and methodological pipeline comparison cards.
