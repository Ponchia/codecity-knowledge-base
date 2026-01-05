---
id: I003
name: CodeCity
origin: University of Lugano (USI), Switzerland
year_introduced: 2007
status: historical
source_refs: [CC015, CC017, CC020, CC023, CC024, CC025, CC035, CC085, CC086, CC098, CC116, CC117, CC005, CC121]
repo_url: null
demo_url: null
primary_language: Smalltalk (Moose framework)
features_implemented: [F001, F017, F002, F005, F007, F006, F008, F021, F018, F019, F020, F022, F023, F024, F025, F049, F026, F013, F015, F027, F028, F029, F030, F031, F032, F033, F034, F035, F036, F037]
last_updated: 2026-01-04
updated_from: [CC015, CC017, CC020, CC023, CC024, CC025, CC035, CC085, CC086, CC098, CC116, CC117, CC005, CC121]
---

# CodeCity

## Overview

CodeCity (Wettel & Lanza) visualizes object-oriented software as a navigable city: packages become districts and classes become buildings. CC023 introduces the core mapping and interaction model; CC035 expands it into a full end-to-end approach including fine-grained method representation (bricks), evolution techniques (age map, time travel, timeline), design-quality overlays (disharmony maps), and tool support (view configurations, scripting).

CC085 motivates CodeCity in terms of **habitability** and **locality**, arguing that a constrained 3D “place” with strong orientation points can support incremental program comprehension. It introduces a small set of building archetypes and discusses tradeoffs among linear, boxplot-based, and threshold-based mappings for producing “habitable” cities, and it describes interactive operations including marking via color/transparency, spawning district-only views, query-based selection (e.g., subclass hierarchies), and eliding.

CC023 also describes CodeCity as written in Smalltalk on top of the Moose reengineering framework, making the tool language-independent for the analyzed systems.

CC020 (the ICSE 2008 tool demo) highlights CodeCity’s “city overview” as a starting point for spotting large-scale structural patterns (e.g., very large buildings as potential god classes).

CC098 (a short 2008 technical report) provides a compact end-to-end description of CodeCity’s UI (city + information pane), navigation, queries, view configurations, and scripting. It also reports applying CodeCity to 9 systems totaling >900 kLOC across Java/C++/Smalltalk (Table 1) and provides a public download link.

## Implementation (from CC020 / CC024)

- **Implementation language**: Smalltalk.
- **Reverse-engineering foundation**: Moose framework with the language-independent **FAMIX** meta-model.
- **Model extraction**: for Java and C++ systems, iPlasma is used to parse code and export a model (MSE exchange format) that Moose can read; for Smalltalk systems Moose builds the model directly.
- **Rendering**: uses Jun for OpenGL rendering.
- **Complementary 2D views**: CC024 notes using Mondrian “class blueprints” as a complementary 2D view within the tool chain.
 - **Runtime environment**: VisualWorks Smalltalk on top of Moose; cross-platform (major OS support). (CC017)
 - **UI structure**: visualization window combines the 3D city with an information panel showing details for the currently focused element. (CC086)
 - **Selection status**: CC098 adds a “selection status bar” and frames selection actions as supporting local visual changes (color/transparency) and spawning additional views.

## Distribution and Licensing (from CC121, CC005)

CC121 (the official CodeCity download page) describes CodeCity as a self-contained, ready-to-run application for Windows and Mac OS X, plus an “image-only” distribution for other operating systems that requires VisualWorks Smalltalk (7.6) to run. It also notes that running CodeCity under X11 on Mac OS X can speed up OpenGL rendering.

CC005 further notes that CodeCity is developed under an academic non-commercial license (use limited to non-commercial contexts).

CC024 also presents a module-level architecture:
- **Model** (Moose/FAMIX + CodeCity extensions)
- **Core** (glyphs, layouts, visual mappings, transformations/color schemes)
- **View management** (view configurations + view builders)
- **Rendering** (Display layer on top of Jun/OpenGL)

## Key Mappings (from CC023)

- **Buildings**: classes (and interfaces)
- **Districts**: packages (recursively nested)
- **Height**: number of methods (NOM)
- **Footprint**: number of attributes (NOA)
- **Metric mapping strategy**: linear vs discretized categories (boxplot-based or threshold-based)
- **Topology**: nested packages as stacked platforms (altitude reflects nesting)

CC035 documents a common “magnitude” overview mapping:
- **Height**: NOM
- **Width/Length**: NOA
- **Building color**: LOC (dark gray → intense blue)
- **District color**: package nesting level (NL; darker → lighter with depth)

