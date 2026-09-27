# [Issue #4484] [Bug] lmdeploy run qwen3.5-122b-a10b-awq , which transformers version?

source: https://github.com/InternLM/lmdeploy/issues/4484
state: open | updated: 2026-04-29T07:09:00Z
labels: 

## 正文

### Checklist

- [ ] 1. I have searched related issues but cannot get the expected help.
- [ ] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug


run : CUDA_VISIBLE_DEVICES=0,1,2,3
lmdeploy serve api_server /home/eric/Qwen3.5-122b-A10B-AWQ --backend pytorch --tp 4 --server-name 0.0.0.0 --server-port 8001  --log-level INFO 

`The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-04-01 16:16:59,225 - lmdeploy - WARNING - archs.py:45 - Fallback to pytorch engine because `/home/eric/Qwen3.5-122b-A10B-AWQ` not supported by turbomind engine.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type qwen3_5_moe to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-04-01 16:17:01,100 - lmdeploy - WARNING - utils.py:340 - The model's config.json does not contain any of the following keys to determine the original maximum length of the model: ['max_position_embeddings', 'n_positions', 'max_seq_len', 'seq_length', 'model_max_length', 'max_sequence_length', 'max_seq_length', 'seq_len']. Assuming the model's maximum length is 2048.
2026-04-01 16:17:07,504 - lmdeploy - ERROR - base.py:55 - ValueError: The checkpoint you are trying to load has model type `qwen3_5_moe` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git`
2026-04-01 16:17:07,504 - lmdeploy - ERROR - base.py:56 - <transformers> check failed!
Load model config with transformers==4.57.1 failed. Please make sure model can be loaded with transformers API.`

### Reproduction

 lmdeploy serve api_server /home/eric/Qwen3.5-122b-A10B-AWQ \
    --model-format awq \
    --tp 4 \
    --server-port 23333 \

### Environment

```Shell
4 gpu titan NVIDIA TITAN RTX ,96g 
cuda version : 13.1 
nvidia-smi : 590.48.01
```

### Error traceback

```Shell

```

## 评论 (3)

### lvhan028 · 2026-04-02

LMDeploy supports the Qwen3.5 AWQ models listed here: https://huggingface.co/collections/QuantTrio/qwen35-awq
AWQ models not in this list may not be supported.

### bltcn · 2026-04-16

官方的gptq版本是否支持？

### lvhan028 · 2026-04-29

> 官方的gptq版本是否支持？
还没有。
@43758726 请将这项任务加入到工作列表中
