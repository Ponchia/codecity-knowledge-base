# CC163: GitLab Test Coverage Visualization

**Source URL**: https://docs.gitlab.com/ee/ci/testing/test_coverage_visualization.html
**Publisher**: GitLab
**Gap Category**: DevOps/CI Integration

## Overview

GitLab provides test coverage visualization integrated directly into the CI/CD workflow.

## Display Methods

Coverage data is displayed in multiple locations:

### Merge Request Widget
- Shows coverage percentage
- Shows changes compared to target branch

### Merge Request Diff
- Reveals which lines are covered by tests
- Inline visualization in code diff view

### Pipeline Jobs
- Allows monitoring of coverage results for individual jobs

## Supported Formats

### Cobertura
- Compatible with multiple languages
- Java, JavaScript, Python, Ruby

### JaCoCo
- Designed specifically for Java projects

## CI/CD Integration

### Configuration
- Uses `artifacts:reports:coverage_report` keyword in pipeline configurations

### Features
- Collects coverage reports from specified paths (including wildcards)
- Combines information from multiple reports automatically
- Processes files in background jobs

### Display
- Aggregates data directly in merge request diffs
- Enables developers to see test coverage impact immediately upon pipeline completion

## Relevance to CodeCity Knowledge Base
- **Primary**: Reference for "CI/CD coverage overlay" feature
- **Bounded Context**: universal
- **Feature Category**: analysis
- **Related Features**:
  - F058 (heat-map-overlay) - coverage as heat map
  - F057 (vulnerability-overlay) - similar overlay pattern
- **Gap Filled**: DevOps pipeline integration patterns
- **Design Patterns**:
  - Cobertura/JaCoCo format parsing
  - Line-level coverage mapping to buildings/bricks
  - Pipeline artifact integration
