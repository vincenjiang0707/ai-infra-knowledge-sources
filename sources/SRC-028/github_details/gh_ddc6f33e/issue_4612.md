# [Issue #4612] [bug] Mid-Training Evaluation Loop Spawns Subprocess Claiming /dev/vfio/0 ('Device or resource busy')

source: https://github.com/AI-Hypercomputer/maxtext/issues/4612
state: open | updated: 2026-07-26T14:07:37Z
labels: bug

## 正文

### Bug report


    1. Deploy single-host GRPO RL training job on an 8-chip Cloud TPU v6e slice (`v6e-2x4`).
    2. Set `eval_interval=10` and `num_test_batches=25` in training parameters.
    3. Upon hitting Step 10, `train_rl.py` lines 747–755 invoke `evaluate(...)`, which calls `create_models_and_meshes(...)` in `model_creation_utils.py`.
    4. `create_models_and_meshes` executes `jax.devices()`, attempting to open `/dev/vfio/0` while the main RL trainer process holds the hardware lock.
    
    **Expected:** In-flight evaluation reuses active TPU device handles without opening new hardware locks.
    **Actual:** Evaluation fails with `RuntimeError: Unable to initialize backend 'tpu': FAILED_PRECONDITION: open(/dev/vfio/0): Device or resource busy`.


### Logs/Output

 FAILED_PRECONDITION: TPU initialization failed: open(/dev/vfio/0): Device or resource busy
```json
    Traceback (most recent call last):
      File "//train.py", line 140, in <module>
        rl_train(config_argv, {})
      File "/usr/local/lib/python3.12/site-packages/maxtext/trainers/post_train/rl/train_rl.py", line 546, in rl_train
        reference_model, reference_mesh, actor_model, actor_mesh, rollout_mesh = model_creation_utils.create_models_and_meshes(...)
      File "/usr/local/lib/python3.12/site-packages/maxtext/utils/model_creation_utils.py", line 650, in create_models_and_meshes
        reference_model, reference_mesh = from_pretrained(trainer_config, devices=trainer_devices, wrap_with_tunix_adapter=True)
      File "/usr/local/lib/python3.12/site-packages/jax/_src/xla_bridge.py", line 482, in devices
        return get_backend(backend).devices()
    RuntimeError: Unable to initialize backend 'tpu': FAILED_PRECONDITION: TPU initialization failed: open(/dev/vfio/0): Device or resource busy
```

### Environment Information

   - **Framework:** MaxText (GRPO RL / JAX Flax NNX)
    - **Hardware:** 8x Cloud TPU v6e (`ct6e-standard-8t`, topology `v6e-2x4`)
    - **OS:** Linux (GKE Standard Container Image)
    - **Python:** 3.12
    - **JAX:** 0.4.35+
    - **Inference Engine:** vLLM V1 TPU (`v0.20.1rc1.dev136`)


### Additional Context

Org: Google Cloud GTM: Global Solutions Team
**Suggested Fix:**
    In `src/maxtext/trainers/post_train/rl/train_rl.py`, update `evaluate(...)` to accept the existing active `actor_mesh` and `trainer_devices` directly, avoiding
  `create_models_and_meshes(...)` re-execution on single-host TPU hardware.


## 评论 (0)
