# [Issue #2739] [BUG] Unable to use PIPELINE_PARALLELISM_OPT_LEVEL_ENABLE: "A cycle is detected while visiting instruction %collective-permute"

source: https://github.com/AI-Hypercomputer/maxtext/issues/2739
state: closed | updated: 2026-04-28T18:23:36Z
labels: bug

## 正文

### Bug report

This script (launched with the correct hardware setup on slurm)

```
export XLA_FLAGS="--xla_gpu_enable_latency_hiding_scheduler=true --xla_gpu_enable_pipelined_p2p=true --xla_gpu_collective_permute_decomposer_threshold=0 --xla_disable_hlo_passes=rematerialization --xla_gpu_enable_nccl_comm_splitting=false --xla_gpu_enable_triton_gemm=false --xla_gpu_experimental_pipeline_parallelism_opt_level=PIPELINE_PARALLELISM_OPT_LEVEL_ENABLE"

python3 -m MaxText.train MaxText/configs/base.yml run_name=test_pp model_name=llama3.1-70b     steps=10 enable_checkpointing=false dataset_path=local dataset_type=synthetic     enable_goodput_recording=false dcn_pipeline_parallelism=2 dcn_fsdp_parallelism=1 ici_fsdp_parallelism=8 dcn_data_parallelism=1     hardware=gpu_multiprocess per_device_batch_size=2     max_target_length=512 attention=cudnn_flash_te num_layers_per_pipeline_stage=10 num_pipeline_microbatches=2
```


Fails with this error

```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/opt/maxtext/src/MaxText/train.py", line 558, in <module>
    app.run(main)
  File "/usr/local/lib/python3.12/dist-packages/absl/app.py", line 316, in run
    _run_main(main, args)
  File "/usr/local/lib/python3.12/dist-packages/absl/app.py", line 261, in _run_main
    sys.exit(main(argv))
             ^^^^^^^^^^
  File "/opt/maxtext/src/MaxText/train.py", line 554, in main
    run(config, recorder, diagnostic_config)
  File "/opt/maxtext/src/MaxText/train.py", line 549, in run
    train_loop(config, recorder)
  File "/opt/maxtext/src/MaxText/train.py", line 409, in train_loop
    compiled = p_train_step.lower(state, shaped_batch, init_rng).compile()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/stages.py", line 569, in compile
    self._lowering.compile(**kw),  # pytype: disable=wrong-keyword-args
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/interpreters/pxla.py", line 2527, in compile
    executable = UnloadedMeshExecutable.from_hlo(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/interpreters/pxla.py", line 3073, in from_hlo
    xla_executable = _cached_compilation(
                     ^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/interpreters/pxla.py", line 2854, in _cached_compilation
    xla_executable = compiler.compile_or_get_cached(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/compiler.py", line 478, in compile_or_get_cached
    return _compile_and_write_cache(
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/compiler.py", line 746, in _compile_and_write_cache
    executable = backend_compile_and_load(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/profiler.py", line 359, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/jax/jax/_src/compiler.py", line 362, in backend_compile_and_load
    return backend.compile_and_load(
           ^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Bad StatusOr access: FAILED_PRECONDITION: A cycle is detected while visiting instruction %collective-permute.7-bwd-send = (bf16[1,2,512,8192]{3,2,1,0}, u32[], token[]) send(%get-tuple-element.8683.0, %collective-permute.7-bwd-after-all.1), channel_id=223, frontend_attributes={_xla_gpu_collective_stream="p2p",_xla_send_recv_pipeline="0",_xla_send_recv_source_target_pairs={{0,8},{1,9},{2,10},{3,11},{4,12},{5,13},{6,14},{7,15}}}, control-predecessors={%collective-permute.7-bwd-recv-done, %collective-permute.7-bwd-recv}, metadata={op_name="jit(train_step)/jvp(TransformerLinenPure.apply)/TransformerLinenPure/decoder/pipeline_module/while/body/closed_call/pipeline_module.run_iteration_scannable/pipeline_module.run_one_iteration/pipeline_module.get_new_loop_state/concatenate" source_file="/opt/maxtext/src/MaxText/layers/pipeline.py" source_line=303 source_end_line=303 source_column=13 source_end_column=13} 

Directed cycle:
  collective-permute.7-bwd-recv-done
 collective-permute.7-bwd-send
 collective-permute.7-bwd-recv-done
```


This failure does not occur when run without `--xla_gpu_experimental_pipeline_parallelism_opt_level=PIPELINE_PARALLELISM_OPT_LEVEL_ENABLE`

### Logs/Output

See above

### Environment Information

Run with 16 B200s, but a similar error occurs for almost any configuration.

### Additional Context

N/A

## 评论 (2)

### chaserileyroberts · 2025-12-10

Attached HLOs from the failure. [pp_failure.zip](https://github.com/user-attachments/files/24086871/pp_failure.zip)

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.


