---
type: paper-card
id: hernandez-pavon-2023-recommendations-open-issues
title: "TMS combined with EEG: Recommendations and open issues for data collection and analysis"
year: 2023
authors: Hernandez-Pavon, Veniero, Bergmann, Belardinelli, Bortoletto, Casarotto, Casula, Farzan, Fecchio, Julkunen, Kallioniemi, Lioumis, Metsomaa, Miniussi, Mutanen, Rocchi, Rogasch, Shafi, Siebner, Thut, Zrenner, Ziemann, Ilmoniemi, and colleagues
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1935861X23016960-main.pdf
doi: 10.1016/j.brs.2023.02.009
tags:
  - recommendations
  - good-practice
  - preprocessing
  - acquisition
  - metric:tep
use_for:
  - good-practice guidance
  - acquisition and analysis recommendations
  - caveats and open issues
confidence: seed-card
---

## Why This Matters For The Agent

This is a central recommendations paper for TMS-EEG data collection and analysis. Use it as a high-priority citation when the user asks for best practice, reporting, acquisition, preprocessing, or open methodological issues.

## Main TEP Nature Points

TEPs are shaped by stimulation target, state, sensory inputs, artifacts, acquisition choices, and preprocessing. The agent should frame TEPs as experimentally constrained evoked responses, not direct readouts of one physiological quantity.

## Methodological Tips And Nuances

Emphasize standardized reporting, control conditions, artifact handling, timing precision, careful preprocessing order, and transparent analysis choices. Use this paper to justify asking for metadata before proposing a pipeline.

## Agent Rules Extracted

- Load this card for broad "what should I do?" TMS-EEG preprocessing questions.
- Require acquisition, artifact, and control-condition details before definitive advice.
- Mention open issues rather than pretending there is one universally accepted pipeline.

## Claims To Avoid

Do not give rigid universal parameters where the field still treats them as open or context-dependent.

## Questions This Source Helps Answer

What are current recommendations for TMS-EEG data collection and analysis? What remains unresolved?

## Related Cards

`guidelines/recommendations-good-practice.md`; `pipelines/conservative-mne-python.md`.
