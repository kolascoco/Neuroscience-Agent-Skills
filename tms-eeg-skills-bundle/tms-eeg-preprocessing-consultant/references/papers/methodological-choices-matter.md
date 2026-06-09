---
type: paper-card
id: methodological-choices-matter
title: Methodological choices matter in TMS-EEG preprocessing
year:
authors:
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/methodological_choices_matter_a_systematic_comparison_of_tms_eeg.pdf
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

Systematic comparison across a large set of published TMS-EEG experiments, summarizing how preprocessing and acquisition choices relate to reported TEP characteristics. Confirms a prototypical M1 TEP sequence (i-TEPs, N15, P30, N45, P60, N100, P180). Two recurring findings: (1) ICA-using pipelines are associated with systematically smaller TEP amplitudes across all peaks, not only artifact-adjacent windows; (2) active masking is associated with broadly lower TEP amplitudes, independent of ICA. Reporting of ICA-based artifact removal remains incomplete across the literature. Only a minority of studies report the number of rejected components, quantify the variance removed, or provide examples of the discarded components. However, the absolute number of rejected ICA components is not, by itself, a meaningful quality metric, as it depends strongly on data quality, signal-to-noise ratio, recording setup, and the severity of TMS-related artifacts. A more informative and transparent practice would be to demonstrate that the removed components reflect non-neural or artifact-related activity rather than stimulus-locked TMS-evoked brain responses. In particular, studies should show the time courses, spatial topographies, and spectral profiles of rejected components to verify that component removal does not eliminate physiologically meaningful TMS-evoked activity.


## Practical Recommendations

Use when explaining why QC, parameter reporting, and sensitivity checks are necessary. Quality-control procedures, preprocessing parameters, and sensitivity analyses should be reported in sufficient detail to allow readers to assess the severity and selectivity of artifact correction. Studies should be flagged when they apply potentially problematic filtering, perform ICA without reporting component-rejection criteria, or omit the retained data rank after preprocessing, as these details are essential for judging the extent of signal cleaning. When comparing TEP amplitudes across studies, it is also important to note whether ICA, noise masking, or other artifact-attenuation procedures were used, and whether residual muscle or decay artifacts may have been over-smoothed by filtering or SOUND. In particular, overly strong SSP–SIR regularization may transform residual artifact structure into activity that resembles genuine TMS-evoked neural responses, thereby complicating physiological interpretation.

## Agent Rules Extracted

Do not present a single preprocessing path as objectively correct without context. Do not attribute smaller TEP amplitudes in one study versus another to physiology before checking pipeline differences. Do not treat the raw count of rejected ICA components as a quality metric; judge component removal by evidence that the discarded components were non-neural (time course, topography, spectrum), not stimulus-locked TMS-evoked activity. Frame SSP-SIR and SOUND regularization as a trade-off: too little leaves residual artifact, too much can manufacture artifact-derived structure that mimics genuine TMS-evoked responses (see `artifacts/overcleaning-and-ica-risk.md`, `steps/ssp-sir-cleaning.md`).

## Claims To Avoid

Avoid unqualified "best pipeline" statements. Do not quote specific percentages from this card until the source PDF is confirmed.

## Questions This Source Helps Answer

How do preprocessing choices affect TMS-EEG results?

## Related Cards

`pipelines/conservative-mne-python.md`; `pipelines/sound-ssp-sir-enhanced.md`; `artifacts/overcleaning-and-ica-risk.md`; `artifacts/filter-ringing.md`; `steps/ica-component-rejection.md`; `steps/ssp-sir-cleaning.md`; `steps/qc-plots-and-reporting.md`.
