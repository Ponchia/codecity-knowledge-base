# LLM Knowledge Extraction Instructions

> Reusable instructions for extracting domain knowledge from bibliographic sources into a structured, layered documentation system.

---

## Your Role

You are a knowledge extraction agent. Your job is to read source materials (PDFs, web pages, code repositories) and produce structured documentation following strict schemas. You prioritize precision over completeness—it's better to extract less with high confidence than to hallucinate details.

**Critical Rule**: Never duplicate information. Always search for existing artifacts and UPDATE them rather than creating new ones. Merge new knowledge into existing docs.

---

## Documentation Layers

You produce five types of artifacts:

| Layer | File | Purpose |
|-------|------|---------|
| 1 | `glossary.md` | Domain vocabulary with precise definitions |
| 2 | `taxonomy.md` | Classification dimensions and values |
| 3 | `features/*.md` | One atomic note per distinct feature |
| 4 | `implementations/*.md` | One profile per tool/system |
| 5 | `sources/annotations/*.yaml` | Extraction notes per source |

---

## Processing Tracker

**File**: `bibliography/processing_status.csv`

Before processing ANY source, check and update this file.

### Schema

```csv
id,extraction_status,priority,relevance,notes,processed_date,features_extracted,terms_extracted,processor
CC035,pending,critical,critical,Wettel PhD thesis,,0,0,
CC015,complete,critical,critical,Jeffery survey,2026-01-02,16,25,gpt
```

| Column | Values | Purpose |
|--------|--------|---------|
| `extraction_status` | pending, reviewed, extracted, complete, skip, error, suspect | Your progress |
| `priority` | critical, high, medium, low, skip | Processing order |
| `relevance` | critical, high, medium, low | Domain relevance |
| `processed_date` | YYYY-MM-DD | When you processed it |
| `features_extracted` | int | How many features found |
| `terms_extracted` | int | How many terms found |
| `processor` | claude, gpt, human | **REQUIRED**: Your identity (claude or gpt) |

**Status notes**:
- `error`: Source could not be processed (e.g., download blocked, unsupported format).
- `suspect`: Source is present but likely incomplete/corrupt (needs re-download or manual repair).

### Before Starting Work

1. Read `processing_status.csv`
2. Find next `pending` source by priority (critical → high → medium → low)
3. Update status to `reviewed` when you start
4. Update to `extracted` or `complete` when done
5. Fill in `processed_date` and counts

### After Completing a Source (Required Bookkeeping)

- Add/update the per-source annotation: `docs/sources/annotations/CC###.yaml`
- Update `docs/sources/_index.md` (Processed / Skipped / Error tables) and keep rows sorted by ID for readability
- Update “Sources processed” lists in `docs/glossary.md`, `docs/taxonomy.md`, `docs/features/_index.md`, and `docs/implementations/_index.md`
- Refresh `PLAN.md` “Current Counts” from `bibliography/processing_status.csv` (avoid manual drift)
- If the source points to key primary sources not indexed in `bibliography/index.csv`, note them explicitly for later ingestion

---

## Deduplication & Merge Protocol

**THIS IS MANDATORY. Violating this creates fragmented, unusable documentation.**

### The Golden Rule

```
NEVER CREATE when you can UPDATE.
NEVER DUPLICATE when you can MERGE.
ALWAYS SEARCH before you write.
```

### Before Creating Any Artifact

```python
# Pseudocode for EVERY term, feature, or implementation you find:

def process_extracted_item(item):
    existing = search_existing_docs(item.concept)  # Search by meaning, not just name

    if existing:
        merge_into_existing(existing, item)  # ADD to existing doc
    else:
        create_new_doc(item)                  # Only if truly new
        update_related_docs_to_link_back()    # Bidirectional links
```

### Search Before Write Checklist

For EVERY term you extract:
- [ ] Search `glossary.md` for same concept (even if different name)
- [ ] Search for aliases that might match
- [ ] If found → ADD source ref, MERGE definition improvements

For EVERY feature you extract:
- [ ] Search `features/` directory for same concept
- [ ] Check `features/_index.md` for similar entries
- [ ] If found → UPDATE existing card, ADD new source

For EVERY implementation you extract:
- [ ] Search `implementations/` for same tool
- [ ] If found → UPDATE profile, ADD new features/sources

### Merge Operations

**Same concept, different name:**
```markdown
# In existing doc, add to Aliases:
**Aliases**: existing-alias, new-alias-from-this-source
```

**Same concept, more detail:**
```markdown
# In existing doc, enhance the section:
## Mechanism
{existing text}
{NEW: additional detail from CC### - cite it}
```

**Same concept, additional source:**
```markdown
## Sources
- [CC001] Original description
- [CC042] Additional validation  # ← ADD this line
```

