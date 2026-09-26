# [Issue #148] torch_npu 2.1.0 + CANN 8.0.0 在昇腾910B上微调Qwen3-ASR 模型

source: https://github.com/Ascend/pytorch/issues/148
state: open | updated: 2026-07-02T11:01:16Z
labels: 

## 正文

**核心问题是**“  E90003: Compile operator failed
  bfloat16 of tbe.dsl.transdata is not supported.
  optype: [TransData]
”



**### 在模型微调训练时遇到如下bug：**
“/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/torch_npu/dynamo/__init__.py:18: UserWarning: Register eager implementation for the 'npu' backend of dynamo, as torch_npu was
  not compiled with torchair.
    warnings.warn(
  [device] train_device=npu:0, model_dtype=torch.bfloat16
  The following generation flags are not valid and may be ignored: ['temperature']. Set `TRANSFORMERS_VERBOSITY=info` for more details.
  /home/zhenglin/lrs/code/Qwen3-ASR-main/finetuning/qwen3_asr_sft.py:348: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `CastFloatInputsTrainer.__init__`. Use
  `processing_class` instead.
    trainer = CastFloatInputsTrainer(
  Detected kernel version 4.14.0, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
  The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values.
  Updated tokens: {'eos_token_id': 151645, 'pad_token_id': 151643}.
    0%|
  | 0/8728 [00:00<?, ?it/s][W NeKernelNpu.cpp:45] Warning: The oprator of ne is executed, Currently High Accuracy but Low Performance OP with 64-bit has been used, Please Do Some Cast at Python Functions with
  32-bit for Better Performance! (function operator())
  [W AddKernelNpu.cpp:80] Warning: The oprator of add is executed, Currently High Accuracy but Low Performance OP with 64-bit has been used, Please Do Some Cast at Python Functions with 32-bit for Better
  Performance! (function operator())
  ...../usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/qwen_asr/core/transformers_backend/modeling_qwen3_asr.py:691: UserWarning: AutoNonVariableTypeMode is deprecated and will be removed in 1.10
  release. For kernel implementations please use AutoDispatchBelowADInplaceOrView instead, If you are looking for a user facing API to enable running your inference-only workload, please use
  c10::InferenceMode. Using AutoDispatchBelowADInplaceOrView in user code is under risk of producing silent wrong result in some edge cases. See Note [AutoDispatchBelowAutograd] for more details. (Triggered
  internally at torch_npu/csrc/aten/common/TensorFactories.cpp:74.)
    chunk_lengths[chunk_lengths == 0] = self.n_window * 2
  [W OpCommand.cpp:75] Warning: [Check][offset] Check input storage_offset[%ld] = 0 failed, result is untrustworthy100 (function operator())
  ...E90003: [PID: 9680] 2026-06-23-09:34:04.407.177 Compile operator failed, cause: Template constraint, detailed information: bfloat16 of tbe.dsl.transdata is not supported.
          TraceBack (most recent call last):
          Failed to compile Op [trans_TransData_17,]. (oppath: [Compile /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/trans_data.py failed with errormsg/stack: File "/
  usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/dsl/compute/util.py", line 1886, in dtype_check_decorator
      raise RuntimeError(dict_args, get_error_message(dict_args))
  RuntimeError: ({'errCode': 'E90003', 'detailed_cause': 'bfloat16 of tbe.dsl.transdata is not supported'}, 'Compile operator failed, cause: Template constraint, detailed information: bfloat16 of
  tbe.dsl.transdata is not supported.')
  ], optype: [TransData])
          Compile op[trans_TransData_17,] failed, oppath[/usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/trans_data.py], optype[TransData], taskID[123]. Please check op's
  compilation error message.[FUNC:ReportBuildErrMessage][FILE:fusion_manager.cc][LINE:367]
          [SubGraphOpt][Compile][ProcFailedCompTask] Thread[281449366221152] recompile single op[trans_TransData_17] failed[FUNC:ProcessAllFailedCompileTasks][FILE:tbe_op_store_adapter.cc][LINE:1069]
          [SubGraphOpt][Compile][ParalCompOp] Thread[281449366221152] process fail task failed[FUNC:ParallelCompileOp][FILE:tbe_op_store_adapter.cc][LINE:1116]
          [SubGraphOpt][Compile][CompOpOnly] CompileOp failed.[FUNC:CompileOpOnly][FILE:op_compiler.cc][LINE:1190]
          [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1410]
          Call OptimizeFusedGraph failed, ret:4294967295, engine_name:AIcoreEngine, graph_name:partition0_rank6_new_sub_graph8[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:119]
          subgraph 5 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:815]
          build graph failed, graph id:68, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1618]
          [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
          [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
          build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

  Traceback (most recent call last):
    File "/home/zhenglin/lrs/code/Qwen3-ASR-main/finetuning/qwen3_asr_sft.py", line 371, in <module>
      main()
    File "/home/zhenglin/lrs/code/Qwen3-ASR-main/finetuning/qwen3_asr_sft.py", line 367, in main
      trainer.train()
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/transformers/trainer.py", line 2325, in train
      return inner_training_loop(
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/transformers/trainer.py", line 2674, in _inner_training_loop
      tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/transformers/trainer.py", line 4020, in training_step
      loss = self.compute_loss(model, inputs, num_items_in_batch=num_items_in_batch)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/transformers/trainer.py", line 4110, in compute_loss
      outputs = model(**inputs)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
      return self._call_impl(*args, **kwargs)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
      return forward_call(*args, **kwargs)
    File "/home/zhenglin/lrs/code/Qwen3-ASR-main/finetuning/qwen3_asr_sft.py", line 55, in forward
      return self.thinker.forward(
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/transformers/utils/generic.py", line 918, in wrapper
      output = func(self, *args, **kwargs)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/qwen_asr/core/transformers_backend/modeling_qwen3_asr.py", line 1196, in forward
      audio_features = self.get_audio_features(
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/qwen_asr/core/transformers_backend/modeling_qwen3_asr.py", line 1125, in get_audio_features
      audio_output = self.audio_tower(
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
      return self._call_impl(*args, **kwargs)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
      return forward_call(*args, **kwargs)
    File "/usr/local/miniconda3/envs/qwen3/lib/python3.10/site-packages/qwen_asr/core/transformers_backend/modeling_qwen3_asr.py", line 718, in forward
      hidden_states = padded_embed[padded_mask_after_cnn]
  RuntimeError: The Inner error as above.
   ASCEND kernel errors might be asynchronously reported at some other API call, so the stacktrace may not correct.
  For getting the stacktrace of OP in PyTorch, consider passing ASCEND_LAUNCH_BLOCKING=1.

”




## 评论 (1)

### lrs02 · 2026-07-02

Found  a way to solve this problem. Just change into 910B2 and update CANN  and torch_npu
