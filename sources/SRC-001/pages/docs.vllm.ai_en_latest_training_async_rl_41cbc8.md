source: https://docs.vllm.ai/en/latest/training/async_rl/
lastmod: 2026-09-24

# Async Reinforcement Learning[¶](https://docs.vllm.ai#async-reinforcement-learning)

## Overview[¶](https://docs.vllm.ai#overview)

In a standard RL training loop, generation and training happen sequentially: the policy generates rollouts, then training runs on those rollouts, and the cycle repeats. During generation the training accelerators sit idle, and vice versa.

The **one-off pipelining** approach separates the generation and training phases into two parallel coroutines, allowing the model to generate new samples while simultaneously training on previously generated data. This can lead to better GPU utilization and greater training throughput.

However, this overlap introduces a complication: weights must be updated in the inference engine mid-flight, while requests may still be in progress.

## The Pause and Resume API[¶](https://docs.vllm.ai#the-pause-and-resume-api)

To safely update weights while the inference engine is running, vLLM provides `pause_generation`

and `resume_generation`

methods. These let the trainer coordinate a clean window for weight synchronization without losing in-flight work.

### pause_generation[¶](https://docs.vllm.ai#pause_generation)

The `mode`

parameter controls how in-flight requests are handled:

| Mode | Behavior |
|---|---|
`"abort"` | Abort all in-flight requests immediately and return partial results (default) |
`"wait"` | Wait for all in-flight requests to finish before pausing |
`"keep"` | Freeze requests in the queue; they resume when `resume_generation` is called |

The `clear_cache`

parameter controls whether to clear the KV cache and prefix cache after pausing.

### resume_generation[¶](https://docs.vllm.ai#resume_generation)

Resumes the scheduler after a pause. Any requests frozen with `mode="keep"`

will continue generating.

### HTTP Endpoints[¶](https://docs.vllm.ai#http-endpoints)

With `VLLM_SERVER_DEV_MODE=1`

, the vLLM HTTP server exposes the same functionality via:

`POST /pause?mode=keep`

- Pause generation`POST /resume`

- Resume generation`POST /abort_requests`

- Abort in-flight requests without pausing the scheduler (send`{}`

to abort all, or`{"request_ids": [...]}`

)`GET /weight_info`

- Return the latest committed`weight_version`


Data Parallelism

When using data parallelism with vLLM's **internal load balancer** (i.e. `data_parallel_backend="ray"`

), pause and resume are handled automatically across all DP ranks -- a single call is sufficient. When using an **external load balancer** (i.e. multiple independent vLLM instances behind a proxy), you must send pause and resume requests to **every** engine instance individually before and after the weight update.

## Typical Async RL Flow[¶](https://docs.vllm.ai#typical-async-rl-flow)

A typical async RL loop with weight syncing looks like this:

- Start generating rollouts from the current policy
- Once trainer has new weights to update to, pause generation with
`mode="keep"`

- Sync the updated weights from the trainer to the inference engine (see
[Weight Transfer](https://docs.vllm.ai/weight_transfer/)) - Resume generation -- in-flight requests continue with the new weights
- Repeat

The key insight is that requests paused with `mode="keep"`

will produce tokens from the **old** weights before the pause and tokens from the **new** weights after resume. The `clear_cache`

parameter controls whether the KV cache is invalidated during the pause. When `clear_cache=True`

, previously cached key-value entries are discarded, so all tokens generated after resume will be computed entirely with the new weights. When `clear_cache=False`

, existing KV cache entries are retained, meaning some tokens in context may still reflect the old weights (stale KV cache).

## Example[¶](https://docs.vllm.ai#example)

The [ async RLHF example](https://github.com/vllm-project/vllm/blob/main/examples/rl/rlhf_async_new_apis.py) demonstrates this pattern with `vllm.AsyncLLMEngine`

, NCCL weight transfer, and mid-flight pause/resume with validation.