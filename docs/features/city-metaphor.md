---
id: F001
title: City Metaphor
category: metaphor
status: canonical
maturity: established
bounded_context: [city-metaphor]
introduced_by: CC023
implementations: [Software World, Component City, CodeCity, Vizz3D, SkyscrapAR, UML-City, VizzAspectJ-3D, EvoStreets, SynchroVis / ExplorViz, CityVR, VR City, Code Park, High-Rise, LD-City, CodeCharta, CodeMetropolis, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, m3triCity, VariCity / VariMetrics]
related_features: [F017, F002, F038, F003, F004, F005, F006, F008]
supersedes: []
taxonomy:
  granularity: [file, class, function, component]
  visual_element: [building, district, street, platform]
  metric_category: [size, complexity, coupling, evolution, behavior, variability]
last_updated: 2026-01-05
updated_from: [CC009, CC015, CC017, CC018, CC020, CC023, CC024, CC025, CC035, CC036, CC038, CC040, CC053, CC059, CC091, CC092, CC093, CC102, CC104, CC085, CC002, CC045]
---

# City Metaphor

## Problem & Motivation

CC023 motivates the metaphor as a way to restore **locality** in 3D software visualization: instead of freely movable objects in space (which can cause disorientation), the city provides well-defined placement rules in a familiar spatial context.

CC085 builds on the same motivation explicitly in terms of **habitability** and locality for program comprehension, arguing that a city-like “place” with strong orientation points and constrained navigation can help developers feel “at home” in a system during incremental exploration.

CC035 extends this motivation by emphasizing **habitability**: a “place” that supports incremental familiarity during exploration, reducing disorientation risks typical of unconstrained 3D environments.

CC002 provides a modern industry-motivation framing: code cities can serve as a **shared metaphor** for team communication and faster orientation, and they can act as a spatial “substrate” for layering other analysis results (e.g., dependency overlays) on top of the familiar cityscape.

CC020 reinforces the same rationale in a tool-demo framing: cities provide familiar orientation points and support incremental exploration; it also explicitly argues against starting with low-level class internals (“one does not start by looking into particular houses”).

CC024 similarly emphasizes incremental exploration and uses the “nutshell” description to connect the city overview to practical follow-up exploration via contextual menus and a query mechanism.

The metaphor works because:
- Cities are semi-planned artificial constructs (like software)
- Humans have strong spatial memory for navigation
- Building size/shape intuitively conveys magnitude
- District organization maps to hierarchical structure

## Definition

A visualization paradigm that depicts software systems as cities, leveraging human spatial cognition and familiarity with urban environments to make abstract code structures tangible and navigable. Software entities become buildings, organizational structures become districts, and the resulting cityscape enables intuitive understanding of system size, structure, and properties.

## Context & Applicability

**Use when:**
- You need a high-level structural overview and orientation for large systems (thousands of entities), leveraging locality and spatial memory (CC023, CC035).
- You want a shared spatial metaphor to communicate structure and hotspots across a team, and a substrate for layered overlays (CC002, CC023).
- You plan to combine structural context with additional analyses (quality, evolution, dependencies) in one navigable scene (CC035, CC023).

**Avoid when:**
- The primary task is reading/writing detailed code or long text; city views complement (not replace) IDE workflows (CC023, CC009).
- The system lacks a meaningful containment structure for the chosen granularity (packages/folders), so the metaphor would mislead (CC023, CC035).

**Prerequisites:** A structural model (packages/classes/files/functions) plus at least one metric; a concept mapping + property mapping; a layout algorithm; and basic navigation/selection interactions.
**Alternatives:** [[island-metaphor]] for bundle/module archipelagos; [[software-landscape-view]] for multi-application landscapes; [[clothing-metaphor]] for non-spatial class metaphors; 2D-first maps when 3D navigation cost is too high.

## Forces

| Force | Pull |
|-------|------|
| Familiarity vs. accuracy | Lean on a familiar “city” mental model for faster orientation, but avoid implying semantics the code does not have. |
| Overview scalability vs. inspection detail | Fit thousands of entities into one view, but accept that fine-grained code/relationships must be on-demand. |
| Locality vs. travel cost | Constrain navigation to preserve spatial memory (“habitability”), but mitigate the time cost of moving long distances. |
| Overlay expressiveness vs. visual clutter | Layer multiple analyses onto a stable city substrate, but prevent channel conflicts (especially color) and occlusion. |

## Mechanism (Solution)

**Input**: Software system model (classes, packages, metrics)

**Process**:
1. Map software entities to city elements (concept mapping)
2. Map entity properties to visual attributes (property mapping)
3. Arrange elements spatially using layout algorithm
4. Render as 3D visualization

**Output**: Interactive 3D city visualization

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Provides an intuitive mental model for structure. | Metaphor can oversimplify or mislead. |
| Supports orientation via spatial cues. | Different users may interpret metaphors differently. |

**Complexity**: Medium
**Performance**: Depends on rendering scale and navigation.
**Cognitive Load**: Medium (requires mapping concepts to visuals).

## Variations

| Implementation | Primary Entity | District Concept |
|----------------|----------------|------------------|
| CodeCity | class | package |
| Software World | method | class |
| EvoStreets | class | directory (via streets) |
| Code Park | class | n/a (navigation focus) |
| CodeCharta | file | folder |
| JSCity | function | folder (and file as sub-district) |
| SoftVis3D | file | folder/package |
| m3triCity | class | package |

