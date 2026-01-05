---
id: I004
name: Vizz3D (software city based on Vizz3D)
origin: Panas et al. (ICECCS 2007)
year_introduced: 2007
status: historical
source_refs: [CC015]
repo_url: null
demo_url: null
primary_language: C/C++
features_implemented: [F001, F003, F014, F016]
last_updated: 2026-01-02
updated_from: [CC015]
---

# Vizz3D (software city based on Vizz3D)

## Overview

CC015 describes an unnamed software city implementation for C++ built using the Vizz3D visualization package. It renders member functions as buildings and adds dependency and profiling information.

## CC015 Table 1

- **Language**: C/C++
- **VR**: n/a
- **Building**: function
- **Source code**: n/a
- **Static**: LOC, complexity, call graphs, contains, inheritance, structural connectivity components
- **Dynamic**: gprof
- **Instrumentation**: none (-pg)

## Notes (from CC015)

- Buildings represent member functions placed on a class “platform”.
- LOC is indicated via exterior wall texture (not height).
- CC015 reports additional dependency depictions (e.g., header-file relationships) and gprof timing augmentation.

## Sources

- [CC015] Jeffery survey — Vizz3D description and Table 1

