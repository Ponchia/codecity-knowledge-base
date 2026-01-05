# CodeCity Knowledge Extraction Plan

## Overview

This plan transforms 154 indexed bibliography sources into a structured, layered knowledge base for the CodeCity domain. The output serves three purposes:

1. **Implementation guide** — Domain understanding for building a CodeCity-style tool
2. **Research synthesis** — Comprehensive coverage of the field (400+ publications)
3. **Gap analysis baseline** — Feature inventory to compare against your implementation

---

## Architecture

```
bibliography/
├── index.csv                      # Source registry (id, url, type)
├── llm_index.jsonl                # Download status + local file paths
├── processing_status.csv          # Extraction tracking (what's been processed)
└── sources/                       # Downloaded artifacts
    ├── pdf/
    ├── pdf_text/
    ├── web/
    └── repo/

docs/
├── glossary.md                    # Layer 1: Domain vocabulary
├── taxonomy.md                    # Layer 2: Classification system
├── features/                      # Layer 3: Atomic feature notes
│   ├── _index.md                  #   Feature catalog with status
│   ├── city-metaphor.md           #   Core metaphor
│   ├── treemap-layout.md          #   Layout algorithm
│   ├── height-mapping.md          #   Property mapping
│   └── ...                        #   One file per feature
├── implementations/               # Layer 4: Tool profiles
│   ├── _index.md                  #   Comparison matrix
│   ├── codecity.md               #   Wettel/Lanza Smalltalk
│   ├── codecharta.md              #   MaibornWolff
│   └── ...                        #   One file per tool
└── sources/                       # Layer 5: Source summaries
    ├── _index.md                  #   Bibliography with notes
    └── annotations/               #   Per-source extraction notes
```

---

## Processing Tracker

**File**: `bibliography/processing_status.csv`

Tracks which sources have been processed for knowledge extraction.

### Schema

| Column | Values | Purpose |
|--------|--------|---------|
| `id` | CC001-CC154 | Links to llm_index.jsonl |
| `extraction_status` | pending, reviewed, extracted, complete, skip, error, suspect | Processing stage |
| `priority` | critical, high, medium, low, skip | Processing order |
| `relevance` | critical, high, medium, low | Domain relevance |
| `notes` | string | What this source is |
| `processed_date` | YYYY-MM-DD | When extracted |
| `features_extracted` | int | Count of features found |
| `terms_extracted` | int | Count of terms found |
| `processor` | claude, gpt, human | Which system processed this source |

### Status Definitions

- **pending**: Not yet reviewed
- **reviewed**: Skimmed, determined relevance, no extraction yet
- **extracted**: Terms/features pulled out, docs updated
- **complete**: Fully processed, cross-references verified
- **skip**: Not relevant or download failed
- **error**: Source could not be processed (e.g., blocked download, unsupported format)
- **suspect**: Source is present but likely incomplete/corrupt (needs repair/re-download)

### Current Counts

As of 2026-01-05:

```
BY PRIORITY:        BY STATUS:
  critical:  9        pending:    0
  high:     48        reviewed:    0
  medium:   67        extracted:   0
  low:      43        complete:   90
  skip:      1        skip:       78
                    partial:     1
                    error:       0
                    suspect:     0

TOTAL SOURCES: 169 (154 original + 15 SOTA gap sources)
TOTAL FEATURES: 87
```

---

## Layer 1: Glossary

**Purpose**: Establish ubiquitous language for the domain (DDD: Ubiquitous Language).

### Schema

```yaml
# glossary.md structure
term:
  definition: string           # 1-2 sentence definition
  aliases: [string]            # Alternative names
  category: enum               # metaphor | metric | mapping | layout | interaction | analysis | platform
  bounded_context: enum        # universal | city-metaphor | island-metaphor | landscape-metaphor | clothing-metaphor | treemap-only
  source_refs: [CC###]         # First/authoritative sources
  related_terms: [string]      # Cross-references
  example: string              # Optional concrete example
```

### Bounded Contexts (DDD Integration)

Terms and features may only apply within certain visualization paradigms. The `bounded_context` field clarifies where a concept is valid:

