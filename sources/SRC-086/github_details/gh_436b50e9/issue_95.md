# [Issue #95] Medusa Training Loss

source: https://github.com/FasterDecoding/Medusa/issues/95
state: open | updated: 2025-08-22T01:57:10Z
labels: 

## 正文

When utilizing Axolotl, the training loss reduces to 0 following the gradient accumulation steps. Is this expected behaviour?
<img width="786" alt="image" src="https://github.com/FasterDecoding/Medusa/assets/69984048/316510a1-26a7-463d-9e1a-2da96cf45fde">

With Torchrun, the training loss consistently remains NaN.
<img width="745" alt="image" src="https://github.com/FasterDecoding/Medusa/assets/69984048/1b5f0d33-2ea7-49d5-9d2b-1d9566d440ba">

Thanks for the help!! Here is the training configuration:
base_model: teknium/OpenHermes-2.5-Mistral-7B
base_model_config: teknium/OpenHermes-2.5-Mistral-7B
model_type: MistralForCausalLM
tokenizer_type: LlamaTokenizer
is_llama_derived_model: false

load_in_8bit: false
load_in_4bit: false
strict: false

datasets:
  - path: ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json
    type: sharegpt
dataset_prepared_path:
val_set_size: 0.1
output_dir: ./openhermes7B_medusa_stage1

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
use_reentrant: True

warmup_steps: 40
eval_steps: 0.01
evaluation_strategy: steps
save_strategy: steps
save_steps:
save_total_limit: 1
debug:
deepspeed:
weight_decay: 0.0
fsdp:
fsdp_config:
special_tokens:
  bos_token: "<s>"
  eos_token: "<|im_end|>"
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



## 评论 (9)

### vivekmadan2 · 2024-04-08

I am also facing the same issue with Mistral example listed in the repo.

### FatPigeorz · 2024-04-10

same issue

### wrcai356 · 2024-04-12

Have you solved this problem？

### TomYang-TZ · 2024-04-12

Unfortunately no

### wrcai356 · 2024-05-06

I find some problems with the data，you can check it

### YuanlinChu · 2025-02-26

Have you solved this problem？I'm facing the same problem 

### TomYang-TZ · 2025-02-26

Still no luck ...

### YuanlinChu · 2025-02-26

> I find some problems with the data，you can check it

what's the problem? Have you solved the problem of NaN's loss？

### wittycheng · 2025-08-22

Hi, have you solved the this problem?
