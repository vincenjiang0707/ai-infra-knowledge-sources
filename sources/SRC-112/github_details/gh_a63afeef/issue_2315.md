# [Issue #2315] Proposal: add Unofficial DeepSeek-V4-Flash 4xH200 SGLang recipe / 提案：新增非官方 DeepSeek-V4-Flash 4×H200 SGLang 配方

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2315
state: open | updated: 2026-07-25T00:47:25Z
labels: 

## 正文

## Proposal

Add a distinct `DeepSeek-V4-Flash` single-node recipe based on the public SGLang Hopper recommendation: stock MXFP4 checkpoint, 4×H200, TP4, Marlin, and EAGLE with 3 steps / top-k 1 / 4 draft tokens. This must remain **Unofficial** until accepted and rerun through the repository's authorized infrastructure.

Prepared fork branch: https://github.com/kfastino/InferenceX/tree/add-deepseek-v4-flash-h200-sglang
Commit: `f7e751b5`
Upstream base: `2ac531d95d213c4f1990850f256e8c2e67d22d48`

## Exact InferenceX method

The branch uses the existing upstream harness without changing metric semantics:

- 8,192 ISL / 1,024 OSL
- deterministic random tokens, seed 0, ratio 1.0
- DeepSeek-V4 chat encoding (`--dsv4`)
- ignore EOS, infinite request rate
- `2 × concurrency` warmups and `10 × concurrency` measured requests
- concurrency 1, 2, 4, 8, 16, 32, 64, 128
- stock checkpoint revision `60d8d70770c6776ff598c94bb586a859a38244f1`
- SGLang `v0.5.15.post1`, amd64 digest `sha256:289cf51da1e5fd6f8eb3231f0202d46800c2e241ecf28f68a5a51507ed928e31`

Local config generation produced the complete matrix, `bash -n` passed, and all 224 matrix tests passed.

## Why this is an issue, not a result PR

Two bounded 4×H200 Modal attempts allocated the requested hardware and loaded all 46 pinned checkpoint shards. Runtime resolution confirmed TP4, Marlin MXFP4, DSV4 attention, FP8 KV cache, EAGLE 3/1/4, and a 256-request cap. However, neither attempt exposed `/v1/models`; the exact upstream client remained in warmup, so **no benchmark measurements or curves are claimed**.

The contribution rules require a green full sweep including evals, company CODEOWNER sign-off, linked upstream recipe evidence, and maintainer `/reuse-sweep-run`. Those private/authorized runner and sign-off requirements are unavailable to an external fork. Please advise whether maintainers can run the prepared configuration on the H200 runner pool, or whether a different public contribution path is preferred.

Public recipe evidence:
- https://lmsysorg.mintlify.app/cookbook/autoregressive/DeepSeek/DeepSeek-V4#hopper-h100-h200-note
- https://github.com/fastino-ai/Pioneer/pull/5521

## 中文说明

建议新增独立的 `DeepSeek-V4-Flash` 单节点配方，依据公开的 SGLang Hopper 推荐配置：原始 MXFP4 检查点、4×H200、TP4、Marlin，以及 EAGLE 3 步 / top-k 1 / 4 个草稿 token。在上游接收并通过授权基础设施重新运行之前，该配置和任何派生结果必须保持 **Unofficial**。

已准备的派生仓库分支与提交见上方。该分支直接复用现有上游基准测试工具，不修改指标语义；工作负载为 8,192 ISL / 1,024 OSL、随机 token、seed 0、DeepSeek-V4 对话编码、ignore EOS，并扫描并发 1–128。配置生成、Shell 语法检查及 224 项矩阵测试均已通过。

我们在 Modal 上进行了两次有界的 4×H200 尝试，均成功分配硬件并加载全部 46 个固定版本检查点分片。运行时已确认 TP4、Marlin MXFP4、DSV4 attention、FP8 KV cache、EAGLE 3/1/4 以及 256 个运行请求上限。但两次均未开放 `/v1/models`，上游客户端停留在预热阶段，因此**不声明任何基准测试数值或性能曲线**。

仓库合并要求包含完整绿色扫描与评估、公司 CODEOWNER 签署、上游配方证据，以及维护者执行 `/reuse-sweep-run`。外部派生仓库无法满足这些私有/授权运行器与签署条件。请维护者确认是否可在 H200 运行器池上执行已准备的配置，或建议其他公开贡献流程。


## 评论 (2)

### kfastino · 2026-07-23

## Recovery update: valid Unofficial lower sweep points

The API-readiness diagnosis is now concrete: the two earlier attempts were terminated before the normal startup lifecycle completed; they were not model-load failures. Reusing the unchanged known-good Modal app from Pioneer commit `8a1f0116a` recovered the endpoint.

Phase timings on the recovered 4×H200 container (PDT, 2026-07-23):
- 11:53:09 launch handoff (`subprocess.Popen`), pinned SGLang image/checkpoint/TP4/Marlin/EAGLE 3/1/4
- 11:55:11 target load began; 46/46 shards complete at 11:55:43
- 11:56:41–12:03:59 target MHC prewarm (430.6–437.5 s by rank)
- 12:04:12–12:04:13 target model load complete (541.1–541.5 s)
- 12:04:16–12:04:49 EAGLE `DeepseekV4ForCausalLMNextN` load complete (31.3–32.8 s)
- 12:04:50 target verify CUDA-graph capture began; DeepGEMM JIT session began 12:05:45
- `/v1/models` returned 200 at 12:19:34