| Context | Description | Example Tools |
|---------|-------------|---------------|
| `universal` | Applies across all paradigms | metric mapping, filtering, navigation |
| `city-metaphor` | 3D city with buildings/districts | CodeCity, CodeCharta, GoCity, JSCity |
| `island-metaphor` | Landmasses in water | IslandViz, OSGi Islands |
| `landscape-metaphor` | Terrain/topography features | ExplorViz (landscape view) |
| `clothing-metaphor` | Wardrobe/garment metaphor | CodeVestimenta |
| `treemap-only` | 2D treemap without 3D city | Pure treemap tools |

**Usage guidelines:**
- Use `universal` when a concept applies to any software visualization
- Use a specific context when a term only makes sense within that paradigm
- A term like "district" is `city-metaphor` only; "height mapping" is `universal`

### Seed Terms (extract from bibliography)

| Category | Terms to Extract |
|----------|------------------|
| **Metaphor** | city metaphor, code city, building, district, street, block, island metaphor, landscape metaphor |
| **Concept Mapping** | class→building, package→district, method→building (variant), file→building, folder→district |
| **Property Mapping** | height mapping, base/footprint mapping, color mapping, texture mapping |
| **Metrics** | LOC, NOM (number of methods), NOA (number of attributes), complexity, coupling, cohesion, churn, code smells |
| **Layout** | treemap, rectangle packing, space-filling, EvoStreets, progressive bricks |
| **Interaction** | navigation, filtering, selection, drill-down, fly-through |
| **Platform** | desktop, web, VR, AR, immersive, game engine (Minecraft, Unity) |
| **Analysis** | program comprehension, software evolution, design quality, technical debt, hotspot detection |

### Extraction Process

1. Scan foundational sources first: CC035 (Wettel PhD), CC015 (Jeffery survey), CC023 (VISSOFT 2007)
2. Extract term + definition + source
3. Cross-reference with implementation docs (CodeCharta, ExplorViz, GoCity)
4. Normalize aliases (e.g., "code city" vs "CodeCity" vs "software city")

---

## Layer 2: Taxonomy

**Purpose**: Multi-dimensional classification for features and implementations.

### Dimensions

```yaml
# taxonomy.md structure
dimensions:
  granularity:
    description: "What software element becomes the primary visual unit"
    values:
      - file        # CodeCharta, GoCity
      - class       # Original CodeCity
      - method      # Software World
      - function    # JSCity
      - component   # Component City
      - module      # IslandViz

  visual_element:
    description: "What the primary element is rendered as"
    values:
      - building
      - district/block
      - street
      - island
      - tower

  metric_category:
    description: "What aspect of code is measured"
    values:
      - size        # LOC, file size
      - complexity  # cyclomatic, cognitive
      - coupling    # dependencies, imports
      - cohesion    # LCOM
      - evolution   # churn, age, authors
      - quality     # code smells, issues, coverage

  platform:
    description: "Rendering/interaction environment"
    values:
      - desktop_native    # Original Smalltalk
      - web_2d            # Treemaps
      - web_3d            # Three.js, BabylonJS
      - vr_headset        # Oculus, Vive
      - ar_overlay        # HoloLens
      - game_engine       # Minecraft, Unity

  analysis_mode:
    description: "Static vs dynamic vs temporal"
    values:
      - static            # Snapshot analysis
      - dynamic           # Runtime traces
      - evolution         # Time-series
      - collaborative     # Multi-user

  layout_algorithm:
    description: "Spatial arrangement strategy"
    values:
      - treemap           # Squarified treemap
      - rectangle_packing # Wettel's approach
      - street_based      # EvoStreets
      - force_directed    # Graph-based
      - hierarchical      # Nested levels
```

---

## Layer 3: Feature Cards (Pattern Language)

**Purpose**: One markdown file per distinct feature, following the **Pattern Language** format (Christopher Alexander / Gang of Four). This format captures not just WHAT a feature is, but WHY it exists, WHEN to use it, and what TRADE-OFFS it involves.

### Design Philosophy

Feature cards are **design patterns**, not encyclopedia entries. A good feature card enables an implementer to:
1. Understand the problem being solved
2. Decide whether this feature fits their context
3. Implement the feature correctly
4. Anticipate trade-offs and limitations

### Frontmatter Schema

