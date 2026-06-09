---
type: artifact-card
id: early-pulse-residual-risk
title: Early Pulse Residual Risk
tags:
  - artifact:pulse
  - metric:itep
  - caution:early-latency
---

## What It Is

Residual pulse, recovery, interpolation, or ringing artifact inside the immediate post-pulse analysis window.

## Why It Matters

i-TEPs are analyzed close to the strongest artifact in the recording. The decay artifact can extend tens of milliseconds beyond the interpolated pulse window, with amplitude correlated to pulse amplitude (ρ ≈ 0.86; Lankinen et al. 2026), so a short interpolation window (e.g., −2 to 10 ms) may leave a decay tail that mimics an early biological response but is actually capacitive discharge.

## Detection Clues

Sharp discontinuities, edge effects at interpolation boundaries, channel-wide synchronous peaks, and inconsistent single-trial morphology.

## Mitigation Options

Conservative artifact windows, sensitivity analysis, single-trial QC, no-filter diagnostics, and explicit reporting.

## Pipeline Implications

Load this card for every i-TEP request.

## Interpretation Caveats

Without artifact-boundary evidence, describe early findings as exploratory.

## Sources

Lankinen et al. 2026 (decay tail); Beck 2024; Nuyts 2025; Jamil 2024.
