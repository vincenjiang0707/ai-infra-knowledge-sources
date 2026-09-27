# [Issue #1668] [BUG] Tensor mismatch on a lot of models

source: https://github.com/ModelCloud/GPTQModel/issues/1668
state: closed | updated: 2025-12-23T10:29:01Z
labels: bug

## 正文

RuntimeError: The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 3
PS C:\Users\User1\Documents\Code\ContextQ> pip install -v gptqmodel --no-build-isolation 

This happens with the demo code on readme as well as Llama 3.1 and Mistral.

Makes it unusable and always happens while quantizing the second layer

## 评论 (18)

### QingshuiL · 2025-08-12

You can try downgrading the transformers == 4.51.2. 

### gapsong · 2025-08-12

@QingshuiL 
Thank you! It works, but why?

### Qubitium · 2025-08-21

Fixed in `main`. 

### gapsong · 2025-09-25

@Qubitium where did you fix it? I have still the same error

### Qubitium · 2025-09-25

@gapsong  `main` 5.0.0dev0  is currently unstable. Which version are you on and what exactly is your stack trace?

### gapsong · 2025-09-26

@Qubitium I just pulled the newest version from github
and installed via pip install -e .

### Qubitium · 2025-09-26

@gapsong  Need stacktrace.

### gapsong · 2025-09-26

`Traceback (most recent call last):                                                                                              
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/runpy.py", line 198, in _run_module_as_main
    return _run_code(code, main_globals, None,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/runpy.py", line 88, in _run_code
    exec(code, run_globals)
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 71, in <module>
    cli.main()
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 501, in main
    run()
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 351, in run_file
    runpy.run_path(target, run_name="__main__")
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 310, in run_path
    return _run_module_code(code, init_globals, run_name, pkg_name=pkg_name, script_name=fname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 127, in _run_module_code
    _run_code(code, mod_globals, init_globals, mod_name, mod_spec, pkg_name, script_name)
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 118, in _run_code
    exec(code, run_globals)
  File "/home/nudel/Documents/peft/examples/qalora_finetuning/ultimate_train_collection.py", line 1068, in <module>
    train()
  File "/home/nudel/Documents/peft/examples/qalora_finetuning/ultimate_train_collection.py", line 509, in train
    model = load_or_quantize_model(
            ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/peft/examples/qalora_finetuning/ultimate_train_collection.py", line 350, in load_or_quantize_model
    model = AutoModelForCausalLM.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/models/auto/auto_factory.py", line 604, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/modeling_utils.py", line 288, in _wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/modeling_utils.py", line 5283, in from_pretrained
    hf_quantizer.postprocess_model(model, config=config)
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/quantizers/base.py", line 251, in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/quantizers/quantizer_gptq.py", line 116, in _process_model_after_weight_loading
    self.optimum_quantizer.quantize_model(model, self.quantization_config.tokenizer)
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/optimum/optimum/gptq/quantizer.py", line 777, in quantize_model
    block(*layer_inputs[j], **layer_input_kwargs[j])
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 294, in forward
    hidden_states, _ = self.self_attn(
                       ^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 241, in forward
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/peft_testing/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 138, in apply_rotary_pos_emb
    q_embed = (q * cos) + (rotate_half(q) * sin)
               ~~^~~~~
RuntimeError: The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 3`

@Qubitium 

### gapsong · 2025-09-26

@Qubitium  
I'm encountering a version-specific issue with GPTQModel. When I use an older version of transformers, I can successfully quantize and cache the model. However, a problem arises during loading, as an incorrect ModelType is automatically selected.
Conversely, when using a newer version like 5.0.0dev, the model loading logic works correctly. The issue with this newer version is that the quantization process fails due to a dimension error.
My current workaround involves using the older version to quantize and create the cached models. Once I have all the quantized versions cached, I upgrade to the newer version and install the latest transformers library to utilize the cached models.

### Qubitium · 2025-09-30

@gapsong please test newest version of 5.0 on main. Lots and lots of changes and bug fixes.

### gapsong · 2025-10-02