- **Language**: SmallTalk, Java, C++
- **VR**: n/a
- **Building**: class
- **Source code**: yes (view source code for visualized classes; CC035)
- **Static**: #attributes, #methods, package structure
- **Dynamic**: n/a
- **Instrumentation**: n/a

## CC015 Table 1 (survey summary)

| Feature | Notes |
|---------|-------|
| [[city-metaphor]] | City metaphor framing for large systems |
| [[class-as-building]] | One building per class |
| [[height-mapping]] | Height encodes number of methods |
| [[base-mapping]] | Footprint encodes number of member variables |
| [[treemap-layout]] | Treemap layout; terrain elevation indicates package nesting |
| [[evolution-visualization]] | Used for studying evolution over time (per CC015) |

## Evidence / Notes

CC023 demonstrates CodeCity on large systems and reports scalability to industrial-size software: ArgoUML (over 2,500 classes), Azureus (over 4,500 classes), and VisualWorks (over 8,000 classes). It also notes that very large systems can stress interactivity/navigability and mentions level-of-detail techniques as a potential optimization.

CC025 provides the controlled experiment details: CodeCity is compared to an Eclipse+Excel baseline (same source code plus tabular metrics/design-problem data) on FindBugs (medium) and Azureus (large) using a between-subjects randomized block design. After outlier removal, 41 subjects remain; the paper reports significant main effects of tool on correctness (F(1,37)=14.722, p=.001) and completion time (F(1,37)=4.392, p=.043), and reports +24.26% correctness (5.968 vs 4.803 points) and −12.01% completion time (36.117 vs 41.048 minutes). The paper also documents a ceiling effect for task A4.2 (CodeCity subjects largely unable to solve it) and excludes it from parts of the analysis.

CC035 reports additional performance/scalability observations (e.g., visualization build times across multiple large systems) and expands the experiment discussion in the thesis context.

CC116 focuses specifically on evolution analysis in CodeCity, introducing age maps, time travel, and timelines on large systems and reporting case-study findings that were confirmed by developers.

CC024 reports build+render time measurements (class-level granularity) across multiple systems (e.g., Azureus: 274 kLOC, 4,737 classes, 260s build time on a 2.4GHz Core2Duo MacBook Pro) and notes that rendering/navigation remains fluid for thousands of simple cuboid glyphs, while finer granularity and relationship rendering increase build cost. It also notes the presence of 270+ unit tests covering the core (glyphs/layouts/mappers/transformations) and configuration management.

CC098 reports applying CodeCity to 9 systems totaling over 900 kLOC across Java/C++/Smalltalk, and provides package/class counts for each (including ArgoUML, Azureus, JDK 1.5 core, and ScummVM), reinforcing CodeCity’s intended use for large-scale reverse engineering.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — foundational description of the approach + tool details
- [CC085] Wettel & Lanza (ICPC 2007) — habitability/locality framing, building archetypes, and mapper tradeoffs
- [CC025] Wettel & Lanza (ICSE 2011) — controlled experiment design + results for CodeCity vs. Eclipse+Excel baseline
- [CC035] Wettel PhD thesis — full approach (evolution + design quality), tool architecture/configuration, and controlled experiment
- [CC015] Jeffery survey — later overview and comparison table entry
- [CC017] Wettel CodeCity homepage — project overview + platform stack (VisualWorks Smalltalk, Moose, OpenGL)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — city overview + implementation details (Moose/FAMIX, iPlasma, Jun/OpenGL)
- [CC024] Wettel & Lanza (WASDeTT 2008) — architecture (modules), view-configuration/mappers, and scalability/performance notes
- [CC086] Wettel & Lanza (2008) — CodeCity overview (queries, tunable views, architecture, and performance data)
- [CC098] Wettel & Lanza (2008 tech report) — compact tool overview (UI, queries, view configurations, scripting) and multi-system application table
- [CC116] Wettel & Lanza (WCRE 2008) — evolution-focused CodeCity visualizations (age map, time travel, timeline) with case studies
- [CC117] Wettel & Lanza (SoftVis 2008) — disharmony maps for visual localization of design problems in the city
- [CC005] Power of Data Visualization blog — secondary overview mentioning distribution packaging and non-commercial academic licensing
- [CC121] CodeCity download page — official platform packaging notes (Windows/Mac app + image-only for other OS; X11 mention)
