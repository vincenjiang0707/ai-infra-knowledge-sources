# [Issue #10] 使用NPU+Pytorch2.1.0+SFTTrainer训练时tensor未完全加载于NPU

source: https://github.com/Ascend/pytorch/issues/10
state: open | updated: 2024-12-11T06:08:56Z
labels: 

## 正文

在使用如下代码使用NPU训练LLaMA模型时，在执行trainer.train()时报错。
代码如下：

```
import os
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer
import torch
import torch_npu

from accelerate import Accelerator
accelerator = Accelerator()

device_map = accelerator.device

# source '/home/HwHiAiUser/Ascend/ascend-toolkit/set_env.sh'

x = torch.randn(2, 2).npu()
y = torch.randn(2, 2).npu()
z = x.mm(y)

print(z)
print(device_map)

# The model that you want to train from the Hugging Face hub
model_name = "/home/HwHiAiUser/Code/model/llama-3b"

# The instruction dataset to use
dataset_name = "/home/HwHiAiUser/Code"

# Fine-tuned model name
new_model = "llama-3b-NPU"

################################################################################
# QLoRA parameters
################################################################################

# LoRA attention dimension
lora_r = 64

# Alpha parameter for LoRA scaling
lora_alpha = 16

# Dropout probability for LoRA layers
lora_dropout = 0.1

################################################################################
# bitsandbytes parameters
################################################################################

# Activate 4-bit precision base model loading
use_4bit = True

# Compute dtype for 4-bit base models
bnb_4bit_compute_dtype = "float16"

# Quantization type (fp4 or nf4)
bnb_4bit_quant_type = "nf4"

# Activate nested quantization for 4-bit base models (double quantization)
use_nested_quant = False

################################################################################
# TrainingArguments parameters
################################################################################

# Output directory where the model predictions and checkpoints will be stored
output_dir = "./results"

# Number of training epochs
num_train_epochs = 10

# Enable fp16/bf16 training (set bf16 to True with an A100)
fp16 = False
bf16 = False

# Batch size per GPU for training
per_device_train_batch_size = 5

# Batch size per GPU for evaluation
per_device_eval_batch_size = 5

# Number of update steps to accumulate the gradients for
gradient_accumulation_steps = 5

# Enable gradient checkpointing
gradient_checkpointing = True

# Maximum gradient normal (gradient clipping)
max_grad_norm = 0.3

# Initial learning rate (AdamW optimizer)
learning_rate = 2e-4

# Weight decay to apply to all layers except bias/LayerNorm weights
weight_decay = 0.001

# Optimizer to use
optim = "paged_adamw_32bit"

# Learning rate schedule (constant a bit better than cosine)
lr_scheduler_type = "constant"

# Number of training steps (overrides num_train_epochs)
max_steps = -1

# Ratio of steps for a linear warmup (from 0 to learning rate)
warmup_ratio = 0.03

# Group sequences into batches with same length
# Saves memory and speeds up training considerably
group_by_length = True

# Save checkpoint every X updates steps
save_steps = 50

# Log every X updates steps
logging_steps = 50

################################################################################
# SFT parameters
################################################################################

# Maximum sequence length to use
max_seq_length = None

# Pack multiple short examples in the same input sequence to increase efficiency
packing = False

# Load dataset (you can process it here)
dataset = load_dataset(dataset_name, split="train")

# Load tokenizer and model with QLoRA configuration
compute_dtype = getattr(torch, bnb_4bit_compute_dtype)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=use_4bit,
    bnb_4bit_quant_type=bnb_4bit_quant_type,
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=use_nested_quant,
)


# Load base model

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    # torch_dtype=torch.float16,
    # quantization_config=bnb_config,
    trust_remote_code=True,
    device_map=device_map
)
model.config.use_cache = False
model.config.pretraining_tp = 1

# Load LLaMA tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    model_name, use_fast=False, trust_remote_code=True,
    device_map=device_map)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"  # Fix weird overflow issue with fp16 training

 # Load LoRA configuration
peft_config = LoraConfig(
    lora_alpha=lora_alpha,
    lora_dropout=lora_dropout,
    r=lora_r,
    bias="none",
    task_type="CAUSAL_LM",
)

# Set training parameters
training_arguments = TrainingArguments(
    output_dir=output_dir,
    num_train_epochs=num_train_epochs,
    per_device_train_batch_size=per_device_train_batch_size,
    gradient_accumulation_steps=gradient_accumulation_steps,
    optim=optim,
    save_steps=save_steps,
    logging_steps=logging_steps,
    learning_rate=learning_rate,
    weight_decay=weight_decay,
    fp16=fp16,
    bf16=bf16,
    max_grad_norm=max_grad_norm,
    max_steps=max_steps,
    warmup_ratio=warmup_ratio,
    group_by_length=group_by_length,
    lr_scheduler_type=lr_scheduler_type,
    report_to="tensorboard"
)

# Set supervised fine-tuning parameters
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    tokenizer=tokenizer,
    args=training_arguments,
    packing=packing,
)

# Train model
trainer.train()

# Save trained model
trainer.model.save_pretrained(new_model)

```
报错信息如下：

