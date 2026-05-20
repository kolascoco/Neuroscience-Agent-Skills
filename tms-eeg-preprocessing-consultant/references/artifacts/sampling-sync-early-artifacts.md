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

## Pipeline Implications

Early analysis must report sampling and synchronization details.

## Interpretation Caveats

An early latency shift can be technical, not physiological.

## Sources

Jamil et al. 2024.
