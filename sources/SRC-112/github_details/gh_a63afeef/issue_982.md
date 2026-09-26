# [Issue #982] starter task: MVP port mi355 deepseek disagg recipe to mi300 / 入门任务：将 MI355 DeepSeek 分离式配方移植到 MI300

source: https://github.com/SemiAnalysisAI/InferenceX/issues/982
state: open | updated: 2026-07-04T05:11:13Z
labels: p0, AMD

## 正文

 after porting mi355 to mi325, port to mi300
1. https://github.com/SemiAnalysisAI/InferenceX/blob/41147ad860b2d04b3fad8553d02d88a7b7e89c46/.github/configs/amd-master.yaml#L506-L556 (mi355 disagg fp8 deepseek for non-mtp & mtp) port over to mi325 (CDNA3)
2. https://github.com/SemiAnalysisAI/InferenceX/blob/main/benchmarks/multi_node/dsr1_fp8_mi355x_sglang-disagg.sh (that then calls generate sweep py which calls this launcher script) . This uses (`image: rocm/sgl-dev:sglang-0.5.9-rocm720-mi35x-mori-0227-2` but @JordanNanos u probably need to find the mi30x evquilaent of this. check the upstream nightly images have MoRI included https://hub.docker.com/r/lmsysorg/sglang-daily/tags, if not build using this. https://github.com/akao-amd/sglang/blob/main/docker/rocm.Dockerfile . ensure that u build it with the correct NIC)
3. which calls the files in here https://github.com/SemiAnalysisAI/InferenceX/tree/main/benchmarks/multi_node/amd_utils (which is based on bill's repo, it might be easier as first attempt to use bill's repo to locally run it https://github.com/billishyahao/sglang_disagg without the abstractions of runners/generate config .py/etc)

probably start doing 1k/1k on 1P1D first since it is an faster debugging loop, and then after u got that working with /sweep, add the rest of the configs to ur PR

## 中文说明
在完成 MI325 移植后，将 MI355 DeepSeek 分离式推理配方移植到 MI300 (CDNA3)。包括：(1) 将 `amd-master.yaml` 中的 MI355 分离式 FP8 DeepSeek 配置（非 MTP 和 MTP）移植到 MI300；(2) 适配多节点启动脚本，找到 MI300 对应的 SGLang ROCm 镜像（需包含 MoRI，若上游 nightly 无此镜像则需自行构建，并确保使用正确的 NIC）；(3) 复用 `benchmarks/multi_node/amd_utils` 中的工具。建议先从 1k/1k 的 1P1D 开始调试。


## 评论 (1)

### JiwaniZakir · 2026-04-18

The core risk here is MoRI support in the MI300X-compatible images — the MI355X recipe pins `rocm/sgl-dev:sglang-0.5.9-rocm720-mi35x-mori-0227-2`, which was a custom build, and the upstream SGLang nightly images on Docker Hub (`lmsysorg/sglang-daily`) may not have MoRI compiled in for `mi30x` targets. Before anything else, inspect those nightly tags for `mi300x` or `mi30x` variants and verify MoRI is present (`python -c "import sglang; print(sglang.__version__)"` won't catch this — you'd need to check for the MoRI-specific collective ops or confirm via the build flags in the Dockerfile). If MoRI is absent, the disaggregated decode bootstrap will silently fall back or fail at the KV transfer step, which is notoriously hard to distinguish from a generic NCCL/RCCL timeout. Starting with Bill's repo (`billishyahao/sglang_disagg`) at 1P1D 1k/1k is the right call since it removes the `generate_sweep.py` abstraction layer and makes it easier to isolate whether failures are in the launcher config or the underlying MoRI/RCCL stack.
