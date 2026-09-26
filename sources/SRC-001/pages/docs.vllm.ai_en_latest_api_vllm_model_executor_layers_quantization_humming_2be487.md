source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/humming/
lastmod: 2026-09-24

class HummingMoEMethod(FusedMoEMethodBase):
def __init__(
self, quant_config: HummingLayerQuantizationConfig, moe: "FusedMoEConfig"
) -> None:
super().__init__(moe)
self.quant_config = quant_config
self.weight_schema = quant_config.weight_schema
self.input_schema = quant_config.input_schema
self.force_weight_schema = quant_config.force_weight_schema
self.force_input_schema = quant_config.force_input_schema
# Derive QuantKeys from humming schemas.
# Prefer force schemas (the final format after requant) over base.
weight_key = weight_schema_to_quant_key(
self.force_weight_schema or self.weight_schema, moe.in_dtype
)
runtime_input_schema = check_and_fallback_input_schema(
weight_schema=self.force_weight_schema or self.weight_schema,
input_schema=self.force_input_schema or self.input_schema,
param_dtype=moe.in_dtype,
allow_fallback=quant_config.allow_input_schema_fallback,
)
activation_key = input_schema_to_quant_key(runtime_input_schema, moe.in_dtype)
# Select Humming MoE experts
self.experts_cls = select_humming_moe_experts(
config=self.moe,
weight_key=weight_key,
activation_key=activation_key,
)
def prepare_weight_loader(self, layer, weight_loader):
def new_weight_loader(
param: torch.nn.Parameter,
loaded_weight: torch.Tensor,
weight_name: str,
shard_id: str,
expert_id: int | None = None,
return_success: bool = False,
):
name = param.param_name
float_dtypes = [torch.float16, torch.bfloat16, torch.float32]
is_unquantized = name == "weight" and loaded_weight.dtype in float_dtypes
# online quant (fp16/bf16 -> quant_type)
if is_unquantized:
assert isinstance(self.weight_schema, _hm.HummingWeightSchema)
tensors = self.weight_schema.quant_tensor(
loaded_weight.to(param.device),
self.weight_schema,
layer.param_dtype,
)
success = True
for key, tensor in tensors.items():
if tensor is None or tensor.nelement() == 0:
continue
sublayer_name = "w2" if shard_id == "w2" else "w13"
param = getattr(layer, sublayer_name + "_" + key)
part_success = param.weight_loader(
param=param,
loaded_weight=tensor.cpu(),
weight_name=shard_id + "_" + key,
shard_id=shard_id,
expert_id=expert_id,
return_success=return_success,
)
success = success and part_success
return success if return_success else None
# weight processing logic for specific quantization schema
loaded_weight = self.weight_schema.process_loaded_weight(
tensor=loaded_weight,
name=name,
)
return weight_loader(
param,
loaded_weight,
weight_name,
shard_id=shard_id,
expert_id=expert_id,
return_success=return_success,
)
return new_weight_loader
def create_weights(
self,
layer: RoutedExperts,
num_experts: int,
hidden_size: int,
intermediate_size_per_partition: int,
params_dtype: torch.dtype,
**extra_weight_attrs,
):
layer.num_experts = num_experts
layer.param_dtype = params_dtype
layer.intermediate_size = intermediate_size_per_partition
input_schema = self.force_input_schema or self.input_schema
input_schema = input_schema.to_humming_schema(params_dtype)
shape_k = gcd(hidden_size, intermediate_size_per_partition)
for name in ("weight_schema", "force_weight_schema"):
schema = getattr(self, name)
if getattr(schema, "hadamard_block_size", None) == -1:
schema = humming_update_schema_hadamard_block_size(
weight_schema=schema,
input_schema=input_schema,
shape_k=shape_k,
)
setattr(self, name, schema)
weight_loader = extra_weight_attrs.get("weight_loader", default_weight_loader)
weight_loader = self.prepare_weight_loader(layer, weight_loader)
extra_weight_attrs["weight_loader"] = weight_loader
# sublayer: a layer contains multiple sets of weights for quantized GEMM
# (e.g., weight, weight_scale, etc.).
# The weight names of sublayer start with the prefix "{sublayer_name}_"
w13_output_size = intermediate_size_per_partition * self.moe.w13_num_shards
layer.sublayer_configs = {
"w13": {
"shape_n": w13_output_size,
"shape_k": hidden_size,
"tensors_attrs": self.weight_schema.get_padded_tensors_attrs(
shape_n=w13_output_size,
shape_k=hidden_size,
num_experts=num_experts,
param_dtype=params_dtype,
has_bias=self.moe.has_bias,
),
},
"w2": {
"shape_n": hidden_size,
"shape_k": intermediate_size_per_partition,
"tensors_attrs": self.weight_schema.get_padded_tensors_attrs(
shape_n=hidden_size,
shape_k=intermediate_size_per_partition,
num_experts=num_experts,
param_dtype=params_dtype,
has_bias=self.moe.has_bias,
),
},
}
for sublayer_name, configs in layer.sublayer_configs.items():
for name, attrs in configs["tensors_attrs"].items():
tensor = torch.empty(attrs["shape"], dtype=attrs["dtype"])
param = torch.nn.Parameter(tensor, requires_grad=False)
extra_attrs = attrs.get("extra_attrs", {}).copy()
extra_attrs.update(extra_weight_attrs)
param = prepare_moe_param(tensor, name, extra_attrs)
setattr(layer, f"{sublayer_name}_{name}", param)
if self.force_input_schema is not None:
self.input_schema = self.force_input_schema
def get_fused_moe_quant_config(self, layer: RoutedExperts) -> FusedMoEQuantConfig:
return get_humming_moe_quant_config(
layer,
self.humming_configs,
gemm1_alpha=getattr(layer, "swiglu_alpha", None),
gemm1_beta=getattr(layer, "swiglu_beta", None),
gemm1_clamp_limit=getattr(layer, "swiglu_limit", None),
)
def process_weights_after_loading(self, layer: RoutedExperts) -> None:
if getattr(self, "processed", False):
return
self.processed = True
# Convert weights to Humming kernel format
self.humming_configs = convert_to_humming_moe_kernel_format(
layer=layer,
sublayer_configs=layer.sublayer_configs,
weight_schema=self.weight_schema,
input_schema=self.input_schema,
force_weight_schema=self.force_weight_schema,
allow_input_schema_fallback=self.quant_config.allow_input_schema_fallback,
)
# Build the MoE kernel
self.moe_quant_config = self.get_fused_moe_quant_config(layer)
assert self.moe_quant_config is not None
assert self.experts_cls is not None
self.moe_kernel = make_humming_moe_kernel(
self.moe_quant_config,
self.moe,
self.experts_cls,
routing_tables=layer._expert_routing_tables(),
)
def apply(
self,
layer: RoutedExperts,
x: torch.Tensor,
topk_weights: torch.Tensor,
topk_ids: torch.Tensor,
shared_experts: SharedExperts | None,
shared_experts_input: torch.Tensor | None,
) -> torch.Tensor:
"""Apply Humming-quantized MoE computation using the standard kernel flow.
This method uses FusedMoEKernel.apply() which orchestrates:
1. Preparation (quantization if needed - skipped for Humming via
expects_unquantized_inputs=True to prevent double quantization)
2. Expert computation (via experts.apply())
3. Finalization (weight application & reduction - no-op for Humming
since it's already done internally)
Humming handles quantization, weight application, and reduction
internally in the experts implementation.
Humming experts consume the weights and quantization tensors passed
through the standard modular kernel interface.
"""
assert self.moe_kernel is not None
return self.moe_kernel.apply(
hidden_states=x,
w1=layer.w13_weight,
w2=layer.w2_weight,
topk_ids=topk_ids,
topk_weights=topk_weights,
activation=layer.activation,
global_num_experts=layer.global_num_experts,
expert_map=layer.expert_map,
apply_router_weight_on_input=False,
shared_experts=shared_experts,
shared_experts_input=shared_experts_input,
)