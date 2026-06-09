---
type: artifact-card
id: pulse-artifact
title: TMS Pulse Artifact
tags:
  - artifact:pulse
  - caution:early-latency
---

## What It Is

The large electromagnetic artifact around the TMS pulse, typically 4–5 orders of magnitude larger than background EEG (Rogasch et al. 2017). Its true width is roughly 0.2 ms but low-pass filtering stretches it to ~0.55 ms (Lankinen et al. 2026). It is causally linked to the subsequent decay/recharge artifact, with which it is strongly correlated (ρ ≈ 0.86), both arising from electromagnetic induction through electrode lead loops.

## Why It Matters

It can saturate channels, contaminate filters and ICA, and dominate early response windows.

## Detection Clues

Sharp pulse-locked transient, channel-wide amplitude excursion, clipping, and abnormal recovery after pulse.

## Mitigation Options

Accurate event timing, marking/removal/interpolation windows, artifact-specific toolbox routines, and post-removal QC. At the hardware level, sample-and-hold amplifiers hold voltage during the pulse (recovery ~2–5 ms), while DC-coupled amplifiers with high sampling (≥5 kHz) and fine resolution (≤24 nV/bit) are an alternative for very early recording (Rogasch et al. 2017).

## Pipeline Implications

Handle before filtering and before ICA: filtering across an unremoved pulse introduces ringing that can persist across the whole analysis window and cannot be removed afterward (Rogasch et al. 2017; 2022). Pulse artifact amplitude and duration also depend strongly on acquisition: sampling frequency is the dominant predictor and stimulation intensity the second (Jamil et al. 2024), so the artifact window must be matched to the dataset, not assumed universal (see `artifacts/stimulation-intensity-sampling-rate-sync.md`). For i-TEPs, report the exact artifact window and justify any early analysis window.

## Interpretation Caveats

Any response close to the pulse requires proof that residual artifact is not driving the effect.

## Sources

Rogasch et al. 2017; Lankinen et al. 2026; Jamil et al. 2024; TESA and MNE/tmseegpy workflow cards.
