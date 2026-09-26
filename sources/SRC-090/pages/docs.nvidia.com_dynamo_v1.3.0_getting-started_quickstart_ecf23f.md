source: https://docs.nvidia.com/dynamo/v1.3.0/getting-started/quickstart
lastmod: 2026-09-24T19:58:16.636Z

# Quickstart

Get a Dynamo OpenAI-compatible endpoint running in a container in about 5 minutes.

## Choose Your Path

Dynamo is backend-agnostic and Kubernetes-native without being Kubernetes-only. Use this container path to try the same frontend/router/worker stack locally; use the Kubernetes path when you want the operator, CRDs, Gateway API integration, autoscaling, scheduling, and cluster lifecycle management.

## Pull a Container

###### CUDA

###### XPU

Containers have all dependencies pre-installed. Pick your backend:

###### SGLang

###### TensorRT-LLM

###### vLLM

For container versions and tags, see [Release Artifacts](https://docs.nvidia.com/dynamo/v1.3.0/resources/release-artifacts#container-images).

**Hugging Face token required for gated models.** Llama, Kimi, Qwen-VL, and other gated models require `HF_TOKEN`

in your environment and accepting the model card’s license on huggingface.co. Set `export HF_TOKEN=hf_…`

before launching.

## Start the Frontend

In your container, start the OpenAI-compatible frontend on port 8000:

`--discovery-backend file`

avoids needing etcd. To run frontend and worker in the same terminal, background each command with `> logfile.log 2>&1 &`

.

## Start a Worker

In another terminal, launch a worker for your backend:

###### CUDA

###### XPU

###### SGLang

###### TensorRT-LLM

###### vLLM

## Verify and Test

Check the endpoint is up:

If you see `OK`

, send a chat completion:

Connection refused? The frontend takes a few seconds to start — retry. For production liveness and readiness probes, see [Health Checks](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/health-checks).

## From the Digest

## Dive Deeper

Pick a full install path from the [four options above](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/quickstart#choose-your-path), or explore how Dynamo works under the hood: