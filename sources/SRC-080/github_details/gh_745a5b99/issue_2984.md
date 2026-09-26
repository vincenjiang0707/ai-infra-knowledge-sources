# [Issue #2984] [Bug]: Loading models with DDP leads to race condition on HF `cached_files`

source: https://github.com/vllm-project/llm-compressor/issues/2984
state: closed | updated: 2026-09-23T08:06:05Z
labels: bug, good first issue

## 正文

### ⚙️ Your current environment

```
$ uv pip list | grep -e "transformers\|hf\|hub"
hf-xet                 1.5.2
huggingface-hub        1.25.1
transformers           5.15.0.dev0            (main)
```

### 🐛 Describe the bug

Using the latest transformers hf versions, I encounter a race condition where DDP ranks will attempt to call `cached_files` and not find files, despite the files existing

EDIT: to be clear, the model is already downloaded. However, ranks still trigger race conditions as if the files did not exist.

```
$ uv pip list | grep -e "transformers\|hf\|hub"
hf-xet                 1.5.2
huggingface-hub        1.25.1
transformers           5.15.0.dev0            (main)
```

```
[rank3]: Traceback (most recent call last):
[rank3]:   File "/home/kylesayrs/llm-compressor/examples/quantizing_moe/kimi_k3_example.py", line 26, in <module>
[rank3]:     model = KimiK3ForConditionalGeneration.from_pretrained(  # KimiK3ForConditionalGeneration
[rank3]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/home/kylesayrs/llm-compressor/src/llmcompressor/modeling/moe/linearize.py", line 64, in patched
[rank3]:     model = original_from_pretrained(*args, **kwargs)
[rank3]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/home/kylesayrs/compressed-tensors/src/compressed_tensors/offload/load.py", line 93, in patched
[rank3]:     model = original_from_pretrained(*args, **kwargs)
[rank3]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/home/kylesayrs/transformers/src/transformers/modeling_utils.py", line 4258, in from_pretrained
[rank3]:     checkpoint_files, sharded_metadata = _get_resolved_checkpoint_files(
[rank3]:                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/home/kylesayrs/transformers/src/transformers/modeling_utils.py", line 796, in _get_resolved_checkpoint
_files
[rank3]:     checkpoint_files, sharded_metadata = get_checkpoint_shard_files(
[rank3]:                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/home/kylesayrs/transformers/src/transformers/utils/hub.py", line 894, in get_checkpoint_shard_files
[rank3]:     cached_filenames = cached_files(
[rank3]:                        ^^^^^^^^^^^^^
[rank3]:   File "/home/kylesayrs/transformers/src/transformers/utils/hub.py", line 543, in cached_files
[rank3]:     raise OSError(
[rank3]: OSError: moonshotai/Kimi-K3 does not appear to have files named ('model-00001-of-000096.safetensors', 'model-00
002-of-000096.safetensors', 'model-00003-of-000096.safetensors', 'model-00004-of-000096.safetensors', 'model-00005-of-00
0096.safetensors'). Checkout 'https://huggingface.co/moonshotai/Kimi-K3/tree/main' for available files.
Fetching 96 files: 100%|█████████████████████████████████████████████████████████████| 96/96 [00:00<00:00, 1355.30it/s]
```

### 🛠️ Steps to reproduce

1. Replicate the issue (use a ddp example, consider creating a fake model with many safetensors files)
2. Trace through `cached_files` to find if there's a potential race condition that could trigger with torchrun ranks

## 评论 (12)

### rohan9446 · 2026-07-30

Hi @kylesayrs, I’d like to work on this issue. I’ve looked into the race and have a downstream mitigation that prefetches the checkpoint on one rank per node and synchronizes all ranks before loading. Could you please assign it to me?


### sonalibiswas242 · 2026-08-14

