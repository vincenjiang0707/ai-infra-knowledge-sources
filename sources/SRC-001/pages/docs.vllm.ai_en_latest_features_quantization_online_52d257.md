source: https://docs.vllm.ai/en/latest/features/quantization/online/
lastmod: 2026-09-24

# Online Quantization[¶](https://docs.vllm.ai#online-quantization)

Online quantization lets you take a BF16/FP16 model and quantize its Linear and MoE weights to lower precision (such as FP8) at load time, without needing a pre-quantized checkpoint or calibration data. Weights are converted during model loading and activations are dynamically scaled during each forward pass.

## Quick Start[¶](https://docs.vllm.ai#quick-start)

Pass a scheme name to the `quantization`

parameter:

from vllm import LLM
# Per-tensor FP8 quantization (one scale per weight tensor)
llm = LLM("meta-llama/Llama-3.1-8B", quantization="fp8_per_tensor")
# Per-block FP8 quantization (128x128 block scaling for weights and 1x128 block scaling for activations)
llm = LLM("meta-llama/Llama-3.1-8B", quantization="fp8_per_block")
# MXFP8 quantization for weights and activations
llm = LLM("meta-llama/Llama-3.1-8B", quantization="mxfp8")
# MXFP4 weight; activation quantization depends on the `linear_backend` picked
llm = LLM("meta-llama/Llama-3.1-8B", quantization="mxfp4")
# MXFP4 MOE-only weight and activation quantization
llm = LLM(
"Qwen/Qwen3.5-35B-A3B",
quantization="mxfp4",
quantization_config={"linear": {"activation": None, "weight": None}}
)


Or with the CLI:

```bash
vllm serve meta-llama/Llama-3.1-8B --quantization fp8_per_tensor
vllm serve meta-llama/Llama-3.1-8B --quantization fp8_per_block
vllm serve meta-llama/Llama-3.1-8B --quantization mxfp8
vllm serve meta-llama/Llama-3.1-8B --quantization mxfp4
vllm serve Qwen/Qwen3.5-35B-A3B --quantization mxfp4 \
--quantization-config '{"linear":{"activation":null,"weight":null}}'
```


## Supported Schemes[¶](https://docs.vllm.ai#supported-schemes)

