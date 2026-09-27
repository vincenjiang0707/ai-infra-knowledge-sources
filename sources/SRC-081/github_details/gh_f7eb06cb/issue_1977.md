# [Issue #1977] [BUG] Vram on cuda:0 usage vs 4.2.5

source: https://github.com/ModelCloud/GPTQModel/issues/1977
state: closed | updated: 2026-01-01T09:38:54Z
labels: bug

## 正文

Trying to quantize with gptqmodel commit hash d8f3c78988bb8f11982a5e52361537ffba05d145
with `mock_quantization=False`, and got an error on first layer with experts (layer 1) (GLM-4.5-Air):

```
Quantizing mlp.experts.32.gate_proj in layer  [1 of 45] ████-------------------------------------------------------------------------------------------------| 0:13:41 / 5:14:43 [2/46] 4.3%Traceback (most recent call last):
  File "/home/ubuntu/Documents/Quantize/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py", line 489, in <module>
    model.quantize(
    ~~~~~~~~~~~~~~^
        calibration_dataset,
        ^^^^^^^^^^^^^^^^^^^^
        batch_size=BATCH_SIZE,
        ^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/models/base.py", line 717, in quantize
    return module_looper.loop(
           ~~~~~~~~~~~~~~~~~~^
        backend=backend,
        ^^^^^^^^^^^^^^^^
        fail_safe=self.quantize_config.fail_safe,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 850, in loop
    name, m = fut.result()
              ~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 449, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/utils/threadx.py", line 360, in _run
    result = fn(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 842, in _process_on_worker
    proc.process(module=nm)
    ~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/gptq_processor.py", line 123, in process
    wq, q_scales, q_zeros, q_g_idx, duration, avg_loss, damp_percent, nsamples = g.quantize()
                                                                                 ~~~~~~~~~~^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 354, in quantize
    Hinv, damp = self.hessian_inverse(self.H)
                 ~~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 257, in hessian_inverse
    H2 = torch.linalg.cholesky(H2)
RuntimeError: cusolver error: CUSOLVER_STATUS_INTERNAL_ERROR, when calling `cusolverDnCreate(handle)`. If you keep seeing this error, you may use `torch.backends.cuda.preferred_linalg_library()` to try linear algebra operators with other supported backends. See https://pytorch.org/docs/stable/backends.html#torch.backends.cuda.preferred_linalg_library
```

## 评论 (43)

### Qubitium · 2025-10-04

Another threading bug. This one is wild. So it just suddently stopped working. Looks like linalg ops are flaky under threading.

### Qubitium · 2025-10-04

@avtc  Both issue should be fixed for good. Please try it now. Will reopen if you still get errors. 

### avtc · 2025-10-04

```
INFO  ModuleLooper: forward start (processor=`gptq`, layer=`model.layers.1`, subset=3/7, batches=1057)                     %
Quantizing mlp.experts.32.gate_proj in layer  [1 of 45] █------------------------------------| 0:12:39 / 4:50:57 [2/46] 4.3%Traceback (most recent call last):
  File "/home/ubuntu/Documents/Quantize/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py", line 489, in <module>
    model.quantize(
    ~~~~~~~~~~~~~~^
        calibration_dataset,
        ^^^^^^^^^^^^^^^^^^^^
        batch_size=BATCH_SIZE,
        ^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/models/base.py", line 946, in quantize
    return module_looper.loop(
           ~~~~~~~~~~~~~~~~~~^
        backend=backend,
        ^^^^^^^^^^^^^^^^
        fail_safe=self.quantize_config.fail_safe,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 860, in loop
    name, m = fut.result()
              ~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/utils/threadx.py", line 367, in _run
    result = fn(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 852, in _process_on_worker
    proc.process(module=nm)
    ~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/gptq_processor.py", line 123, in process
    wq, q_scales, q_zeros, q_g_idx, duration, avg_loss, damp_percent, nsamples = g.quantize()
                                                                                 ~~~~~~~~~~^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 354, in quantize
    Hinv, damp = self.hessian_inverse(self.H)
                 ~~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 250, in hessian_inverse
    H2 = TORCH_LINALG.cholesky(H2)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/utils/safe.py", line 47, in locked
    return attr(*args, **kwargs)
RuntimeError: cusolver error: CUSOLVER_STATUS_INTERNAL_ERROR, when calling `cusolverDnCreate(handle)`. If you keep seeing this error, you may use `torch.backends.cuda.preferred_linalg_library()` to try linear algebra operators with other supported backends. See https://pytorch.org/docs/stable/backends.html#torch.backends.cuda.preferred_linalg_library
terminate called without an active exception
Aborted (core dumped)
```

Could be a memory issue? With 10 samples instead of 1084 - it does not throw.