Thus the apparent stall was bounded MHC + uncached DeepGEMM/JIT and CUDA-graph capture. The existing HF volume was mounted correctly but persists model files only; no persistent DeepGEMM cache mount exists in the known-good app, so startup recompiles.

Using the exact upstream client semantics (8,192/1,024, ratio 1.0, seed 0, DSV4 chat framing, ignore EOS, infinite request rate, 2× concurrency warmups, 10× measured requests), three valid lower points completed with zero failed requests and exact 8,192 input / 1,024 output tokens:

| Concurrency | Requests | Output tok/s | Mean TTFT | P99 TTFT | Mean TPOT | P99 TPOT |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 153.21 | 0.879 s | 0.918 s | 5.67 ms | 8.73 ms |
| 4 | 40 | 160.24 | 18.924 s | 26.085 s | 5.66 ms | 8.24 ms |
| 8 | 80 | 177.28 | 39.066 s | 45.634 s | 5.15 ms | 7.40 ms |

The local cost-bounded run was stopped before concurrency 16 finished because TTFT had already exceeded 39 s at concurrency 8 and each point uses 10× concurrency requests. These measurements remain **Unofficial**. The full green sweep/evals and authorized `/reuse-sweep-run` are still required before a result PR; proposal #2315 remains the appropriate upstream path for now.

## 中文更新

已确认此前并非模型加载失败，而是进程在正常的 MHC 编译、EAGLE 草稿模型加载以及 DeepGEMM/CUDA Graph 阶段完成前被终止。复用 Pioneer 提交 `8a1f0116a` 中完全相同的 Modal 应用后，接口于 12:19:34 PDT 正常返回 200。

严格按照上游 8K/1K、seed 0、DeepSeek-V4 对话格式、ignore EOS、2× 并发预热及 10× 并发测量请求的方法，已完成并发 1、4、8 三个有效点；所有请求成功，输入/输出 token 均精确为 8192/1024。结果见上表，仍标记为 **Unofficial**。由于并发 8 的平均 TTFT 已超过 39 秒，为控制 H200 成本，本次未完成并发 16–128；完整绿色扫描、评估与维护者授权运行仍是结果 PR 的前提。


### kfastino · 2026-07-25

Opened #2329 with the prepared branch, rebased onto current `main`.

Two asks before anyone spends real review time on it:

1. **Scope confirmation** — is `DeepSeek-V4-Flash` in scope at all? #1135 was closed in favour of Pro. If Flash is still unwanted, say so and I will close both #2329 and this issue.
2. **Runner + CODEOWNER sponsorship** — the PR cannot progress without a green upstream H200 full sweep with evals, and an NVIDIA CODEOWNER (`configs/nvidia-master.yaml`) willing to review and post the checklist sign-off. I have no access to the H200 pool, and I deliberately did not apply a sweep label since a full fan-out is expensive shared GPU time. Please apply `full-sweep-fail-fast` only if you want it to run.

The PR claims **no benchmark numbers**. Our local c1/c4/c8 Modal figures are diagnostic and Unofficial — hand-run off authorized infrastructure — and are **not** committed, since `results/` is not a tracked directory in this repository. Happy to attach them here if useful.

One correction versus the description above: the stock checkpoint declares `quant_method: fp8`, and every H200 DeepSeek-V4 entry in `nvidia-master.yaml` already labels this same stock-checkpoint + Marlin path as `fp8`, so the PR uses `dsv4flash-fp8-h200-sglang-mtp` rather than `-fp4-`. The SGLang cookbook calls the same Hopper path "original FP4", so the two taxonomies disagree — maintainer preference decides, and the key, `precision`, and script filename have to move together.

中文：已基于当前 `main` 变基后提交 #2329。

在投入实质评审前，有两点请确认：

1. **收录范围确认** —— `DeepSeek-V4-Flash` 是否在收录范围内？此前 #1135 已被关闭并转向 Pro。若 Flash 仍不在范围内，请告知，我会同时关闭 #2329 与本 issue。
2. **运行器与 CODEOWNER 支持** —— 该 PR 必须具备包含评估在内的、全绿的上游 H200 完整扫描，以及一位愿意评审并发布检查清单签署的 NVIDIA CODEOWNER（`configs/nvidia-master.yaml`），否则无法推进。我无法访问 H200 资源池；考虑到完整扫描会占用大量共享 GPU 资源，我特意没有添加 sweep 标签。如需运行，请自行添加 `full-sweep-fail-fast`。

该 PR **不声明任何基准测试数值**。我们本地的 c1/c4/c8 Modal 数据仅供诊断且为非官方结果（在非授权基础设施上人工运行），并**未**提交入库——因为 `results/` 在本仓库中并非受版本控制的目录。如有需要，我可以附在此处。

对上文描述的一处更正：原始检查点的 `quant_method` 声明为 `fp8`，且 `nvidia-master.yaml` 中所有 H200 的 DeepSeek-V4 条目都已将"原始检查点 + Marlin"这一路径标注为 `fp8`，因此 PR 采用 `dsv4flash-fp8-h200-sglang-mtp` 而非 `-fp4-`。SGLang cookbook 则将同一条 Hopper 路径称为 "original FP4"，两套命名口径不一致，最终以维护者的偏好为准；需要注意配置键、`precision` 与脚本文件名必须同步修改。
