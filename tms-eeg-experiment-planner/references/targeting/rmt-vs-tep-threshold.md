---
type: targeting-card
id: rmt-vs-tep-threshold
title: RMT Versus TEP Threshold
tags:
  - rmt
  - tep-threshold
  - intensity
---

## Purpose

Help the agent reason about stimulation intensity when RMT, E-field dose, online TEP amplitude, and artifact ceiling may disagree.

## Key Distinction

RMT indexes corticospinal excitability for motor cortex. TEP quality indexes EEG-observable target response and artifact burden. They are related only indirectly and may diverge, especially outside M1.

## Planning Rules

- Use RMT as a safety and starting reference, not as the sole intensity rule for non-motor TMS-EEG.
- For non-motor targets, adjust intensity based on online TEP visibility, artifact profile, discomfort, and safety limits.
- Treat early local TEP amplitude as a QC variable. Local notes suggest about `8-10 uV` peak-to-peak in `8-50 ms` near the coil as a practical acquisition target, not a universal threshold.
- If increasing intensity improves late N100/P200 but not early local response, suspect sensory contamination.
- Retune auditory masking whenever intensity changes.

## Output Rule

Report intensity as a decision chain: initial RMT/E-field estimate, online TEP response, artifact/discomfort ceiling, and final locked value.

## Sources

Local good-practice note; rt-TEP tool paper; DLPFC reliability/excitability cards in preprocessing skill.
