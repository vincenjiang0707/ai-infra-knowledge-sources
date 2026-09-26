# [Issue #1933] Quantizing error for Qwen3.6 35B A3B

source: https://github.com/NVIDIA/Model-Optimizer/issues/1933
state: open | updated: 2026-08-02T22:08:39Z
labels: bug

## 正文

## Describe the bug
Qwen3.6-35B A3B NVPF4 Quantization  IndexError: tuple index out of range error

### Steps/Code to reproduce bug

docker run --rm -it --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864   -v "./output_models:/workspace/output_models"   -v "$HOME/.cache/huggingface:/root/.cache/huggi
ngface"   -e HF_TOKEN=$HF_TOKEN   nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc20   bash -c "                                                                                                                   
    git clone --depth 1 --branch main https://github.com/NVIDIA/Model-Optimizer.git /app/Model-Optimizer && \                                                                                                 
    cd /app/Model-Optimizer/ && \                                                                                                                                                                             
    pip install -e '.' && \                                                                                                                                                                                   
    cd /app/Model-Optimizer/examples/hf_ptq && \                                                                                                                                                              
    export ROOT_SAVE_PATH='/workspace/output_models' && \                                                                                                                                                     
    scripts/huggingface_example.sh --model 'Qwen/Qwen3.6-35B-A3B' --quant nvfp4 --tasks quant --tp 1                                                                                                          
  "                                                            


```
Loading safetensors weights in parallel: 100%|██████████| 3/3 [00:02<00:00,  1.18it/s]                                                                                                                        
[07/07/2026-03:31:36] [TRT-LLM] [E] [executor] Failed to initialize executor on rank 0: tuple index out of range                                                                                              
[07/07/2026-03:31:36] [TRT-LLM] [E] [executor] Traceback (most recent call last):                                                                                                                             
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/worker.py", line 302, in worker_main                                                                                                    
    worker: GenerationExecutorWorker = worker_cls(                                                                                                                                                            
                                       ^^^^^^^^^^^                                                                                                                                                            
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/worker.py", line 67, in __init__                                                                                                        
    self.setup_engine()                                                                                                                                                                                       
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/base_worker.py", line 286, in setup_engine                                                                                              
    self.engine = _create_py_executor(                                                                                                                                                                        
                  ^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                        
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/base_worker.py", line 257, in _create_py_executor                                                                                       
    _executor = create_executor(**args)                                                                                                                                                                       
                ^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                       
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/py_executor_creator.py", line 516, in create_py_executor                                                                       
    model_engine = PyTorchModelEngine(                                                                                                                                                                        
                   ^^^^^^^^^^^^^^^^^^^                                                                                                                                                                        
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/model_engine.py", line 341, in __init__                                                                                        
    self.model, moe_load_balancer = self.model_loader.load(                                                                                                                                                   
                                    ^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                   
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/model_loader.py", line 519, in load                                                                                            
    self._call_load_weights(model.load_weights, weights,                                                                                                                                                      
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/model_loader.py", line 1135, in _call_load_weights                                                                             
    load_method(weights, **kargs)                                                                                                                                                                             
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/modeling_qwen3_next.py", line 980, in load_weights                                                                                 
    new_weights = weight_mapper.preprocess_weights(weights)                                                                                                                                                   
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                   
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py", line 327, in preprocess_weights                                                          
    packed_weights = self._pack_split_projections(normalized_weights)                                                                                                                                         
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                         
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py", line 258, in _pack_split_projections                                                     
    q_tensor, k_tensor, v_tensor = split_packed_qkv(                                                                                                                                                          
                                   ^^^^^^^^^^^^^^^^^                                                                                                                                                          
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py", line 169, in _split_qkv_tensor                                                           
    assert tensor.shape[0] == expected_total, (                                                                                                                                                               
           ~~~~~~~~~~~~^^^                                                                                                                                                                                    
IndexError: tuple index out of range                                                                                                                                                                          
                                                   
[07/07/2026-03:31:36] [TRT-LLM] [E] [executor] Executor worker initialization error: Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/worker.py", line 302, in worker_main                                                                                               
    worker: GenerationExecutorWorker = worker_cls(                                                     
                                       ^^^^^^^^^^^                                                     
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/worker.py", line 67, in __init__
    self.setup_engine()                                                                                
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/base_worker.py", line 286, in setup_engine                                                                        
    self.engine = _create_py_executor( 
File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/base_worker.py", line 257, in _create_py_executor
    _executor = create_executor(**args)
                ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/py_executor_creator.py", line 516, in create_py_executor
    model_engine = PyTorchModelEngine(
                   ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/model_engine.py", line 341, in __init__
    self.model, moe_load_balancer = self.model_loader.load(
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/model_loader.py", line 519, in load
    self._call_load_weights(model.load_weights, weights,
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/pyexecutor/model_loader.py", line 1135, in _call_load_weights
    load_method(weights, **kargs)
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/modeling_qwen3_next.py", line 980, in load_weights
    new_weights = weight_mapper.preprocess_weights(weights)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py", line 327, in preprocess_weights
    packed_weights = self._pack_split_projections(normalized_weights)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py", line 258, in _pack_split_projections
    q_tensor, k_tensor, v_tensor = split_packed_qkv(
                                   ^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py", line 169, in _split_qkv_tensor
    assert tensor.shape[0] == expected_total, (
           ~~~~~~~~~~~~^^^
IndexError: tuple index out of range

IndexError: tuple index out of range

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/app/Model-Optimizer/examples/hf_ptq/run_tensorrt_llm.py", line 96, in <module>
    run(args)
  File "/app/Model-Optimizer/examples/hf_ptq/run_tensorrt_llm.py", line 71, in run
    llm = LLM(
          ^^^^
  File "/app/Model-Optimizer/modelopt/deploy/llm/generate.py", line 148, in __init__
    super().__init__(
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/llmapi/llm.py", line 1877, in __init__
    super().__init__(model, tokenizer, tokenizer_mode, skip_tokenizer_init,
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/llmapi/llm.py", line 1717, in __init__
    super().__init__(model,
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/llmapi/llm.py", line 349, in __init__
    self._build_model()
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/llmapi/llm.py", line 1824, in _build_model 
    self._executor = self._executor_cls.create(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                            22:42:35 [196/2078]
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/executor.py", line 639, in create 
    return GenerationExecutor._create_ipc_executor( 
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/executor.py", line 510, in _create_ipc_executor
    return GenerationExecutorProxy(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/proxy.py", line 150, in __init__
    self._start_executor_workers(worker_kwargs)
  File "/usr/local/lib/python3.12/dist-packages/tensorrt_llm/executor/proxy.py", line 437, in _start_executor_workers
    raise RuntimeError(
RuntimeError: Executor worker returned error
```


### Expected behavior

Working quantized model output


## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used: nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc20 
- OS: Ubuntu 22.04,
- CPU architecture: aarch64
- GPU: GB10
- GPU memory size: 128GB
- Number of GPUs:  1



## 评论 (5)

### heyparth1 · 2026-07-07

I'd like to work on this — opening a PR shortly.

### kristianpaul · 2026-07-07

Looks the issue is on Tensor RTT. I'll let this here but also look on their repo and/or create/link bug report on that side.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: cd71356b3da6054effff115da5971277a3ebe8dc73f6c465579de9c647600a56

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: f8c9398a05c9ed3cf201a018369ff6ad595d7ef219788870fa1214b86c4048b6

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 0bad577c8ce045cf7d809f2b96a751ad6cddce39f625dc4e3332019141a5f67e

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
