---
id: F017
title: Package-as-District Mapping
category: mapping
status: canonical
maturity: established
bounded_context: [city-metaphor]
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, CodeCharta, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, m3triCity, SecCityVR]
related_features: [F001, F002, F008, F021]
supersedes: []
taxonomy:
  granularity: [package]
  visual_element: [district]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC009, CC017, CC020, CC023, CC024, CC035, CC036, CC038, CC040, CC059, CC091, CC093, CC102, CC104, CC069]
---

# Package-as-District Mapping

## Problem & Motivation

Grouping buildings into districts provides the primary spatial structure of a city metaphor. CC023 maps packages to districts so related classes are co-located, supporting orientation and scalable navigation across large systems.

## Definition

A concept mapping where each package is rendered as a city district (a grouped ground area) that contains buildings for the package’s classes.

## Context & Applicability

**Use when:**
- Package/directory structure reflects meaningful modularization and is a natural navigation unit (CC023, CC035).
- You want overlays (quality/evolution/security) to align with structural boundaries (CC023, CC069).

**Avoid when:**
- Package/folder organization is noisy (generated code, monorepo conventions) or does not match architectural components (CC035).
- You need grouping by a different principle (ownership, variability, recovered components) rather than namespace structure.

**Prerequisites:** A containment hierarchy (packages/folders) and a layout strategy for placing subpackages and leaf buildings within each district (CC023).
**Alternatives:** [[configurable-grouping]] for non-namespace groupings, or [[street-layout]] where streets encode hierarchy instead of enclosed districts.

## Forces

| Force | Pull |
|-------|------|
| Structural fidelity vs. “accidental structure” | Use namespaces/folders as meaningful districts, but avoid reinforcing arbitrary repository conventions as architecture. |
| Nesting clarity vs. visual complexity | Show deep hierarchies faithfully, but prevent tiny/stacked districts from becoming unreadable. |
| Stable orientation vs. alternative groupings | Districts provide strong landmarks, but other tasks may require grouping by ownership, components, or variability. |

## Mechanism (Solution)

**Input**: Package hierarchy + contained classes.

**Process**:
1. Create a district region per package.
2. Place buildings (classes) inside the district via a layout algorithm.
3. For nested packages, apply layout recursively and use topology cues to reflect nesting.

**Output**: A city where package structure provides the primary spatial organization.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Creates the main spatial “neighborhood” structure that supports navigation and overview comprehension. | Can mislead when package/folder boundaries do not align with true components or responsibilities. |
| Provides natural containment boundaries for overlays (quality/evolution/security). | Deep nesting produces many small districts that are hard to select and reason about without additional cues/aggregation. |

**Complexity**: Low
**Performance**: Typically cheap; depends on recomputation frequency.
**Cognitive Load**: Low–Medium (depends on legend/scale).

## Implementation Notes

- Apply layout recursively per package; keep district borders and padding consistent for readability (CC023).
- Use topology cues for deep nesting (e.g., [[stacked-platform-topology]] or nesting-level shading) (CC023).
- Consider distinguishing first-party vs third-party code via district/platform styling in overlay-heavy views (CC069).

## Known Limitations

- Deep nesting can create many small districts that are hard to select and interpret; aggregation/summaries help (CC023).
- Packages/folders are not always a good proxy for architectural components; the city can reinforce accidental structure (CC035).
- Without clear nesting cues, recursively nested districts can be visually confusing (CC023).

## Variations

| Implementation | District unit | Notes |
|----------------|---------------|-------|
| CodeCity | package | Canonical mapping: packages become districts containing class buildings (CC023). |
| CodeCharta / SoftVis3D | folder | File-level cities reuse folder containment as districts (CC091, CC038). |
| JSCity | folder + file sub-districts | Adds an intermediate “file” containment level beneath folders (CC036). |
| SecCityVR | package platforms | Uses package platforms/districts with additional styling to distinguish dependency code (CC069). |
| CodeMetropolis | namespace plates | Uses treemap-like “plates” as containment regions (CC102). |

## Evidence

CC023’s foundational CodeCity mapping uses packages as districts to preserve locality and provide a scalable navigation unit; CC035 reiterates the rationale and discusses when package boundaries do (and do not) align with meaningful components.

## Open Questions

- When should a tool recommend switching from namespace-based districts to recovered components or ownership-based groupings?
- How should district boundaries be visualized in very deep hierarchies (stacked platforms, shading, minimaps) without overloading the scene?
- What defaults help users detect “bad modularization” (e.g., tangled dependencies) when districts are based on containment, not relations?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — packages as districts; classes as buildings
- [CC035] Wettel PhD thesis — concept mapping rationale + package-hierarchy organization
- [CC091] CodeCharta docs — folders as districts for file-level buildings
- [CC017] Wettel CodeCity homepage — packages depicted as districts
- [CC009] Romano et al. (2019) — Code2City/Code2CityVR (packages as districts)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — packages depicted as districts (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — CodeCity nutshell mapping (packages as districts)
- [CC036] Viana et al. (arXiv 2017) — directories as districts and files as sub-districts in JSCity
- [CC038] SoftVis3D website — folders/packages as districts for file buildings
- [CC040] SoftVis3D repository — district layout implementation (file leaf nodes, parent package/directory nodes)
- [CC059] Pfahler et al. (2020) — packages depicted as districts in an evolving web-based city (m3triCity)
- [CC093] GoCity repository — folders rendered as districts
- [CC104] GoCity SANER 2019 — directories as districts in GoCity
- [CC102] Balogh & Beszedes (2013) — namespace plates organized as treemap-like districts
- [CC069] Wueppelmann & Yigitbas (2025) — package platforms for SecCityVR with treemap/bin-packing placement

## See Also

- [[city-metaphor]] — districts are a core structuring element of a city view
- [[class-as-building]] — common inhabitants of districts
- [[treemap-layout]] — common containment layout used inside districts
- [[stacked-platform-topology]] — alternative nesting cue using altitude
- [[configurable-grouping]] — grouping beyond namespace/folder structure
- [[code-ownership-segmentation]] — alternative “district-like” segmentation by ownership
