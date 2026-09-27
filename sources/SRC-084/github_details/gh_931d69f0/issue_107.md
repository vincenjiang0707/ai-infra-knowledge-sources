# [Issue #107]  TypeError: Object of type dtype is not JSON serializable

source: https://github.com/dropbox/hqq/issues/107
state: closed | updated: 2024-09-05T03:09:47Z
labels: 

## 正文

I want to train a 1bit-quantized model.
at first,I got a 1bit model using AutoHQQHFModel
`
model     = AutoHQQHFModel.from_quantized(model_id, cache_dir=cache_dir, compute_dtype=compute_dtype)
`
then I get peft model 
`
model = get_peft_model(model, peft_config)
`
so l train the model with SFTtrainer
`
trainer = SFTTrainer(
```bash
    model=model,
    tokenizer=tokenizer,
    max_seq_length=max_tokens,
    train_dataset=small_train_dataset,#dataset,
    args=SFTConfig(output_dir="/tmp"),
    formatting_func=formatting_prompts_func,
    data_collator=collator,
    dataset_text_field="instruction",
```
)

model.train()
trainer.train()
`
and i got these report 
`
TypeError                                 Traceback (most recent call last)
Cell In[14], line 2
      1 quantized_peft_model.train()
----> 2 trainer.train()

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/trl/trainer/sft_trainer.py:451, in SFTTrainer.train(self, *args, **kwargs)
    448 if self.neftune_noise_alpha is not None and not self._trainer_supports_neftune:
    449     self.model = self._trl_activate_neftune(self.model)
--> 451 output = super().train(*args, **kwargs)
    453 # After training we make sure to retrieve back the original forward pass method
    454 # for the embedding layer by removing the forward post hook.
    455 if self.neftune_noise_alpha is not None and not self._trainer_supports_neftune:

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/transformers/trainer.py:1948, in Trainer.train(self, resume_from_checkpoint, trial, ignore_keys_for_eval, **kwargs)
   1946         hf_hub_utils.enable_progress_bars()
   1947 else:
-> 1948     return inner_training_loop(
   1949         args=args,
   1950         resume_from_checkpoint=resume_from_checkpoint,
   1951         trial=trial,
   1952         ignore_keys_for_eval=ignore_keys_for_eval,
   1953     )

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/transformers/trainer.py:2366, in Trainer._inner_training_loop(self, batch_size, args, resume_from_checkpoint, trial, ignore_keys_for_eval)
   2363     self.state.epoch = epoch + (step + 1 + steps_skipped) / steps_in_epoch
   2364     self.control = self.callback_handler.on_step_end(args, self.state, self.control)
-> 2366     self._maybe_log_save_evaluate(tr_loss, grad_norm, model, trial, epoch, ignore_keys_for_eval)
   2367 else:
   2368     self.control = self.callback_handler.on_substep_end(args, self.state, self.control)

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/transformers/trainer.py:2817, in Trainer._maybe_log_save_evaluate(self, tr_loss, grad_norm, model, trial, epoch, ignore_keys_for_eval)
   2814     metrics = self._evaluate(trial, ignore_keys_for_eval)
   2816 if self.control.should_save:
-> 2817     self._save_checkpoint(model, trial, metrics=metrics)
   2818     self.control = self.callback_handler.on_save(self.args, self.state, self.control)

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/transformers/trainer.py:2896, in Trainer._save_checkpoint(self, model, trial, metrics)
   2894 run_dir = self._get_output_dir(trial=trial)
   2895 output_dir = os.path.join(run_dir, checkpoint_folder)
-> 2896 self.save_model(output_dir, _internal_call=True)
   2898 if not self.args.save_only_model:
   2899     # Save optimizer and scheduler
   2900     self._save_optimizer_and_scheduler(output_dir)

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/transformers/trainer.py:3464, in Trainer.save_model(self, output_dir, _internal_call)
   3461         self.model_wrapped.save_checkpoint(output_dir)
   3463 elif self.args.should_save:
-> 3464     self._save(output_dir)
   3466 # Push to the Hub when `save_model` is called by the user.
   3467 if self.args.push_to_hub and not _internal_call:

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/transformers/trainer.py:3535, in Trainer._save(self, output_dir, state_dict)
   3533             torch.save(state_dict, os.path.join(output_dir, WEIGHTS_NAME))
   3534 else:
-> 3535     self.model.save_pretrained(
   3536         output_dir, state_dict=state_dict, safe_serialization=self.args.save_safetensors
   3537     )
   3539 if self.tokenizer is not None:
   3540     self.tokenizer.save_pretrained(output_dir)

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/peft/peft_model.py:396, in PeftModel.save_pretrained(self, save_directory, safe_serialization, selected_adapters, save_embedding_layers, is_main_process, convert_pissa_to_lora, path_initial_model_for_weight_conversion, **kwargs)
    393         if peft_config.alpha_pattern:
    394             peft_config.alpha_pattern = {key: 2 * val for key, val in peft_config.alpha_pattern.items()}
--> 396     peft_config.save_pretrained(output_dir, auto_mapping_dict=auto_mapping_dict)
    397 peft_config.inference_mode = inference_mode

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/site-packages/peft/config.py:81, in PeftConfigMixin.save_pretrained(self, save_directory, **kwargs)
     79 # save it
     80 with open(output_path, "w") as writer:
---> 81     writer.write(json.dumps(output_dict, indent=2, sort_keys=True))

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/json/__init__.py:238, in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
    232 if cls is None:
    233     cls = JSONEncoder
    234 return cls(
    235     skipkeys=skipkeys, ensure_ascii=ensure_ascii,
    236     check_circular=check_circular, allow_nan=allow_nan, indent=indent,
    237     separators=separators, default=default, sort_keys=sort_keys,
--> 238     **kw).encode(obj)

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/json/encoder.py:202, in JSONEncoder.encode(self, o)
    200 chunks = self.iterencode(o, _one_shot=True)
    201 if not isinstance(chunks, (list, tuple)):
--> 202     chunks = list(chunks)
    203 return ''.join(chunks)

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/json/encoder.py:432, in _make_iterencode.<locals>._iterencode(o, _current_indent_level)
    430     yield from _iterencode_list(o, _current_indent_level)
    431 elif isinstance(o, dict):
--> 432     yield from _iterencode_dict(o, _current_indent_level)
    433 else:
    434     if markers is not None:

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/json/encoder.py:406, in _make_iterencode.<locals>._iterencode_dict(dct, _current_indent_level)
    404         else:
    405             chunks = _iterencode(value, _current_indent_level)
--> 406         yield from chunks
    407 if newline_indent is not None:
    408     _current_indent_level -= 1

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/json/encoder.py:439, in _make_iterencode.<locals>._iterencode(o, _current_indent_level)
    437         raise ValueError("Circular reference detected")
    438     markers[markerid] = o
--> 439 o = _default(o)
    440 yield from _iterencode(o, _current_indent_level)
    441 if markers is not None:

File /workspace/python_code/home/workspace/envs/githqq/lib/python3.11/json/encoder.py:180, in JSONEncoder.default(self, o)
    161 def default(self, o):
    162     """Implement this method in a subclass such that it returns
    163     a serializable object for ``o``, or calls the base implementation
    164     (to raise a ``TypeError``).
   (...)
    178 
    179     """
--> 180     raise TypeError(f'Object of type {o.__class__.__name__} '
    181                     f'is not JSON serializable')

TypeError: Object of type dtype is not JSON serializable
`
trainer use model.save_pretrained() function but hqq-quantized model can't deal with it.So how can I train the model?