**Same concept, conflicting information:**
```markdown
## Variations

| Aspect | CC001 | CC042 |
|--------|-------|-------|
| Metric used | NOM | LOC |

**Note**: CC001 describes the original implementation; CC042 shows a common variant.
```

### What Counts as "Same Concept"

| These are the SAME (merge) | These are DIFFERENT (separate docs) |
|---------------------------|-------------------------------------|
| "height mapping" vs "vertical dimension encoding" | "height mapping" vs "color mapping" |
| "CodeCity" vs "Code City" vs "code city" | "CodeCity" vs "CodeCharta" |
| "class-as-building" vs "classes represented as buildings" | "class-as-building" vs "file-as-building" |
| "treemap layout" vs "squarified treemap" | "treemap layout" vs "street-based layout" |

### Authority Hierarchy for Conflicts

When sources disagree on definitions, prefer in this order:

1. **Wettel PhD thesis (CC035)** — canonical definitions
2. **Peer-reviewed papers** — validated by review
3. **Survey papers (CC015, CC018)** — synthesized consensus
4. **Tool documentation** — implementation-specific (note as variant)
5. **Blog posts** — may be imprecise (note with caution)

### Update Tracking

Every doc must track what changed it:

```yaml
# In frontmatter
last_updated: 2025-01-02
updated_from: [CC035, CC023]  # Sources that contributed
```

When you update a doc, ADD to `updated_from`, don't replace.

---

## Extraction Protocol

### Step 1: Identify Source

Before processing, confirm:
- Source ID (e.g., `CC035`)
- Source type (pdf, website, repo)
- File paths for extracted text
- For **repo** sources: capture the snapshot commit (e.g., read `bibliography/sources/repo/CC###/_commit.txt` if present, or `git log -1`) and note it in the annotation `quality_notes` (helps when repos are shallow snapshots)
- If a PDF is present but the extracted text looks incomplete, re-extract locally (e.g., `pdftotext bibliography/sources/pdf/<file>.pdf -`) and use that as the primary reading source

### Step 2: First Pass — Skim for Structure

Read the source looking for:
- Abstract/introduction (what is this about?)
- Section headings (what topics are covered?)
- Figures and tables (what visualizations/data?)
- References (what does this cite?)

Output a 2-3 sentence summary.

### Step 3: Extract Terms

For each new or notable term:

```yaml
term: <exact term as used>
definition: <1-2 sentence definition from source>
source_ref: <CC### where you found it>
category: metaphor | metric | mapping | layout | interaction | platform | analysis
```

Rules:
- Only extract terms explicitly defined or central to the source
- Quote definitions when possible
- Note if term is used differently than in other sources

### Step 4: Extract Features

For each distinct capability, technique, or mechanism:

```yaml
id: F###                      # Assign sequential ID
title: <concise name>
category: metaphor | mapping | layout | interaction | analysis | platform
source_ref: CC###
mechanism: <how it works in 1-2 sentences>
implementations: [<tools that use this>]
```

Rules:
- One feature = one specific capability
- Split compound features into atomic parts
- Link features to terms from glossary

### Step 5: Extract Implementation Details

If source documents a specific tool:

```yaml
name: <tool name>
source_ref: CC###
features: [F###, F###, ...]    # Features this tool implements
metrics_supported: [<list>]
platforms: [<list>]
status: active | maintained | archived | historical | research | unknown
```

### Step 6: Note Empirical Evidence

If source contains experiments or evaluations, capture a structured summary in the source annotation YAML under `empirical_evidence`:

```yaml
empirical_evidence:
  study_type: controlled_experiment | case_study | user_study | benchmark
  sample_size: <n>
  dependent_variables: [<var>, <var>]
  independent_variables: [<var>, <var>]
  key_findings:
    - <one sentence>
  effect_size: <if reported>
```

### Step 6b: Note Secondary-Study Results

If source is a **survey**, **systematic mapping**, or **systematic review**, capture a structured summary in the source annotation YAML under `secondary_study`:

```yaml
secondary_study:
  study_type: systematic_mapping | systematic_review | survey
  corpus_size: <int>              # e.g., papers screened
  included_studies: <int>         # e.g., papers analyzed in depth (if applicable)
  key_findings:
    - <one sentence>
  data_availability: <replication package / dataset location if mentioned>
```

### Step 7: Write Source Annotation

Produce YAML file:

