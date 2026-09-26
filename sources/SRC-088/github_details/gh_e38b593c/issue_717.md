# [Issue #717] [RFC]: Add Timing Metrics and Performance Tracing to Training and Data Generation Pipelines

source: https://github.com/vllm-project/speculators/issues/717
state: open | updated: 2026-07-17T13:45:45Z
labels: RFC

## 正文

### Motivation.

Speculators currently has a well-structured metric logging system (`speculators.metrics` logger with TensorBoard/W&B/Trackio/MLflow backends) that tracks model quality metrics (loss, accuracy, per-position acceptance rates), but has no instrumentation for performance. Other important parts of the pipeline like response regeneration also does not record any meaningful performance metric. There are lots of ongoing work for preprocessing & regeneration pipeline hardening, multi-node training and they can all benefit from a better performance tracing system.

### Proposed Change.

Add a lightweight step timer to the trainer that breaks each training step into phases and emits per-window averages through the existing `speculators.metrics` logger (TensorBoard / W&B / Trackio / MLflow).
Metrics:

- `profile/fetch_ms` -- data loading + host-to-device transfer
- `profile/fwd_ms` -- model forward pass
- `profile/bwd_ms` -- loss.backward + grad clipping
- `profile/opt_ms` -- optimizer step + LR scheduler
- `profile/step_ms` -- total step wall-clock
- `profile/tokens_per_s` -- throughput
- `profile/fetch_frac` -- fraction of step spent waiting on data (fetch-bound indicator)

Similarly, add timing to the response regeneration pipeline (`scripts/response_regeneration/`) and offline data generation (`scripts/data_generation_offline.py`):

- Per-request latency (already partially exists in response regeneration via `time.time()`, but not aggregated)
- Batch/window throughput (requests/s, tokens/s)
- Queue/wait time when the vLLM server is saturated
- Safetensors write time for data generation

Or any other reasonably design.

### Any Other Things.

_No response_

## 评论 (5)

### omerap12 · 2026-07-05

Hey @shanjiaz , I have opened this #722 to address some of the tasks above :)

### orestis-z · 2026-07-06

Thanks @omerap12 !

I'll take the remaining two items (response regeneration pipeline timing + offline data generation timing). These are independent of #722.

### orestis-z · 2026-07-06

@shanjiaz one thought on the response regeneration + offline data generation timing :

The RFC mentions emitting through the `speculators.metrics` logger, which makes sense for the trainer (step-indexed scalars → TensorBoard/W&B). For the batch scripts though, I think plain logging + tqdm is a better fit:

- These are one-shot pipeline runs, not training loops — there's no natural step axis for experiment tracking
- `response_regeneration/script.py` currently has zero imports from `speculators.*`, and `data_generation_offline.py` only imports `setup_root_logger` — adding metrics logger coupling is a real cost
- The value of seeing "regeneration throughput" in a W&B dashboard alongside training curves seems low

I'm planning to go with: live throughput in tqdm postfix (req/s, tokens/s), periodic log summaries, and a final stats summary at the end. This gives the same observability with less plumbing, and matches the "or any other reasonable design" escape hatch in the RFC.

Open to pushback if there's a use case I'm missing for experiment-tracked pipeline metrics.

### orestis-z · 2026-07-06

> [@shanjiaz](https://github.com/shanjiaz) one thought on the response regeneration + offline data generation timing :
> 
> The RFC mentions emitting through the `speculators.metrics` logger, which makes sense for the trainer (step-indexed scalars → TensorBoard/W&B). For the batch scripts though, I think plain logging + tqdm is a better fit:
> 
> * These are one-shot pipeline runs, not training loops — there's no natural step axis for experiment tracking
> * `response_regeneration/script.py` currently has zero imports from `speculators.*`, and `data_generation_offline.py` only imports `setup_root_logger` — adding metrics logger coupling is a real cost
> * The value of seeing "regeneration throughput" in a W&B dashboard alongside training curves seems low
> 
> I'm planning to go with: live throughput in tqdm postfix (req/s, tokens/s), periodic log summaries, and a final stats summary at the end. This gives the same observability with less plumbing, and matches the "or any other reasonable design" escape hatch in the RFC.
> 
> Open to pushback if there's a use case I'm missing for experiment-tracked pipeline metrics.

@rahul-tuli tagging you since Helen is out

### shanjiaz · 2026-07-06

@orestis-z I think it makes sense! Let's use tqdm and logging.
