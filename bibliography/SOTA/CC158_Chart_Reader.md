# CC158: Chart Reader: Accessible Visualization Experiences Designed with Screen Reader Users

**Source URL**: https://dl.acm.org/doi/10.1145/3544548.3581186
**Authors**: John R. Thompson, Jesse J. Martinez, Alper Sarikaya, Edward Cutrell, Bongshin Lee
**Conference**: CHI 2023 (Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems)
**Location**: Hamburg, Germany
**Publisher**: Association for Computing Machinery
**Gap Category**: Accessibility

## Problem Statement

Most visualizations are incompatible with screen readers, even though screen readers are a core accessibility tool for blind and low vision individuals (BLVIs).

## Research Approach

- Partnered with 10 BLV screen reader users (SRUs) in an iterative co-design study
- Five-month study with three one-hour sessions per participant
- Designed and developed accessible visualization experiences that afford SRUs the autonomy to interactively read and understand visualizations

## Key Contribution

Chart Reader is a prototype accessibility engine that synthesizes:
- **Hierarchical navigation**
- **Sonification**
- **Cross-cutting insights**

Enables screen reader users to navigate and consume a data visualization as a data experience.

## System Features

### Five Regions for Navigation
1. **Data insights region** - subdivides into types: summary, trends, anomalies, statistics
2. **X-Axis region** - divided into bins for quick time navigation
3. **Y-Axis region** - divided into bins for value range navigation
4. **Data Points region** - linear navigation with sonification augmentations
5. **Series Filters** - list/hide available data series for targeted comparison

### Design Dimensions
- Structure
- Navigation
- Description
- Non-speech audio
- Focus

## Relevance to CodeCity Knowledge Base
- **Primary**: Foundation for "accessibility-mode" feature in software cities
- **Bounded Context**: universal
- **Feature Category**: platform/interaction
- **Techniques to Apply**: Hierarchical navigation, sonification, structured descriptions
- **Gap Filled**: Accessibility for 3D code visualization
