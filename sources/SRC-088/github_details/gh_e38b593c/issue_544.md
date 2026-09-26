# [Issue #544] [Bug]: qwen3-8b dflash

source: https://github.com/vllm-project/speculators/issues/544
state: closed | updated: 2026-06-18T17:03:20Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM 0.18.0
- Speculators 0.5.0
- CUDA 13.0
- PyTorch 2.9
- Transformers 5.5.4
- Hardware A100
- Model qwen3-8b


### 🐛 Describe the bug

[14:41:10] INFO     Started distributed with local_rank=1, world_size=2                                                                                                                                                                   utils.py:39
[14:41:10] INFO     Started distributed with local_rank=0, world_size=2                                                                                                                                                                   utils.py:39
           INFO     Loading vocab mappings from '/output/dflash_qwen3_8b_onestepmodel/d2t.npy' and 'output/dflash_qwen3_8b_onestepmodel/t2d.npy'                                                      train.py:161
[14:41:12] WARNING  Added <|MASK|> to tokenizer, mask_token_id=151669 (tokenizer len=151670, vocab_size=151936)                                                                                                                           utils.py:85
2026-05-25 14:41:24.498 | INFO     | speculators.utils.loading:_resolve_file:83 - Loading from local directory: /output/e2e_78_bl140_260410/v3-20260509-033321/checkpoint-968-merged
2026-05-25 14:41:24.584 | INFO     | speculators.utils.loading:_resolve_file:83 - Loading from local directory: /output/e2e_78_bl140_260410/v3-20260509-033321/checkpoint-968-merged
2026-05-25 14:41:24.614 | INFO     | speculators.utils.loading:_resolve_file:83 - Loading from local directory: /output/e2e_78_bl140_260410/v3-20260509-033321/checkpoint-968-merged
2026-05-25 14:41:24.644 | INFO     | speculators.utils.loading:_resolve_file:83 - Loading from local directory: /doutput/e2e_78_bl140_260410/v3-20260509-033321/checkpoint-968-merged
2026-05-25 14:41:24.742 | INFO     | speculators.utils.loading:_resolve_file:83 - Loading from local directory: /output/e2e_78_bl140_260410/v3-20260509-033321/checkpoint-968-merged
2026-05-25 14:41:24.772 | INFO     | speculators.utils.loading:_resolve_file:83 - Loading from local directory: /output/e2e_78_bl140_260410/v3-20260509-033321/checkpoint-968-merged
Loading dataset from disk: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 22/22 [00:00<00:00, 97.34it/s]
Loading dataset from disk: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 22/22 [00:00<00:00, 174.17it/s]
Loading dataset from disk: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 22/22 [00:00<00:00, 478.85it/s]
Loading dataset from disk: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 22/22 [00:00<00:00, 83.92it/s]
[14:41:34] INFO     No previous checkpoint found. Starting from scratch.                                                                                                                                                                trainer.py:90
[14:41:39] INFO     Training epoch 1/5 started                                                                                                                                                                                         trainer.py:306
[14:41:56] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:41:57] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:41:58] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:41:59] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:42:01] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:42:02] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:42:14] WARNING  Request aborted (attempt 2/4): Request timed out.. Retrying in 4s...                                                                                                                                            vllm_client.py:31
Epoch 0   0% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/67,878  [ 0:00:50 < -:--:-- , ? it/s ][rank1]: Traceback (most recent call last):
[rank1]:   File "/code/speculators/scripts/train.py", line 657, in <module>
[rank1]:     main(args)
[rank1]:   File "/code/speculators/scripts/train.py", line 382, in main
[rank1]:     trainer.run_training()
[rank1]:   File "/code/speculators/src/speculators/train/trainer.py", line 307, in run_training
[rank1]:     self.train_epoch(epoch)
[rank1]:   File "/code/speculators/src/speculators/train/trainer.py", line 201, in train_epoch
[rank1]:     _draft_tokens, loss, metrics = self.model(
[rank1]:                                    ^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1881, in _call_impl
[rank1]:     return inner()
[rank1]:            ^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1829, in inner
[rank1]:     result = forward_call(*args, **kwargs)
[rank1]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 845, in compile_wrapper
[rank1]:     raise e.remove_dynamo_frames() from None  # see TORCHDYNAMO_VERBOSE=1
[rank1]:     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/output_graph.py", line 2196, in _call_user_compiler
[rank1]:     raise BackendCompilerFailed(
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/output_graph.py", line 2171, in _call_user_compiler
[rank1]:     compiled_fn = compiler_fn(gm, example_inputs)
[rank1]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/repro/after_dynamo.py", line 156, in __call__
[rank1]:     compiled_gm = compiler_fn(gm, example_inputs)
[rank1]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/__init__.py", line 2392, in __call__
[rank1]:     return compile_fx(model_, inputs_, config_patches=self.config)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 2681, in compile_fx
[rank1]:     return aot_autograd(
[rank1]:            ^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/backends/common.py", line 117, in __call__
[rank1]:     cg = aot_module_simplified(gm, example_inputs, **self.kwargs)
[rank1]:          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/aot_autograd.py", line 1106, in aot_module_simplified
[rank1]:     compiled_fn, _ = aot_stage2_compile(aot_state, aot_graph_capture)
[rank1]:                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/graph_compile.py", line 242, in aot_stage2_compile
[rank1]:     return aot_stage2_inference(aot_state, aot_graph_capture)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/graph_compile.py", line 315, in aot_stage2_inference
[rank1]:     compiled_fw = compiler(fw_module, updated_flat_args)
[rank1]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/schemas.py", line 1251, in __call__
[rank1]:     return self.compiler_fn(gm, example_inputs)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 2558, in fw_compiler_base
[rank1]:     return compile_fx_forward(
[rank1]:            ^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 2211, in compile_fx_forward
[rank1]:     _recursive_joint_graph_passes(gm)
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 527, in _recursive_joint_graph_passes
[rank1]:     joint_graph_passes(gm)
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/fx_passes/joint_graph.py", line 601, in joint_graph_passes
[rank1]:     ).apply_graph_pass(patterns.apply)
[rank1]:       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/fx/passes/graph_transform_observer.py", line 88, in apply_graph_pass
[rank1]:     return pass_fn(self.gm.graph)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/pattern_matcher.py", line 1982, in apply
[rank1]:     if is_match(m) and guard_or_false(entry.extra_check(m)):
[rank1]:                                       ^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/pattern_matcher.py", line 1425, in check_fn
[rank1]:     raise RuntimeError(
[rank1]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[rank1]: RuntimeError: Not all inputs to pattern found in match.kwargs. Perhaps one of the inputs is unused? argnames=['x', 'slice_shape'], match.kwargs={'x': squeeze}

[rank1]: Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"

Epoch 0   0% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/67,878  [ 0:00:53 < -:--:-- , ? it/s ]
[rank0]: Traceback (most recent call last):
[rank0]:   File "/code/speculators/scripts/train.py", line 657, in <module>
[rank0]:     main(args)
[rank0]:   File "code/speculators/scripts/train.py", line 382, in main
[rank0]:     trainer.run_training()
[rank0]:   File /code/speculators/src/speculators/train/trainer.py", line 307, in run_training
[rank0]:     self.train_epoch(epoch)
[rank0]:   File "/code/speculators/src/speculators/train/trainer.py", line 201, in train_epoch
[rank0]:     _draft_tokens, loss, metrics = self.model(
[rank0]:                                    ^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1881, in _call_impl
[rank0]:     return inner()
[rank0]:            ^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1829, in inner
[rank0]:     result = forward_call(*args, **kwargs)
[rank0]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 845, in compile_wrapper
[rank0]:     raise e.remove_dynamo_frames() from None  # see TORCHDYNAMO_VERBOSE=1
[rank0]:     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/output_graph.py", line 2196, in _call_user_compiler
[rank0]:     raise BackendCompilerFailed(
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/output_graph.py", line 2171, in _call_user_compiler
[rank0]:     compiled_fn = compiler_fn(gm, example_inputs)
[rank0]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/repro/after_dynamo.py", line 156, in __call__
[rank0]:     compiled_gm = compiler_fn(gm, example_inputs)
[rank0]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/__init__.py", line 2392, in __call__
[rank0]:     return compile_fx(model_, inputs_, config_patches=self.config)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 2681, in compile_fx
[rank0]:     return aot_autograd(
[rank0]:            ^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/backends/common.py", line 117, in __call__
[rank0]:     cg = aot_module_simplified(gm, example_inputs, **self.kwargs)
[rank0]:          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/aot_autograd.py", line 1106, in aot_module_simplified
[rank0]:     compiled_fn, _ = aot_stage2_compile(aot_state, aot_graph_capture)
[rank0]:                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/graph_compile.py", line 242, in aot_stage2_compile
[rank0]:     return aot_stage2_inference(aot_state, aot_graph_capture)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/graph_compile.py", line 315, in aot_stage2_inference
[rank0]:     compiled_fw = compiler(fw_module, updated_flat_args)
[rank0]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/schemas.py", line 1251, in __call__
[rank0]:     return self.compiler_fn(gm, example_inputs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 2558, in fw_compiler_base
[rank0]:     return compile_fx_forward(
[rank0]:            ^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 2211, in compile_fx_forward
[rank0]:     _recursive_joint_graph_passes(gm)
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/compile_fx.py", line 527, in _recursive_joint_graph_passes
[rank0]:     joint_graph_passes(gm)
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/fx_passes/joint_graph.py", line 601, in joint_graph_passes
[rank0]:     ).apply_graph_pass(patterns.apply)
[rank0]:       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/fx/passes/graph_transform_observer.py", line 88, in apply_graph_pass
[rank0]:     return pass_fn(self.gm.graph)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/pattern_matcher.py", line 1982, in apply
[rank0]:     if is_match(m) and guard_or_false(entry.extra_check(m)):
[rank0]:                                       ^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib/python3.12/site-packages/torch/_inductor/pattern_matcher.py", line 1425, in check_fn
[rank0]:     raise RuntimeError(
[rank0]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[rank0]: RuntimeError: Not all inputs to pattern found in match.kwargs. Perhaps one of the inputs is unused? argnames=['x', 'slice_shape'], match.kwargs={'x': squeeze}

[rank0]: Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"

[14:42:46] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
[14:42:47] WARNING  Request aborted (attempt 1/4): Request timed out.. Retrying in 2s...                                                                                                                                            vllm_client.py:31
Epoch 0   0% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/67,878  [ 0:00:00 < -:--:-- , ? it/s ][sept-filters-deal-j8t-wei-master-0][101714:103566][1][init.cc:2565] NCCL INFO pcclCommAbort!
[sept-filters-deal-j8t-wei-master-0][101714:102099][1][proxy.cc:1354] NCCL INFO [Service thread] Connection closed by localRank 1
[sept-filters-deal-j8t--wei-master-0][101714:103566][1][ext_kernel.cc:161] NCCL INFO Closing extKernel: 'CustomAllReduce'
[sept-filters-deal-j8t--wei-master-0][101714:103566][1][init.cc:2595] NCCL INFO comm 0x56406137e980 rank 1 nranks 2 hggcDev 1 busId c000 - Abort COMPLETE
W0525 14:43:32.658000 101623 site-packages/torch/distributed/elastic/multiprocessing/api.py:908] Sending process 101713 closing signal SIGTERM
E0525 14:43:32.923000 101623 site-packages/torch/distributed/elastic/multiprocessing/api.py:882] failed (exitcode: 1) local_rank: 1 (pid: 101714) of binary: /usr/local/bin/python3
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 357, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/torch/distributed/run.py", line 936, in main
    run(args)
  File "/usr/local/lib/python3.12/site-packages/torch/distributed/run.py", line 927, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 156, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/torch/distributed/launcher/api.py", line 293, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 


## 评论 (4)

### sunny-infra · 2026-05-25

Could you provide more details on how you started the vLLM service and what error messages appeared on the vLLM server side?

### Jim2016713 · 2026-05-25

> Could you provide more details on how you started the vLLM service and what error messages appeared on the vLLM server side?


The vLLM server started without any issues, and access is also fine.
python3 -m vllm.entrypoints.cli.main serve 'model'\
    --speculative_config '{"method": "extract_hidden_states", "num_speculative_tokens": 1, "draft_model_config": {"hf_config": {"eagle_aux_hidden_state_layer_ids": [2, 18, 33, 36]}}}' \
    --kv_transfer_config '{"kv_connector": "ExampleHiddenStatesConnector", "kv_role": "kv_producer", "kv_connector_extra_config": {"shared_storage_path": "/tmp/hidden_states"}}' \
    --data-parallel-size 1 \
    --port 8001

### sunny-infra · 2026-05-25

OK, I see. You can try commenting out @torch.compile in the src/speculators/models/dflash/core.py file, as shown in the figure below at the indicated location.
<img width="977" height="283" alt="Image" src="https://github.com/user-attachments/assets/ae5cfbd3-3f3e-476a-9502-4f632edece8e" />

### Jim2016713 · 2026-06-03

> OK, I see. You can try commenting out @torch.compile in the src/speculators/models/dflash/core.py file, as shown in the figure below at the indicated location. <img alt="Image" width="977" height="283" src="https://private-user-images.githubusercontent.com/176372238/597666192-ae5cfbd3-3f3e-476a-9502-4f632edece8e.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODA0NjU5NTAsIm5iZiI6MTc4MDQ2NTY1MCwicGF0aCI6Ii8xNzYzNzIyMzgvNTk3NjY2MTkyLWFlNWNmYmQzLTNmM2UtNDc2YS05NTAyLTRmNjMyZWRlY2U4ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNjAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDYwM1QwNTQ3MzBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mOGQwZGExM2RmMDUzNzY3YzBmOGM0MjgwOGM2MTI1MTQyNGI5OTBiZmY3NjQ1NzYxNThjYjE1ZTRiMTEzZDNiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.L40AORVVlIOEkyZ4oS5NF9c1P7UeSQmqsiyiQ3Nlgew">

The issue has been identified—it is related to the size of total-seq-len. In my business scenario, total-seq-len reaches 16384–20000.
