# Taxonomy

> Classification dimensions for software city features and implementations.

---

## Dimensions

### granularity

**Description**: What software element becomes a primary visual unit (building/district/brick/etc.).

| Value | Definition | Examples |
|-------|------------|----------|
| package | Package/namespace rendered as a district or grouped area | CodeCity (districts) |
| class | Object-oriented class | CodeCity, SynchroVis, CityVR |
| method | Object-oriented method (within a class) | CodeCity (fine-grained bricks), Progressive Bricks |
| function | Individual function or method | Software World, Vizz3D, High-Rise, JSCity |
| component | Higher-level component (architectural/subsystem unit) | Component City |
| module | Module (e.g., JavaScript AMD/Angular module declarations) | JSCity (module buildings) |
| file | Source file | CodeCharta, SoftVis3D |
| system | Whole software system (or multi-application landscape) | ExplorViz (landscape-level views) |
| database | Database/schema entity represented alongside the city | m3triCity 2 (database cloud/underground) |
| table | Database table entity inferred from code usage | m3triCity 2 (table cylinders) |

**Sources**: CC015 (Table 1, "Building" column); CC035 (fine-grained method-level views); CC036 (function-level JavaScript city); CC094 (module declarations rendered as buildings in JSCity); CC014 (file/folder mapping on CodeCharta website); CC038 (file/folder mapping on SoftVis3D website); CC053 (landscape-level/system granularity); CC079 (database/table entities in m3triCity 2)

---

### visual_element

**Description**: What the primary software entity is rendered as.

| Value | Definition |
|-------|------------|
| building | 3D cuboid or cylinder representing code entity |
| district | Grouped area containing buildings |
| brick | Small cuboid representing a method (fine-grained view) |
| floor | Storey-level slice inside a building representing a method/instance as a stacked unit |
| street | Linear element organizing districts (EvoStreets) |
| platform | Elevated surface grouping related elements (Vizz3D) |
| edge | Rendered relation/dependency between entities |
| island | Landmass representing a module/bundle in an island metaphor |
| clothing | Garment silhouette representing a class in a wardrobe metaphor |

**Sources**: CC015; CC035 (method bricks; dependency edges); CC106 (methods as floors in VR City); CC070 (island metaphor); CC041 (clothing metaphor)

---

### metric_category

**Description**: What aspect of code is measured and visualized.

| Value | Definition | Example Metrics |
|-------|------------|-----------------|
| size | Volume/quantity of code | LOC, NOM, NOA, NOV |
| complexity | Structural complexity | cyclomatic complexity |
| coupling | Dependencies between entities | call graphs, inheritance |
| cohesion | Internal relatedness of an entity’s responsibilities | LCOM5 |
| evolution | Change over time | churn, author, modification date |
| behavior | Runtime execution properties | timing, thread operations |
| variability | Variability-related implementation density | overload counts, variability metrics (e.g., via symfinder) |
| quality | Design-quality signals and anomalies | design disharmonies, smells |

**Sources**: CC015 (Table 1, "Static" and "Dynamic" columns); CC035 (design quality assessment); CC075 (cohesion metrics); CC045 (variability metrics + technical-debt-focused overlays)

---

### metric_mapping_strategy

**Description**: How numeric values are transformed before being applied to visual properties.

| Value | Definition | Examples |
|-------|------------|----------|
| linear | Continuous mapping proportional to value | Baseline mapping described in CC023 |
| linear_scaled | Linear mapping with a global scaling cap (scale down if some values exceed a max) | SoftVis3D (CC040) |
| logarithmic | Continuous mapping using a logarithmic transform to compress outliers | SoftVis3D (CC040) |
| exponential | Continuous mapping using an exponential transform to reshape the distribution | SoftVis3D (CC040) |
| boxplot_binned | Discrete categories with boundaries derived from value distribution | CodeCity (CC023) |
| threshold_binned | Discrete categories with absolute empirical thresholds | CodeCity (CC023) |

**Sources**: CC023 (metric mapping discussion); CC040 (scaling method options in SoftVis3D)

---

### layout_algorithm

**Description**: Spatial arrangement strategy for placing buildings and groups.