The dataset to repro with GLM-4.5-Air:
```
import random

# Set seed for reproducibility
random.seed(42)

# 1. General Language
c4 = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
).shuffle(seed=42).select(range(300)) # 300

# 2. Reasoning
gsm8k = load_dataset("gsm8k", "main", split="train").shuffle(seed=42).select(range(300)) # 300
arc = load_dataset("ai2_arc", "ARC-Challenge", split="train").shuffle(seed=42).select(range(300)) # 300

# 3. Technical/Development
humaneval = load_dataset("openai_humaneval", split="test").shuffle(seed=42).select(range(164)) # 164

# 4. Instruction-Following
alpaca = load_dataset("tat41s0u-lab/alpaca", split="train").shuffle(seed=42).select(range(20)) # 20

# Process each dataset and extract text
calibration_texts = []

# Process C4 dataset
for item in c4:
    calibration_texts.append(item["text"])

# Process GSM8K dataset
for item in gsm8k:
    calibration_texts.append(f"Question: {item['question']}\nAnswer: {item['answer']}")

# Process ARC dataset
for item in arc:
    calibration_texts.append(f"{item['question']}")

# Process HumanEval dataset
for item in humaneval:
    calibration_texts.append(item["prompt"])

# Process Alpaca dataset
for item in alpaca:
    input_text = f"\nInput: {item['input']}" if item.get("input") else ""
    calibration_texts.append(f"Instruction: {item['instruction']}{input_text}\nOutput: {item['output']}")

# Final shuffle to mix domains
random.shuffle(calibration_texts)

# Verify length
print(f"Total samples: {len(calibration_texts)}")

# Use with GPTQModel
calibration_dataset = calibration_texts  # This is your final calibration dataset
```

### Qubitium · 2025-10-04

@avtc  What! This looks to be a torch internal bug inferfacing with low level cusolver. I got the same crash as yours and solved with the PR fixes. Let me triple check your stacktrace to see how the heck it is still happening. There is a gigantic global lock on the linalg ops now so there is not possible for two thrads to execute anything torch.linalg related. 

Can you send me your full running quant script and I will replicted on my end. 

So I don't think it has any absolute relationship with your calibration dataset size or the memory usage of the ops. The dataset size only changed the timing of the calls. 

### avtc · 2025-10-04

@Qubitium 
The full script.
[quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py](https://github.com/user-attachments/files/22692254/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py)

I have lowered number of samples in:
```
c4 = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
).shuffle(seed=42).select(range(100)) # 300
```
and got another error, look like memory related:
```
Quantizing mlp.experts.33.gate_proj in layer  [1 of 45] █------------------------------------| 0:11:43 / 4:29:29 [2/46] 4.3%Traceback (most recent call last):
  File "/home/ubuntu/Documents/Quantize/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py", line 489, in <module>
    model.quantize(
    ~~~~~~~~~~~~~~^
        calibration_dataset,
        ^^^^^^^^^^^^^^^^^^^^
        batch_size=BATCH_SIZE,
        ^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/models/base.py", line 946, in quantize
    return module_looper.loop(
           ~~~~~~~~~~~~~~~~~~^
        backend=backend,
        ^^^^^^^^^^^^^^^^
        fail_safe=self.quantize_config.fail_safe,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 860, in loop
    name, m = fut.result()
              ~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 449, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/utils/threadx.py", line 367, in _run
    result = fn(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 852, in _process_on_worker
    proc.process(module=nm)
    ~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/gptq_processor.py", line 123, in process
    wq, q_scales, q_zeros, q_g_idx, duration, avg_loss, damp_percent, nsamples = g.quantize()
                                                                                 ~~~~~~~~~~^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 494, in quantize
    W1[:, i:] -= err1.unsqueeze(1).matmul(Hinv1[i, i:].unsqueeze(0))
                 ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`
terminate called without an active exception
Aborted (core dumped)
```

### avtc · 2025-10-04

It there a switch to turn off data-parallelism to check without it?

### avtc · 2025-10-04

After lowering samples more it passes the layer 1, will check how it goes.
```
# 1. General Language (40% - 410 samples)
c4 = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
).shuffle(seed=42).select(range(100)) # 300

# 2. Reasoning (30% - 307 samples)
gsm8k = load_dataset("gsm8k", "main", split="train").shuffle(seed=42).select(range(100)) # 300
arc = load_dataset("ai2_arc", "ARC-Challenge", split="train").shuffle(seed=42).select(range(300)) # 300

# 3. Technical/Development (20% - 205 samples)
humaneval = load_dataset("openai_humaneval", split="test").shuffle(seed=42).select(range(164)) # 164