Hi @kylesayrs, I'd like to work on this if it's still available, I noticed there's a linked branch already, just want to confirm before I start. I have background in concurrency/systems debugging (built a C++ inference gateway with request batching, and a TLS-terminating reverse proxy) so a race condition in cache loading is right up my alley. Could you point me to any additional context on repro steps or the suspected root cause? Happy to dig into it either way.

### brian-dellabetta · 2026-08-18

Hi @rohan9446 , sorry just seeing your post and PR for this issue now. I just came across this after replying to @sonalibiswas242 's PR, that this should be a relatively straightforward few-line patch to load_context with the transformers 

### rohan9446 · 2026-08-18

Thanks @brian-dellabetta, no worries. I took a look at #3030 and your suggestion there as well.

The main difference is that #2988 already wires this into load_context, so existing DDP callers don't need to invoke a separate prefetch helper. It also does per-node prefetch, propagates prefetch failures across ranks, and preserves the relevant from_pretrained kwargs.

On main_process_first, I see two constraints with that approach. In Transformers it isn't importable from transformers.utils, while Accelerate exposes main_process_first() / local_main_process_first() on its process state APIs. More importantly, those context managers serialize the entire block: the other ranks don't enter until the main process exits.

In this path, load_offloaded_model can perform distributed collectives during model loading, so wrapping the full load_context risks having the leading rank enter a collective while the peers are still waiting outside the context. Prefetching only the checkpoint download avoids that every rank is present again before the actual model load begins.

Would you prefer that I adapt #2988 toward a main_process_first style approach while preserving the current collective safe loading behavior?

### kylesayrs · 2026-08-18

Hi all @rohan9446 @sonalibiswas242 ,

I should have made this much clearer, that's my mistake.

> DDP ranks will attempt to call cached_files and not find files, despite the files existing

The "despite the files existing" part means that the model is already downloaded. However, ranks still trigger race conditions as if the files did not exist.

I think it's important to replicate the issue first, using a model with lots of safetensors files (each of which can be small) on a multi-gpu setup, where the model has already been predownloaded. Solutions which do a "prefetch" will likely not solve the issue described above.

### sonalibiswas242 · 2026-08-20

Thanks for clarifying, @kylesayrs that's a different failure mode than what I diagnosed. My fix (and it sounds like Rohan's #2988) both address the 'files not yet downloaded' race, not this one. I'd like to try reproducing the actual issue you're describing (pre-downloaded model, many small safetensors shards, multi-GPU) before proposing a different fix want to make sure I understand the real race in cached_files before touching more code. Will report back once I can reproduce it locally.

### kylesayrs · 2026-08-26

I was recently able to replicate the issue. Note that the model has already been downloaded at this point

```bash
rm -r /data/kylesayrs/hub/offload_folder-qwen38-flash-next-nvfp4-fp8 && CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 torchrun --nproc-per-node 8 examples/qwen38_flash_next_nvfp4.py
```

