---
id: F064
title: Metaphor-Aware Navigation (Assisted Paths)
category: interaction
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC030
implementations: [CyberNet]
related_features: [F026]
supersedes: []
taxonomy:
  granularity: [class, package]
  visual_element: [building, district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC030]
---

# Metaphor-Aware Navigation (Assisted Paths)

## Problem & Motivation

This capability helps enable efficient details-on-demand and focused exploration in dense scenes. A navigation approach where movement and viewpoint controls are adapted to the metaphor (e.g., building/city) and embedded into the metaphor’s components, allowing the system to assist locomotion (and sometimes wayfinding) with metaphor-feasible paths that reduce disorientation. Without it, exploration becomes slower and more error-prone because users cannot inspect and act in-context.

## Definition

A navigation approach where movement and viewpoint controls are adapted to the metaphor (e.g., building/city) and embedded into the metaphor’s components, allowing the system to assist locomotion (and sometimes wayfinding) with metaphor-feasible paths that reduce disorientation.

## Mechanism (Solution)

**Input**: A metaphor hierarchy (metaphor tree), per-component navigation capabilities, and a target object of interest.

**Process**:
1. Associate navigation schemes with metaphor components (e.g., corridors vs floors vs districts), rather than relying on one generic 3D “browser” control scheme.
2. When a target is selected, optionally trigger assisted navigation where the system handles locomotion details.
3. For “path” travel, route the user along a feasible metaphor-consistent path (e.g., corridors/stairs; no wall/ceiling traversal) to preserve route knowledge and orientation.
4. Optionally support a “jump to” mode that moves the user directly to the target when constraints can be relaxed.
5. Support semantic navigation through the underlying hierarchy (e.g., up/down/next/previous) when there is a tight semantic↔metaphor binding.

**Output**: The user/camera is repositioned and oriented relative to the metaphor in a way that preserves spatial understanding while reducing manual navigation effort.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Enables details-on-demand workflows. | Adds UI/interaction complexity. |
| Reduces cognitive load by filtering/focusing. | Can create mode errors if state is unclear. |

## Sources

- [CC030] Russo dos Santos (Eurêcom/Telecom Paris thesis) — introduces “metaphor-aware navigation” and assisted navigation modes.

## See Also

- [[navigation-modes]] — fly/walk navigation levels (survey vs route knowledge) in city metaphors
