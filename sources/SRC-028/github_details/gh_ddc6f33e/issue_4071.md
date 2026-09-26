# [Issue #4071] Kimi-K2.6 unscanned checkpoint converter OOMs on hosts < ~2.5 TB RAM (buffers all 64 shards before write)

source: https://github.com/AI-Hypercomputer/maxtext/issues/4071
state: closed | updated: 2026-09-04T18:28:13Z
labels: 

## 正文

# Summary
`convert_deepseek_family_unscanned_ckpt --model_size kimi-k2.6-text` accumulates every dequantized bf16 tensor for all 64 HF safetensors shards in a single in-memory `chkpt_vars` dict before assembling and writing Orbax. For Kimi-K2.6 that's ~2.3 TB of CPU RAM at peak. There's no streaming/low-memory mode, and the documented runbook doesn't mention a host-size requirement.

# Environment
- `maxtext==0.2.2` installed via `pip install maxtext[tpu]` (PyPI), Python 3.12, CPU-only `torch==2.12.0+cpu` (Note: `maxtext[tpu]` pulls `torch==2.12.0+cu130` whose `torch._dynamo` segfaults at import on a CPU-only host — forced reinstall with `--index-url https://download.pytorch.org/whl/cpu` to fix.)
- Host: GCP `n2-standard-32` (32 vCPU, 128 GB RAM), 2 TB pd-balanced disk, Ubuntu 22.04.
- Zone: `us-east5-a` (chosen to be local to v5e TPU quota in this project; us-east5 has no `m1/m2/m3-ultramem` SKUs).
- HF source: `moonshotai/Kimi-K2.6` (96 files, 64 `*.safetensors` shards, 555 GB on disk).

# Repro
```sh
python -m maxtext.checkpoint_conversion.standalone_scripts.convert_deepseek_family_unscanned_ckpt \
    --model_size kimi-k2.6-text \
    --base_model_path /home/$USER/kimi-k2.6-hf \
    --maxtext_model_path gs://<bucket>/k2.6-unscanned
```

# Memory growth observed (RSS via `free -g`)
| After loading shard | RSS used |
| --- | --- |
| 2 | 16 GB |
| 3 | 53 GB |
| 4 | 90 GB |
| 5 | 124 GB |
| 6 | **SIGKILL (rc=137)** |

~35–37 GB per shard, linear. Extrapolating across all 64 shards → ~2.3 TB RSS at peak.

# Root cause (from reading the script)
In [`convert_deepseek_family_unscanned_ckpt.py`](https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/checkpoint_conversion/standalone_scripts/convert_deepseek_family_unscanned_ckpt.py), the outer loop over `ckpt_paths` populates a single `chkpt_vars = {}` with every `dequantize_pack_quantized_int4(...)` result before the assembly phase begins. Nothing is freed; nothing is written until the entire model is resident.

# Asks
1. Is there a supported low-memory / streaming mode for the K2.6 (or any K2-Thinking/K2.5) converter? The K2.6 runbook doesn't mention host-memory requirements.
2. If not, what host SKU does the MaxText team use to convert K2.6? `m1-ultramem-160` (3.75 TB) appears necessary but is unavailable in zones where v5e Lite TPU quota lives (`us-east5`, `europe-west4`).
3. Would a per-layer streaming patch be welcome upstream? Happy to PR it if there's interest.

# Workarounds considered
- Cross-region: convert in `us-central1` (has `m1-ultramem-160`), pay ~\$80 GCS egress to land the Orbax in `us-east5`.
- Patch the script to dequant + emit per layer, freeing after each.
- Use the scanned converter then unscan at decode time — does this avoid the same accumulation?

## 评论 (4)

### discobot · 2026-06-13

The buffering you found is only half the peak: assembly holds a second full fp16 copy,
and the default save path re-materializes the whole pytree in RAM via
`shard_jax_weights`, so a loader-only patch would still OOM at save time. Fix in
#4160: shard loading is now lazy by default, and `--low_memory true` stages converted
weights in disk-backed memmaps and saves via the single-device path (bit-identical,
topology-independent checkpoint), keeping peak RSS at O(one tensor).


### shralex · 2026-07-22

@entrpn could you please take a look / triage

### entrpn · 2026-07-22

@sardaniksd 

An [m4-ultramem-224](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4n_machine_types) (224 vCPUs, 5,952 GB Memory) with a 10TB external disk attached was used using the instructions outlined [here](https://github.com/AI-Hypercomputer/maxtext/blob/main/tests/end_to_end/tpu/kimi/Run_Kimi.md). 

We welcome PRs. @discobot PR looks to be a good start.

### entrpn · 2026-09-04

I'm closing this issue. If you need help with this please open a new issue and link this one. 
