source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/marlin_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.quantization.utils.marlin_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils)

Functions:

-
–[check_moe_marlin_supports_config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.check_moe_marlin_supports_config)Whether the fused MoE Marlin kernel supports

`config`

. -
–[get_marlin_workspace](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.get_marlin_workspace)Get zero-initialized locks for the current stream, ubatch, and lane.

-
–[marlin_moe_intermediate_size](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_moe_intermediate_size)Given Marlin packed weight matrices w1_packed, and w2_packed,

-
–[marlin_moe_padded_intermediate](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_moe_padded_intermediate)Smallest MoE intermediate size satisfying the Marlin MoE thread tiles.

-
–[marlin_pad_dim](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_pad_dim)Zero-pad the last dim from size to padded (activations K, bias N).

-
–[marlin_pad_qweight](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_pad_qweight)Zero-pad a GPTQ-layout packed weight (size_k / pack, size_n) for

-
–[marlin_pad_scales](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_pad_scales)Zero-pad weight scales (num_groups, size_n); call before

-
–[marlin_padded_nk](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_padded_nk)Minimal (padded_n, padded_k) satisfying a Marlin thread-tile family.

-
–[marlin_repacked_nk](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_repacked_nk)Recover the (size_n, size_k) a Marlin weight was repacked with

-
–[marlin_unpad_output](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_unpad_output)Strip padded output columns back to the logical N.

-
–[moe_packed_to_marlin_zero_points](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.moe_packed_to_marlin_zero_points)Convert compressed-tensors packed zero points to Marlin format.


##

`check_moe_marlin_supports_config(config, group_size, allow_tile_padding=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.check_moe_marlin_supports_config)

Whether the fused MoE Marlin kernel supports `config`

.

With `allow_tile_padding=True`

, a tile-misaligned intermediate size is zero-padded to a valid thread tile at weight prep (see marlin_moe_padded_intermediate), so only a group straddling the padded boundary stays unsupported. hidden_size is the MoE I/O extent and is never padded.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`get_marlin_workspace(device)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.get_marlin_workspace)

Get zero-initialized locks for the current stream, ubatch, and lane.

Marlin resets its locks after each call, so ordered calls can reuse them.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_moe_intermediate_size(w1_packed, w2_packed)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_moe_intermediate_size)

Given Marlin packed weight matrices w1_packed, and w2_packed, return the MoE intermediate size N

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_moe_padded_intermediate(intermediate_size, group_size=-1)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_moe_padded_intermediate)

Smallest MoE intermediate size satisfying the Marlin MoE thread tiles.

The kernel needs gate-up `2 * intermediate % 128 == 0`

and down `intermediate % 64 == 0`

, i.e. `intermediate % 64 == 0`

. A misaligned size is zero-padded to the next valid tile at weight prep, kept a multiple of `group_size`

so the group count stays integral. The padded region never reaches the MoE output: w13's padded output channels are zeroed by the zero-padded scales, so the padded inputs to w2 are zero.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_pad_dim(x, size, padded)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_pad_dim)

Zero-pad the last dim from size to padded (activations K, bias N).

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_pad_qweight(qweight, size_n, size_k, padded_n, padded_k)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_pad_qweight)

Zero-pad a GPTQ-layout packed weight (size_k / pack, size_n) for gptq_marlin_repack.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_pad_scales(scales, size_n, size_k, padded_n, padded_k, group_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_pad_scales)

Zero-pad weight scales (num_groups, size_n); call before marlin_permute_scales and pass the padded extents to it.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_padded_nk(size_n, size_k, group_size=-1)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_padded_nk)

Minimal (padded_n, padded_k) satisfying a Marlin thread-tile family.

Marlin GEMM and repack require (n % 64, k % 128) or (n % 128, k % 64); shapes satisfying neither are zero-padded up to the cheaper family. K stays divisible by group_size so padded scales keep an integral group count. Padded weight regions contribute nothing to the GEMM output: quantized value 0 decodes to 0.0 (FP4/FP8) or is cancelled by the zero-padded scales/zero-points (INT).

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_repacked_nk(qweight, num_bits)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_repacked_nk)

Recover the (size_n, size_k) a Marlin weight was repacked with (including any tile padding) from its packed shape.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`marlin_unpad_output(output, size_n, padded_n)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.marlin_unpad_output)

Strip padded output columns back to the logical N.

TODO: marlin_gemm could instead write the un-padded columns directly into a caller-provided `c`

buffer so this slice copy disappears.

## Source code in `vllm/model_executor/layers/quantization/utils/marlin_utils.py`


##

`moe_packed_to_marlin_zero_points(q_zp_packed, size_k, size_n, num_bits, is_a_8bit=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.marlin_utils.moe_packed_to_marlin_zero_points)

Convert compressed-tensors packed zero points to Marlin format.

Unlike AWQ, compressed-tensors uses standard bit packing without interleaving, so we just unpack and apply Marlin permutation directly.