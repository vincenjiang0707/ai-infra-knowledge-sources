source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/utils/
lastmod: 2026-09-24

#

`vllm.kernels.helion.utils`

[¶](https://docs.vllm.ai#vllm.kernels.helion.utils)

Utility functions for Helion kernel management.

Functions:

-
–[canonicalize_gpu_name](https://docs.vllm.ai#vllm.kernels.helion.utils.canonicalize_gpu_name)Canonicalize GPU name for use as a platform identifier.


##

`canonicalize_gpu_name(name)`

[¶](https://docs.vllm.ai#vllm.kernels.helion.utils.canonicalize_gpu_name)

Canonicalize GPU name for use as a platform identifier.

Converts to lowercase, replaces separators with underscores, and maps known variant names to their canonical form via _GPU_NAME_ALIASES. e.g., "NVIDIA H100 80GB HBM3" -> "nvidia_h100" "NVIDIA A100-SXM4-80GB" -> "nvidia_a100" "AMD Instinct MI300X" -> "amd_instinct_mi300x"