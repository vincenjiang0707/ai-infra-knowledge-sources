# [Issue #52] torch.nn.ConvTranspose3d  不支持计算

source: https://github.com/Ascend/pytorch/issues/52
state: open | updated: 2024-09-21T07:02:05Z
labels: 

## 正文

if torch set jit_compile= False,  torch.npu.set_compile_mode(jit_compile=False)，
torch.nn.ConvTranspose3d() in NPU compute is Error.

E60108: 2024-09-09-06:13:16.140.829 In op[conv3d_backprop_input], [prebuild failed, not support input size's shape [-1] and [-2]]
        TraceBack (most recent call last):
        Failed to compile Op [Conv3DTranspose1]. (oppath: [Compile /usr/local/Ascend/ascend-toolkit/8.0.RC2.alpha003/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/conv3d_transpose.py failed with errormsg/stack: File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/utils/errormgr/error_manager_util.py", line 69, in raise_runtime_error_cube
    raise RuntimeError(args_dict, *msgs)
RuntimeError: ({'errCode': 'E60108', 'op_name': 'conv3d_backprop_input', 'reason': "prebuild failed, not support input size's shape [-1] and [-2]"}, "In op[conv3d_backprop_input], [prebuild failed, not support input size's shape [-1] and [-2]]")
], optype: [Conv3DTranspose])
        Compile op[Conv3DTranspose1] failed, oppath[/usr/local/Ascend/ascend-toolkit/8.0.RC2.alpha003/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/conv3d_transpose.py], optype[Conv3DTranspose], taskID[9]. Please check op's compilation error message.[FUNC:ReportBuildErrMessage][FILE:fusion_manager.cc][LINE:751]
        [SubGraphOpt][Compile][ProcFailedCompTask] Thread[281465463632160] recompile single op[Conv3DTranspose1] failed[FUNC:ProcessAllFailedCompileTasks][FILE:tbe_op_store_adapter.cc][LINE:961]
        [SubGraphOpt][Compile][ParalCompOp] Thread[281465463632160] process fail task failed[FUNC:ParallelCompileOp][FILE:tbe_op_store_adapter.cc][LINE:1009]
        [SubGraphOpt][Compile][CompOpOnly] CompileOp failed.[FUNC:CompileOpOnly][FILE:op_compiler.cc][LINE:1112]
        [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1422]
        Call OptimizeFusedGraph failed, ret:-1, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph2[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:119]
        subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:1011]
        build graph failed, graph id:0, ret:-1[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1608]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

[W compiler_depend.ts:563] Warning: 0Failed to find function aclrtGetMemUceInfo (function operator())
Traceback (most recent call last):
  File "/root/dat/code/run_test/test_ConvTranspose3d.py", line 19, in <module>
    conv_transpose_layer = torch.nn.ConvTranspose3d(in_channels=3, out_channels=3, kernel_size=3).to('npu')
  File "/usr/local/python3.10.12/lib/python3.10/site-packages/torch_npu/utils/_module.py", line 75, in to
    return self._apply(convert)
  File "/usr/local/python3.10.12/lib/python3.10/site-packages/torch/nn/modules/module.py", line 833, in _apply
    param_applied = fn(param)
  File "/usr/local/python3.10.12/lib/python3.10/site-packages/torch_npu/utils/_module.py", line 73, in convert
    return t.to(device, dtype if t.is_floating_point() or t.is_complex() else None, non_blocking)
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Conv3DTranspose.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
[ERROR] 2024-09-09-06:13:16 (PID:2731301, Device:0, RankID:-1) ERR00100 PTA call acl api failed

torch is 2.1.0
python 3.10
310P



## 评论 (1)

### yunyiyun · 2024-09-21

https://gitee.com/ascend/pytorch/issues/IAQRLU?from=project-issue
