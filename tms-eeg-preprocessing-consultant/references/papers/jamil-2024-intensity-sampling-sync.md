---
type: paper-card
id: jamil-2024-intensity-sampling-sync
title: The Effect of Stimulation Intensity, Sampling Frequency, and Sample Synchronization in TMS-EEG on the TMS Pulse Artifact Amplitude and Duration
year: 2024
authors: Jamil et al.
source_pdf: ../../../TMS-EEG-artifacts/articles/TMS-EEG/The_Effect_of_Stimulation_Intensity_Sampling_Frequency_and_Sample_Synchronization_in_TMS-EEG_on_the_TMS_Pulse_Artifact_Amplitude_and_Duration.pdf
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

Digest full methods before citing exact quantitative relationships.

## Practical Recommendations

Ask for stimulation intensity, sampling rate, synchronization, and trigger timing when discussing early responses.

## Agent Rules Extracted

Never give an i-TEP analysis plan without reporting sampling/synchronization and artifact window assumptions.

## Claims To Avoid

Do not attribute early amplitude/duration changes to physiology before acquisition effects are checked.

## Questions This Source Helps Answer

How do sampling rate and synchronization affect early TMS-EEG artifacts?

## Related Cards

`artifacts/sampling-sync-early-artifacts.md`; `steps/early-latency-qc.md`.
