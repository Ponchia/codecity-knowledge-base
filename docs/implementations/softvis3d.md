---
id: I019
name: SoftVis3D
origin: stefanrinderle (open-source)
year_introduced: 2015
status: maintained
source_refs: [CC038, CC040, CC114, CC128, CC129]
repo_url: https://github.com/stefanrinderle/softvis3d
demo_url: https://softvis3d.com/sonar/
primary_language: Java (SonarQube plugin) + TypeScript/React (frontend)
features_implemented: [F001, F005, F006, F007, F009, F013, F015, F017, F022, F023, F025, F030, F035, F038, F047, F048, F068, F070]
last_updated: 2026-01-04
updated_from: [CC038, CC040, CC114, CC128, CC129]
---

# SoftVis3D

## Overview

SoftVis3D is a SonarQube-integrated 3D software visualization tool that renders a “code city” in the browser (WebGL). It focuses on exploring project structure and identifying hotspots by mapping SonarQube metrics onto building footprint, height, and color.

## Architecture (from CC040)

- **SonarQube plugin**: serves the SoftVis3D UI as a SonarQube extension.
- **Frontend**: TypeScript/React/MobX + Three.js; uses orbit-style camera controls and a share mechanism that serializes view state into the URL (`visualizationStatus`).
- **Layout engine**: uses the `codecity-visualizer` library (district and evostreet illustrators) with configurable mapping rules. CC128 documents this library as a reusable TypeScript/ES2015 package with container-based placement strategies (e.g., grid/strip-treemap and lightmap packing) and Evostreet-specific configuration (house/road sizing, distribution, and layout constraints).

## Key Mappings (from CC038, CC040)

- **Buildings**: files
- **Districts**: folders/packages
- **Footprint / height**: configurable SonarQube metrics (default risk profile uses complexity for footprint and `ncloc` for height)
- **Color**: selectable metric (e.g., issues, coverage, authors, commits)

## Layouts / Profiles

- **District (CodeCity) layout**: standard district-based layout (folders/packages as districts).
- **Evostreet layout**: stable street-based layout for evolving systems (streets represent subsystems; branching streets indicate containment).
- **Profiles**: presets for common tasks (e.g., default risk, leak period/new code, duplicated lines); switching metrics creates a custom profile.
- **Filtering**: include/exclude patterns applied to file names via JavaScript regular expressions.
- **Scaling**: supports multiple scaling methods for footprint/height (logarithmic, exponential, linear with scaling cap, and linear without a max).

## Data / Limits (from CC038, CC040)

- **Metrics source**: “any metric from SonarSource” (via SonarQube).
- **SCM-derived signals**: author and commit counts are derived from SCM blame info; the implementation loads SCM data via SonarQube’s SCM API endpoint and computes `number_of_authors` / `number_of_commits` per file. If SCM blame info is unavailable, those signals are disabled.

## Dependency View (legacy Sonar plugin, from CC129)

CC129 (deprecated Sonar plugin) documents a second “dependency view” alongside the city view:

- **Graphviz requirement**: the plugin uses Graphviz `dot` to compute per-layer layouts (and requires configuring the `dot` binary path in SonarQube).
- **Dependency aggregation**: leaf dependencies are expanded into hierarchy-following “path” edges, inserting synthetic interface nodes (e.g., `interface_<parentId>`) and aggregating multiple dependencies onto shared path edges.
- **Edge weights**: edges track included dependency IDs and are rendered with a weight/thickness proportional to the aggregated count (`penwidth`).

## Reflexion-Model Integration Prototype (from CC114)

CC114 (a 2025 master’s thesis) describes a SoftVis3D-based prototype that integrates reflexion-model architecture analysis for a specific target system (Apache Lucene):

- **Architecture modules as islands**: defines architecture modules via regex package mappings and renders one island per module, arranged in a fixed grid layout.
- **Architecture dependency arrows**: renders module-to-module arrows and labels them as conforming vs violating dependencies (e.g., blue vs red), with a “show only violations” filter.
- **Hierarchical drill-down**: selecting a module-to-module arrow reveals the underlying class-to-class arrows on demand to avoid rendering all dependencies at once (≈7,000 class dependencies).
- **Highlight houses**: recolors buildings participating in the selected dependency relationship (purple) to connect architectural relationships to concrete classes/files.
- **Evaluation**: task-based remote user study with 5 participants (mean impact rating 4.2/5 reported), focused on identifying dependencies and violations.

The thesis reports replication packages on GitHub via a forked SoftVis3D repo and a modified `codecity-visualizer` library, but notes the prototype is hard-coded to Lucene’s architecture definitions.

## Sources

- [CC038] SoftVis3D website — SonarQube integration, city mappings, profiles, filtering, and metric options
- [CC040] SoftVis3D repository — inception year (2015), modules/tech stack, URL-serialized view state, and mapping/scaling rules
- [CC128] codecity-visualizer repository — layout/packing and evolution-model details used by SoftVis3D
- [CC129] sonar-softvis3d-plugin repository — deprecated SonarQube plugin; dependency view, Graphviz `dot` layout, and dependency aggregation logic
- [CC114] Mohsen (2025) — SoftVis3D-based prototype integrating reflexion models with island layout and violation arrows; includes a small user study
