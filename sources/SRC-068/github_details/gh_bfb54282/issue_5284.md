# [Issue #5284] [Bug] Ragged prefill benchmark enables unsupported CUDA Graph mode for CUTLASS

source: https://github.com/flashinfer-ai/flashinfer/issues/5284
state: open | updated: 2026-09-22T02:52:24Z
labels: needs-triage

## 正文

## Summary
The ragged-prefill benchmark enables CUDA Graph mode for an explicit CUTLASS backend by default. The wrapper now rejects this combination because its plan buffers are allocated on each plan() call. As a result, valid benchmark commands stop during wrapper preparation instead of returning benchmark results.

Observed on B200 and GB300 at `2694e1e` and again at `24c30bd`, for DeepSeek-R1 and cute-dsl-coverage-h128-MHA. These are observed failing revisions; the introducing commit has not been independently established.

## Failure
```text
the cutlass backend allocates its plan buffers per plan() call and is not CUDA-graph safe; use backend='auto' to get a graph-safe backend, or an explicit 'cudnn'/'fa2'
```

## Source attribution
At `2694e1e`, `benchmarks/routines/attention.py` sets `is_cuda_graph_compatible = not args.no_cuda_graph` and passes that value to the CUTLASS wrapper. The special case disabling graph mode applies only to `fa2`. The following `plan()` call reaches the deliberate CUTLASS graph-mode rejection in `flashinfer/prefill.py`.

The wrapper guard prevents unsafe replay. The benchmark should respect the backend restriction: skip the unsupported combination or run CUTLASS without graph capture, while keeping other supported backends testable. This report does not request removal of the safety guard.

## Reproduction
From the public repository's `benchmarks` directory, on B200 or GB300 at either observed failing revision:

```bash
python3 flashinfer_benchmark.py --routine BatchPrefillWithRaggedKVCacheWrapper --backends fa2 fa3 cutlass cudnn trtllm-native --batch_size 1 --s_qo 1024 --s_kv 1024 --num_qo_heads 128 --num_kv_heads 128 --head_dim_qk 192 --head_dim_vo 128 --random_actual_seq_len -vv --refcheck --causal --q_dtype bfloat16 --kv_dtype bfloat16 --allow_output_mismatch --generate_repro_command --case_tag "DeepSeek-R1"
```

```bash
python3 flashinfer_benchmark.py --routine BatchPrefillWithRaggedKVCacheWrapper --backends fa2 fa3 cutlass cudnn trtllm-native cute-dsl --batch_size 1 --s_qo 8192 --s_kv 8192 --num_qo_heads 128 --num_kv_heads 128 --head_dim_qk 128 --head_dim_vo 128 --random_actual_seq_len -vv --refcheck --causal --q_dtype bfloat16 --kv_dtype bfloat16 --allow_output_mismatch --generate_repro_command --case_tag "cute-dsl-coverage-h128-MHA"
```

The failure above is from completed CI executions; these commands have not been rerun locally. Adding `--no_cuda_graph` is a source-derived workaround to validate, not a verified passing result.

## CI evidence
- [GB300 completed execution](https://nv/flashinfer-ci/-/jobs/441094290)
- [B200 execution](https://nv/flashinfer-ci/-/jobs/441094381)

The same normalized failure and complete case commands recur at both observed revisions. No performance regression is inferred from the missing results.


## 评论 (2)

### LiRunGuo · 2026-09-22

!claim

I'd like to take this. The mechanism is still present on current main (`621fd46e`): `testBatchPrefillWithRaggedKVCacheWrapper` builds every wrapper with `use_cuda_graph=is_cuda_graph_compatible` except fa2, then calls `plan()`, which reaches the deliberate CUTLASS graph-mode rejection added in #5133.

Plan, keeping the wrapper's safety guard as-is: treat `cutlass` the way the routine already treats `fa2`. It gets planned with `use_cuda_graph=False` and timed without graph capture in `bench_gpu_time`, while the other backends in the same `--backends` list still run under graph replay. The routine prints an `[INFO]` line when it does this. `--no_cuda_graph` behaves as before. The change is confined to the ragged routine; the MLA routine's `cutlass` path has no equivalent guard and isn't affected.

One limitation: I only have Hopper hardware, where `cutlass` is filtered out of this routine by compute capability, so I can verify that the routine runs end to end in both modes on H200 but not the CUTLASS branch itself. If someone could run the DeepSeek-R1 command from the issue on B200/GB300 against the PR, that would close the loop. PR coming shortly.


### flashinfer-bot · 2026-09-22

Issue assigned to @LiRunGuo.
