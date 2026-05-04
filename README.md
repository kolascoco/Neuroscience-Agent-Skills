# Neuroscience Agent Skills

Reusable AI agent skills for neuroscience research, learning, dataset discovery, and analysis workflows.

This repository is a growing toolkit for agents that need to work fluently with neuroscience resources: public datasets, anatomy references, imaging archives, connectomics tools, lab catalogs, and eventually analysis pipelines.

## What This Is

Neuroscience work often lives across scattered APIs, lab pages, file portals, atlas projects, and educational resources. These skills give an AI agent practical instructions for finding the right resource, querying it correctly, preserving citations and license notes, and returning useful structured results instead of vague links.

Think of this repo as a field kit for research agents.

## Available Skills

| Skill | What it helps with | Status |
|---|---|---|
| `neuroscience-database-lookup` | Search public neuroscience datasets and educational anatomy resources across OpenNeuro, OSF, BRAVA, NITRC, Oliva Lab, TEMCA2/FAFB, and BrainFacts 3D Brain. | Ready |

## First Skill: Neuroscience Database Lookup

The included `neuroscience-database-lookup` skill helps agents retrieve and summarize resources such as:

- BIDS datasets from OpenNeuro
- EEG, MEG, fMRI, MRI, PET, iEEG, and MRA datasets
- OSF neuroscience projects, files, registrations, and protocols
- Brain arterial reconstruction and vascular morphology resources
- Human magnetic resonance angiography atlas data
- Visual cognition and neuroimaging datasets from the Oliva Lab
- Drosophila EM/connectomics resources including TEMCA2/FAFB
- BrainFacts 3D Brain anatomy pages for teaching and region lookup

The skill emphasizes exact source links, API endpoints, access notes, licensing, citations, and clear output formatting.

## Repository Layout

```text
.
├── README.md
├── .gitignore
└── neuroscience-database-lookup/
    ├── SKILL.md
    └── references/
        ├── brainfacts-3d-brain.md
        ├── brava.md
        ├── nitrc-icbmmra.md
        ├── oliva-lab.md
        ├── openneuro.md
        ├── osf.md
        └── temca2-fafb.md
```

## Roadmap

Future skills could include:

- `neuroimaging-bids-qc` - inspect BIDS datasets, metadata, and common quality-control signals
- `eeg-analysis-helper` - guide preprocessing, event handling, referencing, filtering, and artifact checks
- `fmri-methods-assistant` - support design matrices, contrasts, confounds, and reporting conventions
- `connectomics-resource-finder` - navigate connectome datasets, viewers, skeletons, and annotations
- `neuroanatomy-tutor` - explain structures, pathways, functions, and lesion associations
- `paper-to-protocol` - convert neuroscience papers into reproducible experiment or analysis checklists

## Design Principles

- Prefer primary sources, official APIs, and direct dataset pages.
- Preserve citations, licenses, access restrictions, and download instructions.
- Return structured, verifiable results instead of unsupported summaries.
- Keep each skill narrow enough to be reliable, but rich enough to be useful in real research workflows.
- Make neuroscience tooling easier to use without hiding the scientific caveats.

## Contributing

Add each new skill as its own directory with a `SKILL.md` file and any supporting references in a local `references/` folder. Keep examples concrete, cite source URLs where possible, and include error-recovery notes for fragile APIs or older academic websites.