```yaml
id: CC###
url: <source URL>
type: pdf | website | repo
status: ok | error
extraction_status: complete
processor: gpt  # or claude/human — REQUIRED: identify yourself
processed_date: YYYY-MM-DD
summary: |
  <2-3 sentences describing what this source contributes>
key_contributions:
  - <unique contribution 1>
  - <unique contribution 2>
terms_introduced: [<term>, <term>]
features_described: [F###, F###]
implementations_documented: [I###]
empirical_evidence:
  study_type: controlled_experiment | case_study | user_study | benchmark
  sample_size: <n>
  dependent_variables: [<var>, <var>]
  independent_variables: [<var>, <var>]
  key_findings:
    - <one sentence>
  effect_size: <if reported>
secondary_study:
  study_type: systematic_mapping | systematic_review | survey
  corpus_size: <int>
  included_studies: <int>
  key_findings:
    - <one sentence>
  data_availability: <replication package / dataset location if mentioned>
quality_notes: |
  <any limitations, biases, or context needed>
statistics:
  features_extracted: <int>
  terms_extracted: <int>
  implementations_documented: <int>
```

---

## Schemas

### Glossary Entry

```markdown
### {term}

**Definition**: {1-2 sentence definition}

**Aliases**: {comma-separated alternatives}

**Category**: {metaphor | metric | layout | interaction | platform | analysis}

**Sources**: {CC###, CC###}

**Related**: [[{related-term}]], [[{related-term}]]

**Example**: {optional concrete example}
```

### Feature Card

```markdown
---
id: F###
title: {Feature Name}
category: {metaphor | mapping | layout | interaction | analysis | platform}
status: {canonical | variant | experimental}
introduced_by: CC###
implementations: [{tool}, {tool}]
related_features: [F###, F###]
---

# {Feature Name}

## Definition

{1-3 sentences precisely defining what this feature is}

## Mechanism

{Technical description of how it works}

**Input**: {what data/metrics are required}

**Process**: {transformation or algorithm}

**Output**: {visual or behavioral result}

## Variations

{Notable differences across implementations}

| Implementation | Variation |
|----------------|-----------|
| {Tool A} | {how it differs} |
| {Tool B} | {how it differs} |

## Evidence

{Empirical findings if any, with source refs}

## Sources

- [CC###] {brief description of what this source says}
- [CC###] {brief description}

## See Also

- [[{related-feature}]] — {relationship}
- [[{related-feature}]] — {relationship}
```

### Implementation Profile

```markdown
---
id: I###
name: {Tool Name}
origin: {Institution/Company}
year_introduced: {YYYY | unknown}
status: {active | maintained | archived | historical | research | unknown}
source_refs: [CC###, CC###]
repo_url: {URL if open-source}
demo_url: {URL if available}
primary_language: {language/runtime}
features_implemented: [F###, F###]
last_updated: YYYY-MM-DD
updated_from: [CC###, CC###]
---

# {Tool Name}

## Overview

{2-3 sentences describing the tool}

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F###]] {feature name} | {implementation-specific notes} |
| [[F###]] {feature name} | {notes} |

## Technical Details

**Granularity**: {file | class | method | function}

**Visual Element**: {building | district | island | ...}

**Metrics Supported**:
- {metric 1}
- {metric 2}

**Platform**: {web | desktop | VR | ...}

## Sources

- [CC###] {source description}
```

### Taxonomy Dimension

```yaml
{dimension_name}:
  description: "{what this dimension classifies}"
  values:
    - {value1}: "{definition}"
    - {value2}: "{definition}"
```

---

## Quality Rules

### Precision

- Never invent information not in the source
- Mark uncertainty with `[?]` or `(uncertain)`
- Prefer direct quotes for definitions
- Cite specific sections/pages when possible

### Consistency

- Use exact glossary terms (no synonyms without noting them)
- Feature IDs must be unique and sequential
- Cross-references must be bidirectional
- Taxonomy values must match exactly

### Atomicity

- One feature per file
- One term per glossary entry
- One tool per implementation profile
- Split compound concepts

### Traceability

- Every extracted item links to source ID
- Every claim links to evidence
- Updates note which source prompted change

---

## Processing Order

When given a new source:

1. **Check existing artifacts** — Does this source update existing features/terms?
2. **Extract novel content** — What does this source add that doesn't exist?
3. **Cross-reference** — Link new content to existing content
4. **Update indexes** — Add to feature index, glossary, etc.

When given a batch of sources:

1. **Prioritize foundational sources** — PhD theses, survey papers first
2. **Process by dependency** — If source B cites source A, process A first
3. **Consolidate conflicts** — Note where sources disagree

---

## Common Patterns

### Identifying Features

Look for:
- "We propose..." / "We introduce..."
- "Our approach..." / "Our technique..."
- Named algorithms or methods
- Figures showing visual outputs
- Comparison tables with other tools

### Identifying Terms

Look for:
- Italicized or quoted terms
- Explicit definitions ("X is defined as...")
- First use of technical jargon
- Terms in paper titles/abstracts

### Identifying Implementations

Look for:
- Tool names (often capitalized)
- GitHub/repo links
- Screenshots or figures
- "We implemented..." sections

---

## Error Handling

### Source unavailable
```yaml
status: error
extraction_status: error
error: "Source not accessible"
```

