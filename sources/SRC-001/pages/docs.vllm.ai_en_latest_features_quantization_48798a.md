source: https://docs.vllm.ai/en/latest/features/quantization/
lastmod: 2026-09-24

# Quantization[¶](https://docs.vllm.ai#quantization)

Quantization trades off model precision for smaller memory footprint, allowing large models to be run on a wider range of devices.

Tip

To get started with quantization, see [LLM Compressor](https://docs.vllm.ai/llm_compressor/), a library for optimizing models for deployment with vLLM that supports FP8, INT8, INT4, and other quantization formats.

The following are the supported quantization formats for vLLM:

[AutoAWQ](https://docs.vllm.ai/auto_awq/)[BitsAndBytes](https://docs.vllm.ai/bnb/)[GPTQModel](https://docs.vllm.ai/gptqmodel/)[Intel Neural Compressor](https://docs.vllm.ai/inc/)[LLM Compressor](https://docs.vllm.ai/llm_compressor/)[NVIDIA Model Optimizer](https://docs.vllm.ai/modelopt/)[Online Quantization](https://docs.vllm.ai/online/)[AMD Quark](https://docs.vllm.ai/quark/)[Quantized KV Cache](https://docs.vllm.ai/quantized_kvcache/)[TorchAO](https://docs.vllm.ai/torchao/)[FP8 ViT Encoder Attention](https://docs.vllm.ai/fp8_vit_attn/)

## Selecting Linear Backends per Quantization[¶](https://docs.vllm.ai#selecting-linear-backends-per-quantization)

`--linear-backend`

selects one backend for all quantized linear layers. For mixed-precision models that use more than one linear quantization scheme, use `linear_backend_per_quant`

to override the backend for individual schemes:

vllm serve <model> \
--linear-backend cutlass \
--kernel-config '{"linear_backend_per_quant":{"nvfp4_w4a16":"humming"}}'


Here, NVFP4 W4A16 linear layers use Humming, while all other quantized linear layers use CUTLASS. Per-quantization overrides take precedence over `--linear-backend`

; schemes without an override continue to use the global setting, including automatic selection when it is `auto`

.

## Supported Hardware[¶](https://docs.vllm.ai#supported-hardware)

The table below shows the compatibility of various quantization implementations with different hardware platforms in vLLM:

| Implementation | Volta | Turing | Ampere | Ada | Hopper | AMD GPU | Intel GPU | x86 CPU | Arm CPU |
|---|---|---|---|---|---|---|---|---|---|
| AWQ | ❌ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ❌ | ✅︎ | ✅︎ | ❌ |
| GPTQ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ❌ | ✅︎ | ✅︎ | ❌ |
| Marlin (GPTQ/AWQ/FP8/FP4) | ❌ | ✅︎* | ✅︎ | ✅︎ | ✅︎ | ❌ | ❌ | ❌ | ❌ |
| llm-compressor INT8 (W8A8) | ❌ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ❌ | ❌ | ✅︎ | ✅︎ |
| llm-compressor INT8 (W4A8) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅︎ |
| llm-compressor FP8 (W8A8) | ❌ | ❌ | ❌ | ✅︎ | ✅︎ | ✅︎ | ❌ | ❌ | ❌ |
| bitsandbytes | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ❌ | ❌ | ❌ | ❌ |
| DeepSpeedFP | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ❌ | ❌ | ❌ | ❌ |
| GGUF | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ✅︎ | ❌ | ❌ | ❌ |

- Volta refers to SM 7.0, Turing to SM 7.5, Ampere to SM 8.0/8.6, Ada to SM 8.9, and Hopper to SM 9.0.
- ✅︎ indicates that the quantization method is supported on the specified hardware.
- ❌ indicates that the quantization method is not supported on the specified hardware.
- All Intel Gaudi quantization support has been migrated to
[vLLM-Gaudi](https://github.com/vllm-project/vllm-gaudi). - *Turing does not support Marlin MXFP4.

Note

For information on quantization support on Google TPU, please refer to the [TPU-Inference Recommended Models and Features](https://docs.vllm.ai/projects/tpu/en/latest/recommended_models_features/) documentation.

Note

This compatibility chart is subject to change as vLLM continues to evolve and expand its support for different hardware platforms and quantization methods.

For the most up-to-date information on hardware support and quantization methods, please refer to [ vllm/model_executor/layers/quantization](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/quantization) or consult with the vLLM development team.

## Out-of-Tree Quantization Plugins[¶](https://docs.vllm.ai#out-of-tree-quantization-plugins)

vLLM supports registering custom, out-of-tree quantization methods using the `@register_quantization_config`

decorator. This allows you to implement and use your own quantization schemes without modifying the vLLM codebase.

### Registering a Custom Quantization Method[¶](https://docs.vllm.ai#registering-a-custom-quantization-method)

To register a custom quantization method, create a class that inherits from [ QuantizationConfig](https://docs.vllm.ai/api/vllm/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig) and decorate it with

`@register_quantization_config`

. The `get_quant_method`

dispatches to the appropriate quantize method based on the layer type:import torch
from vllm.model_executor.layers.quantization import (
register_quantization_config,
)
from vllm.model_executor.layers.quantization.base_config import (
QuantizationConfig,
QuantizeMethodBase,
)
from vllm.model_executor.layers.linear import LinearBase
from vllm.model_executor.layers.fused_moe import FusedMoE
@register_quantization_config("my_quant")
class MyQuantConfig(QuantizationConfig):
"""Custom quantization config."""
def get_name(self) -> str:
return "my_quant"
def get_supported_act_dtypes(self) -> list:
return [torch.float16, torch.bfloat16]
@classmethod
def get_min_capability(cls) -> int:
# Minimum GPU compute capability, -1 for no restriction
return -1
@staticmethod
def get_config_filenames() -> list[str]:
# Config files to search for in model directory
return []
@classmethod
def from_config(cls, config: dict) -> "MyQuantConfig":
# Create config from model's quantization config
return cls()
def get_quant_method(
self, layer: torch.nn.Module, prefix: str
) -> QuantizeMethodBase | None:
# Dispatch based on layer type
# NOTE: you only need to implement methods you care about
if isinstance(layer, LinearBase):
return MyQuantLinearMethod()
elif isinstance(layer, FusedMoE):
return MyQuantMoEMethod(layer.moe_config)
return None


### Required QuantizationConfig Methods[¶](https://docs.vllm.ai#required-quantizationconfig-methods)

Your custom [ QuantizationConfig](https://docs.vllm.ai/api/vllm/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig) subclass must implement these abstract methods:

| Method | Description |
|---|---|
`get_name()` | Returns the name of the quantization method |
`get_supported_act_dtypes()` | Returns list of supported activation dtypes (e.g., `torch.float16` ) |
`get_min_capability()` | Returns minimum GPU compute capability (e.g., 80 for Ampere, -1 for no restriction) |
`get_config_filenames()` | Returns list of config filenames to search for in model directory |
`from_config(config)` | Class method to create config from model's quantization config dict |
`get_quant_method(layer, prefix)` | Returns the quantization method for a given layer, or `None` to skip |

### Implementing a Quantized Linear Method[¶](https://docs.vllm.ai#implementing-a-quantized-linear-method)

For linear layers, return a [ QuantizeMethodBase](https://docs.vllm.ai/api/vllm/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizeMethodBase) subclass from

`get_quant_method`

. You can extend [as a starting point:](https://docs.vllm.ai/api/vllm/model_executor/layers/linear/#vllm.model_executor.layers.linear.UnquantizedLinearMethod)

`UnquantizedLinearMethod`

from vllm.model_executor.layers.linear import UnquantizedLinearMethod
class MyQuantLinearMethod(UnquantizedLinearMethod):
"""Custom quantization method for linear layers."""
def create_weights(
self, layer: torch.nn.Module, *weight_args, **extra_weight_attrs
):
# Create quantized weights for the layer
...
def apply(
self,
layer: torch.nn.Module,
x: torch.Tensor,
bias: torch.Tensor | None = None,
) -> torch.Tensor:
# Apply custom quantization logic here
...


### Implementing a Quantized MoE Method[¶](https://docs.vllm.ai#implementing-a-quantized-moe-method)

For Mixture of Experts (MoE) models, return a `FusedMoEMethodBase`

subclass from `get_quant_method`

. You can use [ UnquantizedFusedMoEMethod](https://docs.vllm.ai/api/vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method/#vllm.model_executor.layers.fused_moe.unquantized_fused_moe_method.UnquantizedFusedMoEMethod) to skip MoE quantization:

from vllm.model_executor.layers.fused_moe.layer import UnquantizedFusedMoEMethod
from vllm.model_executor.layers.fused_moe.fused_moe_method_base import (
FusedMoEMethodBase,
)
from vllm.model_executor.layers.fused_moe.config import FusedMoEQuantConfig
class MyQuantMoEMethod(FusedMoEMethodBase):
"""Custom quantization method for MoE layers."""
def create_weights(
self,
layer: torch.nn.Module,
num_experts: int,
hidden_size: int,
intermediate_size_per_partition: int,
params_dtype: torch.dtype,
**extra_weight_attrs,
):
# Create quantized weights for the MoE layer
...
def apply(
self,
layer: torch.nn.Module,
router: "FusedMoERouter",
x: torch.Tensor,
router_logits: torch.Tensor,
) -> torch.Tensor:
# Apply MoE computation with quantized weights
...
def get_fused_moe_quant_config(
self, layer: torch.nn.Module
) -> FusedMoEQuantConfig | None:
# Return the MoE quantization configuration
...


See existing implementations like [ Fp8MoEMethod](https://docs.vllm.ai/api/vllm/model_executor/layers/quantization/fp8/#vllm.model_executor.layers.quantization.fp8.Fp8MoEMethod) in

`vllm/model_executor/layers/quantization/fp8.py`

for reference.### Using the Plugin[¶](https://docs.vllm.ai#using-the-plugin)

Once registered, you can use your custom quantization method with vLLM:

# Register your quantization method (import the module containing your config)
import my_quant_plugin
from vllm import LLM
# Use the custom quantization method
llm = LLM(model="your-model", quantization="my_quant")


For more information on the plugin system, see the [Plugin System documentation](https://docs.vllm.ai/design/plugin_system/).