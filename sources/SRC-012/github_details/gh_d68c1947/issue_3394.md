# [Issue #3394] [Bug] phi3V (phi3.5v) inference is broken

source: https://github.com/mlc-ai/mlc-llm/issues/3394
state: open | updated: 2026-07-12T18:42:33Z
labels: bug

## 正文

## 🐛 Bug

phi3.5v inference is broken, the process immediately crashes after the model is loaded:

```log
[2025-12-09 14:34:43] INFO jit.py:126: Using compiled model lib: /root/.cache/mlc_llm/model_lib/8da4c80d51ba1a6e6f4cce4f0dce5e38.so
[14:34:43] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:798: Under mode "local", max batch size will be set to 4, max KV cache token capacity will be set to 8192, prefill chunk size will be set to 8192. 
[14:34:43] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:798: Under mode "interactive", max batch size will be set to 1, max KV cache token capacity will be set to 43087, prefill chunk size will be set to 8192. 
[14:34:43] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:798: Under mode "server", max batch size will be set to 128, max KV cache token capacity will be set to 42918, prefill chunk size will be set to 8192. 
[14:34:43] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:879: The actual engine mode is "interactive". So max batch size is 1, max KV cache token capacity is 43087, prefill chunk size is 8192.
[14:34:43] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:884: Estimated total single GPU memory usage: 20514.564 MB (Parameters: 2640.795 MB. KVCache: 16399.739 MB. Temporary buffer: 1474.030 MB). The actual usage might be slightly larger than the estimated number.
You can use the following special commands:
  /help               print the special commands
  /exit               quit the cli
  /stats              print out stats of last request (token/sec)
  /metrics            print out full engine metrics
  /reset              restart a fresh chat
  /set [overrides]    override settings in the generation config. For example,
                      `/set temperature=0.5;top_p=0.8;seed=23;max_tokens=100;stop=str1,str2`
                      Note: Separate stop words in the `stop` option with commas (,).
  Multi-line input: Use escape+enter to start a new line.

Exception in thread Thread-1:
Traceback (most recent call last):
  File "/root/autodl-tmp/envs/mlc/lib/python3.12/threading.py", line 1075, in _bootstrap_inner
    self.run()
  File "/root/autodl-tmp/envs/mlc/lib/python3.12/threading.py", line 1012, in run
    self._target(*self._args, **self._kwargs)
  File "python/tvm_ffi/cython/function.pxi", line 678, in core.Function.__call__
  File "/root/autodl-tmp/mlc-llm/cpp/serve/threaded_engine.cc", line 185, in mlc::llm::serve::ThreadedEngineImpl::RunBackgroundLoop()
    background_engine_->Step();

  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine.cc", line 752, in mlc::llm::serve::EngineImpl::Step()
    processed_requests = action->Step(estate_);

  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine_actions/new_request_prefill.cc", line 138, in mlc::llm::serve::NewRequestPrefillActionObj::Step(mlc::llm::serve::EngineState)
    models_[model_id]->BatchPrefill(embeddings, request_internal_ids, prefill_lengths);

  File "/root/autodl-tmp/mlc-llm/cpp/serve/model.cc", line 313, in mlc::llm::serve::ModelImpl::BatchPrefill(tvm::ffi::ObjectRef const&, std::vector<long, std::allocator<long> > const&, std::vector<int, std::allocator<int> > const&)
    ret = single_batch_prefill_func(embeddings_dref_or_nd, kv_cache_, params_).cast<ObjectRef>();

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 545, in tvm::runtime::vm::VirtualMachineImpl::InvokeClosurePacked(tvm::ffi::ObjectRef const&, tvm::ffi::PackedArgs, tvm::ffi::Any*)
    clo->impl.CallPacked(ffi::PackedArgs(packed_args.data(), packed_args.size()), rv);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 618, in operator()
    *rv = static_cast<VirtualMachineImpl*>(ctx_ptr)->InvokeBytecode(gf_idx, inputs);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 689, in tvm::runtime::vm::VirtualMachineImpl::InvokeBytecode(long, std::vector<tvm::ffi::Any, std::allocator<tvm::ffi::Any> > const&)
    RunLoop();
  
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 812, in tvm::runtime::vm::VirtualMachineImpl::RunLoop()
    this->RunInstrCall(curr_frame, instr);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 763, in tvm::runtime::vm::VirtualMachineImpl::RunInstrCall(tvm::runtime::vm::VMFrame*, tvm::runtime::vm::Instruction)
    this->InvokeClosurePacked(func_pool_[instr.func_idx].cast<ObjectRef>(), args, &ret);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/kv_state.cc", line 81, in operator()
    kv_cache->AttentionWithFusedQKV(layer_id, std::move(qkv_data), std::nullopt,

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/paged_kv_cache.cc", line 1335, in tvm::runtime::vm::PagedAttentionKVCacheObj::AttentionWithFusedQKV(long, tvm::runtime::Tensor, tvm::ffi::Optional<tvm::runtime::Tensor, void>, tvm::runtime::Tensor, double)
    f_split_rotary_(qkv_data_view, q_rope_position_map_view_, q_data, k_data, v_data,

  File "./IRModule.CodeGenLLVM", line 0, in __tvm_ffi_fused_rope_longrope_scaling
RuntimeError: Assert fail: T.Cast("int32", fused_rope_longrope_scaling_ext_factors_handle_shape[0]) == 48, Argument fused_rope_longrope_scaling.ext_factors_handle.shape[0] has an unsatisfied constraint: 48 == T.Cast("int32", fused_rope_longrope_scaling_ext_factors_handle_shape[0])
```

