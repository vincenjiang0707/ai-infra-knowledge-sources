# [Issue #2518] [optimized-baseline] XPU vLLM guide crashes on Gemma4 due to --disable-sliding-window

source: https://github.com/llm-d/llm-d/issues/2518
state: closed | updated: 2026-09-17T05:57:11Z
labels: 

## 正文

## Summary

The XPU vLLM `optimized-baseline` guide currently adds `--disable-sliding-window` unconditionally. Deploying `google/gemma-4-12B-it-qat-w4a16-ct` with `ghcr.io/llm-d/llm-d-xpu:v0.9.0` (vLLM 0.26.0) causes both model-server replicas to crash during startup.

## Reproduction

1. Deploy `google/gemma-4-12B-it-qat-w4a16-ct` using the `optimized-baseline` XPU/vLLM guide.
2. Use the upstream image `ghcr.io/llm-d/llm-d-xpu:v0.9.0`.
3. Observe the generated vLLM command contains:

```text
--disable-sliding-window
```

## Observed behavior

Both model-server Pods enter `CrashLoopBackOff` and never become ready. The container logs show:

```text
TypeError: Field 'sliding_window' expected int, got NoneType (value: None)\n...\nhuggingface_hub.errors.StrictDataclassFieldValidationError: Validation error for field 'sliding_window'\n```\n\nThe failure occurs in vLLM 0.26.0 while creating the model config for `Gemma4UnifiedForConditionalGeneration`; the deployment fails before the model server starts listening.\n\n## Expected behavior\n\nThe guide should either:\n\n- avoid adding `--disable-sliding-window` for models/runtime combinations that are incompatible with it; or\n- provide a model/runtime-specific conditional override; or\n- document and use a compatible vLLM/`huggingface_hub` image version.\n\n## Additional context\n\nThe argument is currently defined in:\n\n`guides/optimized-baseline/modelserver/xpu/vllm/patch-vllm.yaml`\n\nRemoving the argument through Prism UI custom runtime overrides is not currently possible because the guide supplies it as a base argument; an empty override preserves the flag and setting it to `false` is not valid for this valueless argument.\n\nRemoving the argument from the generated manifest allows testing whether the image/model combination starts successfully.\n\nEnvironment: Intel XPU, Kubernetes, model parallelism TP=2, replicas=2.

## 评论 (1)

### wimCCC · 2026-09-17

Closing this issue because the affected behavior is in the llm-d-prism deployment/configuration flow rather than the upstream guide repository. I will track it in the Prism repository instead.
