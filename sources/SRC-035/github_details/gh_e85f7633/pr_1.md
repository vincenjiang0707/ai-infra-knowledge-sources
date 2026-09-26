# [PR #1] [Feature] 新增 GLM-5.3-Flash (glm5_next) 免校准 W8A8 量化支持

source: https://github.com/Ascend/msmodelslim/pull/1
state: closed | updated: 2026-08-30T06:40:30Z
labels: ascend-cla/no

## 正文

# PR 提交说明

提交前请阅读 [贡献指南](https://gitcode.com/Ascend/msmodelslim/blob/master/docs/zh/contributing/contributing_guide.md)，开发者文档：[模型接入指南](../docs/zh/knowledge_base/model/integrating_models.md)

PR 标题前缀：[Feature]、[Bugfix]、[Doc]、[Test]（与 CONTRIBUTING 一致）

## 1. 影响面评估

**接口变更（按需）：**
- 新增 `GLM-5.3-Flash` 模型类型（pedigree `glm5_next`）的适配器注册，`msmodelslim quant --model_type GLM-5.3-Flash` 不再回退到 default 适配器。
- 新增转换 API：`msmodelslim.model.glm5_next.w8a8_dynamic.convert_to_w8a8_dynamic(model_path, save_path)`（以及适配器方法 `export_w8a8_dynamic`）。

> 备注：均为新增能力，不改动任何既有接口与既有模型的适配行为。

**输出件变更（按需）：**
- 新增 GLM-5.3-Flash 的量化产物导出能力：`quant_model_description.json`、`quant_model_weights-xxxxx.safetensors`（含 `quant_model_weights.safetensors.index.json`）与 tokenizer / config 文件，可被 vLLM-Ascend 等框架直接加载。对存量模型的产物无影响。

**非兼容变更（按需）：** 无

**SIG 评审结论（按需）：** 无

## 2. 修改描述

**修改背景（可选）：** GLM-5.3-Flash（`model_type=glm5_next`，transformers 5.16.0 起）与已适配的 GLM-5 / GLM-5.1（MLA + Indexer）、GLM-5.2（`glm_moe_dsa`）结构差异很大：

- 45 层混合架构 = 34 层 KDA 线性注意力 + 11 层 DeepSeek 稀疏注意力（含 Indexer `wq_b` / `wk` / `weights_proj`）；
- 每层引入 MHC（multi-hyper-connection）超连接模块 `hc_attn_*` / `hc_ffn_*`；
- 288 专家 MoE，`first_k_dense_replace=3` 层为稠密 FFN；
- 1 层 MTP 投机草稿层（checkpoint 中的 `model.language_model.layers.45`，带 `enorm` / `hnorm` / `eh_proj` / `shared_head`）。

当前 master 的 entry points 最高只到 GLM-5.1（`glm_5`）与 GLM-5.2（`glm_5_2`），`GLM-5.3-Flash` 会回退到 default 适配器，得到的量化范围是错误的。

**修改目的：** 为 GLM-5.3-Flash 提供**免校准 W8A8_DYNAMIC** 转换能力（per-channel 对称 INT8 权重 + per-token 动态激活），并把 `glm5_next` 注册进模型适配插件。带校准的量化管线不在本 PR 范围内（见下方「范围与 TODO」）。

**修改内容：**

- **infra/模型适配**：新增 `msmodelslim/model/glm5_next/`（`__init__.py`、`loader.py`、`model_adapter.py`、`w8a8_dynamic.py`），在 `config/config.ini` 注册 `glm5_next = GLM-5.3-Flash`、entry point 与依赖（`transformers>=5.16.0`，即 checkpoint 元数据声明的版本）。
- **量化范围（已验证）**：仅 FFN 侧投影 —— `mlp.experts.{gate,up,down}_proj`、`mlp.shared_experts.{gate,up,down}_proj`、`mlp.{gate,up,down}_proj`（稠密 FFN 层），MTP 草稿层除外。权重按输出通道做对称 INT8 min/max 量化（无校准数据、无前向），激活按 token 动态量化；每层权重导出 `weight_scale` / `weight_offset`（offset 为全零，保持与 ModelSlim 产物一致的布局），scale/offset 直接挂在层名下（不带中间 `.weight`）。
- **保留 BF16 的模块及原因**：
  - KDA 注意力投影（`q/k/v_proj`、`b_proj`、`f_a/g_a_proj`、`f_b/g_b_proj`、`o_proj`）与逐通道 `q/k/v_conv1d`：推理引擎会把 KDA 侧投影融合为单一 `in_proj_qkvbfg_a`，免校准条件下无法逐投影得到可靠的激活范围；原生 FP8 checkpoint 也通过 `modules_to_not_convert` 把这些模块留在 BF16。
  - 稀疏注意力投影（`q_a/q_b/kv_a/kv_b_proj`、`o_proj`）与 Indexer（`wq_b`、`wk`、`weights_proj`）：`wk` + `weights_proj` 消费的是 `input_layernorm` 输出，其 norm-linear 融合伙伴集合与所有已支持 pedigree 都不同。
  - MHC 超连接模块、MoE 路由、各层 Norm、embedding / `lm_head`、视觉塔、MTP 草稿层。
- **校准管线显式不支持**：适配器继承 `DefaultModelAdapter`，但在 `load_model` / `init_model` 中抛出 `UnsupportedError` 并给出可执行的替代路径（指向免校准转换 API），而不是继承一条会在错误量化范围上跑通的路径；`get_adapter_config_for_subgraph()` 返回空（无 norm-linear / ov 融合子图），且适配器不继承 anti-outlier / QuaRot / FA3 接口。
- **app/最佳实践量化**：新增 `lab_practice/glm5_next/glm5_next_w8a8.yaml`，用标准配置语言描述同一量化范围（仅 `linear_quant`，无 `quarot` / `flex_smooth_quant` 阶段）。
- **docs**：更新 `docs/zh/knowledge_base/model/README.md` 支持矩阵（GLM5-MOE 系列 +1 行）与 `example/GLM-5/README.md`（架构说明 + 免校准量化命令）。

## 3. 功能验证

- [x] 功能自验
- [x] 本地自验用例截图（请勿包含个人信息；可附复现命令）

**复现步骤（可选）：**

1. 单元测试（18 个用例，CPU，无需 NPU）：

```bash
pytest test/cases/model/glm5_next/ -q
# 18 passed
```

2. 免校准转换（GLM-5.3-Flash BF16 checkpoint，120 个 safetensors 分片）：

```python
from msmodelslim.model.glm5_next.w8a8_dynamic import convert_to_w8a8_dynamic

convert_to_w8a8_dynamic('/path/to/GLM-5.3-Flash-BF16', '/path/to/GLM-5.3-Flash-W8A8')
```

实测：36423 个 FFN 投影被量化（其余张量保持 FLOAT），产物 63 个分片 / 315 GB；`quant_model_description.json` 共 111618 个键。量化范围已与真实 checkpoint 的 `model.safetensors.index.json` 逐键比对（`should_quantize` 命中的张量集合与已验证产物完全一致）。

3. 端到端验证：Atlas A2（Atlas 800I A3 / 910B3 ×8）上用 vLLM-Ascend 加载上述产物做真实权重推理，输出正常。

### 范围与 TODO（请评审重点关注）

- **本 PR 不提供带校准的量化**：校准需要 KDA 线性注意力与 MHC 层的 `forward` 实现（transformers 5.16.0 才提供 `glm5_next`，而本仓库其他 GLM pedigree 钉在 5.4.0 / 5.12.0）。`lab_practice/glm5_next/glm5_next_w8a8.yaml` 是同一量化范围的标准配置表达，供后续校准支持参考，本次未通过 `msmodelslim quant` 一键量化跑通端到端。
- 产物 description 目前只保留 `group_size` 与 `metadata` 两个头部键（与在设备上验证过的产物一致）。官方 ascendv1_saver 产物额外携带 `model_quant_type` / `version` / `is_rot_used` / `optional`，如评审需要完全对齐可以再加（`w8a8_dynamic.py` 内已有 NOTE 说明）。
- 分片命名为 `quant_model_weights-00001.safetensors`，如需与 ascendv1_saver 的 `-00001-of-00063` 完全一致也可调整（消费方按 index 文件取权重，两种命名都能加载）。

## 4. 自检（请逐项确认，不适用标 N/A）

**典型安全编码问题**

- [x] 是否已校验外部数据（模型路径 / config.json / 张量形状与有效性均校验，异常统一走 `InvalidModelError`）
- [x] 是否未采集或打印敏感信息（日志只输出分片名、张量数与耗时统计）
- [x] 是否已正确设置文件权限（输出目录 `0750`，权重与 JSON 产物 `0600`，与 ascendv1_saver 一致）
- [x] 是否充分考虑浮点运算溢出、除零等异常场景（`amax` 先 `clamp(min=1e-8)` 再做除法；权重含 NaN/Inf 直接报错）
- [x] 是否已对正则表达式做 ReDos 检查（3 条模式均为线性、无嵌套量词/回溯）

**DT**

- [x] 是否具备 UT 测试用例看护（路径：`test/cases/model/glm5_next/test_loader_glm5_next.py`、`test/cases/model/glm5_next/test_w8a8_dynamic.py`；覆盖 scope 判定、量化/反量化一致性、MTP 与注意力层保留 BF16、产物索引与文件权限、异常分支）
- [ ] 是否需要添加冒烟：否（若「是」请说明冒烟场景及对应用途）：免校准转换属离线工具链，NPU 侧冒烟由 vLLM-Ascend 侧用例看护


## 评论 (2)

### ascend-robot · 2026-08-29

### CLA Signature Guide  

 @Liears , thanks for your pull request. 

The following commit(s) are not associated with a signed **<font color=green>_Contributor License Agreement (CLA)_</font>**.

| Commit | Reason |
|--|--|
| [9b326d42  \[Feature] 新增 GLM-5.3-Flash ...](https://github.com/Ascend/msmodelslim/commit/9b326d42d2d41140f11e02c4267edcc9d6550428) | the email used in the commit is not linked to a signed CLA! <br>please verify that it matches the email you used when signing the CLA. | 

To sign CLA, [**<ins>click here</ins>**](https://clasign.osinfra.cn/sign-cla/690ca9ddf91c03dee6082ab1/individual). 

To check if your email is configured correctly, refer to the [**<font color=red><ins>_FAQs_</ins></font>**](https://gitcode.com/Ascend/infrastructure/blob/master/docs/cla/cla%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md#faq). 

Once you've signed the CLA or updating your email, please comment **`/check-cla`** to revalidate CLA status.

### Liears · 2026-08-30

Closing this PR. Thank you for the review bandwidth — after checking upstream, GLM-5-Next (glm5_next) quantization support is already being developed for ModelSlim (see the in-flight glm5_next integration: QuaRot rotation + SmoothQuant + W8A8/W4A8/MXFP8 configs), which supersedes this standalone calibration-free conversion script. Keeping a single well-integrated implementation upstream is better than two competing ones. The local script remains available for our own use.
