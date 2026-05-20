---
type: artifact-card
id: stimulation-intensity-sampling-rate-sync
title: Stimulation Intensity, Sampling Rate, And Synchronization
tags:
  - artifact:sampling-sync
  - caution:early-latency
---

## What It Is

Acquisition and stimulation parameters that alter pulse artifact amplitude, duration, and timing precision.

## Why It Matters

Early responses can be distorted by sample alignment, sampling rate, trigger precision, and stimulation intensity.

## Detection Clues

Pulse artifact duration changes with intensity, sample-level onset jitter, and different artifact morphology across acquisition settings.

## Mitigation Options

High-quality triggers, documented sampling rate, synchronized acquisition, intensity-aware artifact windows, and timing QC.

## Pipeline Implications

Report these parameters for i-TEP analysis and avoid early-window claims without them.

## Interpretation Caveats

Differences in early amplitudes may reflect acquisition/artifact differences rather than physiology.

## Sources

Jamil et al. 2024 paper card.
