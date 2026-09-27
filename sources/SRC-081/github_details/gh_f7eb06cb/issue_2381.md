# [Issue #2381] [BUG] AttributeError: 'NoneType' object has no attribute 'make_q_matrix'

source: https://github.com/ModelCloud/GPTQModel/issues/2381
state: closed | updated: 2026-01-29T08:45:31Z
labels: bug

## 正文

**Describe the bug**

AttributeError: 'NoneType' object has no attribute 'make_q_matrix'
This error appears in version 5.6.2 and later versions, while everything works fine in versions prior to 5.6.0.

**GPU Info**
NVIDIA A100
NVIDIA-SMI 550.163.01             
Driver Version: 550.163.01     
CUDA Version: 12.4 

**Software Info**

Ubuntu + python 3.10 + pytorch 2.9.1

**To Reproduce**

Install gptqmodel from the GitHub releases page.
v5.6.2 https://github.com/ModelCloud/GPTQModel/releases/download/v5.6.2/gptqmodel-5.6.2+cu126torch2.9-cp310-cp310-linux_x86_64.whl
v5.6.0 https://github.com/ModelCloud/GPTQModel/releases/download/v5.6.0/gptqmodel-5.6.0+cu126torch2.9-cp310-cp310-linux_x86_64.whl

**Additional context**

```
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py:604: in from_pretrained
    return model_class.from_pretrained(
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/transformers/modeling_utils.py:277: in _wrapper
    return func(*args, **kwargs)
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/transformers/modeling_utils.py:5144: in from_pretrained
    hf_quantizer.postprocess_model(model, config=config)
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/transformers/quantizers/base.py:238: in postprocess_model
    return self._process_model_after_weight_loading(model, **kwargs)
../auto_round/inference/auto_quantizer.py:360: in _process_model_after_weight_loading
    self.post_init_model(model)
../auto_round/inference/auto_quantizer.py:350: in post_init_model
    post_init(model, self.used_backends)
../auto_round/inference/convert_model.py:508: in post_init
    model = gptq_post_init(model, use_act_order=False)
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/gptqmodel/utils/model.py:957: in hf_gptqmodel_post_init
    return gptqmodel_post_init(model, use_act_order, quantize_config, max_input_length)
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/gptqmodel/utils/model.py:1084: in gptqmodel_post_init
    submodule.post_init(scratch_space=model.device_tensors[device])
/home/uttest/miniforge3/envs/unittest_cuda/lib/python3.10/site-packages/gptqmodel/nn_modules/qlinear/exllamav2.py:136: in post_init
    self.q_handle = self.ext_make_q_matrix(self.q_tensors, temp_dq)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ExllamaV2QuantLinear()
w = {'g_idx': tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,...8388563,  2000095033,  ..., -1738516155,
         -1674495164, -1852467156]], device='cuda:0', dtype=torch.int32), ...}
temp_dq = tensor([nan, nan, nan,  ..., nan, nan, nan], device='cuda:0',
       dtype=torch.float16)
key = None

    def ext_make_q_matrix(self, w: dict, temp_dq, key: str = None):
        """
        Create Q matrix
        """
        # EXL2
        # won't work as the moment because the tensors are not the same.
        if "q_weight" in w:
            w["q_scale_max"] /= 256
            w["q_perm"] = w["q_perm"].short()
            w["q_invperm"] = w["q_invperm"].short()
            return self.gptqmodel_exllamav2_kernels.make_q_matrix(
                w["q_weight"],
                w["q_perm"],
                w["q_invperm"],
                w["q_scale"],
                w["q_scale_max"],
                w["q_groups"],
                NONE_TENSOR,
                NONE_TENSOR,
                NONE_TENSOR,
                temp_dq,
            )
        # GPTQ
        elif "qweight" in w:
            if w["scales"].dtype == torch.float:
                w["scales"] = w["scales"].half()
    
            # GPTQ with g_idx (act_order)
            if "g_idx" in w and not (w["g_idx"] == 0).all().item():
                w["q_perm"] = torch.empty(
                    (w["qweight"].shape[0] * 8,),
                    dtype=torch.short,
                    device=w["qweight"].device,
                )
                w["q_invperm"] = torch.empty_like(w["q_perm"])
                # make_q4 segfaults if g_idx is not on cpu in the act-order case. In the non act-order case, None needs to be passed for g_idx.
>               return self.gptqmodel_exllamav2_kernels.make_q_matrix(
                    w["qweight"],
                    w["q_perm"],
                    w["q_invperm"],
                    NONE_TENSOR,
                    NONE_TENSOR,
                    NONE_TENSOR,
                    w["qzeros"],
                    w["scales"],
                    w["g_idx"].cpu(),
                    temp_dq,
                )
E               AttributeError: 'NoneType' object has no attribute 'make_q_matrix'
```


## 评论 (3)

### Qubitium · 2026-01-26

@XuehaoSun Do you have a reproducing script? and/or also with latest main branch?

### XuehaoSun · 2026-01-27

> [@XuehaoSun](https://github.com/XuehaoSun) Do you have a reproducing script? and/or also with latest main branch?

I tried the latest commit(3d55cec116bdf63ef4d773dfea1f6a4798a551c1), same error.

```bash
pip install auto-round torch==2.9.1 transformers==4.57.6
```
```python
import torch
from auto_round import AutoRound
from transformers import AutoModelForCausalLM, AutoRoundConfig, AutoTokenizer

model_name = "facebook/opt-125m"
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
bits, group_size, sym = 4, 128, False
autoround = AutoRound(
    model,
    tokenizer,
    bits=bits,
    group_size=group_size,
    sym=sym,
    iters=0,
    seqlen=2,
)
quantized_model_path = "test"
autoround.quantize_and_save(output_dir=quantized_model_path, format="auto_round:gptqmodel")

quantization_config = AutoRoundConfig(backend="gptqmodel:exllamav2")
model = AutoModelForCausalLM.from_pretrained(
    quantized_model_path, torch_dtype=torch.float16, device_map="auto", quantization_config=quantization_config
)
tokenizer = AutoTokenizer.from_pretrained(quantized_model_path)
```

### Qubitium · 2026-01-27

@ZX-ModelCloud  @XuehaoSun This appears to not be a bug in our package but `autoround` calling us and crashing. Is AutoRound calling some deprecated exllama v2 `post_init`?