<!-- A clear and concise description of what the bug is. -->

The phi3.5v

## To Reproduce

Steps to reproduce the behavior:

just compile the latest code on master branch, and run chat: `python -m mlc_llm chat Phi-3.5-vision-instruct-q4f16_1-MLC`

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

It just should not crash

<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): CUDA 12.8
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Ubuntu 22.04
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...): RTX 3090
 - How you installed MLC-LLM (`conda`, source): source
 - How you installed TVM (`pip`, source): source
 - Python version (e.g. 3.10): 3.12
 - GPU driver version (if applicable): 570.124
 - CUDA/cuDNN version (if applicable): 12.8
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models): c6fb2be79f654588fd94727a74b9ca0754f63fa4
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (12)

### cmpute · 2025-12-09

Alright, it turns out that I'm not using the latest commit (which updated the tvm submodule just several hours ago). The latest tvm submodule included required changes (https://github.com/apache/tvm/pull/18422)

However, with the latest commit, there pop out new errors:

```log
...
[2025-12-09 19:06:03] INFO compile.py:142: Creating model from: Phi3VConfig(model_type='phi3_v', hidden_size=3072, vocab_size=32064, num_hidden_layers=32, num_attention_heads=32, intermediate_size=8192, rms_norm_eps=1e-05, num_key_value_heads=32, max_position_embeddings=131072, vision_config=CLIPVisionConfig(hidden_size=1024, image_size=336, intermediate_size=4096, num_attention_heads=16, num_hidden_layers=24, patch_size=14, projection_dim=768, vocab_size=None, num_channels=3, layer_norm_eps=1e-05, kwargs={}), img_processor={'image_dim_out': 1024, 'model_name': 'openai/clip-vit-large-patch14-336', 'name': 'clip_vision_model', 'num_img_tokens': 144}, position_embedding_base=10000.0, rope_scaling={'long_factor': [1.0800000429153442, 1.1100000143051147, 1.1399999856948853, 1.340000033378601, 1.5899999141693115, 1.600000023841858, 1.6200000047683716, 2.620000123977661, 3.2300000190734863, 3.2300000190734863, 4.789999961853027, 7.400000095367432, 7.700000286102295, 9.09000015258789, 12.199999809265137, 17.670000076293945, 24.46000099182129, 28.57000160217285, 30.420001983642578, 30.840002059936523, 32.590003967285156, 32.93000411987305, 42.320003509521484, 44.96000289916992, 50.340003967285156, 50.45000457763672, 57.55000305175781, 57.93000411987305, 58.21000289916992, 60.1400032043457, 62.61000442504883, 62.62000274658203, 62.71000289916992, 63.1400032043457, 63.1400032043457, 63.77000427246094, 63.93000411987305, 63.96000289916992, 63.970001220703125, 64.02999877929688, 64.06999969482422, 64.08000183105469, 64.12000274658203, 64.41000366210938, 64.4800033569336, 64.51000213623047, 64.52999877929688, 64.83999633789062], 'short_factor': [1.08, 1.1, 1.1300000000000001, 1.2800000000000002, 1.3100000000000003, 1.4500000000000004, 1.4500000000000004, 1.9500000000000008, 2.030000000000001, 2.4299999999999926, 2.5699999999999896, 2.9499999999999815, 3.729999999999965, 3.869999999999962, 4.189999999999955, 4.43999999999995, 4.6399999999999455, 4.979999999999938, 5.159999999999934, 5.279999999999932, 5.759999999999922, 5.889999999999919, 5.889999999999919, 5.969999999999917, 6.089999999999915, 6.2799999999999105, 6.7699999999999, 6.8899999999998975, 7.109999999999893, 7.129999999999892, 7.179999999999891, 7.289999999999889, 7.339999999999888, 7.559999999999883, 7.619999999999882, 7.69999999999988, 7.879999999999876, 7.879999999999876, 7.879999999999876, 7.939999999999875, 7.949999999999875, 7.979999999999874, 8.19999999999987, 8.439999999999864, 8.469999999999864, 8.589999999999861, 8.809999999999857, 8.999999999999853], 'type': 'longrope', 'rope_type': 'longrope', 'max_position_embeddings': 131072, 'original_max_position_embeddings': 4096}, original_max_position_embeddings=4096, context_window_size=131072, prefill_chunk_size=8192, head_dim=96, tensor_parallel_shards=1, max_batch_size=128, kwargs={})
[2025-12-09 19:06:03] INFO compile.py:160: Exporting the model to TVM compiler
error: unknown dtype `bool8`
 --> /root/autodl-tmp/mlc-llm/python/mlc_llm/model/vision/image_processing.py:248:36
     |  
 248 |                                  if h_idx < t or h_idx > h + b or w_idx < l or w_idx > w + r:
     |                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
note: run with `TVM_BACKTRACE=1` environment variable to display a backtrace.
[19:06:06] /root/autodl-tmp/mlc-llm/3rdparty/tvm/src/relax/ir/block_builder.cc:64: Warning: BlockBuilder destroyed with remaining blocks!
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/__main__.py", line 69, in <module>
    main()
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/__main__.py", line 46, in main
    cli.main(sys.argv[2:])
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/cli/chat.py", line 36, in main
    chat(
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/interface/chat.py", line 288, in chat
    JSONFFIEngine(
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/json_ffi/engine.py", line 232, in __init__
    model_args = _process_model_args(models, device, engine_config)[0]
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/serve/engine_base.py", line 171, in _process_model_args
    model_args: List[Tuple[str, str]] = [_convert_model_info(model) for model in models]
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/serve/engine_base.py", line 164, in _convert_model_info
    model_lib = jit.jit(
                ^^^^^^^^
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/interface/jit.py", line 164, in jit
    _run_jit(
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/interface/jit.py", line 124, in _run_jit
    raise RuntimeError("Cannot find compilation output, compilation failed")
RuntimeError: Cannot find compilation output, compilation failed
```

