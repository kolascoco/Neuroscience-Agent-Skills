# TEMCA2 / FAFB

Source: https://www.temca2data.org/

TEMCA2 Data hosts the full adult fly brain (FAFB) electron microscopy image volume imaged at synaptic resolution. Use it for Drosophila EM/connectomics data, CATMAID browsing, large image tile downloads, and links to tracing/analysis tools.

## Best Uses

- Browse FAFBv14 online through CATMAID/Virtual Fly Brain.
- Download and trace locally using a preconfigured CATMAID installation.
- Download large losslessly compressed image tiles.
- Find tools for CATMAID, pymaid, natverse, rcatmaid, and FAFB community analysis.
- Check license/citation expectations.

## Key Links Observed

- Online CATMAID browser: `https://fafb.catmaid.virtualflybrain.org/`
- Local tracing page: `https://www.temca2data.org/data.html`
- Large image tile download page: `https://www.temca2data.org/download.html`
- Paper: Zheng, Lauritzen et al. 2018, Cell
- Analysis code and neuronal skeletons: linked from the TEMCA2 page
- License: CC-BY-NC 4.0

## Catalog Extraction

```bash
curl -L -s "https://www.temca2data.org/" |
  rg "FAFB|Download|Browse online|CATMAID|license|CC-BY-NC|synaptic|Pymaid|natverse|tiles"
```

## Access Pattern

For exploratory browsing:

```text
https://fafb.catmaid.virtualflybrain.org/
```

For programmatic work, use CATMAID-compatible tools:

- R: `rcatmaid`, `nat`, `natverse`
- Python: `pymaid`

The CATMAID server and tile data are large. Avoid full downloads unless the user explicitly wants them.

## Output Requirements

Return:

- FAFB resource URL
- Which access path was used: online browser, local CATMAID, tile download, tools page
- License and citation note
- Any relevant data volume/version, especially `FAFBv14`
- Tool recommendations for the user language, e.g. Python `pymaid` or R `rcatmaid`
