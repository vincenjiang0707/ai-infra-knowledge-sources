# [Issue #61] 运行vllm op编译失败

source: https://github.com/Ascend/pytorch/issues/61
state: open | updated: 2025-03-29T10:46:20Z
labels: 

## 正文

## 报错信息
INFO 03-04 12:56:50 [loader.py:422] Loading weights took 0.73 seconds
start compile Ascend C operator RmsNorm. kernel name is te_rmsnorm_aae85cefc31cdd975d122e4e5f45a69aa294b5f0c3a33875e6926398caa9e973_1
compile Ascend C operator: RmsNorm success!
ERROR 03-04 12:57:08 [engine.py:409] InnerRun:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:230 OPS function error: RepeatInterleave, error code is 500002
ERROR 03-04 12:57:08 [engine.py:409] [ERROR] 2025-03-04-12:57:08 (PID:1506531, Device:0, RankID:-1) ERR01100 OPS call acl api failed
ERROR 03-04 12:57:08 [engine.py:409] [Error]: A GE error occurs in the system.
ERROR 03-04 12:57:08 [engine.py:409]         Rectify the fault based on the error information in the ascend log.
ERROR 03-04 12:57:08 [engine.py:409] E40024: 2025-03-04-12:56:24.963.302 Failed call Python Func/Meathod [get_binfile_sha256_hash_from_c], Reason[SystemError: PY_SSIZE_T_CLEAN macro must be defined for '#' formats
ERROR 03-04 12:57:08 [engine.py:409] ] 
ERROR 03-04 12:57:08 [engine.py:409]         Possible Cause: The Python Func/Meathod does not exist.
ERROR 03-04 12:57:08 [engine.py:409]         TraceBack (most recent call last):
ERROR 03-04 12:57:08 [engine.py:409]         [SubGraphOpt][ParseJson][PkgTvmJsInfo] Parse blockDim failed, the json file:/usr/include/kernel_meta/kernel_meta_6329215882311868227/kernel_meta/te_repeatinterleave_700ef95624df2241182af76e48e66bc5d93a192227847ea739c9ae8cf29a9d43_1.json.[FUNC:PackageTvmJsonInfo][FILE:tbe_json_parse.cc][LINE:953]
ERROR 03-04 12:57:08 [engine.py:409]         [SubGraphOpt][Compile][Normal] Failed to parse json or compress op for graph[partition0_rank1_new_sub_graph2].[FUNC:ReCompileWithNoFusionStrategy][FILE:op_compiler_normal.cc][LINE:86]
ERROR 03-04 12:57:08 [engine.py:409]         [SubGraphOpt][Compile][RunCmplProc] Failed to re-compile op with no lx fusion for graph [partition0_rank1_new_sub_graph2][FUNC:RunCompileProcess][FILE:op_compiler_normal.cc][LINE:153]
ERROR 03-04 12:57:08 [engine.py:409]         [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1385]
ERROR 03-04 12:57:08 [engine.py:409]         Call OptimizeFusedGraph failed, ret:-1, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph2[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:126]
ERROR 03-04 12:57:08 [engine.py:409]         subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:1021]
ERROR 03-04 12:57:08 [engine.py:409]         build graph failed, graph id:20, ret:-1[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1615]
ERROR 03-04 12:57:08 [engine.py:409]         [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 03-04 12:57:08 [engine.py:409]         [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-04 12:57:08 [engine.py:409]         build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-04 12:57:08 [engine.py:409] Traceback (most recent call last):
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 400, in run_mp_engine
ERROR 03-04 12:57:08 [engine.py:409]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 125, in from_engine_args
ERROR 03-04 12:57:08 [engine.py:409]     return cls(ipc_path=ipc_path,
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 77, in __init__
ERROR 03-04 12:57:08 [engine.py:409]     self.engine = LLMEngine(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 277, in __init__
ERROR 03-04 12:57:08 [engine.py:409]     self._initialize_kv_caches()
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 426, in _initialize_kv_caches
ERROR 03-04 12:57:08 [engine.py:409]     self.model_executor.determine_num_available_blocks())
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
ERROR 03-04 12:57:08 [engine.py:409]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 03-04 12:57:08 [engine.py:409]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/utils.py", line 2232, in run_method
ERROR 03-04 12:57:08 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-04 12:57:08 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/root/USERNAME/OthersRepo/vllm-ascend/vllm_ascend/worker.py", line 226, in determine_num_available_blocks
ERROR 03-04 12:57:08 [engine.py:409]     self.model_runner.profile_run()
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-04 12:57:08 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/root/USERNAME/OthersRepo/vllm-ascend/vllm_ascend/model_runner.py", line 1341, in profile_run
ERROR 03-04 12:57:08 [engine.py:409]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-04 12:57:08 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/root/USERNAME/OthersRepo/vllm-ascend/vllm_ascend/model_runner.py", line 1125, in execute_model
ERROR 03-04 12:57:08 [engine.py:409]     hidden_or_intermediate_states = model_executable(
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 463, in forward
ERROR 03-04 12:57:08 [engine.py:409]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
ERROR 03-04 12:57:08 [engine.py:409]     return self.forward(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 339, in forward
ERROR 03-04 12:57:08 [engine.py:409]     hidden_states, residual = layer(
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 243, in forward
ERROR 03-04 12:57:08 [engine.py:409]     hidden_states = self.self_attn(
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 176, in forward
ERROR 03-04 12:57:08 [engine.py:409]     q, k = self.rotary_emb(positions, q, k)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-04 12:57:08 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
ERROR 03-04 12:57:08 [engine.py:409]     return self._forward_method(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/root/USERNAME/OthersRepo/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 45, in rope_forward_oot
ERROR 03-04 12:57:08 [engine.py:409]     torch_npu._npu_rotary_embedding(
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 45, in wrapper
ERROR 03-04 12:57:08 [engine.py:409]     return api_func(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 53, in generated_function
ERROR 03-04 12:57:08 [engine.py:409]     return getattr(torch.ops.atb, api_name)(*args, **kwargs)
ERROR 03-04 12:57:08 [engine.py:409]   File "/home/conda3/envs/swift/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 03-04 12:57:08 [engine.py:409]     return self._op(*args, **(kwargs or {}))
ERROR 03-04 12:57:08 [engine.py:409] RuntimeError: InnerRun:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:230 OPS function error: RepeatInterleave, error code is 500002
ERROR 03-04 12:57:08 [engine.py:409] [ERROR] 2025-03-04-12:57:08 (PID:1506531, Device:0, RankID:-1) ERR01100 OPS call acl api failed
ERROR 03-04 12:57:08 [engine.py:409] [Error]: A GE error occurs in the system.
ERROR 03-04 12:57:08 [engine.py:409]         Rectify the fault based on the error information in the ascend log.
ERROR 03-04 12:57:08 [engine.py:409] E40024: 2025-03-04-12:56:24.963.302 Failed call Python Func/Meathod [get_binfile_sha256_hash_from_c], Reason[SystemError: PY_SSIZE_T_CLEAN macro must be defined for '#' formats
ERROR 03-04 12:57:08 [engine.py:409] ] 
ERROR 03-04 12:57:08 [engine.py:409]         Possible Cause: The Python Func/Meathod does not exist.
ERROR 03-04 12:57:08 [engine.py:409]         TraceBack (most recent call last):
ERROR 03-04 12:57:08 [engine.py:409]         [SubGraphOpt][ParseJson][PkgTvmJsInfo] Parse blockDim failed, the json file:/usr/include/kernel_meta/kernel_meta_6329215882311868227/kernel_meta/te_repeatinterleave_700ef95624df2241182af76e48e66bc5d93a192227847ea739c9ae8cf29a9d43_1.json.[FUNC:PackageTvmJsonInfo][FILE:tbe_json_parse.cc][LINE:953]
ERROR 03-04 12:57:08 [engine.py:409]         [SubGraphOpt][Compile][Normal] Failed to parse json or compress op for graph[partition0_rank1_new_sub_graph2].[FUNC:ReCompileWithNoFusionStrategy][FILE:op_compiler_normal.cc][LINE:86]
ERROR 03-04 12:57:08 [engine.py:409]         [SubGraphOpt][Compile][RunCmplProc] Failed to re-compile op with no lx fusion for graph [partition0_rank1_new_sub_graph2][FUNC:RunCompileProcess][FILE:op_compiler_normal.cc][LINE:153]
ERROR 03-04 12:57:08 [engine.py:409]         [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1385]
ERROR 03-04 12:57:08 [engine.py:409]         Call OptimizeFusedGraph failed, ret:-1, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph2[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:126]
ERROR 03-04 12:57:08 [engine.py:409]         subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:1021]
ERROR 03-04 12:57:08 [engine.py:409]         build graph failed, graph id:20, ret:-1[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1615]
ERROR 03-04 12:57:08 [engine.py:409]         [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 03-04 12:57:08 [engine.py:409]         [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-04 12:57:08 [engine.py:409]         build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

## 环境信息

torch_npu 2.5.1.dev20250226
vllm 0.1.dev1+gbf13d40.empty
vllm_ascend 0.1.dev70+g839dac8

package_name=Ascend-cann-toolkit
version=8.0.RC1
innerversion=V100R001C17SPC001B240
compatible_version=[V100R001C15,V100R001C18],[V100R001C30],[V100R001C13],[V100R003C11],[V100R001C29],[V100R001C10]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.RC1/aarch64-linux

Ascend-cann-nnal_8.0.0_linux-aarch64

## 评论 (2)

### yunyiyun · 2025-03-29

请使用vllm_ascend相关配套版本

### zhangsan5213 · 2025-03-29

> 请使用vllm_ascend相关配套版本

不是这问题，当时就是按照vllm_ascend库一步步配置的。应该是910ProB这卡没有对应的包。
