source: https://docs.nvidia.com/dynamo/zh-CN/reference/examples
lastmod: 2026-09-23T23:30:39.914Z

# Examples

Reference deployments for SGLang, TensorRT-LLM, vLLM, and custom Dynamo backends.

Use these examples when you want a concrete starting point instead of a conceptual guide. The examples in the Dynamo repository track `main`

; if you are using a stable release, prefer the examples from the matching release branch or the versioned recipes in these docs.

## Start Here

[Hello World custom backend](https://github.com/ai-dynamo/dynamo/tree/main/examples/custom_backend/hello_world)— a minimal GPU-unaware graph that demonstrates Dynamo’s component model.[Kubernetes Quickstart](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart)— run a model on Kubernetes with the current recommended path.[CLI Getting Started](https://docs.nvidia.com/dynamo/dev/cli/getting-started/introduction)— run Dynamo locally from the CLI.

## Backend Examples

[vLLM local deployment examples](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/v-llm)— CLI launch patterns for vLLM.[SGLang local deployment examples](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/sg-lang)— CLI launch patterns for SGLang.[TensorRT-LLM local deployment examples](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/tensor-rt-llm)— CLI launch patterns for TensorRT-LLM.

## Kubernetes Templates

[vLLM DGD templates](https://docs.nvidia.com/dynamo/dev/recipes/kubernetes-templates/dgd/v-llm)— aggregated, disaggregated, and multinode Kubernetes manifests.[SGLang DGD templates](https://docs.nvidia.com/dynamo/dev/recipes/kubernetes-templates/dgd/sg-lang)— aggregated and disaggregated Kubernetes manifests.[TensorRT-LLM DGD templates](https://docs.nvidia.com/dynamo/dev/recipes/kubernetes-templates/dgd/tensor-rt-llm)— TensorRT-LLM Kubernetes manifests.[DGDR template](https://docs.nvidia.com/dynamo/dev/recipes/kubernetes-templates/dgdr)— profiler and planner driven deployment request example.

## Component Examples

[Router Examples](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-examples)— Python API usage, Kubernetes examples, and custom routing patterns.[Planner Examples](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/planner/planner-examples)— custom load predictors and non-Kubernetes scaling environments.[Profiler Examples](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/profiler/profiler-examples)— DGDR YAMLs and profiling script examples.

## Repository Examples

Browse the full [examples directory](https://github.com/ai-dynamo/dynamo/tree/main/examples) for source-controlled examples that may not yet have a polished docs page.