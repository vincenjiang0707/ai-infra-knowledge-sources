# [Issue #4883] [Bug] pytorch backend silently hangs under concurrent decoding with qwen3_5_mtp speculative decoding

source: https://github.com/InternLM/lmdeploy/issues/4883
state: open | updated: 2026-08-20T08:22:34Z
labels: 

## 正文

# Bug: LMDeploy pytorch backend hangs under concurrent decoding with `qwen3_5_mtp` speculative decoding

## Summary

Under concurrent, long-context, multi-turn agentic decoding (8 rollout workers), the
LMDeploy **pytorch** backend silently freezes when speculative decoding is enabled with
`method="qwen3_5_mtp"`, `num_speculative_tokens=2`. All 8 single-GPU LMDeploy server
instances stop logging their periodic `Avg thr` heartbeat **simultaneously** and produce no
further output; the surrounding RL produce loop freezes. The pods/processes remain alive
(no crash, no OOM, no error/traceback). Disabling speculative decoding entirely (no
`SpeculativeConfig`) removes the hang in a same-workload control run (>5h, no freeze).

## Environment

| Item | Value |
| --- | --- |
| lmdeploy | `f03bdf1c485ceb1519ae6ea8594349261de04496` (`matrix72c/lmdeploy` fork == `InternLM/lmdeploy` upstream `main`, 2026-08-14, "refactor: separate request preprocessing from generation (#4856)") |
| xtuner | integration `a29fe9fcb8264dff3eef25f4581b32a9dbd3add5` (drives LMDeploy via `xtuner/v1/rl/rollout/lmdeploy.py`) |
| Python | 3.12 |
| Hardware | NVIDIA H200, 8 GPUs per node, RDMA/RoCEv2 |
| Model | Qwen3.5-VL MoE 35B-A3B, served text-only: `Qwen3_5_VLMoE35BA3Config` with `only_llm_forward=True`, vision tower + projector frozen |

## Serving configuration (reproduction)

LMDeploy is launched by xtuner's rollout worker from this rollout config (the
`lmdeploy_*`-prefixed keys become lmdeploy kwargs):

```python
# sandbox_rl configs/builder.py — build_rollout()
RolloutConfig(
    gpus_per_node=8,                         # 8 rollout workers, one per GPU
    tensor_parallel_size=1,                  # tp == 1
    expert_parallel_size=1,                  # ep == 1
    gpu_memory_utilization=0.82,
    context_length=262144,
    dtype="bfloat16",
    rollout_max_batch_size_per_instance=64,
    enable_return_routed_experts=True,
    extra_rollout_config={
        "lmdeploy_backend": "pytorch",
        "lmdeploy_log_level": "ERROR",
        "lmdeploy_uvicorn_log_level": "WARNING",
        "lmdeploy_tool_call_parser": "qwen3coder",
        "lmdeploy_reasoning_parser": "default",
        # --- culprits ---
        "lmdeploy_speculative_algorithm": "qwen3_5_mtp",
        "lmdeploy_speculative_num_draft_tokens": 2,
    },
)
```

xtuner turns those last two keys into lmdeploy's spec-decode config
(`xtuner/v1/rl/rollout/lmdeploy.py:378-388`):

```python
SpeculativeConfig(
    method="qwen3_5_mtp",
    num_speculative_tokens=2,
)
```

So the equivalent engine configuration under test is:

- backend: `pytorch`
- tp = 1, ep = 1, per-worker, 8 independent workers (no cross-GPU tensor/expert parallel)
- speculative decoding: `qwen3_5_mtp`, 2 draft tokens
- MTP proposer `Qwen3_5MTP` shares the target model's token embeddings
  (`lmdeploy/pytorch/spec_decode/proposers/qwen3_5_mtp.py`)

## Workload

Agentic RL rollout (CVE-Bench / Terminal-Bench): the in-sandbox Claude agent drives many
multi-turn tool-call requests through an external routed proxy -> 8 xtuner session servers
-> the 8 LMDeploy servers. Requests are long-context (up to ~262k ctx), reasoning + tool
calls, high request rate (tens of thousands of tokens/s in, thousands of requests).

## Observed symptoms

