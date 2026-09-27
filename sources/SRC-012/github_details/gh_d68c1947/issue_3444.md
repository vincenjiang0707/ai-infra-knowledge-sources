# [Issue #3444] [Bug] In the MLC_LLM branch of qwen3-vl, when running the qwen3-vl model, a Segfault error occurred.

source: https://github.com/mlc-ai/mlc-llm/issues/3444
state: open | updated: 2026-03-27T00:18:18Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->

## To Reproduce

Steps to reproduce the behavior:

1.Build using the qwen3-vl branch from the MLC_LLM source code
1.Use `Qwen/Qwen3-VL-2B-Instruct` ,Use mlc_llm to compile and get `Qwen3-VL-2B-Instruct_q0f16-rocm.so`
1.Use CLI: `python -m mlc_llm chat ./model/Qwen3-VL-2B-Instruct_q0f16-MLC --model-lib ./libs/Qwen3-VL-2B-Instruct_q0f16-rocm.so --device rocm`

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->
```cmd
[2026-03-04 11:30:58] INFO auto_device.py:82: Found device: rocm:0
[2026-03-04 11:30:58] INFO auto_device.py:82: Found device: rocm:1
[2026-03-04 11:30:58] INFO engine_base.py:142: Using library model: ./libs/Qwen3-VL-2B-Instruct_q0f16-rocm.so
[11:30:59] /vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/config.cc:798: Under mode "local", max batch size will be set to 4, max KV cache token capacity will be set to 8192, prefill chunk size will be set to 2048. 
[11:30:59] /vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/config.cc:798: Under mode "interactive", max batch size will be set to 1, max KV cache token capacity will be set to 131230, prefill chunk size will be set to 2048. 
[11:30:59] /vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/config.cc:798: Under mode "server", max batch size will be set to 128, max KV cache token capacity will be set to 128512, prefill chunk size will be set to 2048. 
[11:30:59] /vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/config.cc:879: The actual engine mode is "interactive". So max batch size is 1, max KV cache token capacity is 131230, prefill chunk size is 2048.
[11:30:59] /vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/config.cc:884: Estimated total single GPU memory usage: 20875.997 MB (Parameters: 4057.945 MB. KVCache: 14425.703 MB. Temporary buffer: 2392.348 MB). The actual usage might be slightly larger than the estimated number.
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

!!!!!!! Segfault encountered !!!!!!!
  File "./signal/../sysdeps/unix/sysv/linux/x86_64/libc_sigaction.c", line 0, in 0x00007b76efa4532f
  File "/vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/model.cc", line 111, in mlc::llm::serve::ModelImpl::TokenEmbed(tvm::ffi::Shape, tvm::ffi::ObjectRef*, int)
  File "/vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/data.cc", line 107, in mlc::llm::serve::TokenDataNode::GetEmbedding(mlc::llm::serve::Model, tvm::ffi::ObjectRef*, int) const
  File "/vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/engine_actions/new_request_prefill.cc", line 129, in mlc::llm::serve::NewRequestPrefillActionObj::Step(mlc::llm::serve::EngineState)
  File "/vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/engine.cc", line 752, in mlc::llm::serve::EngineImpl::Step()
  File "/vol2/xudongtian/TVM/mlc-llm_qwen3vl/cpp/serve/threaded_engine.cc", line 185, in mlc::llm::serve::ThreadedEngineImpl::RunBackgroundLoop()
  File "/usr/local/src/conda/python-3.11.14/Objects/call.c", line 343, in _PyObject_Call
  File "/usr/local/src/conda/python-3.11.14/Objects/call.c", line 355, in PyObject_Call
  File "/usr/local/src/conda/python-3.11.14/Python/ceval.c", line 7349, in do_call_core
  File "/usr/local/src/conda/python-3.11.14/Python/ceval.c", line 5376, in _PyEval_EvalFrameDefault
  File "/usr/local/src/conda/python-3.11.14/Include/internal/pycore_ceval.h", line 73, in _PyEval_EvalFrame
  File "/usr/local/src/conda/python-3.11.14/Python/ceval.c", line 6434, in _PyEval_Vector
  File "/usr/local/src/conda/python-3.11.14/Objects/call.c", line 393, in _PyFunction_Vectorcall
  File "/usr/local/src/conda/python-3.11.14/Include/internal/pycore_call.h", line 92, in _PyObject_VectorcallTstate
  File "/usr/local/src/conda/python-3.11.14/Objects/classobject.c", line 67, in method_vectorcall
  File "/usr/local/src/conda/python-3.11.14/Modules/_threadmodule.c", line 1124, in thread_run
  File "/usr/local/src/conda/python-3.11.14/Python/thread_pthread.h", line 241, in pythread_wrapper
  File "./nptl/pthread_create.c", line 447, in start_thread
  File "../sysdeps/unix/sysv/linux/x86_64/clone3.S", line 78, in clone3
  File "<unknown>", line 0, in 0xffffffffffffffff

Segmentation fault (core dumped)
```
One more thing, After the gen config in mlc_llm, I included `"vocab_size": 151936,"prefill_chunk_size": 2048 ` in the "model_config" section of the "mlc-chat-config.json" file. If these are not included, the following errors will occur.
```cmd
ValueError: Check failed: (it != json.end()) is false: key `vocab_size` not found in the JSON object

ValueError: Check failed: (it != json.end()) is false: key `prefill_chunk_size` not found in the JSON object
```

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): ROCM
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Ubuntu
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...) : AMD Radeon RX 7900 XTX
 - How you installed MLC-LLM (`conda`, source): Build from Source,
 - How you installed TVM (`pip`, source):Build from Source,
 - Python version (e.g. 3.10): 3.11
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (1)

### JiwaniZakir · 2026-03-27

The segfault appears to occur during or immediately after KV cache/memory allocation, given the log cuts off mid-sentence at the memory estimation line in `config.cc:884`. With the interactive mode KV cache estimated at ~14.4 GB and total estimated usage at ~20.9 GB, this could be a ROCm memory allocation failure that manifests as a segfault rather than a clean out-of-memory error — particularly if the vision encoder's additional memory footprint (absent in standard LLM models) pushes actual usage beyond what's available and the ROCm allocator doesn't handle the failure gracefully. A likely place to look is the KV cache initialization path in the engine, specifically how the Qwen3-VL branch wires up the visual token KV budget alongside the language model's cache, as a mismatch in the expected vs. allocated buffer sizes for multimodal inputs could cause a null/invalid pointer dereference when the engine first tries to use those buffers.
