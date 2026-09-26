# [Issue #2914] Commit 171a3c6 breaks checkpoint conversion in to_huggingface.py

source: https://github.com/AI-Hypercomputer/maxtext/issues/2914
state: closed | updated: 2026-07-19T03:19:17Z
labels: bug

## 正文

### Bug report

```python
# Training
subprocess.run(
    [
        '/workspace/.venv/bin/python',
        '-m',
        'MaxText.train',
        CNF_PATH,
        'base_output_directory=/data/qwen3-0.6b-fine-tune',
        'model_name=qwen3-0.6b',
        'load_parameters_path=/data/qwen3-0.6b-ckpt/0/items',
        'dataset_type=hf',
        'hf_path=parquet',
        'hf_train_files=/data/gsm8k/train_full.parquet',
        'run_name=gsm8k_finetune',
        'tokenizer_path=/data/Qwen3-0.6B',
        'tokenizer_type=huggingface',
        'enable_checkpointing=true',
        'train_data_columns=["question","answer"]',
        'use_sft=true'
    ],
    cwd=MAXTEXT_PATH,
    check=True
)

# Convert back from checkpoint to safetensors format
subprocess.run(
    [
        '/workspace/.venv/bin/python',
        'src/MaxText/utils/ckpt_conversion/to_huggingface.py',
        CNF_PATH,
        'enable_checkpointing=true',
        'model_name=qwen3-0.6b',
        'load_parameters_path=/data/qwen3-0.6b-fine-tune/gsm8k_finetune/checkpoints/0/items',
        'base_output_directory=/data/Qwen3-0.6B-fine-tune',
        'scan_layers=true'
    ],
    cwd=MAXTEXT_PATH,
    check=True
)
```

### Logs/Output

## Failure Logs

**Error Message:**
```
ValueError: Shape mismatch for model.embed_tokens.weight: Expect [151936, 1024], got (151936, 1024)
```

**Stack Trace:**
```
Traceback (most recent call last):
  File "/workdir/maxtext/src/MaxText/utils/ckpt_conversion/to_huggingface.py", line 237, in <module>
    app.run(main)
  File "/workdir/.venv/lib/python3.12/site-packages/absl/app.py", line 316, in run
    _run_main(main, args)
  File "/workdir/.venv/lib/python3.12/site-packages/absl/app.py", line 261, in _run_main
    sys.exit(main(argv))
             ^^^^^^^^^^
  File "/workdir/maxtext/src/MaxText/utils/ckpt_conversion/to_huggingface.py", line 211, in main
    processed_params = process_maxtext_param(key, weight, param_map, hook_fn_map, shape_map, config)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workdir/maxtext/src/MaxText/utils/ckpt_conversion/utils/utils.py", line 264, in process_maxtext_param
    _process(hf_path, maxtext_param_weight, output_weights, current_hook_fns, hf_shape_map)
  File "/workdir/maxtext/src/MaxText/utils/ckpt_conversion/utils/utils.py", line 203, in _process
    raise ValueError(f"Shape mismatch for {hf_path}: Expect {target_hf_shape}, got {numpy_slice.shape}")
ValueError: Shape mismatch for model.embed_tokens.weight: Expect [151936, 1024], got (151936, 1024)
```

**Root Cause:**
In `utils/utils.py` line 203, the shape comparison fails due to type mismatch:
- `target_hf_shape` is a Python **list**: `[151936, 1024]`
- `numpy_slice.shape` is a NumPy **tuple**: `(151936, 1024)`

The comparison `[151936, 1024] != (151936, 1024)` returns `True` in Python because list ≠ tuple, even though the dimensions are identical.


### Environment Information

- Python 3.12
- Model: Qwen3-0.6B
- Platform: TPU v5e 2x2

I think the problem in Commit 171a3c6, specifically changes in src/MaxText/utils/ckpt_conversion/utils/utils.py. On earlier commits I did not face this issue.

### Additional Context

_No response_

## 评论 (4)

### shuningjin · 2026-01-16

Thanks for reporting the issue! We merged a PR to fix this: https://github.com/AI-Hypercomputer/maxtext/pull/2935. 

Could you fetch the head and retry to see if the error is gone? 


### jedcheng · 2026-01-20

@shuningjin thank you for addressing the issue. I tried install from source to convert Gemma3 4B to hf format using the following command. 

This command works on the stable release on pip, albeit with the need to manually patch the mapping 
https://github.com/AI-Hypercomputer/maxtext/issues/2867

```bash
python3 -m MaxText.utils.ckpt_conversion.to_huggingface src/MaxText/configs/base.yml \
    model_name='gemma3-4b' \
    hf_access_token=${hf_token} \
    load_parameters_path="gs://${whatever_path}/checkpoints/469/items" \
    base_output_directory="/tmp/${model_name}" \
    use_multimodal=false \
    scan_layers=false  
```

I encountered a device HBM OOM error when running the version installed from source:
 
