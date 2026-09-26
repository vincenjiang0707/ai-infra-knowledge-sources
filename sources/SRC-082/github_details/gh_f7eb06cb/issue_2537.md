# [Issue #2537] Request for Demo Code to Successfully Quantize gpt-oss-20b

source: https://github.com/ModelCloud/GPTQModel/issues/2537
state: closed | updated: 2026-03-18T05:49:22Z
labels: 

## 正文

I noticed that the Model Support includes a GPT-OSS model. However, I keep getting errors when trying to quantize the gpt-oss-20b-bf16 model. Would it be possible to share a working demo code for successful quantization as a reference?

## 评论 (10)

### Qubitium · 2026-03-16


@ShiningMaker  You need to test the `main` branch with `oss` fix with latest transformers. 

Also inside `tests/models` fodler we have a sample/simple test script for each model supported. You can try a test using that template.

### ShiningMaker · 2026-03-17

> [@ShiningMaker](https://github.com/ShiningMaker) You need to test the `main` branch with `oss` fix with latest transformers.
> 
> Also inside `tests/models` fodler we have a sample/simple test script for each model supported. You can try a test using that template.

Thank you for your reply. The issue I encountered is that after quantization, I am unable to deploy the model with sglang. The initial error indicated a format mismatch (Half vs Bfloat16). After I forcibly converted everything to float16, the problem still persisted. sglang suggested that I use --disable-cuda-graph to disable the CUDA graph, but in this case, the service crashes during the first inference, with the error shown as follows:
```shell
[2026-03-16 20:12:01 TP0 EP0] max_total_num_tokens=4843298, chunked_prefill_size=8192, max_prefill_tokens=16384, max_running_requests=4096, context_len=131072, available_gpu_mem=25.48 GB
[2026-03-16 20:12:02] INFO:     Started server process [264965]
[2026-03-16 20:12:02] INFO:     Waiting for application startup.
[2026-03-16 20:12:02] Using default chat sampling params from model generation config: {'repetition_penalty': 1.0, 'temperature': 1.0, 'top_k': 50, 'top_p': 1.0}
[2026-03-16 20:12:02] INFO:     Application startup complete.
[2026-03-16 20:12:02] INFO:     Uvicorn running on http://0.0.0.0:5097/ (Press CTRL+C to quit)
[2026-03-16 20:12:03] INFO:     127.0.0.1:50884 - "GET /model_info HTTP/1.1" 200 OK
[2026-03-16 20:12:04 TP0 EP0] Scheduler hit an exception: Traceback (most recent call last):
  File "/nvme3/sglang/python/sglang/srt/managers/scheduler.py", line 3169, in run_scheduler_process
    scheduler.event_loop_overlap()
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/managers/scheduler.py", line 1165, in event_loop_overlap
    batch_result = self.run_batch(batch)
  File "/nvme3/sglang/python/sglang/srt/managers/scheduler.py", line 2328, in run_batch
    batch_result = self.model_worker.forward_batch_generation(
  File "/nvme3/sglang/python/sglang/srt/managers/tp_worker.py", line 456, in forward_batch_generation
    out = self.model_runner.forward(
  File "/nvme3/sglang/python/sglang/srt/model_executor/model_runner.py", line 2401, in forward
    output = self._forward_raw(
  File "/nvme3/sglang/python/sglang/srt/model_executor/model_runner.py", line 2500, in _forward_raw
    ret, can_run_graph = self.forward_extend(
  File "/nvme3/sglang/python/sglang/srt/model_executor/model_runner.py", line 2338, in forward_extend
    self.model.forward(
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/models/gpt_oss.py", line 640, in forward
    hidden_states = self.model(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/models/gpt_oss.py", line 571, in forward
    hidden_states, residual = layer(
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/models/gpt_oss.py", line 486, in forward
    hidden_states = self.mlp(hidden_states, forward_batch, should_allreduce_fusion)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/models/gpt_oss.py", line 171, in forward
    return self.forward_normal(hidden_states, should_allreduce_fusion)
  File "/nvme3/sglang/python/sglang/srt/models/gpt_oss.py", line 196, in forward_normal
    final_hidden_states = self.experts(hidden_states, topk_output)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/layers/moe/fused_moe_triton/layer.py", line 977, in forward
    return self.forward_impl(hidden_states, topk_output)
  File "/nvme3/sglang/python/sglang/srt/layers/moe/fused_moe_triton/layer.py", line 996, in forward_impl
    combine_input = self.run_moe_core(
  File "/nvme3/sglang/python/sglang/srt/layers/moe/fused_moe_triton/layer.py", line 1017, in run_moe_core
    return self.quant_method.apply(
  File "/nvme3/sglang/python/sglang/srt/layers/quantization/gptq.py", line 1258, in apply
    return self.runner.run(dispatch_output, quant_info)
  File "/nvme3/sglang/python/sglang/srt/layers/moe/moe_runner/runner.py", line 78, in run
    return self.fused_func(dispatch_output, quant_info, self.config)
  File "/nvme3/sglang/python/sglang/srt/layers/moe/moe_runner/marlin.py", line 100, in fused_experts_none_to_marlin
    output = fused_marlin_moe(
  File "/usr/local/lib/python3.10/dist-packages/torch/_ops.py", line 1255, in call
    return self._op(*args, **kwargs)
  File "/nvme3/sglang/python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py", line 179, in fused_marlin_moe
    intermediate_cache3 = torch.ops.sgl_kernel.moe_wna16_marlin_gemm.default(
  File "/usr/local/lib/python3.10/dist-packages/torch/_ops.py", line 841, in call
    return self._op(*args, **kwargs)
RuntimeError: Invalid thread config: thread_m_blocks = 1, thread_k = -1, thread_n = -1, num_threads = -1 for MKN = [24, 2880, 2880] and num_bits = 8, group_size = 64, has_act_order = 0, is_k_full = 1, has_zp = 0, is_zp_float = 0, max_shared_mem = 232448
[2026-03-16 20:12:04] SIGQUIT received. signum=None, frame=None. It usually means one child failed.
```

I am starting to suspect that there might be some incorrect parameter settings during my quantization process. Below is my quantization code.
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig
from gptqmodel import GPTQModel, QuantizeConfig, GPTAQConfig
from gptqmodel.quantization import FORMAT, METHOD
from gptqmodel.utils.torch import torch_empty_cache

def main(args):

    start_time = time.perf_counter()

    logging.basicConfig(
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
    )

    model_id = args.pretrained_model_dir

    config = AutoConfig.from_pretrained(args.pretrained_model_dir)
    tokenizer = AutoTokenizer.from_pretrained(args.pretrained_model_dir, trust_remote_code=True)

    calibration_dataset = []
    calibration_dataset = get_local_data(data_path = args.quant_data_dir, tokenizer = tokenizer, num_samples = args.num_samples, hidden_size=config.hidden_size)


    dynamic = None
    if config.model_type in ["qwen3_moe", "deepseek_v3"]:
        dynamic = {
            r"-:.*mlp.gate.*": {},
        }
    if config.model_type in ["gpt_oss"]:
        dynamic = {
            r"-:.*mlp.router.*": {},
        }

    quant_config = QuantizeConfig(
                            bits = 8, 
                            group_size = 64, 
                            quant_method= METHOD.GPTQ,
                            format= FORMAT.GPTQ,
                            desc_act =  False, 
                            dynamic = dynamic,
                            gptaq= None,
                        )

    model = GPTQModel.load(model_id, quant_config, device_map='auto', device = "cuda",
                           trust_remote_code=True)
    
    model.quantize(
                calibration_dataset, 
                # buffered_fwd = args.buffered_fwd, 
                calibration_concat_size = 8192, 
                calibration_data_min_length = 10, 
                batch_size = 1,
                backend = "triton"
                # auto_gc = args.auto_gc
            )

    torch_empty_cache()

    end_time = time.perf_counter()
    runtime = end_time - start_time

    seconds = int(runtime)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60

    print(f"quant time: {runtime:.6f} s", f"{h}h:{m}m:{s}s")

    model.save(args.quantized_model_dir)
```
Could you help me review my quantization code to see if there are any problems, so I can determine whether I should file an issue with the official sglang repository?

### Qubitium · 2026-03-17

@ShiningMaker 

This is a sglang issue as the kernel and infernence code is from there.  You need to report it there, you can @ me there as well. 

Before we move on to sglang, can you gptqmodel to use backend.marlin to run inference on the quantized model? If gptqmodel can run it without issue, then the issue is upstream in sglang which does moe fusing. You may  want to start from basics and `disable` any `tp`, multi-gpu, or fused modules to get it run first.

### ShiningMaker · 2026-03-17

> [@ShiningMaker](https://github.com/ShiningMaker)
> 
> This is a sglang issue as the kernel and infernence code is from there. You need to report it there, you can @ me there as well.
> 
> Before we move on to sglang, can you gptqmodel to use backend.marlin to run inference on the quantized model? If gptqmodel can run it without issue, then the issue is upstream in sglang which does moe fusing. You may want to start from basics and `disable` any `tp`, multi-gpu, or fused modules to get it run first.

Thank you for your suggestion. I followed the method you recommended in the README and ran it with the following code: 
```python
from gptqmodel import GPTQModel

model = GPTQModel.load("/nvme3/models/gpt-oss-20b-gptq-int8-gz64-16-0316")
result = model.generate("Uncovering deep insights begins with")[0] # tokens
print(model.tokenizer.decode(result)) # string output

model.serve(host="0.0.0.0",port="5098")
```
Using the same command that is used to call the sglang service, I was able to invoke it successfully, and it produced correct responses. This suggests that the quantization process completed successfully and that there are no issues with the quantized model itself. However, according to the logs, it defaults to using: Kernel: selected -> `TritonV2QuantLinear`.

### Qubitium · 2026-03-17

@ShiningMaker  Marlin kernel has shape (in/out features) requirements. Looks like Marlin is not auto-selected because it is not compatible. SGLang has less strict (dumb) check for kernel compatiblity than GPTQModel. lol

### ShiningMaker · 2026-03-17

@Qubitium That being said, the inference speed when calling the API in this way is extremely slow, and GPU utilization is very low. Using the same curl command, calling the API of the gpt-oss-20b-bf16 model deployed with sglang takes less than 30 seconds, whereas calling the API with the above code takes over two minutes (I did not wait the entire time — I switched to another page after one to two minutes without any result, and later returned to find that the output had finally appeared). Therefore, I still need to find a way to make this work with sglang.

### Qubitium · 2026-03-17

> [@Qubitium](https://github.com/Qubitium) That being said, the inference speed when calling the API in this way is extremely slow, and GPU utilization is very low. Using the same curl command, calling the API of the gpt-oss-20b-bf16 model deployed with sglang takes less than 30 seconds, whereas calling the API with the above code takes over two minutes (I did not wait the entire time — I switched to another page after one to two minutes without any result, and later returned to find that the output had finally appeared). Therefore, I still need to find a way to make this work with sglang.

You need to `pad` or expand the weights/parameters to be of a shape/size that `Marlin` kernel likes. You can do this dynamically by patching sglang using ai. Just feed it what I just told you. 


### ShiningMaker · 2026-03-17

> > [@Qubitium](https://github.com/Qubitium) That being said, the inference speed when calling the API in this way is extremely slow, and GPU utilization is very low. Using the same curl command, calling the API of the gpt-oss-20b-bf16 model deployed with sglang takes less than 30 seconds, whereas calling the API with the above code takes over two minutes (I did not wait the entire time — I switched to another page after one to two minutes without any result, and later returned to find that the output had finally appeared). Therefore, I still need to find a way to make this work with sglang.
> 
> You need to `pad` or expand the weights/parameters to be of a shape/size that `Marlin` kernel likes. You can do this dynamically by patching sglang using ai. Just feed it what I just told you.

Is the “pad” you mentioned the same as the padding described in this answer  https://github.com/QwenLM/Qwen3/issues/578#issuecomment-2175206751 ？

### Qubitium · 2026-03-17

> > > [@Qubitium](https://github.com/Qubitium) That being said, the inference speed when calling the API in this way is extremely slow, and GPU utilization is very low. Using the same curl command, calling the API of the gpt-oss-20b-bf16 model deployed with sglang takes less than 30 seconds, whereas calling the API with the above code takes over two minutes (I did not wait the entire time — I switched to another page after one to two minutes without any result, and later returned to find that the output had finally appeared). Therefore, I still need to find a way to make this work with sglang.
> > 
> > 
> > You need to `pad` or expand the weights/parameters to be of a shape/size that `Marlin` kernel likes. You can do this dynamically by patching sglang using ai. Just feed it what I just told you.
> 
> Is the “pad” you mentioned the same as the padding described in this answer ([https://github.com/QwenLM/Qwen3/issues/578#issuecomment-2175206751)？](https://github.com/QwenLM/Qwen3/issues/578#issuecomment-2175206751)%EF%BC%9F)

Paddings means:

1. extending the size of the model tensors with empty weight (all zeros). 
2. so that the total size fits some execution requirement of `most` `fast` kernels. Marlin is not the only kernel that has this requirement. 

TritonKernel in gptqmodel is dynamic so has very few if little `size` restrictions. 

### ShiningMaker · 2026-03-17

@Qubitium Understood. My current groupsize is set to 64 because the hidden size of the gpt-oss-20b model is 2880, which cannot be evenly divided by 128 but can be divided by 64. I should try padding it with zeros to 2944 so that it can be evenly divided by 128, right?
