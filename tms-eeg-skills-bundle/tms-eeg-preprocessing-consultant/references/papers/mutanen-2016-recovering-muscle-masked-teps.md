---
type: paper-card
id: mutanen-2016-recovering-muscle-masked-teps
title: Recovering TMS-evoked EEG responses masked by muscle artifacts
year: 2016
authors: Mutanen, Kukkonen, Nieminen, Stenroos, Sarvas, Ilmoniemi
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1053811916301495-main.pdf
doi:
tags:
  - artifact:muscle
  - source-analysis
  - metric:tep
use_for:
  - muscle artifact recovery
  - early TEP preservation
  - source/model-informed cleaning
confidence: seed-card
---

## Why This Matters For The Agent

This article is central for the idea that useful TEP responses may be recoverable even when muscle artifact initially masks them.

## Main TEP Nature Points

Muscle artifacts can hide TEP components rather than simply add noise; cleaning choices can reveal or distort underlying responses.

## Methodological Tips And Nuances

Use before/after waveform and topography checks. Avoid overcleaning that flattens early components. Discuss source/model assumptions when recovery methods are used.

## Agent Rules Extracted

- Load for strong muscle artifact cases.
- Recommend sensitivity checks around early windows.
- Separate "recovered response" from proof of cortical origin.

## Claims To Avoid

Do not claim recovered TEPs are necessarily clean neural signal without controls.

## Questions This Source Helps Answer

Can TEPs be recovered when masked by TMS-evoked muscle artifacts?

## Related Cards

`artifacts/muscle-artifact.md`; `pipelines/sound-ssp-sir-enhanced.md`.
