source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/v-llm-omni-disaggregated-serving
lastmod: 2026-09-24T19:58:16.636Z

vLLM-Omni Disaggregated Multi-Stage Serving


vLLM-Omni Disaggregated Multi-Stage Serving

Architecture of multi-stage vLLM-Omni pipelines (e.g. AR + Diffusion), with each stage on its own GPU for independent scaling and isolation.

Disaggregated serving is an advanced deployment mode of the vLLM-Omni backend (`dynamo.vllm.omni`

), used for models whose pipeline has multiple stages (e.g., AR + Diffusion). Each stage runs as an independent process on its own GPU, enabling independent scaling, GPU isolation, and multi-worker replicas per stage. It uses the omni entrypoint with the `--stage-id`

and `--omni-router`

flags described below. See the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview) for installation and shared configuration.

## Architecture

A lightweight router coordinates the stages, acting as a **pure message broker** — it never inspects or transforms inter-stage data.

**How it works:**

- The router sends the initial request to Stage 0 and receives back a lightweight connector reference (pointer to the output in shared memory).
- The router forwards that reference — unchanged — to the next stage. It never reads the bulk data.
- Each stage fetches its inputs from the connector, runs any model-specific processor (e.g.,
`ar2diffusion`

,`thinker2talker`

), then runs its engine. - Connector references accumulate as the pipeline progresses, so any stage can access outputs from all previous stages.
- The final stage’s result goes back to the router for formatting and response.

## Quick Start: GLM-Image (2-Stage, 2 GPUs)

GLM-Image is a 2-stage text-to-image model with an AR stage (generates prior token IDs) and a DiT stage (diffusion denoising + VAE decode). The built-in vLLM-Omni stage config already assigns each stage to a separate GPU.


Experimental:GLM-Image support is experimental; generation may fail or produce incorrect/garbled outputs for some prompts and sizes.

Test:

## Scaling Stage Replicas

Each stage registers independently with Dynamo’s service discovery. To scale a bottleneck stage, launch additional workers with the same `--stage-id`

on different GPUs — the router automatically load-balances across all replicas for that stage. Other stages are unaffected.

## Tested Models

## CLI Flags (Disaggregated Mode)

These flags are specific to disaggregated mode. For the full flag surface, see the [vLLM-Omni Configuration reference](https://docs.nvidia.com/dynamo/reference/backends/v-llm-omni-configuration).

Run as a single-stage worker for the given stage ID. Requires `--stage-configs-path`

.

Run as the stage router. Requires `--stage-configs-path`

. Mutually exclusive with `--stage-id`

.

Path to vLLM-Omni stage configuration YAML.

`async_chunk=true`

(streaming between stages) is not yet supported.