| Scheme | Weight recipe | Activation recipe | Notes |
|---|---|---|---|
`fp8_per_tensor` | fp8_e4m3 data, fp32 per-tensor scale | fp8_e4m3 data, fp32 per-tensor scale | On some GPUs (Ada, Hopper) linear activations use per-token scaling for better performance |
`fp8_per_block` | fp8_e4m3 data, fp32 per-128x128-block scale | fp8_e4m3 data, fp32 per-1x128-block scale | |
`mxfp8` | fp8_e4m3 data, e8m0 per-1x32-block scale | fp8_e4m3 data, e8m0 per-1x32-block scale | Requires SM 100+ (Blackwell or newer) for w8a8, other GPUs use a w8a16 fallback |
`mxfp4` | fp4_e2m1 data, e8m0 per-1x32-block scale (
|

- MOE: fp4_e2m1 data, e8m0 per-1x32-block scale.

`--linear-backend`

to pin one (e.g. `--linear-backend flashinfer`

).## Advanced Configuration[¶](https://docs.vllm.ai#advanced-configuration)

For fine-grained control, use a `quantization_config`

dictionary.

### Schema[¶](https://docs.vllm.ai#schema)

quantization_config:
linear:
weight: <name> # see QUANT_KEY_NAMES in vllm/config/quantization.py
activation: <name>
moe:
weight: <name>
activation: <name>
ignore: [<layer-name-or-regex-or-fnmatch-pattern>, ...]


`linear`

and `moe`

accept a full `{weight, activation}`

dict, or a bare string. A string resolves first against the `--quantization`

shorthands (taking the matching layer-kind slot), then against `QUANT_KEY_NAMES`

as a weight name. Unset fields fall back to the `--quantization`

shorthand's defaults, or for already-quantized checkpoints to whatever the checkpoint declares.

On XPU, non-block FP8 scaled-mm linear layers default to W8A16; setting `--linear-backend xpu`

forces W8A8. Use `--linear-backend xpu_woq`

to explicitly select weight-only quantization (W8A16). Setting `--linear-backend torch`

also forces W8A8 but runs the GEMM through `torch._scaled_mm`

instead of the custom XPU kernel.

The CLI accepts the same shape as JSON or as dotted keys:

vllm serve <model> --quantization-config '{"moe":{"activation":"mxfp8"}}'
vllm serve <model> --quantization-config.moe.activation mxfp8


### Activation overrides on already-quantized checkpoints[¶](https://docs.vllm.ai#activation-overrides-on-already-quantized-checkpoints)

For checkpoint-quantized models, `quantization_config`

lets you pick an activation format independently of the baked-in weights. The supported overrides are checkpoint-specific; today this is wired up for MXFP4 MoE checkpoints (gpt-oss) where you can opt into FP8 activations:

Combine with `--moe-backend`

to pin a specific kernel family.

### Online quantization on unquantized layers from partially-quantized checkpoints[¶](https://docs.vllm.ai#online-quantization-on-unquantized-layers-from-partially-quantized-checkpoints)

Online quantization can be used on already quantized checkpoints independently of their original `quant_method`

(`modelopt`

, `compressed-tensors`

, `quark`

, etc.), for layers that are left unquantized in the original checkpoint.

The checkpoint `quant_method`

remains responsible for its quantized layers, while the selected unquantized layers use the requested online method.

For example:

adds MXFP8 quantization to the dense linear layers of a Quark checkpoint where only MOE experts are quantized.

Info

`quantization_config.ignore`

is an online-only exclusion: the original `quant_method`

relies solely on its own ignore implementation and on the ignored layers specified in `config.json`

.

### Separate Schemes for Dense and MoE Layers[¶](https://docs.vllm.ai#separate-schemes-for-dense-and-moe-layers)

You can apply different quantization schemes to dense linear layers and MoE expert layers via the `linear`

and `moe`

fields. Each accepts either a full spec dict, or a bare string naming an online shorthand (e.g. `"fp8_per_block"`

) or weight format (e.g. `"fp8_per_block_static"`

); fields not set fall back to the shorthand defaults.

from vllm import LLM
# Linear: per-block FP8; MoE: per-tensor FP8 (inherited from the shorthand)
llm = LLM(
"ibm-granite/granite-3.0-1b-a400m-base",
quantization="fp8_per_tensor",
quantization_config={
"linear": "fp8_per_block",
},
)


Or,

from vllm import LLM
# Linear: per-tensor FP8 (inherited); MoE: per-block FP8
llm = LLM(
"ibm-granite/granite-3.0-1b-a400m-base",
quantization="fp8_per_tensor",
quantization_config={
"moe": "fp8_per_block",
},
)


### Excluding Layers from Quantization[¶](https://docs.vllm.ai#excluding-layers-from-quantization)

Use the `ignore`

parameter to skip specific layers. It accepts exact layer names, regex patterns (prefixed with `re:`

), and patterns understood by [ fnmatch.fnmatch](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch):

from vllm import LLM
llm = LLM(
"ibm-granite/granite-3.0-1b-a400m-base",
quantization="fp8_per_tensor",
quantization_config={
"ignore": [
# exact layer name
"model.layers.1.self_attn.o_proj",
# regex: skip all QKV projections
"re:.*[qkv]_proj",
# fnmatch: skip all MoE experts
"*mlp.experts*",
],
},
)


Note

For fused layers (e.g., `qkv_proj`

which fuses `q_proj`

, `k_proj`

, `v_proj`

), patterns may match the fused name directly or all of its unfused shard names.

### Fine-Grained Per-Layer Quantization Schemes[¶](https://docs.vllm.ai#fine-grained-per-layer-quantization-schemes)

Use the `targets`

parameter to apply different online shorthands to different layers, instead of one scheme applied everywhere via `linear`

/`moe`

. Keys are exact layer names, regex patterns (prefixed with `re:`

), or patterns understood by [ fnmatch.fnmatch](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch); values are shorthand names (

`fp8_per_tensor`

, `fp8_per_block`

, `fp8_per_channel`

, `mxfp8`

, `int8_per_channel_weight_only`

, `nvfp4_per_token`

).Example:

from vllm import LLM
llm = LLM(
"Qwen/Qwen3.5-35B-A3B",
quantization="online",
quantization_config={
"targets": {
# exact layer name
"model.layers.0.self_attn.o_proj": "fp8_per_tensor",
# regex: quantize all QKV projections
r"re:.*self_attn\.qkv_proj.*": "mxfp8",
# fnmatch: quantize all MoE experts
"*mlp.experts*": "mxfp4",
},
},
)


Or with the CLI:

vllm serve Qwen/Qwen3.5-35B-A3B \
--quantization online \
--quantization-config '{"targets":{"model.layers.0.self_attn.o_proj":"fp8_per_tensor","re:.*self_attn\\.qkv_proj.*":"mxfp8","*mlp.experts*":"mxfp4"}}'


Info

`targets`

is mutually exclusive with online`linear`

and`moe`

: set one or the other, not both.- A layer that matches no
`targets`

pattern is left unchanged from its checkpoint dtype. - A layer name may not match both
`targets`

and`ignore`

, raising an error. - A layer may not match more than one
`targets`

pattern, raising an error. - fnmatch-style patterns are supported only by online quantization; they are not applied to Quark or compressed-tensors configurations.