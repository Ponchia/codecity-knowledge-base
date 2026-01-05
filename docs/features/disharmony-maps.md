---
id: F034
title: Disharmony Maps
category: analysis
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC117
implementations: [CodeCity, Code2City, Code2CityVR]
related_features: [F006, F025, F037]
supersedes: []
taxonomy:
  granularity: [class, method]
  visual_element: [building, brick]
  metric_category: [quality]
last_updated: 2026-01-05
updated_from: [CC025, CC035, CC086, CC117, CC055, CC064]
---

# Disharmony Maps

## Problem & Motivation

Smell/disharmony result lists often lose the structural context needed for refactoring decisions. CC117 introduces disharmony maps to localize detection results in the city by coloring affected entities while keeping the surrounding structure neutral, enabling questions about distribution and dominant disharmony types.

## Definition

A design-quality visualization that overlays the software city with colors indicating detected design disharmonies (“code smells”), enabling an overview of the proportion, distribution, and dominant types of design problems while preserving structural context.

## Context & Applicability

**Use when:**
- You have disharmony/code-smell detection results and need to prioritize refactoring by where problems cluster (CC117, CC035).
- You want to correlate design problems with structural size/shape while preserving context (CC117).

**Avoid when:**
- Detection results are noisy or not calibrated for the codebase/language; the map may mislead (CC117).
- Too many disharmonies are highlighted simultaneously; filter by type/severity to avoid overload (CC086).

**Prerequisites:** A smell/disharmony detection pipeline producing per-entity labels and a vivid color palette mapping disharmony types to colors (CC117).
**Alternatives:** Other overlays such as [[vulnerability-overlay]] for security findings, or metric-only overlays via [[color-mapping]] / [[production-cost-overlay]].

## Forces

| Force | Pull |
|-------|------|
| Highlighting vs. channel conflict | Vivid smell colors make issues visible, but compete with color used for metrics, tagging, or other overlays. |
| Sensitivity vs. trust | Aggressive detection surfaces more potential issues, but false positives/negatives affect user trust in the visualization. |
| Overview clarity vs. multi-label complexity | Simple single-color per entity is readable, but entities with multiple smells can be hard to represent faithfully. |

## Mechanism (Solution)

**Input**: Detection-strategy results per entity (boolean/label per disharmony type), plus the city’s usual structural metric mappings.

**Process**:
1. Assign a vivid color per disharmony type.
2. Color affected entities with the disharmony color; render unaffected entities in neutral gray.
3. Keep structural metrics on geometry (e.g., height/footprint) while color encodes disharmony.

**Output**: A “map” of design problems embedded in the system’s spatial structure.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Makes smell hotspots visible in structural context, supporting prioritization and discussion. | Visualization inherits detector noise; false positives/negatives can mislead without calibration and explanation. |
| Preserves geometry-based structural cues while overlaying smell categories via color. | Multi-smell cases and strong palettes can overwhelm other encodings and reduce readability. |

**Complexity**: Medium
**Performance**: Depends on analysis pipeline and refresh cadence.
**Cognitive Load**: Medium–High (interpretation requires metric literacy).

## Variations

| Implementation | Variation | Notes |
|----------------|-----------|------|
| CodeCity | disharmony maps (neutral context + vivid smells) | Canonical “disease map” style with neutral grays for unaffected entities (CC086, CC117). |
| Code2City / Code2CityVR | smell-based coloring | Uses distinct colors for selected smell categories (e.g., brain/data/god classes) in a UE4-based city (CC055, CC064). |

## Implementation Notes

- Use vivid colors for disharmony types and render unaffected entities in neutral tones to preserve context (CC086, CC117).
- Provide toggles/filters per disharmony type to reduce overload and support targeted investigation (CC035).
- Keep structural metric mappings stable so users can interpret disharmony in context (CC117).

## Evidence

### Evidence (from CC086)

CC086 describes disharmony maps as being inspired by disease maps: use vivid colors to highlight detected “harmony breakers” while rendering unaffected entities in neutral grays to keep context present but non-distracting.

### Evidence (from CC117)

CC117 introduces disharmony maps as a way to localize detection-strategy results in context:
- Encode disharmony types in color while keeping structural metrics mapped to geometry (e.g., NOA/NOM).
- Support overview questions like **distribution** across packages and **dominant disharmony types**.
- Avoid the context loss of long textual result lists, and make it more feasible to correlate multiple disharmony types.

### Evidence (from CC055)

CC055 describes Code2City supporting smell-based coloring to help identify design problems, including distinct colors for brain classes, data classes, and god classes while keeping the city’s structural context.

## Known Limitations

- Visualization quality depends on smell detection quality; false positives/negatives propagate into the map (CC117).
- Single-color encodings can hide multi-label cases when an entity has multiple disharmonies (CC117).
- Strong overlays can overwhelm other encodings and reduce readability of the base city (CC086).

## Open Questions

- How should tools help calibrate/validate smell detection results per project (thresholds, explanations, false-positive review workflows)?
- What are readable encodings for multi-smell entities that do not collapse multiple labels into one color?
- How should disharmony maps combine with other “issue overlays” (security, architecture violations) without overwhelming the city?

## Sources

- [CC117] Wettel & Lanza (SoftVis 2008) — introduces disharmony maps for visual localization of design problems
- [CC035] Wettel PhD thesis — disharmony maps inspired by disease maps + multiple case studies
- [CC025] Wettel & Lanza (ICSE 2011) — disharmony-map example and design-problem tasks in controlled experiment context
- [CC086] Wettel & Lanza (2008) — disharmony-map explanation and example (vivid colors vs neutral context)
- [CC055] Code2City project report — smell-based coloring for brain/data/god classes in a UE4-based software city
- [CC064] Romano et al. (IST 2019) — controlled experiment paper documenting Code2City’s smell highlighting (brain/data/god classes)

## See Also

- [[color-mapping]] — primary channel used for smell categories
- [[visual-tagging]] — interaction-level coloring that can conflict with smell overlays
- [[vulnerability-overlay]] — analogous “issue overlay” for security findings