## Implementation Notes

- Choose the primary granularity (class vs file vs function) based on language and target tasks (CC023, CC035, CC036, CC091).
- Provide sane default encodings (height/base/color) and scaling/discretization options to keep overviews readable (CC023, CC035, CC085).
- Optimize for scalability (simple glyphs, batching/culling/LOD) and preserve locality with constrained navigation (CC023, CC085).
- Support shareable/reproducible views via configurations/presets or view-state serialization (CC024, CC040, CC091).

## Evidence

CC023 provides a foundational end-to-end realization (CodeCity) and demonstrates the approach on large systems; CC015 later surveys 14 implementations across research groups.

CC018 (a systematic mapping study) reports continued community activity around the city metaphor, screening 406 citing publications and extracting categorial information from 168. It also reports that most identified tools do not use extended reality (85% non-XR), highlighting both growth and a technology gap.

CC053 describes ExplorViz using the city metaphor at the application level (within a broader software-landscape visualization) and exploring collaborative interaction styles, including multi-user VR for joint comprehension tasks.

CC025 reports a controlled experiment (CodeCity vs. Eclipse+Excel baseline) across two real-world Java systems (FindBugs “medium” and Azureus “large”). After outlier removal (n=41), a two-way ANOVA shows a significant main effect of tool on correctness (F(1,37)=14.722, p=.001) and completion time (F(1,37)=4.392, p=.043), with no tool×system-size interaction on correctness (F(1,37)=.034, p=.862). Reported deltas are +24.26% correctness (5.968 vs 4.803 points) and −12.01% completion time (36.117 vs 41.048 minutes).

CC009 reports a controlled experiment comparing a desktop (Code2City) and VR (Code2CityVR, Oculus Rift) implementation of the city metaphor against Eclipse, focusing on feelings/emotions and post-task thinking measures. It finds significantly higher positive affect for the VR condition versus Eclipse, but also reports frequent VR side effects (e.g., headache, nausea, visual annoyance).

CC036 adapts the city metaphor to JavaScript by switching to function-level buildings and representing nested functions as stacked buildings. It also demonstrates a browser-based implementation approach (Three.js) and reports experience producing visualizations for 40 popular JavaScript systems.

## Known Limitations

Current challenges:
- VR headsets inadequate for displaying large quantities of text
- Bifurcation between high-text desktop and low-text VR implementations

## Open Questions

- What is the right balance between in-scene text (labels/tooltips) and IDE-linked detail views, especially in VR?
- How stable does a city layout need to be across versions before users can reliably compare evolution in the same “place”?
- Which overlay channels (color/texture/geometry) should be reserved for “analysis” vs “interaction” (tagging/highlighting) to avoid misinterpretation?
- When do alternative metaphors (islands/landscapes/2D maps) outperform cities for specific tasks (dependencies, architecture, runtime behavior)?

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — foundational approach and CodeCity tool
- [CC085] Wettel & Lanza (ICPC 2007) — habitability/locality framing and mapping strategy discussion
- [CC017] Wettel CodeCity homepage — city metaphor overview (classes as buildings, packages as districts)
- [CC018] Moreno-Lumbreras et al. (JSS 2024) — systematic mapping of city metaphor influence and tool characteristics (incl. XR trend)
- [CC053] Hasselbring et al. (Software Impacts 2020) — ExplorViz application-level city metaphor + collaboration/VR context
- [CC025] Wettel & Lanza (ICSE 2011) — controlled experiment evaluating CodeCity vs. IDE+spreadsheet baseline
- [CC045] Mortara et al. (JSS 2024 preprint) — VariCity/VariMetrics: configurable city metaphor for variability and quality overlays
- [CC035] Wettel PhD thesis — habitable city metaphor + tool support + controlled experiment
- [CC009] Romano et al. (2019) — Code2City/Code2CityVR tool description and controlled experiment on affect/thinking
- [CC015] Jeffery survey — later comparison of multiple city-metaphor implementations
- [CC091] CodeCharta docs — modern open-source city-metaphor implementation (files/folders, treemap/street layouts)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — city-metaphor rationale + CodeCity overview framing
- [CC024] Wettel & Lanza (WASDeTT 2008) — city-metaphor recap + interaction via queries/menus
- [CC036] Viana et al. (arXiv 2017) — city-metaphor adaptation for JavaScript (functions + nested functions) and browser-based visualization
- [CC038] SoftVis3D website — SonarQube-integrated city metaphor (folders/packages as districts; files as buildings)
- [CC040] SoftVis3D repository — implementation details for a SonarQube-integrated code city
- [CC059] Pfahler et al. (2020) — web-based “evolving software city” platform (m3triCity)
- [CC092] GoCity website — positions GoCity as a Code City metaphor for Go source code in 3D
- [CC093] GoCity repository — confirms GoCity as a Code City implementation (Go source code in 3D)
- [CC104] GoCity SANER 2019 — GoCity adaptation of the city metaphor for Go
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis Minecraft-based city visualization
- [CC002] Galois blog post (2024) — industry framing of code cities as shared metaphors; suggests layering additional analysis results onto the cityscape

## See Also

- [[class-as-building]] — common entity mapping
- [[height-mapping]] — encoding metrics in building height
- [[treemap-layout]] — common spatial arrangement