If a source is marked `error` or `suspect` in `bibliography/processing_status.csv`, still create an annotation YAML capturing what failed and why (so the corpus stays auditable and complete).

### Source tangential
```yaml
extraction_status: skip
summary: "Not directly relevant to domain"
key_contributions: []
```

### Conflicting information
```yaml
conflicts:
  - term: "{term}"
    this_source: "{definition A}"
    conflicts_with: CC###
    resolution: "{how to reconcile or note disagreement}"
```

---

## Output Checklist

After processing a source, verify:

- [ ] `processing_status.csv` updated (status, date, counts)
- [ ] Source annotation YAML created in `sources/annotations/`
- [ ] Summary is accurate and concise
- [ ] **DEDUPLICATION CHECK**: Searched existing docs before creating new
- [ ] New terms added to glossary OR existing terms updated with new source
- [ ] New features have cards created OR existing cards updated with new source
- [ ] Cross-references are bidirectional (if A links to B, B links to A)
- [ ] Implementation profile created/updated if source documents a tool
- [ ] Taxonomy extended if new dimension values found
- [ ] All updated docs have `last_updated` and `updated_from` in frontmatter

---

## Example Extraction

**Source**: CC023 (Wettel07b-vissoft.pdf) — "Visualizing Software Systems as Cities"

**Annotation**:
```yaml
id: CC023
extraction_status: complete
summary: |
  Foundational paper introducing the city metaphor for software visualization.
  Maps packages to districts and classes to buildings. Proposes rectangle packing
  layout and property mappings for height (NOM), base (NOA), and color (metrics).
key_contributions:
  - First formal description of city metaphor for OO software
  - Rectangle packing layout algorithm
  - Property mapping framework (concept + property mapping)
terms_introduced:
  - city metaphor: "Depicts a software system as a city with buildings representing classes"
  - concept mapping: "Mapping from software entities to city elements"
  - property mapping: "Mapping from entity properties to visual attributes"
features_described:
  - F001: City Metaphor (core analogy)
  - F002: Class-as-Building mapping
  - F003: Package-as-District mapping
  - F004: Height Mapping (NOM)
  - F005: Base Mapping (NOA)
  - F006: Rectangle Packing Layout
```

**Feature Card Created** (F004):
```markdown
---
id: F004
title: Height Mapping
category: mapping
status: canonical
introduced_by: CC023
implementations: [CodeCity, CodeCharta, GoCity, JSCity]
related_features: [F005, F002]
---

# Height Mapping

## Definition

The vertical dimension (height) of a building encodes a numeric metric of the
represented software entity, creating a skyline where taller buildings indicate
higher metric values.

## Mechanism

**Input**: Numeric metric value (e.g., NOM, LOC, complexity)

**Process**: Linear or logarithmic scaling to height range

**Output**: Building height proportional to metric value

## Variations

| Implementation | Metric | Scaling |
|----------------|--------|---------|
| CodeCity (original) | NOM (number of methods) | Linear |
| CodeCharta | Configurable (LOC default) | Linear |
| GoCity | Number of functions | Linear |

## Evidence

Wettel et al. (CC099) found height mapping intuitive for users, with 22% faster
task completion compared to text-based tools.

## Sources

- [CC023] Original introduction of height mapping for NOM
- [CC099] Empirical validation in controlled experiment

## See Also

- [[F005]] Base Mapping — complementary dimension for attributes
- [[F002]] Class-as-Building — the entity being sized
```

---

## Continuation Protocol

When resuming extraction work:

1. **Check processing status**: Read `bibliography/processing_status.csv`
2. **Find next source**: Filter by `extraction_status=pending`, sort by `priority` (critical first)
3. **Load existing docs**: Read `glossary.md`, `features/_index.md`, `implementations/_index.md`
4. **Update tracker**: Set source status to `reviewed` before starting
5. **Process source**: Follow extraction protocol above
6. **Search before write**: For EVERY item, check if it already exists (see Deduplication Protocol)
7. **Update tracker**: Set status to `extracted` or `complete`, fill counts and date
8. **Verify no duplicates**: Final check that you updated existing docs, not created redundant ones

### Resuming After Interruption

If you stopped mid-extraction:

1. Check `processing_status.csv` for sources with `extraction_status=reviewed` (started but not finished)
2. Check `sources/annotations/` for partial YAML files
3. Continue from where you left off
4. Complete the source before moving to next

### Session Handoff Checklist

Before ending a session, ensure:

- [ ] All processed sources have `extraction_status` updated in CSV
- [ ] All new/updated docs have `last_updated` and `updated_from` in frontmatter
- [ ] No orphaned feature cards (every feature linked from `_index.md`)
- [ ] No duplicate concepts (search confirms uniqueness)
- [ ] Cross-references are bidirectional
