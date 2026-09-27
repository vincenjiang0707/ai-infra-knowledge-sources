# [Issue #165] Issues Integrating HQQ Quantization with lmms-eval and vLLM Backend (vllm version 0.11.0)

source: https://github.com/dropbox/hqq/issues/165
state: closed | updated: 2025-10-26T08:02:52Z
labels: 

## 正文

Hello, HQQ team

I am currently trying to analyze the impact of quantization (specifically using your HQQ and GEMLITE implementation) on VLM models. (Llava, Gemma, Qwen2.5, etc) To do this, I am running benchmarks using the lmms-eval harness with the vllm backend.

However, I have encountered a couple of technical issues and was hoping you might be able to provide some guidance:

**1. set_vllm_hqq_backend and set_vllm_onthefly_quant are not taking effect. I declared both of these parameters before the lmms_eval framework invokes its vllm.py script, but they do not seem to be working. The benchmark results suggest that the quantization is not being applied.**

Modified
[lmms_eval/models/simple/vllm.py line 25
](https://github.com/EvolvingLMMs-Lab/lmms-eval/blob/94af1e0834a40acdf4362a2a0ec20f8436d66b2c/lmms_eval/models/simple/vllm.py#L26) 
```
try:
    skip_modules = "['lm_head', 'vision', 'visual']"
    weight_bits=4
    quant_mode="mxfp4_dynamic"
    from hqq.utils.vllm import set_vllm_hqq_backend, VLLM_HQQ_BACKEND, set_vllm_onthefly_hqq_quant
    set_vllm_hqq_backend(backend=VLLM_HQQ_BACKEND.GEMLITE)

    skip_modules = {skip_modules}

    set_vllm_onthefly_hqq_quant(weight_bits={weight_bits},quant_mode={quant_mode}, skip_modules=skip_modules)
    print(f"set vllm onthefly hqq quant: weight_bits={weight_bits}, quant_mode={quant_mode}")
    
    from vllm import LLM, SamplingParams
except ImportError:
    vllm = None

```

And my run script code 
```
python3 -m lmms_eval \
    --model vllm \
    --model_args model=google/gemma-3-4b-it \
    --batch_size 64 \
    --log_samples \
    --log_samples_suffix vllm \
    --output_path ./logs/W${weight_bits}_Q${quant_mode} \
    --limit 256 \
    --tasks mme
```
Important library version
```
lmms_eval = 0.4.0
vllm = 0.11.0
hqq = 0.2.8
gemlite = 0.5.1
torch = 2.8.0
ubuntu 24.04
NVIDIA blackwell RTX6000 (It can run gemlite's MX format)
```

Uncertainty regarding vllm initialization (v0.11.0+). I noticed that since vllm version 0.11.0, the multiprocessing module has been integrated, which makes it unclear where the vllm instance or its quantization settings should now be declared. I did attempt to test this with vllm 0.10.0 using a previous solution, but the benchmark results remained unchanged, which seems to confirm the issue in point #163 and #152 .


I would greatly appreciate any advice or potential solutions you could offer to resolve these issues.

Thank you for your time and assistance.

## 评论 (4)

### mobicham · 2025-10-18

Hey, thanks for opening this. 
The issue is that vLLM engine uses spawn multiprocessing, so the patching does't take effect. It will only take effect if you run the patching tfirst hen in` __main__` you start a vLLM instance via `LLM()`. Here are a couple of solutions:
* Use torchao to first quantize the model and save it, you can load it in vLLM. You can follow this example: https://huggingface.co/jerryzh168/phi4-mini-int4wo-gemlite but the results will be slightly different than using  the hqq lib.
* Do the patching in vLLM `engine.py`, but requires building vLLM via `pip install -e .`
* Use `lm_eval` instead not via the command line but via a model instance that passes the HF transformers model
* Wait for a PR, will try to squeeze some time to do it the next days.

The first option is the easiest imo.

Btw, there's no hqq in mxfp4 and you should not evaluate mxfp4/nvfp4 because the quality is not good out-of-the-box. HQQ is only used for A16W4, the rest uses basic quantization in gemlite.

Hope this helps!

### pdh930105 · 2025-10-18

thanks to response!

I will test your solution and stay your PR!

Good luck!

### mobicham · 2025-10-24

Hey @pdh930105, any update or something I can help with?

### pdh930105 · 2025-10-26

Oh i'm sorry. I was tested your solution 1, but i can't sucesss. (Maybe I think I'm still not good at torch.ao)

Therefore, I will be waiting for your update.


Best regard!
