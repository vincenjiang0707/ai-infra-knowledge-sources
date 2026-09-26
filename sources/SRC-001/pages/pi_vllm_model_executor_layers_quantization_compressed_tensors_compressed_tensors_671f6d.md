source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors/
lastmod: 2026-09-24

class CompressedTensorsConfig(QuantizationConfig):
def __init__(
self,
target_scheme_map: dict[str, Any],
ignore: list[str],
quant_format: str,
kv_cache_scheme: dict[str, Any] | None = None,
config: dict[str, Any] | None = None,
transform_config: dict[str, Any] | None = None,
total_num_heads: int | None = None,
total_num_kv_heads: int | None = None,
):
super().__init__()
self.ignore = ignore
self.quant_format = quant_format
# Map from [target -> scheme]
self.target_scheme_map = target_scheme_map
self.kv_cache_scheme = kv_cache_scheme
self.config = config
self.total_num_heads = total_num_heads
self.total_num_kv_heads = total_num_kv_heads
if transform_config:
self.transform_config = TransformConfig.model_validate(transform_config)
else:
self.transform_config = None
def get_linear_method(self) -> "CompressedTensorsLinearMethod":
return CompressedTensorsLinearMethod(self)
def get_supported_act_dtypes(cls) -> list[torch.dtype]:
return [torch.float32, torch.float16, torch.bfloat16]
@classmethod
def get_min_capability(cls) -> int:
return 70
def get_name(self) -> QuantizationMethods:
return "compressed-tensors"
def apply_vllm_mapper(self, hf_to_vllm_mapper: "WeightsMapper"):
"""Transform layer paths in config targets to match vLLM's naming.
The WeightsMapper is designed for weight paths, but some backends
(e.g. transformers) use broad prefix mappings like "" -> "model."
which would incorrectly transform non-path targets.
compressed-tensors targets can be:
- Layer paths: "layers.0.self_attn.q_proj" -> transformed
- Module class names: "Linear" -> preserved (no ".")
- Regex patterns: "re:.*proj" -> preserved (starts with "re:")
"""
def _map_target(target: str) -> str | None:
is_layer_path = "." in target and not target.startswith("re:")
if is_layer_path:
return hf_to_vllm_mapper._map_name(target)
return target
def _apply_dict(d: dict) -> dict:
return {k: v for t, v in d.items() if (k := _map_target(t)) is not None}
def _apply_list(lst: list) -> list:
return [t for x in lst if (t := _map_target(x)) is not None]
self.target_scheme_map = _apply_dict(self.target_scheme_map)
self.ignore = _apply_list(self.ignore)
if self.kv_cache_scheme is not None:
self.kv_cache_scheme = _apply_dict(self.kv_cache_scheme)
def get_quant_method(
self,
layer: torch.nn.Module,
prefix: str,
) -> "QuantizeMethodBase | None":
if isinstance(layer, LinearBase):
# collect schemes
quant_scheme = self.get_scheme(layer=layer, layer_name=prefix)
input_tfms, output_tfms = get_linear_transform_schemes(
layer, prefix, self.transform_config, self.packed_modules_mapping
)
# choose quantization method
quant_method: LinearMethodBase = UnquantizedLinearMethod()
if quant_scheme is not None:
layer.scheme = quant_scheme
quant_method = CompressedTensorsLinearMethod(self)
# choose transform method
if any((input_tfms, output_tfms)):
return CompressedTensorsLinearTransformMethod.from_schemes(
quant_method, quant_scheme, input_tfms, output_tfms
)
else:
return quant_method
if isinstance(layer, ParallelLMHead):
try:
quant_scheme = self.get_scheme(layer=layer, layer_name=prefix)
except ValueError:
quant_scheme = None
if quant_scheme is not None:
layer.scheme = quant_scheme
return CompressedTensorsLinearMethod(self)
# ParallelLMHead subclasses VocabParallelEmbedding but is handled above as
# a linear; only true embedding lookups land here.
if isinstance(layer, VocabParallelEmbedding):
scheme_dict = self.get_scheme_dict(layer, layer_name=prefix)
weight_quant = scheme_dict.get("weights") if scheme_dict else None
if weight_quant is None:
return None # unquantized embedding
if not (
isinstance(weight_quant, QuantizationArgs)
and self._is_wNa16_group_channel(weight_quant, None)
and weight_quant.type == QuantizationType.INT
):
raise ValueError(
"compressed-tensors embeddings only support weight-only INT "
f"group/channel (WNA16) quantization, got: {weight_quant}"
)
return CompressedTensorsEmbeddingWNA16Int(weight_quant)
if isinstance(layer, Attention):
return CompressedTensorsKVCacheMethod(self)
if isinstance(layer, RoutedExperts):
return CompressedTensorsMoEMethod.get_moe_method(
self, layer, layer_name=prefix
)
return None
def _add_fused_moe_to_target_scheme_map(self): # XXXXXXXXXXXXXXXXXXXXXX
"""Helper function to update target_scheme_map
since linear layers get fused into RoutedExperts
targeting 'Linear' needs to also match
RoutedExperts modules.
"""
if (
"Linear" not in self.target_scheme_map
or "RoutedExperts" in self.target_scheme_map
):
return
self.target_scheme_map["RoutedExperts"] = self.target_scheme_map["Linear"]
@classmethod
def from_config(cls, config: dict[str, Any]) -> "CompressedTensorsConfig":
# We keep only config groups which are not doing Attention quantization
# because Attention quantization on its own is not supported by vLLM.
# It is coupled with KV-cache quantization, and if scales are present in the
# checkpoint, they will be used properly.
if "config_groups" in config:
grps_without_attn_quant = {}
for k, v in config["config_groups"].items():
# e.g. LlamaAttention, Qwen3Attention, etc.
if len(v["targets"]) == 1 and v["targets"][0].endswith("Attention"):
logger.warning(
"Skipping CompressedTensors config group for %s. Attention "
"quant is coupled with KV-cache quantization in vLLM.",
v["targets"][0],
)
continue
grps_without_attn_quant[k] = v
config["config_groups"] = grps_without_attn_quant
ignore: list[str] = cast(list[str], config.get("ignore", []))
quant_format = cast(str, config.get("format"))
target_scheme_map = cls._quantization_scheme_map_from_config(config=config)
# Check for deprecated sparsity config
cls._parse_sparsity_config(config=config)
return cls(
target_scheme_map=target_scheme_map,
ignore=ignore,
quant_format=quant_format,
config=config,
transform_config=config.get("transform_config"),
kv_cache_scheme=config.get("kv_cache_scheme"),
total_num_heads=config.get("total_num_heads"),
total_num_kv_heads=config.get("total_num_kv_heads"),
)
@classmethod
def _parse_sparsity_config(
cls, config: dict[str, Any]
) -> tuple[dict[str, SparsityCompressionConfig], list[str]]:
"""Args:
config: The `quantization_config` dictionary from config.json
Returns:
A tuple with two elements
1. A dictionary mapping target layer names to their corresponding
sparsity_config
2. A list of layer names to ignore for sparsity
"""
if not (sparsity_config := config.get(SPARSITY_CONFIG_NAME)):
return dict(), []
sparsity_config = SparsityCompressionConfig.model_validate(sparsity_config)
sparse_scheme_map: dict[str, SparsityCompressionConfig] = {
target: sparsity_config for target in sparsity_config.targets or list()
}
sparsity_ignore_list = sparsity_config.ignore or list()
# Raise DeprecationError if non-empty sparse_scheme_map is detected
if sparse_scheme_map:
raise DeprecationWarning(
"Sparsity support has been removed from compressed-tensors. "
"Please use a model without sparsity configuration."
)
return sparse_scheme_map, sparsity_ignore_list
@classmethod
def _quantization_scheme_map_from_config(
cls, config: dict[str, Any]
) -> QUANTIZATION_SCHEME_MAP_TYPE:
"""Args:
config: The `quantization_config` dictionary from config.json
Returns:
A dictionary mapping target layer names to their corresponding
quantization_args for weights and input activations
"""
target_scheme_map: dict[str, Any] = dict()
quant_format = cast(str, config.get("format"))
# The quant_config has multiple config_groups, each containing
# an input_activations key with details about how the activations are
# quantized, a weights key indicating how the weights are quantized,
# and a list of targets under the `targets` key, dictating which
# layers are impacted by the quantization details. The quantization
# details follow the structure defined by the QuantizationArgs
# pydantic model, which is used to verify the structure of the
# quant_config and also store the details for later use.
config_groups = config.get("config_groups", dict())
for _, quant_config in config_groups.items():
targets = quant_config.get("targets")
for target in targets:
target_scheme_map[target] = {}
weight_quant = QuantizationArgs.model_validate(
quant_config.get("weights")
)
if weight_quant.actorder in (
ActivationOrdering.GROUP.value,
ActivationOrdering.DYNAMIC.value,
):
raise ValueError(
"Compressed-tensors group/dynamic activation ordering "
f"(actorder={weight_quant.actorder!r}) is no longer supported. "
"Use a checkpoint with static/weight activation ordering or "
"without activation ordering."
)
target_scheme_map[target]["weights"] = weight_quant
target_scheme_map[target]["input_activations"] = None
target_scheme_map[target]["format"] = quant_config.get("format")
format = target_scheme_map[target].get("format")
# If no per-config format defined, use global format in config
act_quant_format = (
is_activation_quantization_format(format)
if format is not None
else is_activation_quantization_format(quant_format)
)
# w4a8fp8 is in packed-quantized format
# but needs input activation quantization
input_activations = quant_config.get("input_activations")
if act_quant_format or input_activations:
# The only case where we have activation quant supported
# but no input_activations provided in the config
# should be w8a16fp8 w8a16fp8 can also run for cases where
# there is an input_quant but it is ignored
if not input_activations:
assert (
target_scheme_map[target]["weights"].type
== QuantizationType.FLOAT
)
else:
target_scheme_map[target]["input_activations"] = (
QuantizationArgs.model_validate(
quant_config.get("input_activations")
)
)
# Static output-activation quant is applied as a float fake-quant
# on the layer output; capture it when present.
target_scheme_map[target]["output_activations"] = None
output_activations = quant_config.get("output_activations")
if output_activations:
target_scheme_map[target]["output_activations"] = (
QuantizationArgs.model_validate(output_activations)
)
return target_scheme_map
@classmethod
def get_config_filenames(cls) -> list[str]:
return []
@staticmethod
def _check_scheme_supported(
min_capability: int, error: bool = True, match_exact: bool = False
) -> bool:
capability_tuple = current_platform.get_device_capability()
if capability_tuple is not None:
capability = capability_tuple.to_int()
if match_exact:
supported = capability == min_capability
if error and not supported:
raise RuntimeError(
"Quantization scheme is not supported for the current GPU. "
f"Required capability: {min_capability}. "
f"Current capability: {capability}."
)
else:
supported = capability >= min_capability
if error and not supported:
raise RuntimeError(
"Quantization scheme is not supported for the current GPU. "
f"Min capability: {min_capability}. "
f"Current capability: {capability}."
)
return supported
else:
return not match_exact
@staticmethod
def _is_nvfp4_format(quant_args: QuantizationArgs):
if quant_args is None:
return False
is_tensor_group_quant = (
quant_args.strategy == QuantizationStrategy.TENSOR_GROUP.value
)
is_symmetric = quant_args.symmetric
is_group_size_16 = quant_args.group_size == 16
is_float_type = quant_args.type == QuantizationType.FLOAT
is_4_bits = quant_args.num_bits == 4
return (
is_tensor_group_quant
and is_float_type
and is_4_bits
and is_group_size_16
and is_symmetric
)
@staticmethod
def _is_mxfp4(quant_args: QuantizationArgs) -> bool:
if quant_args is None:
return False
is_group_quant = quant_args.strategy == QuantizationStrategy.GROUP.value
is_symmetric = quant_args.symmetric
is_group_size_32 = quant_args.group_size == 32
is_float_type = quant_args.type == QuantizationType.FLOAT
is_4_bits = quant_args.num_bits == 4
return (
is_group_quant
and is_float_type
and is_4_bits
and is_group_size_32
and is_symmetric
)
@staticmethod
def _is_mxfp8(quant_args: QuantizationArgs) -> bool:
if quant_args is None:
return False
is_group_quant = quant_args.strategy == QuantizationStrategy.GROUP.value
is_symmetric = quant_args.symmetric
is_group_size_32 = quant_args.group_size == 32
is_float_type = quant_args.type == QuantizationType.FLOAT
is_8_bits = quant_args.num_bits == 8
is_mxfp8_scale_dtype = quant_args.scale_dtype == torch.uint8
return (
is_group_quant
and is_float_type
and is_8_bits
and is_group_size_32
and is_symmetric
and is_mxfp8_scale_dtype
)
@staticmethod
def _is_static_tensor_w8a8(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
is_8_bits = weight_quant.num_bits == input_quant.num_bits == 8
weight_strategy = (
weight_quant.strategy == QuantizationStrategy.TENSOR.value
or weight_quant.strategy == QuantizationStrategy.CHANNEL.value
)
is_tensor = (
weight_strategy
and input_quant.strategy == QuantizationStrategy.TENSOR.value
)
is_static = not weight_quant.dynamic and not input_quant.dynamic
# Both symmetric and asymmetric input quantization supported.
# Only symmetric weight quantization supported.
return is_8_bits and is_tensor and weight_quant.symmetric and is_static
@staticmethod
def _is_dynamic_token_w8a8(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
is_8_bits = weight_quant.num_bits == input_quant.num_bits == 8
weight_strategy = (
weight_quant.strategy == QuantizationStrategy.TENSOR.value
or weight_quant.strategy == QuantizationStrategy.CHANNEL.value
)
is_token = (
weight_strategy and input_quant.strategy == QuantizationStrategy.TOKEN.value
)
is_dynamic = not weight_quant.dynamic and input_quant.dynamic
# Both symmetric and asymmetric input quantization supported.
# Only symmetric weight quantization supported.
return is_8_bits and is_token and weight_quant.symmetric and is_dynamic
@staticmethod
def _is_dynamic_token_w4a8_int(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
is_weight_4_bits = weight_quant.num_bits == 4
is_activation_8_bits = input_quant.num_bits == 8
weight_strategy = (
weight_quant.strategy == QuantizationStrategy.GROUP.value
or weight_quant.strategy == QuantizationStrategy.CHANNEL.value
)
is_token = (
weight_strategy and input_quant.strategy == QuantizationStrategy.TOKEN.value
)
is_dynamic = not weight_quant.dynamic and input_quant.dynamic
# Both symmetric and asymmetric input quantization supported.
# Only symmetric weight quantization supported.
return (
is_weight_4_bits
and is_activation_8_bits
and is_token
and weight_quant.symmetric
and is_dynamic
)
@staticmethod
def _is_fp8_w8a8(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
# Confirm weights and activations quantized.
if weight_quant is None or input_quant is None:
return False
# Confirm weight scheme is supported.
is_floating_point = (
weight_quant.type == QuantizationType.FLOAT
and input_quant.type == QuantizationType.FLOAT
)
is_symmetric_weight = weight_quant.symmetric
is_static_weight = not weight_quant.dynamic
is_tensor_or_channel_or_block_weight = weight_quant.strategy in [
QuantizationStrategy.TENSOR,
QuantizationStrategy.CHANNEL,
QuantizationStrategy.BLOCK,
]
if not (
is_floating_point
and is_symmetric_weight
and is_static_weight
and is_tensor_or_channel_or_block_weight
):
return False
# Dynamic quantization is always supported if weights supported.
if input_quant.dynamic:
return True
# Confirm activation scheme is supported.
is_symmetric_activation = input_quant.symmetric
is_per_tensor_activation = input_quant.strategy == QuantizationStrategy.TENSOR
return is_symmetric_activation and is_per_tensor_activation
@staticmethod
def _is_fp8_w4a8(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
if not weight_quant or not input_quant:
return False
is_weight_4_bits = weight_quant.num_bits == 4
is_activation_8_bits = input_quant.num_bits == 8
weight_strategy = weight_quant.strategy == QuantizationStrategy.GROUP.value
is_token = (
weight_strategy and input_quant.strategy == QuantizationStrategy.TOKEN.value
)
is_dynamic = not weight_quant.dynamic and input_quant.dynamic
is_symmetric = weight_quant.symmetric and input_quant.symmetric
# Only per-group symmetric weight (4bit)
# + per-tok symmetric activation (8bit) quantization supported.
return (
is_weight_4_bits
and is_activation_8_bits
and is_token
and is_symmetric
and is_dynamic
)
@classmethod
def _is_fp8_w4a8_sm90(
cls, weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
return cls._check_scheme_supported(
90, error=False, match_exact=True
) and cls._is_fp8_w4a8(weight_quant, input_quant)
@classmethod
def _is_fp8_w8a8_sm90(
cls, weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
return cls._check_scheme_supported(
90, error=False, match_exact=True
) and cls._is_fp8_w8a8(weight_quant, input_quant)
@classmethod
def _is_fp8_w8a8_sm100(
cls, weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
return cls._check_scheme_supported(
100, error=False, match_exact=True
) and cls._is_fp8_w8a8(weight_quant, input_quant)
@staticmethod
def _is_fp8_w8a16(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
# Confirm weights quantized.
if weight_quant is None:
return False
# Confirm we have floating points.
if weight_quant.type != QuantizationType.FLOAT:
return False
# Confirm weight scheme is supported.
is_symmetric_weight = weight_quant.symmetric
is_static_weight = not weight_quant.dynamic
is_tensor_or_channel_or_block_weight = weight_quant.strategy in [
QuantizationStrategy.TENSOR,
QuantizationStrategy.CHANNEL,
QuantizationStrategy.BLOCK,
]
return (
is_symmetric_weight
and is_static_weight
and is_tensor_or_channel_or_block_weight
)
@staticmethod
def _is_wNa16_group_channel(
weight_quant: QuantizationArgs, input_quant: QuantizationArgs
) -> bool:
input_quant_none = input_quant is None
is_channel_group = (
weight_quant.strategy == QuantizationStrategy.CHANNEL.value
or weight_quant.strategy == QuantizationStrategy.GROUP.value
)
is_static = not weight_quant.dynamic
return is_channel_group and input_quant_none and is_static
@staticmethod
def _is_wNa8o8_int(
weight_quant: QuantizationArgs,
input_quant: QuantizationArgs | None,
output_quant: QuantizationArgs | None,
format: str | None,
) -> bool:
"""Weight N-bit INT (pack-quantized for sub-byte, int-quantized for 8-bit)
with static per-tensor INT8 input/output activation quant, applied as a float
fake-quant around a weight-only matmul."""
is_int_pack_format = format in (
CompressionFormat.pack_quantized.value,
CompressionFormat.int_quantized.value,
)
is_channel_group = weight_quant.strategy in (
QuantizationStrategy.CHANNEL.value,
QuantizationStrategy.GROUP.value,
)
is_static_int = (
weight_quant.type == QuantizationType.INT and not weight_quant.dynamic
)
is_intN_weight = is_static_int and is_channel_group and is_int_pack_format
is_static_int8_in = (
input_quant is not None
and input_quant.type == QuantizationType.INT
and input_quant.strategy == QuantizationStrategy.TENSOR.value
and input_quant.num_bits == 8
and not input_quant.dynamic
)
is_static_int8_out = (
output_quant is not None
and output_quant.type == QuantizationType.INT
and output_quant.strategy == QuantizationStrategy.TENSOR.value
and output_quant.num_bits == 8
and not output_quant.dynamic
)
return is_intN_weight and (is_static_int8_in and is_static_int8_out)
@staticmethod
def _is_wNaM_int(
weight_quant: QuantizationArgs,
input_quant: QuantizationArgs | None,
format: str | None,
) -> bool:
"""Weight N-bit INT with symmetric dynamic INT activation quant
via Humming kernel."""
if input_quant is None:
return False
is_pack_format = format == CompressionFormat.pack_quantized.value
is_channel_group = weight_quant.strategy in (
QuantizationStrategy.CHANNEL.value,
QuantizationStrategy.GROUP.value,
)
is_int_N_weight = (
weight_quant.type == QuantizationType.INT and not weight_quant.dynamic
)
is_int_input = input_quant.type == QuantizationType.INT
is_symmetric_input = input_quant.symmetric
is_dynamic_input = input_quant.dynamic
is_per_token_or_group_input = input_quant.strategy in (
QuantizationStrategy.TOKEN.value,
QuantizationStrategy.GROUP.value,
)
return (
is_int_N_weight
and is_channel_group
and is_pack_format
and is_int_input
and is_symmetric_input
and is_dynamic_input
and is_per_token_or_group_input
)
def _get_scheme_from_parts(
self,
weight_quant: QuantizationArgs,
input_quant: QuantizationArgs,
output_quant: QuantizationArgs | None = None,
format: str | None = None,
layer_name: str | None = None,
) -> "CompressedTensorsScheme":
# use the per-layer format if defined, otherwise, use global format
format = format if format is not None else self.quant_format
# Detect If Mixed Precision
if self._is_nvfp4_format(weight_quant):
if input_quant is None:
return CompressedTensorsW4A4Fp4(use_a16=True)
if not self._is_nvfp4_format(input_quant):
raise ValueError(
"For NVFP4 weights, input quantization must also be NVFP4 "
"format, None for NVFP4A16"
)
return CompressedTensorsW4A4Fp4()
if self._is_mxfp4(weight_quant):
return CompressedTensorsW4A4Mxfp4()
if self._is_mxfp8(weight_quant):
return CompressedTensorsW8A8Mxfp8()
if self._is_fp8_w4a8_sm90(weight_quant, input_quant):
return CompressedTensorsW4A8Fp8(
num_bits=weight_quant.num_bits,
strategy=weight_quant.strategy,
symmetric=weight_quant.symmetric,
group_size=weight_quant.group_size,
)
# Must come before the WNA16 check; standard 4/8-bit weight-only (no
# output-activation scale) still falls through to WNA16.
if self._is_wNa8o8_int(weight_quant, input_quant, output_quant, format):
return CompressedTensorsWNA8O8Int(
num_bits=weight_quant.num_bits,
strategy=weight_quant.strategy,
group_size=weight_quant.group_size,
has_input_act=input_quant is not None,
has_output_act=output_quant is not None,
layer_name=layer_name,
quant_format=format,
)
if (
self._is_wNaM_int(weight_quant, input_quant, format)
and input_quant.num_bits == 8
):
return CompressedTensorsWNA8Int(
num_bits=weight_quant.num_bits,
strategy=weight_quant.strategy,
group_size=weight_quant.group_size,
symmetric=weight_quant.symmetric,
input_quant=input_quant,
layer_name=layer_name,
quant_format=format,
)
if (
self._is_wNaM_int(weight_quant, input_quant, format)
and input_quant.num_bits == 4
):
return CompressedTensorsWNA4Int(
num_bits=weight_quant.num_bits,
strategy=weight_quant.strategy,
group_size=weight_quant.group_size,
symmetric=weight_quant.symmetric,
input_quant=input_quant,
layer_name=layer_name,
quant_format=format,
)
if self._is_wNa16_group_channel(weight_quant, input_quant) and (
format == CompressionFormat.pack_quantized.value
):
return CompressedTensorsWNA16(
num_bits=weight_quant.num_bits,
strategy=weight_quant.strategy,
symmetric=weight_quant.symmetric,
group_size=weight_quant.group_size,
layer_name=layer_name,
)
act_quant_format = is_activation_quantization_format(format)
if act_quant_format:
if self._is_fp8_w8a8(weight_quant, input_quant):
if current_platform.is_xpu():
# On XPU, --linear-backend xpu or torch opts into W8A8 FP8
# linear kernel; otherwise default to W8A16.
config = get_current_vllm_config_or_none()
is_fp8_w8a8_supported = config is not None and (
config.kernel_config.linear_backend in ("xpu", "torch")
)
weight_quant_is_block_strategy = (
weight_quant
and weight_quant.strategy == QuantizationStrategy.BLOCK
)
if weight_quant_is_block_strategy and not is_fp8_w8a8_supported:
# On XPU, block quantized weights always use the
# W8A8 kernel, due to lack of w8a16 support.
is_fp8_w8a8_supported = True
else:
is_fp8_w8a8_supported = self._check_scheme_supported(
CompressedTensorsW8A8Fp8.get_min_capability(), error=False
)
if is_fp8_w8a8_supported:
return CompressedTensorsW8A8Fp8(
weight_quant=weight_quant,
is_static_input_scheme=(
input_quant and not input_quant.dynamic
),
)
else:
# note: input_quant will be present for converted models;
# will be ignored during inference post loading
return CompressedTensorsW8A16Fp8(
weight_quant=weight_quant,
is_static_input_scheme=not input_quant.dynamic,
)
# note: input_quant can be None
if self._is_fp8_w8a16(weight_quant, input_quant):
is_static_input_scheme = input_quant and not input_quant.dynamic
return CompressedTensorsW8A16Fp8(
weight_quant=weight_quant,
is_static_input_scheme=is_static_input_scheme,
)
if self._is_static_tensor_w8a8(weight_quant, input_quant):
return CompressedTensorsW8A8Int8(
strategy=weight_quant.strategy,
is_static_input_scheme=True,
input_symmetric=input_quant.symmetric,
)
if self._is_dynamic_token_w8a8(weight_quant, input_quant):
return CompressedTensorsW8A8Int8(
strategy=weight_quant.strategy,
is_static_input_scheme=False,
input_symmetric=input_quant.symmetric,
)
if self._is_dynamic_token_w4a8_int(weight_quant, input_quant):
is_static_input_scheme = input_quant and not input_quant.dynamic
return CompressedTensorsW4A8Int(
num_bits=weight_quant.num_bits,
strategy=weight_quant.strategy,
group_size=weight_quant.group_size,
is_static_input_scheme=is_static_input_scheme,
input_symmetric=input_quant.symmetric,
)
raise NotImplementedError(
f"No compressed-tensors compatible scheme was found for {layer_name=}, "
f"{weight_quant=}, {input_quant=}, {output_quant=}, {format=}"
)
def get_scheme(
self, layer: torch.nn.Module, layer_name: str | None = None
) -> "CompressedTensorsScheme | None":
"""compressed-tensors supports non uniform in the following way:
targets of config_groups: There can be N config_groups which each
have a quantization scheme. Each config_group has a list of targets
which can be a full layer_name, a regex for a layer_name, or
an nn.Module name.
Detect whether a layer_name is found in any target and
use the quantization scheme corresponding to the matched target
to select the CompressedTensorsScheme used for inference.
"""
# Use the new get_quant_args method to extract QuantizationArgs
scheme_dict = self.get_scheme_dict(layer, layer_name)
weight_quant = None
input_quant = None
output_quant = None
format = None
if scheme_dict:
weight_quant = scheme_dict.get("weights")
input_quant = scheme_dict.get("input_activations")
output_quant = scheme_dict.get("output_activations")
format = scheme_dict.get("format")
if weight_quant is None:
# Falling back to UnquantizedLinearMethod
return None
else:
# Find the quant_scheme
scheme = self._get_scheme_from_parts( # type: ignore
weight_quant=weight_quant,
input_quant=input_quant,
output_quant=output_quant,
format=format,
layer_name=layer_name,
)
# Raise error if device does not support the scheme
# (e.g. fp8 needs ada lovelace)
self._check_scheme_supported(scheme.get_min_capability())
logger.debug("Using scheme: %s for %s", scheme.__class__.__name__, layer_name)
return scheme
def get_scheme_dict(
self, layer: torch.nn.Module, layer_name: str | None = None
) -> dict[str, QuantizationArgs | str | None] | None:
"""Extract the QuantizationArgs for a given layer.
Returns:
dict with {
"weights": QuantizationArgs,
"input_activations": QuantizationArgs | None,
"format": str | None
} | None
"""
# TODO (@kylesayrs): support ignore module names with ct matching utils
if should_ignore_layer(
layer_name, ignore=self.ignore, fused_mapping=self.packed_modules_mapping
):
return None
# Will be empty for models with only sparsity
if self.target_scheme_map:
matched_target = find_matched_target(
layer_name=layer_name,
module=layer,
targets=self.target_scheme_map.keys(),
fused_mapping=self.packed_modules_mapping,
)
if matched_target is not None:
scheme_dict = self.target_scheme_map[matched_target]
if scheme_dict.get("format") is None:
scheme_dict["format"] = self.quant_format
return scheme_dict
return None
def has_blocked_weights(self) -> bool:
for scheme in self.target_scheme_map.values():
weight_quant = scheme.get("weights")
if (
weight_quant is not None
and weight_quant.strategy == QuantizationStrategy.BLOCK
):
return True
return False