It might be related to auto-vectorization. I tried to change the if condition to a simple `h_idx < t`, and the compilation can proceed. So the issue is coming from the `or` operator, which is beyond my ability to investigate, please help with this.

### cmpute · 2025-12-10

More information: when checked out to this commit 862a73116ef58241e85dd1f09e30c8e8f8f8f6af, the phi-3.5-vision model works, but only with flashinfer disabled. If flashinfer is enabled, there will be CUDA kernel failures (see details below).

<details>

```log
2025-12-10 10:36:55] INFO auto_config.py:70: Found model configuration: /root/autodl-tmp/weights/Phi-3.5-vision-instruct-q4f16_1-MLC/mlc-chat-config.json
[2025-12-10 10:36:55] INFO auto_target.py:91: Detecting target device: cuda:0
[2025-12-10 10:36:55] INFO auto_target.py:93: Found target: {'kind': 'cuda', 'tag': '', 'keys': ['cuda', 'gpu'], 'max_num_threads': 1024, 'thread_warp_size': 32, 'arch': 'sm_86', 'max_threads_per_block': 1024, 'max_shared_memory_per_block': 49152}
[2025-12-10 10:36:55] INFO auto_target.py:110: Found host LLVM triple: x86_64-pc-linux-gnu
[2025-12-10 10:36:55] INFO auto_target.py:111: Found host LLVM CPU: znver2
[2025-12-10 10:36:55] INFO auto_target.py:334: Generating code for CUDA architecture: sm_86
[2025-12-10 10:36:55] INFO auto_target.py:335: To produce multi-arch fatbin, set environment variable MLC_MULTI_ARCH. Example: MLC_MULTI_ARCH=70,72,75,80,86,87,89,90a
[2025-12-10 10:36:55] INFO auto_config.py:154: Found model type: phi3_v. Use `--model-type` to override.
Compiling with arguments:
  --config          Phi3VConfig(model_type='phi3_v', hidden_size=3072, vocab_size=32064, num_hidden_layers=32, num_attention_heads=32, intermediate_size=8192, rms_norm_eps=1e-05, num_key_value_heads=32, max_position_embeddings=131072, vision_config=CLIPVisionConfig(hidden_size=1024, image_size=336, intermediate_size=4096, num_attention_heads=16, num_hidden_layers=24, patch_size=14, projection_dim=768, vocab_size=None, num_channels=3, layer_norm_eps=1e-05, kwargs={}), img_processor={'image_dim_out': 1024, 'model_name': 'openai/clip-vit-large-patch14-336', 'name': 'clip_vision_model', 'num_img_tokens': 144}, position_embedding_base=10000.0, rope_scaling={'long_factor': [1.0800000429153442, 1.1100000143051147, 1.1399999856948853, 1.340000033378601, 1.5899999141693115, 1.600000023841858, 1.6200000047683716, 2.620000123977661, 3.2300000190734863, 3.2300000190734863, 4.789999961853027, 7.400000095367432, 7.700000286102295, 9.09000015258789, 12.199999809265137, 17.670000076293945, 24.46000099182129, 28.57000160217285, 30.420001983642578, 30.840002059936523, 32.590003967285156, 32.93000411987305, 42.320003509521484, 44.96000289916992, 50.340003967285156, 50.45000457763672, 57.55000305175781, 57.93000411987305, 58.21000289916992, 60.1400032043457, 62.61000442504883, 62.62000274658203, 62.71000289916992, 63.1400032043457, 63.1400032043457, 63.77000427246094, 63.93000411987305, 63.96000289916992, 63.970001220703125, 64.02999877929688, 64.06999969482422, 64.08000183105469, 64.12000274658203, 64.41000366210938, 64.4800033569336, 64.51000213623047, 64.52999877929688, 64.83999633789062], 'short_factor': [1.08, 1.1, 1.1300000000000001, 1.2800000000000002, 1.3100000000000003, 1.4500000000000004, 1.4500000000000004, 1.9500000000000008, 2.030000000000001, 2.4299999999999926, 2.5699999999999896, 2.9499999999999815, 3.729999999999965, 3.869999999999962, 4.189999999999955, 4.43999999999995, 4.6399999999999455, 4.979999999999938, 5.159999999999934, 5.279999999999932, 5.759999999999922, 5.889999999999919, 5.889999999999919, 5.969999999999917, 6.089999999999915, 6.2799999999999105, 6.7699999999999, 6.8899999999998975, 7.109999999999893, 7.129999999999892, 7.179999999999891, 7.289999999999889, 7.339999999999888, 7.559999999999883, 7.619999999999882, 7.69999999999988, 7.879999999999876, 7.879999999999876, 7.879999999999876, 7.939999999999875, 7.949999999999875, 7.979999999999874, 8.19999999999987, 8.439999999999864, 8.469999999999864, 8.589999999999861, 8.809999999999857, 8.999999999999853], 'type': 'longrope', 'rope_type': 'longrope', 'max_position_embeddings': 131072, 'original_max_position_embeddings': 4096}, original_max_position_embeddings=4096, context_window_size=131072, prefill_chunk_size=8192, head_dim=96, tensor_parallel_shards=1, max_batch_size=128, kwargs={})
  --quantization    GroupQuantize(name='q4f16_1', kind='group-quant', group_size=32, quantize_dtype='int4', storage_dtype='uint32', model_dtype='float16', linear_weight_layout='NK', quantize_embedding=True, quantize_final_fc=True, num_elem_per_storage=8, num_storage_per_group=4, max_int_value=7, tensor_parallel_shards=0)
  --model-type      phi3_v
  --target          {'kind': 'cuda', 'tag': '', 'keys': ['cuda', 'gpu'], 'host': {'kind': 'llvm', 'tag': '', 'keys': ['cpu'], 'mtriple': 'x86_64-pc-linux-gnu', 'mcpu': 'znver2'}, 'libs': ['thrust'], 'max_shared_memory_per_block': 49152, 'max_threads_per_block': 1024, 'arch': 'sm_86', 'thread_warp_size': 32, 'max_num_threads': 1024}
  --opt             flashinfer=1;cublas_gemm=0;faster_transformer=0;cudagraph=1;cutlass=1;ipc_allreduce_strategy=NONE
  --system-lib-prefix ""
  --output          /tmp/tmp8nwg57vt/lib.so
  --overrides       context_window_size=None;sliding_window_size=None;prefill_chunk_size=None;attention_sink_size=None;max_batch_size=None;tensor_parallel_shards=None;pipeline_parallel_stages=None;disaggregation=None
[2025-12-10 10:36:55] INFO compile.py:140: Creating model from: Phi3VConfig(model_type='phi3_v', hidden_size=3072, vocab_size=32064, num_hidden_layers=32, num_attention_heads=32, intermediate_size=8192, rms_norm_eps=1e-05, num_key_value_heads=32, max_position_embeddings=131072, vision_config=CLIPVisionConfig(hidden_size=1024, image_size=336, intermediate_size=4096, num_attention_heads=16, num_hidden_layers=24, patch_size=14, projection_dim=768, vocab_size=None, num_channels=3, layer_norm_eps=1e-05, kwargs={}), img_processor={'image_dim_out': 1024, 'model_name': 'openai/clip-vit-large-patch14-336', 'name': 'clip_vision_model', 'num_img_tokens': 144}, position_embedding_base=10000.0, rope_scaling={'long_factor': [1.0800000429153442, 1.1100000143051147, 1.1399999856948853, 1.340000033378601, 1.5899999141693115, 1.600000023841858, 1.6200000047683716, 2.620000123977661, 3.2300000190734863, 3.2300000190734863, 4.789999961853027, 7.400000095367432, 7.700000286102295, 9.09000015258789, 12.199999809265137, 17.670000076293945, 24.46000099182129, 28.57000160217285, 30.420001983642578, 30.840002059936523, 32.590003967285156, 32.93000411987305, 42.320003509521484, 44.96000289916992, 50.340003967285156, 50.45000457763672, 57.55000305175781, 57.93000411987305, 58.21000289916992, 60.1400032043457, 62.61000442504883, 62.62000274658203, 62.71000289916992, 63.1400032043457, 63.1400032043457, 63.77000427246094, 63.93000411987305, 63.96000289916992, 63.970001220703125, 64.02999877929688, 64.06999969482422, 64.08000183105469, 64.12000274658203, 64.41000366210938, 64.4800033569336, 64.51000213623047, 64.52999877929688, 64.83999633789062], 'short_factor': [1.08, 1.1, 1.1300000000000001, 1.2800000000000002, 1.3100000000000003, 1.4500000000000004, 1.4500000000000004, 1.9500000000000008, 2.030000000000001, 2.4299999999999926, 2.5699999999999896, 2.9499999999999815, 3.729999999999965, 3.869999999999962, 4.189999999999955, 4.43999999999995, 4.6399999999999455, 4.979999999999938, 5.159999999999934, 5.279999999999932, 5.759999999999922, 5.889999999999919, 5.889999999999919, 5.969999999999917, 6.089999999999915, 6.2799999999999105, 6.7699999999999, 6.8899999999998975, 7.109999999999893, 7.129999999999892, 7.179999999999891, 7.289999999999889, 7.339999999999888, 7.559999999999883, 7.619999999999882, 7.69999999999988, 7.879999999999876, 7.879999999999876, 7.879999999999876, 7.939999999999875, 7.949999999999875, 7.979999999999874, 8.19999999999987, 8.439999999999864, 8.469999999999864, 8.589999999999861, 8.809999999999857, 8.999999999999853], 'type': 'longrope', 'rope_type': 'longrope', 'max_position_embeddings': 131072, 'original_max_position_embeddings': 4096}, original_max_position_embeddings=4096, context_window_size=131072, prefill_chunk_size=8192, head_dim=96, tensor_parallel_shards=1, max_batch_size=128, kwargs={})
[2025-12-10 10:36:55] INFO compile.py:158: Exporting the model to TVM compiler
[2025-12-10 10:36:56] WARNING attention.py:117: FlashInfer only supports head_dim in [128], but got 64. Skip and fallback to default implementation.
[2025-12-10 10:37:01] INFO compile.py:164: Running optimizations using TVM
[2025-12-10 10:37:01] INFO compile.py:186: Registering metadata: {'model_type': 'phi3_v', 'quantization': 'q4f16_1', 'context_window_size': 131072, 'sliding_window_size': -1, 'attention_sink_size': -1, 'prefill_chunk_size': 8192, 'tensor_parallel_shards': 1, 'pipeline_parallel_stages': 1, 'disaggregation': False, 'kv_state_kind': 'kv_cache', 'max_batch_size': 128}
[2025-12-10 10:37:18] INFO pipeline.py:57: Running TVM Relax graph-level optimizations
[2025-12-10 10:37:21] INFO pipeline.py:57: Lowering to TVM TIR kernels
[10:37:21] /root/autodl-tmp/mlc-llm/3rdparty/tvm/include/tvm/topi/transform.h:1232: Warning: Fast mode segfaults when there are out-of-bounds indices. Make sure input indices are in bound
[10:37:22] /root/autodl-tmp/mlc-llm/3rdparty/tvm/include/tvm/topi/transform.h:1232: Warning: Fast mode segfaults when there are out-of-bounds indices. Make sure input indices are in bound
[10:37:22] /root/autodl-tmp/mlc-llm/3rdparty/tvm/include/tvm/topi/transform.h:1232: Warning: Fast mode segfaults when there are out-of-bounds indices. Make sure input indices are in bound
[2025-12-10 10:37:23] INFO pipeline.py:57: Running TVM TIR-level optimizations
[2025-12-10 10:37:33] INFO pipeline.py:57: Running TVM Dlight low-level optimizations
[2025-12-10 10:37:48] INFO pipeline.py:57: Lowering to VM bytecode
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `alloc_embedding_tensor`: 48.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `argsort_probs`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `batch_decode`: 10.75 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `batch_prefill`: 688.75 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `batch_verify`: 688.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `create_flashinfer_paged_kv_cache`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `create_tir_paged_kv_cache`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `decode`: 0.08 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `embed`: 48.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `image_embed`: 178.77 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `multinomial_from_uniform`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `prefill`: 688.01 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `renormalize_by_top_p`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `sample_with_top_p`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `sampler_take_probs`: 0.01 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `sampler_verify_draft_tokens`: 0.00 MB
[2025-12-10 10:37:50] INFO estimate_memory_usage.py:58: [Memory usage] Function `softmax_with_temperature`: 0.00 MB
[2025-12-10 10:37:56] INFO pipeline.py:57: Compiling external modules
[2025-12-10 10:37:56] INFO pipeline.py:57: Compilation complete! Exporting to disk
[2025-12-10 10:38:29] INFO model_metadata.py:94: Total memory usage without KV cache: 3329.54 MB (Parameters: 2640.79 MB. Temporary buffer: 688.75 MB)
[2025-12-10 10:38:29] INFO model_metadata.py:128: KV cache size: 0.38 MB per token in the context window
[2025-12-10 10:38:29] INFO model_metadata.py:133: Total memory usage with a 4K KV cache: 4865.54 MB
[2025-12-10 10:38:29] INFO model_metadata.py:139: To reduce memory usage, tweak `prefill_chunk_size`, `context_window_size` and `sliding_window_size`
[2025-12-10 10:38:29] INFO compile.py:208: Generated: /tmp/tmp8nwg57vt/lib.so
[10:38:30] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:798: Under mode "local", max batch size will be set to 4, max KV cache token capacity 4096 is specified by user, prefill chunk size will be set to 4096. 
[10:38:30] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:798: Under mode "interactive", max batch size will be set to 1, max KV cache token capacity 4096 is specified by user, prefill chunk size will be set to 4096. 
[10:38:30] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:798: Under mode "server", max batch size will be set to 128, max KV cache token capacity 4096 is specified by user, prefill chunk size will be set to 8192. 
[10:38:30] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:879: The actual engine mode is "server". So max batch size is 128, max KV cache token capacity is 4096, prefill chunk size is 8192.
[10:38:30] /root/autodl-tmp/mlc-llm/cpp/serve/config.cc:884: Estimated total single GPU memory usage: 5956.272 MB (Parameters: 2640.795 MB. KVCache: 1778.078 MB. Temporary buffer: 1537.398 MB). The actual usage might be slightly larger than the estimated number.
Traceback (most recent call last):
  File "/root/autodl-tmp/mlc-llm/examples/python/vlm_test.py", line 33, in <module>
    output_texts, _ = engine.generate(
                      ^^^^^^^^^^^^^^^^
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/serve/sync_engine.py", line 282, in generate
    self.step()
  File "/root/autodl-tmp/mlc-llm/python/mlc_llm/serve/sync_engine.py", line 350, in step
    self._ffi["step"]()
  File "python/tvm_ffi/cython/function.pxi", line 678, in core.Function.__call__
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine.cc", line 752, in mlc::llm::serve::EngineImpl::Step()
    processed_requests = action->Step(estate_);

  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine_actions/new_request_prefill.cc", line 138, in mlc::llm::serve::NewRequestPrefillActionObj::Step(mlc::llm::serve::EngineState)
    models_[model_id]->BatchPrefill(embeddings, request_internal_ids, prefill_lengths);

  File "/root/autodl-tmp/mlc-llm/cpp/serve/model.cc", line 315, in mlc::llm::serve::ModelImpl::BatchPrefill(tvm::ffi::ObjectRef const&, std::vector<long, std::allocator<long> > const&, std::vector<int, std::allocator<int> > const&)
    ret = prefill_func(embeddings_dref_or_nd, logit_pos_dref_or_nd, kv_cache_, params_)

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 545, in tvm::runtime::vm::VirtualMachineImpl::InvokeClosurePacked(tvm::ffi::ObjectRef const&, tvm::ffi::PackedArgs, tvm::ffi::Any*)
    clo->impl.CallPacked(ffi::PackedArgs(packed_args.data(), packed_args.size()), rv);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 618, in operator()
    *rv = static_cast<VirtualMachineImpl*>(ctx_ptr)->InvokeBytecode(gf_idx, inputs);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 689, in tvm::runtime::vm::VirtualMachineImpl::InvokeBytecode(long, std::vector<tvm::ffi::Any, std::allocator<tvm::ffi::Any> > const&)
    RunLoop();
  
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 812, in tvm::runtime::vm::VirtualMachineImpl::RunLoop()
    this->RunInstrCall(curr_frame, instr);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/vm.cc", line 763, in tvm::runtime::vm::VirtualMachineImpl::RunInstrCall(tvm::runtime::vm::VMFrame*, tvm::runtime::vm::Instruction)
    this->InvokeClosurePacked(func_pool_[instr.func_idx].cast<ObjectRef>(), args, &ret);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/kv_state.cc", line 81, in operator()
    kv_cache->AttentionWithFusedQKV(layer_id, std::move(qkv_data), std::nullopt,

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/paged_kv_cache.cc", line 1367, in tvm::runtime::vm::PagedAttentionKVCacheObj::AttentionWithFusedQKV(long, tvm::runtime::Tensor, tvm::ffi::Optional<tvm::runtime::Tensor, void>, tvm::runtime::Tensor, double)
    AttentionInternal(layer_id, q_data, k_data, v_data, o_data_view, sm_scale);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/paged_kv_cache.cc", line 2092, in tvm::runtime::vm::PagedAttentionKVCacheObj::AttentionInternal(long, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, double)
    MHASelfAttnInternal(q_data, k_data, v_data, output, merged_attn_lse_view_, sm_scale);

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/paged_kv_cache.cc", line 2106, in tvm::runtime::vm::PagedAttentionKVCacheObj::MHASelfAttnInternal(tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, double)
    f_attention_prefill_ragged_->MHA(

  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/vm/attn_backend.h", line 340, in tvm::runtime::vm::FlashInferRaggedPrefillFunc::MHA(tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, tvm::runtime::Tensor, bool, tvm::runtime::vm::RoPEMode, double, double, double, tvm::runtime::Tensor, tvm::runtime::Tensor, void*)
    attn_func_(float_workspace_buffer_, int_workspace_buffer_, plan_info_vec_, q, k, v, qo_indptr,

  File "<unknown>", line 0, in __tvm_ffi_batch_prefill_ragged_run
  File "/root/.cache/flashinfer/86/generated/batch_prefill_tvm_dtype_q_float16_dtype_kv_float16_dtype_o_float16_qk_head_dim_96_v_head_dim_96_enable_inline_rope_False/batch_prefill.cu", line 193, in BatchPrefillWithRaggedKVCacheRun(tvm::ffi::Tensor, tvm::ffi::Tensor, tvm::ffi::Array<long int>, tvm::ffi::Tensor, tvm::ffi::Tensor, tvm::ffi::Tensor, tvm::ffi::Tensor, tvm::ffi::Tensor, tvm::ffi::Tensor, tvm::ffi::Optional<tvm::ffi::Tensor>, int64_t, int64_t, int64_t, bool, double, double, double)::<lambda()>
    TVM_FFI_ICHECK(status == cudaSuccess)

tvm.error.InternalError: Check failed: (status == cudaSuccess) is false: BatchPrefillWithRaggedKVCache failed with error an illegal memory access was encountered
terminate called after throwing an instance of 'tvm::runtime::InternalError'
  what():  Traceback (most recent call last):
  File "<unknown>", line 0, in TVMFFIObjectDecRef
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine.cc", line 1031, in mlc::llm::serve::EngineModule::GetFunction(tvm::ffi::String const&)::{lambda(tvm::ffi::PackedArgs, tvm::ffi::Any*)#3}::~Any()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 515, in tvm::ffi::ObjectPtr<tvm::ffi::Object>::~ObjectPtr()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 566, in tvm::ffi::ObjectPtr<tvm::ffi::Object>::reset()
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine.cc", line 1026, in mlc::llm::serve::EngineModule::~EngineModule()
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine.cc", line 343, in mlc::llm::serve::EngineImpl::~EngineImpl()
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine.cc", line 343, in mlc::llm::serve::EngineImpl::~EngineImpl()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/container/array.h", line 359, in tvm::ffi::Array<mlc::llm::serve::EngineAction, void>::~Array()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 754, in tvm::ffi::ObjectRef::~ObjectRef()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 515, in tvm::ffi::ObjectPtr<tvm::ffi::Object>::~ObjectPtr()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 566, in tvm::ffi::ObjectPtr<tvm::ffi::Object>::reset()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/container/array.h", line 50, in tvm::ffi::ArrayObj::~ArrayObj()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 417, in tvm::ffi::Object::DecRef()
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine_actions/batch_decode.cc", line 29, in mlc::llm::serve::BatchDecodeActionObj::~BatchDecodeActionObj()
  File "/root/autodl-tmp/mlc-llm/cpp/serve/engine_actions/../sampler/sampler.h", line 134, in mlc::llm::serve::Sampler::~Sampler()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 754, in tvm::ffi::ObjectRef::~ObjectRef()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 515, in tvm::ffi::ObjectPtr<tvm::ffi::Object>::~ObjectPtr()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 566, in tvm::ffi::ObjectPtr<tvm::ffi::Object>::reset()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/3rdparty/tvm-ffi/include/tvm/ffi/object.h", line 417, in tvm::ffi::Object::DecRef()
  File "/root/autodl-tmp/mlc-llm/cpp/serve/sampler/gpu_sampler.cc", line 118, in mlc::llm::serve::GPUSampler::~GPUSampler()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/cuda/cuda_device_api.cc", line 232, in tvm::runtime::CUDADeviceAPI::FreeStream(DLDevice, void*)
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/include/tvm/runtime/logging.h", line 321, in tvm::runtime::detail::LogFatal::~LogFatal()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/include/tvm/runtime/logging.h", line 337, in tvm::runtime::detail::LogFatal::Entry::Finalize()
  File "/root/autodl-tmp/mlc-llm/3rdparty/tvm/src/runtime/cuda/cuda_device_api.cc", line 234, in 
InternalError: Check failed: (e == cudaSuccess || e == cudaErrorCudartUnloading) is false: CUDA: an illegal memory access was encountered

Aborted (core dumped)
```

