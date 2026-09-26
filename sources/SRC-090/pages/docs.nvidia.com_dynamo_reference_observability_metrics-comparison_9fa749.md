source: https://docs.nvidia.com/dynamo/reference/observability/metrics-comparison
lastmod: 2026-09-24T19:58:16.636Z

**REQUEST STATE & QUEUE** | | | | |
| Running requests | `num_requests_running` | `num_running_reqs` | - |
| Waiting/queued requests | `num_requests_waiting` | `num_queue_reqs` | - |
| Queue time | `request_queue_time_seconds` | `queue_time_seconds` | `request_queue_time_seconds` |
| Grammar queue | - | `num_grammar_queue_reqs` | - |
| Offline batch running | - | `num_running_reqs_offline_batch` | - |
| Prefill prealloc queue | - | `num_prefill_prealloc_queue_reqs` | - |
| Prefill inflight queue | - | `num_prefill_inflight_queue_reqs` | - |
| Decode prealloc queue | - | `num_decode_prealloc_queue_reqs` | - |
| Decode transfer queue | - | `num_decode_transfer_queue_reqs` | - |
**LATENCY** | | | | |
| Time to first token | `time_to_first_token_seconds` | `time_to_first_token_seconds` | `time_to_first_token_seconds` |
| Inter-token latency | `inter_token_latency_seconds` | `inter_token_latency_seconds` | - |
| E2E request latency | `e2e_request_latency_seconds` | `e2e_request_latency_seconds` | `e2e_request_latency_seconds` |
| Time per output token | `request_time_per_output_token_seconds` | - | `time_per_output_token_seconds` |
| Inference time | `request_inference_time_seconds` | - | - |
| Prefill time | `request_prefill_time_seconds` | - | - |
| Decode time | `request_decode_time_seconds` | - | - |
| Per-stage latency | - | `per_stage_req_latency_seconds` | - |
**TOKEN METRICS** | | | | |
| Prompt/prefill tokens | `prompt_tokens_total` | `prompt_tokens_total` | - |
| Generation tokens | `generation_tokens_total` | `generation_tokens_total` | - |
| Request prompt tokens (histogram) | `request_prompt_tokens` | - | - |
| Request generation tokens (histogram) | `request_generation_tokens` | - | - |
| Iteration tokens | `iteration_tokens_total` | - | - |
| Max generation tokens | `request_max_num_generation_tokens` | - | - |
| Realtime tokens | - | `realtime_tokens_total` | - |
| Used tokens | - | `num_used_tokens` | - |
| Cached tokens by source | - | `cached_tokens_total` | - |
| Prefill KV computed tokens | `request_prefill_kv_computed_tokens` | - | - |
| Prompt tokens by source | `prompt_tokens_by_source_total` | - | - |
| Prompt tokens cached | `prompt_tokens_cached_total` | - | - |
| Prompt tokens recomputed | `prompt_tokens_recomputed_total` | - | - |
**REQUEST SUCCESS & ABORT** | | | | |
| Request success (by reason) | `request_success_total` | - | `request_success_total` |
| Total requests | - | `num_requests_total` | - |
| Aborted requests | - | - | `num_aborted_requests_total` |
**REQUEST TYPES** | | | | |
| Image requests | - | - | `request_type_image_total` |
| Structured output requests | - | - | `request_type_structured_output_total` |
**KV CACHE & MEMORY** | | | | |
| KV cache usage % | `kv_cache_usage_perc` | - | - |
| KV cache hit rate | - | - | `kv_cache_hit_rate` |
| KV cache utilization | - | - | `kv_cache_utilization` |
| Token usage | - | `token_usage` | - |
| Max total tokens | - | `max_total_num_tokens` | - |
| SWA token usage | - | `swa_token_usage` | - |
| Mamba usage | - | `mamba_usage` | - |
| Pending prealloc token usage | - | `pending_prealloc_token_usage` | - |
**PREFIX CACHE** | | | | |
| Cache hit rate | - | `cache_hit_rate` | - |
| Cache config info | `cache_config_info` | `cache_config_info` | - |
| Prefix cache queries | `prefix_cache_queries_total` | - | - |
| Prefix cache hits | `prefix_cache_hits_total` | - | - |
| External prefix cache queries | `external_prefix_cache_queries_total` | - | - |
| External prefix cache hits | `external_prefix_cache_hits_total` | - | - |
**MULTI-MODAL CACHE** | | | | |
| MM cache queries | `mm_cache_queries_total` | - | - |
| MM cache hits | `mm_cache_hits_total` | - | - |
**ENGINE STATE** | | | | |
| Engine sleep state | `engine_sleep_state` | - | - |
| Engine startup time | - | `engine_startup_time` | - |
| Engine load weights time | - | `engine_load_weights_time` | - |
| Estimated FLOPs per GPU | `estimated_flops_per_gpu_total` | - | - |
| Estimated read bytes per GPU | `estimated_read_bytes_per_gpu_total` | - | - |
| Estimated write bytes per GPU | `estimated_write_bytes_per_gpu_total` | - | - |
| CUDA graph state | - | `is_cuda_graph` | - |
| CUDA graph passes | - | `cuda_graph_passes_total` | - |
| Utilization | - | `utilization` | - |
| New token ratio | - | `new_token_ratio` | - |
**PREEMPTION & RETRACTION** | | | | |
| Preemptions | `num_preemptions_total` | - | - |
| Retracted requests | - | `num_retracted_reqs` | - |
| Number of retractions | - | `num_retractions` | - |
| Paused requests | - | `num_paused_reqs` | - |
**REQUEST PARAMETERS** | | | | |
| Request param n | `request_params_n` | - | - |
| Request param max_tokens | `request_params_max_tokens` | - | - |
**THROUGHPUT & PERFORMANCE** | | | | |
| Generation throughput | - | `gen_throughput` | - |
| Decode sum sequence lens | - | `decode_sum_seq_lens` | - |
**ROUTING** | | | | |
| Unique running routing keys | - | `num_unique_running_routing_keys` | - |
| Routing key all req count | - | `routing_key_all_req_count` | - |
| Routing key running req count | - | `routing_key_running_req_count` | - |
**SPECULATIVE DECODING** | | | | |
| Spec accept length | - | `spec_accept_length` | - |
| Spec accept rate | - | `spec_accept_rate` | - |
**KV TRANSFER** | | | | |
| KV transfer speed (GB/s) | - | `kv_transfer_speed_gb_s` | `kv_transfer_speed_gb_s` |
| KV transfer latency | - | `kv_transfer_latency_ms` | `kv_transfer_latency_seconds` |
| KV transfer bootstrap (ms) | - | `kv_transfer_bootstrap_ms` | - |
| KV transfer alloc (ms) | - | `kv_transfer_alloc_ms` | - |
| KV transfer total (MB) | - | `kv_transfer_total_mb` | - |
| KV transfer bytes | - | - | `kv_transfer_bytes` |
| KV transfer success | - | - | `kv_transfer_success_total` |