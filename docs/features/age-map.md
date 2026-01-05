---
id: F031
title: Age Map
category: analysis
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC116
implementations: [CodeCity]
related_features: [F015, F006, F032, F033]
supersedes: []
taxonomy:
  granularity: [class, method]
  visual_element: [building, brick]
  metric_category: [evolution]
last_updated: 2026-01-05
updated_from: [CC035, CC116]
---

# Age Map

## Problem & Motivation

Evolutionary age helps distinguish legacy code from newly introduced areas. CC116 uses age maps to color artifacts by how long they have survived across sampled versions, enabling quick identification of stable core parts versus new/volatile regions.

## Definition

An evolution overlay that colors city artifacts by “age” (how long an artifact has existed/survived across sampled versions), enabling quick identification of old vs newly introduced parts.

## Context & Applicability

**Use when:**
- You need to assess system growth, identify newly introduced features, or focus reviews on recent additions (CC116).
- You want to compare longevity at multiple granularities (class-level vs method-brick-level) (CC116, CC035).

**Avoid when:**
- History is incomplete or sampling is too coarse, making “age” misleading (CC116).
- Entity identity is unstable due to frequent renames/moves without tracking, causing ages to reset (uncertain).

**Prerequisites:** A sampled version history, stable entity identifiers across versions, and a sequential color map with legend (CC116, CC035).
**Alternatives:** [[time-travel]] and [[timeline-visualization]] for step-wise evolution exploration, or other [[evolution-visualization]] overlays (churn/authorship).

## Forces

| Force | Pull |
|-------|------|
| Interpretability vs. channel competition | Age colors are easy to scan, but compete with other overlays (smells, vulnerabilities, metric color mappings). |
| Sampling simplicity vs. temporal accuracy | Coarse sampling is cheap and stable, but can hide short-lived entities and distort “age”. |
| Identity continuity vs. refactoring reality | Stable IDs preserve age meaning, but renames/moves/splits challenge continuity without tracking. |

## Mechanism (Solution)

**Input**: Sampled version history + a reference version.

**Process**:
1. Compute each artifact’s age as the number of sampled versions it survived up to the reference version.
2. Map age to a sequential color scheme (new → old).

**Output**: A city where color encodes historical longevity.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Quickly distinguishes long-lived core areas from recent additions in spatial context. | Misleading when history is incomplete or identity tracking across refactorings is weak. |
| Supports layered reasoning when paired with structure (size) and other evolution views. | Uses the color channel, which may already be reserved for other encodings/overlays. |

**Complexity**: Medium
**Performance**: Depends on analysis pipeline and refresh cadence.
**Cognitive Load**: Medium–High (interpretation requires metric literacy).

## Implementation Notes

- Define the sampling strategy (versions/interval) and reference version; compute age as “survived sample count” (CC116).
- Use a perceptually ordered color scheme and keep it consistent across views; allow toggling coarse vs fine-grained age maps (CC116, CC035).
- Where possible, track moves/renames so age reflects continuity rather than delete+create (uncertain; see CC035 evolution model discussion).

## Evidence

CC116 applies age maps at two levels:
- **Coarse-grained age map**: colors classes/packages in the current city based on how long they have existed in the sampled history (used to reason about long-lived vs recently introduced parts).
- **Fine-grained age map**: colors method-level “bricks” to highlight which methods are old/new within a class over time.

## Variations

| Variation | Granularity | Notes |
|----------|-------------|------|
| Coarse-grained age map | classes/packages | Overview of old vs new areas at city scale (CC116). |
| Fine-grained age map | method bricks | Within-class longevity differences (“method generations”) (CC116, CC035). |

## Known Limitations

- Age depends on sampling granularity; coarse sampling can hide short-lived entities and overstate stability (CC116).
- Renames/moves can distort ages without identity tracking across versions (CC035).
- Color-based overlays compete with other overlays (smells/vulnerabilities); mode switching/legends are needed.

## Open Questions

- How should tools present confidence/uncertainty when identity tracking across refactorings is approximate?
- What sampling/bucketing defaults preserve useful “age” signals while keeping computation and UI manageable?
- How can age maps coexist with other color-driven overlays without forcing constant mode switching?

## Sources

- [CC035] Wettel PhD thesis — coarse- and fine-grained age map technique
- [CC116] Wettel & Lanza (WCRE 2008) — age map for large-scale system evolution (coarse + fine grained)

## See Also

- [[evolution-visualization]] — broader class of time-based views (churn, authorship, growth)
- [[time-travel]] — stable-layout stepping through versions
- [[timeline-visualization]] — compact per-version evolution context