```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/jed351/maxtext/src/MaxText/utils/ckpt_conversion/to_huggingface.py", line 216, in <module>
    app.run(main)
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/absl/app.py", line 316, in run
    _run_main(main, args)
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/absl/app.py", line 261, in _run_main
    sys.exit(main(argv))
             ^^^^^^^^^^
  File "/home/jed351/maxtext/src/MaxText/utils/ckpt_conversion/to_huggingface.py", line 139, in main
    checkpoint_dict = load_orbax_checkpoint(config)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/src/MaxText/utils/ckpt_conversion/utils/utils.py", line 798, in load_orbax_checkpoint
    return ckptr.restore(checkpoint_path, restore_args=restore_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/checkpointers/checkpointer.py", line 306, in restore
    restored = self._restore(directory, args=ckpt_args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/checkpointers/checkpointer.py", line 338, in _restore
    return self._handler.restore(directory, args=args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/handlers/pytree_checkpoint_handler.py", line 860, in restore
    return self._handler_impl.restore(directory, args=args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/handlers/base_pytree_checkpoint_handler.py", line 1049, in restore
    tree_memory_size, restored_item = asyncio_utils.run_sync(
                                      ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/asyncio_utils.py", line 36, in run_sync
    return asyncio.run(coro)
           ^^^^^^^^^^^^^^^^^
  File "/home/jed351/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/home/jed351/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/.local/share/uv/python/cpython-3.12.12-linux-x86_64-gnu/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/handlers/base_pytree_checkpoint_handler.py", line 794, in _maybe_deserialize
    deserialized_batches += await asyncio.gather(*deserialized_batches_ops)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/serialization/jax_array_handlers.py", line 1110, in deserialize
    ret = await _deserialize_arrays(
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/serialization/jax_array_handlers.py", line 792, in _deserialize_arrays
    ret, array_metadatas = await asyncio.gather(
                           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/serialization/jax_array_handlers.py", line 789, in _async_deserialize
    return await asyncio.gather(*deserialize_ops)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/serialization/serialization.py", line 490, in async_deserialize
    return await read_and_create_array(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/serialization/serialization.py", line 440, in read_and_create_array
    dbs = sum(await asyncio.gather(*read_array_coros), [])
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/orbax/checkpoint/_src/serialization/serialization.py", line 394, in _read_array_index_and_device_put
    result.append(jax.device_put(shard, Format(dll, sharding)))  # pytype: disable=wrong-arg-types
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/api.py", line 2840, in device_put
    out_flat = dispatch._batched_device_put_impl(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/dispatch.py", line 581, in _batched_device_put_impl
    shard_arg_results = pxla.shard_args(dsa_shardings, [None] * len(dsa_xs),
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/profiler.py", line 359, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/interpreters/pxla.py", line 125, in shard_args
    return shard_arg_handlers[type(arg)]([arg], shardings, layouts,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/interpreters/pxla.py", line 211, in _shard_np_array
    results.append(batched_device_put(aval, sharding, shards, devices))
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jed351/maxtext/maxtext_venv/lib/python3.12/site-packages/jax/_src/interpreters/pxla.py", line 256, in batched_device_put
    return xc.batched_device_put(aval, sharding, xs, list(devices), committed,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
jax.errors.JaxRuntimeError: RESOURCE_EXHAUSTED: Error allocating device buffer: Attempting to allocate 100.00M. That was not possible. There are 30.95M free.; (0x0x0_HBM0)
```

### shuningjin · 2026-07-19

Hi @jedcheng, thanks for the issue!

To my understanding, your issue is about `to_huggingface` conversion for `gemma3-4b` failing with an **HBM OOM** error when running the version installed from source, while it works on the stable pip release.

This seems independent of the original issue, which was about a **shape mismatch** during Qwen3-0.6B conversion. It will require a separate investigation. Feel free to open a new issue if you still encounter this.

### shuningjin · 2026-07-19

I am closing the issue as I have verified the fix.

---

Hi @panalexeu, 

As mentioned in the previous comment, I believe the original issue was resolved by https://github.com/AI-Hypercomputer/maxtext/pull/2935.

As a sanity check, I ran `to_huggingface` on the latest maxtext head (`dfd8d293d266fe224b90f7cb0b49f3e8084e9892`) on CPU and it completed successfully.

```bash
# to_maxtext: generate checkpoint
BASE_OUTPUT_PATH=gs://runner-maxtext-logs/$(date +%Y-%m-%d-%H-%M); \
echo $BASE_OUTPUT_PATH/0/items; \
python3 -m maxtext.checkpoint_conversion.to_maxtext \
src/maxtext/configs/base.yml model_name=qwen3-0.6b scan_layers=true \
base_output_directory=$BASE_OUTPUT_PATH hf_access_token=$HF_TOKEN \
hardware=cpu skip_jax_distributed_system=True \
attention=dot_product \
--eager_load_method=safetensors --save_dtype=bfloat16
# output is gs://runner-maxtext-logs/2026-07-19-02-30/0/items
```

```bash
# to_huggingface: check conversion
SCANNED_CKPT_PATH=gs://runner-maxtext-logs/2026-07-19-02-30/0/items # input
HF_PATH=/home/tmp/qwen3-0.6b-hf-$(date +%Y-%m-%d-%H-%M-%S) # output
python3 -m maxtext.checkpoint_conversion.to_huggingface \
src/maxtext/configs/base.yml \
model_name=qwen3-0.6b \
scan_layers=true load_parameters_path=$SCANNED_CKPT_PATH \
base_output_directory=$HF_PATH \
skip_jax_distributed_system=true 
```

```
I0719 02:38:48.923796 140241813907264 to_huggingface.py:426] ✅ MaxText model successfully saved in HuggingFace format at /home/tmp/qwen3-0.6b-hf-2026-07-19-02-38-03
I0719 02:38:48.923956 140241813907264 to_huggingface.py:428] Elapse for transform and save: 0.34 min
I0719 02:38:48.928704 140241813907264 to_huggingface.py:543] Overall Elapse: 0.41 min
I0719 02:38:48.929090 140241813907264 utils.py:786] Peak Memory: 7.78 GB
```
