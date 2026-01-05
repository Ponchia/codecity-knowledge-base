---
id: I025
name: SecCityVR
origin: Paderborn University
year_introduced: 2025
status: research
source_refs: [CC069]
repo_url: https://github.com/dewue/SecCityVR
demo_url: https://www.youtube.com/watch?v=A0nZKu9Zsjg
primary_language: unknown
features_implemented: [F001, F002, F017, F008, F045, F005, F006, F030, F042, F026, F057]
last_updated: 2026-01-04
updated_from: [CC069]
---

# SecCityVR

## Overview

SecCityVR is a VR code-city environment that overlays static application security testing (SAST) results onto a 3D city. Classes are buildings, packages are platforms laid out with a treemap/bin-packing variant, and methods appear as floors (normally hidden). Vulnerable methods are widened and colored by severity; call-graph arcs can be toggled to show propagation between vulnerable methods. The tool targets Meta Quest headsets and supports collaborative multi-user exploration.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F001]] city-metaphor | City used to host vulnerability overlays. |
| [[F002]] class-as-building | Classes as buildings placed on package platforms. |
| [[F017]] package-as-district | Packages rendered as platforms; main code vs dependencies distinguished by platform color. |
| [[F008]] treemap-layout | Adapted treemap/bin-packing to keep near-square footprints. |
| [[F045]] method-as-floors | Methods mapped to internal floors; vulnerable methods highlighted. |
| [[F005]] height-mapping | Class building height extruded to LOC; method floor size/position derived from LOC. |
| [[F006]] color-mapping | Severity palette (red/orange/green/blue) for vulnerabilities. |
| [[F057]] vulnerability-overlay | SAST findings overlaid as widened, colored method floors; dependency platforms tinted magenta. |
| [[F030]] contextual-dependency-view | On-demand call-graph arcs for vulnerable methods. |
| [[F026]] navigation-modes | Fly/walk modes in VR city. |
| [[F042]] collaborative-multi-user-vr | Supports paired users exploring the same city session. |

## Technical Details (from CC069)

**Input**: SpotBugs/FindSecBugs XML for vulnerabilities; custom JSON with package hierarchy and call graph (built via SootUp Rapid Type Analysis).

**Pipeline**: CLI tools produce XML/JSON artifacts -> renderer builds city geometry -> VR client renders in Meta Quest.

**Encodings**: Methods wider than building footprint; severity colors: high=red, medium=orange, low=green, info=blue; dependency platforms colored magenta.

**Interaction**: Toggle incoming/outgoing call-graph arcs for vulnerable methods; controllers show legend and controls; teleport/fly/walk for navigation; info panel provides vulnerability description and mitigation guidance.

**Collaboration**: Multi-user session synchronizes positions/controllers; users can teleport to each other and enable a guided-review “follow” mode (developer auto-follows auditor). Call-graph visualization events are synchronized so all users see the same rendered arcs/highlighted methods.

## Evaluation (from CC069)

User study (n=17) compared SecCityVR to a dashboard: SUS median 70 vs 58.75; temporal demand (TLX) 10 vs 42.5; frustration 17.5 vs 52.5; task times longer in VR (~4 minutes per set). Collaboration study (n=8) reported similar trends with lower temporal demand in VR.

## Sources

- [CC069] Wueppelmann & Yigitbas (2025) - SecCityVR VR vulnerability visualization, mappings, call-graph overlays, and user studies
