source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/ocp_mx_utils/
lastmod: 2026-09-27

Normalize a Quark weight quant config to `(mx_dtype, scale_block_rows)`

.

Quark spells OCP MX weights two ways. The canonical one is 1-D per-group: `qscheme="per_group"`

, `group_size=32`

, `scale_format="e8m0"`

. MXFP8 checkpoints may instead use a 2-D per-block spelling (`qscheme="per_block"`

, `block_size=[R, 32]`

, `scale_type="float8_e8m0fnu"`

), which carries one scale per `R`

weight rows rather than one per row. `scale_block_rows`

is that `R`

; it is 1 for the canonical spelling, where the two layouts coincide.

Returns `None`

when the config is not an OCP MX weight quantization.

## Source code in `vllm/model_executor/layers/quantization/utils/ocp_mx_utils.py`


```python
| def ocp_mx_weight_dtype_and_rows(
weight_quant: dict[str, Any] | None,
) -> tuple[str, int] | None:
"""Normalize a Quark weight quant config to ``(mx_dtype, scale_block_rows)``.
Quark spells OCP MX weights two ways. The canonical one is 1-D per-group:
``qscheme="per_group"``, ``group_size=32``, ``scale_format="e8m0"``. MXFP8
checkpoints may instead use a 2-D per-block spelling
(``qscheme="per_block"``, ``block_size=[R, 32]``,
``scale_type="float8_e8m0fnu"``), which carries one scale per ``R`` weight
rows rather than one per row. ``scale_block_rows`` is that ``R``; it is 1
for the canonical spelling, where the two layouts coincide.
Returns ``None`` when the config is not an OCP MX weight quantization.
"""
if not isinstance(weight_quant, dict):
return None
dtype = weight_quant.get("dtype")
if not isinstance(dtype, str):
return None
mx_dtype = dtype.replace("fp", "mxfp")
if mx_dtype not in _WEIGHT_QUANT_KEY_MAP:
return None
qscheme = weight_quant.get("qscheme")
if qscheme == "per_group":
if weight_quant.get("group_size") != OCP_MX_BLOCK_SIZE:
return None
if weight_quant.get("scale_format") != "e8m0":
return None
return mx_dtype, 1
if qscheme == "per_block":
# Only the unpacked dtypes are accepted here: expanding a 2-D scale
# over a sub-byte packed weight has no checkpoint to validate against.
if mx_dtype not in OCP_MX_UNPACKED_DTYPES:
return None
block_size = list(weight_quant.get("block_size") or [])
if len(block_size) != 2 or block_size[1] != OCP_MX_BLOCK_SIZE:
return None
if weight_quant.get("scale_type") != "float8_e8m0fnu":
return None
if weight_quant.get("symmetric") is not True or weight_quant.get("is_dynamic"):
return None
return mx_dtype, block_size[0]
return None
|
```