```yaml
# features/<feature-slug>.md frontmatter
---
id: F###                        # Stable feature ID
title: string                   # Human-readable name
category: enum                  # metaphor | mapping | layout | interaction | analysis | platform
status: enum                    # canonical | variant | experimental | deprecated
maturity: enum                  # established | emerging | research
bounded_context: [enum]         # DDD: where this feature applies (see Layer 1)
introduced_by: CC###            # First source to describe
implementations: [string]       # Tools that implement this
related_features: [F###]        # Cross-links
supersedes: [F###]              # If this replaces older approaches
taxonomy:                       # Classification
  granularity: [enum]
  visual_element: [enum]
  metric_category: [enum]
last_updated: YYYY-MM-DD
updated_from: [CC###]           # Sources that contributed
---
```

**Bounded context values**: `universal`, `city-metaphor`, `island-metaphor`, `landscape-metaphor`, `clothing-metaphor`, `treemap-only`

Use an array when a feature applies to multiple contexts (e.g., `[city-metaphor, island-metaphor]`).

### Body Structure (Pattern Language)

```markdown
# {title}

## Problem & Motivation
WHY does this feature exist? What problem does it solve?
- The pain point or challenge it addresses
- The insight that led to this approach
- What happens WITHOUT this feature (negative scenario)

## Definition
1-3 sentences defining the feature precisely (the WHAT).

## Context & Applicability
WHEN should you use this feature?

**Use when:**
- Condition 1
- Condition 2

**Avoid when:**
- Condition 1
- Condition 2

**Prerequisites:** Required features, data sources, or conditions
**Alternatives:** [[other-feature]] for specific scenarios

## Forces
What tensions does this feature balance?

| Force | Pull |
|-------|------|
| Concern A | How it pulls one way |
| Concern B | How it pulls another |

How the feature resolves these competing forces.

## Mechanism (Solution)
How it works technically (the HOW).

**Input**: What data/metrics are required
**Process**: Step-by-step transformation
**Output**: Visual or behavioral result

## Consequences & Trade-offs
What do you gain and lose?

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Advantage 1 | Disadvantage 1 |

**Complexity**: Low | Medium | High
**Performance**: Implications
**Cognitive Load**: User impact

## Variations
Notable variations across implementations.

| Implementation | Variation | Notes |
|----------------|-----------|-------|
| Tool A | How it differs | Source |

## Implementation Notes
Practical guidance for implementers.
- Key algorithms or libraries
- Common pitfalls
- Integration points
- Recommended defaults

## Evidence
Empirical findings with effect sizes where available.

## Known Limitations
What this feature does NOT handle well.

## Open Questions
Unresolved debates or research gaps.

## Sources
- [CC###] Primary source description
- [CC###] Additional sources

## See Also
- [[related-feature]] — relationship (variant of, depends on, conflicts with)
```

### Section Requirements by Status

| Section | canonical | variant | experimental |
|---------|:---------:|:-------:|:------------:|
| Problem & Motivation | ✅ | ✅ | ⚠️ Brief |
| Definition | ✅ | ✅ | ✅ |
| Context & Applicability | ✅ | ⚠️ | ⚠️ |
| Forces | ✅ | ⚠️ | ❌ |
| Mechanism | ✅ | ✅ | ✅ |
| Consequences | ✅ | ✅ | ⚠️ |
| Variations | ✅ If exist | ⚠️ | ❌ |
| Implementation Notes | ✅ | ⚠️ | ❌ |
| Evidence | ✅ If available | ⚠️ | ❌ |
| Known Limitations | ✅ | ⚠️ | ⚠️ |
| Open Questions | ⚠️ | ❌ | ✅ |
| Sources | ✅ | ✅ | ✅ |
| See Also | ✅ | ✅ | ✅ |

### Pattern Language Principles

1. **Problem-first**: Always start with WHY
2. **Context-sensitive**: Document when to use AND when NOT to use
3. **Forces in tension**: Make competing concerns explicit
4. **Consequences matter**: Document both benefits and liabilities
5. **Actionable**: Enable implementation from the card alone
6. **Honest about limits**: Document what doesn't work

### Initial Feature Set (extract from bibliography)

**Core Metaphor Features**:
- `city-metaphor` — The foundational analogy
- `class-as-building` — Original Wettel mapping
- `file-as-building` — Modern variant (CodeCharta)
- `method-as-building` — Fine-grained variant (Software World)
- `package-as-district` — Hierarchical grouping
- `folder-as-district` — File-system variant

