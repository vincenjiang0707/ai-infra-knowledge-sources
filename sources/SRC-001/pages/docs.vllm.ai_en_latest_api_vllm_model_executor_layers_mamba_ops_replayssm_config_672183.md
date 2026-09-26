source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/replayssm_config/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.ops.replayssm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.replayssm_config)

Launch-config selection for the ReplaySSM Mamba2 output_only decode kernel.

Mirrors `mamba_ssm.py`

: a hard-coded heuristic per kernel, plus an `override`

context manager for benchmarks/tests/config sweeps. Hardware is auto-detected (Blackwell vs not) so call sites need not thread it through.

Functions:

-
–[get_replayssm_config](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.replayssm_config.get_replayssm_config)Return the launch config for

`kernel`

(override > tuned default).

##

`get_replayssm_config(kernel, **shape)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.replayssm_config.get_replayssm_config)

Return the launch config for `kernel`

(override > tuned default).

kernel: "mamba2_output_only". `shape`

carries the keying dims (dstate; `L`

for the buffer length, default 16); hardware is auto-detected.