source: https://docs.vllm.ai/en/latest/api/vllm/lora/punica_wrapper/punica_cpu/
lastmod: 2026-09-24

#

`vllm.lora.punica_wrapper.punica_cpu`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu)

Classes:

-
–[PunicaWrapperCPU](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU)PunicaWrapperCPU is designed to manage and provide metadata for the punica


##

`PunicaWrapperCPU`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU)

Bases: [PunicaWrapperBase](https://docs.vllm.ai/punica_base/#vllm.lora.punica_wrapper.punica_base.PunicaWrapperBase)

PunicaWrapperCPU is designed to manage and provide metadata for the punica kernel. The main function is to maintain the state information for Multi-LoRA, and to provide the interface for the pytorch punica ops.

Methods:

-
–[add_expand](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand)Performs GEMM for multiple slices of lora_b.

-
–[add_lora_embedding](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding)Applies lora specifically for VocabParallelEmbeddingWithLoRA.

-
–[add_lora_linear](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear)Applicable to linear-related lora.

-
–[add_lora_logits](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits)Applies lora specifically for LogitsProcessorWithLoRA.

-
–[add_shrink](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink)Performs GEMM for multiple slices of lora_a.


## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


|
|

###

`_apply_expand(y, x, w_t_all, y_offset, y_slice_size, add_inputs=True)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU._apply_expand)

Perform the `y[:,y_offset:y_offset+y_slice_size]+=x@w_t_all`

computation, which is suitable for the GEMM of lora'b.

## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


###

`_apply_shrink(y, x, w_t_all, scale)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU._apply_shrink)

Perform the `y+=x@w_t_all`

computation, which is suitable for the GEMM of lora'a. When `is_prefill is`

true, it indicates that it is currently the prefill stage, and the `_shrink_prefill`

function should be called. Otherwise, it is the decode stage, and the _shrink_decode function should be called.

## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


###

`add_expand(y, x, lora_b_stacked, output_slices, offset_start=0, add_inputs=True, **kwargs)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand)

Performs GEMM for multiple slices of lora_b.

## Semantics

for i in range(len(lora_b_stacked)): slice = output_slices[i] y[:, offset:offset+slice] += x[i] @ lora_b_stacked[i] offset += slice

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(x))`Union[`

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Input tensors

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(lora_b_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_b's weight

-

(`output_slices`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(output_slices))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Every slice's size

-

(`offset_start`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(offset_start))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –The starting position of y, defaults to 0.

-

(`add_inputs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(add_inputs))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Defaults to True.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_expand(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Unused; accepted for compatibility with the base class signature.


## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


###

`add_lora_embedding(y, x, lora_b_stacked, add_inputs=True, **kwargs)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding)

Applies lora specifically for VocabParallelEmbeddingWithLoRA.

## Semantics

y += x @ lora_b_stacked

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor.

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding(lora_b_stacked))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)lora_b's weights.

-

(`add_inputs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding(add_inputs))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Default to True.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_embedding(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Unused; accepted for compatibility with the base class signature.


## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


###

`add_lora_linear(y, x, lora_a_stacked, lora_b_stacked, scale, output_slices, *, buffer=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear)

Applicable to linear-related lora.

## Semantics

for i in range(len(lora_a_stacked)): y[i] += ( x[i].unsqueeze(0) @ lora_a_stacked[indices[i], layer_idx, :, :] @ lora_b_stacked[indices[i], layer_idx, :, :] * scale ).squeeze(0)

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor. Will be changed in-place.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`lora_a_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(lora_a_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_a's weight.

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(lora_b_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_b's weight.

-

(`scale`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Scaling factor.

-

(`output_slices`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(output_slices))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Every slice's size.

-

(`buffer`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(buffer))`Optional[`

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]]`None`

) –Defaults to None.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_linear(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Unused; accepted for compatibility with the base class signature.


## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


###

`add_lora_logits(y, x, lora_a_stacked, lora_b_stacked, scale, *, buffer=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits)

Applies lora specifically for LogitsProcessorWithLoRA.

## Semantics

buffer = (x @ lora_a_stacked) * scale y += buffer @ lora_b_stacked

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor.

-

(`lora_a_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(lora_a_stacked))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)lora_a's weights.

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(lora_b_stacked))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)lora_b's weights.

-

(`scale`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Scaling factor.

-

(`buffer`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(buffer))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Default to None.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_lora_logits(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Forwarded to

`add_shrink`

and`add_expand`

.

## Source code in `vllm/lora/punica_wrapper/punica_cpu.py`


###

`add_shrink(y, x, lora_a_stacked, scale, **kwargs)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink)

Performs GEMM for multiple slices of lora_a. When `is_prefill is`

true, it indicates that it is currently the prefill stage, and the `_shrink_prefill`

function should be called. Otherwise, it is the decode stage, and the _shrink_decode function should be called.

Semantics: for i in range(len(lora_a_stacked)): y[i] += (x @ lora_a_stacked[i]) * scale

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink(y))`Union[`

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Output tensors

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`lora_a_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink(lora_a_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_a's weights

-

(`scale`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Scaling factor for the operation

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.punica_cpu.PunicaWrapperCPU.add_shrink(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Unused; accepted for compatibility with the base class signature.