---
id: F015
title: Evolution Visualization
category: analysis
status: canonical
introduced_by: CC035
implementations: [CodeCity, EvoStreets, CrocoCosmos, SkyscrapAR, VR City, CodeCharta, SoftVis3D, m3triCity, Langelier Quality Visualization Framework, Getaviz, BabiaXR-CodeCity, Trend Maps (UE4 prototype)]
related_features: [F001, F006, F031, F032, F033, F039]
taxonomy:
  granularity: [file, class, package, method]
  visual_element: [building, street, brick]
  metric_category: [evolution]
last_updated: 2026-01-05
updated_from: [CC015, CC035, CC038, CC040, CC059, CC075, CC091, CC106, CC116, CC131, CC134, CC034, CC054, CC066, CC100, CC101]
---

# Evolution Visualization

## Definition

Visualization of how a software system changes over time (e.g., origin date, churn, authorship, modification date), using the city as a spatial context for temporal information.

## Mechanism

**Input**: Version-control or repository-derived history (dates, churn, authors).

**Process**:
1. Compute evolution-related properties per entity.
2. Map them to geometry/topography or visual encodings (e.g., elevation, height, color/brightness).
3. Provide views to compare or focus on time slices.

**Output**: A city that exposes change-over-time signals.

## Evidence (from CC015)

CC015 describes:
- CodeCity being used for studying evolution over time.
- EvoStreets encoding origin date via elevation/topography and listing module age / last modification date / author.
- SkyscrapAR mapping churn (code change volume) into the visualization.
- VR City supporting revision-log information such as author commits.

CC131’s Getaviz README states that generated visualizations can be enriched with evolutionary information from git and svn repositories and supports tracking changes across multiple versions. The generator component also accepts a Hismo model as an optional input alongside FAMIX (structure).

## Variations (SoftVis3D, from CC038)

CC038 describes a “Leak period” profile intended to focus on new code (e.g., new LOC and new issues) and an “Evostreet” stable layout for evolving systems. It also notes that author/commit signals are derived from SCM blame info (current lines only, no SCM history).

CC040 defines a dedicated leak-period commit signal (`number_of_commits`) as “number of commits during the current leak period”, computed from SCM blame information loaded via SonarQube.

## Evidence (from CC106)

CC106 describes VR City’s evolution animation over a selected commit range:
- Users specify a commit interval by date or SHA; commits are sampled via Git.
- Authors are visualized as colored spheres moving between waypoints computed from the centroid of modified classes.
- Users can pause the animation to inspect modifications (including browsing code), and apply filters (e.g., focus on selected authors or selected buildings).

CC106 also notes two constraints of the current implementation:
- Building positions are kept fixed during the animation (no re-layout).
- Classes created and removed outside the current revision do not appear in the animation.

## Evidence (from CC035)

CC035 details three concrete evolution techniques implemented in CodeCity:
- [[age-map]] — color overlay encoding artifact age
- [[time-travel]] — stepping through versions with stable spatial placement (locality)
- [[timeline-visualization]] — side-by-side version timelines (fine-grained)

CC116 presents the same three techniques as a focused evolution-visualization approach (coarse + fine grained), and reports case studies on ArgoUML, JHotDraw, and Jmol with findings confirmed by developers.

## Evidence (from CC091)

CC091 documents CodeCharta supporting evolution analysis by generating maps from VCS history (e.g., Git/SVN log parsers) and by providing a dedicated [[delta-comparison]] view to compare two snapshots (two maps).

## Evidence (from CC059)

CC059 presents m3triCity as an evolution-first city visualization for Git repositories:
- Uses a history-resistant (stable) layout to avoid version-to-version “layout jumps” when stepping through time.
- Explicitly visualizes structural refactorings (moves/renames) as movements between positions (with arcs via 3D edge bundling).
- Provides interactive evolution controls, including time bucketing and a timeline view that supports jumping to specific points in history.

## Evidence (from CC100)

