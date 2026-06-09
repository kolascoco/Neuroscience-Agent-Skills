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

Early responses can be distorted by sample alignment, sampling rate, trigger precision, and stimulation intensity. Among these, sampling frequency is the dominant predictor of pulse artifact amplitude (~56% of variance) and duration (~49%), stimulation intensity is second (~38% / ~41%), and synchronization is a minor third factor (~6% / ~9%) (Jamil et al. 2024).

## Detection Clues

Pulse artifact duration changes with intensity, sample-level onset jitter, and different artifact morphology across acquisition settings. Acquiring at 20 kHz versus 5 kHz yields ~86% higher pulse amplitude but ~57% shorter duration; higher intensity adds ~6% amplitude and ~30% duration; synchronized acquisition lowers amplitude ~3% and improves within-subject consistency (Jamil et al. 2024). High-Fs data can thus appear to need a shorter artifact window while actually carrying a sharper, higher-amplitude transient.

## Mitigation Options

High-quality triggers, documented sampling rate, synchronized acquisition, intensity-aware artifact windows, and timing QC.

Avoid changing sampling rate before checking whether stimulation intensity changes pulse width, decay duration, or muscle artifact morphology. Downsampling can hide or smear these differences through anti-alias filtering.

## Pipeline Implications

Report these parameters for i-TEP analysis and avoid early-window claims without them.

When downsampling is performed, report the original and final sampling rates, resampling step location, and whether event timing was rechecked afterward.

## Interpretation Caveats

Differences in early amplitudes may reflect acquisition/artifact differences rather than physiology. Filtering and anti-alias operations can also create condition-specific ringing if artifact morphology differs between conditions.

## Sources

Jamil et al. 2024 paper card; filtering and downsampling step cards.
