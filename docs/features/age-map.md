---
id: F031
title: Age Map
category: analysis
status: canonical
introduced_by: CC116
implementations: [CodeCity]
related_features: [F015, F006, F032, F033]
taxonomy:
  granularity: [class, method]
  visual_element: [building, brick]
  metric_category: [evolution]
last_updated: 2026-01-04
updated_from: [CC035, CC116]
---

# Age Map

## Definition

An evolution overlay that colors city artifacts by “age” (how long an artifact has existed/survived across sampled versions), enabling quick identification of old vs newly introduced parts.

## Mechanism (from CC035)

**Input**: Sampled version history + a reference version.

**Process**:
1. Compute each artifact’s age as the number of sampled versions it survived up to the reference version.
2. Map age to a sequential color scheme (new → old).

**Output**: A city where color encodes historical longevity.

## Evidence (from CC116)

CC116 applies age maps at two levels:
- **Coarse-grained age map**: colors classes/packages in the current city based on how long they have existed in the sampled history (used to reason about long-lived vs recently introduced parts).
- **Fine-grained age map**: colors method-level “bricks” to highlight which methods are old/new within a class over time.

## Sources

- [CC035] Wettel PhD thesis — coarse- and fine-grained age map technique
- [CC116] Wettel & Lanza (WCRE 2008) — age map for large-scale system evolution (coarse + fine grained)
