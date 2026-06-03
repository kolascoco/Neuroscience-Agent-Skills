---
type: routing-card
id: code-language-selection
title: Code Language Selection For TMS-EEG Preprocessing
tags:
  - routing
  - code
  - language:python
  - language:matlab
---

## Purpose

Choose whether the agent should write Python/MNE-style code, MATLAB/EEGLAB/TESA-style code, or both.

## Selection Rules

| User context | Prefer | Load |
|---|---|---|
| asks for Python, MNE, notebooks, BIDS, FIF, BrainVision | Python | `pipelines/conservative-mne-python.md`, Python recipes, `repos/mne-python.md` |
| asks for MATLAB, EEGLAB, TESA, `.set`, FastICA, `pop_tesa_*` | MATLAB | `pipelines/tesa-inspired-two-pass-ica.md`, `recipes/tesa_matlab_preprocessing.md`, `repos/tesa.md` |
| asks for AARATEP | MATLAB | `pipelines/automated-artist-aaratep.md`, `recipes/aaratep_matlab_skeleton.md`, `repos/aaratep-pipeline.md` |
| asks for SOUND/SSP-SIR in Python | Python | `pipelines/sound-ssp-sir-enhanced.md`, `repos/pytep-sound-ssp-sir.md` |
| asks for comparison or migration | Both | corresponding Python and MATLAB pipeline cards |

## Default

If language is unspecified, give a short choice:

- Python/MNE for general reproducible scripting and notebooks.
- MATLAB/EEGLAB/TESA for classical TMS-EEG workflows, `.set` files, TESA functions, and teaching scripts.

If the user asks for code immediately and gives `.set`/TESA clues, choose MATLAB without asking.

## MATLAB/TESA Requirements

State dependencies before code:

- MATLAB
- EEGLAB
- TESA EEGLAB plugin
- FastICA when using TESA FastICA workflows
- optional helper functions from the user's project if referenced

Use Context7 `/nigelrogasch/tesa` or TESA GitHub fallback before writing unfamiliar TESA calls.
