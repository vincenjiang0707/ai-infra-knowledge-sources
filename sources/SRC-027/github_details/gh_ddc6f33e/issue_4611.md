# [Issue #4611] [bug] Dynamic TPU Metric Protobuf Import Causes Linkage Panic ('Check failed: GeneratedDatabase()->Add(...)')

source: https://github.com/AI-Hypercomputer/maxtext/issues/4611
state: open | updated: 2026-08-25T01:20:42Z
labels: bug

## 正文

### Bug report

1. Launch MaxText GRPO RL training on Cloud TPU v6e using `train_rl.py`.
    2. Keep default config parameters: `managed_mldiagnostics=True` (default in `configs/post_train/rl.yml`).
    3. Top-level import `from maxtext.common.managed_mldiagnostics import ManagedMLDiagnostics` in `metric_logger.py` executes C++ Protobuf registration at Python module load time.
    4. When `multiprocessing.spawn` re-imports module files in worker processes, dynamic Protobuf descriptor linkage panics on startup.
    
    **Expected:** Training process initializes without Protobuf symbol linkage errors.
    **Actual:** Process aborts immediately on startup with `Symbol name 'maxtext.TPUMetricService' is already defined`.

### Logs/Output

[libprotobuf ERROR google/protobuf/descriptor_database.cc:642] Symbol name "maxtext.TPUMetricService" is already defined.
    [libprotobuf FATAL google/protobuf/descriptor.cc:1370] CHECK failed: GeneratedDatabase()->Add(encoded_file_descriptor, size): 
    *** Abortcat traceback ***
      @     0x7f23a8123456  google::protobuf::GoogleOnceInitImpl()
      @     0x7f23a8123789  maxtext::TPUMetricService_default_instance()
      @     0x7f23a8124012  pybind11::cpp_function::dispatcher()
    Fatal Python error: Aborted
    
    Current thread 0x00007f23b1234700 (most recent call first):
      File "/usr/local/lib/python3.12/site-packages/clu/metric_writers/__init__.py", line 18 in <module>
      File "/usr/local/lib/python3.12/site-packages/maxtext/trainers/post_train/rl/train_rl.py", line 42 in <module>

### Environment Information

  - **Framework:** MaxText (GRPO RL / JAX Flax NNX)
  - **Hardware:** 8x Cloud TPU v6e (`ct6e-standard-8t`, topology `v6e-2x4`)
  - **OS:** Linux (GKE Standard Container Image)
  - **Python:** 3.12
  - **JAX:** 0.4.35+
  - **Inference Engine:** vLLM V1 TPU (`v0.20.1rc1.dev136`)


### Additional Context

**Org**: Google Cloud GTM: Global Solutions Team
    
 **Suggested Fix:**
    In `src/maxtext/common/metric_logger.py`, move `from maxtext.common.managed_mldiagnostics import ManagedMLDiagnostics` inside the `write_metrics_to_managed_mldiagnostics()` method so
  it loads lazily only when `config.managed_mldiagnostics=True`.


## 评论 (1)

### karajendran · 2026-08-25

### Update: Root Cause & Fix Identified in SFT / Pydantic Config
We tested `managed_mldiagnostics=True` on `maxtext.trainers.post_train.sft.train_sft` (MaxText 0.2.3 / current HEAD) and confirmed the exact point of failure.

 #### 1. Traceback
When initializing `ManagedMLDiagnostics(config)`:

    File "/deps/src/maxtext/common/metric_logger.py", line 111, in __init__
      ManagedMLDiagnostics(config)
    File "/deps/src/maxtext/common/managed_mldiagnostics.py", line 67, in __init__
      config_dict = {key: value for key, value in config.get_keys().items() if should_log_key(key, value)}
    File "/usr/local/lib/python3.12/site-packages/pydantic/main.py", line 1042, in __getattr__
      raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}')
    AttributeError: 'MaxTextConfig' object has no attribute 'get_keys'

  #### 2. Root Cause

  Following the migration from PyConfig to Pydantic MaxTextConfig, managed_mldiagnostics.py still expects the legacy get_keys() method on the config object.

  #### 3. Suggested Fix

  In src/maxtext/common/managed_mldiagnostics.py https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/common/managed_mldiagnostics.py#L67:

    # Before:
    config_dict = {key: value for key, value in config.get_keys().items() if should_log_key(key, value)}

    # After:
    raw_keys = config.get_keys() if hasattr(config, "get_keys") else dict(config)
    config_dict = {key: value for key, value in raw_keys.items() if should_log_key(key, value)}

