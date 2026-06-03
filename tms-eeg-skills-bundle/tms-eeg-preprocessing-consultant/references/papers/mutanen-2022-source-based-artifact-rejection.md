---
type: paper-card
id: mutanen-2022-source-based-artifact-rejection
title: Source-based artifact-rejection techniques for TMS-EEG
year: 2022
authors: Mutanen, Metsomaa, Makkonen, Varone, Marzetti, Ilmoniemi
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S0165027022002199-main.pdf
doi: 10.1016/j.jneumeth.2022.109693
tags:
  - artifact:muscle
  - step:ssp-sir
  - step:sound
  - source-analysis
use_for:
  - source-based artifact rejection
  - SOUND/SSP-SIR rationale
  - model-informed cleaning caveats
confidence: seed-card
---

## Why This Matters For The Agent

This paper anchors the skill's source-based artifact-rejection branch and supports cautious use of methods such as SOUND and SSP-SIR.

## Main TEP Nature Points

Some early TMS-EEG activity may be contaminated or masked by artifacts that have spatial/source structure. Source-based methods can help, but their assumptions influence what remains in the TEP.

## Methodological Tips And Nuances

Require valid electrode locations, source/model assumptions, rank/projection reporting, and before/after QC. Source-based rejection is not a black-box replacement for artifact understanding.

## Agent Rules Extracted

- Load this card for SOUND, SSP-SIR, source-based rejection, or muscle artifact recovery questions.
- Ask for montage/electrode coordinates before recommending source-based cleaning.
- Report rank/projection effects and pre/post TEP comparisons.

## Claims To Avoid

Do not claim source-based cleaning proves cortical origin of a TEP component.

## Questions This Source Helps Answer

How can source-based artifact-rejection techniques help TMS-EEG preprocessing?

## Related Cards

`pipelines/sound-ssp-sir-enhanced.md`; `steps/sound-cleaning.md`; `steps/ssp-sir-cleaning.md`.
