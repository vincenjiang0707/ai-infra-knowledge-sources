# [Issue #85] Why medusa-2 train llama2 with no such great improvement?

source: https://github.com/FasterDecoding/Medusa/issues/85
state: open | updated: 2026-01-06T06:03:17Z
labels: 

## 正文

In the given examples  axoltol [exmaples/medusa](https://github.com/ctlllll/axolotl/tree/main/examples/medusa),
I follow the `vicuna_7b_qlora_stage1.yml` and `vicuna_7b_qlora_stage2.yml` to write my llama2 trainning config.

Howerver I did't get such greate performance improvement, below is my test results with different tokens generation in A100
![image](https://github.com/FasterDecoding/Medusa/assets/53092165/2092b341-5821-4da3-9350-142d21090bf6)

Then I use official vicuna-7b medusa2 weigths, it does work.
![image](https://github.com/FasterDecoding/Medusa/assets/53092165/e5081313-d4ba-425d-92f8-2738a6c9d972)

So here I want to know what's the difference ?  Is my training config fault.


## 评论 (3)

### MeJerry215 · 2024-02-26

@ctlllll 

and here is my training config `llama2_7b_stage1.yml`
```yml
base_model: Llama-2-7b-hf
base_model_config: Llama-2-7b-hf
model_type: LlamaForCausalLM
tokenizer_type: LlamaTokenizer
is_llama_derived_model: true

load_in_8bit: false
load_in_4bit: true
strict: false

datasets:
  - path: ./ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json
    type: sharegpt
dataset_prepared_path:
val_set_size: 0.01
output_dir: ./Llama2_7b_qlora_stage1

adapter: qlora
lora_model_dir:

lora_r: 32
lora_alpha: 16
lora_dropout: 0.05
lora_target_modules:
  - gate_proj
  - down_proj
  - up_proj
  - q_proj
  - v_proj
  - k_proj
  - o_proj
  - lm_head
lora_target_linear:
lora_fan_in_fan_out:
lora_modules_to_save:

sequence_len: 4096
sample_packing: true
pad_to_sequence_len: true

wandb_project:
wandb_entity:
wandb_watch:
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 4
micro_batch_size: 2
num_epochs: 2
optimizer: adamw_bnb_8bit
lr_scheduler: cosine
learning_rate: 0.0005

train_on_inputs: false
group_by_length: false
bf16: true
fp16: false
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 40
eval_steps: 40
save_steps:
save_total_limit: 1
debug:
deepspeed:
weight_decay: 0.0
fsdp:
fsdp_config:
special_tokens:
  bos_token: "<s>"
  eos_token: "</s>"
  unk_token: "<unk>"

medusa_num_heads: 5
medusa_num_layers: 1
medusa_heads_coefficient: 0.2
medusa_decay_coefficient: 0.8
medusa_logging: true
medusa_scheduler: constant
medusa_lr_multiplier: 4.0
medusa_only_heads: true
ddp_find_unused_parameters: true
# Stage 1: only train the medusa heads
# Stage 2: train the whole model

```

`llama2_7b_stage2.yml`.

```yml
base_model: Llama-2-7b-hf
base_model_config: Llama-2-7b-hf
model_type: LlamaForCausalLM
tokenizer_type: LlamaTokenizer
is_llama_derived_model: true

load_in_8bit: false
load_in_4bit: true
strict: false

datasets:
  - path: ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json
    type: sharegpt
dataset_prepared_path:
val_set_size: 0.01
output_dir: ./Llama2_7b_qlora_stage2

adapter: qlora
lora_model_dir:

lora_r: 32
lora_alpha: 16
lora_dropout: 0.05
lora_target_modules:
  - gate_proj
  - down_proj
  - up_proj
  - q_proj
  - v_proj
  - k_proj
  - o_proj
  - lm_head
lora_target_linear:
lora_fan_in_fan_out:
lora_modules_to_save:
lora_model_dir: ./Llama2_7b_qlora_stage1

sequence_len: 4096
sample_packing: true
pad_to_sequence_len: true

wandb_project:
wandb_entity:
wandb_watch:
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 4
micro_batch_size: 2
num_epochs: 2
optimizer: adamw_bnb_8bit
lr_scheduler: cosine
learning_rate: 0.0005

train_on_inputs: false
group_by_length: false
bf16: true
fp16: false
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 40
eval_steps: 40
save_steps:
save_total_limit: 1
debug:
deepspeed:
weight_decay: 0.0
fsdp:
fsdp_config:
special_tokens:
  bos_token: "<s>"
  eos_token: "</s>"
  unk_token: "<unk>"

medusa_num_heads: 5
medusa_num_layers: 1
medusa_heads_coefficient: 0.2
medusa_decay_coefficient: 0.8
medusa_logging: true
medusa_scheduler: constant
medusa_lr_multiplier: 4.0
# medusa_only_heads: true
# ddp_find_unused_parameters: true
# Stage 1: only train the medusa heads
# Stage 2: train the whole model

```

Thanks a lot.

Also I saw the checkpoints  you provid, there is no any lora adapter weight, Is It just remove all the lora config?


### chenhan97 · 2024-03-27

same, I couldn't reproduce medusa-1 as well. Not sure if you have solved the issue. My guess is the training dataset was not cleaned (or simply not the one used by Vicuna model). 

### zszdsze · 2026-01-06

Hi, could you please tell me if you use medusa V1.0 or medusa V0.1? It seems that I meet the same problem.
