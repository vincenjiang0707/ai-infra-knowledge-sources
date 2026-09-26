# [Issue #884] Unable to run Magistral-Small-2509 benchmark

source: https://github.com/modelscope/evalscope/issues/884
state: closed | updated: 2026-07-08T06:16:27Z
labels: enhancement

## 正文

## Problem Description

Unable to run Magistral-Small-2509 benchmark


## EvalScope Version (Required)
1.1.0

## Executed Code or Instructions

evalscope perf \
    --url "http://127.0.0.1:7999/v1/chat/completions" \
    --parallel 1 4 16 64 \
    --number 100 100 100 100 \
    --model /models/Magistral-Small-2509 \
    --api openai \
    --dataset random \
    --min-prompt-length 1024 \
    --max-prompt-length 1024 \
    --min-tokens 256 \
    --max-tokens 256 \
    --tokenizer-path mistralai/Magistral-Small-2509


## Error Log

2025-10-17 16:56:31 - evalscope - ERROR: Exception in async function 'benchmark': <class 'transformers.models.mistral3.configuration_mistral3.Mistral3Config'>
Traceback (most recent call last):
  File "/home/llmsvc1/venv/lib/python3.10/site-packages/evalscope/perf/utils/handler.py", line 17, in async_wrapper
    return await func(*args, **kwargs)
  File "/home/llmsvc1/venv/lib/python3.10/site-packages/evalscope/perf/benchmark.py", line 184, in benchmark
    api_plugin = api_plugin_class(args)
  File "/home/llmsvc1/venv/lib/python3.10/site-packages/evalscope/perf/plugin/api/openai_api.py", line 31, in __init__
    self.tokenizer = AutoTokenizer.from_pretrained(param.tokenizer_path)
  File "/home/llmsvc1/venv/lib/python3.10/site-packages/modelscope/utils/hf_util/patcher.py", line 285, in from_pretrained
    module_obj = module_class.from_pretrained(
  File "/home/llmsvc1/venv/lib/python3.10/site-packages/transformers/models/auto/tokenization_auto.py", line 1141, in from_pretrained
    tokenizer_class_py, tokenizer_class_fast = TOKENIZER_MAPPING[type(config)]
  File "/home/llmsvc1/venv/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py", line 815, in __getitem__
    raise KeyError(key)
KeyError: <class 'transformers.models.mistral3.configuration_mistral3.Mistral3Config'>


## Running Environment

- Operating System: Ubuntu 22.04.5 LTS
- Python Version: 3.10.12

## Additional Information

No problem running on Qwen3-VL-30B-A3B-Instruct and Qwen3-VL-235B-A22B-Thinking.


## 评论 (2)

### Yunnglin · 2025-10-17

This is mainly because the default transformers doesn't support directly loading Mistral models. You need to install mistral_common and set tokenizer_type="mistral". Let me see how to make it compatible.

### Yunnglin · 2026-07-08

Thanks for reporting this. We checked the tokenizer loading path and this is caused by an older `transformers` version not having a tokenizer mapping for `Mistral3Config`.

Recent `transformers` versions already handle this via `MistralCommonBackend` from `mistral_common`, so EvalScope does not need a separate `tokenizer_type="mistral"` compatibility branch here. Please upgrade the related dependencies and try again:

```bash
pip install -U "transformers!=4.57.2" mistral_common
```

If the issue still reproduces after the upgrade, please feel free to reopen with the output of:

```bash
python -c "import transformers; print(transformers.__version__)"
```

Closing this as a dependency compatibility issue rather than an EvalScope perf bug.

