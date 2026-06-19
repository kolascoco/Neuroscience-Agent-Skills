# TMS-EEG Skills Bundle

This folder groups the TMS-EEG agent skills as one methodological bundle while keeping each sub-skill separately callable.

## Included Skills

| Skill | Role |
|---|---|
| `tms-eeg-experiment-planner` | Designs TMS-EEG studies before acquisition: target, coil orientation, intensity, trial count, sensory controls, rt-TEP monitoring, acquisition QC, neuronavigation, E-field simulation, SlicerTMS/NaviNIBS, and i-TEP practice. |
| `tms-eeg-preprocessing-consultant` | Plans, explains, and codes preprocessing/TEP analysis workflows after acquisition: artifact handling, MNE/Python, MATLAB/TESA, TEPs, GMFA/LMFP, i-TEPs, SOUND/SSP-SIR, ARTIST/AARATEP, and PyTepFit-oriented reasoning. |

## Runtime Design

- Keep each sub-skill narrow enough to route reliably.
- Use the experiment planner before data collection.
- Use the preprocessing consultant after data collection or when writing preprocessing scripts.
- Share methodological concepts through parallel card formats: routing cards, method cards, artifact cards, repository cards, paper cards, and templates/recipes.
- Keep raw PDFs and article folders outside the skill bundle. Cards may preserve local provenance paths, but the agent should rely on distilled cards at runtime.

## Article Diagrams

- `assets/diagrams/article-ready-bundle-scheme.md`: article-ready text scheme with Mermaid equivalents.
- `assets/diagrams/bundle-structure.svg`: bundle folder and sub-skill structure.
- `assets/diagrams/bundle-knowledge-layers.svg`: layered knowledge architecture.
- `assets/diagrams/bundle-functional-branches.svg`: functional branches across planning and preprocessing.
- `assets/diagrams/bundle-runtime-block-logic.svg`: runtime routing/block logic.
- `assets/diagrams/bundle-lifecycle-routing.svg`: lifecycle routing of queries to each sub-skill with capability and guardrail detail.

## Future Bundle Candidates

- `tms-eeg-interpretation-critic`: critique physiological claims, sensory confounds, source claims, PCIst/complexity interpretations, and target-specific mechanisms.
- `tms-eeg-source-modeling-consultant`: head models, digitization, source localization, E-field-to-source reasoning, and reporting.
- `tms-eeg-literature-reviewer`: article digestion, evidence tables, method comparisons, and citation-ready summaries.
