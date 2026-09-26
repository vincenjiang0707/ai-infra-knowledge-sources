# [Issue #1681] GPT-OSS supported?

source: https://github.com/ModelCloud/GPTQModel/issues/1681
state: closed | updated: 2025-12-19T00:39:32Z
labels: model

## 正文

Will this series be supported?

## 评论 (11)

### liuqianchao · 2025-08-14

+1, such as mxfp4 quantization after finetune the model and got fp16 weights

### Qubitium · 2025-08-19

We are checking since the model appears to already use MXFP4 for qunatization so for it to go through gptqmodel we need to first decompress it bf16 or fp16.

@liuqianchao So you finetuned gpt-oss and in final `model.save` you passed FP16 as weight format option correct?

### xiaotianns · 2025-08-22

> We are checking since the model appears to already use MXFP4 for qunatization so for it to go through gptqmodel we need to first decompress it bf16 or fp16.
> 
> [@liuqianchao](https://github.com/liuqianchao) So you finetuned gpt-oss and in final `model.save` you passed FP16 as weight format option correct?

Can the quantization of GPT-OSS with BF16 precision to INT8 precision be achieved? I have tried to do so but have not succeeded

### Qubitium · 2025-08-22

@xiaotianns  Yes. First we can need to decompress eveyrthing to BF16 and than requantize down to INT8 or INT4. 

Do you have an script to decompres the MXFP4 model to BF16? I am sure someone has aready written a script for it. 

### Qubitium · 2025-08-25

Use `unsloth/gpt-oss-20b-BF16` for bf15 version of gpt-oss but we are running into issue where the modeling code is puting some the modules as `nn.Parameters` instead of expected `nn.Linear` types. We need to find a workaround as our current module scanning/looper code does not handle `nn.Parameters`. 

### xiaotianns · 2025-08-25

> Use `unsloth/gpt-oss-20b-BF16` for bf15 version of gpt-oss but we are running into issue where the modeling code is puting some the modules as `nn.Parameters` instead of expected `nn.Linear` types. We need to find a workaround as our current module scanning/looper code does not handle `nn.Parameters`.
When we quantize the accuracy of BF16's GPT OSS to INT8, using version 2.2.0 of the GPT qmodel will prompt that GPT OSS is not supported. Changing to the latest version 4.0.0 of the GPT qmodel can solve this problem?


### xiaotianns · 2025-08-25

> Use `unsloth/gpt-oss-20b-BF16` for bf15 version of gpt-oss but we are running into issue where the modeling code is puting some the modules as `nn.Parameters` instead of expected `nn.Linear` types. We need to find a workaround as our current module scanning/looper code does not handle `nn.Parameters`.

I tried to update the gptqmodel to 4.0.0, but still received a prompt stating that gpt oss is not supported. Can we only wait for you to update the gptqmodel to quantify the gpt oss of BF16

<img width="1482" height="90" alt="Image" src="https://github.com/user-attachments/assets/870dcda0-1db2-4aee-80c4-4e7087491032" />

### Qubitium · 2025-08-25

@xiaotianns  gpt-oss is not yet supported. I am just updating on the progress in this thread on what we are finding. No code has been added to enable gpt-oss yet. 

### Qubitium · 2025-08-25

Once we fix llama-4 support, which has similar issues to gpt-oss, we should be able to add gpt-oss easily. 

Tracking: https://github.com/ModelCloud/GPTQModel/pull/1508

### Qubitium · 2025-09-02

Closed with PR #1737

### farzadab · 2025-12-19

Is there a minimal example of running quantization for GPT OSS?

I tried the basic script and I keep running into issues:
```python
import datasets
import gptqmodel

model_id = "openai/gpt-oss-20b"
quant_path = "gpt-oss-everything-4bit"

calibration_dataset = datasets.load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  ).select(range(1024))["text"]

quant_config = gptqmodel.QuantizeConfig(bits=4, group_size=32, gptaq=True)

model = gptqmodel.GPTQModel.load(model_id, quant_config)
model.quantize(calibration_dataset, batch_size=1)

model.save(quant_path)
```

I originally ran into some issues saying `Mxfp4Config` doesn't have `.get`. After adding a workaround for that now I see issues with the weights being on the `meta` device:
```
...
  File "/ElastiCore/projects/mltest/.venv/lib/python3.13/site-packages/gptqmodel/looper/stage_inputs_capture.py", line 132, in cache_inputs
    layers[0] = layers[0].to(self.gptq_model.quantize_config.device)
                ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/ElastiCore/projects/mltest/.venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1371, in to
    return self._apply(convert)
           ~~~~~~~~~~~^^^^^^^^^
  File "/ElastiCore/projects/mltest/.venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
    ~~~~~~~~~~~~~^^^^
  File "/ElastiCore/projects/mltest/.venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 930, in _apply
    module._apply(fn)
    ~~~~~~~~~~~~~^^^^
  File "/ElastiCore/projects/mltest/.venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 957, in _apply
    param_applied = fn(param)
  File "/ElastiCore/projects/mltest/.venv/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1364, in convert
    raise NotImplementedError(
    ...<2 lines>...
    ) from None
NotImplementedError: Cannot copy out of meta tensor; no data! Please use torch.nn.Module.to_empty() instead of torch.nn.Module.to() when moving module from meta to a different device.
```

Package versions:
```
gptqmodel: 5.6.12
torch: 2.9.0+cu128
transformers: 4.57.1
```
