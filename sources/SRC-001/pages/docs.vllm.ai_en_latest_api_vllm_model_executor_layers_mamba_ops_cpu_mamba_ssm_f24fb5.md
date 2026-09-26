source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/cpu/mamba_ssm/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.ops.cpu.mamba_ssm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.mamba_ssm)

Functions:

-
–[selective_state_update](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.mamba_ssm.selective_state_update)CPU implementation for selective_state_update.


##

`selective_state_update(state, x, dt, A, B, C, D=None, z=None, dt_bias=None, dt_softplus=False, state_batch_indices=None, dst_state_batch_indices=None, null_block_id=NULL_BLOCK_ID, out=None, num_accepted_tokens=None, cu_seqlens=None, is_blackwell=False, enable_stochastic_rounding=False, cache_philox_rounds=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.mamba_ssm.selective_state_update)

CPU implementation for selective_state_update.