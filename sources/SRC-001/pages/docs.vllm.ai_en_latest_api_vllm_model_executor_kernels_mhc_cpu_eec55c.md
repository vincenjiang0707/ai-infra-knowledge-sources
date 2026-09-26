source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/cpu/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.mhc.cpu`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu)

Functions:

-
–[hc_head_fused_cpu](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu.hc_head_fused_cpu)CPU-ported HC head reduction (see

`test_hc_head_cpu`

in -
–[mhc_post_cpu](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu.mhc_post_cpu)CPU-ported mHC post block (see

`mhc_post_torch`

for the eager reference). -
–[mhc_pre_cpu](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu.mhc_pre_cpu)CPU-ported mHC pre block (see

`mhc_pre_torch`

for the eager reference).

##

`hc_head_fused_cpu(hidden_states, hc_fn, hc_scale, hc_base, rms_norm_eps, hc_eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu.hc_head_fused_cpu)

CPU-ported HC head reduction (see `test_hc_head_cpu`

in tests/kernels/test_mhc_kernels.py for the eager reference this is tested against).

The ported kernel's C++ signature takes `(hc_eps, norm_eps)`

-- the opposite order from this wrapper's `(rms_norm_eps, hc_eps)`

, which matches the real call site in `models/deepseek_v4/cpu/model.py`

.

## Source code in `vllm/model_executor/kernels/mhc/cpu.py`


##

`mhc_post_cpu(x, residual, post_layer_mix, comb_res_mix)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu.mhc_post_cpu)

CPU-ported mHC post block (see `mhc_post_torch`

for the eager reference).

## Source code in `vllm/model_executor/kernels/mhc/cpu.py`


##

`mhc_pre_cpu(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cpu.mhc_pre_cpu)

CPU-ported mHC pre block (see `mhc_pre_torch`

for the eager reference).

The ported kernel (`hc_pre_fused_cpu`

) only exposes one merged `hc_eps`

(used for both `hc_pre_eps`

/`hc_sinkhorn_eps`

) and hardcodes the post-mix multiplier to 2.0 -- true of every real call site in `models/deepseek_v4/cpu/model.py`

, so this is not a capability loss here.