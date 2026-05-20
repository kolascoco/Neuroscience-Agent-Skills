---
type: paper-card
id: rogasch-2016-tesa
title: TESA / TMS-EEG preprocessing reference
year: 2016
authors: Rogasch et al.
source_pdf: ../../../TMS-EEG-artifacts/articles/TMS-EEG/rogasch2016.pdf
doi:
tags:
  - pipeline:tesa-inspired
  - step:ica
  - metric:tep
use_for:
  - TESA-style preprocessing
  - artifact cleaning rationale
confidence: seed-card
---

## Why This Matters For The Agent

Core local source for TESA-style TMS-EEG preprocessing and TEP analysis.

## Key Methods

Digest full paper before using exact recommendations.

## Practical Recommendations

Use as a source card for two-pass/structured artifact cleaning and TEP workflow rationale.

## Agent Rules Extracted

TMS-EEG preprocessing requires domain-specific artifact handling, not generic EEG cleaning alone.

## Claims To Avoid

Do not imply TESA choices are universally mandatory.

## Questions This Source Helps Answer

What is the classical TESA-style preprocessing logic?

## Related Cards

`repos/tesa.md`; `pipelines/tesa-inspired-two-pass-ica.md`.