```
发生异常: RuntimeError
Expected all tensors to be on the same device. Expected NPU tensor, please check whether the input tensor device is correct.
  File "/home/HwHiAiUser/Code/main.py", line 212, in <module>
    trainer.train()
RuntimeError: Expected all tensors to be on the same device. Expected NPU tensor, please check whether the input tensor device is correct.
```


```
(NPU) [HwHiAiUser@localhost Code]$  cd /home/HwHiAiUser/Code ; /usr/bin/env /home/HwHiAiUser/下载/yes/envs/NPU/bin/python /home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher 41483 -- /home/HwHiAiUser/Code/main.py
/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/bitsandbytes/cextension.py:34: UserWarning: The installed version of bitsandbytes was compiled without GPU support. 8-bit optimizers, 8-bit multiplication, and GPU quantization are unavailable.
  warn("The installed version of bitsandbytes was compiled without GPU support. "
/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/bitsandbytes/libbitsandbytes_cpu.so: undefined symbol: cadam32bit_grad_fp32
Warning: Device do not support double dtype now, dtype cast repalce with float.
tensor([[-1.1986,  0.8204],
        [-1.6992,  1.1416]], device='npu:0')
npu
You are using the legacy behaviour of the <class 'transformers.models.llama.tokenization_llama.LlamaTokenizer'>. This means that tokens that come after special tokens will not be properly handled. We recommend you to read the related pull request available at https://github.com/huggingface/transformers/pull/24565
/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/trl/trainer/sft_trainer.py:159: UserWarning: You didn't pass a `max_seq_length` argument to the SFTTrainer, this will default to 1024
  warnings.warn(
Map: 100%|███████████| 122606/122606 [03:51<00:00, 529.37 examples/s]
  0%|                                      | 0/49040 [00:00<?, ?it/s]Traceback (most recent call last):
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 39, in <module>
    cli.main()
  File "/home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 430, in main
    run()
  File "/home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 284, in run_file
    runpy.run_path(target, run_name="__main__")
  File "/home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 321, in run_path
    return _run_module_code(code, init_globals, run_name,
  File "/home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 135, in _run_module_code
    _run_code(code, mod_globals, init_globals,
  File "/home/HwHiAiUser/.vscode/extensions/ms-python.python-2023.18.0/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 124, in _run_code
    exec(code, run_globals)
  File "/home/HwHiAiUser/Code/main.py", line 212, in <module>
    trainer.train()
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/transformers/trainer.py", line 1539, in train
    return inner_training_loop(
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/transformers/trainer.py", line 1809, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/transformers/trainer.py", line 2654, in training_step
    loss = self.compute_loss(model, inputs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/transformers/trainer.py", line 2679, in compute_loss
    outputs = model(**inputs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/peft/peft_model.py", line 922, in forward
    return self.base_model(
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/transformers/models/llama/modeling_llama.py", line 806, in forward
    outputs = self.model(
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/transformers/models/llama/modeling_llama.py", line 646, in forward
    inputs_embeds = self.embed_tokens(input_ids)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/modules/sparse.py", line 162, in forward
    return F.embedding(
  File "/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/site-packages/torch/nn/functional.py", line 2233, in embedding
    return torch.embedding(weight, input, padding_idx, scale_grad_by_freq, sparse)
RuntimeError: Expected all tensors to be on the same device. Expected NPU tensor, please check whether the input tensor device is correct.
/home/HwHiAiUser/下载/yes/envs/NPU/lib/python3.9/tempfile.py:821: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/tmpi3_cfqya'>
  _warnings.warn(warn_message, ResourceWarning)
  0%|          | 0/49040 [1:41:42<?, ?it/s]                          
(NPU) [HwHiAiUser@localhost Code]$

```

