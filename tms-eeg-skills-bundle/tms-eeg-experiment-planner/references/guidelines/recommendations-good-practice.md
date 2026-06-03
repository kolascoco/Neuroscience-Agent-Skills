---
type: guideline-card
id: recommendations-good-practice
title: Recommendations, Instructions, And Good Practice
source_file: ../../../../TMS-EEG-artifacts/Recommendations, instructions, and good practice.md
tags:
  - good-practice
  - experiment-planning
  - rt-tep
  - artifacts
  - masking
  - i-tep
use_for:
  - designing a session before acquisition
  - deciding whether anatomy, RMT, online TEPs, and artifact risk agree
  - writing practical setup checklists
confidence: working-note
---

## Why This Matters For The Agent

This local note is the most practice-facing source in the experiment-planning skill. It turns the planner away from purely anatomical targeting and toward a session design that tests whether the planned setup produces usable TEPs before full acquisition.

Use it as the default practical anchor when the user asks how to choose target, orientation, intensity, online monitoring, masking, trial count, or go/no-go criteria.

## Core Planning Rules

- Treat neuronavigation target, coil orientation, intensity, online TEP visibility, and artifact profile as a coupled setup problem.
- Do not rely on fixed 45-degree orientation or fixed percent RMT when the target is non-motor or artifact-prone.
- Use online TEP monitoring before formal acquisition whenever possible.
- Use small setup averages, often around 10-30 trials, to inspect early local responses and artifact profile.
- Treat early local TEP amplitude as a setup and QC variable, not as proof of pure cortical activation.
- If early local responses are weak and late N100/P200 dominates, consider sensory contamination, target mismatch, or insufficient effective stimulation.
- Tune masking and scalp-contact controls after changing intensity, coil orientation, foam, or target.
- For i-TEP work, require higher sampling, synchronized stimulation, explicit artifact windows, lead-configuration documentation, and conservative interpretation.

## Target And Artifact Practicalities

- Frontal, lateral frontal, temporal, inferior parietal, and facially proximate targets should be flagged for craniofacial muscle and sensory confounds.
- Superior parietal targets may be comparatively favorable for low-muscle setups, but still require online inspection.
- Occipital targets may produce strong responses and visual/sensory confounds; plan controls accordingly.
- For M1, distinguish motor thresholding for stimulation safety/calibration from TEP thresholding for EEG response quality.
- For i-TEP acquisition, small changes in coil position, current direction, and cable layout can make the difference between a plausible early response and scalp artifact.

## Channel And Lead Setup Rules

- Before recording, inspect impedance, gel bridges, loose electrodes, cable loops, cable tension, and electrode-cap fit under and around the coil.
- Orient wires approximately perpendicular to the coil handle or expected induced artifact direction when feasible, and avoid cable slack near the coil.
- If decay artifacts appear online, check electrode contact, wire routing, amplifier recovery, recharge timing, and synchronization before assuming preprocessing can fix it.
- Do not plan a session that depends on offline cleaning to rescue obvious pulse/recharge/decay artifacts.

## Online QC Rules

- Inspect raw traces, pulse artifact, recharge artifact, decay, early muscle, auditory/somatosensory responses, trial rejection rate, and online average topography.
- Save setup screenshots or notes for target coordinates, coil orientation, intensity, pulse timing, masking settings, and online TEP quality.
- Define a go/no-go criterion before the main block: for example, stable early local response without unacceptable pulse decay or muscle contamination.
- Use online TEPs as an optimization signal, but do not overfit to a noisy 10-30 trial preview.

## Reporting Requirements

The agent should ask the user to report:

- target definition and coordinate system
- coil model, orientation, current direction, and handle angle
- stimulation intensity and whether it is based on RMT, E-field, online TEP threshold, or another rule
- trial count per condition and expected usable trials after rejection
- sham/control condition, masking method, foam/spacer setup, and sensory ratings if available
- EEG amplifier, sampling frequency, synchronization method, impedance/contact policy, and lead routing
- online QC procedure and go/no-go criteria
- artifact handling plan for pulse, recharge, decay, muscle, auditory, somatosensory, and overcleaning risk

## Claims To Avoid

- Do not claim that RMT-normalized intensity guarantees equivalent cortical activation at non-motor targets.
- Do not claim that visible early TEPs are automatically cortical.
- Do not claim that good neuronavigation removes the need for online artifact inspection.
- Do not claim that sham alone controls all auditory, somatosensory, expectancy, and muscle confounds.

## Related Cards

- `references/targeting/rmt-vs-tep-threshold.md`
- `references/targeting/coil-orientation-and-intensity.md`
- `references/online-qc/rt-tep-monitoring.md`
- `references/online-qc/online-artifact-checklist.md`
- `references/artifacts/channel-lead-preparation-decay-avoidance.md`
- `references/design/sham-and-sensory-controls.md`
- `references/online-qc/itep-acquisition-practice.md`
