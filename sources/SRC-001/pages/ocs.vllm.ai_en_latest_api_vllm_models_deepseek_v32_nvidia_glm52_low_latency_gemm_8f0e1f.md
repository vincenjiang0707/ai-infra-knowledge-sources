source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v32/nvidia/glm52_low_latency_gemm/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v32.nvidia.glm52_low_latency_gemm`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.nvidia.glm52_low_latency_gemm)

GLM-5.2 decode GEMM selection for unquantized BF16 on SM103.

Functions:

-
–[build_glm52_plan](https://docs.vllm.ai#vllm.models.deepseek_v32.nvidia.glm52_low_latency_gemm.build_glm52_plan)Plan for a weight the walk below cannot reach (a plain

`nn.Linear`

).

##

`build_glm52_plan(weight, dtype)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v32.nvidia.glm52_low_latency_gemm.build_glm52_plan)

Plan for a weight the walk below cannot reach (a plain `nn.Linear`

).