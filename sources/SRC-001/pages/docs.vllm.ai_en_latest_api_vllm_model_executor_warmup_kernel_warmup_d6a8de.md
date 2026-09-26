source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/kernel_warmup/
lastmod: 2026-09-24

Autotune FlashInfer operations. FlashInfer have many implementations for the same operation, autotuning runs benchmarks for each implementation and stores the results. The results are cached transparently and future calls to FlashInfer will use the best implementation. Without autotuning, FlashInfer will rely on heuristics, which may be significantly slower.

Every rank profiles the same tactics. When distributed, per-tactic timings are averaged over the world CPU group so all ranks select the same tactic.

## Source code in `vllm/model_executor/warmup/kernel_warmup.py`


| def flashinfer_autotune(runner: "GPUModelRunner") -> None:
"""Autotune FlashInfer operations.
FlashInfer have many implementations for the same operation,
autotuning runs benchmarks for each implementation and stores
the results. The results are cached transparently and
future calls to FlashInfer will use the best implementation.
Without autotuning, FlashInfer will rely on heuristics, which may
be significantly slower.
Every rank profiles the same tactics. When distributed, per-tactic
timings are averaged over the world CPU group so all ranks select the
same tactic.
"""
from flashinfer.autotuner import AutoTuner, set_autotune_process_group
import vllm.utils.flashinfer as fi_utils
from vllm.distributed.parallel_state import get_world_group
world = get_world_group()
is_leader = world.rank_in_group == 0
tuner = AutoTuner.get()
autotune_kwargs: dict = {}
skip_ops = _flashinfer_autotune_skip_ops(runner)
if skip_ops:
logger.info_once(
"Skipping FlashInfer autotuning for ops %s",
tuple(sorted(skip_ops)),
)
autotune_kwargs["skip_ops"] = skip_ops
cache_path = resolve_flashinfer_autotune_file(runner)
if is_leader:
logger.info_once("Using FlashInfer autotune cache file: %s", cache_path)
# We skip EPLB here since we don't want to record dummy metrics.
# Randomize inputs to avoid every token pick the same experts,
# which lead to some EP ranks receiving no tokens and skipping their
# MoE kernel entirely, and cause hang due to all-reduce collective
# during synchronized autotuning.
# Read cached autotune results and broadcast to all ranks.
cached_results: bytes | None = None
if is_leader and cache_path.exists():
with open(cache_path, "rb") as f:
cached_results = f.read()
cached_results = world.broadcast_object(cached_results, src=0)
if cached_results is not None:
write_flashinfer_autotune_cache(cache_path, cached_results)
world.barrier()
tuner.load_configs(str(cache_path))
group = world.cpu_group if world.world_size > 1 else None
set_autotune_process_group(group)
try:
with (
torch.inference_mode(),
fi_utils.autotune(tune_mode=True, **autotune_kwargs),
):
hisparse_enabled = (
runner.vllm_config.attention_config.hisparse_config is not None
)
if hisparse_enabled:
# HiSparse hot-buffer attention is bounded by decode batch
# size, not the prefill-sized batch used for the full model.
autotune_hisparse_flashinfer_attention(runner)
_run_flashinfer_autotune_dummy_runs(runner, skip_attn=hisparse_enabled)
replayssm_autotune_warmup(runner)
_autotune_kimi_k3_kda_qkvg(runner.get_model())
with torch.inference_mode():
_run_flashinfer_bf16_autotune_dummy_run(
runner, skip_ops=skip_ops, skip_attn=hisparse_enabled
)
finally:
set_autotune_process_group(None)
if world.world_size > 1:
world.barrier()
if is_leader:
tuner.save_configs(str(cache_path))
|