---
id: F006
title: Color Mapping
category: mapping
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC023
implementations: [CodeCity, Software World, UML-City, VizzAspectJ-3D, CityVR, VR City, CodeCharta, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, Langelier Quality Visualization Framework, SecCityVR, VariCity / VariMetrics]
related_features: [F001, F005, F025, F057]
supersedes: []
taxonomy:
  granularity: [file, class, function]
  visual_element: [building]
  metric_category: [size, complexity, coupling, evolution, behavior, quality, variability]
last_updated: 2026-01-05
updated_from: [CC009, CC015, CC020, CC023, CC024, CC035, CC036, CC038, CC040, CC075, CC091, CC106, CC093, CC104, CC069, CC045, CC117]
---

# Color Mapping

## Problem & Motivation

Color provides an additional low-cost channel for encoding metrics or categories on top of existing city geometry, enabling overlays without changing layout. CC023 and CC035 use color (and translucency) both for metric mapping and for interactive marking/tagging during exploration.

## Definition

A property mapping where color (hue/saturation/brightness and sometimes translucency) encodes an attribute of the represented software entity (e.g., visibility, LOC, author, complexity, dependencies).

## Context & Applicability

**Use when:**
- You need to encode a categorical attribute (type/smell/severity) or a secondary numeric metric while keeping geometry stable (CC023, CC035).
- You want to layer analysis results (quality/evolution/security) while preserving structural context (CC035, CC069).

**Avoid when:**
- Precise quantitative comparison is required without supplementary legends/tooltips (color alone is approximate).
- Too many overlays compete for the same color channel, creating semantic overload and ambiguous interpretations (CC035).

**Prerequisites:** A defined palette/scale and legend; consistent handling of missing values; and accessibility-aware choices (e.g., colorblind-safe palettes).
**Alternatives:** [[height-mapping]] / [[base-mapping]] for geometric encodings; [[texture-mapping]] for patterned materials; interactive highlighting via [[visual-tagging]].

## Forces

| Force | Pull |
|-------|------|
| Channel capacity vs. semantic overload | Color can encode many things, but reusing it across modes (smells, severity, metrics, tags) risks confusion. |
| Flexibility vs. consistency | Let users choose “color metric” per task, but keep meanings stable enough for collaboration and comparison. |
| Accessibility vs. expressiveness | Use vivid palettes for categorical overlays, but ensure color-vision deficiencies and display differences are handled. |

## Mechanism (Solution)

**Input**: Categorical or numeric property per entity.

**Process**:
1. Select a color encoding (binary, categorical palette, or continuous scale).
2. Apply the encoding to building surfaces and/or overlays.
3. Optionally provide view-dependent encodings (e.g., “complexity view” vs “dependencies view”).

**Output**: A city where color communicates additional information without changing geometry.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Low-cost overlay channel that preserves geometry and layout. | Easy to misread without legends; multiple overlays can collide on the same channel. |
| Supports categorical “issue” overlays (smells, severity) and secondary numeric metrics. | Colorblindness and display variance can reduce reliability; requires careful palette selection. |

**Complexity**: Low
**Performance**: Typically cheap; depends on recomputation frequency.
**Cognitive Load**: Low–Medium (depends on legend/scale).

## Variations

