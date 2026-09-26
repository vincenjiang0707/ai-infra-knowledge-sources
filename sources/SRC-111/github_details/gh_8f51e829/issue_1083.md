# [Issue #1083] vLLM Python backends start up twice

source: https://github.com/vllm-project/guidellm/issues/1083
state: closed | updated: 2026-09-08T14:34:51Z
labels: priority-medium, internal

## 正文

### Bug Description

When using the `vllm_python` backend the initial validation triggers a vLLM startup on the main process. Then the spawned worker initializes the backend again.

### Expected Behavior

This likely broke due to the switch to spawn as the default context, since before we would have passed the initialized backend directly to the worker. The correct behavior is to not initialize the backend in the main process.

### Steps to Reproduce

Run a benchmark with the vllm_python backend an observe vLLM starting twice:

```sh
guidellm run \
    --backend kind=vllm_python,model=Qwen/Qwen3-0.6B \
    --data kind=synthetic_text,prompt_tokens=256,output_tokens=128 \
    --profile kind=constant,rate=3 \
    --constraint kind=max_duration,seconds=20
```

### Operating System

Ubuntu 22.04.5 (Container)

### Python Version

3.12.13

### GuideLLM Version

main

### Installation Method

pip install guidellm

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell

```

### Additional Context

_No response_

## 评论 (1)

### Pragadeesh122 · 2026-09-04

Hey @sjmonson 👋 — I'll pick this up. Plan: skip the main-process backend startup/validate in `resolve_backend` for in-process backends (e.g. `vllm_python`) so the engine only initializes in the worker, and resolve `default_model` without a startup.
