# [Issue #1428] ROCm6.2 Error cublasLt Encountered Error!

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1428
state: closed | updated: 2026-02-21T20:10:03Z
labels: ROCm

## 正文

### System Info

OS: WSL2 Ubuntu22.04
bitsandbytes: 0.44.1.dev0+cd73601
torch: 2.5.1+rocm6.2
GPU: RX 7900XT

### Reproduction

Ask questions about the 8-bit quantization model, the error cublasLt ran into an error!, and the 4-bit model will have no problem

error info:
`2024-11-24 22:28:21,223 xinference.model.llm.transformers.utils 21723 ERROR    Internal error for batch inference: cublasLt ran into an error!.
Traceback (most recent call last):
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xinference/model/llm/transformers/utils.py", line 483, in batch_inference_one_step
    _batch_inference_one_step_internal(
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xinference/model/llm/transformers/utils.py", line 317, in _batch_inference_one_step_internal
    out = model(**inf_kws, use_cache=True, past_key_values=past_key_values)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/transformers/models/qwen2/modeling_qwen2.py", line 1164, in forward
    outputs = self.model(
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/transformers/models/qwen2/modeling_qwen2.py", line 895, in forward
    layer_outputs = decoder_layer(
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/transformers/models/qwen2/modeling_qwen2.py", line 623, in forward
    hidden_states, self_attn_weights, present_key_value = self.self_attn(
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/transformers/models/qwen2/modeling_qwen2.py", line 501, in forward
    query_states = self.q_proj(hidden_states)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/accelerate/hooks.py", line 170, in new_forward
    output = module._old_forward(*args, **kwargs)
  File "/root/bitsandbytes/bitsandbytes/nn/modules.py", line 862, in forward
    out = bnb.matmul(x, self.weight, bias=self.bias, state=self.state)
  File "/root/bitsandbytes/bitsandbytes/autograd/_functions.py", line 567, in matmul
    return MatMul8bitLt.apply(A, B, out, bias, state)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/torch/autograd/function.py", line 575, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
  File "/root/bitsandbytes/bitsandbytes/autograd/_functions.py", line 406, in forward
    out32, Sout32 = F.igemmlt(C32A, state.CxB, SA, state.SB)
  File "/root/bitsandbytes/bitsandbytes/functional.py", line 1744, in igemmlt
    return backends[A.device.type].igemmlt(A, B, SA, SB, out=out, Sout=Sout, dtype=dtype)
  File "/root/bitsandbytes/bitsandbytes/backends/cuda.py", line 360, in igemmlt
    raise Exception("cublasLt ran into an error!")
Exception: cublasLt ran into an error!
2024-11-24 22:28:21,232 xinference.api.restful_api 21131 ERROR    Chat completion stream got an error: [address=0.0.0.0:33279, pid=21723] cublasLt ran into an error!
Traceback (most recent call last):
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xinference/api/restful_api.py", line 2010, in stream_results
    async for item in iterator:
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/api.py", line 340, in __anext__
    return await self._actor_ref.__xoscar_next__(self._uid)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/context.py", line 231, in send
    return self._process_result_message(result)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/context.py", line 102, in _process_result_message
    raise message.as_instanceof_cause()
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/pool.py", line 659, in send
    result = await self._run_coro(message.message_id, coro)
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/backends/pool.py", line 370, in _run_coro
    return await coro
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/api.py", line 384, in __on_receive__
    return await super().__on_receive__(message)  # type: ignore
  File "xoscar/core.pyx", line 558, in __on_receive__
    raise ex
  File "xoscar/core.pyx", line 520, in xoscar.core._BaseActor.__on_receive__
    async with self._lock:
  File "xoscar/core.pyx", line 521, in xoscar.core._BaseActor.__on_receive__
    with debug_async_timeout('actor_lock_timeout',
  File "xoscar/core.pyx", line 526, in xoscar.core._BaseActor.__on_receive__
    result = await result
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/api.py", line 431, in __xoscar_next__
    raise e
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/api.py", line 419, in __xoscar_next__
    r = await asyncio.create_task(_async_wrapper(gen))
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xoscar/api.py", line 409, in _async_wrapper
    return await _gen.__anext__()  # noqa: F821
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xinference/core/model.py", line 475, in _to_async_gen
    async for v in gen:
  File "/root/miniconda3/envs/xinf/lib/python3.10/site-packages/xinference/core/model.py", line 671, in _queue_consumer
    raise RuntimeError(res[len(XINFERENCE_STREAMING_ERROR_FLAG) :])
RuntimeError: [address=0.0.0.0:33279, pid=21723] cublasLt ran into an error!`

### Expected behavior

8bit quantization model normal answer

## 评论 (1)

### TimDettmers · 2026-02-21

Closing this issue due to insufficient information and no activity for over a year. The `cublasLt` error on ROCm can be caused by hipBLAS architecture compatibility issues. This was reported on an old dev build (0.44.1.dev0) through a third-party application (xinference).

If you're still hitting this on the latest bitsandbytes with ROCm, please open a new issue with the output of `python -m bitsandbytes` and a minimal reproduction script outside of third-party applications.