**Property Mapping Features**:
- `height-mapping` — Vertical dimension encodes metric
- `base-mapping` — Footprint encodes metric
- `color-mapping` — Hue/saturation encodes metric
- `texture-mapping` — Surface pattern encodes metric

**Layout Features**:
- `treemap-layout` — Space-filling rectangular
- `rectangle-packing` — Wettel's algorithm
- `evostreets-layout` — Street-based evolution
- `progressive-bricks` — Fine-grained method layout

**Interaction Features**:
- `navigation-flythrough` — 3D camera movement
- `filtering` — Show/hide by criteria
- `drill-down` — Hierarchical exploration
- `selection-inspection` — Click-to-detail

**Analysis Features**:
- `hotspot-detection` — Identify problematic areas
- `evolution-visualization` — Change over time
- `disharmony-maps` — Design problem detection
- `dependency-visualization` — Coupling display

**Platform Features**:
- `vr-immersion` — Head-mounted display
- `web-deployment` — Browser-based
- `sonarqube-integration` — Metric import
- `git-integration` — Evolution data

---

## Layer 4: Implementation Profiles

**Purpose**: Document each tool's feature set for comparison.

### Schema

```yaml
# implementations/<tool-slug>.md frontmatter
---
id: I###                        # Stable implementation ID
name: string                    # Tool name
origin: string                  # Institution/Company
year_introduced: number
status: enum                    # active | maintained | archived | historical | research | unknown
source_refs: [CC###]            # Bibliography sources
repo_url: string                # If open-source
demo_url: string                # If available
primary_language: string
features_implemented: [F###]    # Feature IDs
---
```

### Implementation Matrix (to generate)

| Tool | Granularity | Visual | Metrics | Platform | Status |
|------|-------------|--------|---------|----------|--------|
| CodeCity (original) | class | building | NOM, NOA | desktop | historical |
| CodeCharta | file | building | LOC, complexity, churn | web | active |
| GoCity | package/struct | building | LOC, functions | web | active |
| JSCity | function | building | LOC | web | maintained |
| ExplorViz | class | building | traces | web+VR | active |
| IslandViz | module | island | OSGi metrics | VR | research |
| SoftVis3D | file | building | SonarQube | web | maintained |
| CodeMetropolis | class | building | various | Minecraft | research |

---

## Layer 5: Source Annotations

**Purpose**: Per-source extraction notes linking to features/terms.

### Schema

```yaml
# sources/annotations/CC###.yaml
id: CC###
url: string
type: pdf | website | repo
status: ok | error
extraction_status: pending | complete | skip | error | suspect
processor: claude | gpt | human
processed_date: YYYY-MM-DD
summary: string                 # 2-3 sentence summary
key_contributions:
  - string                      # What this source uniquely adds
terms_introduced: [string]      # Terms first defined here (definitions live in glossary.md)
features_described: [F###]      # Features documented here
implementations_documented: [I###]
quality_notes: string           # Empirical evidence, limitations
statistics:
  features_extracted: int
  terms_extracted: int
  implementations_documented: int
```

---

## Extraction Workflow

### Phase 1: Foundation (Priority Sources)

Process these first to establish core vocabulary and feature set:

| ID | Source | Why Priority |
|----|--------|--------------|
| CC035 | Wettel PhD thesis | Canonical definition of everything |
| CC015 | Jeffery survey | Comprehensive implementation comparison |
| CC023 | VISSOFT 2007 paper | Original city metaphor paper |
| CC099 | ICSE 2011 experiment | Empirical validation |
| CC091 | CodeCharta repo | Modern reference implementation |

### Phase 2: Survey Papers

Systematic reviews that identify features across many papers:

| ID | Source | Coverage |
|----|--------|----------|
| CC018 | Moreno-Lumbreras 2024 | 406 publications systematic mapping |
| CC015 | Jeffery survey | Implementation comparison |

### Phase 3: Implementation Documentation

Extract feature lists from tool docs and repos:

- CC014, CC090 (CodeCharta website)
- CC093 (GoCity repo)
- CC094 (JSCity repo)
- CC080 (ExplorViz repo)
- CC091 (CodeCharta repo)

