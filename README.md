# Neuroscience Agent Skills

Reusable AI agent skills for neuroscience research, learning, dataset discovery, and analysis workflows.

This repository is a growing toolkit for agents that need to work fluently with neuroscience resources: public datasets, anatomy references, imaging archives, connectomics tools, lab catalogs, and eventually analysis pipelines.

## What This Is

Neuroscience work often lives across scattered APIs, lab pages, file portals, atlas projects, and educational resources. These skills give an AI agent practical instructions for finding the right resource, querying it correctly, preserving citations and license notes, and returning useful structured results instead of vague links.

Think of this repo as a field kit for research agents.

## Available Skills

| Skill | What it helps with | Status |
|---|---|---|
| `neuroscience-database-lookup` | Search public neuroscience datasets and educational anatomy resources across OpenNeuro, OSF, Figshare, Dryad, Harvard Dataverse, Science Data Bank, Zenodo, TDBRAIN, HCP, BRAVA, NITRC, Oliva Lab, visual stimulus/eye-tracking resources, TEMCA2/FAFB, and BrainFacts 3D Brain. | Ready |
| `tms-eeg-skills-bundle/tms-eeg-experiment-planner` | Design TMS-EEG studies before data collection: target choice, coil orientation/intensity, RMT versus TEP threshold, sham/sensory controls, rt-TEP monitoring, acquisition QC, neuronavigation, E-field modeling, SlicerTMS, and session checklists. | Draft |
| `tms-eeg-skills-bundle/tms-eeg-preprocessing-consultant` | Plan, explain, and code TMS-EEG preprocessing workflows for TEP/GMFA/LMFP and immediate TEP/i-TEP analysis, with Context7-first/GitHub-fallback software lookup and artifact-aware QC cards. | Draft |

## First Skill: Neuroscience Database Lookup

The included `neuroscience-database-lookup` skill helps agents retrieve and summarize resources such as:

- BIDS datasets from OpenNeuro
- EEG, MEG, fMRI, MRI, PET, iEEG, and MRA datasets
- General repository search across Figshare, Dryad, Harvard Dataverse, Science Data Bank, and Zenodo
- Data descriptor article fallback through sources such as Scientific Data when a direct dataset link cannot be found
- Clinical EEG resources including TDBRAIN, MSU EEG links, and Parkinson/cognition datasets from Narayanan Lab
- Human Connectome Project access routes and connectomics resources
- OSF neuroscience projects, files, registrations, and protocols
- Brain arterial reconstruction and vascular morphology resources
- Human magnetic resonance angiography atlas data
- Visual cognition and neuroimaging datasets from the Oliva Lab
- Standardized visual stimuli, emotional face/task materials, image memorability data, and eye-tracking/fixation datasets
- Drosophila EM/connectomics resources including TEMCA2/FAFB
- BrainFacts 3D Brain anatomy pages for teaching and region lookup

The skill emphasizes exact source links, API endpoints, access notes, licensing, citations, clear output formatting, and a compact "Big Data Fit" check for volume, variety, velocity, veracity, and scientific value.

## Repository Layout

```text
.
├── README.md
├── .gitignore
├── neuroscience-database-lookup/
│   ├── SKILL.md
│   └── references/
│       ├── brainfacts-3d-brain.md
│       ├── brava.md
│       ├── clinical-eeg-and-big-data.md
│       ├── general-data-repositories-and-data-articles.md
│       ├── human-connectome-project.md
│       ├── nitrc-icbmmra.md
│       ├── oliva-lab.md
│       ├── openneuro.md
│       ├── osf.md
│       ├── temca2-fafb.md
│       └── visual-stimulus-and-eyetracking.md
└── tms-eeg-skills-bundle/
    ├── README.md
    ├── tms-eeg-experiment-planner/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    └── tms-eeg-preprocessing-consultant/
        ├── SKILL.md
        ├── assets/
        ├── recipes/
        └── references/
```

## Roadmap

Future skills could include:

- `neuroimaging-bids-qc` - inspect BIDS datasets, metadata, and common quality-control signals
- `eeg-analysis-helper` - guide preprocessing, event handling, referencing, filtering, and artifact checks
- `fmri-methods-assistant` - support design matrices, contrasts, confounds, and reporting conventions
- `connectomics-resource-finder` - navigate connectome datasets, viewers, skeletons, and annotations
- `neuroanatomy-tutor` - explain structures, pathways, functions, and lesion associations
- `paper-to-protocol` - convert neuroscience papers into reproducible experiment or analysis checklists
- `tms-eeg-interpretation-critic` - critique TEP/GMFA/LMFP/PCIst claims and separate physiological interpretation from sensory/artifact confounds

## Design Principles

- Prefer primary sources, official APIs, and direct dataset pages.
- Preserve citations, licenses, access restrictions, and download instructions.
- Return structured, verifiable results instead of unsupported summaries.
- Keep each skill narrow enough to be reliable, but rich enough to be useful in real research workflows.
- Make neuroscience tooling easier to use without hiding the scientific caveats.

## Contributing

Add each new skill as its own directory with a `SKILL.md` file and any supporting references in a local `references/` folder. Domain-specific families, such as TMS-EEG, can be grouped in a bundle folder with a bundle README. Keep examples concrete, cite source URLs where possible, and include error-recovery notes for fragile APIs or older academic websites.

## License

This project is licensed under the MIT License.
