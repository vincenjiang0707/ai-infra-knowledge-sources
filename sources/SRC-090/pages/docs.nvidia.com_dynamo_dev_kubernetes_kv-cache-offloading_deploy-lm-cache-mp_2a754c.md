source: https://docs.nvidia.com/dynamo/dev/kubernetes/kv-cache-offloading/deploy-lm-cache-mp
lastmod: 2026-09-24T19:58:16.636Z

# Deploy LMCache MP

Run aggregated vLLM serving with KV cache offloaded to a per-node LMCache MP DaemonSet over cross-Pod CUDA IPC.

This guide deploys Dynamo aggregated vLLM serving on Kubernetes with KV cache offloaded to a per-node LMCache MP DaemonSet, sharing tensors with the worker via cross-Pod CUDA IPC. It uses the [ v1beta1/agg_lmcache.yaml](https://github.com/ai-dynamo/dynamo/blob/fc626a5f053cdc4112d752be47eb08a303623311/examples/backends/vllm/deploy/v1beta1/agg_lmcache.yaml) manifest plus an

`LMCacheEngine`

CR managed by the LMCache operator.## Prerequisites

[cert-manager](https://cert-manager.io/docs/installation/)— the LMCache operator’s webhook certificates are issued through it:

### Install the LMCache operator

Tested with the LMCache operator image `lmcache/lmcache-operator:v0.5.2`

.

Verify the install:

### Create the HF token Secret

Both `Frontend`

and `worker`

reference `hf-token-secret`

via a Secret ref.
The Secret must exist or the pods fail to start with `secret "hf-token-secret" not found`

.

### Deploy the LMCacheEngine

Replace `my-tag`

below with the `lmcache/vllm-openai`

image tag you want to run.

The server tag must match
the LMCache version bundled inside the Dynamo worker image from the next step.
Validated: server `v0.4.6`

paired with
`nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.3.0`

(bundles LMCache 0.4.6). Check it with:
`docker run --rm --entrypoint python3 <worker-image> -c "import lmcache; print(lmcache.__version__)"`

.
Mismatched versions do not speak the same MP wire protocol.

Verify with:

### Deploy the Dynamo worker

Edit [ examples/backends/vllm/deploy/v1beta1/agg_lmcache.yaml](https://github.com/ai-dynamo/dynamo/blob/fc626a5f053cdc4112d752be47eb08a303623311/examples/backends/vllm/deploy/v1beta1/agg_lmcache.yaml): replace

`nvcr.io/nvidia/ai-dynamo/vllm-runtime:my-tag`

(on both `Frontend`

and
`worker`

) with your Dynamo vllm-runtime image.Verify with:

## Cleanup

## Related pages

[Set up KV Cache Offloading](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-cache-offloading/overview)— choose an offloading connector for a DGD worker.[KV Cache Offloading for vLLM](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/v-llm/kv-cache-offloading)— engine internals and the local-CLI workflow.