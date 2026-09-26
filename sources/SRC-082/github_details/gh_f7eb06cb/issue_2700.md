# [Issue #2700] Quantized Qwen3.5-MoE seems to have stopped

source: https://github.com/ModelCloud/GPTQModel/issues/2700
state: closed | updated: 2026-04-16T12:36:55Z
labels: 

## 正文

When I follow the instruction to quantize qwen3.5-MoE (35B), the time required seems unusual; the quantification process appears to have stalled.

My code:
from datasets import load_dataset
from gptqmodel import QuantizeConfig, GPTQModel

model_id = "/data/models/Qwen/Qwen3.5-35B-A3B"
quant_path = "Qwen3.5-35B-A3B-GPTQ-Int4"

local_file_path = "c4-train.00001-of-01024.json.gz"

calibration_dataset = load_dataset(
    "json", 
    data_files=local_file_path, 
    split="train"
).select(range(512))["text"]

quant_config = QuantizeConfig(bits=4, group_size=128)

model = GPTQModel.load(model_id, quant_config)

model.quantize(calibration_dataset, batch_size=1)

model.save(quant_path)

My Environment:
GPT-QModel   : 5.8.0
Transformers : 5.5.0
Torch        : 2.10.0+cu128
Triton       : 3.6.0

The time consuming:
Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:15 / 1 day, 14:45:00 [2/40] 5.0%
> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
Forward replay (layer=`model.language_model.layers.1`, batches=512, rows=512) Forward replay rows 241/512 █████████████████████████���████████████████████▏░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:06:16 / 0:13:18 [241/512] 47.> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
Forward replay (layer=`model.language_model.layers.1`, batches=512, rows=512) Forward replay rows 242/512 ██████████████████████████████████████████████▎░░░░░░░░��░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:06:16 / 0:13:15 [242/512] 47.3> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░��░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
> Quantizing mlp.shared_expert.down_proj in layer ['p' to ||] [1 of 39] ██████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░���░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 1:56:17 / 1 day, 14:45:40 [2/40] 5.0%
Forward replay (layer=`model.language_model.layers.1`, batches=512, rows=512) Forward replay rows 248/512 ███████████████████████████████████████████████▍░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:06:16 / 0:12:56 [248/512] 48.4%


## 评论 (4)

### Qubitium · 2026-04-09

@IAN-YE  Use latest `main` branch and make sure it works on 1 gpu before give it move than 1 gpu. > 1 gpu is only supported with PYTHON_GIL=0 and and nogil enabled Python. 

### ZX-ModelCloud · 2026-04-10

I was unable to reproduce this issue in GPT-QModel 5.8.0 using the code provided. `qwen3_5_moe` quantizes successfully.

Please provide more information—for example, your Python environment, the GPU model and quantity you are using, etc.

### Qubitium · 2026-04-12

@IAN-YE  Unless we get more debugging data, I need to close this off. 

### Qubitium · 2026-04-16

@IAN-YE  I have just fixed a threading race that may have caused the `deadlock` in your quantization. 

https://github.com/ModelCloud/GPTQModel/pull/2749
