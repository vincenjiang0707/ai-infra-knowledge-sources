# [Issue #1434] When using dcn-DP and dcn-FSDP together got error when saving checkpoint.

source: https://github.com/AI-Hypercomputer/maxtext/issues/1434
state: open | updated: 2026-04-29T15:39:40Z
labels: 

## 正文

We tried multinode training with saving checkpoint. If dcn-dp = 2, dcn-fsdp=-1, the nodes in the first set of dcn-fsdp will always timeout. In the log below, we tried 16N training with dcn-dp=2 and dcn-fsdp=8, ici-fsdp=8. But the first 8Nodes all get timeout error. Could you check why this happens? (No error if we don't checkpoint)

```
completed step: 46, seconds: 64.453, TFLOP/s/device: 424.123, Tokens/s/device: 889.699, total_weights: 7304679, loss: 6.548
completed step: 47, seconds: 64.593, TFLOP/s/device: 423.203, Tokens/s/device: 887.769, total_weights: 7311923, loss: 6.544
completed step: 48, seconds: 64.648, TFLOP/s/device: 422.845, Tokens/s/device: 887.018, total_weights: 7310686, loss: 6.532
Waiting for step 50 to finish before checkpoint...
Waited 0.0007607936859130859 seconds for step 50 to finish before starting checkpointing.
I0320 20:56:05.504717 140582565907968 checkpoint_manager.py:1664] [process=15][thread=MainThread][wait_until_finished] Initiating wait for Save Finalize thread.
I0320 20:56:05.504896 140582565907968 checkpoint_manager.py:1682] [process=15][thread=MainThread][step=0][wait_until_finished] Waiting for Save Finalize thread (save_finalize) to complete.
E0320 20:56:05.504981 140582565907968 checkpoint_manager.py:1701] [process=15][thread=MainThread][step=0][wait_until_finished] Save Finalize thread (save_finalize) failed.
Traceback (most recent call last):
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1690, in wait_until_finished
    self._finalize_thread.join()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 151, in join
    raise self.exception
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 144, in run
    super().run()
  File "/pyenv/versions/3.10.15/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1787, in _finalize
    self._wait_for_checkpointers()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1659, in _wait_for_checkpointers
    self._checkpointer.wait_until_finished()  # pytype: disable=attribute-error
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 437, in wait_until_finished
    self._async_manager.wait_until_finished()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 234, in wait_until_finished
    self.check_for_errors()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 209, in check_for_errors
    raise exception  # pylint: disable=raising-bad-type
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 144, in _thread_func
    self._sync_fn(
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 82, in <lambda>
    self._sync_fn: Callable[[str], None] = lambda key: barrier_sync_fn(
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/multihost/utils.py", line 179, in _fn
    client.wait_at_barrier(key, timeout_ms)
jaxlib.xla_extension.XlaRuntimeError: DEADLINE_EXCEEDED: Barrier timed out. Id: 0_async_write_complete.0.1. This usually happens because a task triggered the barrier too early or too slowly. Please look at the task logs (both timed out and first task) to debug further.
# of tasks that reached the barrier: 8/16.
The first task at the barrier: /job:jax_worker/replica:0/task:13. Some timed out task names:
/job:jax_worker/replica:0/task:6
/job:jax_worker/replica:0/task:0
/job:jax_worker/replica:0/task:4
/job:jax_worker/replica:0/task:5
/job:jax_worker/replica:0/task:2
/job:jax_worker/replica:0/task:3
/job:jax_worker/replica:0/task:7
/job:jax_worker/replica:0/task:1


RPC: /tensorflow.CoordinationService/Barrier [type.googleapis.com/tensorflow.CoordinationServiceError='']
I0320 20:56:05.506100 140582565907968 checkpoint_manager.py:1722] [process=15][thread=MainThread][step=0][wait_until_finished] Resetting Save Finalize thread (save_finalize) running at step=0, also errors if any.
Traceback (most recent call last):
  File "/home/maxtext/MaxText/train.py", line 1004, in <module>
    app.run(main)
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/absl/app.py", line 308, in run
    _run_main(main, args)
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/absl/app.py", line 254, in _run_main
    sys.exit(main(argv))
  File "/home/maxtext/MaxText/train.py", line 1000, in main
    train_loop(config)
  File "/home/maxtext/MaxText/train.py", line 880, in train_loop
    if save_checkpoint(checkpoint_manager, int(step), state_to_save, config.dataset_type, data_iterator, config):
  File "/home/maxtext/MaxText/train.py", line 237, in save_checkpoint
    return checkpoint_manager.save(
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1145, in save
    self.wait_until_finished()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1690, in wait_until_finished
    self._finalize_thread.join()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 151, in join
    raise self.exception
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 144, in run
    super().run()
  File "/pyenv/versions/3.10.15/lib/python3.10/threading.py", line 953, in run
    self._target(*self._args, **self._kwargs)
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1787, in _finalize
    self._wait_for_checkpointers()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1659, in _wait_for_checkpointers
    self._checkpointer.wait_until_finished()  # pytype: disable=attribute-error
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 437, in wait_until_finished
    self._async_manager.wait_until_finished()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 234, in wait_until_finished
    self.check_for_errors()
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 209, in check_for_errors
    raise exception  # pylint: disable=raising-bad-type
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 144, in _thread_func
    self._sync_fn(
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/async_checkpointer.py", line 82, in <lambda>
    self._sync_fn: Callable[[str], None] = lambda key: barrier_sync_fn(
  File "/pyenv/versions/3.10.15/lib/python3.10/site-packages/orbax/checkpoint/multihost/utils.py", line 179, in _fn
    client.wait_at_barrier(key, timeout_ms)
jaxlib.xla_extension.XlaRuntimeError: DEADLINE_EXCEEDED: Barrier timed out. Id: 0_async_write_complete.0.1. This usually happens because a task triggered the barrier too early or too slowly. Please look at the task logs (both timed out and first task) to debug further.
# of tasks that reached the barrier: 8/16.
The first task at the barrier: /job:jax_worker/replica:0/task:13. Some timed out task names:
/job:jax_worker/replica:0/task:6
/job:jax_worker/replica:0/task:0
/job:jax_worker/replica:0/task:4
/job:jax_worker/replica:0/task:5
/job:jax_worker/replica:0/task:2
/job:jax_worker/replica:0/task:3
/job:jax_worker/replica:0/task:7
/job:jax_worker/replica:0/task:1


RPC: /tensorflow.CoordinationService/Barrier [type.googleapis.com/tensorflow.CoordinationServiceError='']
I0320 20:56:05.661344 138575314155072 grain_pool.py:400] Grain pool is exiting.
I0320 20:56:05.661531 138575314155072 grain_pool.py:405] Shutting down multiprocessing system.
I0320 20:56:09.454429 138575314155072 grain_pool.py:405] Shutting down multiprocessing system.
2025-03-20 20:56:09.547450: I external/xla/xla/pjrt/distributed/client.cc:150] Distributed task shutdown initiated.
2025-03-20 20:56:09.930431: I external/xla/xla/pjrt/distributed/client.cc:152] Distributed task shutdown result: OK
I0320 20:56:10.495969 140582565907968 grain_pool.py:482] Destroying multiprocess iterator.
LETE
```

Here are the configs:
```
2025-03-20 19:27:33.508912: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2025-03-20 19:27:33.524086: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2025-03-20 19:27:33.528313: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2025-03-20 19:27:34.279747: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
Updating keys from env and command line: ['base_output_directory']
Running Model: llama2-70b
Updating following parameters in config

base_emb_dim: 8192
base_num_query_heads: 64
base_num_kv_heads: 8
base_mlp_dim: 28672
base_num_decoder_layers: 80
head_dim: 128
mlp_activations: ['silu', 'linear']
vocab_size: 32000
logits_via_embedding: False
normalization_layer_epsilon: 1e-05
decoder_block: llama2
logical_axis_rules: [['norm', 'fsdp']]
Updating keys from model: ['base_emb_dim', 'base_num_query_heads', 'base_num_kv_heads', 'base_mlp_dim', 'base_num_decoder_layers', 'head_dim', 'mlp_activations', 'vocab_size', 'logits_via_embedding', 'normalization_layer_epsilon', 'decoder_block', 'logical_axis_rules']
Attempting to initialize the jax distributed system for GPU backend...
2025-03-20 19:27:37.400282: I external/tsl/tsl/platform/default/grpc_credentials.cc:30] gRPC insecure client credentials are used.
I0320 19:27:37.401081 140582565907968 distributed.py:119] Connecting to JAX distributed service on usmocpm2m-446-055:12345
2025-03-20 19:27:41.651707: I external/xla/xla/pjrt/distributed/client.cc:132] Connected to distributed JAX controller
2025-03-20 19:27:48.641533: I external/xla/xla/pjrt/pjrt_c_api_client.cc:127] PjRtCApiClient created.
I0320 19:27:48.740416 140582565907968 xla_bridge.py:906] Unable to initialize backend 'tpu': INTERNAL: Failed to open libtpu.so: libtpu.so: cannot open shared object file: No such file or directory
JAX global devices: [RocmDevice(id=0), RocmDevice(id=1), RocmDevice(id=2), RocmDevice(id=3), RocmDevice(id=4), RocmDevice(id=5), RocmDevice(id=6), RocmDevice(id=7), RocmDevice(id=8), RocmDevice(id=9), RocmDevice(id=10), RocmDevice(id=11), RocmDevice(id=12), RocmDevice(id=13), RocmDevice(id=14), RocmDevice(id=15), RocmDevice(id=16), RocmDevice(id=17), RocmDevice(id=18), RocmDevice(id=19), RocmDevice(id=20), RocmDevice(id=21), RocmDevice(id=22), RocmDevice(id=23), RocmDevice(id=24), RocmDevice(id=25), RocmDevice(id=26), RocmDevice(id=27), RocmDevice(id=28), RocmDevice(id=29), RocmDevice(id=30), RocmDevice(id=31), RocmDevice(id=32), RocmDevice(id=33), RocmDevice(id=34), RocmDevice(id=35), RocmDevice(id=36), RocmDevice(id=37), RocmDevice(id=38), RocmDevice(id=39), RocmDevice(id=40), RocmDevice(id=41), RocmDevice(id=42), RocmDevice(id=43), RocmDevice(id=44), RocmDevice(id=45), RocmDevice(id=46), RocmDevice(id=47), RocmDevice(id=48), RocmDevice(id=49), RocmDevice(id=50), RocmDevice(id=51), RocmDevice(id=52), RocmDevice(id=53), RocmDevice(id=54), RocmDevice(id=55), RocmDevice(id=56), RocmDevice(id=57), RocmDevice(id=58), RocmDevice(id=59), RocmDevice(id=60), RocmDevice(id=61), RocmDevice(id=62), RocmDevice(id=63), RocmDevice(id=64), RocmDevice(id=65), RocmDevice(id=66), RocmDevice(id=67), RocmDevice(id=68), RocmDevice(id=69), RocmDevice(id=70), RocmDevice(id=71), RocmDevice(id=72), RocmDevice(id=73), RocmDevice(id=74), RocmDevice(id=75), RocmDevice(id=76), RocmDevice(id=77), RocmDevice(id=78), RocmDevice(id=79), RocmDevice(id=80), RocmDevice(id=81), RocmDevice(id=82), RocmDevice(id=83), RocmDevice(id=84), RocmDevice(id=85), RocmDevice(id=86), RocmDevice(id=87), RocmDevice(id=88), RocmDevice(id=89), RocmDevice(id=90), RocmDevice(id=91), RocmDevice(id=92), RocmDevice(id=93), RocmDevice(id=94), RocmDevice(id=95), RocmDevice(id=96), RocmDevice(id=97), RocmDevice(id=98), RocmDevice(id=99), RocmDevice(id=100), RocmDevice(id=101), RocmDevice(id=102), RocmDevice(id=103), RocmDevice(id=104), RocmDevice(id=105), RocmDevice(id=106), RocmDevice(id=107), RocmDevice(id=108), RocmDevice(id=109), RocmDevice(id=110), RocmDevice(id=111), RocmDevice(id=112), RocmDevice(id=113), RocmDevice(id=114), RocmDevice(id=115), RocmDevice(id=116), RocmDevice(id=117), RocmDevice(id=118), RocmDevice(id=119), RocmDevice(id=120), RocmDevice(id=121), RocmDevice(id=122), RocmDevice(id=123), RocmDevice(id=124), RocmDevice(id=125), RocmDevice(id=126), RocmDevice(id=127)]
Jax distributed system initialized on GPU!
Not using emergency checkpoint, ignoring local_checkpoint_directory, local_checkpoint_period, use_replicator_service and replicator_backup_interval_minutes
dataset_type set to hf, will use keys['hf_path']='parquet', keys['hf_data_dir']='' and keys['hf_train_files']='/mnt/shared_nfs/c4_en_train/*.parquet' to read data
Config param activations_in_float32: False
Config param adam_b1: 0.9
Config param adam_b2: 0.95
Config param adam_eps: 1e-08
Config param adam_eps_root: 0.0
Config param adam_weight_decay: 0.1
Config param add_bos: True
Config param add_eos: True
Config param allow_split_physical_axes: False
Config param ar_cache_axis_order: 1,2,0,3
Config param async_checkpointing: True
Config param attention: cudnn_flash_te
Config param attention_type: global
Config param attn_logits_soft_cap: None
Config param autoregressive_decode_assert: 
Config param base_config: base.yml
Config param base_emb_dim: 8192
Config param base_mlp_dim: 28672
Config param base_num_decoder_layers: 80
Config param base_num_kv_heads: 8
Config param base_num_query_heads: 64
Config param base_output_directory: /mnt/shared_nfs/output/gpu_train_test_llama2_70b_96N_short_run
Config param capacity_factor: -1.0
Config param cast_logits_to_fp32: True
Config param checkpoint_dir: /mnt/shared_nfs/output/gpu_train_test_llama2_70b_96N_short_run/gpu_train_test_llama2_70b_16N_short_run/checkpoints/
Config param checkpoint_is_quantized: False
Config param checkpoint_period: 50
Config param checkpoint_storage_target_data_file_size_bytes: 2147483648
Config param checkpoint_storage_use_ocdbt: True
Config param checkpoint_storage_use_zarr3: True
Config param collect_stack_trace: False
Config param compile_topology: 
Config param compile_topology_num_slices: -1
Config param compiled_trainstep_file: 
Config param compute_axis_order: 0,1,2,3
Config param context: remat
Config param cosine_learning_rate_final_fraction: 0.1
Config param custom_mesh: 
Config param data_sharding: (('data', 'stage', 'fsdp', 'fsdp_transpose', 'sequence', 'tensor', 'tensor_sequence', 'expert', 'autoregressive'),)
Config param data_shuffle_seed: 0
Config param dataset_name: c4/en:3.0.1
Config param dataset_path: 
Config param dataset_type: hf
Config param dcn_autoregressive_parallelism: 1
Config param dcn_data_parallelism: 2
Config param dcn_expert_parallelism: 1
Config param dcn_fsdp_parallelism: -1
Config param dcn_fsdp_transpose_parallelism: 1
Config param dcn_parallelism: [2, 1, -1, 1, 1, 1, 1, 1, 1]
Config param dcn_pipeline_parallelism: 1
Config param dcn_sequence_parallelism: 1
Config param dcn_tensor_parallelism: 1
Config param dcn_tensor_sequence_parallelism: 1
Config param decode_sampling_nucleus_p: -1
Config param decode_sampling_strategy: greedy
Config param decode_sampling_temperature: 1.0
Config param decode_sampling_top_k: 0
Config param decoder_block: llama2
Config param decoder_layer_input: device
Config param dpo_beta: 0.1
Config param dpo_label_smoothing: 0.0
Config param dropout_rate: 0.0
Config param dtype: bfloat16
Config param dump_hlo: False
Config param dump_hlo_delete_local_after: True
Config param dump_hlo_gcs_dir: 
Config param dump_hlo_local_dir: /tmp/xla_dump/
Config param dump_hlo_module_name: jit_train_step
Config param dump_hlo_upload_all: False
Config param dump_hlo_xla_flags: 
Config param emb_dim: 8192
Config param enable_checkpoint_cloud_logger: False
Config param enable_checkpointing: True
Config param enable_data_shuffling: True
Config param enable_dropout: True
Config param enable_emergency_checkpoint: False
Config param enable_goodput_recording: False
Config param enable_jax_profiler: False
Config param enable_model_warmup: False
Config param enable_pathways_goodput: False
Config param enable_single_controller: False
Config param enable_single_replica_ckpt_restoring: False
Config param eval_data_columns: ['text']
Config param eval_dataset_name: c4/en:3.0.1
Config param eval_interval: -1
Config param eval_per_device_batch_size: 7
Config param eval_split: validation
Config param eval_steps: -1
Config param expansion_factor_real_data: -1
Config param final_logits_soft_cap: None
Config param force_unroll: False
Config param fused_mlp: False
Config param fused_qkv: False
Config param gcs_metrics: False
Config param global_batch_size_to_eval_on: 896
Config param global_batch_size_to_load: 896
Config param global_batch_size_to_load_eval: 896
Config param global_batch_size_to_train_on: 896
Config param global_parameter_scale: 1
Config param goodput_upload_interval_seconds: 60
Config param gradient_accumulation_steps: 1
Config param gradient_clipping_threshold: 1.0
Config param grain_eval_files: 
Config param grain_train_files: 
Config param grain_worker_count: 1
Config param hardware: gpu
Config param head_dim: 128
Config param hf_access_token: 
Config param hf_data_dir: 
Config param hf_eval_files: None
Config param hf_eval_split: 
Config param hf_path: parquet
Config param hf_train_files: /mnt/shared_nfs/c4_en_train/*.parquet
Config param ici_autoregressive_parallelism: 1
Config param ici_data_parallelism: 1
Config param ici_expert_parallelism: 1
Config param ici_fsdp_parallelism: 8
Config param ici_fsdp_transpose_parallelism: 1
Config param ici_parallelism: [1, 1, 8, 1, 1, 1, 1, 1, 1]
Config param ici_pipeline_parallelism: 1
Config param ici_sequence_parallelism: 1
Config param ici_tensor_parallelism: 1
Config param ici_tensor_sequence_parallelism: 1
Config param inference_benchmark_test: False
Config param inference_metadata_file: 
Config param inference_microbenchmark_log_file_path: 
Config param inference_microbenchmark_loop_iters: 10
Config param inference_microbenchmark_prefill_lengths: 64,128,256,512,1024
Config param inference_microbenchmark_stages: prefill,generate
Config param inference_server: MaxtextInterleavedServer
Config param init_weights_seed: 0
Config param jax_cache_dir: ~/jax_cache
Config param jax_debug_log_modules: 
Config param jax_distributed_initialization_timeout: 300
Config param jax_profiler_port: 9999
Config param key_proj: remat
Config param kv_quant_axis: heads_and_dkv
Config param kv_quant_dtype: int8
Config param learning_rate: 3e-05
Config param learning_rate_schedule_steps: 150
Config param load_balance_loss_weight: 0.01
Config param load_from_prefill_dir: False
Config param load_full_state_path: 
Config param load_parameters_path: 
Config param local_checkpoint_directory: 
Config param local_checkpoint_period: 0
Config param log_config: True
Config param log_period: 50
Config param logical_axis_rules: (('activation_batch', ('data', 'fsdp', 'fsdp_transpose', 'expert')), ('activation_batch_no_exp', ('data', 'fsdp', 'fsdp_transpose')), ('activation_embed_and_logits_batch', ('data', 'stage', 'fsdp', 'fsdp_transpose', 'expert')), ('activation_heads', ('tensor', 'sequence', 'tensor_sequence')), ('activation_kv_heads', ('tensor', 'sequence', 'tensor_sequence')), ('activation_length', ('sequence',)), ('activation_norm_length', ('tensor_sequence', 'sequence')), ('activation_embed', 'tensor'), ('activation_mlp', ('tensor', 'tensor_sequence')), ('activation_kv', ('tensor', 'tensor_sequence')), ('activation_prefill_kv_batch', ('data', 'fsdp', 'fsdp_transpose', 'expert')), ('activation_kv_batch', ('data', 'fsdp', 'fsdp_transpose', 'expert')), ('activation_kv_head_dim', ('tensor', 'tensor_sequence')), ('activation_vocab', ('tensor', 'sequence', 'tensor_sequence')), ('activation_vocab', 'tensor'), ('activation_vocab', 'tensor_sequence'), ('activation_vocab', 'sequence'), ('activation_stage', 'stage'), ('activation_exp', 'expert'), ('mlp', ('fsdp_transpose', 'tensor', 'tensor_sequence', 'autoregressive')), ('vocab', ('tensor', 'tensor_sequence', 'autoregressive')), ('embed', ('fsdp', 'fsdp_transpose', 'sequence', 'expert')), ('embed', ('fsdp', 'sequence', 'expert')), ('embed_no_exp', ('fsdp', 'fsdp_transpose', 'sequence')), ('embed_no_exp', ('fsdp', 'sequence')), ('q_heads', ('tensor', 'tensor_sequence', 'autoregressive')), ('heads', ('tensor', 'tensor_sequence', 'autoregressive')), ('layers', 'stage'), ('kv', ()), ('kv_heads', ('tensor', 'tensor_sequence', 'autoregressive')), ('kv_head_dim', ()), ('cache_batch_prefill', ()), ('cache_batch', ()), ('cache_heads', ('autoregressive', 'tensor', 'tensor_sequence')), ('cache_kv', ()), ('cache_sequence', ()), ('exp', 'expert'), ('norm', 'fsdp'))
Config param logits_dot_in_fp32: False
Config param logits_via_embedding: False
Config param matmul_precision: default
Config param max_checkify: False
Config param max_corpus_chars: 10000000
Config param max_prefill_predict_length: 64
Config param max_target_length: 8192
Config param megablox: False
Config param mesh_axes: ['data', 'stage', 'fsdp', 'fsdp_transpose', 'sequence', 'tensor', 'tensor_sequence', 'expert', 'autoregressive']
Config param metrics_dir: /mnt/shared_nfs/output/gpu_train_test_llama2_70b_96N_short_run/gpu_train_test_llama2_70b_16N_short_run/metrics/
Config param metrics_file: 
Config param micro_batch_size_to_eval_on: 896
Config param micro_batch_size_to_train_on: 896
Config param mlp_activations: ['silu', 'linear']
Config param mlp_dim: 28672
Config param mlpwi: remat
Config param mlpwi_0: remat
Config param mlpwi_1: remat
Config param mlpwo: remat
Config param model_call_mode: 
Config param model_name: llama2-70b
Config param monitor_goodput: False
Config param normalization_layer_epsilon: 1e-05
Config param normalize_embedding_logits: True
Config param num_decoder_layers: 80
Config param num_experts: 1
Config param num_experts_per_tok: 1
Config param num_kv_heads: 8
Config param num_layers_per_pipeline_stage: 1
Config param num_pipeline_microbatches: -1
Config param num_pipeline_repeats: -1
Config param num_query_heads: 64
Config param num_slices: 16
Config param opt_type: adamw
Config param optimizer_memory_host_offload: False
Config param out_proj: remat
Config param param_scan_axis: 1
Config param per_device_batch_size: 7
Config param pipeline_delay_activation_forwarding: False
Config param prefill_cache_axis_order: 1,2,0,3
Config param prefill_cache_dir: 
Config param profile_cleanly: True
Config param profiler: 
Config param profiler_steps: 5
Config param prometheus_port: 0
Config param prompt: I love to
Config param qkv_proj: remat
Config param quant_cfg_path: 
Config param quantization: 
Config param quantization_local_shard_count: 16
Config param quantize_kvcache: False
Config param query_proj: remat
Config param ragged_block_size: 256
Config param record_internal_nn_metrics: 0
Config param remat_policy: full
Config param replicate_quant_scale: False
Config param replicator_backup_interval_minutes: 0
Config param reshape_q: False
Config param reuse_example_batch: 0
Config param rope_max_timescale: 10000
Config param rope_min_timescale: 1
Config param run_name: gpu_train_test_llama2_70b_16N_short_run
Config param sa_block_kv: 512
Config param sa_block_kv_compute: 512
Config param sa_block_kv_dkv: 512
Config param sa_block_kv_dkv_compute: 512
Config param sa_block_kv_dq: 512
Config param sa_block_q: 512
Config param sa_block_q_dkv: 512
Config param sa_block_q_dq: 512
Config param sa_k_layout: HEAD_DIM_MINOR
Config param sa_q_layout: HEAD_DIM_MINOR
Config param sa_use_fused_bwd_kernel: False
Config param sa_v_layout: HEAD_DIM_MINOR
Config param save_config_to_gcs: False
Config param save_quantized_params_path: 
Config param scan_layers: True
Config param scan_pipeline_iterations: True
Config param set_remat_policy_on_layers_per_stage: False
Config param set_remat_policy_on_pipeline_iterations: True
Config param sharding_tolerance: 0.02
Config param skip_first_n_steps_for_profiler: 3
Config param skip_jax_distributed_system: False
Config param sliding_window_size: 0
Config param stack_prefill_result_cache: False
Config param stack_trace_interval_seconds: 600
Config param stack_trace_to_cloud: False
Config param steps: 150
Config param target_eval_loss: 0.0
Config param tensorboard_dir: /mnt/shared_nfs/output/gpu_train_test_llama2_70b_96N_short_run/gpu_train_test_llama2_70b_16N_short_run/tensorboard/
Config param tokenize_eval_data: True
Config param tokenize_train_data: True
Config param tokenizer_path: /mnt/shared_nfs/llama3.1-8b-tokenizer
Config param train_data_columns: ['text']
Config param trainable_position_size: -1
Config param upload_all_profiler_results: False
Config param use_dpo: False
Config param use_iota_embed: True
Config param use_post_attn_norm: False
Config param use_post_ffw_norm: False
Config param use_ragged_attention: False
Config param use_replicator_service: False
Config param use_untrainable_positional_embedding: False
Config param use_vertex_tensorboard: False
Config param using_pipeline_parallelism: False
Config param value_proj: remat
Config param vertex_tensorboard_project: 
Config param vertex_tensorboard_region: 
Config param vocab_size: 32000
Config param warmup_steps_fraction: 0.002
Config param weight_dtype: bfloat16
System Information: Jax Version: 0.4.35.dev20241202+8985f20e4
System Information: Jaxlib Version: 0.4.35
System Information: Jax Backend: PJRT C API
rocm 60301
WARNING: 'dataset_path' might be pointing your local file system
WARNING: 'base_output_directory' might be pointing your local file system
Num_devices: 128, shape (2, 1, 64, 1, 1, 1, 1, 1, 1)
I0320 19:27:51.360803 140582565907968 _schedule.py:74] A polynomial schedule was set with a non-positive `transition_steps` value; this results in a constant schedule with value `init_value`.
Setting up checkpoint logger...
Creating checkpoint manager...
I0320 19:27:51.651366 140582565907968 checkpoint_manager.py:557] [process=15][thread=MainThread] CheckpointManager init: checkpointers=None, item_names=('items',), item_handlers={'items': <orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeCheckpointHandler object at 0x7fd972768b20>}, handler_registry=None
I0320 19:27:51.651550 140582565907968 composite_checkpoint_handler.py:224] Deferred registration for item: "items". Adding handler `<orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeCheckpointHandler object at 0x7fd972768b20>` for item "items" and save args `<class 'orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeSaveArgs'>` and restore args `<class 'orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeRestoreArgs'>` to `_handler_registry`.
I0320 19:27:51.651610 140582565907968 composite_checkpoint_handler.py:489] Initialized registry DefaultCheckpointHandlerRegistry({('items', <class 'orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeSaveArgs'>): <orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeCheckpointHandler object at 0x7fd972768b20>, ('items', <class 'orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeRestoreArgs'>): <orbax.checkpoint._src.handlers.pytree_checkpoint_handler.PyTreeCheckpointHandler object at 0x7fd972768b20>}).
I0320 19:27:51.651901 140582565907968 abstract_checkpointer.py:35] orbax-checkpoint version: 0.6.4
I0320 19:27:51.652071 140582565907968 async_checkpointer.py:65] [process=15][thread=MainThread] Using barrier_sync_fn: <function get_barrier_sync_fn.<locals>._fn at 0x7fd9727e2440> timeout: 300 secs and primary_host=0 for async checkpoint writes
I0320 19:27:51.652165 140582565907968 utils.py:253] [process=15][thread=MainThread] Waiting with jax/sync_global_devices("CheckpointManager:create_directory")
usmocpm2m-446-084:17:664 [2] NCCL INFO RCCL_MSCCL_ENABLE set by environment to 0.
usmocpm2m-446-084:17:664 [2] NCCL INFO ROCr version 1.14

## 评论 (1)

### NuojCheng · 2026-04-29

It's been a while and let me know if the issue still exists. I will then take a look.
