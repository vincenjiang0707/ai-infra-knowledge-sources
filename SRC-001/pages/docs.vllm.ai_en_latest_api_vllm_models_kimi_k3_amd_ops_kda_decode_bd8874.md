source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/ops/kda_decode/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.amd.ops.kda_decode`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode)

ROCm entry points for the fused Kimi-K3 KDA decode kernel.

The kernel in `csrc/libtorch_stable/kimi_k3/fused_kda_decode_kernel_rocm.cu`

replaces, for a pure non-speculative decode batch, the three Triton launches and two copies the AMD KDA layer otherwise runs per layer: the packed causal conv1d update, the recurrent delta-rule step, and the gated output RMSNorm.

The kernel wants a width-major conv weight and an fp32 norm weight, so both are staged once at load time by the weight loaders below.

Functions:

-
–[is_fused_kda_decode_supported](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode.is_fused_kda_decode_supported)Whether the fused decode kernel can serve this layer on this device.

-
–[make_decode_conv1d_weight_loader](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode.make_decode_conv1d_weight_loader)Load the packed conv1d weight, mirroring a width-major fp32 copy.

-
–[make_decode_norm_weight_loader](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode.make_decode_norm_weight_loader)Load the gated-norm weight, mirroring an fp32 copy for the kernel.


##

`is_fused_kda_decode_supported(num_heads, head_dim, conv_width, num_spec, input_dtype, conv_state_dtype)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode.is_fused_kda_decode_supported)

Whether the fused decode kernel can serve this layer on this device.

## Source code in `vllm/models/kimi_k3/amd/ops/kda_decode.py`


##

`make_decode_conv1d_weight_loader(dims, tp_size, tp_rank, decode_conv1d_weight)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode.make_decode_conv1d_weight_loader)

Load the packed conv1d weight, mirroring a width-major fp32 copy.

The fused kernel indexes the weight as `[qkv, width, channel]`

so the channel dimension is the contiguous one; the Triton prefill and fallback decode kernels keep the `[channel, width]`

layout.

## Source code in `vllm/models/kimi_k3/amd/ops/kda_decode.py`


##

`make_decode_norm_weight_loader(decode_norm_weight)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_decode.make_decode_norm_weight_loader)

Load the gated-norm weight, mirroring an fp32 copy for the kernel.