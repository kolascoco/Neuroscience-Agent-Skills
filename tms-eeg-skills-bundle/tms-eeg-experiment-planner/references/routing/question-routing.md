---
type: routing-card
id: question-routing
title: TMS-EEG Experiment Planning Question Routing
tags:
  - routing
  - experiment-planning
---

## Route By User Intent

| User asks about... | Load first | Also load |
|---|---|---|
| full experiment plan or protocol | `design/study-design-checklist.md` | `../templates/experiment-protocol-template.md`, `guidelines/recommendations-good-practice.md`, target-risk routing |
| session procedure or day-of checklist | `design/session-workflow.md` | `../templates/session-checklist.md`, `guidelines/recommendations-good-practice.md`, `online-qc/rt-tep-monitoring.md` |
| target selection or artifact risk | `routing/target-risk-routing.md` | relevant `targets/*.md`, `artifacts/target-specific-artifact-risks.md` |
| tactile feeling or somatosensory TMS-EEG | `targets/somatosensory-s1.md` | `guidelines/tactile-feeling-local-notes.md`, `design/sham-and-sensory-controls.md`, `papers/hernandez-pavon-2023-recommendations-open-issues.md` |
| coil orientation or coil position | `targeting/coil-orientation-and-intensity.md` | coil orientation paper cards |
| RMT, intensity, or TEP threshold | `targeting/rmt-vs-tep-threshold.md` | `online-qc/rt-tep-monitoring.md` |
| sham, click masking, or sensory controls | `design/sham-and-sensory-controls.md` | `papers/gordon-2018-realistic-sham.md`, `papers/gordon-2026-somatosensory-inputs.md`, `papers/grasin-2019-realistic-sham.md` |
| neuronavigation or E-field simulation | `targeting/neuronavigation-and-efield.md` | `repos/simnibs.md`, `repos/nexstim-efield-navigation.md`, `repos/slicertms.md`, `repos/navinibs.md`, `papers/hernandez-pavon-2023-recommendations-open-issues.md` |
| real-time TEP monitoring | `online-qc/rt-tep-monitoring.md` | `papers/casarotto-2022-rt-tep-tool.md` |
| i-TEP acquisition | `online-qc/itep-acquisition-practice.md` | `papers/beck-2024-iteps.md`, `artifacts/channel-lead-preparation-decay-avoidance.md` |
| channel prep, decay, recharge, lead orientation | `artifacts/channel-lead-preparation-decay-avoidance.md` | `papers/lankinen-2026-lead-configuration-early-artifacts.md` |
| what an artifact looks like | `artifact-appearance/tms-pulse-artifact-appearance.md` | `artifact-appearance/decay-artifact-appearance.md`, `artifact-appearance/muscle-artifact-appearance.md`, `papers/stango-2025-high-frequency-sampling-artifacts.md` |
| TMS pulse artifact appearance | `artifact-appearance/tms-pulse-artifact-appearance.md` | `papers/stango-2025-high-frequency-sampling-artifacts.md` |
| decay artifact appearance | `artifact-appearance/decay-artifact-appearance.md` | `artifacts/channel-lead-preparation-decay-avoidance.md`, `papers/stango-2025-high-frequency-sampling-artifacts.md` |
| muscle artifact appearance | `artifact-appearance/muscle-artifact-appearance.md` | `artifacts/target-specific-artifact-risks.md`, target-risk routing |
| state-dependent or closed-loop design | `design/state-dependent-closed-loop.md` | `papers/wischnewski-2024-real-time-tms-eeg.md`, `papers/stefanou-2019-brain-state-dependent.md` |
| methods/preregistration text | `design/study-design-checklist.md` | `../templates/preregistration-methods-template.md`, `guidelines/recommendations-good-practice.md` |

## Required Metadata

- research question and target network
- stimulation target and backup target
- coil type, orientation plan, neuronavigation plan
- intensity basis: RMT, E-field, online TEP, i-TEP, or safety maximum
- EEG system, sampling rate, channels, electrode type, lead/cable layout
- sham/control conditions and masking
- trial count, blocks, inter-pulse interval, task/rest condition
- online QC tools and go/no-go criteria
- primary analysis endpoint: TEP, i-TEP, GMFA/LMFP, source TEP, behavior, state-dependent response