1. After ~3.5 h of producing rollouts (5 of 8 groups complete = 20 rollouts done), the 8
   `run_lmdeploy_server_wrapper` processes' `Avg thr ...` heartbeat (logged every ~10 s,
   idle or busy) **stopped simultaneously** at `13:44:49`.
2. The RL produce progress froze at `DisaggAsyncProduceStrategy ... 62% 5/8`.
3. The training log file's mtime froze (no further writes for hours).
4. Kubernetes pods stayed `RUNNING`; `kubebrain` reported no events (no OOM, no restart).
   No error or traceback was emitted anywhere — a silent hang, not a crash.
5. Only 6 non-fatal `SessionServer response hook failed` (malformed model responses,
   `KeyError: 'choices'` / `tool_use block missing id/name`) appeared earlier and are
   unrelated to the freeze point.

## Control experiment (speculative decoding disabled)

Same pipeline/config, only difference: removed the `lmdeploy_speculative_algorithm` and
`lmdeploy_speculative_num_draft_tokens` keys (=> `SpeculativeConfig` is `None`).

Result: **no hang**. Over 5+ h the LMDeploy heartbeat never stalled (log idle < 10 s the
whole time), rollouts kept completing (9 completed + 6 failed — the 6 failures were all
sandbox-creation `EnvGateway 429 Too Many Requests` exhaustion with
`sandbox_create_attempts=64`, an unrelated external capacity issue).

The failure fingerprint changed completely:

| | speculative ON (qwen3_5_mtp) | speculative OFF |
| --- | --- | --- |
| LMDeploy heartbeat | 8 instances stop simultaneously | continuous, >5 h |
| produce loop | frozen at 5/8 | keeps progressing |
| failure mode | silent hang (alive, no output) | active retry vs external 429 |

## Code pointers / hypotheses

The `qwen3_5_mtp` path in the pytorch engine is recent (added #4437; follow-up fixes #4568
tp>1, #4572 quant, #4611 dp). Relevant files:

- `lmdeploy/pytorch/spec_decode/proposers/qwen3_5_mtp.py` — `Qwen3_5MTP` (shares target
  `embed_tokens`, asserts it is not None).
- `lmdeploy/pytorch/spec_decode/proposers/deepseek_mtp.py` — base proposer.
- `lmdeploy/pytorch/spec_decode/spec_agent.py:595-693` — `_async_model_forward`, the MTP
  draft loop (`loop_count = num_spec_tokens - 1`, `proposer.get_outputs()`, `inputs.step()`).
- `lmdeploy/pytorch/spec_decode/base.py` — `BaseSpecModelAgent`, `update_main_model_outputs`.

Known hang-prone spots in the engine (not proven to be the cause):

- `lmdeploy/pytorch/engine/engine_loop.py:476` — `TODO: add watermark check event instead of
  async sleep`; currently waits with `await asyncio.sleep(0.1)` when no runnable request.
- `lmdeploy/pytorch/engine/mp_engine/zmq_rpc.py:32,422` — comments about avoiding hangs.
- `lmdeploy/pytorch/engine/executor/ray_executor.py:440` — "hope this will not lead to hanging".

## Still needed to pin the exact deadlock

1. A **minimal LMDeploy-only reproduction** (no xtuner): `serve api_server` with
   `--backend pytorch` + `SpeculativeConfig(method="qwen3_5_mtp", num_speculative_tokens=2)`
   on the Qwen3.5-35B-A3B model, hammered by concurrent multi-turn tool-call requests that
   mirror the agentic workload above.
2. A **stack dump of the frozen process** (e.g. `py-spy dump --pid <lmdeploy server>`) at the
   moment the `Avg thr` heartbeat stops. The LMDeploy internal logs live in the pod under
   `/tmp/ray` and are not captured by the outer job log, so a live stack is the quickest way
   to localize the deadlock.

## Reference runs

- Hang (speculative ON): cvebench smoke, job
  `sandbox-rl-cvebench-qwen35-rloo-smoke-020851-f4744`, freeze at `2026-08-19 13:44:49 +08:00`.
- Control (speculative OFF): cvebench smoke, job
  `sandbox-rl-cvebench-qwen35-rloo-smoke-080830-e6ca1`, no hang over >5 h.

## 评论 (1)

### RunningLeon · 2026-08-20

@matrix72c Thanks for your feedback. We'll try to reproduce it locally if possible. If possible, you could share the log files to check.
