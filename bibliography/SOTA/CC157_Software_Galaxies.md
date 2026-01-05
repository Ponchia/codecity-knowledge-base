# CC157: Software Galaxies: Displaying Coding Activities using a Galaxy Metaphor

**Source URL**: https://dl.acm.org/doi/10.1145/3481549.3481573
**Authors**: Daniel Atzberger, Willy Scheibel, Daniel Limberger, Jürgen Döllner
**Conference**: VINCI '21 (14th International Symposium on Visual Information Communication and Interaction)
**Date**: September 6-8, 2021, Potsdam, Germany
**Gap Category**: Alternative Metaphor

## Abstract

Software visualization uses metaphors to depict software and software development data that usually has no gestalt. This work presents a novel approach to 3D software visualization called Software Galaxy.

## Key Approach

### Layout Method
- Based on applying **Latent Dirichlet Allocation (LDA)** on source code
- Uses text clustering techniques from Natural Language Processing (NLP) domain
- Similarity extracted directly from source code

### Metaphor
- Utilizes a metaphor inspired from astronomy
- Depicts software metrics for single files and clusters
- 3D visualization capturing semantic relatedness

## Problem & Motivation

The choice of a metaphor and visual depiction is researched broadly, but deriving a layout based on similarity is still challenging. Through identifier names and comments, developers encode semantics and domain knowledge directly in source code. This motivates the use of NLP techniques on source code.

## Results

First experiments indicate that a 3D visualization capturing semantic relatedness can be beneficial for standard program comprehension tasks.

## Relevance to CodeCity Knowledge Base
- **Primary**: Alternative metaphor to city (galaxy-metaphor)
- **Bounded Context**: Could warrant new "galaxy-metaphor" context
- **Feature Category**: metaphor/layout
- **Differentiator**: Uses NLP/semantic similarity for layout vs structural hierarchy
- **Related Features**: F068 (island-metaphor), F001 (city-metaphor)
