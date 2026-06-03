---
type: paper-card
id: momi-2023-recurrent-network-dynamics
title: TMS-EEG evoked responses are driven by recurrent large-scale network dynamics
year: 2023
authors: Momi, Wang, Griffiths
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/elife-83232-v1.pdf
doi: 10.7554/eLife.83232
tags:
  - pipeline:tepfit
  - model:jansen-rit
  - model:connectome
  - model:recurrent-network
  - metric:tep
use_for:
  - model-aware TEP interpretation
  - local versus recurrent dynamics
  - PyTepFit analysis
confidence: seed-card
---

## Why This Matters For The Agent

This paper anchors the PyTepFit analysis branch and helps the agent discuss TEPs as possible mixtures of local reverberatory activity and recurrent large-scale network feedback.

## Key Methods

The paper combines source-localized TMS-EEG analyses and whole-brain connectome-based computational modeling. The abstract reports that recurrent network feedback begins to drive TEP responses from about 100 ms post-stimulation, with earlier components attributed to local reverberatory activity within the stimulated region.

## Practical Recommendations

Use after preprocessing/QC when the user asks what TEP components may reflect mechanistically. Keep artifact, sensory, and preprocessing caveats separate from model interpretation.

## Agent Rules Extracted

Do not interpret late TEP components as purely local. Do not interpret model-derived excitability/inhibition parameters as directly measured physiology without caveats.

## Claims To Avoid

Do not use this paper to justify preprocessing choices. Do not claim that all post-100 ms activity is recurrent in every dataset or target without matching analysis.

## Questions This Source Helps Answer

How can cleaned TEPs be interpreted through recurrent network dynamics? What is PyTepFit for? How might local and network contributions differ over latency?

## Related Cards

`repos/pytepfit.md`; `pipelines/tepfit-network-modeling-analysis.md`; `steps/tepfit-modeling-analysis.md`.
