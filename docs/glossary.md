# Glossary

> Domain vocabulary for CodeCity and software city visualization.

---

## Metaphor

### city metaphor

**Definition**: A visualization approach that depicts a software system as a city, where code structures become city elements (buildings, districts, streets) to leverage human spatial cognition for understanding complex systems.

**Aliases**: code city, software city, city visualization

**Category**: metaphor

**Bounded Context**: city-metaphor

**Sources**: CC015, CC023, CC025, CC035

**Related**: [building](#building), [district](#district)

**Example**: Classes rendered as 3D buildings on a ground plane, grouped into districts by package.

---

### island metaphor

**Definition**: A visualization approach that depicts a modular software system as an archipelago, where modules/bundles become islands and internal structure is shown on each island (e.g., packages as regions and classes as buildings).

**Aliases**: archipelago metaphor, island visualization

**Category**: metaphor

**Bounded Context**: island-metaphor

**Sources**: CC070

**Related**: [city metaphor](#city-metaphor), [district](#district), [[island-metaphor]]

---

### clothing metaphor

**Definition**: A visualization approach that depicts software classes as garments in a wardrobe, encoding class-level metrics in garment attributes to support program comprehension.

**Aliases**: wardrobe metaphor, clothing visualization

**Category**: metaphor

**Bounded Context**: clothing-metaphor

**Sources**: CC041

**Related**: [city metaphor](#city-metaphor), [[clothing-metaphor]]

**Example**: Each class is shown as a shirt or pants whose size, color, collar, and stripes reflect quality metrics.

---

### galaxy metaphor

**Definition**: A visualization approach that depicts software as a galaxy/constellation where files are rendered as stars and semantic clusters appear as nebulae, with spatial layout determined by semantic similarity (via NLP/LDA) rather than structural hierarchy.

**Aliases**: software galaxy, constellation metaphor

**Category**: metaphor

**Bounded Context**: galaxy-metaphor

**Sources**: CC157

**Related**: [city metaphor](#city-metaphor), [semantic layout](#semantic-layout), [[galaxy-metaphor]]

**Example**: Files with similar topics (from LDA analysis) cluster together as a nebula, regardless of their package structure.

---

### building

**Definition**: A 3D visual element representing a software entity (class, method, function, or component), with dimensions encoding metrics such as lines of code or number of methods.

**Aliases**: block, tower

**Category**: metaphor

**Bounded Context**: city-metaphor

**Sources**: CC015, CC023, CC035

**Related**: [city metaphor](#city-metaphor), [[height-mapping]]

---

### district

**Definition**: A visual grouping in a software city corresponding to a package, directory, or namespace, providing spatial organization for related buildings.

**Aliases**: block, neighborhood, platform, quarter

**Category**: metaphor

**Bounded Context**: city-metaphor

**Sources**: CC015, CC023, CC035, CC134

---

### brick

**Definition**: A small cuboid used in fine-grained software cities to represent a method (often placed on or within the building representing the method’s class).

**Aliases**: method brick

**Category**: metaphor

**Bounded Context**: city-metaphor

**Sources**: CC035

**Related**: [building](#building), [[method-as-bricks]]

---

### locality

**Definition**: A sense of stable spatial placement and orientation that helps users avoid disorientation when navigating a 3D visualization.

**Aliases**: sense of place, orientation

**Category**: metaphor

**Bounded Context**: universal

**Sources**: CC023, CC035, CC085

**Related**: [city metaphor](#city-metaphor), [building](#building)

---

### habitability

**Definition**: The property of a visualization environment that supports sustained “living in” the representation during analysis, emphasizing locality/orientation so users can build familiarity (a feeling of being “at home”) rather than become disoriented.

**Aliases**: habitable visualization

**Category**: metaphor

**Bounded Context**: universal

**Sources**: CC035, CC085

**Related**: [locality](#locality), [city metaphor](#city-metaphor)

---

## Metrics

### churn

**Definition**: The number of lines of changes to a class over time, used as a metric that may indicate probability of containing software bugs.

**Aliases**: code churn, change frequency

**Category**: metric

**Bounded Context**: universal

**Sources**: CC015

**Related**: [[evolution-visualization]]

**Example**: SkyscrapAR uses building height to represent churn.

---

### bus factor

**Definition**: A risk-oriented metric estimating how many distinct contributors would need to become unavailable before development or maintenance is seriously impacted; low values imply concentrated knowledge/ownership.

**Aliases**: truck factor

**Category**: metric

**Bounded Context**: universal

**Sources**: CC038

**Related**: [[evolution-visualization]], [[color-mapping]]

**Example**: SoftVis3D frames “number of authors” (from SCM blame) as a bus-factor signal for files.

---

### code ownership

**Definition**: A metric describing which developers “own” which parts of a codebase, often derived from version-control blame data by attributing lines or hunks to last-modifying authors.

**Aliases**: ownership, authorship distribution

**Category**: metric

**Bounded Context**: universal

**Sources**: CC136

**Related**: [SCM blame](#scm-blame), [bus factor](#bus-factor), [[evolution-visualization]]

**Example**: CoderCity segments each file-building by git-blame hunks and colors segments by author to show ownership within a file.

---

### LOC

**Definition**: Lines of Code — a size metric counting the number of source code lines in a file, class, or method.

**Aliases**: lines of code, SLOC

**Category**: metric

**Bounded Context**: universal

**Sources**: CC015, CC035, CC093, CC104

**Related**: [[height-mapping]], [[base-mapping]], [[texture-mapping]]

---

### LLOC

**Definition**: Logical Lines of Code — a size metric counting logical statements rather than physical lines (used for method size in CodeMetropolis).

**Aliases**: logical lines of code

**Category**: metric

**Bounded Context**: universal

**Sources**: CC102

**Related**: [[height-mapping]]

---

### McCC

**Definition**: McCabe's cyclomatic complexity — a complexity metric measuring the number of linearly independent paths through a program unit.

**Aliases**: cyclomatic complexity, McCabe complexity

**Category**: metric

**Bounded Context**: universal

**Sources**: CC102

**Related**: [[base-mapping]]

---

### NOM

**Definition**: Number of Methods — a size metric counting methods/functions in a class.

**Aliases**: number of methods, method count

**Category**: metric

**Bounded Context**: universal

**Sources**: CC015, CC023, CC035, CC093, CC104

**Related**: [[height-mapping]]

---

### NOA

**Definition**: Number of Attributes — a size metric counting member variables/fields in a class.

**Aliases**: number of attributes, attribute count, number of member variables

**Category**: metric

**Bounded Context**: universal

**Sources**: CC015, CC023, CC035

---

### NII

**Definition**: Number of Incoming Invocations — a coupling metric counting how many incoming calls/invocations a method receives.

**Aliases**: number of incoming invocations

**Category**: metric

**Bounded Context**: universal

**Sources**: CC102, CC130

**Related**: [[base-mapping]]

---

### NOI

**Definition**: Number of Outgoing Invocations — a coupling metric counting how many calls/invocations a method issues to other methods.

**Aliases**: number of outgoing invocations

**Category**: metric

**Bounded Context**: universal

**Sources**: CC102, CC130

**Related**: [[base-mapping]]

---

### NUMPAR

**Definition**: Number of Parameters — a size metric counting the parameters of a method/function.

**Aliases**: number of parameters

**Category**: metric

**Bounded Context**: universal

**Sources**: CC102, CC130

---

### NOS

**Definition**: Number of Statements - a size metric counting statements in a method or function (used to map wall material in CodeMetropolis).

**Aliases**: number of statements, statement count

**Category**: metric

**Bounded Context**: universal

**Sources**: CC102, CC103

**Related**: [[texture-mapping]]

---

### SAST

**Definition**: Static Application Security Testing - analysis of source/bytecode to detect security vulnerabilities without executing the program.

**Aliases**: static application security testing, static security analysis

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC069

**Related**: [[vulnerability-overlay]]

---

### coupling

**Definition**: The degree of interdependence between software entities; high coupling indicates many dependencies and is often treated as a quality risk.

**Aliases**: coupling between classes

**Category**: metric

**Bounded Context**: universal

**Sources**: CC075

**Related**: [[color-mapping]]

---

### logical coupling

**Definition**: Coupling inferred from version-control history: two files are logically coupled if they are frequently modified together in the same commits.

**Aliases**: co-change coupling, change coupling

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC148

**Related**: [churn](#churn), [coupling](#coupling), [[evolution-visualization]]

**Example**: Viseagull (CC148) clusters files into “cities” using a Jaccard-distance matrix derived from file×commit co-change data.

---

### semantic coupling

**Definition**: Coupling inferred from lexical similarity: two files are semantically coupled if they share a similar vocabulary/lexicon (e.g., as measured by tf-idf vectors and cosine similarity).

**Aliases**: lexical coupling

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC148

**Related**: [coupling](#coupling), [static analysis](#static-analysis)

**Example**: Viseagull (CC148) groups files into clusters based on cosine-distance similarity of tf-idf vectors (described as supported for Python files).

---

### cohesion

**Definition**: The degree to which the responsibilities of a class/module are internally related; higher cohesion is generally preferred.

**Aliases**: class cohesion

**Category**: metric

**Bounded Context**: universal

**Sources**: CC075

**Related**: [[orientation-mapping]]

---

### CBO

**Definition**: Coupling Between Objects — a coupling metric counting how many other classes a class is coupled to.

**Aliases**: Coupling Between Objects

**Category**: metric

**Bounded Context**: universal

**Sources**: CC075

**Related**: [[color-mapping]], [coupling](#coupling)

---

### LCOM5

**Definition**: Lack of Cohesion in Methods (variant 5) — a cohesion metric where higher values indicate lower cohesion within a class.

**Aliases**: Lack of Cohesion in Methods

**Category**: metric

**Bounded Context**: universal

**Sources**: CC075

**Related**: [[orientation-mapping]], [cohesion](#cohesion)

---

### WMC

**Definition**: Weighted Methods per Class — a size/complexity metric counting (or weighting) methods in a class.

**Aliases**: Weighted Methods per Class

**Category**: metric

**Bounded Context**: universal

**Sources**: CC075

**Related**: [[height-mapping]]

---

### DIT

**Definition**: Depth in Inheritance Tree — an inheritance metric indicating how deep a class is in the inheritance hierarchy.

**Aliases**: Depth in Inheritance Tree

**Category**: metric

**Bounded Context**: universal

**Sources**: CC075

---

### NOC

**Definition**: Number of Child Classes — an inheritance metric counting the immediate subclasses of a class.

**Aliases**: number of child classes

**Category**: metric

**Bounded Context**: universal

**Sources**: CC041

**Related**: [DIT](#dit)

---

### RFC

**Definition**: Response for Class — a metric counting the number of methods that can be executed in response to a message received by an object (including methods invoked by the class).

**Aliases**: Response for Class

**Category**: metric

**Bounded Context**: universal

**Sources**: CC041

**Related**: [CBO](#cbo)

---

### NOV

**Definition**: Number of Variables — a size metric counting declared variables in a function (used in some function-level cities as a proxy for local state/complexity).

**Aliases**: number of variables, variable count

**Category**: metric

**Bounded Context**: universal

**Sources**: CC036, CC093, CC104

**Related**: [[base-mapping]], [[function-as-building]]

---

### NL

**Definition**: Nesting Level — a metric for packages indicating depth within the package hierarchy (e.g., how deeply a package is nested).

**Aliases**: nesting level, depth in hierarchy, DIH

**Category**: metric

**Bounded Context**: universal

**Sources**: CC024, CC035, CC086

**Related**: [district](#district), [[package-as-district]]

---

### god class

**Definition**: A class that accumulates disproportionate responsibility and becomes abnormally large; often treated as a design smell.

**Aliases**: god object

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC023, CC035

---

### data class

**Definition**: A class dominated by fields with few or no methods; often treated as a design smell.

**Aliases**: data-only class

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC023, CC035

**Related**: [[base-mapping]]

---

### brain class

**Definition**: A class-level design disharmony characterized by high complexity and “brain” logic concentrated in a single class (often treated as a code smell).

**Aliases**: brain class smell

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035

**Related**: [god class](#god-class), [design disharmony](#design-disharmony)

---

### Blob

**Definition**: A large, complex class that accumulates much of a system’s behavior and interacts with many small classes (an anti-pattern).

**Aliases**: Blob class

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC075

**Related**: [god class](#god-class)

## Mapping

### concept mapping

**Definition**: The step in defining a city metaphor where software entities (e.g., classes, packages) are mapped to city concepts (e.g., buildings, districts).

**Aliases**: entity-to-glyph mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC035

**Related**: [property mapping](#property-mapping), [city metaphor](#city-metaphor)

---

### property mapping

**Definition**: Mapping from software properties/metrics to visual properties (e.g., building height, footprint, color, transparency) to encode information in the city.

**Aliases**: metric mapping, visual encoding

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC035

**Related**: [concept mapping](#concept-mapping), [[height-mapping]], [[color-mapping]]

---

### magnitude mapping

**Definition**: A CodeCity mapping preset aimed at overviews, mapping NOM→height, NOA→width/length, LOC→building color, and NL→district color.

**Aliases**: magnitude property mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC035

**Related**: [NOM](#nom), [NOA](#noa), [LOC](#loc), [NL](#nl)

---

### polymetric view

**Definition**: A lightweight reverse-engineering visualization where multiple software metrics are mapped onto visual properties of glyphs; CodeCity extends this idea into 3D by mapping metrics onto building width/length/height.

**Aliases**: polymetric views

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC020

**Related**: [property mapping](#property-mapping), [magnitude mapping](#magnitude-mapping)

---

### height mapping

**Definition**: A property mapping where building height encodes a metric value.

**Aliases**: vertical mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC015, CC023, CC035

**Related**: [[height-mapping]]

---

### base mapping

**Definition**: A property mapping where building footprint (length/width/area) encodes a metric value.

**Aliases**: footprint mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC015, CC023, CC035

**Related**: [[base-mapping]]

---

### color mapping

**Definition**: A property mapping where color (including brightness/translucence) encodes an attribute such as visibility, size, authorship, complexity, or dependencies.

**Aliases**: color coding

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC015, CC023, CC035

**Related**: [[color-mapping]]

---

### texture mapping

**Definition**: A property mapping where surface texture encodes an attribute (e.g., LOC via wall texture).

**Aliases**: texture encoding

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC015

---

### discretized metric mapping

**Definition**: A mapping approach that limits a visual property to a small number of discrete categories (e.g., five size levels) to keep overviews readable in the presence of outliers.

**Aliases**: binned mapping, categorical scaling

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC023

**Related**: [[discretized-metric-mapping]]

---

### boxplot-based mapping

**Definition**: A discretized mapping strategy where category boundaries are derived from the distribution of values in the analyzed system (via a boxplot technique).

**Aliases**: boxplot binned mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC023, CC035

**Related**: [[boxplot-metric-mapping]]

---

### threshold-based mapping

**Definition**: A discretized mapping strategy where category boundaries are fixed absolute thresholds (often empirically derived) so cities can be compared across systems.

**Aliases**: threshold binned mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC023, CC035

**Related**: [[threshold-metric-mapping]]

---

### linear mapping

**Definition**: A continuous mapping strategy where a visual property changes proportionally with the metric value.

**Aliases**: proportional mapping

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC023, CC035

**Related**: [[texture-mapping]]

---

### identity mapping

**Definition**: A mapping strategy where the visual value is computed directly from the metric value (f(x)=x), typically with unit/scale conversion for rendering.

**Aliases**: identity mapper

**Category**: mapping

**Bounded Context**: universal

**Sources**: CC035

**Related**: [linear mapping](#linear-mapping)

## Analysis

### static analysis

**Definition**: Analysis of source code structure without executing the program, extracting properties like LOC, complexity, inheritance, and dependencies.

**Aliases**: static information

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

**Related**: [dynamic analysis](#dynamic-analysis)

---

### dynamic analysis

**Definition**: Analysis of program behavior during execution, capturing runtime properties like call traces, thread operations, timing, and memory allocation.

**Aliases**: dynamic information, runtime analysis, execution analysis

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

**Related**: [static analysis](#static-analysis)

---

### Layered Structure Model (LSM)

**Definition**: A model of a system’s dependency graph that assigns entities to ordered levels (“layers”) to describe a layered architecture; ideally most dependencies point from higher levels to lower levels, with cycles treated as special cases.

**Aliases**: LSM, layered structure model

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC137

**Related**: [[levelized-layout]], [[contextual-dependency-view]]

**Example**: Holoware/DynaCity (CC137) builds an LSM from a `.dot` dependency graph and uses LSM levels to arrange packages/classes into rows.

---

### reflexion model

**Definition**: A lightweight, executable architecture model that compares an intended (high-level) module structure and allowed dependencies to dependencies derived from source code, highlighting mismatches between the planned and implemented architecture.

**Aliases**: reflexion modeling, software reflexion model, RM

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC114

**Related**: [module](#module), [coupling](#coupling), [static analysis](#static-analysis), [architectural erosion](#architectural-erosion)

**Example**: CC114 maps code to architecture modules using regular expressions, derives module dependencies from class dependencies, and marks prohibited dependencies as violations.

---

### architectural erosion

**Definition**: Degradation of a system’s intended architecture as the implementation diverges over time, often observed as unexpected or prohibited dependencies between modules.

**Aliases**: architectural degradation

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC114

**Related**: [reflexion model](#reflexion-model), [technical debt](#technical-debt), [coupling](#coupling)

**Example**: In CC114, architectural erosion is surfaced as red inter-module arrows representing dependencies not permitted by the architecture plan.

---

### module

**Definition**: A cohesive unit of code that groups related functionality and exposes an interface; the exact construct varies by language and ecosystem (e.g., JavaScript AMD `define(...)` modules or framework module declarations).

**Aliases**: code module

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015, CC094

**Related**: [district](#district), [[module-as-building]]

**Example**: In JSCity (CC094), an AMD `define('name', ...)` declaration can be rendered as a “Module” building.

---

### code hotspot

**Definition**: A file or module flagged as high-risk or high-priority because one or more metrics (e.g., complexity, churn, or issue counts) indicate elevated maintenance cost or defect likelihood; often emphasized visually (e.g., tall/red buildings).

**Aliases**: hotspot, code hotspot

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC014, CC040

**Related**: [churn](#churn), [[color-mapping]]

**Example**: CodeCharta highlights “hot” files as large or red buildings when complexity or change frequency is high.

---

### software variability

**Definition**: The ability of a software artifact (system or element) to be efficiently extended, changed, customized, or configured toward a specific context.

**Aliases**: variability, configurability

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC045

**Related**: [technical debt](#technical-debt), [[variability-hotspot-overlay]]

**Example**: VariCity focuses on variability implemented via OO mechanisms (e.g., inheritance/overloading) in a single codebase.

---

### technical debt

**Definition**: Short-term applications of design and implementation constructs that make future modifications more costly or impossible, impacting maintainability and evolution.

**Aliases**: design debt

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC045

**Related**: [code hotspot](#code-hotspot), [[disharmony-maps]], [[variability-hotspot-overlay]]

**Example**: VariMetrics overlays quality metrics to highlight variability hotspots that are also debt-critical.

---

### variability debt

**Definition**: A form of technical debt applied to variability mechanisms, characterized by missing knowledge/traceability about implemented variability in the source code and its negative impacts on maintenance.

**Aliases**: variability technical debt

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC045

**Related**: [technical debt](#technical-debt), [software variability](#software-variability), [[variability-hotspot-overlay]]

---

### variation point

**Definition**: A code location/entity where variation is realized; in CC045 a variation point can be a class with at least two subclasses, a class with overloaded methods/constructors, or a detected design pattern instance.

**Aliases**: VP, vp, variation point (vp)

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC045

**Related**: [variant](#variant), [software variability](#software-variability)

---

### variant

**Definition**: A concrete alternative for a variation point; in CC045 variants are represented by subclasses (class-level variants) or overloads (method-level variants).

**Aliases**: variability variant

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC045

**Related**: [variation point](#variation-point)

---

### leak period

**Definition**: In SonarQube-style quality tracking, a configured “new code” window used to scope differential metrics such as new lines of code and new issues for a recent period.

**Aliases**: new code period

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC038, CC040

**Related**: [[evolution-visualization]], [code hotspot](#code-hotspot)

**Example**: SoftVis3D provides a “Leak period” profile that focuses height and color metrics on new-code properties.

---

### remodularization analysis

**Definition**: An analysis task that evaluates or proposes changes to a system’s modular decomposition (e.g., packages/modules) to improve cohesion and reduce coupling, often informed by dependency and semantic clustering signals.

**Aliases**: modularization analysis

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC106

**Related**: [module](#module), [[remodularization-analysis]]

---

### semantic cluster

**Definition**: A grouping of code entities based on semantic similarity (e.g., identifier/text similarity) rather than declared package structure, used as an alternative modular view for comparison with coupling.

**Aliases**: semantic clustering

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC106

**Related**: [remodularization analysis](#remodularization-analysis), [[remodularization-analysis]]

---

### program comprehension

**Definition**: The activity of understanding a software system to answer questions needed for tasks like maintenance, reverse engineering, and reengineering.

**Aliases**: software comprehension, code comprehension

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC025

**Related**: [city metaphor](#city-metaphor), [static analysis](#static-analysis)

---

### software production visualization

**Definition**: A visualization approach that emphasizes production- and maintenance-cost signals (e.g., work distribution, hot spots, frequent modifications) alongside code structure to support maintenance and management decisions.

**Aliases**: production visualization, production-cost visualization

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC006

**Related**: [program comprehension](#program-comprehension), [code hotspot](#code-hotspot)

**Example**: CC006 proposes overlaying “fire” for hot execution spots and flashes for high-cost (frequently modified) components on top of a software city.

---

### software map

**Definition**: A map-oriented visualization of a software system (often based on a 2D/2.5D treemap) that shows hierarchical structure and encodes software metrics using visual variables to support monitoring and decision-making.

**Aliases**: software maps, software cartography

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC054

**Related**: [[treemap-layout]], [city metaphor](#city-metaphor), [[color-mapping]]

**Example**: A 2.5D treemap where file rectangles are extruded to cuboids and colored by a metric.

---

### trend map

**Definition**: A software map augmented to visualize metric changes over a revision range by encoding per-entity or aggregated **trend values** (e.g., increasing/decreasing) in a single view.

**Aliases**: trend maps

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC054

**Related**: [software map](#software-map), [[evolution-visualization]]

---

### item-based metaphor

**Definition**: A metaphor design that modifies the visual appearance of individual map items (e.g., surface/material properties of a treemap cuboid) to communicate state or trends.

**Aliases**: item-based effect

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC054

**Related**: [context-based metaphor](#context-based-metaphor), [[texture-mapping]]

---

### context-based metaphor

**Definition**: A metaphor design that affects the surrounding space of a region or group of items (e.g., particle effects around a directory/package region) to communicate group-level state or trends.

**Aliases**: context-based effect

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC054

**Related**: [item-based metaphor](#item-based-metaphor), [[production-cost-overlay]]

---

### software landscape

**Definition**: A set of software applications/services and their deployment context (e.g., servers) considered as a connected whole, often including the runtime communication between parts.

**Aliases**: application landscape, system landscape

**Category**: analysis

**Bounded Context**: landscape-metaphor

**Sources**: CC053, CC084

**Related**: [dynamic analysis](#dynamic-analysis), [program comprehension](#program-comprehension)

---

### software city landscape

**Definition**: A visualization that combines multiple software cities to represent component-level architecture, placing cities to convey structural relationships or dependencies between components.

**Aliases**: city landscape

**Category**: analysis

**Bounded Context**: landscape-metaphor

**Sources**: CC101

**Related**: [software landscape](#software-landscape), [[software-landscape-view]]

---

### live trace visualization

**Definition**: Visualization of runtime traces (events and interactions) as they are collected, to support near-real-time comprehension of a running system.

**Aliases**: live monitoring visualization

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC053, CC084

**Related**: [dynamic analysis](#dynamic-analysis), [software landscape](#software-landscape)

---

### controlled experiment

**Definition**: An empirical study that compares two or more treatments under controlled conditions and measures outcomes (e.g., correctness and completion time) to test hypotheses about effectiveness and efficiency.

**Aliases**: experimental study

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC025

**Related**: [program comprehension](#program-comprehension)

---

### PANAS

**Definition**: The Positive Affect and Negative Affect Schedule (PANAS) — a 20-item self-report questionnaire used to measure current positive and negative affect.

**Aliases**: Positive Affect and Negative Affect Schedule

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC009

**Related**: [positive affect score (PAS)](#positive-affect-score-pas), [negative affect score (NAS)](#negative-affect-score-nas), [controlled experiment](#controlled-experiment)

---

### positive affect score (PAS)

**Definition**: The PANAS-derived sum of the 10 positive-affect items (range 10–50); higher values indicate higher positive affect.

**Aliases**: PAS, positive affect score

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC009

**Related**: [PANAS](#panas), [negative affect score (NAS)](#negative-affect-score-nas)

---

### negative affect score (NAS)

**Definition**: The PANAS-derived sum of the 10 negative-affect items (range 10–50); lower values indicate lower negative affect.

**Aliases**: NAS, negative affect score

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC009

**Related**: [PANAS](#panas), [positive affect score (PAS)](#positive-affect-score-pas)

---

### systematic mapping study

**Definition**: A structured secondary-study method that surveys a research area and classifies the literature into categories to characterize trends, gaps, and the distribution of approaches (often broader than a systematic literature review).

**Aliases**: mapping study, systematic mapping

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC018

**Related**: [city metaphor](#city-metaphor)

---

### design harmony

**Definition**: A perspective on software design quality where well-structured code follows design guidelines, contrasted with design disharmonies that violate them.

**Aliases**: design harmony concept

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035

**Related**: [design disharmony](#design-disharmony)

---

### design disharmony

**Definition**: A formalized design shortcoming (a “smell”) identified as a violation of a design guideline, typically detected via metric-based detection strategies.

**Aliases**: design anomaly, design flaw

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035

**Related**: [detection strategy](#detection-strategy), [[disharmony-maps]]

---

### detection strategy

**Definition**: A metric-based logical rule used to detect violations of design guidelines (often yielding a boolean “affected/unaffected” result for each entity).

**Aliases**: smell detector, anomaly detection rule

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035

**Related**: [design disharmony](#design-disharmony)

---

### disharmony map

**Definition**: A city visualization whose colors encode detected design disharmonies (affected entities in vivid colors; unaffected entities in gray) while keeping structural context.

**Aliases**: design disharmony map

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035, CC025

**Related**: [[disharmony-maps]], [design disharmony](#design-disharmony)

---

### age map

**Definition**: An evolution overlay that maps artifact age (survival across sampled versions) to a sequential color scheme.

**Aliases**: age overlay

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035

**Related**: [[age-map]], [[time-travel]]

---

### time travel

**Definition**: An evolution technique that steps through versions while maintaining stable spatial placement for entity histories so change is perceived as transformation over time.

**Aliases**: time traveling

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035, CC059

**Related**: [[time-travel]], [[timeline-visualization]]

---

### time shift mode

**Definition**: A runtime-analysis control that shifts a live monitoring visualization away from “now” to inspect earlier snapshots/time windows (e.g., pausing/rewinding a live trace stream).

**Aliases**: time-shift mode, time shift, time shifting

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC084, CC108, CC080

**Related**: [live trace visualization](#live-trace-visualization), [software landscape](#software-landscape), [time travel](#time-travel)

---

### time bucketing

**Definition**: A time-travel control that aggregates commits into coarser time units (e.g., day, week, month, year) so multiple commits are displayed at once.

**Aliases**: temporal aggregation

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC059

**Related**: [[time-travel]]

---

### timeline

**Definition**: An evolution view that places versions along an axis and renders per-version representations (e.g., method bricks or change markers) to support navigation and show when changes occur.

**Aliases**: timeline technique

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC035, CC059

**Related**: [[timeline-visualization]], [age map](#age-map)

---

### data file (city entity)

**Definition**: A non-source data artifact (e.g., XML/JSON/CSV) represented explicitly in the software city to expose data structure alongside code.

**Aliases**: data file entity

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC079

**Related**: [[data-file-visualization]], [[file-as-building]]

---

### table access

**Definition**: A relationship indicating that a class accesses a database table (e.g., via embedded SQL), used to connect code to data entities in the visualization.

**Aliases**: table access relation

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC079

**Related**: [[database-access-visualization]]

---

### SQLInspect

**Definition**: A static analyzer that inspects database usage in Java applications by extracting embedded SQL queries to infer database schemas and table accesses.

**Aliases**: SQLInspect analyzer

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC079

**Related**: [[database-access-visualization]]

---

## Layout

### treemap

**Definition**: A hierarchical, space-filling layout that partitions an area into nested rectangles used to place grouped entities.

**Aliases**: treemap layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC015, CC023, CC035

**Related**: [[treemap-layout]]

---

### sunburst

**Definition**: A radial, space-filling layout that assigns hierarchical groups to angular slices and displays nested levels as concentric rings.

**Aliases**: sunburst layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC075

**Related**: [[sunburst-layout]], [[treemap-layout]]

---

### rectangle packing

**Definition**: A layout approach that packs fixed-size rectangles (e.g., building footprints) into a region while minimizing wasted space, used as a basis for CodeCity’s district layouts.

**Aliases**: rectangle packing layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC035, CC059

**Related**: [[treemap-layout]]

---

### treeline

**Definition**: A simple depth-first layout that places classes row-by-row with separators to indicate package levels, used as a baseline comparison in evaluations.

**Aliases**: treeline layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC035

---

### semantic layout

**Definition**: A layout algorithm that positions code elements based on semantic similarity extracted from source code (identifiers, comments) using NLP techniques like LDA topic modeling, rather than structural hierarchy.

**Aliases**: semantic similarity layout, NLP-based layout, topic-based layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC157

**Related**: [[semantic-similarity-layout]], [[galaxy-metaphor]]

**Example**: Files discussing "authentication" cluster together regardless of package structure

**Sources**: CC075

---

### history-resistant layout

**Definition**: A layout strategy for evolving cities that keeps artifacts at fixed positions across versions by pre-allocating the maximum space each entity will need over the whole history, avoiding “layout jumps”.

**Aliases**: history resistant layout, stable layout (evolution)

**Category**: layout

**Bounded Context**: universal

**Sources**: CC059

**Related**: [[time-travel]], [rectangle packing](#rectangle-packing)

---

### EvoStreets

**Definition**: A street-based layout approach where inner hierarchy nodes are rendered as straight streets and leaf nodes as square plots attached to streets, designed to preserve spatial order and expose evolution through consistent growth.

**Aliases**: EvoStreets layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC101

**Related**: [[street-layout]], [layout consistency](#layout-consistency)

---

### layout consistency

**Definition**: The degree to which successive layouts preserve spatial relationships (order, side, and neighborhood) so users can maintain a stable mental map across versions.

**Aliases**: layout stability, mental-map preservation

**Category**: layout

**Bounded Context**: universal

**Sources**: CC101

**Related**: [[street-layout]], [[time-travel]]

---

### city with clouds

**Definition**: A layout variant where the database is rendered above the code city (in the “sky”), visually separating inferred data entities from source-code artifacts.

**Aliases**: cloud layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC079

**Related**: [[database-access-visualization]]

---

### city with underground

**Definition**: A layout variant where the database is rendered below the code city (in the “underground”), leaving the main ground plane for source code artifacts.

**Aliases**: underground layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC079

**Related**: [[database-access-visualization]]

---

### edge bundling

**Definition**: A technique that routes many edges along shared paths so related edges form bundles, reducing visual clutter in dependency visualizations.

**Aliases**: bundled edges

**Category**: layout

**Bounded Context**: universal

**Sources**: CC035, CC059

**Related**: [[bundled-edge-relations]]

---

### progressive bricks

**Definition**: An adaptive brick layout that spreads method bricks around building “walls” to avoid extreme building height for classes with very high method counts.

**Aliases**: Progressive Bricks

**Category**: layout

**Bounded Context**: universal

**Sources**: CC035

**Related**: [[progressive-bricks-layout]]

---

### street layout

**Definition**: A layout that organizes buildings around streets representing directories or packages, aiming to improve navigability and spatial orientation.

**Aliases**: street-based layout

**Category**: layout

**Bounded Context**: universal

**Sources**: CC015

---

### spectral ordering

**Definition**: A graph-based ordering technique that uses eigenvectors of the graph Laplacian (notably the Fiedler vector) to place strongly related nodes closer together in a 1D sequence.

**Aliases**: spectral sequencing

**Category**: layout

**Bounded Context**: universal

**Sources**: CC106

**Related**: [Fiedler vector](#fiedler-vector)

---

### Fiedler vector

**Definition**: The eigenvector corresponding to the second-smallest eigenvalue of a graph Laplacian, commonly used for graph partitioning and spectral ordering.

**Aliases**: algebraic connectivity vector

**Category**: layout

**Bounded Context**: universal

**Sources**: CC106

**Related**: [spectral ordering](#spectral-ordering)

---

### Hilbert curve

**Definition**: A space-filling curve that maps a 1D sequence to a 2D path while preserving locality, often used to place items in a plane such that nearby sequence elements remain spatially close.

**Aliases**: Hilbert space-filling curve

**Category**: layout

**Bounded Context**: universal

**Sources**: CC106

**Example**: CC106 places “floor blocks” along a Hilbert curve and merges them into class buildings in VR City.

---

### topology

**Definition**: Structural cues in the city (e.g., altitude/stacking) that help convey hierarchy such as nested packages.

**Aliases**: city topology

**Category**: layout

**Bounded Context**: universal

**Sources**: CC023

---

### stacked platforms

**Definition**: A topology technique where nested package districts are rendered on platforms at different altitudes.

**Aliases**: stacked-platform topology

**Category**: layout

**Bounded Context**: universal

**Sources**: CC023

**Related**: [[stacked-platform-topology]]

**Related**: [[street-layout]]

---

## Instrumentation

### instrumentation

**Definition**: The mechanism used to collect runtime execution data (e.g., profiler output or monitoring traces) for dynamic visualization.

**Aliases**: tracing, monitoring

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

---

### gprof

**Definition**: Profiler output used to provide timing information for dynamic visualization (as reported for Vizz3D in CC015).

**Aliases**: GNU profiler

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

---

### Kieker

**Definition**: Monitoring traces used as an instrumentation source for dynamic city visualization (as reported for SynchroVis/ExplorViz in CC015).

**Aliases**: Kieker traces

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

---

### inTrace

**Definition**: An Eclipse-based tracing tool used to record execution traces for dynamic visualization overlays; CC106 describes using inTrace without source-code modification and with user-defined trace filters.

**Aliases**: inTrace traces

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015, CC106

---

### ASM injection

**Definition**: Bytecode-injection approach used to obtain real-time timing information (as reported for High-Rise in CC015).

**Aliases**: bytecode injection

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

---

### JVMTI

**Definition**: Java Virtual Machine Tool Interface — cited by CC015 as an example of a general-purpose execution framework for reporting execution events.

**Aliases**: JVM Tool Interface

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC015

---

## Interaction

### entity

**Definition**: A dynamic rendered object a user can interact with; CC015 borrows videogame terminology when discussing dynamic software-city elements.

**Aliases**: rendered object

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC015

---

### citizen

**Definition**: A proposed “inhabitant” of the software city representing dynamic runtime objects (e.g., domain instances), discussed by CC015 as a way to depict execution behavior without overwhelming the viewer.

**Aliases**: city inhabitant

**Category**: metaphor

**Bounded Context**: universal

**Sources**: CC015

---

### selection

**Definition**: Interaction that selects a set of buildings/districts as the target for inspection or further operations.

**Aliases**: selection set

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC023, CC035

**Related**: [[selection]]

---

### teleportation

**Definition**: A VR locomotion technique where a user “jumps” to a new position in the virtual space, commonly used to traverse large scenes when physical room-scale walking area is limited.

**Aliases**: teleport locomotion

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC106

**Related**: [VR visualization](#vr-visualization)

---

### metaphor-aware navigation

**Definition**: A navigation approach where movement controls are adapted to the metaphor and the system can assist locomotion (e.g., routing along metaphor-feasible paths) to reduce disorientation in 3D worlds.

**Aliases**: metaphor-dependent navigation, assisted navigation

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC030

**Related**: [[navigation-modes]]

**Example**: In a city/building metaphor, moving from one "office" to another follows corridors and stairs rather than passing through walls.

---

### sonification

**Definition**: Converting data values into non-speech audio tones for non-visual consumption, enabling blind/low-vision users and eyes-free exploration of metric values.

**Aliases**: audio encoding, metric sonification

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC158, CC159

**Related**: [[sonification-navigation]], [[accessibility-mode]]

**Example**: Building height encoded as audio pitch—taller buildings produce higher-pitched tones when focused.

---

### gaze-guided navigation

**Definition**: Using eye-tracking to infer user intent and guide navigation in VR, enabling hands-free interaction based on where the user looks.

**Aliases**: eye-tracking navigation, gaze-based interaction

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC161

**Related**: [[gaze-based-interaction]], [[vr-immersion]]

---

### LLM-guided navigation

**Definition**: A navigation enhancement that uses Large Language Models to interpret natural language developer queries and guide exploration to relevant code elements in the visualization.

**Aliases**: AI-guided exploration, intent-aware navigation

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC155

**Related**: [[llm-guided-navigation]], [[navigation-modes]]

**Example**: User asks "show me the authentication logic" and the system navigates to relevant buildings.

---

### semantic zoom

**Definition**: A camera-distance-responsive visualization mechanism where the graphical representation of software elements changes based on the virtual camera's distance from visual objects, showing aggregate views at far distances and detailed views at close distances.

**Aliases**: level-of-detail zoom, context-aware zoom

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC164

**Related**: [[semantic-zoom]], [[adaptive-lod]], [[multilevel-visualization]]

**Example**: At far zoom, packages appear as colored regions; zooming in reveals individual class buildings with metric encodings.

---

### mini-map

**Definition**: A miniature two-dimensional top-view projection of the software city displayed alongside the 3D visualization, providing navigational context and enabling quick orientation and teleportation to different areas.

**Aliases**: overview map, navigation map, radar view

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC164

**Related**: [[mini-map-navigation]], [[navigation-modes]]

---

### adaptive LOD

**Definition**: Dynamic adjustment of visualization Level of Detail based on multiple contextual factors including user roles, current development tasks, code metrics, and real-time code changes.

**Aliases**: context-aware LOD, dynamic level of detail

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC166

**Related**: [[adaptive-lod]], [[semantic-zoom]]

---

### evolution sonification

**Definition**: Encoding software evolution patterns (commit frequency, change intensity) as audio signals, using a heartbeat metaphor where tempo and intensity convey the health and activity rhythm of the evolving codebase.

**Aliases**: heartbeat sonification, evolution audio

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC165

**Related**: [[evolution-sonification]], [[sonification-navigation]], [[evolution-visualization]]

---

### developer competence metric

**Definition**: An expertise score derived from version control data (commit frequency, change significance, recency) indicating how much knowledge a developer has about specific code areas.

**Aliases**: expertise score, knowledge metric

**Category**: metric

**Bounded Context**: universal

**Sources**: CC168

**Related**: [[developer-knowledge-map]], [bus factor](#bus-factor), [code ownership](#code-ownership)

---

### knowledge gray zone

**Definition**: A code area with dangerously scarce developer competence, where no team member has sufficient expertise to maintain or modify the code effectively—a high bus factor risk.

**Aliases**: expertise gap, knowledge desert

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC168

**Related**: [[developer-knowledge-map]], [bus factor](#bus-factor)

---

### XAI for SE

**Definition**: Application of Explainable AI techniques to software engineering tasks, providing human-interpretable explanations for ML model predictions about code quality, defects, or security vulnerabilities.

**Aliases**: explainable AI for software engineering

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC169

**Related**: [[explainable-ai-overlay]]

---

### line-level risk localization

**Definition**: Using XAI attribution techniques to identify which specific lines of code within a file contributed most to an AI model's prediction (e.g., defect risk), enabling targeted remediation.

**Aliases**: line attribution, code risk localization

**Category**: analysis

**Bounded Context**: universal

**Sources**: CC169

**Related**: [[explainable-ai-overlay]], [[vulnerability-overlay]]

---

### CollaVRation

**Definition**: An immersive virtual reality environment for collaborative software development featuring live programming, UML visualization, round-trip engineering, and multi-user synchronization.

**Aliases**: collaborative VR development

**Category**: platform

**Bounded Context**: universal

**Sources**: CC167

**Related**: [[collaborative-multi-user-vr]]

---

### spawning

**Definition**: Creating an isolated view containing only a selected subset of the city to focus exploration.

**Aliases**: isolate selection

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC023, CC035

**Related**: [[spawning]]

---

### tagging

**Definition**: Assigning color and/or transparency to a selection to remember, emphasize, or deemphasize it during exploration.

**Aliases**: visual tagging

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC023, CC035, CC059

**Related**: [[visual-tagging]]

---

### query filtering

**Definition**: Selecting/filtering entities based on criteria (e.g., name, type, category, or relationships) using a query mechanism.

**Aliases**: query-based selection

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC023, CC035, CC059

**Related**: [[query-filtering]]

---

### elision

**Definition**: An interaction that removes selected artifacts from the current view (temporarily) to reduce occlusion and focus attention on the remaining city.

**Aliases**: hide selected

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC059

**Related**: [[elision]], [[selection]], [[query-filtering]]

---

### vertical navigation

**Definition**: Navigation mode that lets the user orbit or fly around the city, move forward/backward, and change altitude.

**Aliases**: flyover navigation

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC023, CC035

---

### horizontal navigation

**Definition**: Navigation mode that constrains movement within the city among buildings (no passing through buildings; no going below ground) to preserve realism and orientation.

**Aliases**: walk/drive navigation

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC023, CC035

---

### examine

**Definition**: A details-on-demand interaction that reveals an artifact’s identity and mapped metric values when the user hovers over it.

**Aliases**: hover inspection

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC035, CC059

**Related**: [[hover-inspection]]

---

### Multiple Collaborative Representations (MCR)

**Definition**: A collaborative visualization approach where each participant can create and modify their own tailored representation of the same underlying data, enabling parallel perspectives during a shared analysis session.

**Aliases**: MCR, multiple representations

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC057

**Related**: [[collaborative-multi-user-vr]], [[view-configuration]]

---

### Moose

**Definition**: A reengineering framework used as the foundation for CodeCity (making the tool language-independent for analyzed systems).

**Aliases**: Moose framework

**Category**: platform

**Bounded Context**: universal

**Sources**: CC020, CC023, CC024, CC035

---

## Platform

### CDF (Common Data Format)

**Definition**: A CodeMetropolis intermediate data format produced by the `converter` tool to represent code entities and metrics in a tool-agnostic way, serving as input to the mapping stage.

**Aliases**: Common Data Format, CDF file

**Category**: platform

**Bounded Context**: universal

**Sources**: CC130

**Related**: [CMXML](#cmxml), [IXML](#ixml)

---

### CMXML

**Definition**: The CodeMetropolis XML format used to represent buildable city elements (hierarchy plus mapped attributes, sizes, and positions) as input/output between toolchain stages.

**Aliases**: CodeMetropolis XML, CMXML format

**Category**: platform

**Bounded Context**: universal

**Sources**: CC130

**Related**: [CDF (Common Data Format)](#cdf-common-data-format), [IXML](#ixml)

---

### IXML

**Definition**: CodeMetropolis “Intermediate XML” produced by the mapping stage (and then enriched by placing) before rendering to a Minecraft world.

**Aliases**: intermediate XML, IXML file

**Category**: platform

**Bounded Context**: universal

**Sources**: CC130

**Related**: [CDF (Common Data Format)](#cdf-common-data-format), [CMXML](#cmxml)

---

### FAMIX

**Definition**: A language-independent meta-model for modeling object-oriented software structure (packages, classes, methods, attributes and relations), used as the basis for CodeCity’s analysis.

**Aliases**: FAMIX meta-model

**Category**: platform

**Bounded Context**: universal

**Sources**: CC020, CC024, CC035

**Related**: [Hismo](#hismo), [Moose](#moose)

---

### Hismo

**Definition**: A meta-model that extends FAMIX with historical data, modeling entity histories as sequences of versions/snapshots for evolution analysis.

**Aliases**: Hismo meta-model

**Category**: platform

**Bounded Context**: universal

**Sources**: CC035

**Related**: [FAMIX](#famix), [Moose](#moose), [time travel](#time-travel)

---

### iPlasma

**Definition**: A platform for parsing and quality assessment of object-oriented software; in CodeCity’s pipeline it is used to extract models from Java and C++ systems for import into Moose/FAMIX.

**Aliases**: iPlasma platform, iplasma

**Category**: platform

**Bounded Context**: universal

**Sources**: CC020, CC024

**Related**: [FAMIX](#famix), [Moose](#moose)

---

### Jun

**Definition**: An object-oriented 3D multimedia library used by CodeCity for OpenGL rendering of the interactive city visualization.

**Aliases**: Jun library

**Category**: platform

**Bounded Context**: universal

**Sources**: CC020, CC024

**Related**: [Moose](#moose)

---

### Abstract Syntax Tree (AST)

**Definition**: A tree representation of the syntactic structure of source code, commonly used as an intermediate format for analysis and metric extraction.

**Aliases**: AST

**Category**: platform

**Bounded Context**: universal

**Sources**: CC036

**Related**: [Esprima](#esprima)

---

### Esprima

**Definition**: A JavaScript parser used to generate an AST for JavaScript source code as part of a city-visualization pipeline.

**Aliases**: Esprima parser

**Category**: platform

**Bounded Context**: universal

**Sources**: CC036

**Related**: [Abstract Syntax Tree (AST)](#abstract-syntax-tree-ast)

---

### Three.js

**Definition**: A JavaScript 3D rendering framework (WebGL-based) used to draw and interact with software city visualizations in the browser.

**Aliases**: ThreeJS, three.js

**Category**: platform

**Bounded Context**: universal

**Sources**: CC036

**Related**: [VR visualization](#vr-visualization)

---

### A-Frame

**Definition**: A web framework for building 3D, augmented reality (AR), and virtual reality (VR) experiences in the browser; it extends HTML with 3D scene entities and integrates with WebXR.

**Aliases**: A-Frame framework

**Category**: platform

**Bounded Context**: universal

**Sources**: CC096, CC134

**Related**: [WebXR](#webxr), [WebGL](#webgl)

---

### BabiaXR

**Definition**: An open-source toolset for browser-based 3D data visualization built on A-Frame/WebXR; it includes a CodeCity component (BabiaXR-CodeCity) for software-city scenes.

**Aliases**: BabiaXR toolset

**Category**: platform

**Bounded Context**: universal

**Sources**: CC096, CC134

**Related**: [A-Frame](#a-frame), [WebXR](#webxr), [VR visualization](#vr-visualization)

---

### WebGL

**Definition**: A browser API for GPU-accelerated 2D/3D rendering used to implement interactive 3D visualizations on the web.

**Aliases**: Web Graphics Library

**Category**: platform

**Bounded Context**: universal

**Sources**: CC038, CC040

**Related**: [Three.js](#threejs)

---

### WebXR

**Definition**: A browser API for running virtual reality (VR) and augmented reality (AR) experiences in the browser, enabling “XR” interaction for web-based 3D visualizations.

**Aliases**: WebXR Device API

**Category**: platform

**Bounded Context**: universal

**Sources**: CC077

**Related**: [XR visualization](#xr-visualization), [VR visualization](#vr-visualization), [AR visualization](#ar-visualization), [WebGL](#webgl)

---

### OpenTelemetry

**Definition**: An observability standard/tooling ecosystem for collecting telemetry (traces, metrics, logs); in a live visualization pipeline it can provide runtime trace data for dynamic analysis.

**Aliases**: OTel, opentelemetry

**Category**: platform

**Bounded Context**: universal

**Sources**: CC077

**Related**: [dynamic analysis](#dynamic-analysis), [[dynamic-visualization]]

---

### SonarQube

**Definition**: A code-quality platform that runs static analysis and aggregates metrics/issues for projects; SoftVis3D integrates as a SonarQube extension to visualize project structure and metrics.

**Aliases**: Sonar

**Category**: platform

**Bounded Context**: universal

**Sources**: CC038, CC040

**Related**: [static analysis](#static-analysis), [code hotspot](#code-hotspot)

---

### SCM blame

**Definition**: Version-control “blame”/annotation data that attributes each current source line to a last-modifying author/revision; it can be used to derive per-file authorship/commit signals without full history (e.g., SoftVis3D loads SonarQube SCM data via the `/sources/scm` endpoint).

**Aliases**: blame info, annotate

**Category**: platform

**Bounded Context**: universal

**Sources**: CC038, CC040, CC136

**Related**: [bus factor](#bus-factor), [[evolution-visualization]]

---

### GraphViz

**Definition**: A graph visualization and layout toolkit; in software-structure visualizations it is often used both to compute node positions (layout engines like `dot` and `neato`) and to route edges.

**Aliases**: dot, neato

**Category**: platform

**Bounded Context**: universal

**Sources**: CC043

**Related**: [X3DOM](#x3dom)

---

### X3DOM

**Definition**: A JavaScript framework that renders X3D scenes in the browser by embedding X3D elements in HTML, enabling interactive 3D visualizations without native plugins.

**Aliases**: X3D in HTML

**Category**: platform

**Bounded Context**: universal

**Sources**: CC043

**Related**: [WebGL](#webgl), [GraphViz](#graphviz)

---

### Goanna

**Definition**: A static-analysis toolchain (NICTA) that can provide project dependency information; SoftViz3D integrates with a Goanna “reporter” API to retrieve dependency data.

**Aliases**: Goanna reporter

**Category**: platform

**Bounded Context**: universal

**Sources**: CC043

**Related**: [static analysis](#static-analysis), [[contextual-dependency-view]]

---

### MSE exchange format

**Definition**: A model interchange format used in the Moose ecosystem; CodeCity’s pipeline uses MSE files to import models extracted from source code into Moose/FAMIX.

**Aliases**: MSE, MSE format

**Category**: platform

**Bounded Context**: universal

**Sources**: CC024

**Related**: [iPlasma](#iplasma), [FAMIX](#famix), [Moose](#moose)

---

### Mondrian

**Definition**: An agile visualization framework in the Moose suite, used in the CodeCity tool chain for complementary 2D views (e.g., class blueprints) and as inspiration for CodeCity’s scripting approach.

**Aliases**: Mondrian framework

**Category**: platform

**Bounded Context**: universal

**Sources**: CC024

**Related**: [Moose](#moose), [class blueprint](#class-blueprint)

---

### class blueprint

**Definition**: A compact 2D visualization that supports understanding a class by depicting its internal structure and metrics as a blueprint-style view; used as a complementary view alongside the 3D city.

**Aliases**: class blueprints

**Category**: interaction

**Bounded Context**: universal

**Sources**: CC024

**Related**: [Mondrian](#mondrian), [[selection]]

---

### view configuration

**Definition**: A reusable specification of what to visualize (visibility, glyph types, layouts) and how to encode it (visual mappers), enabling task-specific city “views” without changing the underlying model.

**Aliases**: view configurations

**Category**: platform

**Bounded Context**: universal

**Sources**: CC024, CC035

**Related**: [[view-configuration]]

---

### cc.json

**Definition**: CodeCharta’s JSON-based interchange format for software “maps”, representing a file/folder hierarchy with per-node metric attributes and optional edges/metadata (often stored as `.cc.json`, sometimes compressed).

**Aliases**: CCJSON, .cc.json

**Category**: platform

**Bounded Context**: universal

**Sources**: CC091

**Related**: [city metaphor](#city-metaphor), [[file-as-building]]

---

### extended reality (XR)

**Definition**: An umbrella term for immersive/overlay interaction technologies (typically VR and AR; sometimes also mixed reality) used as environments for interacting with a software city visualization.

**Aliases**: XR, extended reality visualization

**Category**: platform

**Bounded Context**: universal

**Sources**: CC018

**Related**: [VR visualization](#vr-visualization), [AR visualization](#ar-visualization)

---

### CAVE

**Definition**: A room-sized projection-based virtual reality system (“Cave Automatic Virtual Environment”) that surrounds the user with stereoscopic imagery and tracks head/hand position for immersive navigation and interaction.

**Aliases**: Cave Automatic Virtual Environment

**Category**: platform

**Bounded Context**: universal

**Sources**: CC057

**Related**: [VR visualization](#vr-visualization)

---

### VR visualization

**Definition**: Software city visualization rendered in virtual reality using head-mounted displays (HMD) like Oculus Rift or HTC Vive, enabling immersive exploration.

**Aliases**: virtual reality visualization, immersive visualization, HMD visualization

**Category**: platform

**Bounded Context**: universal

**Sources**: CC015

**Related**: [AR visualization](#ar-visualization)

---

### AR visualization

**Definition**: Software city visualization using augmented reality, overlaying the city on the physical world via devices like HoloLens or marker cards.

**Aliases**: augmented reality visualization

**Category**: platform

**Bounded Context**: universal

**Sources**: CC015

**Related**: [VR visualization](#vr-visualization)

**Example**: SkyscrapAR projects the city onto a physical marker card.

---

## Last Updated

- **Date**: 2026-01-05
- **Sources processed**: CC009, CC014, CC015, CC017, CC018, CC020, CC023, CC024, CC025, CC035, CC036, CC038, CC040, CC041, CC043, CC053, CC059, CC075, CC079, CC080, CC085, CC086, CC091, CC092, CC093, CC094, CC096, CC102, CC103, CC104, CC106, CC069, CC071, CC077, CC098, CC108, CC116, CC117, CC128, CC129, CC130, CC131, CC133, CC134, CC137, CC140, CC002, CC005, CC006, CC021, CC026, CC030, CC034, CC045, CC054, CC055, CC057, CC064, CC066, CC070, CC074, CC076, CC078, CC083, CC084, CC100, CC101, CC107, CC114, CC120, CC121, CC126, CC136, CC143, CC147, CC148
