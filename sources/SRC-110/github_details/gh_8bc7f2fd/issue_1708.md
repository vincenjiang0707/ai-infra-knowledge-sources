# [Issue #1708] mv_bench 评测报错，fine_grained_pose 子数据集截断

source: https://github.com/modelscope/evalscope/issues/1708
state: open | updated: 2026-09-08T03:00:38Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。

## EvalScope 版本（必填）
v1.11.1


## 执行的代码或指令
evalscope eval \
    --model  qwen-3.8-27b \
    --api-url   xxxxx \
    --api-key EMPTY_TOKEN \
    --datasets mvbench 

## 错误日志

[long_text_FBE67283-BA16-4C62-9FDE-CC2509C10C41.txt](https://github.com/user-attachments/files/31906678/long_text_FBE67283-BA16-4C62-9FDE-CC2509C10C41.txt)


## 运行环境

- 操作系统：ubuntu24
- Python版本：3.12

## 其他信息

定位到可能是默认下载的 mv_bench  fine_grained_pose 子数据集截断。


## 评论 (1)

### Yunnglin · 2026-09-08

Thanks for the detailed report.

From the log, `fine_grained_pose` itself does not appear to be truncated:

- The dataset loader processed all 200 records for this subset.
- `got 6 predictions, remaining 594 samples` refers to reused prediction cache entries, not the number of available dataset samples.
- The failing video was decoded with `total_num_frames=82`.

The failure occurs later in the OpenAI-compatible model server while applying `Qwen3VLProcessor`. The server received a decoded video with one selected frame (`frames_indices=[0]`), then returned HTTP 400. EvalScope only forwards this server-side error, so the client traceback does not include the underlying processor exception.

Could you please provide:

1. The vLLM version, `transformers` version, and `qwen-vl-utils` version used by the serving endpoint.
2. The vLLM server startup command, especially video-related options such as `--media-io-kwargs`.
3. The complete server-side traceback corresponding to this request.
4. Whether the same error reproduces with a single `fine_grained_pose` sample after disabling/rebuilding the local dataset cache.

As a preliminary workaround, please try upgrading the serving stack to a recent vLLM release and verify the video sampling configuration. We will be able to determine whether this is a server-side video preprocessing issue or a problematic media file once the server traceback is available.
