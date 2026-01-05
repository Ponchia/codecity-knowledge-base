---
id: F067
title: Multiple Collaborative Representations (MCR)
category: interaction
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC057
implementations: []
related_features: [F042, F035, F023]
supersedes: []
taxonomy:
  granularity: [system]
  visual_element: [building, district]
  metric_category: [behavior]
last_updated: 2026-01-05
updated_from: [CC057]
---

# Multiple Collaborative Representations (MCR)

## Problem & Motivation

This capability helps support collaborative program/system comprehension with shared context. A collaboration paradigm for immersive software visualization where participants can create and tailor their **own** representations (views) of the same underlying data during a shared session, rather than being limited to a single shared representation. Without it, collaboration relies on external coordination (screen sharing, meetings) and shared context is harder to maintain.

## Definition

A collaboration paradigm for immersive software visualization where participants can create and tailor their **own** representations (views) of the same underlying data during a shared session, rather than being limited to a single shared representation.

## Mechanism (Solution)

**Input**: A shared dataset to explore and multiple collaborating users (often in immersive VR).

**Process**:
1. Allow each collaborator to construct and modify a representation suited to their focus (e.g., different metrics, filters, or structural perspectives).
2. Maintain awareness/coordination so collaborators can compare or communicate insights across their individualized views.
3. Use the division of perspectives to reduce per-user complexity, letting team expertise partition the system’s many dimensions.

**Output**: Collaborative analysis where multiple tailored views can coexist and be used to jointly solve comprehension/maintenance tasks.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables details-on-demand workflows. | Adds UI/interaction complexity. |
| Reduces cognitive load by filtering/focusing. | Can create mode errors if state is unclear. |

## Implementation Notes

CC057 positions MCR as an alternative to “everyone shares the same view” collaborative VR, aiming to increase the value of collaboration by enabling individually tailorable representations.

## Sources

- [CC057] Maletic et al. (ICSE 2001) — proposes MCR for collaborative immersive software visualization (Imsovision direction)

## See Also

- [[collaborative-multi-user-vr]] — synchronized multi-user exploration of a shared representation
- [[view-configuration]] — per-user configuration of mappings/layouts/views
