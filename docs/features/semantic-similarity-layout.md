---
id: F077
title: Semantic Similarity Layout
category: layout
status: experimental
maturity: research
bounded_context: [universal]
introduced_by: CC157
implementations: [Software Galaxies]
related_features: [F008, F010, F076]
supersedes: []
taxonomy:
  granularity: [file, class]
  visual_element: [building, star]
  metric_category: []
last_updated: 2026-01-05
updated_from: [CC157]
---

# Semantic Similarity Layout

## Problem & Motivation

Traditional layout algorithms (treemap, rectangle packing, street-based) arrange elements by structural hierarchy. This places structurally adjacent elements together regardless of their semantic relationship. Conceptually related code in different packages ends up far apart.

- **Challenge**: How do you arrange code elements so that semantically related code is spatially close?
- **Insight**: NLP techniques can extract semantic similarity from source code
- **Without this**: Layout reflects structure only; semantic clusters are scattered

## Definition

A layout algorithm that positions code elements based on semantic similarity extracted from source code (identifiers, comments) using NLP techniques like LDA topic modeling, rather than structural hierarchy.

## Mechanism (Solution)

**Input**: Source code files/classes with identifiers and comments

**Process**:
1. Tokenize and preprocess source code (extract identifiers, split camelCase, remove stopwords)
2. Apply topic modeling (LDA) to extract topic distributions per file
3. Compute pairwise semantic similarity matrix
4. Apply dimensionality reduction (t-SNE, UMAP, MDS) to project to 2D/3D coordinates
5. Position elements at computed coordinates

**Output**: Spatial arrangement where semantically similar elements cluster together

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Reveals semantic clusters across structural boundaries | Loses structural hierarchy information |
| Enables discovery of related code in different packages | Depends on identifier/comment quality |
| Can be combined with other visual encodings | Expensive preprocessing (NLP + dim reduction) |
| Position reflects conceptual relationships | Non-deterministic (different runs may vary) |

**Complexity**: High - requires NLP pipeline and dimensionality reduction
**Performance**: O(n^2) for similarity matrix; dim reduction adds overhead
**Cognitive Load**: Medium - positions need explanation since not structural

## Open Questions

- Optimal topic count for LDA on source code
- Best dimensionality reduction technique for code similarity
- How to handle incremental updates without layout instability
- Combining semantic layout with structural grouping

## Sources

- [CC157] Atzberger et al. VINCI 2021 - LDA-based layout for Software Galaxies

## See Also

- [[treemap-layout]] — structural hierarchy layout
- [[coupling-layout]] — dependency-based layout (related but uses coupling, not semantics)
- [[galaxy-metaphor]] — metaphor that uses this layout