Hi @Qubitium,
I've encountered an issue after the package was apparently renamed from gpt-qmodel to gptqmodel. My installation of the transformers library (version 5.0.0) is now raising an error, stating that the gptqmodel package cannot be found and needs to be installed.
I'm curious about the reason for this name change. Was there a specific motivation, such as aligning with Python package naming conventions or improving integration with other libraries? A brief explanation in the README or release notes could be very helpful for the community to understand these changes and avoid confusion during future updates.

### gapsong · 2025-10-02

@Qubitium I have upgraded the version to gptq now and have the same error still.

INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/pare-hiccoughing/`                                                                      
INFO:optimum.gptq.quantizer:Quantizing self_attn.o_proj in block 1/24...█████▊                                                 | 3/7 [00:03<00:04,  1.00s/it]
INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/myxoedema-mercantile/`                                                                  
INFO:optimum.gptq.quantizer:Quantizing mlp.gate_proj in block 1/24...█████████████████████▏                                    | 4/7 [00:04<00:02,  1.02it/s]
INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/unprobably-bluffers/`                                                                   
INFO:optimum.gptq.quantizer:Quantizing mlp.up_proj in block 1/24...███████████████████████████████████▍                        | 5/7 [00:04<00:01,  1.03it/s]
INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/myelodiastasis-thrack/`                                                                 
INFO:optimum.gptq.quantizer:Quantizing mlp.down_proj in block 1/24...█████████████████████████████████████████████▋            | 6/7 [00:05<00:00,  1.03it/s]
Quantizing model.layers blocks :   4%|███▋                                                                                    | 1/24 [00:09<03:35,  9.35s/it]INFO:optimum.gptq.quantizer:Start quantizing block model.layers 2/24                                                                                                 
INFO:optimum.gptq.quantizer:Module to quantize [['self_attn.q_proj'], ['self_attn.k_proj'], ['self_attn.v_proj'], ['self_attn.o_proj'], ['mlp.gate_proj'], ['mlp.up_proj'], ['mlp.down_proj']]
INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/swouning-thanklessly/`                                                                  
Quantizing model.layers blocks :   4%|███▋                                                                                    | 1/24 [00:09<03:37,  9.44s/it], ?it/s]
Traceback (most recent call last):                                                                                                                                   
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/runpy.py", line 198, in _run_module_as_main
    return _run_code(code, main_globals, None,
                     "__main__", mod_spec)
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/runpy.py", line 88, in _run_code
    exec(code, run_globals)
    ~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 71, in <module>
    cli.main()
    ~~~~~~~~^^
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 501, in main
    run()
    ~~~^^
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 351, in run_file
    runpy.run_path(target, run_name="__main__")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 310, in run_path
    return _run_module_code(code, init_globals, run_name, pkg_name=pkg_name, script_name=fname)
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 127, in _run_module_code
    _run_code(code, mod_globals, init_globals, mod_name, mod_spec, pkg_name, script_name)
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/.vscode-server/extensions/ms-python.debugpy-2025.10.0-linux-x64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 118, in _run_code
    exec(code, run_globals)
    ~~~~^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/peft/examples/qalora_finetuning/ultimate_train_collection.py", line 1148, in <module>
    train()
    ~~~~~^^
  File "/home/nudel/Documents/peft/examples/qalora_finetuning/ultimate_train_collection.py", line 925, in train
    check_cached_quantize(quantized_path, full_precision_residual_path, tokenizer=tokenizer, bits=bits, group_size=group_size)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/peft/examples/qalora_finetuning/ultimate_train_collection.py", line 460, in check_cached_quantize
    quantized_model = AutoModelForCausalLM.from_pretrained(
        model_to_quantize, device_map="auto", quantization_config=gptq_config, torch_dtype=torch.float16
    )
  File "/home/nudel/Documents/transformers/src/transformers/models/auto/auto_factory.py", line 604, in from_pretrained
    return model_class.from_pretrained(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        pretrained_model_name_or_path, *model_args, config=config, **hub_kwargs, **kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/nudel/Documents/transformers/src/transformers/modeling_utils.py", line 288, in _wrapper
    return func(*args, **kwargs)
  File "/home/nudel/Documents/transformers/src/transformers/modeling_utils.py", line 5283, in from_pretrained
    hf_quantizer.postprocess_model(model, config=config)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/transformers/src/transformers/quantizers/base.py", line 251, in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/transformers/src/transformers/quantizers/quantizer_gptq.py", line 116, in _process_model_after_weight_loading
    self.optimum_quantizer.quantize_model(model, self.quantization_config.tokenizer)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/nudel/Documents/optimum/optimum/gptq/quantizer.py", line 777, in quantize_model
    block(*layer_inputs[j], **layer_input_kwargs[j])
    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/transformers/src/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/nudel/Documents/transformers/src/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/nudel/Documents/transformers/src/transformers/models/llama/modeling_llama.py", line 294, in forward
    hidden_states, _ = self.self_attn(
                       ~~~~~~~~~~~~~~^
        hidden_states=hidden_states,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<6 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/nudel/miniconda3/envs/master_thesis_new_version/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/nudel/Documents/transformers/src/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/nudel/Documents/transformers/src/transformers/models/llama/modeling_llama.py", line 241, in forward
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
                               ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/nudel/Documents/transformers/src/transformers/models/llama/modeling_llama.py", line 138, in apply_rotary_pos_emb
    q_embed = (q * cos) + (rotate_half(q) * sin)
               ~~^~~~~
RuntimeError: The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 3

### Qubitium · 2025-10-02

> Hi [@Qubitium](https://github.com/Qubitium), I've encountered an issue after the package was apparently renamed from gpt-qmodel to gptqmodel. My installation of the transformers library (version 5.0.0) is now raising an error, stating that the gptqmodel package cannot be found and needs to be installed. I'm curious about the reason for this name change. Was there a specific motivation, such as aligning with Python package naming conventions or improving integration with other libraries? A brief explanation in the README or release notes could be very helpful for the community to understand these changes and avoid confusion during future updates.

The pkg name change will be reverted in the pending PR https://github.com/ModelCloud/GPTQModel/pull/1969

### gapsong · 2025-10-03

@Qubitium We still do not have an answer yet. I could do a Pr if you could give me a potential reason, why that happens.
Do you have any idea why that happens when using a newer transformer version?

File "/home/nudel/Documents/transformers/src/transformers/models/llama/modeling_llama.py", line 138, in apply_rotary_pos_emb
q_embed = (q * cos) + (rotate_half(q) * sin)
~~^~~~~
RuntimeError: The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 3

### Qubitium · 2025-10-03

> @Qubitium We still do not have an answer yet. I could do a Pr if you could give me a potential reason, why that happens.
> Do you have any idea why that happens when using a newer transformer version?
> 
> File "/home/nudel/Documents/transformers/src/transformers/models/llama/modeling_llama.py", line 138, in apply_rotary_pos_emb
> q_embed = (q * cos) + (rotate_half(q) * sin)
> ~~^~~~~
> RuntimeError: The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 3


Because transformers 5.0 is still in dev and unstable is my best answer. I cannot prioritize fixing something for an dev/unstable branch of transformers. Their entire modeling backend has changed for 5.0 so everything may and will break. There are still somethings i need to do beforeoving on to transformer 5.0 compat.



### gapsong · 2025-10-03

@Qubitium thank you for that answer and the effort you put into this project! 
I appreciate your work

### Luadoo · 2025-10-15

Hello, I have try implementation your code get this error, even in the OPT-350M or new model. I am try decreased damp_percent  But the error not fixed yet. Thanks!

<img width="1304" height="895" alt="Image" src="https://github.com/user-attachments/assets/6175c5e7-dcfe-41cf-819e-32db52dec116" />

<img width="1304" height="895" alt="Image" src="https://github.com/user-attachments/assets/c6a7faad-a776-41e3-9525-f3c919c19507" />

### Qubitium · 2025-10-15

@Luadoo  Instrall gptqmodel from `main` branch and run our `tests/models/test_opt.py`. It is passing our tests on `main`. 

```bash
git clone...
cd gptqmodel
pip install -v -e . --no-build-isolation
```

```python
--------lm_eval Eval Result---------
|    Tasks    |Version|Filter|n-shot| Metric |   |Value |   |Stderr|
|-------------|------:|------|-----:|--------|---|-----:|---|-----:|
|arc_challenge|      1|none  |     0|acc     |↑  |0.1954|±  |0.0116|
|             |       |none  |     0|acc_norm|↑  |0.2287|±  |0.0123|

--------lm_eval Result End---------
```
