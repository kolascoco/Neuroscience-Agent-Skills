---
type: artifact-card
id: sampling-sync-early-artifacts
title: Sampling And Synchronization Early Artifacts
tags:
  - artifact:sampling-sync
  - metric:itep
  - caution:early-latency
---

## What It Is

Timing and sampling effects that alter apparent early response amplitude or latency.

## Why It Matters

At early latencies, a few samples of jitter or pulse misalignment can materially change the result.

## Detection Clues

Variable pulse sample index, inconsistent trigger delay, sampling-rate-dependent artifact duration, and intensity-dependent artifact morphology.

## Mitigation Options

Verify triggers, avoid unverified resampling before pulse handling, document sampling rate, and align events carefully.

If downsampling is needed, first confirm that the pulse artifact and interpolation/removal windows are handled and that the resampling method applies anti-alias filtering. Then inspect whether the anti-alias filter introduced ringing or latency changes around the pulse.

## Pipeline Implications

Early analysis must report sampling and synchronization details.

For i-TEPs, keep a native high-sampling copy for pulse/decay QC and justify any downsampling before early-window analysis.

## Interpretation Caveats

An early latency shift can be technical, not physiological. A new early oscillation after resampling or filtering may be filter-induced ringing, not a cortical response.

## Sources

Jamil et al. 2024; filtering and downsampling step cards.
