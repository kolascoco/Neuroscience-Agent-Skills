---
type: paper-card
id: beck-2024-iteps
title: Transcranial magnetic stimulation of primary motor cortex elicits an immediate transcranial evoked potential
year: 2024
authors: Beck et al.
source_pdf: ../../../../TMS-EEG-artifacts/articles/nature of effects/Beck BrainStim2024 iTEPS.pdf
doi:
tags:
  - metric:itep
  - target:m1
  - caution:early-latency
use_for:
  - immediate TEP analysis
  - M1 early response discussion
confidence: seed-card
---

## Why This Matters For The Agent

Primary source defining the immediate TEP (i-TEP) after M1 stimulation: an early EEG response beginning ~2 ms post-pulse, distinct from conventional TEP peaks that are "too late" (≥10 ms) to reflect direct cortical excitation. Routes immediate-response questions to the i-TEP pipeline.

## Key Methods

25 healthy participants; single biphasic pulses (MC-B70 coil, MagVenture X100) over left M1_HAND at 95% and 110% RMT, plus parietal/midline control sites. EEG digitized at **50 kHz** (anti-alias low-pass 10,300 Hz) to shorten the pulse artifact to ~2 ms; recharge delayed to 500 ms; concurrent FDI EMG. Stimulation site optimized via a "TEP-optimized spot" procedure — coil moved/tilted/rotated away from temporalis to avoid scalp-muscle co-activation (CMAPs appear as a >100 µV anterolateral bipolar pattern, visible per-trial); subjects excluded if muscle twitches could not be avoided. Neuronavigated (Localite) on individual T1.

## Practical Recommendations

For i-TEPs, use very high sampling rates to minimize pulse-artifact duration, optimize coil placement online to eliminate scalp-muscle CMAPs (not just rely on cleaning), and inspect single trials for muscle co-activation. Report sampling rate, anti-alias filter, RMT/intensity, current direction, recharge delay, coil-adjustment procedure, and the early-window definition. The multi-peak i-TEP (~1.1–1.4 ms inter-peak interval over sensorimotor electrodes) is modulated by intensity and current direction.

## Agent Rules Extracted

Treat i-TEPs as a special early-latency analysis with stricter artifact controls than ordinary late TEP analysis: muscle co-activation and pulse artifact are the dominant threats and are best handled at acquisition. The authors themselves frame the cortical origin as needing corroboration, including instrumental/physiological-artifact checks.

## Claims To Avoid

Do not claim i-TEPs are clean cortical responses unless pulse-artifact, scalp-muscle, and instrumental controls are addressed. Do not assume conventional TEP peaks reflect the immediate cortical response — by their latency they likely reflect subsequent network excitation.

## Questions This Source Helps Answer

What is an i-TEP and how does it differ from conventional TEP peaks? Why are 50 kHz sampling and coil-position optimization used? How should immediate M1 responses be acquired and analyzed?

## Related Cards

`pipelines/itep-early-response-analysis.md`; `artifacts/early-pulse-residual-risk.md`; `artifacts/muscle-artifact.md`; `artifacts/stimulation-intensity-sampling-rate-sync.md`.
