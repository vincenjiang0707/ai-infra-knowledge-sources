# [Issue #1089] DPO issues

source: https://github.com/AI-Hypercomputer/maxtext/issues/1089
state: closed | updated: 2026-06-16T23:58:39Z
labels: 

## 正文

@rdyro I am testing out the DPO branch, and I am currently facing these two issues with my DPO training:
* Evaluation is not running with HF datasets. Setting `eval_interval: 20` in base.yml simply causes training to stop after finishing evaluation.

* Unable to run with per_device_batch_size > 1

The following code is reproducing the error training a llama3.1 70B on a TPU v5-256:
```python
MaxText/train.py MaxText/configs/dpo.yml \
    base_output_directory='gs://mybucket' \ # Change to a valid bucket
    per_device_batch_size=0.5 \ # Works with 1
    tokenizer_path='north/llama3.1-8b-instruct-reference' \ # The original tokenizer is gated. This one is open
    max_target_length=128 \ # This is way too short, but does not give OOM when training with per_device_batch_size=1
    load_parameters_path='gs://maxtext-public-test/nb-llama-3.1-70B-sft/checkpoints/900/items' \
    steps=181 \
    checkpoint_period=180 \
    run_name='llama3.1-70B_dpo_helpfulandharmless_test1' \
    model_name='llama3.1-70b' \
    enable_checkpointing=True \
    async_checkpointing=True \
    dataset_type='hf' \
    hf_path='json' \
    hf_train_files='gs://maxtext-public-test/hh-rlhf-helpful-and-harmless/train*.jsonl' \
    remat_policy='minimal' \
    attention='flash' \
    warmup_steps_fraction=0.1 \
    hf_eval_split='' \
    hf_eval_files='gs://maxtext-public-test/hh-rlhf-helpful-and-harmless/test*.jsonl' \
    eval_steps=1 \
    allow_split_physical_axes=True \
    ici_tensor_parallelism=8 \
    use_dpo=True \
    dpo_reference_params_path=''
```

Both the model and training set is open. I am hosting it temporarily in a public bucket. This will be shut down when you have tried replicating this.

It seems like it is defaulting to non-dpo training, but I have been unable to figure out where and why. I did however notice that `global_batch_size_to_train_on` and `global_batch_size_to_load` differs when per_device_batch_size < 1. Maybe this mismatch can create a shape mismatch between chosen and rejected pairs?


## 评论 (4)

### peregilk · 2024-12-17

@rdyro Did you have a chance to test if you could reproduce this error?

### jedcheng · 2025-11-09

Has this issue been addressed?

I am trying to use DPO on a grain & hf dataset. The training failed at the first step when calculating the loss. (src/MaxText/dpo_utils.py line 32). It returned a key error for "chosen_segmentation" from the data dict.

The data dict looks like this, without chosen/rejected.

{'inputs': JitTracer<int32[8,512]>, 'inputs_position': JitTracer<int32[8,512]>, 'inputs_segmentation': JitTracer<int32[8,512]>, 'targets': JitTracer<int32[8,512]>, 'targets_position': JitTracer<int32[8,512]>, 'targets_segmentation': JitTracer<int32[8,512]>}

Or did I simply format the data wrongly?

### shralex · 2026-04-18

@igorts-git is working on a new DPO implementation with Tunix, here: https://github.com/AI-Hypercomputer/maxtext/pull/3668

### igorts-git · 2026-06-16

The new DPO implementation is now merged and the old one was deleted. Please refer to https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/dpo.html The new implementation is based on Tunix. It should not have these issues.
