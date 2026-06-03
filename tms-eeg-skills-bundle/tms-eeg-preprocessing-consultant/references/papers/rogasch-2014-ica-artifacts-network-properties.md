---
type: paper-card
id: rogasch-2014-ica-artifacts-network-properties
title: "Removing artefacts from TMS-EEG recordings using independent component analysis: Importance for assessing prefrontal and motor cortex network properties"
year: 2014
authors: Rogasch, Thomson, Farzan, Fitzgibbon, Bailey, Hernandez-Pavon, Daskalakis, Fitzgerald
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S105381191400620X-main.pdf
doi:
tags:
  - step:ica
  - artifact:muscle
  - target:dlpfc
  - target:m1
use_for:
  - ICA artifact removal
  - prefrontal versus motor TMS-EEG comparisons
  - network-property caveats
confidence: seed-card
---

## Why This Matters For The Agent

This card supports ICA as a major TMS-EEG cleaning method and highlights why artifact removal matters for downstream network/property interpretation.

## Main TEP Nature Points

Observed TEP/network differences can depend on whether artifacts are adequately removed, especially across targets with different artifact profiles.

## Methodological Tips And Nuances

ICA decisions should be supported by component topography, time course, spectrum, and before/after TEP plots. Prefrontal and motor targets may need different artifact scrutiny.

## Agent Rules Extracted

- Load this card for ICA explanations.
- Warn that network-property conclusions are preprocessing-sensitive.
- Keep DLPFC muscle/sensory caveats visible.

## Claims To Avoid

Do not state that ICA-cleaned TEPs are automatically artifact-free.

## Questions This Source Helps Answer

Why is ICA important in TMS-EEG, and how can it affect prefrontal/motor interpretations?

## Related Cards

`steps/ica-component-rejection.md`; `pipelines/tesa-inspired-two-pass-ica.md`.
