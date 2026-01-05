---
id: F007
title: Base (Footprint) Mapping
category: mapping
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, CodeCharta, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, SoftViz3D, m3triCity]
related_features: [F001, F005, F018]
supersedes: []
taxonomy:
  granularity: [file, class]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-05
updated_from: [CC009, CC015, CC020, CC023, CC024, CC035, CC036, CC038, CC040, CC043, CC059, CC091, CC093, CC102, CC104]
---

# Base (Footprint) Mapping

## Problem & Motivation

CC023 maps a second size-related metric into building footprint (e.g., NOA), letting users distinguish “tall” from “wide” structures (e.g., many-attribute classes appearing as platforms/“parking lots”). Footprint provides a complementary quantitative channel to height for overview comparisons (CC023, CC020).

## Definition

A property mapping where a building’s footprint (length/width/area) encodes a metric, allowing a second quantitative dimension alongside height.

## Context & Applicability

**Use when:**
- You need two independent metric encodings on a single building (e.g., NOM vs NOA; size vs complexity) (CC023).
- You want footprint/area to convey “mass” while height conveys another dimension (CC023, CC091).

**Avoid when:**
- Variable footprints would make districts unreadable or cause excessive re-layout churn under evolution unless positions are stabilized (CC059).
- The footprint metric would produce extreme sizes that dominate packing unless scaled/binned (CC023, CC040).

**Prerequisites:** A numeric metric mapped to area/width/length, a minimum/maximum footprint policy, and a layout algorithm that can pack variable footprints (CC023, CC040).
**Alternatives:** [[color-mapping]] / [[texture-mapping]] for a second channel without changing footprint; [[discretized-metric-mapping]] to cap extremes; [[height-mapping]] if only one geometric channel is needed.

## Forces

| Force | Pull |
|-------|------|
| Extra encoding capacity vs. layout distortion | Footprint adds a second quantitative channel, but variable bases affect packing and can destabilize perceived structure. |
| Salience vs. pickability | Very small footprints are hard to select; very large footprints dominate districts and hide neighbors. |
| Cross-version stability vs. responsiveness | Updating footprints reflects metric change, but can trigger repacking and “movement noise” in evolution views. |

## Mechanism (Solution)

**Input**: Numeric metric value.

**Process**: Scale a footprint dimension (or area) based on the metric, then render the building with that footprint.

**Output**: Buildings whose “base size” communicates a metric.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Adds a second geometric channel (paired with height) for richer overviews. | Humans judge area less accurately than height; requires legends/tooltips and sensible scaling. |
| “Wide vs tall” contrasts can surface structural differences (e.g., many-attribute vs many-method classes). | Large bases can crowd out neighbors and amplify layout churn under evolution unless stabilized. |

**Complexity**: Low
**Performance**: Typically cheap; depends on recomputation frequency.
**Cognitive Load**: Low–Medium (depends on legend/scale).

## Implementation Notes

- Prefer mapping to **area** and deriving near-square side lengths to avoid extreme aspect ratios; enforce minimum sizes for pickability (CC023).
- Apply scaling/bucketing options (linear/log/discretized) to keep packing stable under outliers (CC023, CC040).
- When footprint changes across versions, consider stable-layout strategies (preallocation) to avoid disruptive re-packing (CC059).

## Evidence

CC023 maps width and length to number of attributes (NOA), making “many attributes / few methods” classes appear like platforms (“parking lots”).

CC009 describes the same mapping in Code2City/Code2CityVR: building base size reflects NOA.

CC020 describes the same mapping in CodeCity: number of attributes is mapped to both width and length (the building’s footprint).

CC024 repeats the same mapping in a “nutshell” description of CodeCity (NOA mapped to base size).

CC036 maps the number of variables (NOV) to the building footprint/width for function-level buildings in JSCity.

CC093 maps the number of variables (NOV) to the building base size in GoCity. CC104 describes the same mapping using “number of attributes/fields” for structs (and for methods/attributes declared outside structs in files), which is consistent with Go’s field/variable terminology.

CC102 maps method cyclomatic complexity (McCC) to floor width and length in CodeMetropolis (method-as-floor representation).

CC091 documents CodeCharta mapping a user-selected “area” metric to the building footprint/area for file nodes.

CC038 describes SoftVis3D mapping a selected SonarQube metric (default: complexity) to building footprint for file buildings.

CC040 further shows SoftVis3D applying selectable scaling strategies (logarithmic/exponential/linear) to the footprint (mapped to both width and length).

CC043 maps an input metric to the building footprint side length in its 2D layout phase; in its dependency view, node footprint is derived from dependency counters and edge thickness is scaled by dependency counts.

CC059 describes choosing a metric for the **depth** of cuboids (in addition to height), making footprint/depth a configurable mapping parameter in m3triCity.

## Variations

| Implementation | Footprint metric | Notes |
|----------------|------------------|-------|
| CodeCity | NOA | Canonical “attributes → width/length” mapping (CC023, CC020). |
| JSCity / GoCity | NOV / fields | Function/file/struct variable counts mapped to footprint in non-class granularity (CC036, CC093, CC104). |
| SoftVis3D | configurable (e.g., complexity) | Profile-driven footprint metric with selectable scaling strategies (CC038, CC040). |
| CodeCharta | user-selected “area” metric | Treats footprint as an interactive mapping dimension (CC091). |

## Known Limitations

- Humans are less accurate at judging area than height; tooltips/legends help interpret footprint values.
- Large footprints can crowd out neighbors and dominate district layouts, hiding smaller entities (CC023).
- Footprint changes can imply layout changes, complicating evolution comparisons unless positions are stabilized (CC059).

## Open Questions

- What footprint scaling defaults best preserve both pickability and fair area comparison under heavy-tailed metric distributions?
- How should footprint changes be handled in evolution views (freeze footprint, stabilize layout, or animate repacking) to avoid misleading movement?
- When is it better to map the second metric to non-geometric channels (color/texture) instead of footprint?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — NOA mapped to footprint
- [CC035] Wettel PhD thesis — magnitude mapping (NOA → width and length)
- [CC015] Jeffery survey — later description of the same mapping
- [CC091] CodeCharta docs — interactive selection of area metric for building footprint
- [CC009] Romano et al. (2019) — NOA mapped to building base size in Code2City/Code2CityVR
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — number of attributes mapped to building width+length (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — NOA mapped to base size in CodeCity overview description
- [CC036] Viana et al. (arXiv 2017) — NOV mapped to footprint/width for function-level buildings in JSCity
- [CC038] SoftVis3D website — configurable footprint metric for file buildings (default: complexity)
- [CC040] SoftVis3D repository — footprint scaling strategies and width+length mapping rule
- [CC043] SoftViz3D repository — footprint side length derived from input metrics/counters (structure and dependency views)
- [CC059] Pfahler et al. (2020) — configurable depth metric for cuboids in m3triCity (paired with height)
- [CC093] GoCity repository — NOV mapped to footprint/base size
- [CC104] GoCity SANER 2019 — struct/file attributes mapped to base size
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis maps McCC to floor width/length

## See Also

- [[height-mapping]] — typically paired with base mapping for two metrics
- [[class-as-building]] — common granularity where base mapping is practical
