---
type: repo-card
id: nexstim-efield-navigation
title: Nexstim NBS / SmartFocus nTMS E-Field Navigation
source_url: https://www.nexstim.com/healthcare-professionals/technology/page
additional_urls:
  - https://www.nexstim.com/research/tms-eeg
  - https://www.nexstim.com/healthcare-professionals/how-smartfocusr-tms-works
tags:
  - nexstim
  - eximia
  - nbs
  - smartfocus
  - neuronavigation
  - efield
  - online-efield
---

## Role In The Skill

Use this card when a user asks about commercial neuronavigation systems with on-board or real-time E-field visualization, especially Nexstim systems historically referred to in older literature as Eximia/eXimia and currently described publicly as NBS / SmartFocus nTMS.

## Software Lookup Policy

1. Prefer current official Nexstim product and technology pages for system names, regulatory claims, and public feature descriptions.
2. Treat Nexstim as a commercial clinical/research system, not an open-source software library.
3. Do not invent internal algorithm details, export formats, or API capabilities unless the user provides manuals or the source is checked.
4. When the user says "eXima", map this cautiously to older Nexstim Eximia/eXimia terminology and clarify current naming as needed.

## What The Agent Should Reuse

- Nexstim describes E-field navigation as visualizing the location, orientation, and magnitude of the maximum stimulating E-field induced by the TMS coil.
- The public technology page describes a multi-sphere model, based on mathematically modeling the brain as more than 40,000 spheres, rather than a single-sphere line-navigation approximation.
- The system displays the maximum induced E-field on a 3D rendering built from the participant's MRI.
- Nexstim describes dynamic recalculation of E-field location/orientation as the operator moves, turns, or tilts the coil.
- Public TMS-EEG material emphasizes that E-field navigated TMS can support repeatability, precision, and reproducibility for TMS-EEG measurements.

## Workflow Concepts

For experiment planning, Nexstim-type on-board E-field navigation is different from offline finite-element planning:

| Use Case | Nexstim NBS / SmartFocus | SimNIBS |
|---|---|---|
| Primary role | real-time/on-board E-field guided neuronavigation during stimulation | offline individualized E-field simulation, dose planning, and coil optimization |
| Operator feedback | live coil pose and estimated E-field location/orientation/magnitude | precomputed or scripted simulation outputs |
| Practical value | repeatable stimulation delivery and online coil adjustment | comparing targets/orientations/dose before acquisition |
| Caveat | commercial system; model details and exports may be system-specific | requires MRI/head model quality and simulation setup |

## Planning Use

When a lab has Nexstim:

- Ask whether the system is NBS, SmartFocus nTMS, or older Eximia/eXimia.
- Ask whether individual MRI, coil pose, target coordinates, E-field magnitude/orientation, and registration quality can be saved/exported.
- Use on-board E-field feedback to document stimulation location and orientation during setup and blocks.
- Combine on-board E-field navigation with online TEP/artifact QC; E-field navigation does not prove cortical TEP quality.
- For repeated sessions, require saved target, coil orientation/current direction, E-field estimate, and tolerance/deviation criteria.

## Reporting Recommendations

Report:

- Nexstim system/version if available.
- MRI-based target definition and registration procedure.
- Coil model and stimulator settings.
- Estimated maximum E-field location, orientation, and magnitude if available.
- Coil pose deviation/tolerance across trials or blocks.
- Whether E-field navigation was used for target selection, dose adjustment, online maintenance, or only documentation.

## Failure Modes

- Treating the displayed maximum E-field as proof of physiological engagement.
- Mixing public Nexstim descriptions with SimNIBS/FEM assumptions without noting model differences.
- Assuming old Eximia/eXimia terminology and current NBS/SmartFocus features are identical.
- Reporting "neuronavigation" without specifying whether it was line-navigation, coil-position navigation, or E-field navigation.
- Ignoring TMS-EEG artifact and sensory-control checks because navigation appears precise.

## Related Cards

- `references/targeting/neuronavigation-and-efield.md`
- `references/repos/simnibs.md`
- `references/repos/navinibs.md`
- `references/online-qc/rt-tep-monitoring.md`
