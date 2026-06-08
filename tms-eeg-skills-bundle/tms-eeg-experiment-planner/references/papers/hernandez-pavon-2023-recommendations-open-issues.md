---
type: paper-card
id: hernandez-pavon-2023-recommendations-open-issues
title: "TMS Combined With EEG: Recommendations And Open Issues For Data Collection And Analysis"
year: 2023
authors: Hernandez-Pavon JC; Veniero D; Bergmann TO; Belardinelli P; Bortoletto M; Casarotto S; Casula E; Farzan F; Fecchio M; Julkunen P; Kallioniemi E; Lioumis P; Metsomaa J; Miniussi C; Mutanen TP; Rocchi L; Rogasch NC; Shafi MM; Siebner HR; Thut G; Zrenner C; Ziemann U; Ilmoniemi RJ; and colleagues
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1935861X23016960-main.pdf
doi: 10.1016/j.brs.2023.02.009
tags:
  - recommendations
  - good-practice
  - acquisition
  - experiment-planning
  - preprocessing
  - artifacts
  - reporting
use_for:
  - pre-acquisition equipment and setup planning
  - target, coil, neuronavigation, and control-condition decisions
  - reporting checklists
  - explaining open issues in TMS-EEG methodology
confidence: high
---

## Why This Matters For The Agent

This is the central broad recommendations paper for TMS-EEG data collection and analysis. In the experiment-planner skill, use it as a high-priority source when the user asks how to design a TMS-EEG study before acquisition.

## Key Methods And Scope

The paper is an expert-panel review covering TMS-EEG preparation, equipment, acquisition, artifact correction, analysis, and interpretation. It explicitly frames many decisions as context-dependent because the field lacks one universally standardized pipeline.

## Practical Recommendations

- Plan around three equipment classes: TMS stimulator/coil, TMS-compatible EEG amplifier, and TMS-compatible electrodes.
- Prefer TMS stimulators that support recharge-delay control when post-pulse EEG windows matter.
- Consider pulse waveform and current direction as methodological variables, not interchangeable technical details.
- Use coil cooling or protocol breaks when long blocks are needed for adequate trial counts.
- Ensure reliable triggering/communication between TMS, EEG, external control, and neuronavigation.
- Use neuronavigation to maintain target, coil orientation, and angulation across trials and sessions.
- For lesion patients, neuronavigation is especially important because stimulating damaged tissue may fail to evoke interpretable responses.
- Use TMS-compatible electrodes, commonly sintered Ag/AgCl pellet or C-ring designs; avoid conventional electrodes that can heat or induce strong eddy-current artifacts.
- Consider that active electrodes can reduce setup time but may increase coil-to-cortex distance and may affect decay artifacts in some setups.
- Report reference, channel count, montage, electrode type, impedance/contact policy, and re-referencing choices.

## Planning Nuances

- Coil type may influence both focality/depth and cranial muscle activation.
- Double-cone or other coils can trigger stronger scalp/facial/neck muscle artifacts depending on target.
- Figure-of-eight coils are common, but the paper notes a lack of systematic evidence on coil effects on TMS-related EEG responses.
- Higher sampling rates and appropriate amplifier settings can shorten the visible pulse artifact, but early artifact end points are still hardware- and parameter-dependent.
- Lower anti-aliasing low-pass cutoffs can lengthen filter ripples around the TMS pulse.
- The number of EEG electrodes is not only about topographic display: higher-density recordings can improve source-level SNR and help localize channel-specific noise or cranial-muscle artifacts.

## Agent Rules Extracted

- Ask about recharge delay, pulse waveform, coil type, cooling, trigger synchronization, neuronavigation, electrode type, and sampling rate before approving a high-precision protocol.
- Do not recommend conventional EEG electrodes for TMS-EEG.
- When advising source/topography or SOUND-like methods, ask about channel density and electrode locations.
- When the user wants early TEPs, include amplifier sampling/filter settings and pulse-ripple duration in the acquisition checklist.
- Treat recommendations as best-practice guidance, not a single mandatory pipeline.

## Claims To Avoid

- Do not claim that TMS-EEG is standardized enough for one universal setup.
- Do not treat TEP peaks as pure physiological markers without sensory/artifact controls.
- Do not assume all TMS-compatible amplifiers or electrodes behave similarly around the pulse.
- Do not imply that neuronavigation alone proves physiological target engagement.

## Questions This Source Helps Answer

- What equipment do I need for TMS-EEG?
- What should I report about acquisition?
- Why does recharge delay matter?
- What electrode types are appropriate?
- Why use neuronavigation?
- How many electrodes are enough?
- Which methodological issues remain open?

## Related Cards

- `references/design/study-design-checklist.md`
- `references/targeting/neuronavigation-and-efield.md`
- `references/artifacts/channel-lead-preparation-decay-avoidance.md`
- `references/design/sham-and-sensory-controls.md`
- `references/online-qc/itep-acquisition-practice.md`
