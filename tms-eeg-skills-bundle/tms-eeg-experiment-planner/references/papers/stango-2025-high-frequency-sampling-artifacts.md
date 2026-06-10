---
type: paper-card
id: stango-2025-high-frequency-sampling-artifacts
title: Impact Of High-Frequency Sampling Rate And Stimulation Intensity On Early TMS Artifacts: Considerations For Immediate TMS-EEG Responses
year: 2025
authors: Stango A; Zazio A; Barchiesi G; Bonfiglio NS; Bortoletto M
source_pdf: 1-s2.0-S1053811925005294-main.pdf
doi: 10.1016/j.neuroimage.2025.121526
tags:
  - early-artifacts
  - tms-pulse-artifact
  - decay-artifact
  - sampling-rate
  - intensity
  - itep
use_for:
  - distinguishing TMS-pulse artifact from decay artifact
  - planning sampling rate for immediate TEP studies
  - explaining why high sampling rate does not fully solve decay
confidence: high
---

## Why This Matters For The Agent

This technical note separates two early artifacts that are often conflated in TMS-EEG discussions: the initial TMS-pulse artifact and the longer decay artifact. It is especially important for immediate TEP/i-TEP planning, where responses of interest may occur only a few milliseconds after stimulation.

## Key Methods

- Phantom recordings using a melon and a simple electrical circuit.
- Sampling rates: 4800 Hz, 9600 Hz, and 19,200 Hz.
- Stimulation intensities: 40%, 70%, and 100% of maximum stimulator output.
- Two commercial stimulators.
- Measured both end of TMS-pulse artifact and back-to-baseline timing.

## Practical Recommendations

- Distinguish the end of the TMS-pulse artifact from complete signal recovery/back-to-baseline.
- Use high sampling rates when immediate TEPs are endpoints, but report amplifier/filter behavior when possible.
- Treat stimulation intensity as an important determinant of decay/back-to-baseline duration.
- Plan explicit decay checks when interpreting responses around 2-6 ms.
- Document what early time window is considered lost, interpolated, fitted, or physiologically interpretable.

## Agent Rules Extracted

- When a user asks how early TMS artifacts look, explain both the initial pulse artifact and the following decay artifact.
- When a user asks whether high sampling solves early artifacts, answer: it helps with the pulse artifact, but decay can persist and is more strongly linked to intensity/setup factors.
- For i-TEP claims, require reporting of sampling rate, amplifier settings, trigger timing, intensity, artifact duration, pulse-removal window, and decay handling.

## Claims To Avoid

- Do not claim that high sampling frequency alone makes immediate TEPs clean.
- Do not treat signal recovery after the pulse artifact as equivalent to signal recovery to baseline.
- Do not assume phantom timings automatically transfer to every human EEG setup, amplifier, coil, and electrode montage.

## Questions This Source Helps Answer

- What is the difference between TMS-pulse artifact and decay artifact?
- Why can the pulse artifact be short while the signal is not yet fully recovered?
- How do sampling rate and intensity affect early artifacts?
- What should be reported for i-TEP artifact windows?

## Related Cards

- `references/artifact-appearance/tms-pulse-artifact-appearance.md`
- `references/artifact-appearance/decay-artifact-appearance.md`
- `references/online-qc/itep-acquisition-practice.md`
- `references/artifacts/channel-lead-preparation-decay-avoidance.md`
