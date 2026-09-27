# [Issue #2295] Hadamard import failure

source: https://github.com/ModelCloud/GPTQModel/issues/2295
state: closed | updated: 2025-12-22T09:45:57Z
labels: bug

## 正文

When using `rotation=hadamard` for Qwen2.5-1.5B-instruct, the import fails with below error.

```
INFO  ENV: Auto setting PYTORCH_CUDA_ALLOC_CONF='expandable_segments:True' for memory saving.                                                                         
INFO  ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.                                                                                                 
[2025-12-21 21:08:03,704] [DEBUG] [utils.py:63:load_model_from_task] Loaded model <class 'transformers.models.auto.modeling_auto.AutoModelForCausalLM'> with name_or_path Qwen/Qwen2.5-1.5B-Instruct
INFO  Model: Loaded `generation_config`: GenerationConfig {
  "bos_token_id": 151643,
  "do_sample": true,
  "eos_token_id": [
    151645,
    151643
  ],
  "pad_token_id": 151643,
  "repetition_penalty": 1.1,
  "temperature": 0.7,
  "top_k": 20,
  "top_p": 0.8
}

INFO  Kernel: loaded -> `[]`                                                                                                                                          
INFO  Packing Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`                                                                                          
INFO:tokenicer.tokenicer:Tokenicer: Auto fixed pad_token_id=151643 (token='<|endoftext|>').
INFO  Rotation requires word embeddings to be untied. Untying.                                                                                                        
Rotating [1 of 28] ████----------------------------------------------------------------------------------------------------------------| 0:00:00 / 0:00:00 [1/28] 3.6%[2025-12-21 21:08:12,370] [ERROR] [engine.py:727:_run_pass] Pass run failed.
Traceback (most recent call last):
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/olive/engine/engine.py", line 715, in _run_pass
    output_model_config = host.run_pass(p, input_model_config, output_model_path)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/olive/systems/local.py", line 45, in run_pass
    output_model = the_pass.run(model, output_model_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/olive/passes/olive_pass.py", line 242, in run
    output_model = self._run_for_config(model, self.config, output_model_path)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/olive/passes/pytorch/gptqmodel.py", line 160, in _run_for_config
    quantized_model.quantize(dataset, tokenizer=get_tokenizer(model.model_path))
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/gptqmodel/models/base.py", line 455, in quantize
    self.model, _ = rotate_model(model=self.model, rotate_mode=self.quantize_config.rotation,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/gptqmodel/quantization/rotation/rotation.py", line 193, in rotate_model
    rotate_ov_proj(layer, num_heads, head_dim)
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/gptqmodel/quantization/rotation/rotation.py", line 164, in rotate_ov_proj
    apply_exact_had_to_linear(v_proj, had_dim=head_dim, output=True)
  File "/prj/pyenvs/olive_venv/lib/python3.12/site-packages/gptqmodel/quantization/rotation/hadamard_utils.py", line 168, in apply_exact_had_to_linear
    fast_hadamard_transform.hadamard_transform( # noqa: F821
    ^^^^^^^^^^^^^^^^^^^^^^^
NameError: name 'fast_hadamard_transform' is not defined. Did you mean: 'import_fast_hadamard_transform'?
```
But if I directly do an import as below, the error goes away
```
def apply_exact_had_to_linear(module, had_dim=-1, output=False):
    import fast_hadamard_transform
    assert isinstance(module, torch.nn.Linear)
    in_features, out_features = module.in_features, module.out_features
```

## 评论 (1)

### Qubitium · 2025-12-22

Fixed by https://github.com/ModelCloud/GPTQModel/pull/2298

