---
type: paper-card
id: biabani-2019-sensory-inputs
title: Characterizing and minimizing the contribution of sensory inputs to TMS-evoked potentials
year: 2019
authors: Biabani, Fornito, Mutanen, Morrow, Rogasch
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1935861X19302931-main.pdf
doi: 10.1016/j.brs.2019.07.009
tags:
  - artifact:auditory
  - artifact:somatosensory
  - caution:sensory-confounds
use_for:
  - sensory input controls
  - auditory/somatosensory caveats
  - TEP nature discussion
confidence: seed-card
---

## Why This Matters For The Agent

This is a key source for separating cortical TMS-evoked activity from sensory input contributions.

## Main TEP Nature Points

TEPs can include substantial auditory and somatosensory contributions. Spatial correlation between peripherally evoked potentials (PEPs) and TEPs emerges from ~60 ms; components earlier than ~60 ms show little overlap and are more cortically specific, while N100/P180 are most contaminated. Even at maximal masking intensity, all subjects still perceived the TMS click. Of ICA, linear regression, and SSP-SIR, SSP-SIR best removed sensory contributions while preserving non-sensory signal; ICA broadly suppressed all peaks and regression distorted early topographies.

## Methodological Tips And Nuances

Ask about masking noise, sham/control conditions, scalp sensation, mechanical vibration, and whether active and sham conditions are sensory-matched. When using SSP-SIR to suppress sensory components, inspect PC topographies and confirm they match PEP spatial patterns before projecting rather than applying it blindly.

## Agent Rules Extracted

- Load this card whenever a user interprets N100/P180/P200 or active-sham differences.
- Warn that sensory minimization is design-level, not only preprocessing-level.

## Claims To Avoid

Do not describe TEP components as target-specific cortical physiology without sensory-control evidence.

## Questions This Source Helps Answer

How can sensory inputs be characterized and minimized in TMS-EEG?

## Related Cards

`artifacts/auditory-somatosensory-confounds.md`; `papers/gordon-2018-realistic-sham.md`.
