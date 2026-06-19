---
type: article-scheme
id: tms-eeg-skills-bundle-article-ready-scheme
title: TMS-EEG Skills Bundle Article-Ready Scheme
tags:
  - tms-eeg
  - skill-bundle
  - experiment-planning
  - preprocessing
  - skill-architecture
---

# TMS-EEG Skills Bundle

## Bundle Structure

```text
tms-eeg-skills-bundle/
├── README.md
├── assets/
│   └── diagrams/
│       ├── bundle-structure.svg
│       ├── bundle-knowledge-layers.svg
│       ├── bundle-functional-branches.svg
│       ├── bundle-runtime-block-logic.svg
│       └── bundle-lifecycle-routing.svg
├── tms-eeg-experiment-planner/        # before acquisition
│   ├── SKILL.md
│   ├── references/
│   │   ├── routing/              (2)
│   │   ├── design/               (5)
│   │   ├── targeting/            (3)
│   │   ├── targets/              (6)
│   │   ├── online-qc/            (3)
│   │   ├── artifacts/            (2)
│   │   ├── artifact-appearance/  (3)
│   │   ├── repos/                (5)
│   │   ├── papers/              (13)
│   │   └── guidelines/           (2)
│   └── templates/                (3)
└── tms-eeg-preprocessing-consultant/  # after acquisition
    ├── SKILL.md
    ├── references/
    │   ├── routing/              (5)
    │   ├── pipelines/            (6)
    │   ├── steps/               (23)
    │   ├── artifacts/           (10)
    │   ├── repos/                (7)
    │   ├── papers/              (33)
    │   ├── guidelines/           (2)
    │   ├── extended-digests/     (2)
    │   └── pipeline-tables/      (3)
    ├── recipes/                 (10)
    └── assets/
```

Card counts are approximate and grow as the corpus expands.

SVG version: `bundle-structure.svg`

## Short Description

The `tms-eeg-skills-bundle` is a modular AI-agent knowledge system for TMS-EEG work across the full study lifecycle. It keeps pre-acquisition experiment planning and post-acquisition preprocessing as separate sub-skills, while preserving a shared methodological logic: source-grounded cards, explicit routing, artifact-aware caveats, software lookup policies, and practical templates.

## Knowledge Layers

```mermaid
flowchart TD
    A["User intent"] --> B["Bundle routing"]
    B --> C["Experiment planner"]
    B --> D["Preprocessing consultant"]
    C --> E["Design, targeting, online QC, templates"]
    D --> F["Pipelines, steps, artifacts, recipes"]
    E --> G["Paper, guideline, repo cards"]
    F --> G
    G --> H["Context7 or GitHub fallback for software"]
    G --> I["Source-grounded methodological caveats"]
    H --> J["Session plan, methods text, code, QC"]
    I --> J
```

SVG version: `bundle-knowledge-layers.svg`

## Functional Branches

```mermaid
flowchart LR
    A["TMS-EEG Skills Bundle"] --> B["Experiment design"]
    A --> C["Targeting and E-field planning"]
    A --> D["Sham and sensory controls"]
    A --> E["Online rt-TEP and acquisition QC"]
    A --> F["Preprocessing pipeline selection"]
    A --> G["Artifact cleaning and appearance triage"]
    A --> H["TEP, GMFA, LMFP, i-TEP analysis"]
    A --> I["Python/MNE and MATLAB/TESA code"]
```

SVG version: `bundle-functional-branches.svg`

## Runtime Block Logic

```mermaid
flowchart TD
    A["User question"] --> B["Classify stage"]
    B --> C["Before acquisition"]
    B --> D["After acquisition"]
    B --> E["Shared or ambiguous"]
    C --> F["Load experiment-planner cards"]
    D --> G["Load preprocessing-consultant cards"]
    E --> H["Load both when needed"]
    F --> I["Return protocol, checklist, QC, caveats"]
    G --> J["Return pipeline, code, QC, caveats"]
    H --> K["Return integrated plan"]
```

SVG version: `bundle-runtime-block-logic.svg`

## Design Principle

The bundle separates the lifecycle of TMS-EEG work into two agent states:

| State | Sub-skill | Main Question |
|---|---|---|
| Before acquisition | `tms-eeg-experiment-planner` | How do we design the session so the data can answer the question? |
| After acquisition | `tms-eeg-preprocessing-consultant` | How do we clean, quantify, code, and interpret the acquired data cautiously? |

This division prevents a common failure mode: treating preprocessing as a rescue operation for avoidable acquisition problems. The planner emphasizes target choice, coil orientation, stimulation intensity, sham/control design, online rt-TEP monitoring, channel preparation, and artifact prevention. The preprocessing consultant emphasizes pipeline choice, pulse/decay/muscle/sensory artifact handling, TEP/GMFA/LMFP/i-TEP computation, code generation, and QC reporting.

## Shared Methodological Rules

- Do not treat RMT or fixed percent RMT as sufficient for non-motor TMS-EEG dosing.
- Do not treat TEP, GMFA, LMFP, or i-TEP amplitude as pure cortical excitability.
- Do not assume preprocessing can recover data dominated by acquisition artifacts.
- For early and immediate TEPs, explicitly separate TMS-pulse artifact, decay/back-to-baseline recovery, muscle artifact, lead configuration, sampling frequency, synchronization, and controls.
- For software-specific code, use Context7 first when available; otherwise inspect the official or GitHub fallback source.
- Prefer compact cards and templates at runtime; keep raw articles as provenance rather than primary runtime context.

## One-Sentence Summary

The TMS-EEG skills bundle turns experiment-planning knowledge, preprocessing workflows, artifact diagnostics, software ecosystems, and methodological literature into a routed AI-agent expert system for designing and analyzing TMS-EEG studies with explicit caveats.
