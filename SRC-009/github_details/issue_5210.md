# [Issue #5210] Broken checkpoint converter for whisper

source: https://github.com/NVIDIA/TensorRT-LLM/issues/5210
state: closed | updated: 2026-09-10T01:14:09Z
labels: bug, triaged, Model customization

## 正文

Hi. I'm trying to recreate this demo: https://github.com/NVIDIA/TensorRT-LLM/tree/e88da961c51b300e6b9c931476428a2de908830d/examples/whisper. 
I use the large-3 model. However, when I try to build the decoder, I get this error:
```python
Traceback (most recent call last):
  File "/usr/local/bin/trtllm-build", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/commands/build.py", line 621, in main
    parallel_build(model_config, ckpt_dir, build_config, args.output_dir,
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/commands/build.py", line 419, in parallel_build
    passed = build_and_save(rank, rank % workers, ckpt_dir,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/commands/build.py", line 384, in build_and_save
    engine = build_model(build_config,
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/commands/build.py", line 361, in build_model
    model = model_cls.from_checkpoint(ckpt_dir, config=rank_config)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/models/modeling_utils.py", line 661, in from_checkpoint
    model.load(weights, from_pruned=is_checkpoint_pruned)
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/models/modeling_utils.py", line 684, in load
    raise RuntimeError(
RuntimeError: Required but not provided tensors:{'decoder_layers.28.cross_attention.dense.weight', 'final_layernorm.weight', 'decoder_layers.31.cross_attention_layernorm.weight', 'decoder_layers.13.self_attention.qkv.weight', 'decoder_layers.6.mlp.fc.bias', 'decoder_layers.4.mlp.proj.weight', 'decoder_layers.18.cross_attention.qkv.bias', 'decoder_layers.6.cross_attention.qkv.bias', 'decoder_layers.26.cross_attention_layernorm.bias', 'decoder_layers.30.cross_attention.qkv.bias', 'decoder_layers.7.cross_attention.qkv.bias', 'decoder_layers.8.cross_attention.qkv.bias', 'decoder_layers.19.self_attention_layernorm.bias', 'decoder_layers.8.mlp.fc.weight', 'decoder_layers.27.self_attention.dense.bias', 'decoder_layers.1.mlp.fc.weight', 'decoder_layers.16.self_attention_layernorm.weight', 'decoder_layers.5.cross_attention.dense.weight', 'decoder_layers.22.self_attention.dense.bias', 'decoder_layers.18.self_attention.qkv.bias', 'decoder_layers.14.mlp.fc.weight', 'decoder_layers.27.mlp.proj.weight', 'decoder_layers.6.self_attention.dense.bias', 'decoder_layers.23.mlp_layernorm.weight', 'decoder_layers.18.mlp.proj.weight', 'decoder_layers.15.cross_attention.qkv.weight', 'decoder_layers.20.self_attention.qkv.bias', 'decoder_layers.20.mlp_layernorm.bias', 'decoder_layers.25.self_attention.qkv.weight', 'decoder_layers.17.cross_attention.qkv.weight', 'decoder_layers.25.mlp_layernorm.weight', 'decoder_layers.2.cross_attention.dense.bias', 'decoder_layers.4.cross_attention.qkv.weight', 'decoder_layers.21.cross_attention.qkv.weight', 'decoder_layers.21.cross_attention_layernorm.bias', 'decoder_layers.2.cross_attention.qkv.bias', 'decoder_layers.3.cross_attention.qkv.weight', 'decoder_layers.27.cross_attention.qkv.weight', 'decoder_layers.15.self_attention_layernorm.bias', 'decoder_layers.23.cross_attention.dense.weight', 'decoder_layers.4.cross_attention_layernorm.weight', 'decoder_layers.11.cross_attention.qkv.weight', 'decoder_layers.13.cross_attention_layernorm.weight', 'decoder_layers.12.self_attention_layernorm.weight', 'decoder_layers.20.cross_attention.dense.bias', 'decoder_layers.12.cross_attention.dense.weight', 'decoder_layers.27.cross_attention_layernorm.weight', 'decoder_layers.16.cross_attention.qkv.bias', 'decoder_layers.16.cross_attention_layernorm.bias', ...
``` 
Any ideas how to fix it?

