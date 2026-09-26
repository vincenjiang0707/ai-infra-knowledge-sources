source: https://docs.nvidia.com/dynamo/cli/getting-started/quickstart
lastmod: 2026-09-25T12:26:00.485Z

# Quickstart

Get a Dynamo OpenAI-compatible endpoint running locally on an NVIDIA GPU or Intel XPU.

## Choose Your Path

Dynamo is backend-agnostic and Kubernetes-native without being Kubernetes-only. Use this container path to try the same frontend/router/worker stack locally; use the Kubernetes path when you want the operator, CRDs, Gateway API integration, autoscaling, scheduling, and cluster lifecycle management.

## Run Dynamo Locally

### Choose and install a build

###### NVIDIA GPU

###### Intel XPU

Containers have all dependencies pre-installed. Pick your backend:

**Hugging Face token required for gated models.** Llama, Kimi, Qwen-VL, and other gated models require `HF_TOKEN`

in your environment and accepting the model card’s license on huggingface.co. Set `export HF_TOKEN=hf_…`

before launching.

The remaining steps run inside the selected container. If you installed an NVIDIA wheel instead, run the same `python3 -m dynamo.*`

commands in your Python environment. See [Local Installation](https://docs.nvidia.com/dynamo/cli/installation/install-dynamo) for host prerequisites and virtual environment setup.

For published NVIDIA container versions and tags, see [Release Artifacts](https://docs.nvidia.com/dynamo/reference/general/release-artifacts.mdx).

### Start the frontend

Start the OpenAI-compatible frontend on port 8000:

`--discovery-backend file`

avoids needing etcd. To run the frontend and worker in the same terminal, background each command with `> logfile.log 2>&1 &`

.

### Start a worker

In another terminal, select the hardware and backend you installed, then launch the worker:

### Choose your worker command

Select the same hardware and backend you used for the installation.

python3 -m dynamo.sglang --model-path Qwen/Qwen3-0.6B --discovery-backend file

### Verify the endpoint

Check that the endpoint is up:

If you see `OK`

, send a chat completion:

Connection refused? The frontend takes a few seconds to start — retry. For production liveness and readiness probes, see [Health Check Reference](https://docs.nvidia.com/dynamo/reference/observability/health-checks).

## From the Digest

## Dive Deeper

Pick a full install path from the [four options above](https://docs.nvidia.com/dynamo/cli/getting-started/quickstart#choose-your-path), or explore how Dynamo works under the hood: