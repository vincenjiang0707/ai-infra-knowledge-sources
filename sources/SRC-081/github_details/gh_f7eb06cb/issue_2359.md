# [Issue #2359] [BUG] self_attn.q_proj in Moonlight-16B-A3B (deepseek v3 arch) qweight is failed to quantized and save

source: https://github.com/ModelCloud/GPTQModel/issues/2359
state: closed | updated: 2026-01-15T05:24:20Z
labels: bug

## 正文

**Model/Datasets**
offical Moonlight-16B-A3B (deepseek v3 arch) , 

**Code**
```
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig  ## v5.7/v5.4

quant_method = "gptq"
model_id = args.model
quant_path = args.model.rstrip("/").split("/")[-1] + "-" + quant_method

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
).select(range(512))["text"]

quant_config = QuantizeConfig(
    bits=4, 
    group_size=128,
    quant_method=quant_method,
)

model = GPTQModel.load(model_id, quant_config, trust_remote_code=True)
model.quantize(calibration_dataset, batch_size=1)
model.save(quant_path)
```

**self_attn.q_proj qweight is failed to quantized, with no logs record in logs.**

When load with: 
```
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        device_map='auto',
        use_safetensors=True,
        trust_remote_code=True
    )

```
with output:
```
Skipping import of cpp extensions due to incompatible torch version 2.8.0+cu128 for torchao version 0.15.0             Please see https://github.com/pytorch/ao/issues/2919 for more info
Loading model:  model/moonlight-16b-a3b-gptq/
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
`torch_dtype` is deprecated! Use `dtype` instead!
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
/home/daodao/anaconda3/envs/cmoe311/lib/python3.11/site-packages/auto_gptq/nn_modules/triton_utils/kernels.py:410: FutureWarning: `torch.cuda.amp.custom_fwd(args...)` is deprecated. Please use `torch.amp.custom_fwd(args..., device_type='cuda')` instead.
  @custom_fwd
/home/daodao/anaconda3/envs/cmoe311/lib/python3.11/site-packages/auto_gptq/nn_modules/triton_utils/kernels.py:418: FutureWarning: `torch.cuda.amp.custom_bwd(args...)` is deprecated. Please use `torch.amp.custom_bwd(args..., device_type='cuda')` instead.
  @custom_bwd
/home/daodao/anaconda3/envs/cmoe311/lib/python3.11/site-packages/auto_gptq/nn_modules/triton_utils/kernels.py:461: FutureWarning: `torch.cuda.amp.custom_fwd(args...)` is deprecated. Please use `torch.amp.custom_fwd(args..., device_type='cuda')` instead.
  @custom_fwd(cast_inputs=torch.float16)
CUDA extension not installed.
CUDA extension not installed.

WARN  Python GIL is enabled: Multi-gpu quant acceleration for MoE models is sub-optimal and multi-core accelerated cpu packing is also disabled. We recommend Python >= 3.13.3t with Pytorch > 2.8 for mult-gpu quantization and multi-cpu packing with env `PYTHON_GIL=0`.
WARN  Feature `utils/Perplexity` requires Python < 3.14 and Python GIL enabled and Python >= 3.13.3T (T for Threading-Free edition of Python) plus Torch 2.8. Feature is currently skipped/disabled.
INFO  ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving.
INFO  ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.
INFO

_____/\\\\\\\\\\\\__/\\\\\\\\\\\\\____/\\\\\\\\\\\\\\\______________________/\\\________/\\\\____________/\\\\_______________________/\\\__________________/\\\\\\____
 ___/\\\//////////__\/\\\/////////\\\_\///////\\\/////____________________/\\\\/\\\\____\/\\\\\\________/\\\\\\______________________\/\\\_________________\////\\\____
  __/\\\_____________\/\\\_______\/\\\_______\/\\\_______________________/\\\//\////\\\__\/\\\//\\\____/\\\//\\\______________________\/\\\____________________\/\\\____
   _\/\\\____/\\\\\\\_\/\\\\\\\\\\\\\/________\/\\\________/\\\\\\\\\\\__/\\\______\//\\\_\/\\\\///\\\/\\\/_\/\\\_____/\\\\\___________\/\\\______/\\\\\\\\_____\/\\\____
    _\/\\\___\/////\\\_\/\\\/////////__________\/\\\_______\///////////__\//\\\______/\\\__\/\\\__\///\\\/___\/\\\___/\\\///\\\____/\\\\\\\\\____/\\\/////\\\____\/\\\____
     _\/\\\_______\/\\\_\/\\\___________________\/\\\______________________\///\\\\/\\\\/___\/\\\____\///_____\/\\\__/\\\__\//\\\__/\\\////\\\___/\\\\\\\\\\\_____\/\\\____
      _\/\\\_______\/\\\_\/\\\___________________\/\\\________________________\////\\\//_____\/\\\_____________\/\\\_\//\\\__/\\\__\/\\\__\/\\\__\//\\///////______\/\\\____
       _\//\\\\\\\\\\\\/__\/\\\___________________\/\\\___________________________\///\\\\\\__\/\\\_____________\/\\\__\///\\\\\/___\//\\\\\\\/\\__\//\\\\\\\\\\__/\\\\\\\\\_
        __\////////////____\///____________________\///______________________________\//////___\///______________\///_____\/////______\///////\//____\//////////__\/////////__

Detected gptqmodel and auto-gptq, will use gptqmodel
[W113 14:59:40.576446585 Context.cpp:320] Warning: torch.backends.cuda.preferred_linalg_library is an experimental feature. If you see any error or unexpected behavior when this flag is set please file an issue on GitHub. (function operator())
INFO  Kernel: Auto-selection: adding candidate `TorchQuantLinear`
INFO  Kernel: selected -> `TorchQuantLinear`.
`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
Detected gptqmodel and auto-gptq, will use gptqmodel
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████| 3/3 [00:02<00:00,  1.12it/s]
Some weights of the model checkpoint at model/Moonlight-16B-A3B-GPTQ/ were not used when initializing DeepseekV3ForCausalLM: ['model.layers.0.self_attn.q_proj.weight', 'model.layers.1.self_attn.q_proj.weight', 'model.layers.10.self_attn.q_proj.weight', 'model.layers.11.self_attn.q_proj.weight', 'model.layers.12.self_attn.q_proj.weight', 'model.layers.13.self_attn.q_proj.weight', 'model.layers.14.self_attn.q_proj.weight', 'model.layers.15.self_attn.q_proj.weight', 'model.layers.16.self_attn.q_proj.weight', 'model.layers.17.self_attn.q_proj.weight', 'model.layers.18.self_attn.q_proj.weight', 'model.layers.19.self_attn.q_proj.weight', 'model.layers.2.self_attn.q_proj.weight', 'model.layers.20.self_attn.q_proj.weight', 'model.layers.21.self_attn.q_proj.weight', 'model.layers.22.self_attn.q_proj.weight', 'model.layers.23.self_attn.q_proj.weight', 'model.layers.24.self_attn.q_proj.weight', 'model.layers.25.self_attn.q_proj.weight', 'model.layers.26.self_attn.q_proj.weight', 'model.layers.3.self_attn.q_proj.weight', 'model.layers.4.self_attn.q_proj.weight', 'model.layers.5.self_attn.q_proj.weight', 'model.layers.6.self_attn.q_proj.weight', 'model.layers.7.self_attn.q_proj.weight', 'model.layers.8.self_attn.q_proj.weight', 'model.layers.9.self_attn.q_proj.weight']
- This IS expected if you are initializing DeepseekV3ForCausalLM from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing DeepseekV3ForCausalLM from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Some weights of DeepseekV3ForCausalLM were not initialized from the model checkpoint at model/Moonlight-16B-A3B-GPTQ/ and are newly initialized: ['model.layers.0.self_attn.q_proj.g_idx', 'model.layers.0.self_attn.q_proj.qweight', 'model.layers.0.self_attn.q_proj.qzeros', 'model.layers.0.self_attn.q_proj.scales', 'model.layers.1.self_attn.q_proj.g_idx', 'model.layers.1.self_attn.q_proj.qweight', 'model.layers.1.self_attn.q_proj.qzeros', 'model.layers.1.self_attn.q_proj.scales', 'model.layers.10.self_attn.q_proj.g_idx', 'model.layers.10.self_attn.q_proj.qweight', 'model.layers.10.self_attn.q_proj.qzeros', 'model.layers.10.self_attn.q_proj.scales', 'model.layers.11.self_attn.q_proj.g_idx', 'model.layers.11.self_attn.q_proj.qweight', 'model.layers.11.self_attn.q_proj.qzeros', 'model.layers.11.self_attn.q_proj.scales', 'model.layers.12.self_attn.q_proj.g_idx', 'model.layers.12.self_attn.q_proj.qweight', 'model.layers.12.self_attn.q_proj.qzeros', 'model.layers.12.self_attn.q_proj.scales', 'model.layers.13.self_attn.q_proj.g_idx', 'model.layers.13.self_attn.q_proj.qweight', 'model.layers.13.self_attn.q_proj.qzeros', 'model.layers.13.self_attn.q_proj.scales', 'model.layers.14.self_attn.q_proj.g_idx', 'model.layers.14.self_attn.q_proj.qweight', 'model.layers.14.self_attn.q_proj.qzeros', 'model.layers.14.self_attn.q_proj.scales', 'model.layers.15.self_attn.q_proj.g_idx', 'model.layers.15.self_attn.q_proj.qweight', 'model.layers.15.self_attn.q_proj.qzeros', 'model.layers.15.self_attn.q_proj.scales', 'model.layers.16.self_attn.q_proj.g_idx', 'model.layers.16.self_attn.q_proj.qweight', 'model.layers.16.self_attn.q_proj.qzeros', 'model.layers.16.self_attn.q_proj.scales', 'model.layers.17.self_attn.q_proj.g_idx', 'model.layers.17.self_attn.q_proj.qweight', 'model.layers.17.self_attn.q_proj.qzeros', 'model.layers.17.self_attn.q_proj.scales', 'model.layers.18.self_attn.q_proj.g_idx', 'model.layers.18.self_attn.q_proj.qweight', 'model.layers.18.self_attn.q_proj.qzeros', 'model.layers.18.self_attn.q_proj.scales', 'model.layers.19.self_attn.q_proj.g_idx', 'model.layers.19.self_attn.q_proj.qweight', 'model.layers.19.self_attn.q_proj.qzeros', 'model.layers.19.self_attn.q_proj.scales', 'model.layers.2.self_attn.q_proj.g_idx', 'model.layers.2.self_attn.q_proj.qweight', 'model.layers.2.self_attn.q_proj.qzeros', 'model.layers.2.self_attn.q_proj.scales', 'model.layers.20.self_attn.q_proj.g_idx', 'model.layers.20.self_attn.q_proj.qweight', 'model.layers.20.self_attn.q_proj.qzeros', 'model.layers.20.self_attn.q_proj.scales', 'model.layers.21.self_attn.q_proj.g_idx', 'model.layers.21.self_attn.q_proj.qweight', 'model.layers.21.self_attn.q_proj.qzeros', 'model.layers.21.self_attn.q_proj.scales', 'model.layers.22.self_attn.q_proj.g_idx', 'model.layers.22.self_attn.q_proj.qweight', 'model.layers.22.self_attn.q_proj.qzeros', 'model.layers.22.self_attn.q_proj.scales', 'model.layers.23.self_attn.q_proj.g_idx', 'model.layers.23.self_attn.q_proj.qweight', 'model.layers.23.self_attn.q_proj.qzeros', 'model.layers.23.self_attn.q_proj.scales', 'model.layers.24.self_attn.q_proj.g_idx', 'model.layers.24.self_attn.q_proj.qweight', 'model.layers.24.self_attn.q_proj.qzeros', 'model.layers.24.self_attn.q_proj.scales', 'model.layers.25.self_attn.q_proj.g_idx', 'model.layers.25.self_attn.q_proj.qweight', 'model.layers.25.self_attn.q_proj.qzeros', 'model.layers.25.self_attn.q_proj.scales', 'model.layers.26.self_attn.q_proj.g_idx', 'model.layers.26.self_attn.q_proj.qweight', 'model.layers.26.self_attn.q_proj.qzeros', 'model.layers.26.self_attn.q_proj.scales', 'model.layers.3.self_attn.q_proj.g_idx', 'model.layers.3.self_attn.q_proj.qweight', 'model.layers.3.self_attn.q_proj.qzeros', 'model.layers.3.self_attn.q_proj.scales', 'model.layers.4.self_attn.q_proj.g_idx', 'model.layers.4.self_attn.q_proj.qweight', 'model.layers.4.self_attn.q_proj.qzeros', 'model.layers.4.self_attn.q_proj.scales', 'model.layers.5.self_attn.q_proj.g_idx', 'model.layers.5.self_attn.q_proj.qweight', 'model.layers.5.self_attn.q_proj.qzeros', 'model.layers.5.self_attn.q_proj.scales', 'model.layers.6.self_attn.q_proj.g_idx', 'model.layers.6.self_attn.q_proj.qweight', 'model.layers.6.self_attn.q_proj.qzeros', 'model.layers.6.self_attn.q_proj.scales', 'model.layers.7.self_attn.q_proj.g_idx', 'model.layers.7.self_attn.q_proj.qweight', 'model.layers.7.self_attn.q_proj.qzeros', 'model.layers.7.self_attn.q_proj.scales', 'model.layers.8.self_attn.q_proj.g_idx', 'model.layers.8.self_attn.q_proj.qweight', 'model.layers.8.self_attn.q_proj.qzeros', 'model.layers.8.self_attn.q_proj.scales', 'model.layers.9.self_attn.q_proj.g_idx', 'model.layers.9.self_attn.q_proj.qweight', 'model.layers.9.self_attn.q_proj.qzeros', 'model.layers.9.self_attn.q_proj.scales']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
The module name  (originally ) is not a valid Python identifier. Please rename the original module to avoid import issues.
INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/hqdpgrum-rkaakpxx/`
INFO  Format: Converting `checkpoint_format` from `FORMAT.GPTQ` to internal `FORMAT.GPTQ_V2`.
INFO  Format: Converting GPTQ v1 to v2
INFO  Optimize: `TorchQuantLinear` compilation triggered.
INFO  gc.collect() reclaimed 52 objects in 0.302s
```