</details>


### Lingrongye · 2025-12-10

Hello, when I run the phi-3.5vision model and interact with it by inputting images, many of the responses it provides are irrelevant. Have you encountered this issue?

### cmpute · 2025-12-10

> Hello, when I run the phi-3.5vision model and interact with it by inputting images, many of the responses it provides are irrelevant. Have you encountered this issue?

Yes, but I'm not sure whether there are bugs in the model or it's just because the model's capabilities are not enough

### Lingrongye · 2025-12-10

<img width="1769" height="597" alt="Image" src="https://github.com/user-attachments/assets/0cf16de7-4ede-4d38-9b43-5447cbf27069" />
The code:

from mlc_llm import MLCEngine

# Create engine
model = "/root/autodl-tmp/phi-mlc"
engine = MLCEngine(model)

# Run chat completion in OpenAI API.
for response in engine.chat.completions.create(
```
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://www.ilankelman.org/stopsigns/australia.jpg",
                },
                {
                    "type": "text",
                    "text": "Describe this image please."
                },
            ],
        },
    ],
    model=model,
    stream=True,
```
):
    for choice in response.choices:
        print(choice.delta.content, end="", flush=True)
print("\n")

engine.terminate()

why the output so strange？


### cmpute · 2025-12-11

@Lingrongye your result seems to be erroneous. In my test, the model generates normal sentences, the problem is just that the answer is not quite relevant to the picture. Your sentences generated by the model is abnormal, there might be some backend issues with it.

