---
id: I012
name: Code Park
origin: Khaloo et al. (VISSOFT 2017)
year_introduced: 2017
status: research
source_refs: [CC015, CC126]
repo_url: null
demo_url: null
primary_language: C#
features_implemented: [F001, F013, F026]
last_updated: 2026-01-04
updated_from: [CC015, CC126]
---

# Code Park

## Overview

Code Park (Khaloo et al., VISSOFT 2017) is a 3D “game-like” code visualization tool aimed at helping users (especially novices) learn an unfamiliar codebase by leveraging spatial memory. CC126 describes a park-like environment where each class is represented as a room and source code is displayed as syntax-aware “wallpaper” on the room’s walls.

Users can navigate the codebase using both an overview (bird’s-eye) mode and a first-person mode for inspecting code. Code Park implements orientation-preserving animated transitions for navigation actions such as “go to definition” (moving via bird’s-eye view and then into the destination class, with a blinking highlight marking the target).

## Evaluation (from CC126)

CC126 reports two studies:
- **Usability study (n=28)** comparing Code Park to Microsoft Visual Studio for C# comprehension tasks, reporting that participants found Code Park significantly easier to get familiar with, more helpful for learning a codebase, and unanimously more enjoyable.
- **Organization study (n=9)** where participants arranged 33 classes in the 3D environment; participants tended to group by existing directory structure when present, otherwise by semantic similarity and/or class size to aid later re-finding.

## CC015 Table 1

- **Language**: C#
- **VR**: n/a
- **Building**: class
- **Source code**: yes
- **Static**: size, method names
- **Dynamic**: n/a
- **Instrumentation**: n/a

## Sources

- [CC015] Jeffery survey — Code Park description and Table 1
- [CC126] Khaloo et al. (VISSOFT 2017) — primary paper (room-based class metaphor, code wallpaper, navigation modes, and two user studies)
