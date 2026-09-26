source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/cpu/causal_conv1d/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d)

Functions:

-
–[causal_conv1d_fn_cpu](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d.causal_conv1d_fn_cpu)CPU implementation for causal_conv1d_fwd.

-
–[causal_conv1d_update_cpu](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d.causal_conv1d_update_cpu)CPU implementation for causal_conv1d_update.

-
–[causal_conv1d_update_torch](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d.causal_conv1d_update_torch)Pure PyTorch fallback for causal_conv1d_update.


##

`causal_conv1d_fn_cpu(x, weight, bias, conv_states, query_start_loc, cache_indices=None, has_initial_state=None, activation='silu', pad_slot_id=PAD_SLOT_ID, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d.causal_conv1d_fn_cpu)

CPU implementation for causal_conv1d_fwd.

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/causal_conv1d.py`


##

`causal_conv1d_update_cpu(x, conv_state, weight, bias=None, activation=None, conv_state_indices=None, query_start_loc=None, pad_slot_id=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d.causal_conv1d_update_cpu)

CPU implementation for causal_conv1d_update.

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/causal_conv1d.py`


##

`causal_conv1d_update_torch(x, conv_state, weight, bias=None, activation=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.causal_conv1d.causal_conv1d_update_torch)

Pure PyTorch fallback for causal_conv1d_update. Currently used as a fallback for Arm (aarch64) to leverage oneDNN/ACL F.conv1d kernels for batched decoding.