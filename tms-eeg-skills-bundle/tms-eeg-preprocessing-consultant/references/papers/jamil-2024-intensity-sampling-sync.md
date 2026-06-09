---
type: paper-card
id: jamil-2024-intensity-sampling-sync
title: The Effect of Stimulation Intensity, Sampling Frequency, and Sample Synchronization in TMS-EEG on the TMS Pulse Artifact Amplitude and Duration
year: 2024
authors: Jamil et al.
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/The_Effect_of_Stimulation_Intensity_Sampling_Frequency_and_Sample_Synchronization_in_TMS-EEG_on_the_TMS_Pulse_Artifact_Amplitude_and_Duration.pdf
doi: 10.1109/TNSRE.2024.3429176
tags:
  - artifact:pulse
  - artifact:sampling-sync
  - caution:early-latency
use_for:
  - acquisition caveats
  - pulse artifact duration
  - i-TEP timing risk
confidence: seed-card
---

## Why This Matters For The Agent

Acquisition parameters directly affect pulse artifact amplitude/duration and early analysis reliability.

## Key Methods

Quantifies how acquisition/stimulation parameters affect the TMS pulse artifact. Sampling frequency is the dominant predictor of artifact amplitude (~56% of variance) and duration (~49%); stimulation intensity is second (~38% / ~41%); sample synchronization is minor (~6% / ~9%). Acquiring at 20 kHz vs. 5 kHz gives ~86% higher amplitude but ~57% shorter duration; higher intensity adds ~6% amplitude and ~30% duration; synchronized acquisition reduces amplitude ~3% and improves within-subject consistency.

## Practical Recommendations

Ask for stimulation intensity, sampling rate, synchronization, and trigger timing when discussing early responses. Artifact-window durations cannot be generalized across datasets acquired at different sampling rates or intensities; the window must be Fs- and intensity-aware.

## Agent Rules Extracted

Never give an i-TEP analysis plan without reporting sampling/synchronization and artifact window assumptions.

## Claims To Avoid

Do not attribute early amplitude/duration changes to physiology before acquisition effects are checked. Do not recommend a fixed artifact-window length (e.g., "use 10 ms") without specifying the sampling-rate and stimulation-intensity context.

## Questions This Source Helps Answer

How do sampling rate and synchronization affect early TMS-EEG artifacts?

## Related Cards

`artifacts/sampling-sync-early-artifacts.md`; `steps/early-latency-qc.md`.
