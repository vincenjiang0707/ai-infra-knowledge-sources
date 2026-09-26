source: https://docs.nvidia.com/dynamo/reference/backends/v-llm-omni-configuration
lastmod: 2026-09-24T19:58:16.636Z

vLLM-Omni Configuration


vLLM-Omni Configuration

CLI flag reference for the vLLM-Omni multimodal backend (python -m dynamo.vllm.omni).

The vLLM-Omni backend uses a dedicated entrypoint: `python -m dynamo.vllm.omni`

. This page documents its CLI flags. For deployment guides and per-modality examples, see the [Diffusion Overview](https://docs.nvidia.com/dynamo/diffusion/overview).

These are the vLLM-Omni orchestration flags. The omni worker also accepts the same underlying vLLM engine arguments and the cross-cutting [Dynamo Runtime](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration) flags (`--namespace`

, `--endpoint`

, and others).

## General Flags

Enable the vLLM-Omni orchestrator (required for all omni workloads).

Output modality the worker registers endpoints for.

Path to stage config YAML (optional; vLLM-Omni uses model defaults if omitted).

MoE expert switching boundary.

Scheduler flow_shift (5.0 for 720p, 12.0 for 480p).

Default frames per second for generated videos.

## Memory & Performance

Enable VAE slicing for memory optimization.

Enable VAE tiling for memory optimization.

Enable layerwise offloading on DiT modules to reduce GPU memory.

Number of ready layers to keep on GPU during generation.

Disable torch.compile for diffusion models.

Enable CPU offloading for diffusion models.

## Diffusion Cache

Diffusion cache backend.

Cache configuration as a JSON string (overrides defaults).

Enable cache-dit summary logging after diffusion forward passes.

## Parallelism

GPUs for Ulysses sequence parallelism in diffusion.

GPUs for ring sequence parallelism in diffusion.

GPUs for classifier-free guidance parallelism (1 or 2).

## Disaggregated Mode

See [vLLM-Omni Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/v-llm-omni-disaggregated-serving) for usage.

Run as a single-stage worker for the given stage ID. Requires `--stage-configs-path`

.

Run as the stage router. Requires `--stage-configs-path`

. Mutually exclusive with `--stage-id`

.

## Media Storage

Filesystem URL for storing generated media.

Base URL for rewriting media paths in responses (optional).