# OpenNeuro

Source: https://openneuro.org/ and https://docs.openneuro.org/api.html

OpenNeuro hosts public BIDS-compatible neuroimaging datasets. Use it for EEG, MRI, fMRI, MEG, iEEG, PET, and other BIDS datasets. Public datasets can be browsed and downloaded without an account. Access options include the web UI, GraphQL API, `openneuro-cli`, DataLad, and direct git/data access.

## Best Uses

- Look up a dataset by accession, e.g. `ds004584`.
- Search for datasets by modality, disease, task, species, author, or DOI.
- Inspect BIDS metadata, latest snapshot, file tree, license, authors, and dataset DOI.
- Download full BIDS datasets for analysis.

## GraphQL Endpoint

```text
https://openneuro.org/crn/graphql
```

## Dataset Metadata Example

```bash
curl -s -H "Content-Type: application/json" \
  --data '{"query":"query { dataset(id: \"ds004584\") { id name public publishDate metadata { datasetName datasetId modalities species studyDomain studyDesign trialCount associatedPaperDOI seniorAuthor } latestSnapshot { tag created size description { Name BIDSVersion License Authors DatasetDOI ReferencesAndLinks } } } }"}' \
  https://openneuro.org/crn/graphql
```

Observed ds004584 metadata:

- Title: `Rest eyes open`
- Modality: `eeg`
- Species: `Human`
- Study domain: `Cognition / Parkinson's disease`
- Study design: `Cross-sectional`
- Latest snapshot: `1.0.0`
- License: `CC0`
- Dataset DOI: `doi:10.18112/openneuro.ds004584.v1.0.0`
- Approximate snapshot size observed from GraphQL: `3078216426` bytes

## Search Example

```bash
curl -s -H "Content-Type: application/json" \
  --data '{"query":"query { search(q: \"Parkinson EEG\", first: 10) { edges { node { id name metadata { modalities species studyDomain } } } } }"}' \
  https://openneuro.org/crn/graphql
```

If the search schema changes, introspect:

```bash
curl -s -H "Content-Type: application/json" \
  --data '{"query":"{ __schema { queryType { fields { name args { name type { name kind ofType { name kind } } } } } } }"}' \
  https://openneuro.org/crn/graphql
```

## File Tree Example

OpenNeuro file trees are git tree objects. The docs show `snapshot(datasetId, tag) { files { id filename size directory annexed } }`.

```bash
curl -s -H "Content-Type: application/json" \
  --data '{"query":"query { snapshot(datasetId: \"ds004584\", tag: \"1.0.0\") { files { id filename size directory annexed } } }"}' \
  https://openneuro.org/crn/graphql
```

For nested directories, recursively follow tree IDs or request recursive files when supported by the current schema.

## Download Options

Use one of:

```bash
# openneuro-cli, if installed
openneuro download --dataset ds004584 --snapshot 1.0.0 ./ds004584

# DataLad, good for large datasets
datalad install https://github.com/OpenNeuroDatasets/ds004584.git
cd ds004584
datalad get .
```

## Output Requirements

Return raw GraphQL JSON for metadata/file queries. Include dataset DOI, license, version tag, modality, species, size, and download method.
