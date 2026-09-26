source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/prefetch_ops/
lastmod: 2026-09-24

#

`vllm.model_executor.offloader.prefetch_ops`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops)

Custom ops for prefetch offloader torch.compile + CUDA graph compatibility.

These ops use mutates_args to create data dependencies that prevent the compiler from reordering prefetch/sync operations.

Functions:

-
–[register_prefetch_offloader_ops](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops.register_prefetch_offloader_ops)Register custom ops for prefetch offloader.


##

`_start_prefetch_impl(output_tensor, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops._start_prefetch_impl)

Start async prefetch of layer_idx weights.

Initiates H2D copy on the copy stream for the specified layer.

Parameters:

-

(`output_tensor`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops._start_prefetch_impl(output_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output from forward - declared as mutated to prevent torch.compile from reordering this op before the computation that produces output_tensor.

-

(`layer_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops._start_prefetch_impl(layer_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the layer to prefetch.


## Source code in `vllm/model_executor/offloader/prefetch_ops.py`


##

`_wait_prefetch_impl(input_tensor, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops._wait_prefetch_impl)

Wait for prefetch of layer_idx to complete.

Synchronizes the compute stream with the copy stream to ensure the prefetched weights are ready for use.

Parameters:

-

(`input_tensor`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops._wait_prefetch_impl(input_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input to the layer (e.g., hidden_states) - declared as mutated to create data dependency for torch.compile.

-

(`layer_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops._wait_prefetch_impl(layer_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the layer to wait for.


## Source code in `vllm/model_executor/offloader/prefetch_ops.py`


##

`register_prefetch_offloader_ops()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch_ops.register_prefetch_offloader_ops)

Register custom ops for prefetch offloader.

Must be called before the ops are used. This is typically done at module import time.