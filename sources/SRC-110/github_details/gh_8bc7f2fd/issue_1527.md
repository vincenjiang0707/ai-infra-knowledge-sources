# [Issue #1527] [Bug] HunyuanOCR 在 OCRBench 上得分与官方结果差异较大，OmniDocBench 评测出现大量 Timeout

source: https://github.com/modelscope/evalscope/issues/1527
state: closed | updated: 2026-08-04T09:49:14Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [ ] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

使用 EvalScope 对 `tencent/HunyuanOCR` 进行 OCRBench 和 OmniDocBench 评测时，发现评测结果与 HunyuanOCR 官方公布的数据存在较大差异：

| Benchmark | EvalScope 结果 | HunyuanOCR 官方结果 |
|---|---:|---:|
| OCRBench | 59 | 860/1000（即 86.0%） |
| OmniDocBench | 大量样本 Timeout，无法获得有效完整结果 | 94.10 |

HunyuanOCR 官方评测结果：

https://github.com/Tencent-Hunyuan/HunyuanOCR/blob/main/HunyuanOCR_v1.0/README_v1.0.md#evaluation

官方 README 提到 HunyuanOCR 的评测结果基于 TensorRT，可能与 Transformers 或 vLLM 推理结果存在轻微差异。不过，OCRBench 当前约 27 个百分点的差距较大；同时 OmniDocBench 存在大量超时，因此想请社区协助确认 EvalScope 的数据集、提示词、推理参数或评分实现是否与官方评测口径一致。


## EvalScope 版本（必填）
v1.19.1

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

模型启动命令：
```
nohup vllm serve /nas/disk1/HunyuanOCR    --host 0.0.0.0  --port 9000   --served-model-name hyocr  --dtype bfloat16   --max-model-len 32768   --trust-remote-code   > vllm.log 2>&1 &

  tail -f vllm.log
```

测评命令：
```
nohup evalscope eval \
  --model hyocr \
  --generation-config '{"max_tokens":20000,"top_k":-1,"temperature":0,"n":1,"timeout":160,"do_sample":false}' \
  --eval-type openai_api \
  --eval-batch-size 10 \
  --api-key EMPTY \
  --api-url http://55.122.12.106:30089/v1 \
  --ignore-errors \
  --datasets omni_doc_bench \
  --dataset-args '{"omni_doc_bench":{"local_path":"/model/lvwx/upload/zqq/OmniDocBench_tsv"}}'  > eval1.log 2>&1 &

tail -f eval1.log


nohup  evalscope eval \
  --model hyocr  \
  --dataset-hub Local \
  --generation-config '{"max_tokens":20000,"top_k":-1,"temperature":0,"n":1,"timeout":60,"do_sample":false}' \
  --eval-type openai_api \
  --eval-batch-size 10 \
  --api-key EMPTY \
  --api-url http://55.122.12.106:30089/v1 \
  --ignore-errors \
  --datasets ocr_bench \
  --dataset-args '{"ocr_bench":{"local_path":"/nas/disk5/JGB-HZ/datasets/OCRBench"}}'   > eval.log 2>&1 &

tail -f eval.log
```
## 错误日志

<img width="1271" height="846" alt="Image" src="https://github.com/user-attachments/assets/60c20cfb-c6ec-4e0a-b959-10eb2f2b2922" />

<img width="1654" height="886" alt="Image" src="https://github.com/user-attachments/assets/c6c3e1f6-85d9-45b9-af43-61f8d427bb4e" />



## 评论 (3)

### Yunnglin · 2026-07-29

您好，感谢反馈。我们核对了 EvalScope 的 OCRBench 评分实现，与官方评测脚本一致（inclusion-based 匹配、HME100k 特判），差距主要来自评测口径与部署方式的不一致，建议按以下方式对齐后重测：

**1. vLLM 部署方式与官方要求不符（主要原因）**

HunyuanOCR 官方 README 明确要求：

```bash
vllm serve tencent/HunyuanOCR --no-enable-prefix-caching --mm-processor-cache-gb 0
```

且需 `vllm>=0.12.0`。您的启动命令缺少这两个 flag，prefix caching 和 mm-processor cache 对该模型有已知精度问题（参考官方 2025/11/28 的修复说明）。另外官方指标基于 TensorRT，README 也说明与 vLLM/Transformers 存在固有差异。

**2. Prompt 口径不同**

HunyuanOCR 是 1B 指令敏感的专家模型，官方评测使用自家推荐指令。EvalScope 的 OmniDocBench 默认使用 OmniDocBench 官方英文 prompt，建议通过 `dataset-args` 覆盖为 Hunyuan 官方中文解析指令：

```bash
--dataset-args '{"omni_doc_bench": {"local_path": "...", "prompt_template": "提取文档图片中正文的所有信息用markdown格式表示，其中页眉、页脚部分忽略，表格用html格式表示，文档中公式用latex格式表示，按照阅读顺序组织进行解析。"}}'
```

**3. OmniDocBench 大量 Timeout**

HunyuanOCR 存在重复生成问题（官方推理脚本内置 `clean_repeated_substrings` 后处理），陷入重复时会生成满 `max_tokens=20000`，单请求远超您设置的 `timeout: 160`。建议将 `timeout` 调至 600 以上、适当降低 `--eval-batch-size`；跑完后可用 `--use-cache <上次输出目录>` 仅补跑失败样本。

按 1、2 对齐后如仍有明显差距，欢迎附上 `outputs/` 下的 predictions 样例，我们进一步排查。


### AuFlow · 2026-07-31

非常感谢你的回复，我按照您说的修改了模型启动命令，以及omnidocbench更换prompt后，结果还是不理想
以ocrbench数据集为例：
模型启动命令：
```
nohup vllm serve /nas/disk1/HunyuanOCR/ \
    --host 0.0.0.0 \
    --port 9000 \
    --served-model-name hyocr \
    --dtype bfloat16 \
    --max-model-len 32768 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --mm-processor-cache-gb 0 \
    > hyvllm.log 2>&1 &
```

测评脚本：
```
evalscope eval \
  --model hyocr \
  --api-url http://55.122.12.106:30044/v1 \
  --api-key EMPTY \
  --eval-type openai_api \
  --datasets ocr_bench \
  --generation-config '{"max_tokens":20000,"top_k":-1,"temperature":0,"n":1,"timeout":160,"do_sample":false}' \
  --dataset-args '{"ocr_bench":{"local_path":"/nas/disk5/JGB-HZ/datasets/OCRBench"}}' \
  --eval-batch-size 8

```

output文件：
https://s3gw.cmbchina.com/lb2003-resource-prd-1255000089/CMB100001/6492d83ec40847248a/bf8cbdb991d547b4b6/output.zip?fileKey=bf8cbdb991d547b4b6&isDlpReview=true


### Yunnglin · 2026-08-04

该问题已通过 #1535 修复并合入 `main`，主要包括：

- 修正 OCRBench 的提示词与图片顺序，确保多模态请求中图片位于文本提示之前。
- 修正 HME100k 的大小写敏感评分行为，其他 OCRBench 子任务仍保持大小写不敏感。
- 修正空 system prompt 的消息处理逻辑。
- 同步修正 OmniDocBench 的图片与提示词顺序。
- 新增 `omni_doc_bench_v1_6`，使用 OpenDataLab/OmniDocBench 数据和官方 Docker 评分环境。

请更新至最新 `main` 或等待包含该修复的新版本发布后重新测试。若仍存在明显的分数差异或 Timeout，请重新打开此 issue，并附上新的运行配置及 `predictions`/`reviews` 输出，我们会继续排查。