## 评论 (11)

### mobicham · 2024-08-21

That's pretty old code, you can use HQQ directly with peft: https://huggingface.co/docs/peft/v0.12.0/en/developer_guides/quantization#hqq-quantization 
I updated the documentation and deleted the old code file.

Why do you want to do 1-bit? 2-bit should work much better and you can actually run it fast via the Bitblas backend

### zxbjushuai · 2024-08-21

thanks for your early reply.I have tried HQQ directly with peft,but I still encounter the same error.It's probably that we can't train the model using HQQ with STFtrainer.Do you have any other methods to solve the problem(some other trainer)?

### zxbjushuai · 2024-08-21

By the way,I would like to do 2-bit if it's better 

### mobicham · 2024-08-21

Can you try this:
```Python
from transformers import HqqConfig, AutoModelForCausalLM
from hqq.core.quantize import *
quant_config = HqqConfig(nbits=2, group_size=32, quant_zero=False, quant_scale=False, axis=1)
HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)

quantized_model = AutoModelForCausalLM.from_pretrained(save_dir_or_hfhub, device='cuda', quantization_config=quant_config)
peft_config = LoraConfig(...)

quantized_model = get_peft_model(quantized_model, peft_config)
```
I don't use HF peft myself but since it's integrated there I suppose that it should work :thinking: 