| Tool | Example encoding |
|------|------------------|
| CodeCity | CC035 documents LOC mapped to a dark-gray→blue scale for buildings and nesting-level mapped to district shading; color/transparency also used for interactive tagging and overlays (e.g., age maps, disharmony maps). |
| Code2City / Code2CityVR | CC009 describes LOC mapped to a dark-blue→light-blue scale for buildings; district shading indicates package nesting. |
| CodeCity | CC020 describes nesting level mapped to district color hue (darker for higher nesting levels). |
| JSCity | CC036 maps color to function kind (named vs anonymous) and uses distinct colors for container levels (directories vs files). |
| GoCity | CC104 maps element category to color (structs blue, files gray, directories red) and uses color intensity for LOC; CC093 reports darker buildings for higher LOC. |
| Software World | Lighter/darker building colors indicate public vs private. |
| UML-City | Metrics can be superimposed as vertical height, color, or shape (via MetricView). |
| VizzAspectJ-3D | Different color codings in complexity and dependencies views for classes/aspects. |
| CityVR | Brightness indicates LOC; source code can be displayed in a translucent HUD. |
| VR City | CC106 uses translucency + per-trace colors to highlight executed methods (floors) in “trace mode”; it also supports remodularization views by coloring buildings by package or semantic cluster (with related colors for subpackages). |
| CodeCharta | Users select a color metric interactively; the legend shows metric ranges and links to metric definitions when available. |
| SoftVis3D | CC038 describes configurable building colors for metrics such as complexity, coverage, issues, LOC, number of authors, and number of commits. CC040 defines per-metric green↔red rules (incl. clamped ranges for LOC/issues) and loads SCM blame info via SonarQube to compute `number_of_authors` and `number_of_commits` (commits during the leak period). |
| Langelier Quality Visualization Framework | Coupling (CBO) is mapped to a blue→red hue scale (low coupling → blue; high coupling → red). |
| SecCityVR | Vulnerability severity mapped to SpotBugs palette: red (high), orange (medium), green (low), blue (info). |
| VariCity / VariMetrics | CC045 uses color to distinguish hotspot/variation-point categories in VariCity and supports configurable quality-metric overlays in VariMetrics (red↔green sequence or saturation). |

## Implementation Notes

CC024 describes CodeCity’s package-color mapping as a linear mapping from “depth in hierarchy” (nesting level) onto a light-blue→dark-blue range (a ColorLinearMapper), producing intermediate shades across the spectrum.

## Evidence

- CC117 introduces disharmony maps that rely on vivid categorical colors for smell types while keeping structural metrics on geometry, illustrating the value (and contention) of the color channel for overlays.
- CC091 and CC038 show modern tools treating color as a user-configurable mapping (choose a “color metric” interactively / via profiles), reinforcing the need for clear legends and consistent semantics.

## Known Limitations

- Color perception varies by display/lighting and may fail for color-vision-deficient users; legends and palette choices matter.
- Multiple overlays using the same channel can create ambiguity; reserve palette semantics or use modes (CC035, CC117).
- Continuous scales can saturate/clamp and hide differences unless ranges are chosen carefully (CC040, CC091).

## Open Questions

- How should tools partition color usage between “metric mapping” and “issue overlays” (smells, vulnerabilities) without forcing constant mode switching?
- What are robust defaults for bivariate encodings (two metrics) that remain readable and accessible?
- How can collaboration/sharing preserve semantic meaning when users can freely remap the color channel?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — color saturation (nesting) and interactive tagging
- [CC035] Wettel PhD thesis — magnitude mapping (LOC + nesting level) and evolution/quality overlays
- [CC015] Jeffery survey — later survey of color/visual encodings across tools
- [CC091] CodeCharta docs — interactive selection of color metric and legend support
- [CC009] Romano et al. (2019) — LOC mapped to building color and nesting mapped to district shading (Code2City/Code2CityVR)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — nesting level mapped to district color hue (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — ColorLinearMapper UI and nesting-level→blue shade mapping
- [CC036] Viana et al. (arXiv 2017) — named/anonymous function colors and directory/file color coding in JSCity
- [CC038] SoftVis3D website — configurable metric-based building colors (incl. SCM blame-based author/commit signals)
- [CC040] SoftVis3D repository — color-metric definitions and implementation rules (ranges, SCM-based metrics)
- [CC075] Langelier et al. (ASE 2005) — CBO mapped to a blue→red color scale for classes
- [CC106] Vincúr et al. (QRS-C 2017) — VR City trace coloring, translucency, and remodularization color schemes
- [CC093] GoCity repository — LOC mapped to building color (darkness encodes high values)
- [CC104] GoCity SANER 2019 — category colors (struct/file/directory) and LOC intensity
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR colors vulnerable method floors by severity (SpotBugs categories)
- [CC045] Mortara et al. (JSS 2024 preprint) — VariCity hotspot coloring and VariMetrics quality overlays (red↔green, saturation)
- [CC117] Wettel & Lanza (SoftVis 2008) — disharmony-map overlays use vivid colors for smell types on top of city geometry

## See Also

- [[height-mapping]] — common complementary encoding
- [[source-code-display]] — source code shown via HUD/walls (often translucent)
- [[vulnerability-overlay]] — example of mapping SAST severity to color (SecCityVR)
