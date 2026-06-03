---
type: paper-card
id: atti-2024-ica-accuracy
title: Measuring the accuracy of ICA-based artifact removal from TMS-evoked potentials
year: 2024
authors: Atti, Belardinelli, Ilmoniemi, Metsomaa
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1935861X23019629-main.pdf
doi: 10.1016/j.brs.2023.12.001
tags:
  - step:ica
  - caution:overcleaning
  - metric:tep
use_for:
  - ICA accuracy caveats
  - component rejection validation
  - overcleaning discussion
confidence: seed-card
---

## Why This Matters For The Agent

This paper gives the skill a specific source for discussing ICA accuracy rather than treating component rejection as inherently reliable.

## Main TEP Nature Points

TEP estimates can depend on how accurately ICA separates artifact from evoked activity.

## Methodological Tips And Nuances

Recommend validation/sensitivity checks, component documentation, pre/post comparisons, and caution around early TEP changes after ICA.

## Agent Rules Extracted

- Load for ICA-heavy pipelines and questions about whether ICA "worked".
- Do not accept automated/manual ICA labels without QC.

## Claims To Avoid

Do not imply ICA removal is objectively accurate without a validation strategy.

## Questions This Source Helps Answer

How accurate is ICA-based artifact removal for TMS-evoked potentials?

## Related Cards

`steps/ica-component-rejection.md`; `artifacts/overcleaning-and-ica-risk.md`.
