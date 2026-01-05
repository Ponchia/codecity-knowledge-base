---
id: F076
title: Galaxy Metaphor
category: metaphor
status: variant
maturity: research
bounded_context: [galaxy-metaphor]
introduced_by: CC157
implementations: [Software Galaxies]
related_features: [F001, F068]
supersedes: []
taxonomy:
  granularity: [file]
  visual_element: [star, nebula, constellation]
  metric_category: [size, complexity]
last_updated: 2026-01-05
updated_from: [CC157]
---

# Galaxy Metaphor

## Problem & Motivation

Traditional software city visualizations arrange code by structural hierarchy (packages, directories). This misses semantic relationships—files that are conceptually related but structurally distant appear far apart, while structurally adjacent but semantically unrelated files appear together.

- **Challenge**: How do you reveal semantic similarity between code elements?
- **Insight**: NLP techniques (LDA, topic modeling) can extract semantic similarity from source code identifiers and comments
- **Without this**: Users see only structural relationships, missing conceptual clustering

## Definition

A visualization metaphor that depicts software as a galaxy/constellation where files are rendered as stars and semantic clusters appear as nebulae, with spatial layout determined by semantic similarity (via NLP/LDA) rather than structural hierarchy.

## Context & Applicability

**Use when:**
- Semantic relationships matter more than structural hierarchy
- Exploring unfamiliar codebase to understand conceptual domains
- Finding files that address similar concerns across different packages

**Avoid when:**
- Package/directory structure is meaningful and should be preserved
- Users need to navigate by structural path
- Codebase has poor identifier naming (NLP won't extract useful semantics)

**Prerequisites:** Source code with meaningful identifiers/comments; NLP processing pipeline

**Alternatives:** [[city-metaphor]] for structural hierarchy; [[island-metaphor]] for modular systems

## Mechanism (Solution)

**Input**: Source code files with identifiers and comments

**Process**:
1. Apply Latent Dirichlet Allocation (LDA) to extract topics from source code
2. Compute semantic similarity between files based on topic distributions
3. Use dimensionality reduction (e.g., t-SNE, UMAP) to create 3D positions
4. Render files as stars/points; clusters as nebulae
5. Map metrics (LOC, complexity) to star size/brightness

**Output**: 3D galaxy where semantically related files cluster together regardless of structural location

## Consequences & Trade-offs

| Benefits | Liabilities |
|----------|-------------|
| Reveals semantic relationships invisible in structural views | Loses structural hierarchy context |
| Enables discovery of conceptually related but distant code | Depends on identifier quality |
| Novel aesthetic may engage users | Unfamiliar metaphor requires learning |
| Works across structural boundaries | NLP processing adds complexity |

**Complexity**: High - requires NLP pipeline and dimensionality reduction
**Performance**: Preprocessing is expensive; rendering is standard 3D
**Cognitive Load**: Medium - new metaphor to learn but leverages spatial intuition

## Variations

| Implementation | Variation | Notes |
|----------------|-----------|-------|
| Software Galaxies | LDA-based | Original research prototype (CC157) |
| Code Galaxies (Anvaka) | Dependency-based | Uses package dependencies, not NLP |

## Sources

- [CC157] Atzberger et al. VINCI 2021 - LDA-based galaxy metaphor for semantic similarity

## See Also

- [[city-metaphor]] — alternative emphasizing structural hierarchy
- [[island-metaphor]] — alternative for modular systems
- [[semantic-similarity-layout]] — the layout algorithm underlying this metaphor
