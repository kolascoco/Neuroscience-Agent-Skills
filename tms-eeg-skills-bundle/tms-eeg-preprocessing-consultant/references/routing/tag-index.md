---
type: routing-card
id: tag-index
title: Controlled Tags For TMS-EEG Preprocessing Cards
tags:
  - routing
  - tags
---

## Namespaces

- `pipeline:*`: `mne`, `tesa-inspired`, `sound-ssp-sir`, `artist-aaratep`, `tepfit`, `itep`
- `step:*`: `data-intake`, `pulse-detection`, `pulse-interpolation`, `automated-rejection`, `filtering`, `ica`, `sound`, `ssp-sir`, `epoching`, `qc`
- `artifact:*`: `pulse`, `muscle`, `decay`, `recharge`, `auditory`, `somatosensory`, `lead-configuration`, `sampling-sync`
- `metric:*`: `tep`, `gmfa`, `lmfp`, `itep`, `pci`, `svd-component`
- `model:*`: `jansen-rit`, `connectome`, `recurrent-network`, `neural-mass`
- `topic:*`: `natural-frequency`, `effective-connectivity`, `reproducibility`, `neuronavigation`, `source-analysis`, `good-practice`
- `language:*`: `python`, `matlab`
- `ecosystem:*`: `mne`, `eeglab`, `tesa`, `tmseegpy`
- `target:*`: `m1`, `dlpfc`, `parietal`, `other`
- `mode:*`: `learning`, `code-engineer`, `qc`
- `caution:*`: `early-latency`, `overcleaning`, `sensory-confounds`, `causal-interpretation`, `api-unverified`

## Rule

Use tags to route context, not to decorate files. Add new tags only when they change retrieval or behavior.
