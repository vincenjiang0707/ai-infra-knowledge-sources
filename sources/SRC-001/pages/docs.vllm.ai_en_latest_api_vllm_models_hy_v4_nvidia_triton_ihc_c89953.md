source: https://docs.vllm.ai/en/latest/api/vllm/models/hy_v4/nvidia/triton_ihc/
lastmod: 2026-09-23

#

`vllm.models.hy_v4.nvidia.triton_ihc`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc)

Triton iHC pre/post kernels for HY V4.

Adapted from the SGLang HY V4 implementation: https://github.com/sgl-project/sglang/pull/36805

Functions:

-
–[triton_ihc_post](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc.triton_ihc_post)Scatter a sub-block output back over the iHC residual channels.

-
–[triton_ihc_pre](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc.triton_ihc_pre)Reduce iHC channels and produce the post gates.

-
–[triton_ihc_supported](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc.triton_ihc_supported)Return whether the in-tree Triton path can run for this input.


##

`triton_ihc_post(x, residual, post)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc.triton_ihc_post)

Scatter a sub-block output back over the iHC residual channels.

## Source code in `vllm/models/hy_v4/nvidia/triton_ihc.py`


##

`triton_ihc_pre(x, weight, scale, base, magnitude, hc_eps, norm_eps)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc.triton_ihc_pre)

Reduce iHC channels and produce the post gates.

## Source code in `vllm/models/hy_v4/nvidia/triton_ihc.py`


|
|

##

`triton_ihc_supported(x)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.triton_ihc.triton_ihc_supported)

Return whether the in-tree Triton path can run for this input.