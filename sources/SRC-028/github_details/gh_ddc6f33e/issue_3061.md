# [Issue #3061] Checkpoint conversion fails on v5litepod TPU - Orbax OCDBT atomic rename ENOENT

source: https://github.com/AI-Hypercomputer/maxtext/issues/3061
state: closed | updated: 2026-05-05T21:01:38Z
labels: 

## 正文

## Environment

- **TPU:** v5litepod-32 (32 chips, 8 hosts)
- **JAX:** 0.9.0
- **orbax-checkpoint:** 0.11.32
- **MaxText:** Latest from main branch
- **Python:** 3.12

## Problem

The HuggingFace to MaxText checkpoint conversion (`llama_or_mistral_ckpt.py`) fails on v5litepod-32 TPU. The layer conversion completes successfully, but the Orbax checkpoint save fails during atomic file rename.

**Related orbax issue:** https://github.com/google/orbax/issues/2837

## Error

```
ValueError: NOT_FOUND: Error writing "params.params.decoder.decoder_norm.scale/c/0" in OCDBT database
Failed to rename fd: 14 ".../__lock" to: "..."
[OS error 2: ENOENT No such file or directory]
```

## Steps to Reproduce

Following the official TPU recipe from `tpu-recipes`:

```bash
# 1. Create TPU
gcloud compute tpus tpu-vm create my-tpu \
    --zone=us-central1-a \
    --accelerator-type=v5litepod-32 \
    --version=tpu-ubuntu2204-base

# 2. Install MaxText
pip install -e .

# 3. Download model
huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Llama-8B

# 4. Convert (FAILS HERE)
JAX_PLATFORMS=cpu python3 llama_or_mistral_ckpt.py \
    --base-model-path=/path/to/model \
    --maxtext-model-path=gs://bucket/checkpoint \
    --model-size=llama3-8b \
    --huggingface-checkpoint=True
```

## Observations

1. Layer conversion completes: `layers: 100%|██████████| 32/32`
2. Orbax save fails during atomic file operations
3. Checkpoint is left incomplete (~11GB but missing tree metadata)
4. `generate_param_only_checkpoint.py` (Step 6) fails with "No structure could be identified"

## Questions

1. Is there a known workaround for this issue on multi-host TPUs?
2. Does the official TPU recipe work on v5litepod-32, or only on specific TPU types?
3. Are there pre-converted MaxText checkpoints available for Llama 3 8B models?

## Additional Context

- The official TPU recipe at `tpu-recipes/inference/trillium/JetStream-Maxtext/DeepSeek-R1-Distill-Llama-70B` references `bash setup.sh` which doesn't exist in MaxText
- The recipe recommends JAX 0.5.0 but MaxText's pyproject.toml requires JAX ≥0.8.1
- This may indicate the documentation is out of date

## Impact

Complete blocker for using MaxText + JetStream serving stack with custom models on v5litepod TPUs.

## 评论 (1)

### YixuanWang-99 · 2026-05-05

Please try our new consolidated [ckpt conversion module](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/guides/checkpointing_solutions/convert_checkpoint.html). Here is the example command in your cases to make the conversion from huggingface to maxtext, I've tested on a TPUv4 pod:

Install maxtext with [tpu]
```bash
pip install -e .[tpu] --resolution=lowest
```

Download the original huggingface ckpt:
```bash
huggingface-cli download deepseek-ai/DeepSeek-R1-Distill-Llama-8B
```

In my machine, it is saved in `~/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Llama-8B/snapshots/6a6f4aa4197940add57724a7707d069478df56b1`

```bash
python3 -m src.maxtext.checkpoint_conversion.to_maxtext \
    model_name='llama3.1-8b' \
    base_output_directory='<path to save the ckpt>'\
    scan_layers=True \
    use_multimodal=false \
    hardware=cpu \
    skip_jax_distributed_system=true \
    checkpoint_storage_use_zarr3=1 \
    checkpoint_storage_use_ocdbt=1\
    --lazy_load_tensors=True \
    --save_dtype=bfloat16 \
    --hf_model_path='<path to the original huggingface ckpt>' 
```


The conversion will take couple of minutes, and here is my result of conversion: 

<img width="786" height="108" alt="Image" src="https://github.com/user-attachments/assets/806376ec-f621-43ea-a444-6a2151f22d09" />

You could also validate the conversion by comparing the original huggingface ckpt against the maxtext ckpt after conversion, here is the command to do so (Be careful about the maxtext ckpt path, its path should contain the metadata, mine is like `~/output/0/items ` (where I provided `~/output/` as the output directory in the first command.):

```bash
python3 -m tests.utils.forward_pass_logit_checker src/maxtext/configs/base.yml \
    load_parameters_path=<path to the converted maxtext ckpt>\
    model_name='llama3.1-8b' \
    skip_jax_distributed_system=true \
    scan_layers=True \
    max_prefill_predict_length=4 \
    max_target_length=8 \
    use_multimodal=false \
    --run_hf_model=True \
    --hf_model_path='<path to the original huggingface ckpt>' \
    --max_kl_div=0.015
```



Then you can get the KL divergence and top 10 tokens comparisons like the following:

<img width="513" height="735" alt="Image" src="https://github.com/user-attachments/assets/5990e7e7-667c-438e-99b1-e98300368a3d" />
<img width="514" height="710" alt="Image" src="https://github.com/user-attachments/assets/4824e8dd-af2e-4f38-b4c2-654d310b9727" />
<img width="523" height="698" alt="Image" src="https://github.com/user-attachments/assets/4f1c8e59-30e2-41b7-b464-63f2ecd686e5" />

 