CC100 describes an “evolving software cities” approach where the **layout itself** incorporates development history so history becomes visible in a smooth, stable way across versions. The city then serves as a platform for overlaying product and process data to create specialized history-oriented visualizations.

## Evidence (from CC101)

CC101 expands the “consistent software cities” approach with EvoStreets layouts that encode evolution directly in the street structure while keeping positions stable across versions. It also presents thematic evolution views such as modification-history maps (height = number of modifications, color = last-modified recency) layered on the stable layout to support maintenance and quality analysis.

## Evidence (from CC075)

CC075 uses multi-version visualizations to analyze package/program evolution, rendering successive versions side-by-side to identify growth patterns and refactoring needs.

## Evidence (Trend Maps, from CC054)

CC054 introduces “trend maps”, which extend a software map of a selected revision to visualize metric changes over a revision range in a single view:
- Computes per-entity metric time series across revisions and aggregates values bottom-up for group-level trends.
- Computes a trend value (linear-regression slope in CC054) and discretizes trends into five levels (strong increase → strong decrease).
- Encodes trend levels using natural-phenomena-inspired effects (item-based surface materials and context-based particle systems).

CC054 notes a conceptual limitation: trends are shown only for entities present in the chosen revision within the range; added/removed entities within the range are not fully represented.

## Notes (from CC066)

CC066 (a software-architecture visualization survey) summarizes additional evolution visualizations that reuse the city metaphor, including an “evolving software cities” variant where streets represent packages and building plots represent classes. It also notes extensions using contour-line “evolution maps” for versions and a modification-history map combining contour lines with towers (height = number of modifications; color = modification date).

## Evidence (BabiaXR-CodeCity, from CC134)

CC134 includes a time-evolution mode for a web-based software city (`babiaxr-codecity`): snapshots are keyed by date and optional commit SHA and can be stepped automatically or via UI events, updating and optionally animating per-entity geometry across versions.

CC034 describes the same line of work as a web-based CodeCity prototype focused on time evolution. It emphasizes keeping building positions stable by updating area/height using unique per-building identifiers, leaving empty terrain for buildings that do not exist in earlier snapshots, and leveraging A-Frame’s built-in VR mode for in-city navigation and interaction.

## Sources

- [CC035] Wettel PhD thesis — detailed evolution techniques (age map, time travel, timeline)
- [CC015] Jeffery survey — later overview mentioning evolution uses across tools
- [CC091] CodeCharta repo/docs — VCS history parsers and delta comparison between two maps
- [CC106] Vincúr et al. (QRS-C 2017) — VR City evolution animation with author waypoints and filtering
- [CC038] SoftVis3D website — leak-period and SCM-blame-based evolution signals
- [CC040] SoftVis3D repository — leak-period commit metric definition + SonarQube SCM API integration
- [CC059] Pfahler et al. (2020) — history-resistant layout + refactoring-aware evolution visualization (m3triCity)
- [CC075] Langelier et al. (ASE 2005) — evolution analysis via multi-version software maps
- [CC054] Würfel et al. (CGVC 2015) — trend maps: natural-phenomena effects to communicate metric trends over revision ranges
- [CC066] Khan et al. (VLUDS 2011) — survey notes on software-city evolution variants and related evolution visualizations
- [CC100] Steinbrückner & Lewerentz (SOFTVIS 2010) — history-aware layout for “evolving software cities” and integrated development-history visualizations
- [CC101] Steinbrückner dissertation — EvoStreets evolution-aware layouts and modification-history thematic maps
- [CC116] Wettel & Lanza (WCRE 2008) — visual exploration of large-scale system evolution (age map, time travel, timeline)
- [CC131] Getaviz repository — git/svn evolution enrichment and Hismo model input for evolutionary views
- [CC134] BabiaXR repository — time-evolution snapshots for a web-based software city (`babiaxr-codecity`)
- [CC034] Moreno-Lumbreras et al. (Benelux 2019) — early BabiaXR CodeCity time-evolution prototype and stable-identifier updates

## See Also

- [[dynamic-visualization]] — runtime behavior (distinct from evolution over versions)
