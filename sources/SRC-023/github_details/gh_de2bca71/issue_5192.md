# [Issue #5192] [Bug]: Memory access fault due to top_k_renorm_probs

source: https://github.com/ROCm/aiter/issues/5192
state: open | updated: 2026-09-02T00:12:21Z
labels: 

## 正文

### Problem Description

Customer reported a Memory access fault by GPU on MI355x.

```bash
> 2026-08-31T17:43:36.650052872Z stderr F (Worker_TP4 pid=955) [aiter] finish build /root/.aiter/build/top_k_renorm_probs_d41d8cd98f00b204e9800998ecf8427e, cost 14.56399715s
> 2026-08-31T17:43:36.6703347Z stderr F Memory access fault by GPU node-6 (Agent handle: 0x501def90) on address 0x7f5e50c00000. Reason: Unknown.
> 2026-08-31T17:43:36.716068815Z stderr F Memory access fault by GPU node-2 (Agent handle: 0x319bf880) on address 0x7f46e0400000. Reason: Unknown.
> 2026-08-31T17:43:36.716090635Z stderr F Memory access fault by GPU node-8 (Agent handle: 0x4df431d0) on address 0x7ef56be00000. Reason: Unknown.
> 2026-08-31T17:43:36.718185052Z stderr F Memory access fault by GPU node-7 (Agent handle: 0x4e39c060) on address 0x7edae0800000. Reason: Unknown.
> 2026-08-31T17:43:36.721672607Z stderr F Memory access fault by GPU node-4 (Agent handle: 0x469696d0) on address 0x7ed267e00000. Reason: Unknown.
> 2026-08-31T17:43:36.721973282Z stderr F Memory access fault by GPU node-9 (Agent handle: 0x51d9e5b0) on address 0x7ec01f200000. Reason: Unknown.
> 2026-08-31T17:43:36.72338185Z stderr F Memory access fault by GPU node-5 (Agent handle: 0x34675e20) on address 0x7f2d15000000. Reason: Unknown.
> 2026-08-31T17:43:36.766605515Z stderr F Memory access fault by GPU node-3 (Agent handle: 0x3e8033a0) on address 0x7f18fc400000. Reason: Unknown.
> 2026-08-31T17:43:37.261697558Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.292193035Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.308371859Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.31648186Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.336479623Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.343519642Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.352567798Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.356473637Z stderr F Failed to write ELF header to pipe: Broken pipe
> 2026-08-31T17:43:37.356480106Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.356482477Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.370427376Z stderr F GPU coredump: execvp failed: No such file or directory
> 2026-08-31T17:43:37.383300541Z stderr F Failed to write program header to pipe: Broken pipe
> 2026-08-31T17:43:37.383318681Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.383320681Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.400902153Z stderr F Failed to write program header to pipe: Broken pipe
> 2026-08-31T17:43:37.400915533Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.400917173Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.439862146Z stderr F Failed to write ELF header to pipe: Broken pipe
> 2026-08-31T17:43:37.439871456Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.439872956Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.443018216Z stderr F Failed to write program header to pipe: Broken pipe
> 2026-08-31T17:43:37.443022206Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.443023796Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.449279947Z stderr F Failed to write program header to pipe: Broken pipe
> 2026-08-31T17:43:37.449286406Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.449288295Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.467498447Z stderr F Failed to write program header to pipe: Broken pipe
> 2026-08-31T17:43:37.467505497Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.467507407Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.499066348Z stderr F Failed to write ELF header to pipe: Broken pipe
> 2026-08-31T17:43:37.499072988Z stderr F GPU coredump: handler exited with error (status: 1)
> 2026-08-31T17:43:37.499074368Z stderr F GPU core dump failed
> 2026-08-31T17:43:37.761398461Z stdout F (EngineCore pid=659) ERROR 08-31 17:43:37 [multiproc_executor.py:295] Worker proc VllmWorker-4 died unexpectedly (exit code: None), shutting down executor.
> 2026-08-31T17:43:37.762255408Z stdout F (EngineCore pid=659) INFO 08-31 17:43:37 [multiproc_executor.py:440] [shutdown] Executor: waiting for worker exit count=7
> 2026-08-31T17:43:37.866675083Z stdout F (EngineCore pid=659) INFO 08-31 17:43:37 [multiproc_executor.py:447] [shutdown] Executor: all workers exited gracefully
> 2026-08-31T17:43:37.867216544Z stdout F (EngineCore pid=659) INFO 08-31 17:43:37 [scheduler.py:2598] Cache-aware scheduling: 8/1084 pops reordered
> 2026-08-31T17:43:37.867772356Z stdout F (EngineCore pid=659) ERROR 08-31 17:43:37 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.26.1rc1.dev305+gadbf08d97.d20260805) with config: model='moonshotai/Kimi-K3', speculative_config=None, tokenizer='moonshotai/Kimi-K3', skip_tokenizer_init=False, tokenizer_mode=kimi_k3, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=1048576, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=mxfp4, quantization_config=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=fp8, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='xgrammar', disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='kimi_k3', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=True, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False, enable_mm_processor_stats=False, enable_logging_iteration_details=False, jit_monitor_mode='warn', jit_monitor_verbose=False), seed=0, served_model_name=moonshotai/Kimi-K3, enable_prefix_caching=True, enable_chunked_prefill=True, pooler_config=None, compilation_config={'mode': <CompilationMode.VLLM_COMPILE: 3>, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'inductor', 'custom_ops': ['+quant_fp8', '+grouped_topk', '+sparse_attn_indexer', 'none', '+quant_fp8', '+sparse_attn_indexer'], 'ir_enable_torch_wrap': True, 'splitting_ops': ['vllm::unified_attention_with_output', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::qwen_gdn_attention_core', 'vllm::gdn_attention_core_xpu', 'vllm::olmo_hybrid_gdn_full_forward', 'vllm::sparse_attn_indexer', 'vllm::rocm_aiter_sparse_attn_indexer', 'vllm::deepseek_v4_attention', 'vllm::hpc_rope_norm_forward', 'vllm::unified_kv_cache_update', 'vllm::unified_mla_kv_cache_update'], 'compile_mm_encoder': False, 'cudagraph_mm_encoder': False, 'encoder_cudagraph_token_budgets': [], 'encoder_cudagraph_max_vision_items_per_batch': 0, 'encoder_cudagraph_max_frames_per_batch': None, 'compile_sizes': [], 'compile_ranges_endpoints': [4681, 4681, 16384], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'size_asserts': False, 'alignment_asserts': False, 'scalar_asserts': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_AND_PIECEWISE: (2, 1)>, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8, 16, 24, 32], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant': True, 'fuse_act_quant': True, 'fuse_attn_quant': False, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': True, 'enable_qk_norm_rope_fusion': False, 'fuse_rope_kvcache_cat_mla': False, 'fuse_act_padding': False, 'fuse_mla_dual_rms_norm': True, 'fuse_rope_kvcache': False, 'fuse_qk_norm_rope_kvcache': False}, 'max_cudagraph_capture_size': 32, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False, 'assume_32_bit_indexing': False}, 'local_cache_dir': None, 'fast_moe_cold_start': True, 'static_all_moe_layers': []}, kernel_config=KernelConfig(ir_op_priority=IrOpPriorityConfig(rms_norm=['aiter', 'native'], fused_add_rms_norm=['aiter', 'native']), enable_flashinfer_autotune=True, enable_cutedsl_warmup=True, enable_jit_warmup=True, enable_bf16x3_router_gemm=False, moe_backend='auto', linear_backend='auto'),
> 2026-08-31T17:43:37.867962742Z stdout F (EngineCore pid=659) ERROR 08-31 17:43:37 [dump_input.py:79] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=chatcmpl-26cb0ced-7c4e-40c7-b0f6-dec57e61fae1-a545b43e,prompt_token_ids_len=2824,prefill_token_ids_len=None,mm_features=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=50, min_p=0.0, seed=None, stop=[], stop_token_ids=[163586], bad_words=[], thinking_token_budget=None, include_stop_str_in_output=False, ignore_eos=False, max_tokens=32768, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=False, spaces_between_special_tokens=False, structured_outputs=None, extra_args=None),block_ids=([1868], [1872], [1867], [1866]),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None)], scheduled_cached_reqs=CachedRequestData(req_ids=['chatcmpl-92bb5764-32cb-4e2b-a4a0-d3efb85c65ab-b4efb597'],resumed_req_ids=set(),new_token_ids_lens=[],all_token_ids_lens={},new_block_ids=[None],num_computed_tokens=[24609],num_output_tokens=[2103]), num_scheduled_tokens={chatcmpl-26cb0ced-7c4e-40c7-b0f6-dec57e61fae1-a545b43e: 1536, chatcmpl-92bb5764-32cb-4e2b-a4a0-d3efb85c65ab-b4efb597: 1}, total_num_scheduled_tokens=1537, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[0, 0, 0, 0], finished_req_ids=[], free_encoder_mm_hashes=[], scheduled_encoder_input_stats=null, preempted_req_ids=[], has_structured_output_requests=false, pending_structured_output_tokens=false, num_invalid_spec_tokens=null, kv_connector_metadata=null, ec_connector_metadata=null, ec_manager_metadata=null, new_block_ids_to_zero=[1866], kv_cache_block_copies=null, partial_tail_offloads=null, num_spec_tokens_to_schedule=0)
> 2026-08-31T17:43:37.868485393Z stdout F (EngineCore pid=659) ERROR 08-31 17:43:37 [dump_input.py:81] Dumping scheduler stats: SchedulerStats(num_running_reqs=2, num_waiting_reqs=0, num_skipped_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.0095628415300546, iteration_details=None, prefix_cache_stats=PrefixCacheStats(reset=False, requests=0, queries=0, hits=0, preempted_requests=0, preempted_queries=0, preempted_hits=0), connector_prefix_cache_stats=None, kv_cache_eviction_events=[], spec_decoding_stats=None, kv_connector_stats=None, waiting_lora_adapters={}, running_lora_adapters={}, cudagraph_stats=None, perf_stats=None)
```

### Operating System

Ubuntu 24.04 LTS (Noble Numbat)

### CPU

AMD EPYC 9575F 64-Core Processor

### GPU

AMD Instinct MI355X

### ROCm Version

ROCm7.2.4

### ROCm Component

_No response_

### Steps to Reproduce

1. GPU: 8xMI355x
2. Docker: rocm/atom-dev:vllm-kimi-k3-20260807
3. Model: Kimi-K3
4. Launch server: [k3_server_crash.sh](https://github.com/user-attachments/files/31712973/k3_server_crash.sh)
5. Launch client: [repro_topk_crash.sh](https://github.com/user-attachments/files/31712981/repro_topk_crash.sh)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_

## 评论 (1)

### peizhang56 · 2026-09-01

Made a fix https://github.com/ROCm/aiter/pull/5191 
