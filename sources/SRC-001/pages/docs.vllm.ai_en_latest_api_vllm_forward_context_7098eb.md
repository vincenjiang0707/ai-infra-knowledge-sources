source: https://docs.vllm.ai/en/latest/api/vllm/forward_context/
lastmod: 2026-09-23

#

`vllm.forward_context`

[¶](https://docs.vllm.ai#vllm.forward_context)

Classes:

-
–[BatchDescriptor](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor)Batch descriptor for cudagraph dispatching. We should keep the num of

-
–[DPMetadata](https://docs.vllm.ai#vllm.forward_context.DPMetadata) -
–[ForwardContext](https://docs.vllm.ai#vllm.forward_context.ForwardContext)

Functions:

-
–[get_forward_context](https://docs.vllm.ai#vllm.forward_context.get_forward_context)Get the current forward context.

-
–[in_piecewise_cudagraph](https://docs.vllm.ai#vllm.forward_context.in_piecewise_cudagraph)Whether the current forward runs in piecewise cudagraph mode (graph

-
–[override_forward_context](https://docs.vllm.ai#vllm.forward_context.override_forward_context)A context manager that overrides the current forward context.

-
–[set_forward_context](https://docs.vllm.ai#vllm.forward_context.set_forward_context)A context manager that stores the current forward context,


##

`BatchDescriptor`

`dataclass`

[¶](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor)

Batch descriptor for cudagraph dispatching. We should keep the num of items as minimal as possible to properly and uniquely describe the padded batch for cudagraph.

Attributes:

-
([has_lora](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.has_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether this batch has active LoRA adapters.

-
([num_active_loras](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.num_active_loras)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of distinct active LoRA adapters in this batch.

-
([num_reqs](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.num_reqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of requests in the batch. Can be None for PIECEWISE cudagraphs where

-
([uniform](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.uniform)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if all the requests in the batch have the same number of tokens.


## Source code in `vllm/forward_context.py`


###

`has_lora = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.has_lora)

Whether this batch has active LoRA adapters.

###

`num_active_loras = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.num_active_loras)

Number of distinct active LoRA adapters in this batch. When cudagraph_specialize_lora_count is enabled, separate CUDA graphs are captured for each num_active_loras value. This allows kernels (like fused_moe_lora) whose grid size depends on num_active_loras to be properly captured.

###

`num_reqs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.num_reqs)

Number of requests in the batch. Can be None for PIECEWISE cudagraphs where the cudagraphs can handle any number of requests.

###

`uniform = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.forward_context.BatchDescriptor.uniform)

True if all the requests in the batch have the same number of tokens.

##

`DPMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.forward_context.DPMetadata)

Methods:

-
–[sp_local_sizes](https://docs.vllm.ai#vllm.forward_context.DPMetadata.sp_local_sizes)Context manager for setting self.local_sizes. Same as self.chunked_sizes


## Source code in `vllm/forward_context.py`


###

`sp_local_sizes(sequence_parallel_size)`

[¶](https://docs.vllm.ai#vllm.forward_context.DPMetadata.sp_local_sizes)

Context manager for setting self.local_sizes. Same as self.chunked_sizes but without any chunking.

## Source code in `vllm/forward_context.py`


##

`ForwardContext`

`dataclass`

[¶](https://docs.vllm.ai#vllm.forward_context.ForwardContext)

Attributes:

-
([slot_mapping](https://docs.vllm.ai#vllm.forward_context.ForwardContext.slot_mapping)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] |[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Type Dict[str, AttentionMetadata] for v1, map from layer_name of each


## Source code in `vllm/forward_context.py`


###

`slot_mapping`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.forward_context.ForwardContext.slot_mapping)

Type Dict[str, AttentionMetadata] for v1, map from layer_name of each attention layer to its attention metadata Type List[Dict[str, AttentionMetadata]] for DBO. List of size two, one for each microbatch. Set dynamically for each forward pass

##

`get_forward_context()`

[¶](https://docs.vllm.ai#vllm.forward_context.get_forward_context)

Get the current forward context.

## Source code in `vllm/forward_context.py`


##

`in_piecewise_cudagraph()`

[¶](https://docs.vllm.ai#vllm.forward_context.in_piecewise_cudagraph)

Whether the current forward runs in piecewise cudagraph mode (graph segments separated by eager breaks), at capture or replay time.

## Source code in `vllm/forward_context.py`


##

`override_forward_context(forward_context)`

[¶](https://docs.vllm.ai#vllm.forward_context.override_forward_context)

A context manager that overrides the current forward context. This is used to override the forward context for a specific forward pass.

## Source code in `vllm/forward_context.py`


##

`set_forward_context(attn_metadata, vllm_config, num_tokens=None, num_tokens_across_dp=None, cudagraph_runtime_mode=CUDAGraphMode.NONE, batch_descriptor=None, ubatch_slices=None, slot_mapping=None, skip_compiled=False, is_padding=None)`

[¶](https://docs.vllm.ai#vllm.forward_context.set_forward_context)

A context manager that stores the current forward context, can be attention metadata, etc. Here we can inject common logic for every model forward pass.

## Source code in `vllm/forward_context.py`


|
|