## 评论 (10)

### VALLIS-NERIA · 2025-06-19

@symphonylyh Can you please help to take a look?

### SerhiiArtemuk · 2025-07-03

@VALLIS-NERIA @symphonylyh hi. Are there any ideas or progress?

### MahmoudAshraf97 · 2025-07-21

check #5984 for a solution
@VALLIS-NERIA @symphonylyh can someone review the PR?

### IooHooI · 2025-07-30

@MahmoudAshraf97 Hello!
I was trying to reproduce instruction in your repo (https://github.com/MahmoudAshraf97/TensorRT-LLM/tree/new_whisper_checkpoint/examples/models/core/whisper) and faced with an issue:

```
2025-07-30 15:42:22,217 - INFO - flashinfer.jit: Prebuilt kernels not found, using JIT backend
[TensorRT-LLM] TensorRT-LLM version: 0.20.0
Generating train split: 336 examples [00:00, 2571.87 examples/s]
Patching 1 scaled_dot_product_attention operator with quantizers
Definition of _QuantWhisperSdpaAttention saved to /tmp/modelopt_zbse1gm9.py
Successfully registered WhisperSdpaAttention for quantization
Inserted 1155 quantizers
Passing a tuple of `past_key_values` is deprecated and will be removed in Transformers v4.43.0. You should pass an instance of `EncoderDecoderCache` instead, e.g. `past_key_values=EncoderDecoderCache.from_legacy_cache(past_key_values)`.
/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py:552: UserWarning: Cannot export model to the model_config. The modelopt-optimized model state_dict (including the quantization factors) is saved to whisper_large_v3_weights_fp8/modelopt_model.0.pth using torch.save for further inspection.
  warn(
Traceback (most recent call last):
  File "/app/tensorrt_llm/TensorRT-LLM/examples/models/core/whisper/../../../quantization/quantize.py", line 160, in <module>
    quantize_and_export(
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/quantization/quantize_by_modelopt.py", line 815, in quantize_and_export
    export_tensorrt_llm_checkpoint(
  File "/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py", line 557, in export_tensorrt_llm_checkpoint
    raise e
  File "/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py", line 488, in export_tensorrt_llm_checkpoint
    for (
  File "/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py", line 229, in torch_to_tensorrt_llm_checkpoint
    assert compatible, "The model is not supported"
           ^^^^^^^^^^
AssertionError: The model is not supported
```

Here is the command I used:

```
python3 ../../../quantization/quantize.py         
    --model_dir openai/whisper-large-v3
    --qformat fp8
    --output_dir ${checkpoint_dir}
    --calib_dataset ./peoples_speech
    --calib_size 100
```

I tried to use this Docker image to run the script:
https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags

And this dataset:
https://huggingface.co/datasets/MLCommons/peoples_speech/viewer/microset?views%5B%5D=microset

Could you maybe give me a clue of what am I doing wrong?

### IooHooI · 2025-07-30

BTW, I get the same error that @SerhiiArtemuk described above.
@VALLIS-NERIA @symphonylyh are there any news on this issue?

### SerhiiArtemuk · 2025-07-31

@IooHooI A week ago, I tried this approach with whisper-large-v3-turbo models, and everything worked and built correctly.
I tried these models: [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) and [Na0s/Medical-Whisper-Large-v3](https://huggingface.co/Na0s/Medical-Whisper-Large-v3).

@MahmoudAshraf97 In my case everything works with TensorRT-LLM version 0.20. However, I am forced to run it with version 0.17. When I try to build the decoder and encoder with version 0.17, I get the same messages about mismatched layer names. Are there any options for downgrading these instructions (checkpoints conversion) from 0.20 to 0.17?



### MahmoudAshraf97 · 2025-07-31

> [@MahmoudAshraf97](https://github.com/MahmoudAshraf97) Hello! I was trying to reproduce instruction in your repo (https://github.com/MahmoudAshraf97/TensorRT-LLM/tree/new_whisper_checkpoint/examples/models/core/whisper) and faced with an issue:
> 
> ```
> 2025-07-30 15:42:22,217 - INFO - flashinfer.jit: Prebuilt kernels not found, using JIT backend
> [TensorRT-LLM] TensorRT-LLM version: 0.20.0
> Generating train split: 336 examples [00:00, 2571.87 examples/s]
> Patching 1 scaled_dot_product_attention operator with quantizers
> Definition of _QuantWhisperSdpaAttention saved to /tmp/modelopt_zbse1gm9.py
> Successfully registered WhisperSdpaAttention for quantization
> Inserted 1155 quantizers
> Passing a tuple of `past_key_values` is deprecated and will be removed in Transformers v4.43.0. You should pass an instance of `EncoderDecoderCache` instead, e.g. `past_key_values=EncoderDecoderCache.from_legacy_cache(past_key_values)`.
> /usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py:552: UserWarning: Cannot export model to the model_config. The modelopt-optimized model state_dict (including the quantization factors) is saved to whisper_large_v3_weights_fp8/modelopt_model.0.pth using torch.save for further inspection.
>   warn(
> Traceback (most recent call last):
>   File "/app/tensorrt_llm/TensorRT-LLM/examples/models/core/whisper/../../../quantization/quantize.py", line 160, in <module>
>     quantize_and_export(
>   File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/quantization/quantize_by_modelopt.py", line 815, in quantize_and_export
>     export_tensorrt_llm_checkpoint(
>   File "/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py", line 557, in export_tensorrt_llm_checkpoint
>     raise e
>   File "/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py", line 488, in export_tensorrt_llm_checkpoint
>     for (
>   File "/usr/local/lib/python3.12/dist-packages/modelopt/torch/export/model_config_export.py", line 229, in torch_to_tensorrt_llm_checkpoint
>     assert compatible, "The model is not supported"
>            ^^^^^^^^^^
> AssertionError: The model is not supported
> ```
> 
> Here is the command I used:
> 
> ```
> python3 ../../../quantization/quantize.py         
>     --model_dir openai/whisper-large-v3
>     --qformat fp8
>     --output_dir ${checkpoint_dir}
>     --calib_dataset ./peoples_speech
>     --calib_size 100
> ```
> 
> I tried to use this Docker image to run the script: https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags
> 
> And this dataset: https://huggingface.co/datasets/MLCommons/peoples_speech/viewer/microset?views%5B%5D=microset
> 
> Could you maybe give me a clue of what am I doing wrong?

 @IooHooI You are using a cloned repo that contains my patch located at `/app/tensorrt_llm/TensorRT-LLM/` but it imports the installed TRT-LLM package installed at `/usr/local/lib/python3.12/dist-packages/tensorrt_llm/` which does not have the patch applied and thus the error

@SerhiiArtemuk you can use the conversion example from the v0.17.0 branch https://github.com/NVIDIA/TensorRT-LLM/tree/v0.17.0


### IooHooI · 2025-07-31

UPD:

I've tried to reproduce an [initial](https://github.com/NVIDIA/TensorRT-LLM/issues/5210#issue-3144474121) error with this Docker Image:
https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags

I used this version:
nvcr.io/nvidia/tensorrt-llm/release:0.20.0

And I could NOT reproduce an issue.

Apparently, it works correctly with TensorRT-LLM version 0.20.

I didn't try to do the same for v0.17.0, not needed for me at the moment.

### IooHooI · 2025-07-31

> @IooHooI You are using a cloned repo that contains my patch located at /app/tensorrt_llm/TensorRT-LLM/ but it imports the installed TRT-LLM package installed at /usr/local/lib/python3.12/dist-packages/tensorrt_llm/ which does not have the patch applied and thus the error

@MahmoudAshraf97, thanks for your comment!
I'll take a look =)

And probably wait until your PR is merged into upstream =))

### brnguyen2 · 2026-09-10

Closing this out as there has been no activity for >1y.
