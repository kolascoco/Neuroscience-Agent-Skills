---
type: artifact-card
id: pulse-artifact
title: TMS Pulse Artifact
tags:
  - artifact:pulse
  - caution:early-latency
---

## What It Is

The large electromagnetic artifact around the TMS pulse, often orders of magnitude larger than EEG.

## Why It Matters

It can saturate channels, contaminate filters and ICA, and dominate early response windows.

## Detection Clues

Sharp pulse-locked transient, channel-wide amplitude excursion, clipping, and abnormal recovery after pulse.

## Mitigation Options

Accurate event timing, marking/removal/interpolation windows, artifact-specific toolbox routines, and post-removal QC.

## Pipeline Implications

Handle before filtering and before ICA. For i-TEPs, report the exact artifact window and justify any early analysis window.

## Interpretation Caveats

Any response close to the pulse requires proof that residual artifact is not driving the effect.

## Sources

Jamil et al. 2024; TESA and MNE/tmseegpy workflow cards.
