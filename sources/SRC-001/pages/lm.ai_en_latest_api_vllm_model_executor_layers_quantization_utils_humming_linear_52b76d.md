source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/humming/linear/
lastmod: 2026-09-23

Rename/reshape a linear layer's quantized params (the canonical MPLinear layout: `weight_packed`

int32 + `weight_scale`

) into the parameter names and layout humming's weight schema expects (`weight`

/ `weight_scale`

).

## Source code in `vllm/model_executor/layers/quantization/utils/humming/linear.py`


| def convert_linear_layer_to_humming_standard(
layer: LinearBase, name_map: dict[str, str]
):
"""Rename/reshape a linear layer's quantized params (the canonical MPLinear
layout: ``weight_packed`` int32 + ``weight_scale``) into the parameter names
and layout humming's weight schema expects (``weight`` / ``weight_scale``)."""
for name, checkpoint_name in name_map.items():
tensor = getattr(layer, checkpoint_name)
delattr(layer, checkpoint_name)
if name == "weight":
input_dim = getattr(tensor, "input_dim", 1)
output_dim = getattr(tensor, "output_dim", 0)
if input_dim == 0 and output_dim == 1:
tensor = tensor.transpose(1, 0).contiguous()
else:
assert output_dim == 0 and input_dim == 1
tensor = tensor.view(tensor.size(0), -1).view(torch.int32)
elif name in ["weight_scale", "zero_point"]:
if getattr(tensor, "output_dim", 0) == 1:
tensor = tensor.transpose(0, 1).contiguous()
if tensor.ndim == 1:
tensor = tensor.unsqueeze(1)
tensor = tensor.view(torch.int32) if name == "zero_point" else tensor
if isinstance(tensor, torch.nn.Parameter):
param = tensor
else:
param = torch.nn.Parameter(tensor, requires_grad=False)
setattr(layer, name, param)
|