### 环境信息
**固件版本检查**
```
(NPU) [HwHiAiUser@localhost ~]$ sudo /usr/local/Ascend/driver/tools/upgrade-tool --device_index -1 --component -1 --version
{
Get component version(6.4.12.1.241) succeed for deviceId(0), componentType(11).
	{"device_id":0, "component":hboot1a, "version":6.4.12.1.241}
Get component version(6.4.12.1.241) succeed for deviceId(0), componentType(12).
	{"device_id":0, "component":hboot1b, "version":6.4.12.1.241}
Get component version(6.4.12.1.241) succeed for deviceId(0), componentType(18).
	{"device_id":0, "component":hlink, "version":6.4.12.1.241}
}
```
**npu-smi info**
```
(NPU) [HwHiAiUser@localhost ~]$ npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 23.0.rc2                                 Version: 23.0.rc2                                     |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 8       310P3                 | OK              | NA           37                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1700 / 21527                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 8                                                                    |
+===============================+=================+======================================================+

```
**CANN安装**
已安装适应pytorch2.1.0版本的CANN7.0.RC1.alpha003，并且环境配置正确，如下代码运行正常：
```
import torch
import torch_npu

# source '/home/HwHiAiUser/Ascend/ascend-toolkit/set_env.sh'

x = torch.randn(2, 2).npu()
y = torch.randn(2, 2).npu()
z = x.mm(y)

print(z)
```
运行结果：
```
(NPU) (base) [HwHiAiUser@bogon Code]$ /home/HwHiAiUser/下载/yes/envs/NPU/bin/python /home/HwHiAiUser/Code/main.py
Warning: Device do not support double dtype now, dtype cast repalce with float.
tensor([[ 0.0766,  0.2028],
        [-2.3419, -1.6132]], device='npu:0')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/5ef3c6dc62c44b8b87843ecba3ddbfc4.png)

```
(NPU) [HwHiAiUser@localhost ~]$ pip list
Package            Version
------------------ ------------
absl-py            2.0.0
accelerate         0.21.0
aiohttp            3.8.6
aiosignal          1.3.1
ascendctools       0.1.0
asttokens          2.4.0
async-timeout      4.0.3
attrs              23.1.0
auto-tune          0.1.0
backcall           0.2.0
bitsandbytes       0.40.2
certifi            2022.12.7
cffi               1.16.0
charset-normalizer 2.1.1
comm               0.1.4
dataflow           0.0.1
datasets           2.14.6
decorator          5.1.1
dill               0.3.7
exceptiongroup     1.1.3
executing          2.0.0
filelock           3.9.0
frozenlist         1.4.0
fsspec             2023.10.0
hccl               0.1.0
hccl-parser        0.1
huggingface-hub    0.18.0
idna               3.4
ipython            8.16.1
ipywidgets         8.1.1
jedi               0.19.1
Jinja2             3.1.2
jupyterlab-widgets 3.0.9
MarkupSafe         2.1.2
matplotlib-inline  0.1.6
mpmath             1.3.0
msadvisor          1.0.0
multidict          6.0.4
multiprocess       0.70.15
networkx           3.0
numpy              1.24.1
op-gen             0.1
op-test-frame      0.1
opc-tool           0.1.0
packaging          23.2
pandas             2.1.1
parso              0.8.3
pathlib2           2.3.7.post1
peft               0.4.0
pexpect            4.8.0
pickleshare        0.7.5
Pillow             9.3.0
pip                23.3
prompt-toolkit     3.0.39
protobuf           3.20.1
psutil             5.9.6
ptyprocess         0.7.0
pure-eval          0.2.2
pyarrow            13.0.0
pycparser          2.21
Pygments           2.16.1
python-dateutil    2.8.2
pytz               2023.3.post1
PyYAML             6.0.1
regex              2023.10.3
requests           2.28.1
safetensors        0.4.0
schedule-search    0.0.1
scipy              1.11.3
sentencepiece      0.1.99
setuptools         68.0.0
six                1.16.0
stack-data         0.6.3
sympy              1.12
te                 0.4.0
tensorboardX       2.6.2.2
tokenizers         0.13.3
torch              2.1.0+cpu
torch-npu          2.1.0rc1
torchaudio         2.1.0+cpu
torchvision        0.16.0+cpu
tqdm               4.66.1
traitlets          5.11.2
transformers       4.31.0
trl                0.4.7
typing_extensions  4.4.0
tzdata             2023.3
urllib3            1.26.13
wcwidth            0.2.8
wheel              0.41.2
widgetsnbextension 4.0.9
xxhash             3.4.1
yarl               1.9.2
WARNING: There was an error checking the latest version of pip.
```


## 评论 (4)

### ji-huazhong · 2023-10-31

FYI, bitsandbytes相关的能力不支持@DataLynnAI

### JunkRoy · 2023-11-14

请问如何获取CANN7.0.RC1的版本的驱动呢

### Matthewlliu · 2024-11-26

请问现在解决了吗，我在昇腾910B上也跑不通和这个类似的lora训练代码，只是训练会卡在0%一动不动没有报错

### KoalaYan · 2024-12-11

```
(fedllm) root@kuntai05:/home/peishenyan/code/FedLLM# bash training_scripts/FedAya/aya_all.sh 
/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/bitsandbytes/cextension.py:34: UserWarning: The installed version of bitsandbytes was compiled without GPU support. 8-bit optimizers, 8-bit multiplication, and GPU quantization are unavailable.
  warn("The installed version of bitsandbytes was compiled without GPU support. "
'NoneType' object has no attribute 'cadam32bit_grad_fp32'
ScriptArguments(model_name_or_path='../Llama-2-7b-hf/', dataset_name='FedAya', log_with='none', learning_rate=2e-05, batch_size=2, seq_length=1024, gradient_accumulation_steps=4, load_in_8bit=True, load_in_4bit=False, use_peft=True, trust_remote_code=False, output_dir='./models/FedAya-Llama2//FedAya_25000_fedavg_c38s4_i10_b2a4_l1024_r16a32_20241211112327', peft_lora_r=16, peft_lora_alpha=32, logging_steps=100, use_auth_token=False, num_train_epochs=3, max_steps=10, save_steps=1000, save_total_limit=10, push_to_hub=False, hub_model_id=None, gradient_checkpointing=True, template='alpaca', seed=2023, dpo_beta=0.1, dataset_sample=25000, local_data_dir='data/Fed-Aya/aya_38c_25k.json', multi_turn_task=False, dynamic_local_step=False, dp_max_grad_norm=1.0, dp_delta=0.0001, dp_epsilon=1.0, dp_sigma=None) FedArguments(fed_alg='fedavg', num_rounds=200, checkpoint_step=50, num_clients=38, sample_clients=4, split_strategy='iid', prox_mu=0.01, fedopt_tau=0.001, fedopt_eta=0.001, fedopt_beta1=0.5, fedopt_beta2=0.99)
[421, 1576, 5016, 418, 1555, 365, 783, 935, 1223, 795, 516, 476, 447, 614, 361, 1363, 298, 1418, 809, 192, 493, 289, 194, 139, 235, 209, 347, 713, 533, 417, 175, 492, 271, 418, 293, 223, 270, 221]
38
/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch_npu/utils/storage.py:38: UserWarning: TypedStorage is deprecated. It will be removed in the future and UntypedStorage will be the only storage class. This should only matter to you if you are using storages directly.  To access UntypedStorage directly, use tensor.untyped_storage() instead of tensor.storage()
  if self.device.type != 'cpu':
Loading checkpoint shards: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:11<00:00,  5.52s/it]
trainable params: 8,388,608 || all params: 6,746,804,224 || trainable%: 0.12433454005023165
Using pad_token, but it is not set yet.
  0%|                                                                                                                                                                             | 0/200 [00:00<?, ?it/s]>> ==================== Round 1 : [2, 16, 24, 26] ====================
