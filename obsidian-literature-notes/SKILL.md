---
name: obsidian-literature-notes
description: >
  Summarize sources and create Obsidian-compatible Zettelkasten notes (.md) with YAML frontmatter,
  tags, wikilinks, and atomic note structure — with rigorous, field-by-field methodology extraction
  for empirical papers. Use this skill whenever the user wants to:
  - Summarize a paper, preprint, article, blog post, web page, PDF, or raw text into a Zettelkasten note
  - Create Obsidian notes with proper tags, metadata, or YAML frontmatter
  - Convert research or reading into linked atomic notes
  - Generate a "literature note", "permanent note", "fleeting note", or MOC
  - Extract the methods of a study in structured, replication-grade detail
  - Build a second brain or PKM (Personal Knowledge Management) entry
  Trigger even if the user just says "summarize this article for Obsidian", "make a zettel for this",
  "add this paper to my vault", or "what did they actually do in this study?".
---

# Obsidian Literature Notes

Turn sources into vault-ready Markdown notes. Two non-negotiables:

1. **Nothing is invented.** Every number, parameter, and claim in the note is traceable to the source. Missing information is recorded as missing, never smoothed over.
2. **Methods are extracted, not summarized.** For empirical work, the Methodology block is a structured field list (see `references/methodology-extraction.md`), not prose.

---

## Config (defaults — override if the user says otherwise)

| Setting | Default |
|---|---|
| Filename | `{citekey} — {Short Title}.md` where citekey = `AuthorYear` (e.g. `Rogasch2017 — Cleaning TMS-EEG.md`) |
| Fallback filename | `{YYYY-MM-DD} — {Short Title}.md` if no author/year |
| Output dir | `/mnt/user-data/outputs/` |
| Default note type | `literature-note` |
| Language | match the source's language for terminology, the user's language for prose |

Strip `\ / : * ? " < > |` from filenames. Keep them under ~80 characters.

---

## Workflow

### 1. Get the content
- **URL** → `web_fetch`. **PDF / file path** → read it. **Pasted text** → use directly.
- If a Zotero MCP is available and the user works from a library, pull metadata, fulltext, and existing annotations from there first (see `zotero-research-skill`), and reuse the Better BibTeX citekey.
- **If retrieval fails or returns only an abstract/paywall stub: say so and stop.** Do not write a methodology section from an abstract. Offer to write an abstract-only note explicitly marked `depth: abstract-only`.

### 2. Extract metadata
Title · authors · journal/venue · year · DOI · URL · citekey · document type (empirical / review / meta-analysis / theory / preprint / opinion / documentation).
Unknown → `unknown`. Never guess a year or a DOI.

### 3. Classify the source
This decides the template. Run this before writing anything:

- **Empirical study** → full template + design-specific methodology fields
- **Meta-analysis / systematic review** → methodology fields = search & synthesis protocol (PRISMA-style)
- **Narrative review / theory / position paper** → replace Methodology with **Argument Structure**; replace Results with **Evidence Marshalled**
- **Methods/tools paper, software, documentation** → Methodology = the procedure/pipeline itself; add **Parameters & Defaults**
- **Blog / opinion / essay** → Claim, Reasoning, Evidence, Counterarguments. No fake Methods section.

### 4. Extract the methodology
**Read `references/methodology-extraction.md` and follow it.** This is the core of the skill. Summary of the rules:

- Structured `**Field**: value` lines, not paragraphs.
- Copy exact numbers and units. Never round, never convert silently, never approximate ("about 30 participants" is a failure; `N = 32 recruited, 29 analysed (3 excluded: excessive artifacts)` is correct).
- Anything the paper does not state → `not reported`. Listing these is part of the job, not a gap in the note.
- Distinguish `[reported]` from `[inferred]` when you have to reason from a figure or a citation to another paper.
- End with a **Reproducibility gaps** line collecting every `not reported` item.
- Self-check: *could someone draft a replication protocol from this block alone? Which field would they have to guess?*

### 5. Extract results separately from discussion
Results = what was observed, with direction, statistics, effect sizes, and units.
Discussion = what the authors think it means, their stated limitations, their conclusion.
Do not merge them, and never let an author's interpretation appear as a result.

### 6. Tags
- Lowercase, hyphenated: `tms-eeg`, `note-taking`. Hierarchical where useful: `method/tms`, `topic/plasticity`.
- 4–10 total. Include one type tag (`literature-note`) and, for empirical work, one method tag and one topic tag.
- Frontmatter tags only — no `#` prefix in YAML, no inline tag spam in the body.

### 7. Write the note
Use the template in `references/templates.md`. Own words throughout. Quotes ≤ 15 words, at most one per source, with a locator (page/section).

### 8. Spawn atomic notes
A literature note is a container bound to one source; it is *not* the atomic unit. After writing it, propose 1–3 **permanent notes** — one claim each, source-independent, titled as a full sentence (`Sham TMS without auditory masking inflates early TEP amplitude`). Ask before generating them unless the user already asked for atomic notes.

### 9. Save and present
Write to the output dir, then `present_files`. If several notes were produced, present the literature note first.

---

## Quality gate (run before presenting)

- [ ] Every number in the note appears in the source
- [ ] No `not reported` item silently omitted
- [ ] Results contain statistics or a clear statement that none were given
- [ ] Author conclusions are attributed to the authors, not asserted
- [ ] `[[wikilinks]]` present (≥ 2), pointing at concepts, not restatements of the title
- [ ] No quote over 15 words; no reproduced paragraphs, abstract, or figure captions
- [ ] Frontmatter YAML is valid (quote any string containing `:`)
- [ ] Filename has no illegal characters

---

## Note types

| Type | Use | `type` |
|---|---|---|
| Literature note | Someone else's work, bound to one source | `literature-note` |
| Permanent note | One synthesized claim in your own words | `permanent-note` |
| Fleeting note | Quick unprocessed capture | `fleeting-note` |
| MOC | Index / map of content over a topic | `moc` |

---

## Asking the user

At most one question, and only when it actually changes the output — e.g. note type when it is genuinely ambiguous, or vault conventions on first use. Never ask for tags, structure, or filenames; generate those.