### Phase 4: Academic Papers

Process remaining PDFs for:
- Novel features
- Empirical evidence
- Variant implementations

### Phase 5: Gap Analysis

Compare extracted features against your implementation:
1. Load your implementation's feature list
2. Generate feature matrix
3. Identify gaps and opportunities

---

## Deduplication & Merge Protocol

**Core Principle**: Never duplicate information. Always update existing artifacts.

### Before Creating Anything New

1. **Search first**: Check if term/feature/implementation already exists
2. **Match by concept, not name**: Same idea with different name = update existing, add alias
3. **When in doubt, merge**: Better to enrich existing doc than fragment knowledge

### When Processing a New Source

```
FOR EACH term/feature/implementation found:
  1. Search existing docs for same concept
  2. IF exists:
     - ADD new source to Sources section
     - MERGE any new details into existing sections
     - UPDATE definition only if new source is more authoritative
     - ADD aliases if source uses different name
  3. IF does not exist:
     - CREATE new doc
     - LINK to related existing docs
     - UPDATE related docs to link back
```

### Merge Rules

| Scenario | Action |
|----------|--------|
| Same feature, different name | Add alias to existing, don't create new |
| Same feature, more detail | Merge details into existing doc |
| Same feature, conflicting info | Add "Variations" section noting difference + sources |
| Variant of existing feature | Create new doc, link as variant of parent |
| Duplicate source (same paper, different URL) | Note in processing_status.csv, mark as skip |

### Handling Conflicts

When sources disagree:

```markdown
## Variations

| Aspect | Source A (CC###) | Source B (CC###) |
|--------|------------------|------------------|
| {what differs} | {version A} | {version B} |

**Resolution**: {which is correct/canonical, or note both are valid variants}
```

### Authority Hierarchy

When definitions conflict, prefer sources in this order:

1. Wettel PhD thesis (CC035) — canonical definitions
2. Peer-reviewed papers — validated concepts
3. Survey papers (CC015, CC018) — synthesized understanding
4. Tool documentation — implementation-specific
5. Blog posts/articles — may be imprecise

### Update Tracking

Every doc should track its evolution:

```yaml
# In frontmatter
last_updated: YYYY-MM-DD
updated_from: [CC###, CC###]  # Sources that contributed to latest update
```

---

## Quality Standards

### Feature Cards
- Every feature must cite at least one source
- Cross-links must be bidirectional
- Technical mechanism must be specific enough to implement
- **No duplicate features** — same concept = same doc

### Glossary
- Definitions must be self-contained (no circular definitions)
- Aliases must all redirect to canonical term
- Categories must match taxonomy dimensions
- **No duplicate terms** — same concept = add alias

### Source Annotations
- Every source with `status: ok` must be annotated
- Key contributions must be **unique** (not restating other sources)
- Features described must link to actual feature cards
- If source adds nothing new, note: `key_contributions: [None - duplicates CC###]`

---

## Maintenance Protocol

### Adding New Sources

1. Add to `bibliography/index.csv` with stable ID
2. Run download script
3. Create `sources/annotations/CC###.yaml`
4. Extract terms → update `glossary.md`
5. Extract features → create/update feature cards
6. Update taxonomy if new dimension values

### Updating Features

1. Edit feature card
2. Update `related_features` in linked cards
3. Update implementation profiles if features changed
4. Log change in source annotation that prompted update

### Periodic Review

- Monthly: Check for new publications in the field
- Quarterly: Verify external links still work
- Per-release: Regenerate gap analysis against implementation

---

## Deliverables

| Artifact | Format | Purpose |
|----------|--------|---------|
| `glossary.md` | Markdown | Domain vocabulary reference |
| `taxonomy.md` | Markdown + YAML | Classification system |
| `features/*.md` | Markdown | Atomic feature documentation |
| `implementations/*.md` | Markdown | Tool profiles |
| `sources/annotations/*.yaml` | YAML | Extraction metadata |
| `gap-matrix.md` | Markdown table | Your implementation vs. state-of-art |

---

## Next Steps

1. Create directory structure
2. Process priority sources (Phase 1)
3. Generate initial glossary from Wettel PhD
4. Create first 10 feature cards for core metaphor
5. Profile CodeCharta as reference implementation
6. Iterate through remaining sources
