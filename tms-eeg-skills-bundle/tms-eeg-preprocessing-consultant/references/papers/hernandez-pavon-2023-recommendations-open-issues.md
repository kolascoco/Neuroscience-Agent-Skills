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
confidence: high
---

## Why This Matters For The Agent

This is a central recommendations paper for TMS-EEG data collection and analysis. Use it as a high-priority citation when the user asks for best practice, reporting, acquisition, preprocessing, or open methodological issues.

## Main TEP Nature Points

TEPs are shaped by stimulation target, state, sensory inputs, artifacts, acquisition choices, and preprocessing. The agent should frame TEPs as experimentally constrained evoked responses, not direct readouts of one physiological quantity.

The paper emphasizes that TEPs are time-locked EEG responses obtained by averaging trials. They likely reflect a spatiotemporal superposition of excitatory and inhibitory postsynaptic potentials after local and network-level activation. Later components, especially beyond roughly 80 ms, can be contaminated by auditory/somatosensory responses; very early components can be contaminated by cranial muscle and residual pulse-related artifacts.

For oscillatory analyses, distinguish TMS-evoked responses that are phase-locked and survive averaging from TMS-induced activity that is related to the pulse but not necessarily phase-locked. Non-phase-locked effects require single-trial time-frequency analysis before averaging.

## Methodological Tips And Nuances

Emphasize standardized reporting, control conditions, artifact handling, timing precision, careful preprocessing order, and transparent analysis choices. Use this paper to justify asking for metadata before proposing a pipeline.

Acquisition details matter for preprocessing interpretation:

- recharge-delay control can move recharge artifacts outside the analysis window
- pulse waveform and current direction can affect artifact amplitude and TEP morphology
- coil type can change both stimulated tissue and cranial-muscle artifact risk
- TMS-compatible electrodes such as sintered Ag/AgCl pellet or C-ring electrodes are preferred over conventional EEG electrodes
- active electrodes can reduce setup time but may increase coil-to-cortex distance and may prolong decay artifacts in some setups
- higher sampling rates and appropriate amplifier filters can shorten pulse-ripple artifacts, while low anti-aliasing cutoffs can lengthen filter ripples
- neuronavigation supports reproducible coil position/orientation and can mark trials with target deviations
- channel count and electrode locations affect source/topography analysis and methods such as SOUND

## Agent Rules Extracted

- Load this card for broad "what should I do?" TMS-EEG preprocessing questions.
- Require acquisition, artifact, and control-condition details before definitive advice.
- Mention open issues rather than pretending there is one universally accepted pipeline.
- Ask for stimulator recharge delay, pulse waveform/current direction, coil type, electrode type, sampling rate, filter settings, trigger synchronization, neuronavigation, reference, and channel count when the question depends on early latency, source analysis, or reproducibility.
- For time-frequency questions, ask whether the user wants phase-locked evoked activity, non-phase-locked induced activity, or mixed TRSP-style measures.

## Claims To Avoid

Do not give rigid universal parameters where the field still treats them as open or context-dependent.

Do not treat TEP peak labels, neurotransmitter mappings, or source-localized activity as self-explanatory without target, pharmacological/paradigm context, artifact controls, and preprocessing details.

## Questions This Source Helps Answer

What are current recommendations for TMS-EEG data collection and analysis? What remains unresolved?

## Related Cards

`guidelines/recommendations-good-practice.md`; `pipelines/conservative-mne-python.md`; `steps/downsampling-and-resampling.md`; `artifacts/auditory-somatosensory-confounds.md`; `artifacts/stimulation-intensity-sampling-rate-sync.md`.
