source: https://docs.nvidia.com/dynamo/cli/disaggregated-serving/overview
lastmod: 2026-09-24T19:58:16.636Z

# Disaggregated Serving

Disaggregated serving separates the prefill and decode phases of inference into independent workers, each scalable on its own and connected via [NIXL](https://docs.nvidia.com/dynamo/knowledge-base/concepts/system-architecture/disaggregated-serving) for KV cache transfer. This is the local equivalent of the disaggregated pattern in the [Kubernetes Disaggregated Serving guide](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview) — the same architecture, driven by CLI flags instead of a DynamoGraphDeployment.

For the architecture and when to use it, see [Disaggregated Serving](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview).

## How it works locally

A disaggregated deployment is still a frontend plus workers (see the [Overview](https://docs.nvidia.com/dynamo/cli/disaggregated-serving/overview)), except instead of one worker doing both phases, you run:

- A
**prefill worker**— computes the prompt’s KV cache. - A
**decode worker**— receives the KV cache over NIXL and generates tokens.

The `launch/disagg.sh`

presets start the frontend and both workers, pinned to separate GPUs with the KV-transfer config wired up. Requires 2 GPUs.

## Disaggregated serving

###### vLLM

###### SGLang

###### TensorRT-LLM

Each worker needs a unique `VLLM_NIXL_SIDE_CHANNEL_PORT`

; the preset sets these for you.

## Adding KV-aware routing

To scale each pool and route requests by cache overlap, use the `disagg_router.sh`

presets (2 prefill + 2 decode workers, 4 GPUs). See [KV-Aware Routing](https://docs.nvidia.com/dynamo/cli/kv-aware-routing/overview#disaggregated-serving-with-kv-routing).

With a disaggregated deployment running, try adding another prefill worker — the frontend discovers and uses it automatically.

## Troubleshooting

**Workers fail to start with NIXL errors.** Ensure NIXL is installed and side-channel ports don’t conflict. Each worker in a multi-worker setup needs a unique side-channel port.

## See also

— design and rationale[Disaggregated Serving (architecture)](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview)— route across prefill/decode pools[KV-Aware Routing](https://docs.nvidia.com/dynamo/cli/kv-aware-routing/overview)— P/D tuning guide[Tuning Disaggregated Performance](https://docs.nvidia.com/dynamo/kubernetes/operations/performance-tuning)— copyable commands for each launch script[vLLM local deployment examples](https://docs.nvidia.com/dynamo/recipes/cli-templates/v-llm)