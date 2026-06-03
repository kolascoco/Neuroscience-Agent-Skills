---
type: design-card
id: state-dependent-closed-loop
title: State-Dependent And Closed-Loop TMS-EEG Design
tags:
  - state-dependent
  - closed-loop
  - real-time
---

## Purpose

Plan experiments where stimulation timing or adaptation depends on EEG-defined brain state.

## Design Distinctions

- Trigger function: when to deliver the pulse.
- Update function: how stimulation parameters adapt based on measured effects.

## Candidate State Markers

- motor mu phase or power
- individualized spatial-spectral-temporal state decoding
- functional connectivity state
- microstates or global pre-stimulus state
- target/network-specific oscillatory state

## Methodological Rules

- Do not assume one phase/state is optimal across targets or populations.
- Use physiologically meaningful state markers and verify signal source.
- For motor cortex, predictive mu signal may not originate from the stimulation target itself.
- Closed-loop precision requires latency, filtering, artifact, and trigger validation.

## Output Rule

For a state-dependent protocol, return target state, signal source, detection algorithm, trigger latency budget, validation method, sham/control plan, and failure modes.

## Sources

Wischnewski et al. 2024; Stefanou et al. 2019; Zrenner et al. 2018; Gordon et al. 2021; local good-practice note.
