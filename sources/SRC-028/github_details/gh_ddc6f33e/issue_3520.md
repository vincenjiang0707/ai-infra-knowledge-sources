# [Issue #3520] [Bug] Qwix Quantization Qwen3-14B: jax._src.dtypes.InvalidInputException

source: https://github.com/AI-Hypercomputer/maxtext/issues/3520
state: open | updated: 2026-04-17T20:36:50Z
labels: bug

## 正文

### Bug report

Attempting to train Qwen3-14B on 4x NVIDIA GH200 120GB:
```
env CUDA_DEVICE_MAX_CONNECTIONS=1 XLA_PYTHON_CLIENT_MEM_FRACTION=0.9 \
python3 -m maxtext.trainers.pre_train.train /opt/maxtext/src/maxtext/configs/base.yml \
run_name=$SLURM_JOB_NAME \
model_name=qwen3-14b \
base_output_directory=/workspace/output \
dataset_type=hf \
hf_path=/share/dataset/fineweb-edu \
'hf_train_files=\"*.parquet\"' \
train_split=train \
hardware=gpu \
ici_fsdp_parallelism=4 \
use_qwix_quantization=True \
quantization=fp8_gpu \
quantize_kvcache=true \
enable_checkpointing=true \
async_checkpointing=false \
per_device_batch_size=2 \
tokenizer_type=huggingface \
tokenizer_path=/share/model/qwen3_14b_hf \
load_parameters_path=/share/model/qwen3_14b_orbax/0/items \
max_target_length=2048 \
num_epoch=1 \
steps=40 \
```

I ran into this issue upon enabling qwix quantization `use_qwix_quantization=True,quantization=fp8_gpu,quantize_kvcache=true`:

```
Traceback (most recent call last):
  File "/opt/jax/jax/_src/pjit.py", line 142, in _run_python_pjit
    out_flat, compiled, profiler, const_args = _pjit_call_impl_python(
                                               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/pjit.py", line 1178, in _pjit_call_impl_python
    return (compiled.unsafe_call(*computation.const_args, *args),
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/profiler.py", line 384, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/interpreters/pxla.py", line 396, in __call__
    input_bufs = self.in_handler(args)
                 ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/interpreters/pxla.py", line 293, in __call__
    return self.handler(input_buffers)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/profiler.py", line 384, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/interpreters/pxla.py", line 112, in shard_args
    arg = dtypes.canonicalize_value(arg)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/dtypes.py", line 393, in canonicalize_value
    raise InvalidInputException(
jax._src.dtypes.InvalidInputException: Argument 'ShapeDtypeStruct(shape=(40, 1024), dtype=float32, sharding=NamedSharding(mesh=Mesh('diloco': 1, 'data': 1, 'stage': 1, 'fsdp': 4, 'fsdp_transpose': 1, 'sequence': 1, 'context': 1, 'context_autoregressive': 1, 'tensor': 1, 'tensor_transpose': 1, 'tensor_sequence': 1, 'expert': 1, 'autoregressive': 1, axis_types=(Auto, Auto, Auto, Auto, Auto, Auto, Auto, Auto, Auto, Auto, Auto, Auto, Auto)), spec=P(), memory_kind=device))' of type <class 'jax.ShapeDtypeStruct'> is not a valid JAX type.
```

### Logs/Output

[step40_bs2_qkv_qfp8.train.log](https://github.com/user-attachments/files/26349467/step40_bs2_qkv_qfp8.train.log)

### Environment Information

Docker container: ghcr.io/nvidia/jax:maxtext-2026-03-21

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.48.01              Driver Version: 590.48.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GH200 120GB             On  |   00000009:01:00.0 Off |                    0 |
| N/A   46C    P0            100W /  900W |       5MiB /  97871MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GH200 120GB             On  |   00000019:01:00.0 Off |                    0 |
| N/A   46C    P0            104W /  900W |      40MiB /  97871MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA GH200 120GB             On  |   00000029:01:00.0 Off |                    0 |
| N/A   46C    P0             80W /  900W |      35MiB /  97871MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA GH200 120GB             On  |   00000039:01:00.0 Off |                    0 |
| N/A   45C    P0            105W /  900W |      23MiB /  97871MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

### Additional Context

_No response_

## 评论 (2)

### RissyRan · 2026-03-30

Hi @khatwanimohit, when you have a chance, could you help take a look about quantization issue? Thanks!

### JiwaniZakir · 2026-04-17

The `jax._src.dtypes.InvalidInputException` raised inside `pxla.py`'s `in_handler` during the input-dispatch phase typically signals a dtype mismatch where a compiled kernel is receiving a tensor of a type it wasn't traced/compiled for. The most likely culprit here is the interaction between `quantize_kvcache=true` and `use_qwix_quantization=True` with `fp8_gpu`: the Qwix-quantized KV cache may be producing fp8-typed tensors that then get fed into an attention or layer-norm kernel that was compiled expecting bfloat16/float32, which Qwen3-14B's GQA attention path (with its specific head grouping ratios) may expose differently than other models. Worth checking the Qwix quantization wrappers in `maxtext/layers/quantizations.py` (or wherever the kvcache quantization path is defined) to see if there's an explicit dtype cast applied after the KV cache dequantization step — that cast may be missing or incorrect for the fp8_gpu backend when `quantize_kvcache` is enabled simultaneously.
