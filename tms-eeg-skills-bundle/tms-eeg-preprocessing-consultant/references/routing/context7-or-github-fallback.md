---
type: routing-card
id: context7-or-github-fallback
title: Context7 Or GitHub Fallback Policy
tags:
  - routing
  - software-lookup
  - context7
  - github
---

## Policy

1. If Context7 is available, resolve/query the target library for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable, incomplete, or missing the library, use the GitHub fallback URL in the relevant repo card.
3. Prefer official docs, README files, examples, tutorials, and source files from the fallback repo.
4. Do not invent function signatures. If an API cannot be verified, write pseudocode or state exactly which source should be checked.
5. Keep local skill cards focused on methodological role, workflow order, assumptions, caveats, and QC.

## Libraries

| Library/repo | Preferred lookup | Fallback |
|---|---|---|
| MNE-Python | Context7 `MNE-Python` | `https://github.com/mne-tools/mne-python` |
| tmseegpy | Context7 `tmseegpy` | `https://github.com/LazyCyborg/tmseegpy` |
| TESA | Context7 `/nigelrogasch/tesa` | `https://github.com/nigelrogasch/TESA` |
| AARATEP Pipeline | Context7 `AARATEPPipeline` | `https://github.com/chriscline/AARATEPPipeline` |
| PyTEP-SOUND-SSP-SIR | Context7 `PyTEP-SOUND-SSP-SIR` | `https://github.com/MarcioCamposJr/PyTEP-SOUND-SSP-SIR` |
| PyTepFit | Context7 `PyTepFit` if available; no Context7 match observed on 2026-05-19 | `https://github.com/GriffithsLab/PyTepFit` |
| SimNIBS | Context7 `SimNIBS` | `https://github.com/simnibs/simnibs` |

## Code Output Rule

When writing code, separate verified API calls from dataset-specific placeholders. Use comments such as `# TODO: confirm event channel name` rather than pretending unknown metadata is known.
