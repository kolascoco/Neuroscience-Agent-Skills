---
type: paper-card
id: methodological-choices-matter
title: Methodological choices matter in TMS-EEG preprocessing
year:
authors:
source_pdf: ../../../TMS-EEG-artifacts/articles/TMS-EEG/methodological_choices_matter_a_systematic_comparison_of_tms_eeg.pdf
doi:
tags:
  - pipeline:mne
  - pipeline:sound-ssp-sir
  - caution:overcleaning
  - step:qc
use_for:
  - preprocessing tradeoffs
  - pipeline sensitivity
confidence: seed-card
---

## Why This Matters For The Agent

Supports the skill's central caution that preprocessing decisions can materially alter TMS-EEG outputs.

## Key Methods

Digest full paper before making detailed claims.

## Practical Recommendations

Use when explaining why QC, parameter reporting, and sensitivity checks are necessary.

## Agent Rules Extracted

Do not present a single preprocessing path as objectively correct without context.

## Claims To Avoid

Avoid unqualified "best pipeline" statements.

## Questions This Source Helps Answer

How do preprocessing choices affect TMS-EEG results?

## Related Cards

`pipelines/conservative-mne-python.md`; `pipelines/sound-ssp-sir-enhanced.md`.
