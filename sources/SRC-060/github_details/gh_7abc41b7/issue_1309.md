# [Issue #1309] 使用FastDeploy和ERNIEkit部署训练后模型，均出现问题

source: https://github.com/PaddlePaddle/ERNIE/issues/1309
state: closed | updated: 2026-01-21T12:01:29Z
labels: 

## 正文

(paddlepaddle) root@mvcbisqaodkjtedf-make-8b45b5549-b22ct:/data/coding/ERNIE# erniekit server examples/configs/ERNIE-4.5-0.3B/run_chat.yaml
/data/miniconda/envs/paddlepaddle/lib/python3.12/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
W1021 11:07:22.496299 63891 gpu_resources.cc:114] Please NOTE: device: 0, GPU Compute Capability: 8.0, Driver API Version: 12.6, Runtime API Version: 12.6
[2025-10-21 11:07:24,732] [    INFO] - user has defined resume_from_checkpoint: None
[2025-10-21 11:07:24,733] [    INFO] - The default value for the training argument `--report_to` will change in v5 (from all installed integrations to none). In v5, you will need to use `--report_to all` to get the same behavior as now. You should start updating your code and make this info disappear :-).
[2025-10-21 11:07:24,733] [    INFO] - reset finetuning arguments global_batch_size to 1
[2025-10-21 11:07:24,733] [ WARNING] - eval_batch_size set to 1
[2025-10-21 11:07:24,733] [    INFO] - No Checkpoint detected, launch server from /data/coding/ERNIE/output/export.
[2025-10-21 11:07:24,733] [    INFO] - The optimal configuration for model deployment can be referred: https://github.com/PaddlePaddle/FastDeploy/tree/develop/docs/zh/optimal_deployment
/data/miniconda/envs/paddlepaddle/lib/python3.12/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
[2025-10-21 11:07:26,993] [    INFO] - Using download source: huggingface
[2025-10-21 11:07:26,993] [    INFO] - Loading configuration file /data/coding/ERNIE/output/export/config.json
[2025-10-21 11:07:26,994] [ WARNING] - You are using a model of type ernie4_5 to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
[2025-10-21 11:07:30,473] [    INFO] - Using download source: huggingface
[2025-10-21 11:07:30,474] [    INFO] - Loading configuration file /data/coding/ERNIE/output/export/config.json
[2025-10-21 11:07:30,474] [ WARNING] - You are using a model of type ernie4_5 to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
[2025-10-21 11:07:31,322] [    INFO] - Using download source: huggingface
[2025-10-21 11:07:31,322] [ WARNING] - PretrainedTokenizer will be deprecated and removed in the next major release. Please migrate to Hugging Face's transformers.PreTrainedTokenizer. Checkout paddleformers/transformers/qwen/tokenizer.py for an example: use class QWenTokenizer(PaddleTokenizerMixin, hf.PreTrainedTokenizer) to support multisource download and Paddle tokenizer operations.
[2025-10-21 11:07:31,370] [    INFO] - Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
INFO     2025-10-21 11:07:35,221 63998 engine.py[line:133] Waiting worker processes ready...
Loading Weights: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:03<00:00, 33.31it/s]
Loading Layers:  94%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏        | 94/100 [00:02<00:00, 46.96it/s]
ERROR    2025-10-21 11:07:45,227 63998 engine.py[line:142] Failed to launch worker processes, check log/workerlog.* for more details.


均报错这个

erniekit                                 0.0.0             /data/coding/ERNIE
fastdeploy-gpu                           2.2.1
paddlepaddle-gpu                         3.3.0.dev20251019

## 评论 (2)

### ckl117 · 2025-10-22

请提供下fastdeploy服务启动命令、log/workerlog.*相关报错信息、模型config.json

### nepeplwu · 2026-01-21

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
