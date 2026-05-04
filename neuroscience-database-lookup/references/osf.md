# OSF

Source: https://osf.io/ and https://api.osf.io/v2/

The Open Science Framework is a general open-science project repository. Use it for neuroscience project pages, preregistrations, study materials, files, protocols, analysis scripts, and supplemental datasets that may not be BIDS datasets.

## Best Uses

- Search public OSF nodes/projects by title, description, or tags.
- Retrieve metadata for a known OSF project ID.
- List files, storage providers, child components, contributors, and registrations.
- Download public files from file metadata links.

## API Root

```text
https://api.osf.io/v2/
```

The API root returns links for nodes, users, collections, registrations, institutions, licenses, schemas, and addons.

## Search Nodes

```bash
# Search titles
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/?filter%5Btitle%5D=neuroscience&page%5Bsize%5D=5"

# Search descriptions
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/?filter%5Bdescription%5D=EEG&page%5Bsize%5D=5"

# Search tags
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/?filter%5Btags%5D=Neuroscience&page%5Bsize%5D=5"
```

The `/v2/search/` endpoint can also return search results:

```bash
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/search/?q=neuroscience&page%5Bsize%5D=5"
```

Search can be noisy. Prefer specific terms: disease, modality, task, author, paper title, or DOI.

## Get Project Metadata

```bash
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/{node_id}/"
```

Important fields:

- `attributes.title`
- `attributes.description`
- `attributes.tags`
- `attributes.public`
- `attributes.date_created`
- `attributes.date_modified`
- `relationships.files.links.related`
- `relationships.children.links.related`
- `relationships.registrations.links.related`

## List Files

```bash
# Storage providers
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/{node_id}/files/"

# OSF storage contents
curl -s -H "Accept: application/vnd.api+json" \
  "https://api.osf.io/v2/nodes/{node_id}/files/osfstorage/"
```

Follow each file object's `links.download` or related metadata link to retrieve content.

## Authentication

Public read access usually does not require a token. Private projects and write operations require an OSF personal access token:

```bash
Authorization: Bearer $OSF_TOKEN
```

Only check `$OSF_TOKEN` when private/write access is requested.

## Output Requirements

Return raw JSON from OSF API calls. Include project ID, title, public/private state, tags, file-provider links, and download links where present.
