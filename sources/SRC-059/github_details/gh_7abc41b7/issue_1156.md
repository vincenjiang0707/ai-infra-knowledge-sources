# [Issue #1156] Add Ernie model support to the Liger-kernel library

source: https://github.com/PaddlePaddle/ERNIE/issues/1156
state: closed | updated: 2026-01-07T12:02:13Z
labels: 

## 正文

I want to add TTS support to the Ernie-0.3B model. However, there is no liger-kernel support. Are you considering adding this? And I want to release the ernie-0.3b-tts model as open source.

## 评论 (4)

### cheng221 · 2025-08-22

Thank you for your support of the ERNIE model. However, we currently lack experience in supporting Liger Kernel for ERNIE-based models, which would make it challenging for us to provide assistance. Would it be possible to explore training directly through ERNIEKit instead? If any issues arise, we would be glad to provide support for that approach.


### kadirnar · 2025-08-26

> Thank you for your support of the ERNIE model. However, we currently lack experience in supporting Liger Kernel for ERNIE-based models, which would make it challenging for us to provide assistance. Would it be possible to explore training directly through ERNIEKit instead? If any issues arise, we would be glad to provide support for that approach.

Could you share a simple usage example for this?

Example my train code:
```py
....

tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, attn_implementation="flash_attention_2")


number_add_tokens = 7 * 4096 + 10
new_tokens = [f"<custom_token_{i}>" for i in range(0, number_add_tokens + 1)]
tokenizer.add_tokens(new_tokens)
model.resize_token_embeddings(len(tokenizer))


ds1 = load_dataset(dsn1, split="train")
ds2 = load_dataset(dsn2, split="train")


batch_total = batch_size * number_processes
train_dataset = BatchedRatioDataset(ds1, ds2, batch_total, ratio=config_ratio)


training_args = TrainingArguments(
    overwrite_output_dir=True,
    num_train_epochs=epochs,
    per_device_train_batch_size=batch_size,
    logging_steps=1,
    bf16=True,
    output_dir=f"./{base_repo_id}",
    fsdp="auto_wrap",
    report_to="wandb",
    save_steps=save_steps,
    remove_unused_columns=True,
    learning_rate=learning_rate,
    lr_scheduler_type="cosine", 
)


trainer = FSDPTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
    log_ratio=config_ratio
)

trainer.train()
```

### wtmlon · 2025-09-23

> > Thank you for your support of the ERNIE model. However, we currently lack experience in supporting Liger Kernel for ERNIE-based models, which would make it challenging for us to provide assistance. Would it be possible to explore training directly through ERNIEKit instead? If any issues arise, we would be glad to provide support for that approach.
> 
> Could you share a simple usage example for this?
> 
> Example my train code:
> 
> ....
> 
> tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
> model = AutoModelForCausalLM.from_pretrained(
>     model_name, attn_implementation="flash_attention_2")
> 
> 
> number_add_tokens = 7 * 4096 + 10
> new_tokens = [f"<custom_token_{i}>" for i in range(0, number_add_tokens + 1)]
> tokenizer.add_tokens(new_tokens)
> model.resize_token_embeddings(len(tokenizer))
> 
> 
> ds1 = load_dataset(dsn1, split="train")
> ds2 = load_dataset(dsn2, split="train")
> 
> 
> batch_total = batch_size * number_processes
> train_dataset = BatchedRatioDataset(ds1, ds2, batch_total, ratio=config_ratio)
> 
> 
> training_args = TrainingArguments(
>     overwrite_output_dir=True,
>     num_train_epochs=epochs,
>     per_device_train_batch_size=batch_size,
>     logging_steps=1,
>     bf16=True,
>     output_dir=f"./{base_repo_id}",
>     fsdp="auto_wrap",
>     report_to="wandb",
>     save_steps=save_steps,
>     remove_unused_columns=True,
>     learning_rate=learning_rate,
>     lr_scheduler_type="cosine", 
> )
> 
> 
> trainer = FSDPTrainer(
>     model=model,
>     args=training_args,
>     train_dataset=train_dataset,
>     data_collator=data_collator,
>     log_ratio=config_ratio
> )
> 
> trainer.train()

May I ask if you intend to expand the vocabulary for post-pretraining or for SFT training? If it's the former, ERNIE does not support pretraining currently. If it's the latter, you can refer to similar code examples [here](https://github.com/PaddlePaddle/ERNIE/blob/21493319cf02871bfd459116a694e0ac94de5a69/erniekit/train/sft/workflow.py#L604).

### nepeplwu · 2026-01-07

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
