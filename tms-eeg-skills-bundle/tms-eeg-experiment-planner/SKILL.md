---
name: tms-eeg-experiment-planner
description: Design and troubleshoot TMS-EEG experiments before data collection. Use for target choice, coil position/orientation, stimulation intensity, RMT versus TEP-threshold reasoning, trial count, sham/control design, auditory and somatosensory masking, online rt-TEP monitoring, acquisition QC, channel/lead preparation, neuronavigation, SimNIBS/Nexstim/SlicerTMS/NaviNIBS planning, and i-TEP practice.
metadata:
  skill-author: local
---

# TMS-EEG Experiment Planner

Use this skill when a user asks how to design, prepare, or run a TMS-EEG experiment before preprocessing. The skill focuses on preventing bad datasets: target selection, coil setup, intensity, control conditions, online QC, artifact prevention, and session checklists.

## Core Workflow

1. **Classify the planning question** with `references/routing/question-routing.md`.
2. **Collect design metadata**: scientific question, target, population, TMS protocol, coil, neuronavigation/E-field plan, EEG system, target TEP components, sham/control design, masking, trial count, safety constraints, and analysis endpoint.
3. **Load target-risk card** from `references/routing/target-risk-routing.md` when target is known.
4. **Load relevant planning cards** from `references/design/`, `references/targeting/`, `references/online-qc/`, and `references/artifacts/`.
5. **Load the good-practice card** (`references/guidelines/recommendations-good-practice.md`) for practical setup questions, go/no-go decisions, or session checklists.
6. **Use repo cards** for software/tooling context: SimNIBS, Nexstim NBS/SmartFocus/Eximia-style E-field navigation, SlicerTMS, NaviNIBS, rt-TEP, and related navigation/E-field workflows.
7. **Return a session-ready plan**: protocol decisions, risks, online QC steps, go/no-go criteria, and a checklist.

## Planning Branches

- Study/session design: `references/design/study-design-checklist.md`
- Trial count/reliability: `references/design/trial-count-and-reliability.md`
- Sham/sensory controls: `references/design/sham-and-sensory-controls.md`
- Coil orientation/intensity: `references/targeting/coil-orientation-and-intensity.md`
- RMT versus TEP threshold: `references/targeting/rmt-vs-tep-threshold.md`
- Neuronavigation/E-field: `references/targeting/neuronavigation-and-efield.md`
- Online rt-TEP QC: `references/online-qc/rt-tep-monitoring.md`
- i-TEP practice: `references/online-qc/itep-acquisition-practice.md`
- Channel/lead preparation: `references/artifacts/channel-lead-preparation-decay-avoidance.md`
- Artifact appearance triage: `references/artifact-appearance/`
- Practical good-practice anchor: `references/guidelines/recommendations-good-practice.md`
- Protocol template: `templates/experiment-protocol-template.md`
- Session checklist template: `templates/session-checklist.md`
- Preregistration/methods template: `templates/preregistration-methods-template.md`

## Hard Rules

- Do not treat RMT or fixed percentage of RMT as sufficient for non-motor TMS-EEG dosing.
- Do not optimize only anatomical target; optimize for target engagement plus artifact profile and online TEP quality.
- Do not promise preprocessing can recover data dominated by pulse, decay, discharge, muscle, or sensory artifacts.
- When asked what an artifact looks like, separate appearance heuristics from interpretation and load artifact-appearance cards before making a physiological claim.
- For i-TEPs, require high temporal precision, online artifact checks, lead-configuration awareness, and explicit pulse-artifact controls.
- For DLPFC/frontal/lateral targets, flag muscle and sensory confounds early.
- For tactile-feeling or somatosensory questions, separate cortical target response, scalp sensation, auditory/somatosensory PEPs, and subjective report.
- For software/tooling questions, use Context7 or official/GitHub fallback sources when current APIs matter.
