source: https://github.com/vllm-project/guidellm/issues/924

### Problem Statement

When deploying models, developers need to choose the best serving framework (e.g. comparing vLLM vs. SGLang) or

choose between different model providers. currently, guideLLM compiles and visualizes only single benchmark runs.

this would be helpful to visualize and choose whats best

### Proposed Solution

Introduce a new CLI command, guidellm compare, which allows users to pass multiple benchmark JSON report files. The command will parse the reports and generate a comparative visualization plot.

### Alternatives Considered

*No response*

### Usage Examples

guidellm compare vllm_benchmark.json sglang_benchmark.json \
--output-formats plot \
--output-path ./results/engine_comparison.png

### Additional Context

*No response*

## Problem Statement

When deploying models, developers need to choose the best serving framework (e.g. comparing vLLM vs. SGLang) or

choose between different model providers. currently, guideLLM compiles and visualizes only single benchmark runs.

this would be helpful to visualize and choose whats best

## Proposed Solution

Introduce a new CLI command, guidellm compare, which allows users to pass multiple benchmark JSON report files. The command will parse the reports and generate a comparative visualization plot.

## Alternatives Considered

No response## Usage Examples

## Additional Context

No response