and model.layers.*.self_attn.q_proj.qweight  is float16 instead of int32, with 0, while other qweights like o_proj.qweight is int32 with real data.



## 评论 (3)

### Qubitium · 2026-01-14

@zzningxp 

What git commit version of main did you use? Can you provide the quant logs?

Also what version of transformers?

### zzningxp · 2026-01-15

I tried multi version of GPTQModel, like #2358, v4.2.5, v5.6, v5.4, all of which meet the same bug.
And the version of transformers is 4.57.5.

### zzningxp · 2026-01-15

Here are some of the quant logs, which is without self_attn.q_proj module.

```
{
    "process": "gptq",
    "layer": 0,
    "module": "self_attn.kv_a_proj_with_mqa",
    "loss": "0.0000028594",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.336",
    "fwd_time": "1.318",
    "max_vram": "196.90MB, 0.00MB"
}
{
    "process": "gptq",
    "layer": 0,
    "module": "self_attn.kv_b_proj",
    "loss": "0.0000031504",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.052",
    "fwd_time": "1.000",
    "max_vram": "198.81MB, 0.00MB"
}
{
    "process": "gptq",
    "layer": 0,
    "module": "self_attn.o_proj",
    "loss": "0.0000000024",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.221",
    "fwd_time": "1.047",
    "max_vram": "203.05MB, 0.00MB"
}
{
    "process": "gptq",
    "layer": 0,
    "module": "mlp.up_proj",
    "loss": "0.0000012301",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.335",
    "fwd_time": "1.156",
    "max_vram": "575.97MB, 17.72MB"
}
{
    "process": "gptq",
    "layer": 0,
    "module": "mlp.gate_proj",
    "loss": "0.0000012628",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.345",
    "fwd_time": "1.156",
    "max_vram": "240.50MB, 17.63MB"
}
{
    "process": "gptq",
    "layer": 0,
    "module": "mlp.down_proj",
    "loss": "0.0000000040",
    "samples": "219553",
    "damp": "0.05000",
    "time": "1.132",
    "fwd_time": "2.605",
    "max_vram": "241.85MB, 17.63MB"
}
{
    "process": "gptq",
    "layer": 1,
    "module": "self_attn.kv_a_proj_with_mqa",
    "loss": "0.0000013720",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.178",
    "fwd_time": "2.444",
    "max_vram": "2052.88MB, 17.63MB"
}
{
    "process": "gptq",
    "layer": 1,
    "module": "self_attn.kv_b_proj",
    "loss": "0.0000020618",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.047",
    "fwd_time": "2.368",
    "max_vram": "2054.32MB, 17.63MB"
}
{
    "process": "gptq",
    "layer": 1,
    "module": "self_attn.o_proj",
    "loss": "0.0000000088",
    "samples": "219553",
    "damp": "0.05000",
    "time": "0.178",
    "fwd_time": "2.415",
    "max_vram": "2059.02MB, 17.63MB"
}

```
