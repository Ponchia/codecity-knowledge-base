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

**Bounded Context**: {universal | city-metaphor | island-metaphor | landscape-metaphor | treemap-only}

**Sources**: {CC###, CC###}

**Related**: [[{related-term}]], [[{related-term}]]

**Example**: {optional concrete example}
```

#### Bounded Contexts (DDD)

Terms and features may only apply within certain visualization paradigms. Use `bounded_context` to clarify applicability:

| Context | Description | Example Tools |
|---------|-------------|---------------|
| `universal` | Applies across all paradigms | metric mapping, filtering, navigation |
| `city-metaphor` | 3D city with buildings/districts | CodeCity, CodeCharta, GoCity, JSCity |
| `island-metaphor` | Landmasses in water | IslandViz, OSGi Islands |
| `landscape-metaphor` | Terrain/topography features | ExplorViz (landscape view) |
| `treemap-only` | 2D treemap without 3D city | Pure treemap tools |

**When to use:**
- `universal`: Concept works in any software visualization
- Specific context: Concept only makes sense within that metaphor (e.g., "district" only in city-metaphor)

### Feature Card (Pattern Language Format)

Feature cards follow the **Pattern Language** format (Christopher Alexander / Gang of Four), capturing not just WHAT a feature is, but WHY it exists, WHEN to use it, and what TRADE-OFFS it involves. This approach transforms feature cards from encyclopedia entries into actionable design patterns.

#### Frontmatter Schema

```yaml
---
id: F###
title: {Feature Name}
category: {metaphor | mapping | layout | interaction | analysis | platform}
status: {canonical | variant | experimental | deprecated}
maturity: {established | emerging | research}
bounded_context: [universal | city-metaphor | island-metaphor | landscape-metaphor | treemap-only]
introduced_by: CC###
implementations: [{tool}, {tool}]
related_features: [F###, F###]
supersedes: [F###]              # If this replaces older approaches
taxonomy:
  granularity: [file, class, method, function]
  visual_element: [building, district, street]
  metric_category: [size, complexity, coupling]
last_updated: YYYY-MM-DD
updated_from: [CC###, CC###]
---
```

#### Body Structure (Pattern Language)

```markdown
# {Feature Name}

## Problem & Motivation

{WHY does this feature exist? What problem or challenge does it address?}

- The pain point or challenge it solves
- The insight or observation that led to this approach
- What happens WITHOUT this feature (the negative scenario)

## Definition

{1-3 sentences precisely defining what this feature is — the WHAT}

## Context & Applicability

{WHEN should you use this feature?}

**Use when:**
- {Condition or scenario 1}
- {Condition or scenario 2}

**Avoid when:**
- {Condition where this is NOT appropriate}
- {Scenario where alternatives work better}

**Prerequisites:** {Required features, data sources, or conditions}

**Alternatives:** [[{other-feature}]] for {scenario}; [[{other-feature}]] for {scenario}

## Forces

{What tensions or competing concerns does this feature balance?}

| Force | Pull |
|-------|------|
| {Concern A} | {How it pulls toward one design choice} |
| {Concern B} | {How it pulls toward another choice} |

{Explanation of how this feature resolves or balances these forces}

## Mechanism (Solution)

{Technical description of HOW it works — the solution to the problem}

**Input**: {What data, metrics, or structures are required}

**Process**:
1. {Step 1 of the algorithm/transformation}
2. {Step 2}
3. {Step 3}

**Output**: {Visual or behavioral result}

## Consequences & Trade-offs

{What do you gain and lose by using this feature?}

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| {Advantage 1} | {Disadvantage 1} |
| {Advantage 2} | {Disadvantage 2} |

**Complexity**: {Low | Medium | High} — {brief justification}

**Performance**: {Any performance implications}

**Cognitive Load**: {How it affects user understanding}

## Variations

{Notable differences across implementations — the VARIANTS}

| Implementation | Variation | Notes |
|----------------|-----------|-------|
| {Tool A} | {How it differs} | {Source ref} |
| {Tool B} | {How it differs} | {Source ref} |

## Implementation Notes

{Practical guidance for implementers}

- **Key algorithms or libraries**: {What's needed to implement}
- **Common pitfalls**: {What to avoid}
- **Integration points**: {How this connects to other features}
- **Recommended defaults**: {Sensible starting configuration}

## Evidence

{Empirical findings with effect sizes where available}

- {Study 1}: {Finding with metrics, e.g., "24% improvement in task completion (p<.05)"}
- {Study 2}: {Finding}

## Known Limitations

{What this feature does NOT handle well}

- {Limitation 1}
- {Limitation 2}
- {Edge cases that break down}

## Open Questions

{Unresolved debates or areas needing research}

- {Question 1 — e.g., "Optimal discretization bin count is not established"}
- {Question 2}

## Sources

- [CC###] {Brief description of what this source contributes}
- [CC###] {Brief description}

## See Also

- [[{related-feature}]] — {Relationship: variant of, complementary to, depends on, conflicts with}
- [[{related-feature}]] — {Relationship}
```

#### Section Requirements by Feature Status

| Section | canonical | variant | experimental |
|---------|:---------:|:-------:|:------------:|
| **Problem & Motivation** | ✅ Required | ✅ Required | ⚠️ Brief |
| **Definition** | ✅ Required | ✅ Required | ✅ Required |
| **Context & Applicability** | ✅ Required | ⚠️ Recommended | ⚠️ If known |
| **Forces** | ✅ Required | ⚠️ If complex | ❌ Optional |
| **Mechanism** | ✅ Required | ✅ Required | ✅ Required |
| **Consequences & Trade-offs** | ✅ Required | ✅ Required | ⚠️ Preliminary |
| **Variations** | ✅ If exist | ⚠️ Parent ref | ❌ N/A |
| **Implementation Notes** | ✅ Required | ⚠️ Differences only | ❌ Optional |
| **Evidence** | ✅ If available | ⚠️ If available | ❌ Usually N/A |
| **Known Limitations** | ✅ Required | ⚠️ Recommended | ⚠️ If known |
| **Open Questions** | ⚠️ If relevant | ❌ Optional | ✅ Required |
| **Sources** | ✅ Required | ✅ Required | ✅ Required |
| **See Also** | ✅ Required | ✅ Required | ✅ Required |

#### Pattern Language Principles

1. **Problem-first**: Always start with WHY. A pattern without a problem is just a description.
2. **Context-sensitive**: Features aren't universally applicable. Document when to use AND when NOT to use.
3. **Forces in tension**: Good patterns resolve competing concerns. Make the trade-offs explicit.
4. **Consequences matter**: Every solution creates new problems. Document both benefits and liabilities.
5. **Actionable**: A reader should be able to implement the pattern from the card alone.
6. **Honest about limits**: Document what doesn't work, not just what does.

#### Minimal vs Full Cards

**Minimal card** (for `variant` or `experimental` status):
```markdown
# {Feature Name}

## Problem & Motivation
{1-2 sentences on why this variant exists}

## Definition
{What it is}

## Mechanism
{How it works}

## Consequences & Trade-offs
| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| {Pro} | {Con} |

## Sources
- [CC###] {Source}

## See Also
- [[{parent-feature}]] — variant of
```

**Full card** (for `canonical` status): All sections populated with multiple sources, evidence, and implementation guidance.

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

**Feature Card Created** (F004 — Pattern Language Format):
```markdown
---
id: F004
title: Height Mapping
category: mapping
status: canonical
maturity: established
bounded_context: [city-metaphor, island-metaphor]  # Works in any building-based viz
introduced_by: CC023
implementations: [CodeCity, CodeCharta, GoCity, JSCity]
related_features: [F005, F002]
taxonomy:
  granularity: [class, file, function]
  visual_element: [building]
  metric_category: [size, complexity]
last_updated: 2026-01-05
updated_from: [CC023, CC099]
---

# Height Mapping

## Problem & Motivation

When visualizing software as a city, users need to quickly compare quantitative metrics across hundreds or thousands of code entities. Reading numeric values from labels doesn't scale—users need a visual encoding that enables rapid, pre-attentive comparison.

- **Challenge**: How do you encode magnitude so users can spot outliers at a glance?
- **Insight**: Humans are highly attuned to height differences (evolutionary advantage for navigation)
- **Without this**: Users must read individual labels or hover for tooltips, breaking flow

## Definition

The vertical dimension (height) of a building encodes a numeric metric of the represented software entity, creating a skyline where taller buildings indicate higher metric values.

## Context & Applicability

**Use when:**
- The metric is always non-negative (height can't be negative)
- Comparison of magnitude matters (e.g., finding the largest/smallest)
- You want users to identify outliers quickly

**Avoid when:**
- The metric can be negative (use color instead)
- Precision matters more than comparison (height is imprecise)
- The metric range is very small (differences become imperceptible)

**Prerequisites:** Building-based visualization ([[city-metaphor]]), numeric metric source

**Alternatives:** [[color-mapping]] for categorical or diverging data; [[base-mapping]] if horizontal comparison preferred

## Forces

| Force | Pull |
|-------|------|
| **Perceptual salience** | Height is immediately noticeable; creates memorable skyline |
| **Occlusion** | Tall buildings can hide shorter ones behind them |
| **Range compression** | Extreme outliers can dwarf everything else |
| **Intuitiveness** | "Taller = more" is culturally universal |

Height mapping resolves these forces by leveraging human spatial perception while accepting some occlusion trade-off. Logarithmic scaling can mitigate range compression.

## Mechanism (Solution)

**Input**: Numeric metric value (e.g., NOM, LOC, cyclomatic complexity)

**Process**:
1. Collect all metric values across entities
2. Determine scaling strategy (linear, logarithmic, or discretized)
3. Map value to height within configured min/max range
4. Apply height to building geometry

**Output**: Building height proportional to metric value; skyline enables rapid comparison

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Immediate visual comparison | Tall buildings occlude shorter ones |
| Intuitive "taller = more" mapping | Extreme outliers dominate the view |
| Creates memorable city skyline | Cannot represent negative values |
| Works across cultures | Precise comparison is difficult |

**Complexity**: Low — simple numeric scaling
**Performance**: Negligible — O(n) scaling operation
**Cognitive Load**: Low — highly intuitive mapping

## Variations

| Implementation | Metric | Scaling | Notes |
|----------------|--------|---------|-------|
| CodeCity (original) | NOM (number of methods) | Linear | CC023 |
| CodeCharta | Configurable (LOC default) | Linear | User-selectable |
| GoCity | Number of functions | Linear | Go-specific |
| SoftVis3D | Configurable | Linear/Log/Exp | CC040 |

## Implementation Notes

- **Key algorithms**: Simple linear interpolation; optional log transform for outlier compression
- **Common pitfalls**: Forgetting to handle zero values (log(0) is undefined); not clamping max height
- **Integration points**: Combine with [[base-mapping]] for second metric; use [[color-mapping]] for third
- **Recommended defaults**: Linear scaling; min height 1 unit; max height 100 units; LOC as default metric

## Evidence

- Wettel et al. (CC099): Height mapping intuitive for users, with **22% faster task completion** compared to text-based tools in controlled experiment (n=41, p<.05)
- User studies show height is the most salient visual variable in 3D city visualizations (CC015)

## Known Limitations

- Cannot represent negative values (e.g., delta metrics with decreases)
- Occlusion in dense cities requires camera rotation to see all buildings
- Very small metric differences are imperceptible
- Extreme outliers (10,000 LOC file among 100 LOC files) require log scaling or clamping

## Open Questions

- Optimal scaling strategy (linear vs log vs discretized) not definitively established
- Interaction between height and other visual variables (color, base) needs more study
- Effectiveness in VR (where scale is more immersive) vs desktop not compared

## Sources

- [CC023] Original introduction of height mapping for NOM in CodeCity
- [CC099] Empirical validation in controlled experiment (ICSE 2011)
- [CC040] SoftVis3D scaling options (linear, logarithmic, exponential)

## See Also

- [[base-mapping]] — complementary dimension for second metric (NOA, footprint)
- [[color-mapping]] — alternative/complementary encoding for categorical or third metric
- [[class-as-building]] — the entity being sized
- [[discretized-mapping]] — variant using bins instead of continuous scale
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
