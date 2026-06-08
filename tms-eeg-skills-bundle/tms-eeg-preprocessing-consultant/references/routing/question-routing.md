---
type: routing-card
id: question-routing
title: TMS-EEG Preprocessing Question Routing
tags:
  - routing
  - preprocessing
---

## Route By User Intent

| User asks about... | Load first | Also load |
|---|---|---|
| First-pass TEP/GMFA/LMFP preprocessing in Python | `pipelines/conservative-mne-python.md` | `repos/mne-python.md`, `repos/tmseegpy.md`, `recipes/compute_teps_gmfa_lmfp.md` |
| TESA-style cleaning or two ICA passes | `pipelines/tesa-inspired-two-pass-ica.md` | `repos/tesa.md`, `artifacts/overcleaning-and-ica-risk.md` |
| MATLAB, EEGLAB, TESA, `.set` files, FastICA | `routing/code-language-selection.md` | `pipelines/tesa-inspired-two-pass-ica.md`, `recipes/tesa_matlab_preprocessing.md`, `repos/tesa.md` |
| Downsampling, resampling, aliasing, anti-aliasing, or filter ringing | `steps/downsampling-and-resampling.md` | `steps/filtering.md`, `artifacts/sampling-sync-early-artifacts.md` |
| Step order, "correct" preprocessing sequence, or pipeline comparison | `pipeline-tables/preprocessing-step-order.md` | Relevant pipeline cards, `steps/downsampling-and-resampling.md`, `steps/filtering.md`, `steps/gmfa-lmfp-computation.md` |
| Automated artifact rejection, ARTIST, or AARATEP | `pipelines/automated-artist-aaratep.md` | `repos/aaratep-pipeline.md`, `papers/wu-2018-artist.md`, `steps/automated-artifact-rejection.md` |
| TMSEEG MATLAB GUI workflow | `papers/atluri-2016-tmseeg.md` | `pipeline-tables/preprocessing-step-order.md`, `pipelines/tesa-inspired-two-pass-ica.md`, `steps/qc-plots-and-reporting.md` |
| SOUND, SSP, SIR, source-space signal cleaning | `pipelines/sound-ssp-sir-enhanced.md` | `repos/pytep-sound-ssp-sir.md`, `steps/sound-cleaning.md`, `steps/ssp-sir-cleaning.md` |
| TEP modeling, recurrent network dynamics, PyTepFit | `pipelines/tepfit-network-modeling-analysis.md` | `repos/pytepfit.md`, `papers/momi-2023-recurrent-network-dynamics.md`, `steps/tepfit-modeling-analysis.md` |
| Immediate TEPs, i-TEPs, early responses | `pipelines/itep-early-response-analysis.md` | `artifacts/early-pulse-residual-risk.md`, `artifacts/lead-configuration-early-artifacts.md`, `artifacts/sampling-sync-early-artifacts.md` |
| Good practice, recommendations, acquisition QC | `guidelines/recommendations-good-practice.md` | `papers/hernandez-pavon-2023-recommendations-open-issues.md` |
| DLPFC TEP reliability, excitability mapping, or DLPFC muscle artifact | `papers/gogulski-2024-dlpfc-tep-reliability.md` | `papers/gogulski-2024-dlpfc-excitability-mapping.md`, `papers/gogulski-2025-dlpfc-methodological-considerations.md`, `papers/kabir-2024-large-scale-brain-state-dynamics.md`, `papers/maki-2011-projecting-muscle-artifacts.md`, `steps/muscle-artifact-handling.md` |
| Sensory confounds or auditory/somatosensory controls | `artifacts/auditory-somatosensory-confounds.md` | `papers/biabani-2019-sensory-inputs.md`, `papers/gordon-2018-realistic-sham.md` |
| Natural frequencies, oscillatory TEPs, effective connectivity | `papers/rosanova-2009-natural-frequencies.md` | `papers/massimini-2005-breakdown-effective-connectivity-sleep.md`, `papers/casali-2012-consciousness-effective-connectivity.md` |
| Only code | `routing/code-language-selection.md` | Relevant pipeline card, `recipes/*.md`, repo card, software lookup policy |
| Beginner explanation | Relevant pipeline card | Step cards named by that pipeline |
| Artifact risk or interpretation caveat | Relevant artifact card | Related paper cards |
| Context7 unavailable | `routing/context7-or-github-fallback.md` | Relevant repo card |

## Required Metadata Checklist

Before giving a definitive pipeline, try to obtain or mark as placeholder:

- data format and reader: FIF, BrainVision, EEGLAB, BIDS, EDF, other
- continuous or epoched data
- sampling rate and hardware synchronization details
- event channel or pulse timing source
- stimulation target and coil orientation if known
- analysis goal: TEP, GMFA, LMFP, i-TEP, PCIst, connectivity, source analysis
- active, sham, auditory, somatosensory, or control conditions
- channel montage, reference, electrode/lead configuration
- known artifact profile and rejected trials

## Response Mode Routing

- `learning mode`: explain each step in practical language, with risks and QC.
- `code-engineer mode`: produce concise code templates and minimal rationale.
- `default`: give an ordered pipeline, brief rationale, code direction, QC checks, caveats.

## Out Of Scope For This Skill

SlicerTMS, neuronavigation, E-field visualization, and 3D Slicer troubleshooting belong in a future experiment-planning/neuronavigation skill, not the preprocessing consultant. Mention this boundary when users ask about SlicerTMS from this skill.
