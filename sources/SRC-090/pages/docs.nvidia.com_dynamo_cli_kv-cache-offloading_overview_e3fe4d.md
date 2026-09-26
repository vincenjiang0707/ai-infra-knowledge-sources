source: https://docs.nvidia.com/dynamo/cli/kv-cache-offloading/overview
lastmod: 2026-09-24T19:58:16.636Z

# Offload KV Cache Locally

KV cache offloading moves reusable KV blocks from GPU memory to host memory or storage. This tutorial starts an aggregated Dynamo deployment with one offloading backend, sends requests through it, and checks that the backend is running.

### Prepare Your Environment

Complete the local installation and start Dynamo’s NATS and etcd services before continuing. Run the commands from the root of the cloned Dynamo repository.

If `docker run`

opened a shell in a prebuilt runtime container, you are already in the correct
environment and can skip package installation when the table below marks the backend as included.
For a container running in the background, open a shell with `docker exec`

; the repository is
available at `/workspace`

:

If you installed Dynamo into a Python environment, activate that environment before continuing.

### Choose a Backend

Select one offloading backend for each worker. KVBM, LMCache, FlexKV, and HiCache are alternatives, not cache layers to stack together. KV-aware routing and NIXL-based prefill/decode transfer are separate features that can operate alongside the selected backend.

The Dynamo Operator does not install these packages. Local containers and Kubernetes deployments get them from the selected runtime image. The Python environment path installs packages on the host instead.

### Start Offloading

Choose a backend and follow its tab. The primary examples use `Qwen/Qwen3-0.6B`

and one GPU; the
optional disaggregated FlexKV example uses two GPUs. The vLLM launch scripts start the Dynamo
frontend and workers, and stop all processes when you press `Ctrl+C`

.

###### KVBM

###### LMCache

###### HiCache

###### FlexKV

KVBM is Dynamo’s native KV block manager and the recommended starting point for vLLM. The current Dynamo vLLM runtime container includes it. For a Python environment, install its wheel first:

Start an aggregated vLLM worker with a 20 GB host-memory cache:

The script selects `DynamoConnector`

. To add a disk tier later, set `DYN_KVBM_DISK_CACHE_GB`

and
`DYN_KVBM_DISK_CACHE_DIR`

. Keep every lower cache tier at least as large as the tier above it to
avoid repeatedly evicting and reloading the same blocks.

For all KVBM settings, see the [KVBM Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/kvbm-configuration).

### Send a Request

After the frontend listens on port 8000, send a request from another terminal:

Send the request again to create an opportunity to reuse its prompt prefix. A short request confirms the deployment path but does not establish a performance improvement. Use a representative workload with long, repeated prefixes to measure Time To First Token (TTFT) and cache hit rate.

## Next Steps

- Add
[KV-aware routing](https://docs.nvidia.com/dynamo/cli/kv-aware-routing/overview)when multiple workers can reuse cached prefixes. - Combine one offloading backend with
[disaggregated serving](https://docs.nvidia.com/dynamo/cli/disaggregated-serving/overview). In that topology, the offloading connector manages storage while NIXL transfers blocks from prefill to decode workers. - Review
[KVBM architecture](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-design)for Dynamo’s cache-tier and transfer design. - To make a custom inference engine visible to the KV router, implement
[KV event publishing](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/publish-kv-events).