number to sample: 80
                                                         /home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/optimization.py:411: FutureWarning: This implementation of AdamW is deprecated and will be removed in a future version. Use the PyTorch implementation torch.optim.AdamW instead, or set `no_deprecation_warning=True` to disable this warning
  warnings.warn(
                                                         `use_cache=True` is incompatible with gradient checkpointing. Setting `use_cache=False`...                                                                                          | 0/10 [00:00<?, ?it/s]
/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py:600: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. In version 2.4 we will raise an exception if use_reentrant is not passed. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)
  0%|                                                                                                                                                                             | 0/200 [00:01<?, ?it/s]
Traceback (most recent call last):
  File "/home/peishenyan/code/FedLLM/main_sft.py", line 133, in <module>
    results = trainer.train()
              ^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/trainer.py", line 1539, in train
    return inner_training_loop(
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/trainer.py", line 1809, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/trainer.py", line 2654, in training_step
    loss = self.compute_loss(model, inputs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/trainer.py", line 2679, in compute_loss
    outputs = model(**inputs)
              ^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/peft/peft_model.py", line 922, in forward
    return self.base_model(
           ^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 806, in forward
    outputs = self.model(
              ^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 685, in forward
    layer_outputs = torch.utils.checkpoint.checkpoint(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/_compile.py", line 31, in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 600, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/utils/checkpoint.py", line 481, in checkpoint
    return CheckpointFunction.apply(function, preserve, *args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/autograd/function.py", line 574, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/utils/checkpoint.py", line 255, in forward
    outputs = run_function(*args)
              ^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 681, in custom_forward
    return module(*inputs, output_attentions, None)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 408, in forward
    hidden_states, self_attn_weights, present_key_value = self.self_attn(
                                                          ^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/accelerate/hooks.py", line 165, in new_forward
    output = old_forward(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 305, in forward
    query_states = self.q_proj(hidden_states)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/peft/tuners/lora.py", line 1064, in forward
    result = super().forward(x)
             ^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/bitsandbytes/nn/modules.py", line 414, in forward
    out = bnb.matmul(x, self.weight, bias=self.bias, state=self.state)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/bitsandbytes/autograd/_functions.py", line 563, in matmul
    return MatMul8bitLt.apply(A, B, out, bias, state)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/autograd/function.py", line 574, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/bitsandbytes/autograd/_functions.py", line 297, in forward
    using_igemmlt = supports_igemmlt(A.device) and not state.force_no_igemmlt
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/bitsandbytes/autograd/_functions.py", line 227, in supports_igemmlt
    if torch.cuda.get_device_capability(device=device) < (7, 5):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/cuda/__init__.py", line 451, in get_device_capability
    prop = get_device_properties(device)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/cuda/__init__.py", line 465, in get_device_properties
    _lazy_init()  # will define _get_device_properties
    ^^^^^^^^^^^^
  File "/home/peishenyan/miniconda3/envs/fedllm/lib/python3.11/site-packages/torch/cuda/__init__.py", line 305, in _lazy_init
    raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
[ERROR] 2024-12-11-11:23:51 (PID:471812, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
  0%|          | 0/10 [00:01<?, ?it/s]  
```

Looks like similar situation...

bitsandbytes still does not support?
