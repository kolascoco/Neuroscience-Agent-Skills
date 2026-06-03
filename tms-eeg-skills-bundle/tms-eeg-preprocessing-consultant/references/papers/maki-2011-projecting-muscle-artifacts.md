---
type: paper-card
id: maki-2011-projecting-muscle-artifacts
title: Projecting out muscle artifacts from TMS-evoked EEG
year: 2011
authors: Maki, Ilmoniemi
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1053811910014710-main.pdf
doi:
tags:
  - artifact:muscle
  - step:projection
  - caution:overcleaning
use_for:
  - muscle artifact projection
  - early TMS artifact handling
confidence: seed-card
---

## Why This Matters For The Agent

This is an early methodological source for projection-based handling of TMS-evoked muscle artifact.

## Main TEP Nature Points

Muscle artifacts can mask or distort TMS-evoked EEG responses, especially in early windows and target-adjacent channels.

## Methodological Tips And Nuances

Projection can suppress artifact structure, but the agent should require pre/post TEP checks and avoid treating projected data as automatically artifact-free.

## Agent Rules Extracted

- Use projection methods only with explicit artifact windows/components.
- Mention risk of attenuating early neural signal.
- Report what was projected and how TEP morphology changed.

## Claims To Avoid

Do not claim projection removes only muscle artifact without affecting EEG.

## Questions This Source Helps Answer

How can projection methods reduce TMS-evoked muscle artifacts?

## Related Cards

`artifacts/muscle-artifact.md`; `steps/ssp-sir-cleaning.md`; `artifacts/overcleaning-and-ica-risk.md`.
