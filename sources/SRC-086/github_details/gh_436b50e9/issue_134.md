# [Issue #134] why my train medusa head result is {'medusa0_top1': nan, 'medusa0_loss': nan, 'medusa1_top1': nan, 'medusa1_loss': nan, 'medusa2_top1': nan, 'medusa2_loss': nan, 'epoch': 0}

source: https://github.com/FasterDecoding/Medusa/issues/134
state: open | updated: 2025-08-22T01:52:52Z
labels: 

## 正文

I'm now preparing to train the medusa header to the readme file and first ran into the following issue：
/data/lx/demo/Medusa/medusa/train/train_legacy.py:392: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `CustomizedTrainer.__init__`. Use `processing_class` instead.
  trainer = CustomizedTrainer(
Loading data...
Formatting inputs...Skip in lazy mode
/data/lx/demo/Medusa/medusa/train/train_legacy.py:392: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `CustomizedTrainer.__init__`. Use `processing_class` instead.
  trainer = CustomizedTrainer(
Detected kernel version 3.10.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
Parameter Offload: Total persistent parameters: 278528 in 68 params
[rank1]: Traceback (most recent call last):
[rank1]:   File "/data/lx/demo/Medusa/medusa/train/train_legacy.py", line 424, in <module>
[rank1]:     train()
[rank1]:   File "/data/lx/demo/Medusa/medusa/train/train_legacy.py", line 399, in train
[rank1]:     trainer.train()
[rank1]:   File "/data/anaconda_envs/medusa/lib/python3.10/site-packages/transformers/trainer.py", line 2241, in train
[rank1]:     return inner_training_loop(
[rank1]:   File "/data/anaconda_envs/medusa/lib/python3.10/site-packages/transformers/trainer.py", line 2548, in _inner_training_loop
[rank1]:     tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
[rank1]:   File "/data/anaconda_envs/medusa/lib/python3.10/site-packages/transformers/trainer.py", line 3698, in training_step
[rank1]:     loss = self.compute_loss(model, inputs, num_items_in_batch=num_items_in_batch)
[rank1]: TypeError: CustomizedTrainer.compute_loss() got an unexpected keyword argument 'num_items_in_batch'
wandb: Using wandb-core as the SDK backend.  Please refer to https://wandb.me/wandb-core for more information.
W0322 10:04:33.002000 13602 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 13669 closing signal SIGTERM
E0322 10:04:33.268000 13602 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 1 (pid: 13670) of binary: /data/anaconda_envs/medusa/bin/python
Traceback (most recent call last):

![Image](https://github.com/user-attachments/assets/322d7138-0627-49dc-ad30-7f63cdedfe01)

I added num_items_in_batch=none to the compute_loss method in the CustomizedTrainer class of the Medusa/medusa/train/train_legacy.py file, and the code was able to run, but the training result is like this, where did I do something wrong that caused the training loss to be nan？

![Image](https://github.com/user-attachments/assets/4bf5e9b8-dc4e-45c5-894e-7a6848d575a2)

My run code is （I have two GPU card ,so I change nproc_per_node is 2 ）：
torchrun --nproc_per_node=2 medusa/train/train_legacy.py --model_name_or_path /data/models/Mistral-7B-Instruct-v0.2 \
    --data_path mistral.json \
    --bf16 True \
    --output_dir test \
    --num_train_epochs 2 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --learning_rate 1e-3 \
    --weight_decay 0.0 \
    --warmup_ratio 0.1 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --lazy_preprocess True \
    --medusa_num_heads 3 \
    --medusa_num_layers 1 \
    --deepspeed deepspeed.json

And result :

![Image](https://github.com/user-attachments/assets/5889b616-0fb2-4bc6-97b6-eed381fc9c18)


## 评论 (1)

### wittycheng · 2025-08-22

Hi, have you solved this problem?