```
Fetching 131 files: 100%|█████████████████████████████████████████████████████████████████████████████████| 131/131 [00:00<00:00, 3663.90it/s]
Download complete: :                                                                                                      |  0.00B
Reconstruction complete: |                                                                                       |  0.00B /  0.00B
Fetching 131 files: 100%|█████████████████████████████████████████████████████████████████████████████████| 131/131 [00:00<00:00, 2123.94it/s]
Downloading bytes:                                                                                                        |  0.00B            [
rank7]: Traceback (most recent call last):                                                                       |  0.00B /  0.00B
[rank7]:   File "/home/kylesayrs/llm-compressor/examples/qwen38_flash_next_nvfp4.py", line 41, in <module>            | 0/131 [00:00<?, ?it/s]
[rank7]:     model = Qwen4ExpForConditionalGeneration.from_pretrained(
[rank7]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank7]:   File "/home/kylesayrs/llm-compressor/src/llmcompressor/modeling/moe/linearize.py", line 64, in patched
[rank7]:     model = original_from_pretrained(*args, **kwargs)
[rank7]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank7]:   File "/home/kylesayrs/compressed-tensors/src/compressed_tensors/offload/load.py", line 89, in patched
[rank7]:     model = original_from_pretrained(*args, **kwargs)
[rank7]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank7]:   File "/home/kylesayrs/llm-compressor/env/lib64/python3.12/site-packages/transformers/modeling_utils.py", line 4293, in from_pretrain
ed
[rank7]:     checkpoint_files, sharded_metadata = _get_resolved_checkpoint_files(
[rank7]:                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank7]:   File "/home/kylesayrs/llm-compressor/env/lib64/python3.12/site-packages/transformers/modeling_utils.py", line 795, in _get_resolved_
checkpoint_files
[rank7]:     checkpoint_files, sharded_metadata = get_checkpoint_shard_files(
[rank7]:                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank7]:   File "/home/kylesayrs/llm-compressor/env/lib64/python3.12/site-packages/transformers/utils/hub.py", line 902, in get_checkpoint_shar
d_files
[rank7]:     cached_filenames = cached_files(
[rank7]:                        ^^^^^^^^^^^^^
[rank7]:   File "/home/kylesayrs/llm-compressor/env/lib64/python3.12/site-packages/transformers/utils/hub.py", line 551, in cached_files
[rank7]:     raise OSError(
[rank7]: OSError: Qwen/Qwen3.8-Flash-Next does not appear to have a file named model-00068-of-00131.safetensors. Checkout 'https://huggingface.
co/Qwen/Qwen3.8-Flash-Next/tree/main' for available files.
```

### Swigler · 2026-09-04

## Root cause found — it's upstream in `huggingface_hub`

The bug is in `huggingface_hub/file_download.py`, function `_create_symlink` ([source](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/file_download.py#L615)).

It does:
```python
os.remove(dst)          # ← symlink GONE
# ... ~40 lines of path computation ...
os.symlink(src, dst)    # ← symlink BACK
```

Between `os.remove` and `os.symlink`, any concurrent `os.path.isfile(dst)` returns `False`. Under DDP with 131 shards × 8 GPUs, the probability of hitting this window is high — measured at **~2% of all `os.path.isfile()` checks** in a controlled test.

The HF devs' own comment (line 689) already acknowledges this: *"exactly between `os.remove` and `os.symlink`"* — but they only handled the `FileExistsError` case (two creates racing), not the missing-file case (a read during the gap).

**Fix:** Atomic symlink replacement: `os.symlink(src, tmp)` + `os.replace(tmp, dst)`. `os.replace()` is atomic on POSIX. After fix: **0 misses across 600k+ checks**.

PR submitted: https://github.com/huggingface/huggingface_hub/pull/4811

This is why solutions that do a "prefetch" or add barriers in llm-compressor / transformers don't solve it — those repos only *read* the symlinks (`os.path.isfile`). The *write* (remove + create) happens in `huggingface_hub`, and needs to be atomic there.

### kylesayrs · 2026-09-04

@Swigler Awesome find! Thanks for the resolution, I'll try this later today

### Wauplin · 2026-09-08

Hey there! Maintainer of the `huggingface_hub` library here (the underlying lib' handling file downloads for transformers/vLLM).

Thanks for the report and suggested PR @Swigler. There is indeed a very-old concurrency issue (introduced 4.5 years ago^^) happening when running `snapshot_download` concurrently from many processes using the same shared cache. After some (claude-led) investigation, it looks like your PR https://github.com/huggingface/huggingface_hub/pull/4811 does not really fix the issue which is happening somewhere else. I have opened https://github.com/huggingface/huggingface_hub/pull/4829 with some more details. Could you folks try it out and let me know how it goes?  cc @kylesayrs 

### kylesayrs · 2026-09-23

Thanks for the follow up @Wauplin! Yes, I have confirmed that I haven't seen an issue since using v1.32.0

### Wauplin · 2026-09-23

Great to hear!
