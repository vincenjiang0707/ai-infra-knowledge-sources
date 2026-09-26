source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16)

Hybrid W4A16 kernel: Triton for prefill, HIP skinny for decode.

## Routes based on batch size M

M <= MAX_SKINNY_BATCH_SIZE: HIP skinny GEMM (wvSplitK_int4_g) M > MAX_SKINNY_BATCH_SIZE: Triton W4A16 fused dequant GEMM

Stores the weights ONCE as int8 [N, K//2] (ExLlama shuffle packed). Both paths read this single buffer: the HIP skinny kernel uses it directly, and the triton kernel reinterprets it as int32 [N, K//8] via a view (and transposes tiles in-register). No dual weight storage.

Classes:

-
–[RDNAHybridW4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.RDNAHybridW4A16LinearKernel)Hybrid W4A16 kernel: HIP skinny for decode, Triton for prefill.


Functions:

-
–[pack_int4_exllama_shuffle](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.pack_int4_exllama_shuffle)Pack uint4 values into ExLlama shuffle format: [N, K] -> [N, K//8] int32.

-
–[triton_w4a16_skinny_fmt_gemm](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm)Fused W4A16 GEMM reading from skinny weight format [N, K//8].


##

`RDNAHybridW4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.RDNAHybridW4A16LinearKernel)

Bases: `MPLinearKernel`


Hybrid W4A16 kernel: HIP skinny for decode, Triton for prefill.

Stores the weights once as int8 [N, K//2] (ExLlama shuffle packed). The HIP skinny kernel reads it directly; the triton kernel reinterprets the same buffer as int32 [N, K//8] via a view, so there is no dual weight storage.

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


|
|

##

`_rdna_hybrid_w4a16_apply_impl(x_2d, w_q, w_s, w_zp, bias, cu_count, group_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16._rdna_hybrid_w4a16_apply_impl)

Dispatch between skinny GEMM and Triton based on batch size M.

`w_zp`

is [N//8, K//G] int32 for asymmetric layers, None for symmetric.

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


##

`_triton_w4a16_skinny_fmt_kernel(a_ptr, b_ptr, scales_ptr, zp_ptr, c_ptr, M, N, K, K8, num_groups, group_size, ZP_BIAS, HAS_ZP, BLOCK_M, BLOCK_N, BLOCK_K)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16._triton_w4a16_skinny_fmt_kernel)

Fused W4A16 GEMM reading weights from skinny format [N, K//8].

B is stored as [N, K//8] int32 using ExLlama shuffle packing: each int32 packs 8 K-values with interleave [0,2,4,6,1,3,5,7]: packed = val[0] | (val[2]<<4) | (val[4]<<8) | (val[6]<<12) | (val[1]<<16) | (val[3]<<20) | (val[5]<<24) | (val[7]<<28)

Scales are [N, K//G] (skinny layout, NOT transposed). When HAS_ZP=True, zp_ptr holds [N//8, K//G] int32 with row n's raw zero-point at word[n//8] bits 4*(n%8), and dequant is (nibble - zp_raw) * scale. When HAS_ZP=False, only the constant ZP_BIAS is subtracted (symmetric).

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


|
|

##

`pack_int4_exllama_shuffle(w_uint4)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.pack_int4_exllama_shuffle)

Pack uint4 values into ExLlama shuffle format: [N, K] -> [N, K//8] int32.

Each int32 packs 8 K-values with interleave order [0,2,4,6,1,3,5,7].

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


##

`triton_w4a16_skinny_fmt_gemm(a, b_q, scales, group_size, zp_bias=8, zp=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm)

Fused W4A16 GEMM reading from skinny weight format [N, K//8].

Parameters:

-

(`a`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm(a))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Activation matrix [M, K], float16 or bfloat16.

-

(`b_q`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm(b_q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Packed weight matrix [N, K//8], int32 (ExLlama shuffle).

-

(`scales`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm(scales))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Per-group scales [N, K//G], same dtype as a.

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Quantization group size (resolved from -1 to K by caller).

-

(`zp_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm(zp_bias))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`8`

) –Constant zero bias (default 8 for unsigned int4).

-

(`zp`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.rdna_hybrid_w4a16.triton_w4a16_skinny_fmt_gemm(zp))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Raw per-group zero-points [N//8, K//G] int32, row n at word[n//8] bits 4*(n%8) (asymmetric). When provided, dequant is (nibble - zp_raw) * scale.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output matrix [M, N], same dtype as a.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/rdna_hybrid_w4a16.py`


|
|