# 4. Instruction-Following (10% - 102 samples)
alpaca = load_dataset("tatsu-lab/alpaca", split="train").shuffle(seed=42).select(range(20)) # 20
```

### Qubitium · 2025-10-04

Can you make it crash again and show me your gptqmodel quant logs on cli before the crash? I need to see your gpu memory usage per device which is now printed per completed quant module

It could be memory pressure. 

### avtc · 2025-10-04

@Qubitium 
Set back dataset size, the issue reproduced.
It does not log experts before the exception.
```
NFO  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INFO  | process     | layer     | module               | loss             | samples     | damp        | time      | fwd_time     | (v)ram                                                                                                              | dynamic     |
INFO  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INFO  | gptq        | 1         | self_attn.k_proj     | 0.0000091407 | 247943      | 0.05000     | 0.960     | 17.797       | cuda:0=14.4GB, cuda:1=9.0GB, cuda:2=6.3GB, cuda:3=7.4GB, cuda:4=6.9GB, cuda:5=8.8GB, cuda:6=7.0GB, cuda:7=7.5GB     | None        | 
INFO  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INFO  | gptq        | 1         | self_attn.v_proj     | 0.0000003122 | 247943      | 0.05000     | 1.007     | 17.797       | cuda:0=14.4GB, cuda:1=9.0GB, cuda:2=6.3GB, cuda:3=7.4GB, cuda:4=6.9GB, cuda:5=8.8GB, cuda:6=7.0GB, cuda:7=7.5GB     | None        | 
INFO  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INFO  | gptq        | 1         | self_attn.q_proj     | 0.0000121996 | 247943      | 0.05000     | 1.558     | 17.797       | cuda:0=14.4GB, cuda:1=9.0GB, cuda:2=6.3GB, cuda:3=7.4GB, cuda:4=6.9GB, cuda:5=8.8GB, cuda:6=7.0GB, cuda:7=7.5GB     | None        | 
INFO  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INFO  ModuleLooper: forward start (processor=`gptq`, layer=`model.layers.1`, subset=2/7, batches=1057)                     %
INFO  GC completed in 13.993s (pass #1).                                                                                   %
INFO  | gptq        | 1         | self_attn.o_proj     | 0.0000000035 | 247943      | 0.05000     | 2.590     | 66.516       | cuda:0=5.9GB, cuda:1=3.5GB, cuda:2=6.7GB, cuda:3=3.5GB, cuda:4=4.1GB, cuda:5=4.1GB, cuda:6=3.5GB, cuda:7=4.1GB      | None        | 
INFO  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INFO  ModuleLooper: forward start (processor=`gptq`, layer=`model.layers.1`, subset=3/7, batches=1057)                     %
Quantizing mlp.experts.32.gate_proj in layer  [1 of 45] █------------------------------------| 0:14:30 / 5:33:30 [2/46] 4.3%Traceback (most recent call last):
  File "/home/ubuntu/Documents/Quantize/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py", line 489, in <module>
    model.quantize(
    ~~~~~~~~~~~~~~^
        calibration_dataset,
        ^^^^^^^^^^^^^^^^^^^^
        batch_size=BATCH_SIZE,
        ^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/models/base.py", line 946, in quantize
    return module_looper.loop(
           ~~~~~~~~~~~~~~~~~~^
        backend=backend,
        ^^^^^^^^^^^^^^^^
        fail_safe=self.quantize_config.fail_safe,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 860, in loop
    name, m = fut.result()
              ~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/utils/threadx.py", line 367, in _run
    result = fn(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/module_looper.py", line 852, in _process_on_worker
    proc.process(module=nm)
    ~~~~~~~~~~~~^^^^^^^^^^^
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/looper/gptq_processor.py", line 123, in process
    wq, q_scales, q_zeros, q_g_idx, duration, avg_loss, damp_percent, nsamples = g.quantize()
                                                                                 ~~~~~~~~~~^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 354, in quantize
    Hinv, damp = self.hessian_inverse(self.H)
                 ~~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/quantization/gptq.py", line 250, in hessian_inverse
    H2 = TORCH_LINALG.cholesky(H2)
  File "/home/ubuntu/git/avtc/GPTQModel/gptqmodel/utils/safe.py", line 47, in locked
    return attr(*args, **kwargs)
RuntimeError: cusolver error: CUSOLVER_STATUS_INTERNAL_ERROR, when calling `cusolverDnCreate(handle)`. If you keep seeing this error, you may use `torch.backends.cuda.preferred_linalg_library()` to try linear algebra operators with other supported backends. See https://pytorch.org/docs/stable/backends.html#torch.backends.cuda.preferred_linalg_library
terminate called without an active exception
terminate called recursively
terminate called recursively
Aborted (core dumped)
```

[gptq_log_infatuation_time_10_04_2025_10h_30m_21s.log](https://github.com/user-attachments/files/22694341/gptq_log_infatuation_time_10_04_2025_10h_30m_21s.log)

### avtc · 2025-10-04

The issue can be closed as related to low vram or large dataset. (btw same dataset worked for me before data parallel)

### Qubitium · 2025-10-04

I still consider this a bug. Data parallel should not bloat vram so much so to cause oom. Please check if latest main solved this. Now barriers are setup at every forward point to make sure all bg threads are done before proceeding. 

### avtc · 2025-10-06

@Qubitium please push `gptqmodel.utils.disk` to `main`

### Qubitium · 2025-10-06

Fixed

### avtc · 2025-10-06

@Qubitium 
I have tried latest `main` with `"cuda:per": 1` and got CUDA OOM. I test converting GLM-4.5-Air to 8bit with same dataset of 1084 samples that worked before data parallel and offload.
Error happen after the first layer with experts finished, on processing second layer with experts.

The trace:
```
INFO  | gptq    | 1     | mlp.experts.123.down_proj | 0.0000000031 | 17310   | 0.05000 | 0.333 | 82.792   | cuda:0=18.1GB, cuda:1=9.5GB, cuda:2=7.5GB, cuda:3=9.0GB, cuda:4=23.0GB, cuda:5=7.6GB, cuda:6=6.6GB, cuda:7=23.4GB      |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  gc.collect(2) reclaimed 4182 objects in 0.231s                                                           %
Loading checkpoint shards: 100%|████████████████████████████████████████████████| 47/47 [00:03<00:00, 12.42it/s]
...
INFO  gc.collect(2) reclaimed 2033 objects in 0.204s                                                           m
INFO  | process | layer | module                    | loss         | samples | damp    | time  | fwd_time | (v)ram                                                                                                                 | dynamic |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  | gptq    | 2     | self_attn.k_proj          | 0.0000000443 | 247943  | 0.05000 | 0.806 | 33.977   | cuda:0=8.9GB, cuda:1=15.9GB, cuda:2=16.3GB, cuda:3=18.6GB, cuda:4=10.2GB, cuda:5=14.8GB, cuda:6=14.8GB, cuda:7=10.4GB  |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  | gptq    | 2     | self_attn.v_proj          | 0.0000000054 | 247943  | 0.05000 | 0.839 | 33.977   | cuda:0=8.9GB, cuda:1=15.9GB, cuda:2=16.3GB, cuda:3=18.6GB, cuda:4=10.2GB, cuda:5=14.8GB, cuda:6=14.8GB, cuda:7=10.4GB  |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  | gptq    | 2     | self_attn.q_proj          | 0.0000001415 | 247943  | 0.05000 | 1.256 | 33.977   | cuda:0=8.9GB, cuda:1=15.9GB, cuda:2=16.3GB, cuda:3=18.6GB, cuda:4=10.2GB, cuda:5=14.8GB, cuda:6=14.8GB, cuda:7=10.4GB  |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  gc.collect(2) reclaimed 10677 objects in 0.222s                                                          .
INFO  | gptq    | 2     | self_attn.o_proj          | 0.0000000000 | 247943  | 0.05000 | 3.584 | 70.584   | cuda:0=11.1GB, cuda:1=22.3GB, cuda:2=21.5GB, cuda:3=22.7GB, cuda:4=10.2GB, cuda:5=14.8GB, cuda:6=21.9GB, cuda:7=15.3GB |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  gc.collect(2) reclaimed 2403 objects in 0.203s                                                           %
Forward start (layer=`model.layers.2`, subset=3/7, batches=1057) [2 of 45] -----| 0:44:21 / 11:20:02 [3/46] 6.5%Traceback (most recent call last):
  File "/home/ubuntu/Documents/Quantize/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py", line 495, in <module>
    model.quantize(
    ~~~~~~~~~~~~~~^
        calibration_dataset,
        ^^^^^^^^^^^^^^^^^^^^
        batch_size=BATCH_SIZE,
        ^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 940, in quantize
    return module_looper.loop(
           ~~~~~~~~~~~~~~~~~~^
        backend=backend,
        ^^^^^^^^^^^^^^^^
        fail_safe=self.quantize_config.fail_safe,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 792, in loop
    forward_outputs = self._run_forward_batches(
        module=module,
    ...<10 lines>...
        reuse_kv=reuse_kv,
    )
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 244, in _run_forward_batches
    return self._run_forward_batches_parallel(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        module=module,
        ^^^^^^^^^^^^^^
    ...<11 lines>...
        devices=devices,
        ^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 394, in _run_forward_batches_parallel
    batch_idx, module_output, kv_next = fut.result()
                                        ~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/utils/threadx.py", line 377, in _run
    result = fn(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/utils/looper_helpers.py", line 348, in forward_batch_worker
    module_output = module(*inputs, **additional_inputs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 395, in forward
    hidden_states = self.mlp(hidden_states)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 345, in forward
    hidden_states = self.moe(hidden_states, topk_indices, topk_weights).view(*orig_shape)
                    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 331, in moe
    expert_output = expert(expert_input)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/transformers/models/glm4_moe/modeling_glm4_moe.py", line 223, in forward
    down_proj = self.down_proj(self.act_fn(self.gate_proj(x)) * self.up_proj(x))
                                           ~~~~~~~~~~~~~~^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/nn_modules/hooked_linear.py", line 221, in forward
    self.forward_hook(self, (input,), output)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 456, in hook
    return inner_hook(module, new_inputs, new_output)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/gptq_processor.py", line 108, in tmp
    g.add_batch(inp[0].data, out.data)  # noqa: F821
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/quantization/gptq.py", line 136, in add_batch
    self.process_batch(inp)
    ~~~~~~~~~~~~~~~~~~^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/quantization/gptq.py", line 188, in process_batch
    self.H = self.H.to(device=reshaped_inp.device)
             ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 64.00 MiB. GPU 0 has a total capacity of 23.58 GiB of which 7.50 MiB is free. Including non-PyTorch memory, this process has 23.55 GiB memory in use. Of the allocated memory 22.76 GiB is allocated by PyTorch, and 332.86 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
```

The quant log attached. Will try with lower samples amount.

[gptq_log_womanizers_time_10_06_2025_15h_37m_30s.log](https://github.com/user-attachments/files/22723273/gptq_log_womanizers_time_10_06_2025_15h_37m_30s.log)

### avtc · 2025-10-06

@Qubitium tried with `offload_to_disk=False`:
```
Traceback (most recent call last):
  File "/home/ubuntu/Documents/Quantize/quantize-glm4.5-Air-gptqmodel-moe-prune-smart-4.py", line 495, in <module>
    model.quantize(
    ~~~~~~~~~~~~~~^
        calibration_dataset,
        ^^^^^^^^^^^^^^^^^^^^
        batch_size=BATCH_SIZE,
        ^^^^^^^^^^^^^^^^^^^^^^
        )
        ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 940, in quantize
    return module_looper.loop(
           ~~~~~~~~~~~~~~~~~~^
        backend=backend,
        ^^^^^^^^^^^^^^^^
        fail_safe=self.quantize_config.fail_safe,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 628, in loop
    input_cache = self.cache_inputs(layers=layers,
                                    calibration_data=processor.calibration_dataset,
                                    use_cache=False)
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/looper/module_looper.py", line 537, in cache_inputs
    self.gptq_model.reload_turtle_model()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/models/base.py", line 1326, in reload_turtle_model
    assert turtle_model is not None and  model_local_path is not None
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

### Qubitium · 2025-10-06

@avtc My bad. Never tested with offload off. Oops. Will fix this.

Right now my focus is to fix a very nasty segfault that is semi random no matter what tricks i tried.

### avtc · 2025-10-06

After using 100 samples less from c4 (so 984 in total), the CUDA OOM happen layer later.
'''
INFO  gc.collect(2) reclaimed 10515 objects in 0.218s                                                          %
INFO  | gptq    | 3     | self_attn.o_proj          | 0.0000000001 | 181592  | 0.05000 | 2.454 | 57.949   | cuda:0=9.3GB, cuda:1=11.1GB, cuda:2=11.2GB, cuda:3=10.9GB, cuda:4=10.8GB, cuda:5=11.0GB, cuda:6=11.2GB, cuda:7=11.7GB  |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  gc.collect(2) reclaimed 539 objects in 0.215s                                                            %
Forward start (layer=`model.layers.3`, subset=3/7, batches=957) [3 of 45] ------| 1:03:11 / 12:06:36 [4/46] 8.7%
'''

### avtc · 2025-10-06

After using 100 less samples from c4, in total 884, the CUDA OOM happen another layer later.
```
INFO  | gptq    | 4     | self_attn.o_proj          | 0.0000000002 | 129228  | 0.05000 | 2.916 | 66.576   | cuda:0=8.6GB, cuda:1=21.5GB, cuda:2=19.1GB, cuda:3=6.4GB, cuda:4=23.6GB, cuda:5=19.7GB, cuda:6=13.3GB, cuda:7=14.9GB   |         |
INFO  +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+
INFO  gc.collect(2) reclaimed 3322 objects in 0.282s                                                           %
Forward start (layer=`model.layers.4`, subset=3/7, batches=857) [4 of 45] -----| 1:27:06 / 13:21:19 [5/46] 10.9%
```
could be vram leak from layer-to-layer or idk.

### Qubitium · 2025-10-06

@avtc  Pull main. I added requirements.txt back so you can easily install updates that are required by new pulls. you need to pull since logbar got updated. 

Core logging got major update where  `forward` (pre-quant) and `forward replay` (post-quant) are both showing as separate progress bars you we can see actuall progress and states instead of getting it `stuck` for large MoE models..

<img width="3912" height="522" alt="Image" src="https://github.com/user-attachments/assets/82ecb6cb-0157-4f55-b384-dd07ca69e87c" />

This is my test on `test_qwen3_moe.py` script. Each layer has 389 modules and gpu vram is very stable between layers. 

Can you do a screen capture too. I weant to see if glm 4.5 air different or not. I don't understand why is glm 4.,5 blowing up oom on forwarding when your log that you provided shows only about 11GB vram in use before forwarding starts and it just blows up the rest of the 13 (24GB-11GB)? Is glm 4.5 air even wider MoE than qwen3 moe? Qwen 3 MoE with 1024 , batch size=4 is only using about 9GB of vram during quant. 

Submodule finalzing (post entire layer quant) is also it's own progress bar as well.  logbar update allowed me to stack unlimitd pbs. 


### Qubitium · 2025-10-06

@avtc btw. Also post what linux os, kerenel version, and cpu you are using. I want to think about why our vram gc strategies are so different. 

### avtc · 2025-10-06

Will check tomorrow 

### avtc · 2025-10-07

1. 
> After using 100 samples less from c4 (so 984 in total), the CUDA OOM happen layer later. ''' INFO gc.collect(2) reclaimed 10515 objects in 0.218s % INFO | gptq | 3 | self_attn.o_proj | 0.0000000001 | 181592 | 0.05000 | 2.454 | 57.949 | cuda:0=9.3GB, cuda:1=11.1GB, cuda:2=11.2GB, cuda:3=10.9GB, cuda:4=10.8GB, cuda:5=11.0GB, cuda:6=11.2GB, cuda:7=11.7GB | | INFO +---------+-------+---------------------------+--------------+---------+---------+-------+----------+------------------------------------------------------------------------------------------------------------------------+---------+ INFO gc.collect(2) reclaimed 539 objects in 0.215s % Forward start (layer=`model.layers.3`, subset=3/7, batches=957) [3 of 45] ------| 1:03:11 / 12:06:36 [4/46] 8.7% '''

After moving `DEVICE_THREAD_POOL.wait()` to execute after each layer, I was able to proceed to layer 4.
And during this test `cuda:per` was set to `4`.

2. Then I have tried to lower `empty_cache_every_n` from `1024` to `10` and got an error at the start of quantization:
```
Exception in thread DP-Janitor:ass #1).                                                                                                   
Traceback (most recent call last): █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:00:14 / 0:10:44 [1/46] 2.2%
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/threading.py", line 1043, in _bootstrap_inner░░| 0:00:14 / 0:10:44 [1/46] 2.2%
    self.run()
    ~~~~~~~~^^
  File "/home/ubuntu/.pyenv/versions/3.13.7t/lib/python3.13t/threading.py", line 994, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/gptqmodel/utils/threadx.py", line 1355, in _janitor_loop
    use_fn()
    ~~~~~~^^
  File "/home/ubuntu/venvs/gptqmodelt/lib/python3.13t/site-packages/torch/cuda/memory.py", line 224, in empty_cache
    torch._C._cuda_emptyCache()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
torch.AcceleratorError: CUDA error: unspecified launch failure
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```
But with `empty_cache_every_n=128` it proceeded.

3. I have very long `Forward start` `Forward rows` for self_attn.o_proj on every layer [with experts], so wanted to try with offload off to see if it makes it faster:

<img width="1655" height="490" alt="Image" src="https://github.com/user-attachments/assets/3fe0c327-93be-4bcd-931a-b5ecc135c572" />

<img width="1721" height="901" alt="Image" src="https://github.com/user-attachments/assets/9a4789a2-a0fe-4eff-8834-82d3c145a39f" />

<img width="1695" height="894" alt="Image" src="https://github.com/user-attachments/assets/18dc60d4-2d84-4e78-ae23-1a12daf51d59" />

Here is finalization screenshot of layer 3:

<img width="1696" height="883" alt="Image" src="https://github.com/user-attachments/assets/72ec8319-1fa1-4b45-bbc1-b183423e1e57" />

Wondering how to make it faster, and why it become so slow.

4. I am using: 
kubuntu 24.04.2 LTS
kernel: 6.11.0-29-generic (had to pause kernel updates to not reinstall the nvidia driver with each update)
cpu: EPYC 9124
mb: ASUS K14PA-U12
ram: 64GB DDR5 4800
8x3090 gpus connected: 1 in pcie-x16, other ones in MCIO x8 ports via cpayne mcio-to-pcie gen5 adapters.
nvme: 990 Pro 4TB

### avtc · 2025-10-07

@Qubitium 

> 3\. I have very long `Forward start` `Forward rows` for self_attn.o_proj on every layer [with experts], so wanted to try with offload off to see if it makes it faster:

I have fixed turning off the offload, and the result is same - it process very long and the VRAM usage is close to 24Gb on each card.

### Qubitium · 2025-10-07

@avtc Pull `main`. Segfault fixed and now layer finalization (very slow for moe due to so many modules) is now concurrent with next layer quantization. As you have proven, the oom issue is unrelated to offload which only deal with cpu memory.

The logs/progressbars are also more active/accurate at stages. 

### Qubitium · 2025-10-07

@avtc On test_qwen3_moe.py (my go to small moe test) where each layer has 380+ modules, my a100 test gpu only use 12GB of vram with 2048 samples of data at batch_size=8. test_qwen3_next with 1700+ moe modules per layer uses 22GB of ram with 256 rows of calib with batch_size=1.

Something is terribly wrong with GLM 4.5 inference that is blowing up memory. Because based on Qwen3-Moe (similar size to GLM 4.5 air), it should be well under 20GB of vram usage with no OOM. Even Qwen3-Next with 3x the size of moe of GLM 4.5 Air, I am not hitting 24GB. 

### avtc · 2025-10-07

@Qubitium 
GLM-4.5-Air is 106B model, it is larger than Qwen3-Next. There is no OOM after adding DEVICE_THREAD_POOL.wait() to execute after each layer. 

But the VRAM usage and time (probably related to VRAM used) for self_attn.o_proj forward pass is too high.

### avtc · 2025-10-07

@Qubitium 
I see, the forward is for expert layers, that's why it takes so much vram and time. (I have disabled quantization for self_attn, but the forward still takes very long before expert layers).

As far as i remember there was an option to enable or disable forward buffering. Idk which mode remains after the switch was removed. But i have used disabled forward buffer option with successful quantization to 8bit of GLM-4.5-Air with 1084 samples.

### avtc · 2025-10-07

I am trying now https://github.com/avtc/GPTQModel/commit/ff3777bcf7f064f0f591930b453a0054e6565477 based on checkpoint 30d87512b17f3cccb03fb8b431911b0d0f386466 (with offload, few commits before data parallel) + `ASYNC_WORKER.join()` on layer finished + lock `Q.to`, to compare with, and it behave much better than latest main with data parallel.
I was able to start and run with 1084 samples with additionally excluded self_attn modules without CUDA OOM.
The estimate for full quantization is around 2 hours, first 5 layers took ~17.5 minutes.
<img width="1696" height="882" alt="Image" src="https://github.com/user-attachments/assets/1cd19a09-0105-4c38-a259-025334146fc7" />

I have tried same exclusion config but with `220` samples on latest main, and it CUDA OOM on layer 5, and proceed very slowly.
```
dynamic = {
    r"-:model.embed_tokens.weight": {},
    r"-:.*shared_experts": {},
    r"-:.*shared_head": {},
    r"-:lm_head.weight": {},
    r"-:.*mlp.down": {},
    r"-:.*mlp.gate": {}, # vllm does not support exclusion of only gate, need to exclude down & up as well
    r"-:.*mlp.up": {},
    r"-:.*post_attention_layernorm": {},
    r"-:.*self_attn": {},
    r"-:.*norm.weight": {},
    r"-:.*enorm": {},
    r"-:.*hnorm": {},
    r"-:.*eh_proj": {},
    r"-:.*input_layernorm": {},
    }
```

The script to repro:
[quantize-glm4.5-air-gptqmodel-2.py](https://github.com/user-attachments/files/22755591/quantize-glm4.5-air-gptqmodel-2.py)

run on gptqmodel venv:
```
export CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True,max_split_size_mb:128"
export PYTHON_GIL=0
python /home/ubuntu/Documents/Quantize/quantize-glm4.5-air-gptqmodel-2.py
```

### Qubitium · 2025-10-08

@avtc  Please run `tests/test_torch_replicate.py` and `test_p2p.py`.  The replicate test wil check/benchmark the copy mech I used for data parallel which will contribute to the slowness you obvservd if it degrades badly. 

```
# a100 on amd 7343
tests/test_torch_replicate.py::test_torch_replicate_benchmark strategy      time_avg_s    time_min_s    time_max_s    mem_avg_MB    mem_min_MB    mem_max_MB
----------  ------------  ------------  ------------  ------------  ------------  ------------
replicate         0.0018        0.0011        0.0022      128.0000      128.0000      128.0000
deepcopy          0.0033        0.0027        0.0039      384.0000      384.0000      384.0000
```

### Qubitium · 2025-10-08

@avtc  Running your script now. Btw, I like your tp padding code. I think this is a great feature to have for packing! 

-> Doing the padding conversion which is super slow on my slow cpu/disk. Going to restart and skip this. 

Btw, I see that you thermal limitd your 3090 to 280 watts? I remember 3090 is 350-375w? Is 280w a sweespot for 3090 where anymore probably doesn't squeeze much out of it? 

### Qubitium · 2025-10-08

@avtc  I can confirm even on layer 0, forwarding (before quant) the moe layers is using max `26.8GB` on gpu:1 on my test. Since my gpu has more vram it didn't need to gc internally so frequently but will likely result in your same oom issues in subsequent layers. So forget about layer1+. The core issue is still the moe layers in glm is cause huge vram spike during forward. Looks like on 3090, the memory pressure is causing torch/cuda's memmory allocator to do internal gc much faster allowing you to progress even beyond layer 0. There is a PYTORCH_ALLOC_CONF you can tweak and see if tweaking the `gc` values to be more aggressive will fix your oom issues.  you need search for PYTORCH_ALLOC_CONF. 

If we fix layer0 vram usage, we should be able to fix everything thing else. 

There is an unrelated regression where on `main` my small llama3_2 on 1 gpu test is regression time by 50% which is unusual which may be related to the slow down you are seeing, separate from the oom issue. 

### avtc · 2025-10-08

> [@avtc](https://github.com/avtc) Running your script now. Btw, I like your tp padding code. I think this is a great feature to have for packing!
> 
> -> Doing the padding conversion which is super slow on my slow cpu/disk. Going to restart and skip this.

Quantizing without padding is OK, it is required to make inference work with multi-gpu. Padding done once and subsequent runs will reuse padded model.

> Btw, I see that you thermal limitd your 3090 to 280 watts? I remember 3090 is 350-375w? Is 280w a sweespot for 3090 where anymore probably doesn't squeeze much out of it?

yes, 280w is sweet spot, it does heat less, less stressing to PSU, and performance is about 5% less than full 350w.

### avtc · 2025-10-08

```
# 3090 on amd 9124, RAM: 64GB DDR5 4800 (1 module)
tests/test_torch_replicate.py::test_replicate_from_cpu_to_multiple_gpu XFAIL (torch.nn.parallel.replicate requires GPU r...)
INFO  gc.collect() reclaimed 141 objects in 0.067s                                                                                 
PASSED
tests/test_torch_replicate.py::test_torch_replicate_benchmark strategy      time_avg_s    time_min_s    time_max_s    mem_avg_MB    mem_min_MB    mem_max_MB
----------  ------------  ------------  ------------  ------------  ------------  ------------
replicate         0.0110        0.0108        0.0114      128.0000      128.0000      128.0000
deepcopy          0.0134        0.0130        0.0146      384.0000      384.0000      384.0000
PASSED

========================================================= warnings summary =========================================================
tests/test_torch_replicate.py:130
  /home/ubuntu/git/avtc/GPTQModel/tests/test_torch_replicate.py:130: PytestUnknownMarkWarning: Unknown pytest.mark.cuda - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.cuda

tests/test_torch_replicate.py:131
  /home/ubuntu/git/avtc/GPTQModel/tests/test_torch_replicate.py:131: PytestUnknownMarkWarning: Unknown pytest.mark.inference - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.inference

tests/test_torch_replicate.py:144
  /home/ubuntu/git/avtc/GPTQModel/tests/test_torch_replicate.py:144: PytestUnknownMarkWarning: Unknown pytest.mark.cuda - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.cuda

tests/test_torch_replicate.py:145
  /home/ubuntu/git/avtc/GPTQModel/tests/test_torch_replicate.py:145: PytestUnknownMarkWarning: Unknown pytest.mark.inference - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.inference

tests/test_torch_replicate.py:163
  /home/ubuntu/git/avtc/GPTQModel/tests/test_torch_replicate.py:163: PytestUnknownMarkWarning: Unknown pytest.mark.cuda - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.cuda

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================ 2 passed, 1 xfailed, 5 warnings in 10.59s =============================================
```

```
(gptqmodelt) ubuntu@ubuntu-k14pau12:~/git/avtc/GPTQModel$ python tests/test_p2p.py 
Devices:
  cuda:0 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:1 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:2 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:3 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:4 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:5 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:6 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6
  cuda:7 NVIDIA GeForce RTX 3090 23.6 GiB CC 8.6

P2P capability (rows=src, cols=dst):
 0:   -  yes yes yes yes yes yes yes
 1: yes   -  yes yes yes yes yes yes
 2: yes yes   -  yes yes yes yes yes
 3: yes yes yes   -  yes yes yes yes
 4: yes yes yes yes   -  yes yes yes
 5: yes yes yes yes yes   -  yes yes
 6: yes yes yes yes yes yes   -  yes
 7: yes yes yes yes yes yes yes   -
```



### Qubitium · 2025-10-08

> replicate         0.0110        0.0108        0.0114      128.0000      128.0000      128.0000
> deepcopy          0.0134        0.0130        0.0146      384.0000      384.0000      384.0000

Why is your `deepcopy` 4x slower than my system? It should be much faster. I am on ddr4 2900 ecc. You are on ddr5, 1.5x the ram speed + 1 gen later CPU with probably higher freq? So strange my `deepcopy` is faster than your `replicate`.

You have pcie5 vs my pcie4 but you have bifurcation enabled for the the 8x3090 but doesn't account for the latency since the copy test is that large. Weird. 

But I don't think it is the cause of the slowness. There is a regression with one of the commits. 4x slower is still fast. 

### avtc · 2025-10-08

I have only 1 module installed, you probably have 8, memory bandwidth limited by module speed * number of modules.

### avtc · 2025-10-27

I have tried to quantize to int4 the cerebras/GLM-4.6-REAP-268B-A32B with two versions - latest main (V5) + exclude cuda:0 when balancing VS pre V5 with slight adjustments (https://github.com/avtc/GPTQModel/tree/feature/v4-adjust-balancing-strategy-save-vram-on-model-save) based on https://github.com/ModelCloud/GPTQModel/commit/30d87512b17f3cccb03fb8b431911b0d0f386466 (with offload, few commits before data parallel) + ASYNC_WORKER.join() on layer finished + lock Q.to + exclude cuda:0 when balancing, i.e,. MEMORY mode.

With `V5` i have tried 768 first samples from c4 and it segfault after layer 39 on 4 x 3090. On 8 x 3090 it usually throws illegal cuda memory access or accelerate invalid argument, so could not use 8 well. Probably it will pass with 512 samples, will check later.

With `pre V5` i have successfully quantized with 1536 samples (first 1024 from c4 + other from gsm/humaneval/arc/alpaca). On 8x3090. It looks like it proceed much faster (but need to compare with exact amount of samples), the VRAM usage is lower and could handle much more samples/layer size.

<img width="1697" height="868" alt="Image" src="https://github.com/user-attachments/assets/52d9fc7e-ca6d-460f-aa1e-20fc833b2caf" />

Actual time taken was around 7 hours. 1536 samples ~520K tokens.

### Qubitium · 2025-10-27

@avtc I have pushed quantized glm 4.6 reap model to hf..can you download and run it to see if it inference correctly? 

[hf.co/modelcloud](https://huggingface.co/ModelCloud/GLM-4.6-REAP-268B-A32B-GPTQMODEL-W4A16)

### avtc · 2025-10-27

What dataset did you use, how many samples, and how much time it took to produce int4 reap 268B? How many GPUs?

Check result: it works.

Request: `Create a Playable Synth Keyboard using html, css, js in a single html file`
With sampling: T0.6, minp=0, maxp=0.95, top-k=40:

<img width="2560" height="1440" alt="Image" src="https://github.com/user-attachments/assets/939ad36c-1e96-42d5-81bb-09e1b12be340" />

From single shot - mouse click work, keyboard keys not work.



### Qubitium · 2025-10-27


> Check result: it works.
> 
> Request: `Create a Playable Synth Keyboard using html, css, js in a single html file` With sampling: T0.6, minp=0, maxp=0.95, top-k=40:
> 
> <img alt="Image" width="2000" height="1440" src="https://private-user-images.githubusercontent.com/10050240/505975291-939ad36c-1e96-42d5-81bb-09e1b12be340.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjE1Njg2NDYsIm5iZiI6MTc2MTU2ODM0NiwicGF0aCI6Ii8xMDA1MDI0MC81MDU5NzUyOTEtOTM5YWQzNmMtMWU5Ni00MmQ1LTgxYmItMDllMWIxMmJlMzQwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMjclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDI3VDEyMzIyNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVkYTgwZTlmYTgxNWJlMTQ0OWY3ZDU3ODU1MGMzOTA5M2QwOTYzMjM5ZWM0NmVmNzM4NWY0NGViNThkMjAzYWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.2PPxPQ5d-LFYTLDyLT7TO_ltf0CAnreZjhkWqsyBReA">
> From single shot - mouse click work, keyboard keys not work.

is this good or bad vs glm 4.6 regular gptq (I have also uploaded 2) and vs your glm 4.5 air quants?

### avtc · 2025-10-27

Sorry, I wanted to check different sampling params for your quant, but had issues with server.
I cannot run int4 regular quant GLM-4.6 / GLM-4.5, as does not fit into VRAM.

Your reap quant without sampling params override:

<img width="2560" height="1440" alt="Image" src="https://github.com/user-attachments/assets/72dc67c0-eb1f-4d1f-aa93-dde31cff6e23" />

Looks much better and works OK with keys/mouse.
Sometimes generation can be fixed by using different sampling params.
(asked two additional requests to fix black keys placement, but it failed)

GLM-4-6 full with 3.0bpw H6 exl3 without sampling params override:

<img width="2560" height="1440" alt="Image" src="https://github.com/user-attachments/assets/b21d4eeb-7d7e-4f01-95b3-45503019e28d" />

GLM-4.5-Air int8 g64 one of my latest quant with dynamic exclusions of all except of non-shared experts and mlp, 1024 c4 en samples, without sampling params override:

<img width="2560" height="1440" alt="Image" src="https://github.com/user-attachments/assets/814366bc-6770-44f3-8033-4170077ddfe5" />

I want to make GLM-4.6-268B int4 g128 quant, as context window is too low with g32 for my setup (~60K).
Btw intermediate size of GLM-4.5 and GLM-4.6 does not require padding to work with tp=8 for group size=128.
--- Update: I was wrong, if shared experts are quantized - their [1536] size must be padded to 2048, or group size must be 32 or 64 at least for them.
And for vllm need to use `--enable-experts-parallel` - this for non-shared experts if their group size is 128.

### Qubitium · 2025-12-23

I think  we can close this?

### avtc · 2025-12-23

I will compare the 5.0 (before data parallel) vs latest main+moe_bypass_routing with force_serial and exclude_device_0_from_compute - for time estimate and vram usage with same amount of calibration data little bit later.

One known not fixed issue is when `offload_to_disk=True` - the latest main uses +5Gb VRAM on device 0 `versus offload_to_disk=False` (while with 5.0 before data parallel it worked fine it seems, but need to recheck)

### avtc · 2026-01-01

vram usage fix proposed in https://github.com/ModelCloud/GPTQModel/pull/2325
