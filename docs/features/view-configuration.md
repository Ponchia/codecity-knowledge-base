---
id: F035
title: View Configuration
category: platform
status: canonical
introduced_by: CC035
implementations: [CodeCity, CodeCharta, SoftVis3D, m3triCity, CodeMetropolis, BabiaXR-CodeCity, Code Arcades, VariCity / VariMetrics]
related_features: [F005, F006, F008, F018, F063]
taxonomy:
  granularity: [package, class]
  visual_element: [district, building]
  metric_category: [size, complexity, coupling, evolution, quality, variability]
last_updated: 2026-01-04
updated_from: [CC020, CC024, CC025, CC035, CC038, CC040, CC059, CC086, CC091, CC103, CC098, CC130, CC134, CC026, CC045, CC120]
---

# View Configuration

## Definition

A configuration mechanism that lets users define what the city shows and how it is encoded (visibility, glyphs, layouts, and property mappers), enabling task-specific views without changing the underlying tool.

## Mechanism (from CC035)

**Input**: Per-element-type configuration (e.g., package/class/method).

**Process**:
1. Define visibility rules (which model elements appear).
2. Choose glyph types for each element type.
3. Choose layouts for containment levels.
4. Attach mappers to visual properties (dimensions, color, transparency, etc.).
5. Save/load configurations; represent them as source-code scripts to make them versionable and resilient to refactorings.

**Output**: Reusable, composable view specifications that generate different city visualizations.

## Notes (from CC024)

CC024 spells out a view configuration as a per-element-type specification of:
- Visibility (whether to render a model element type)
- Glyph type (which figure to use)
- Layout per containment level (e.g., package layout places sub-packages and classes)
- Visual mappers per glyph property

It also notes practical UI/management support:
- A preview panel that applies the current configuration to a dummy model for fast feedback.
- Saving configurations with a name/description and reusing them as a base for new ones.

CC024 also describes persisting configurations as **scripts** (mappers provide an `asScript` representation) and storing them as class-side methods (so they are versioned via the Smalltalk version-control mechanism “Store”).

CC120 reiterates the practical motivation for script-based persistence: earlier file-serialized configurations were not versioned and could break when classes used in the configuration were renamed.

CC086 provides the same core definition of view configurations as a per-model-element-type specification of visibility, glyphs, layouts, and visual mappers.

CC098 includes a dedicated configuration panel screenshot and describes using the view-configuration UI to tune visibility, glyphs, mappings, and layouts for reverse-engineering tasks.

## Variations (CodeCharta, from CC091)

CodeCharta’s Web Studio supports “Custom Views”: downloadable/uploadable configurations that store the current visualization settings (selected metrics for area/height/color, layout choices, and user interaction state like hidden/excluded items and marked packages) without modifying the underlying `cc.json` map.

## Variations (SoftVis3D, from CC038)

CC038 describes **profiles** that preset common metric selections (e.g., a “Default risk” profile and a “Leak period” profile). The example visualization links embed a `visualizationStatus` value (base64 JSON) that serializes configuration choices (layout, profile/metrics, color theme, file filters, and camera position), enabling shareable, reproducible views.

CC040 further shows this as a first-class UI feature (“Share” menu): users can copy/open a link that encodes the full view state, including selected object and camera position; a “plain” link can open the visualization outside the SonarQube chrome.

## Variations (m3triCity, from CC059)

CC059 describes a settings panel that lets users toggle the visibility of UI elements (e.g., title, date, commit message, pop-ups), choose the metrics used for geometry (e.g., depth and height), and adjust layout parameters such as minimum sizes and inter-object gaps (“bump”).

## Variations (CodeMetropolis, from CC103)

CC103 notes a **mapping file** that specifies which metrics drive visual attributes (e.g., height or material), with the format redesigned to support cleaner syntax and additional options. The Eclipse integration exposes settings for the mapping file location, indicating a configurable view specification externalized as a file.

CC130 further documents CodeMetropolis as a multi-stage toolchain where the mapping file (XML) is a first-class input to the `mapping` stage, supporting conversions such as normalization and quantization and binding multiple metrics to multiple visual attributes.

## Variations (BabiaXR, from CC134)

CC134 uses A-Frame component attributes as a view-configuration mechanism: visualizers expose which data fields map to visual properties (e.g., `babia-city` uses `farea` and `fheight`), and the `babia-ui` component can target a visualizer and present available metrics to switch these mappings at runtime.

## Variations (Code Arcades, from CC026)

CC026 describes Code Arcades providing an interactive configuration GUI that lets developers change rendering attributes (e.g., colors, dimensions, illumination, materials/textures) for packages, classes, methods (floors), and method arguments (windows). It also highlights a configurable grouping mechanism for organizing classes by namespaces or architecture-recovery-derived components.

## Variations (VariCity / VariMetrics, from CC045)

CC045 describes VariCity as providing configuration options that let users tailor the visualization to:
- choose **entry points** (and thereby focus on a subpart of the system),
- set **usage orientation** (IN / OUT / IN-OUT) and **usage level** (depth) for usage relationships,
- adjust which relationships are displayed by default vs on hover (to reduce clutter), and
- change visual settings and which metrics bind to building dimensions (e.g., height vs width).

It further describes VariMetrics as allowing users to choose which software-quality metrics to display, configure ranges/thresholds, and select display strategies (red↔green sequence, saturation, crackled texture) and combination rules (with a note that some bivariate color maps are difficult to read).

## Sources

- [CC035] Wettel PhD thesis — CodeCity “view configuration” mechanism and mapper architecture
- [CC025] Wettel & Lanza (ICSE 2011) — notes CodeCity can compose views by choosing metrics and artifact representations
- [CC091] CodeCharta docs — Custom Views (save/load/share display configurations per map)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — view configurations (elements, figure types, mappings, layouts)
- [CC024] Wettel & Lanza (WASDeTT 2008) — view configuration definition, preview UI, and script-based persistence
- [CC120] Wettel (FAMOOSr 2008) — view-configuration persistence as scripts and Store-tracked configuration repository
- [CC086] Wettel & Lanza (2008) — view configurations for tunable visualizations (visibility/glyph/layout/mappers)
- [CC038] SoftVis3D website — profile presets + URL-embedded view state (“visualizationStatus”)
- [CC040] SoftVis3D repository — share menu + URL serialization/deserialization of view state
- [CC059] Pfahler et al. (2020) — settings panel for toggling elements, choosing metrics, and tuning layout parameters in m3triCity
- [CC103] Balogh et al. (2015) - CodeMetropolis mapping file and integration settings
- [CC098] Wettel & Lanza (2008 tech report) — view configuration mechanism and configuration panel UI
- [CC130] CodeMetropolis repository — mapping XML examples and mapping-tool pipeline usage
- [CC134] BabiaXR repository — A-Frame component schemas + `babia-ui` for switching mapped metric fields at runtime
- [CC026] Savidis & Vasilopoulos (ICSEng 2025 preprint) — interactive configuration UI and configurable grouping mechanism
- [CC045] Mortara et al. (JSS 2024 preprint) — VariCity/VariMetrics configuration options for variability-focused views and quality overlays