### Lingrongye · 2025-12-11

how did you download the mlc-llm Python package and TVM. Was it via the command in the official documentation:
`python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cu128 mlc-ai-nightly-cu128`
or did you build it from source? And what version of CUDA are you using? I don't know where I went wrong.

### cmpute · 2025-12-12

@Lingrongye You can look at the bottom of my original post, where I have listed the details of my environment. I built mlc and tvm from source.

### Lingrongye · 2025-12-18

<img width="974" height="247" alt="Image" src="https://github.com/user-attachments/assets/bf1af10d-c720-48f0-b298-2460a3bb2ef2" />
Have you encountered this issue?I built the tvm from source code.

### Lingrongye · 2025-12-18

@cmpute 


### akaashrp · 2026-03-24

Hi @Lingrongye, could you try building TVM and MLC-LLM from source (you might need to revert to a slightly older commit for TVM before the tirx refactor) and installing tvm-ffi using `pip install 3rdparty/tvm-ffi -v` from the tvm repo?

### ErenAta16 · 2026-07-12

You've basically already found it -- disabling FlashInfer works because phi-3.5-vision uses `head_dim=96`, and FlashInfer only supports `head_dim=128`.

There is a guard for this: `python/mlc_llm/op/attention.py`'s `attention()` op explicitly checks `if d not in [128]: ... return _fallback()`. But your crash isn't coming through that function -- it's firing inside `fused_rope_longrope_scaling`, called from `PagedAttentionKVCacheObj::AttentionWithFusedQKV` in TVM's vendored `paged_kv_cache.cc`. That's a separate, lower-level RoPE+attention fusion path (part of `tvm.relax.frontend.nn.llm.kv_cache`, vendored under `3rdparty/tvm`), and it isn't covered by the `head_dim` check in `attention.py` at all -- it unconditionally builds the FlashInfer-oriented longrope kernel regardless of head_dim, and fails the shape assert instead of falling back.

So the real gap is in the vendored TVM PagedKVCache/longrope kernel-generation code, not in the phi3v model file itself -- which is why disabling FlashInfer is currently the only workaround; there's no phi3v-side toggle that would fix it. Flagging this precisely (this file/function) since patching it likely means touching TVM's vendored `kv_cache.py`/`paged_kv_cache.cc`, not just mlc-llm's own tree -- I wasn't able to pull the exact vendored source line-by-line to hand over a diff, so treat the "where exactly to patch" part as a strong lead rather than a finished fix.
