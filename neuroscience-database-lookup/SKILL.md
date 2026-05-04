---
name: neuroscience-database-lookup
description: Search and retrieve public neuroscience datasets and educational anatomy resources. Covers OpenNeuro BIDS datasets, OSF neuroscience projects/files, BRAVA brain arterial reconstruction data, NITRC ICBM MRA atlas data, Oliva Lab visual cognition and neuroimaging datasets, TEMCA2/FAFB fly brain EM connectomics data, and BrainFacts 3D Brain anatomy pages. Use when looking up neuroscience datasets, EEG/fMRI/MEG/MRA/EM data, visual cognition stimulus datasets, brain anatomy teaching material, or dataset download/access instructions.
metadata:
  skill-author: local
---

# Neuroscience Database Lookup

Use this skill to find, inspect, and retrieve neuroscience datasets or brain anatomy resources. It mirrors the `database-lookup` workflow, but is focused on neuroscience resources that are not all clean REST databases. Some are API-first, some are structured HTML download catalogs, and some are educational interactive sites.

## Core Workflow

1. **Understand the query** - Identify the requested data type: EEG, fMRI, MEG, MRA/NIfTI, vascular reconstructions, EM connectomics, visual cognition stimuli, OSF project files, or brain anatomy education.
2. **Select resource(s)** - Use the selection guide below. Query multiple resources when the user asks broadly.
3. **Read the reference file** - Each resource has a file in `references/` with access patterns, endpoints, examples, and limitations.
4. **Make the call or scrape the page** - Prefer JSON/GraphQL APIs where available. For older HTML catalogs, use `curl` plus structured parsing.
5. **Return results** - Always include:
   - The resources queried
   - The exact endpoint/page/download link used
   - Raw JSON when available, or a concise structured extraction from HTML
   - Any access, license, citation, or manual-download restriction

## Resource Selection Guide

| User is asking about... | Primary resource(s) | Also consider |
|---|---|---|
| BIDS neuroimaging datasets | OpenNeuro | OSF |
| EEG, MEG, MRI, fMRI, iEEG, PET datasets | OpenNeuro | OSF, Oliva Lab |
| A specific OpenNeuro accession such as `ds004584` | OpenNeuro | OSF if linked by paper/project |
| General project materials, preregistrations, files, protocols | OSF | OpenNeuro for BIDS imaging |
| Brain arterial trees or vascular morphology | BRAVA | NITRC ICBM MRA |
| Human magnetic resonance angiography atlas, NIfTI MRA data | NITRC ICBM MRA | BRAVA |
| Visual cognition, natural scenes, memorability, Algonauts, fMRI/MEG image datasets | Oliva Lab datasets | OpenNeuro |
| Drosophila full adult fly brain EM/connectomics | TEMCA2/FAFB | Virtual Fly Brain, CATMAID tools |
| Interactive brain anatomy explanation, teaching, region names | BrainFacts 3D Brain | General web search for deeper citations |

## Included References

- `references/openneuro.md` - OpenNeuro GraphQL, openneuro-cli, DataLad, and ds004584 example.
- `references/osf.md` - OSF API v2 nodes, files, registrations, and public project lookup.
- `references/brava.md` - BRAVA all-subject browser, subject pages, SWC download, vascular metrics.
- `references/nitrc-icbmmra.md` - NITRC Magnetic Resonance Angiography Atlas Dataset.
- `references/oliva-lab.md` - MIT Oliva Lab datasets and visual cognition/neuroimaging resources.
- `references/temca2-fafb.md` - TEMCA2/FAFB adult fly brain EM image volume and tools.
- `references/brainfacts-3d-brain.md` - BrainFacts 3D Brain educational anatomy resource.

## Identifier Patterns

| Identifier | Example | Resource |
|---|---|---|
| OpenNeuro dataset accession | `ds004584` | OpenNeuro |
| OpenNeuro DOI | `10.18112/openneuro.ds004584.v1.0.0` | OpenNeuro |
| OSF node/project ID | `q4mez`, `sfbpx` | OSF |
| NITRC group ID | `1113` | NITRC ICBM MRA |
| NITRC file ID | `9725` | NITRC ICBM MRA |
| BRAVA subject page ID | `query_subject.php?id=1` | BRAVA |
| FAFB volume/version | `FAFBv14` | TEMCA2/FAFB |

## API and Access Notes

| Resource | Access style | Authentication |
|---|---|---|
| OpenNeuro | GraphQL, openneuro-cli, DataLad, browser | Public browse/download without account for public datasets |
| OSF | JSON:API REST API, browser | Public read without token; token for private/write access |
| BRAVA | HTML/PHP pages and ZIP download | Public HTML/download |
| NITRC ICBM MRA | NITRC HTML and direct file download | Public download observed; NITRC account may be needed for some files on NITRC generally |
| Oliva Lab | HTML catalog and linked dataset pages/forms | Varies by dataset; some direct, some form-gated |
| TEMCA2/FAFB | HTML catalog, CATMAID browser, tile downloads | Public browse/download; respect license |
| BrainFacts 3D Brain | Interactive web page | Public educational page; not a research dataset API |

## Making Requests

Use `curl` or the available web fetch tool. For OpenNeuro and OSF, prefer structured API calls:

```bash
# OpenNeuro GraphQL dataset metadata
curl -s -H "Content-Type: application/json" \
  --data '{"query":"query { dataset(id: \"ds004584\") { id name public metadata { datasetName modalities species studyDomain studyDesign } latestSnapshot { tag size description { Name License DatasetDOI Authors } } } }"}' \
  https://openneuro.org/crn/graphql

# OSF title search
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/?filter%5Btitle%5D=neuroscience&page%5Bsize%5D=5"
```

For HTML resources, fetch the page and extract links/tables:

```bash
curl -L -s "http://cng.gmu.edu/brava/all_subjects.php?clear=1" |
  rg "query_subject.php|swc_files.zip|metrics.php"
```

## Output Format

Use this shape:

- `## Resources Queried`
- `## Results`
- One subsection per resource, with raw JSON in a fenced `json` block when available.
- `## Access Notes`, including license, citation, download method, and file formats.

For large file lists, summarize the first page and include pagination or recursive download instructions.

## Error Recovery

- If OpenNeuro GraphQL rejects a field, introspect the type first or remove the field. OpenNeuro field names are case-sensitive.
- If OSF filters return broad/noisy results, try `filter[title]`, `filter[description]`, `filter[tags]`, and the `/v2/search/` endpoint.
- If an older HTTP resource fails over plain HTTP, retry HTTPS if available, then try with `curl -L`.
- For resources that are not APIs, do not invent JSON. Return extracted page metadata and direct links.
- Always preserve license/citation warnings, especially for TEMCA2/FAFB and older lab-hosted datasets.
