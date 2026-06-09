---
type: artifact-card
id: filter-ringing
title: Filter Ringing
tags:
  - artifact:filter-ringing
  - step:filtering
  - caution:early-latency
---

## What It Is

Sustained oscillatory artifact introduced by applying temporal filters (FIR/IIR high-pass, low-pass, notch, or anti-alias) to data that still contains large discontinuities: the TMS pulse artifact, muscle transients, or interpolation-window boundaries.

## Why It Matters

Ringing can mimic genuine oscillatory TEP components and spread across the entire analysis window. Once introduced it is impossible to separate from real responses without comparison to unfiltered data.

## Detection Clues

Apparent oscillations symmetric around a discontinuity, "components" that appear in artifact-free or blank epochs filtered under the same settings, and morphology that changes with filter order/band. Edge effects at interpolation boundaries are a common source.

## Mitigation Options

Remove or interpolate the pulse and gross artifacts before any analysis filter. Apply anti-alias filtering only after pulse handling, then inspect the pulse/interpolation edges. Avoid aggressive high-pass filtering on short epochs. Keep any ICA-only filtered copy separate from the final analysis data.

## Pipeline Implications

This is the primary justification for the "pulse first, filter later" ordering used in all standard TMS-EEG pipelines. When downsampling, verify artifact-window boundaries on single-trial traces, not only averages.

## Interpretation Caveats

Early oscillatory findings require a no-filter or filter-sensitivity diagnostic before being treated as physiological.

## Sources

Rogasch et al. 2017; Rogasch et al. 2022; `steps/filtering.md`; `steps/downsampling-and-resampling.md`.
