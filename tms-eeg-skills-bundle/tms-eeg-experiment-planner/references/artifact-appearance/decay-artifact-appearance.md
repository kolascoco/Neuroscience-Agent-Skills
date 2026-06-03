---
type: artifact-appearance-card
id: decay-artifact-appearance
title: Decay Artifact Appearance
artifact_type: decay
tags:
  - decay-artifact
  - early-artifacts
  - electrode-skin-gel
  - itep
load_with:
  - references/artifacts/channel-lead-preparation-decay-avoidance.md
  - references/online-qc/online-artifact-checklist.md
source_cards:
  - references/papers/stango-2025-high-frequency-sampling-artifacts.md
  - references/papers/lankinen-2026-lead-configuration-early-artifacts.md
---

## What It Looks Like

A longer-lasting exponential-like deflection after the pulse. It often appears as a return-to-baseline component following the initial high-amplitude TMS-pulse artifact. It may look like a smooth decay, drift, or sloped residual that can contaminate the first milliseconds to tens of milliseconds depending on setup quality and hardware.

Conceptually, it is often related to charge accumulation and discharge in an electrode-skin-gel system that behaves partly like a capacitor. It may also involve eddy currents in electrodes and leads. Stango et al. 2025 showed that a decay component can remain visible even under controlled phantom conditions with low impedance.

## Timing Clues

- Starts at or immediately after the pulse, but its earliest portion can be hidden under the larger TMS-pulse artifact.
- Becomes visually dominant after the TMS-pulse artifact ends.
- In high-quality high-sampling setups, signal may return to baseline around 2-3 ms, but this is not guaranteed and is strongly setup-dependent.
- For i-TEPs, even sub-millisecond differences in artifact recovery can change interpretation.

## Topography Clues

Decay can be channel-localized when driven by electrode contact, gel, or lead configuration. It may also appear more broadly if amplifier recovery or shared hardware factors dominate. A decay-like topography in channels near the coil or along specific cable paths should be treated as acquisition evidence, not cortical evidence.

## Single-Trial Versus Average Clues

If decay is time-locked and consistent, it remains in averages and can mimic early TEP morphology. If it varies by electrode contact or trial, it may cause unstable early baselines, apparent channel-specific slopes, or early residuals that survive simple averaging.

## Common Confusions

- Decay versus early TEP/i-TEP: an early deflection after pulse removal may still be decay, especially if it follows an exponential-like course or tracks intensity.
- Decay versus pulse artifact: the decay is usually the longer return-to-baseline part, while the pulse artifact is the initial high-amplitude electromagnetic component.
- Decay versus bad channel: bad contact can create isolated decay-like residuals that look like a channel problem rather than a whole-recording artifact.

## Acquisition Checks

- Check impedance/contact quality, gel bridges, electrode stability, cable loops, and cable tension.
- Route wires carefully and orient them approximately perpendicular to the coil handle when feasible.
- Test whether small changes in electrode contact, lead routing, coil placement, or intensity reduce the decay.
- Document sampling frequency, amplifier settings, TMS intensity, coil orientation, and artifact recovery time.

## Preprocessing Checks

- Treat decay as an acquisition/setup problem first.
- ICA, detrending/fitting, SOUND-like methods, and interpolation can help, but they require explicit modeling choices and may remove or distort early physiological responses.
- For i-TEP studies, report how the decay window was identified and what signal was considered unrecoverable.

## What Not To Conclude

- Do not assume that increasing sampling rate alone removes decay. Stango et al. 2025 suggests sampling rate mostly affects the TMS-pulse artifact, while decay/back-to-baseline is more strongly influenced by stimulation intensity and setup factors.
- Do not interpret early local responses as cortical until decay has been separated from pulse artifact and controlled against intensity, lead, and channel effects.

## Sources

Stango et al. 2025 NeuroImage technical note; Lankinen et al. 2026 lead-configuration preprint; local good-practice note.
