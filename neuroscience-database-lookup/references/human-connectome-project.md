# Human Connectome Project

Source:

- `https://www.humanconnectomeproject.org/`
- `https://www.humanconnectomeproject.org/data/`
- `https://www.humanconnectome.org/software/connectomedb`

Use the Human Connectome Project (HCP) for high-quality human connectomics, structural MRI, diffusion MRI, resting/task fMRI, behavioral, clinical, and demographic data.

## Best Uses

- Find multimodal human neuroimaging and connectivity datasets.
- Locate HCP Young Adult, Lifespan, Disease, or related Connectome Coordination Facility datasets.
- Retrieve or explain access steps for ConnectomeDB, the HCP Data Archive, NIH Data Archive, or LONI-hosted resources.
- Identify citation and data-use requirements for HCP-derived analyses.
- Find tool guidance for Connectome Workbench and ConnectomeDB workflows.

## Key Access Notes

- HCP data access usually requires registration and acceptance of data-use terms.
- Some data are fully de-identified/open access after agreement; restricted data require qualified investigator access.
- The HCP data page asks investigators to apply for access and notes that applications are reviewed before archive access.
- ConnectomeDB is designed for searching, filtering, browsing participant data, and downloading analysis packages.
- Connectome Workbench is used for visualization and discovery of HCP-style connectivity data.

## Access Pattern

Use the official data page first:

```text
https://www.humanconnectomeproject.org/data/
```

Then identify the relevant project:

```text
https://www.humanconnectome.org/study/hcp-young-adult/data-releases
```

For tooling:

```text
https://www.humanconnectome.org/software/connectomedb
https://www.humanconnectome.org/software/connectome-workbench
```

## Output Requirements

Return:

- HCP project name or cohort.
- Data types available: structural MRI, diffusion MRI, resting fMRI, task fMRI, behavior, clinical, restricted variables, or derivatives.
- Access route: ConnectomeDB, HCP Data Archive, LONI, NDA, Amazon S3, or DataLad if applicable.
- Whether registration, data-use agreement, or restricted-data approval is required.
- Official citation or acknowledgement instructions when the user plans publication.

## Caveats

- HCP is not one single download link. It is a family of projects and access systems.
- For subject-level data, verify the current archive and access mechanism before giving commands.
- For restricted variables, do not imply public access; point users to the official restricted-data application process.
