# [Issue #957] Qwen3.5 not works with autoquantize?

source: https://github.com/NVIDIA/Model-Optimizer/issues/957
state: closed | updated: 2026-06-22T04:39:07Z
labels: bug, stale, waiting for feedback, torch.quantization

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
<!-- Description of what the bug is, its impact (blocker, should have, nice to have) and any stack traces or error messages. -->

```
RuntimeError: Quantization failed for Qwen/Qwen3.5-4B with exit code 1
  Calibrating for FP8_DEFAULT_CFG(effective-bits: 8.0): 100%|██████████| 43/43 [00:17<00:00,  2.49it/s]/s]
  /opt/Model-Optimizer/modelopt/torch/quantization/plugins/huggingface.py:1194: UserWarning: AutoQuantize: Huggingface model detected - Enabling gradient checkpointing.
  Disable gradient checkpointing after AutoQuantize if this is not desired!
    warnings.warn(
  AutoQuantize: Enabling gradient for param embed_tokens.weight.

  Estimating auto_quantize scores:   0%|          | 0/10 [00:00<?, ?it/s]| 46/256 [00:18<01:24,  2.48it/s]| reserved:  1.35e+05 | max_reserved:  1.35e+05
  Traceback (most recent call last):
    File "/opt/Model-Optimizer/examples/llm_ptq/hf_ptq.py", line 1215, in <module>
      main(args)
    File "/opt/Model-Optimizer/examples/llm_ptq/hf_ptq.py", line 1193, in main
      quantize_main(
    File "/opt/Model-Optimizer/examples/llm_ptq/hf_ptq.py", line 878, in quantize_main
      auto_quantize(
    File "/opt/Model-Optimizer/examples/llm_ptq/hf_ptq.py", line 278, in auto_quantize
      language_model, _ = mtq.auto_quantize(
                          ^^^^^^^^^^^^^^^^^^
    File "/opt/Model-Optimizer/modelopt/torch/quantization/model_quant.py", line 495, in auto_quantize
      searcher.search(model, constraints, config=search_config)  # type: ignore[arg-type]
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/opt/Model-Optimizer/modelopt/torch/opt/searcher.py", line 151, in search
      self.before_search()
    File "/opt/Model-Optimizer/modelopt/torch/quantization/algorithms.py", line 637, in before_search
      self.estimate_sensitivity_scores()
    File "/opt/Model-Optimizer/modelopt/torch/quantization/algorithms.py", line 970, in estimate_sensitivity_scores
      self._estimate_auto_quantize_scores(is_param_grad_enabled)
    File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context
      return func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
    File "/opt/Model-Optimizer/modelopt/torch/quantization/algorithms.py", line 935, in _estimate_auto_quantize_scores
      self._run_func(
    File "/opt/Model-Optimizer/modelopt/torch/quantization/algorithms.py", line 580, in _run_func
      func(self.model, data)
    File "/opt/Model-Optimizer/modelopt/torch/quantization/algorithms.py", line 821, in forward_backward_step
      loss = self.config["loss_func"](output, data)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/opt/Model-Optimizer/examples/llm_ptq/hf_ptq.py", line 263, in loss_func
      return output.loss
             ^^^^^^^^^^^
```

- ?

### Steps/Code to reproduce bug
<!-- Please list *minimal* steps or code snippet for us to be able to reproduce the bug. -->
<!-- A helpful guide on on how to craft a minimal bug report http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports. -->
`--qformat nvfp4,fp8 --auto_quantize_bits 4` with HF_ptq and any qwen3.5 model. 

See https://huggingface.co/docs/transformers/model_doc/qwen3_5 

- ?

### Expected behavior

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): ?
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): ? <!-- If Windows, please add the `windows` label to the issue. -->
- CPU architecture (x86_64, aarch64): ?
- GPU name (e.g. H100, A100, L40S): ?
- GPU memory size: ?
- Number of GPUs: ?
- Library versions (if applicable):
  - Python: ?
  - ModelOpt version or commit hash: ?
  - CUDA: ?
  - PyTorch: ?
  - Transformers: ?
  - TensorRT-LLM: ?
  - ONNXRuntime: ?
  - TensorRT: ?
- Any other details that may help: ?


## 评论 (3)

### vincentzed · 2026-05-24

If it works today, I dont need it anymore, but was looking to use autoquantize(not just regular quantize ptq, i.e different quant for different layer)

### github-actions[bot] · 2026-06-08

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-22

This issue was closed because it has been 14 days without activity since it has been marked as stale.