| Value | Definition | Examples |
|-------|------------|----------|
| treemap | Space-filling hierarchy partition | CodeCity |
| rectangle_packing | Packing fixed-size rectangles with minimal wasted space | CodeCity (CC035 Algorithm 3.1) |
| progressive_bricks | Adaptive wall-based brick layout to avoid extreme height | CodeCity (CC035) |
| force_directed | Force-directed graph layout for positioning elements | SoftViz3D (GraphViz neato) |
| layered_graph | Hierarchical/layered graph layout for dependencies | SoftViz3D (GraphViz dot) |
| levelized | Row-based layout grouping entities by architectural level (e.g., LSM levels) | Holoware/DynaCity |
| street | Streets as organizing elements (directories/packages) | EvoStreets, SoftVis3D |
| coupling | Placement/contact encodes coupling strength | VR City |
| sunburst | Radial space-filling layout for hierarchical data | Langelier framework (CC075) |
| spiral | Center-out spiral placement within each hierarchy level | BabiaXR-CodeCity |

**Sources**: CC015 (tool descriptions + Table 1); CC035 (layout algorithms); CC038 (Evostreet layout description); CC043 (GraphViz dot/neato layouts); CC096 (spiral layout); CC137 (levelized/LSM-based city layout)

---

### platform

**Description**: Rendering and interaction environment.

| Value | Definition | Examples |
|-------|------------|----------|
| desktop | Traditional screen-based | CodeCity (original) |
| web | Browser-based | LD-City (Three.js), JSCity, SoftVis3D, SoftViz3D (X3DOM) |
| game_engine | 3D game engine or game world used as the visualization environment | CodeMetropolis (Minecraft), Trend Maps (UE4), Code2City (UE4) |
| vr_hmd | VR head-mounted display | CityVR (Vive), ExplorViz (Rift), Code2CityVR (Rift) |
| cave | Room-sized projection-based VR environment | Imsovision (CAVE) |
| ar | Augmented reality | SkyscrapAR, HoloLens |
| vrml | VRML browser plugin | Component City |

**Sources**: CC015 (Table 1, "VR" column); CC036 (browser-based Three.js city); CC038 (WebGL-based SoftVis3D); CC102 (Minecraft game engine); CC054 (UE4 prototype); CC055 (UE4-based Code2City / Code2CityVR); CC057 (CAVE-based immersive VR)

---

### analysis_mode

**Description**: Static vs dynamic vs temporal vs collaborative analysis.

| Value | Definition | Examples |
|-------|------------|----------|
| static | Snapshot of code structure | Most implementations |
| dynamic | Runtime execution traces | SynchroVis, VR City, High-Rise |
| evolution | Change over time | EvoStreets, SkyscrapAR, SoftVis3D |
| collaborative | Multi-user/shared analysis sessions | ExplorViz (multi-user VR) |

**Sources**: CC015, CC053, CC038

---

### instrumentation

**Description**: Source of dynamic execution data.

| Value | Definition | Examples |
|-------|------------|----------|
| none | No dynamic instrumentation | Most static-only tools |
| gprof | GCC profiler output | Vizz3D |
| kieker | Kieker monitoring traces | SynchroVis, ExplorViz |
| opentelemetry | OpenTelemetry tracing/telemetry data | ExplorViz |
| intrace | inTrace execution traces | VR City |
| asm_injection | ASM bytecode injection | High-Rise |
| jvmti | JVM Tool Interface | (mentioned as opportunity) |

**Sources**: CC015 (Table 1, "Instr" column); CC077 (ExplorViz about page)

---

## Last Updated

- **Date**: 2026-01-05
- **Sources processed**: CC009, CC014, CC015, CC017, CC018, CC020, CC023, CC024, CC025, CC035, CC036, CC038, CC040, CC041, CC043, CC053, CC059, CC075, CC079, CC080, CC085, CC086, CC091, CC092, CC093, CC094, CC096, CC102, CC103, CC104, CC106, CC069, CC071, CC077, CC098, CC108, CC116, CC117, CC128, CC129, CC130, CC131, CC133, CC134, CC137, CC140, CC002, CC005, CC006, CC021, CC026, CC030, CC034, CC045, CC054, CC055, CC057, CC064, CC066, CC070, CC074, CC076, CC078, CC083, CC084, CC100, CC101, CC107, CC114, CC120, CC121, CC126, CC136, CC143, CC147, CC148
