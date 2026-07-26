# Templates

Drop unused sections rather than filling them with filler. Quote any YAML string containing a colon.

---

## Literature note (empirical)

```markdown
---
id: {{YYYYMMDDHHMM}}
citekey: {{AuthorYear}}
title: "{{Full title}}"
authors: [{{Last, F.}}, {{Last, F.}}]
year: {{YYYY}}
venue: "{{Journal / conference / preprint server}}"
doi: {{10.xxxx/xxxxx}}
url: {{URL}}
type: literature-note
doctype: {{empirical | review | meta-analysis | theory | methods | preprint | opinion}}
depth: {{full-text | abstract-only}}
status: {{unread | skimmed | read | processed}}
created: {{YYYY-MM-DD}}
tags:
  - literature-note
  - {{method/...}}
  - {{topic/...}}
  - {{domain}}
---

# {{Short title}}

> [!abstract] Main idea
> {{1–2 sentences, own words. The claim the paper makes, not what it is "about".}}

## Research question / hypothesis

{{The specific question or directional prediction, as stated. If the hypothesis was not stated a priori, say so — it matters.}}

## Methodology

**Design**: …
**Sample**: N recruited → N analysed; exclusions (n + reason)
**Participants**: …
**Power**: …
**Materials / apparatus**: …
**Procedure**: …
**Variables**: IV … · DV … · covariates …
**Analysis**: …
**Open science**: preregistration … · data … · code … · ethics …

<!-- add the design-specific field block from references/methodology-extraction.md here -->

**Reproducibility gaps**: {{every `not reported` / `unclear` item, comma-separated}}

## Results

- {{Finding, with direction, statistic, effect size + CI, and units. One bullet per result.}}
- {{Null results included — they are results.}}

## Authors' interpretation

{{What they conclude the findings mean, and how far they generalize it. Attributed, not asserted.}}

**Stated limitations**: {{as listed by the authors}}

## Critical appraisal

{{Your own read: does the design support the conclusion? Red flags from the checklist. Distinguish clearly from the authors' own limitations above. Keep it short and specific.}}

## Key insights

1. **{{Insight}}** — {{1–2 sentences.}}
2. **{{Insight}}** — {{1–2 sentences.}}
3. **{{Insight}}** — {{1–2 sentences.}}

## Quote

> "{{≤ 15 words}}" — {{Author}}, {{p./section}}

## Connections

- [[{{Concept}}]] — {{how it connects; agrees / contradicts / extends / uses}}
- [[{{Concept}}]] — {{…}}

## My thoughts

_← Your synthesis goes here_

## Reference

{{Author(s)}} ({{Year}}). {{Title}}. *{{Venue}}*. {{DOI}}
```

---

## Literature note (non-empirical)

Same frontmatter. Body:

```markdown
# {{Short title}}

> [!abstract] Main idea
> {{…}}

## Claim

## Argument structure
1. {{Premise}}
2. {{Inferential move}}
3. {{Conclusion}}

## Evidence offered
- {{Evidence}} — type: {{data | anecdote | authority | analogy | formal}}

## Counterarguments
**Addressed**: …
**Ignored**: …

## Key insights
## Connections
## My thoughts
## Reference
```

---

## Permanent note

One claim, source-independent, title = a full declarative sentence.

```markdown
---
id: {{YYYYMMDDHHMM}}
title: "{{Claim as a full sentence}}"
type: permanent-note
created: {{YYYY-MM-DD}}
tags: [permanent-note, {{topic/...}}]
---

# {{Claim as a full sentence}}

{{2–5 sentences developing the claim in your own words. No source summary — the idea has to stand alone.}}

**Confidence**: {{strong | moderate | tentative}} — {{why}}

**Grounded in**: [[{{AuthorYear}}]], [[{{AuthorYear}}]]
**Tension with**: [[{{AuthorYear}}]] — {{what conflicts}}
**Opens**: {{the question this raises next}}
```

---

## Fleeting note

```markdown
---
id: {{YYYYMMDDHHMM}}
type: fleeting-note
created: {{YYYY-MM-DD}}
tags: [fleeting-note, inbox]
---

{{Raw capture. Where it came from. What to do with it.}}
```

---

## MOC

```markdown
---
id: {{YYYYMMDDHHMM}}
title: "{{Topic}} MOC"
type: moc
created: {{YYYY-MM-DD}}
tags: [moc, {{topic/...}}]
---

# {{Topic}}

{{2–3 sentences: what this map covers and how it is organized.}}

## Core claims
- [[{{Permanent note}}]]

## Open questions
- {{…}}

## Sources
- [[{{AuthorYear}}]] — {{one line}}

## Adjacent maps
- [[{{Other MOC}}]]
```

---

## Dataview snippets for the vault

Papers with reproducibility gaps:

    ```dataview
    TABLE year, venue FROM #literature-note WHERE contains(file.content, "Reproducibility gaps") SORT year DESC
    ```

Unprocessed reading queue:

    ```dataview
    LIST FROM #literature-note WHERE status != "processed" SORT created ASC
    ```