### zxbjushuai · 2024-08-21

I have also used that.Actually,using AutoModelForCausalLM to quantize the model just leads to larger memory usage and it comes to error.
I have tried HQQModelForCausalLM and AutoHQQHFModel to get quantized model.error!
The problem doen't happen when quantizing.It happens when trainer.train() tries to save something.Maybe I need to code this part by myself. 


### mobicham · 2024-08-21

Oh I see, then I think it's better to create an issue on the peft repo: https://github.com/huggingface/peft 
I haven't used it myself for a while, I use some custom code. Are you just trying to do SFT ? Because you can easily implement that in pytorch without the need for SFTTrainer. If you want, I can assist you with that 

### mobicham · 2024-08-21

Can you follow this example? https://github.com/huggingface/peft/blob/6c832c1dd4236262feb1c712786d29daf00b438c/tests/test_gpu_examples.py#L2532-L2592
It should work since it's part of the tests

### zxbjushuai · 2024-08-21

Wow,that is really kind of you.I'll try this tomorrow and told you the result^-^

### zxbjushuai · 2024-08-22

That does work.Thanks again👍

### mobicham · 2024-08-22

Perfect :+1: 

### zxbjushuai · 2024-09-05

Hi,after that I want to reproduce your paper about HQQ+ but meet some problems when training:
1.Loss doesn't decrease but varies up and down
2.The text generated by the model is very poor
I think the reason is that the parameters are not set well enough.
Here is my code.May you give me some suggestions?
quantization code:
```
quant_config = HqqConfig(nbits=1, group_size=64 ,quant_zero=False, quant_scale=False) 
max_memory={0: "16GiB", 1: "16GiB", 2: "16GiB", 3: "16GiB"}
HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)
model = AutoModelForCausalLM.from_pretrained(
    model_id,#llama3-8b
    device_map="auto",
    torch_dtype=compute_dtype,#bfloat16
    quantization_config=quant_config,
    max_memory = max_memory,
)


model = prepare_model_for_kbit_training(model)
```
add adapter code:
```
config = LoraConfig(
    r=32,#I set this value to 32 because it works better than 16.
    lora_alpha=32,
    target_modules=["q_proj","k_proj","v_proj", "o_proj", "gate_proj","up_proj","down_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    use_dora=False,
)
model = get_peft_model(model, config)
```
and training code:
```
trainer = Trainer(
    model=model,
    train_dataset=data,#wikitext-2-raw-v1(full),num_rows =36718
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        num_train_epochs=3,
        learning_rate=1e-5,
        logging_steps=20,
        output_dir=adapter_dir,
        bf16 = True,
        save_steps=100,
        save_total_limit=5,
    ),
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.is_parallelizable       = False
trainer.is_model_parallel     = False
trainer.place_model_on_device = False
model.config.use_cache = False
trainer.train() 
model.save_pretrained(adapter_dir)
```
The performance of the model is much better than before fine-tuning, but not good enough. Is it because I didn’t train enough?

