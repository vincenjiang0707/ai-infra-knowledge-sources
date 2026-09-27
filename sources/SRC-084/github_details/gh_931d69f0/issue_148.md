# [Issue #148] hqq quantization for MoE

source: https://github.com/dropbox/hqq/issues/148
state: closed | updated: 2025-02-20T08:29:29Z
labels: 

## 正文

Everything goes well when I use HQQ to quantize Llama model and use vLLM to do the serving. However, when I use HQQ to compress Mixtral8x7B model and do serving, I got assertion error: ” File “/u/zshao3/vllm/vllm/model_executor/layers/linear.py”, line 238, in weight_loader assert param.size() == loaded_weight.size()“. I asked vLLM's team and they said maybe my model compression is wrong. So I want to know how can I correctly compress the MoE model using HQQ. My quantization script is here:

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig
model_id      = "mistralai/Mixtral-8x7B-v0.1" 
model_path = "/scratch/bcjw/zshao3/huggingface/models--mistralai--Mixtral-8x7B-v0.1"
quant_model = "/scratch/bcjw/zshao3/huggingface/models--mistralai--Mixtral-8x7B-v0.1-w4-gs64"

quant_config = HqqConfig(nbits=4, group_size=64, axis=1)

model = AutoModelForCausalLM.from_pretrained(model_path,
                                            torch_dtype=torch.float16,
                                            cache_dir="/scratch/bcjw/zshao3/huggingface/",
                                            device_map="cuda:0",
                                            quantization_config=quant_config,
                                            low_cpu_mem_usage=True)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

model.save_pretrained(quant_model)
tokenizer.save_pretrained(quant_model)


## 评论 (15)

### mobicham · 2025-02-09

Hey @ZeleiShao , everything seems correct (you don't need trust_remote_code though), I will take a look at it on Monday or Tuesday and get back to you. 

### ZeleiShao · 2025-02-09

Thank you really really much, and wish you a happy weekend~~~~

### mobicham · 2025-02-10

So I looked into it, and I fixed a bug related to model saving + disable quantization for the gate layer, so this one works fine with transformers: https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf

However, it still doesn't load with VLLM. It looks like they didn't implement the quant loader for `ReplicatedLinear` which is used in Mixtral.
Have you already created a vllm github issue? If so can you please share the link so I can comment on it.

### mobicham · 2025-02-10

Here's a temporary hack that works, you'd need enough VRAM though:

```Python
##################################################################
import torch
import torch.nn as nn
from typing import Optional
from vllm.model_executor.layers.linear import RowParallelLinear
from vllm.model_executor.layers.quantization.base_config import QuantizationConfig
class MixtralMLPRowParallel(nn.Module):

    def __init__(
        self,
        num_experts: int,
        hidden_size: int,
        intermediate_size: int,
        quant_config: Optional[QuantizationConfig] = None,
    ) -> None:
        super().__init__()
        self.num_experts = num_experts
        self.ffn_dim = intermediate_size
        self.hidden_dim = hidden_size

        self.w1 = RowParallelLinear(self.hidden_dim,
                                   self.ffn_dim,
                                   bias=False,
                                   quant_config=quant_config)
        self.w2 = RowParallelLinear(self.ffn_dim,
                                   self.hidden_dim,
                                   bias=False,
                                   quant_config=quant_config)
        self.w3 = RowParallelLinear(self.hidden_dim,
                                   self.ffn_dim,
                                   bias=False,
                                   quant_config=quant_config)

        # TODO: Use vllm's SiluAndMul
        self.act_fn = nn.SiLU()

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        w1_out, _ = self.w1(hidden_states)
        w1_out = self.act_fn(w1_out)
        w3_out, _ = self.w3(hidden_states)
        current_hidden_states = w1_out * w3_out
        current_hidden_states, _ = self.w2(current_hidden_states)
        return current_hidden_states

import vllm.model_executor.models.mixtral_quant as mixtral_quant
mixtral_quant.MixtralMLP = MixtralMLPRowParallel
##################################################################

from vllm import LLM
from vllm.sampling_params import SamplingParams
model_id = "mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf"

llm = LLM(model=model_id, gpu_memory_utilization=0.80)
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=1024)
outputs = llm.generate(["What is the capital of Germany?"], sampling_params)
print(outputs[0].outputs[0].text)
```

### ZeleiShao · 2025-02-10

> So I looked into it, and I fixed a bug related to model saving + disable quantization for the gate layer, so this one works fine with transformers: https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf
> 
> However, it still doesn't load with VLLM. It looks like they didn't implement the quant loader for `ReplicatedLinear` which is used in Mixtral. Have you already created a vllm github issue? If so can you please share the link so I can comment on it.

I created an issue, but one deal with it. Maybe because the error wasn't clear enough? Then I asked the question in vLLM's slack and @one of the authors of hqq_marlin.py and he answered it quickly. So now I think that it's better we ask some of the authors of the mixtral_quant.py and model_executor.layers.linear in slack or create a new issue......Or do you want to comment in my chat in vLLM's slack?

### ZeleiShao · 2025-02-10

> Here's a temporary hack that works, you'd need enough VRAM though:
> 
> ##################################################################
> import torch
> import torch.nn as nn
> from typing import Optional
> from vllm.model_executor.layers.linear import RowParallelLinear
> from vllm.model_executor.layers.quantization.base_config import QuantizationConfig
> class MixtralMLPRowParallel(nn.Module):
> 
>     def __init__(
>         self,
>         num_experts: int,
>         hidden_size: int,
>         intermediate_size: int,
>         quant_config: Optional[QuantizationConfig] = None,
>     ) -> None:
>         super().__init__()
>         self.num_experts = num_experts
>         self.ffn_dim = intermediate_size
>         self.hidden_dim = hidden_size
> 
>         self.w1 = RowParallelLinear(self.hidden_dim,
>                                    self.ffn_dim,
>                                    bias=False,
>                                    quant_config=quant_config)
>         self.w2 = RowParallelLinear(self.ffn_dim,
>                                    self.hidden_dim,
>                                    bias=False,
>                                    quant_config=quant_config)
>         self.w3 = RowParallelLinear(self.hidden_dim,
>                                    self.ffn_dim,
>                                    bias=False,
>                                    quant_config=quant_config)
> 
>         # TODO: Use vllm's SiluAndMul
>         self.act_fn = nn.SiLU()
> 
>     def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
>         w1_out, _ = self.w1(hidden_states)
>         w1_out = self.act_fn(w1_out)
>         w3_out, _ = self.w3(hidden_states)
>         current_hidden_states = w1_out * w3_out
>         current_hidden_states, _ = self.w2(current_hidden_states)
>         return current_hidden_states
> 
> import vllm.model_executor.models.mixtral_quant as mixtral_quant
> mixtral_quant.MixtralMLP = MixtralMLPRowParallel
> ##################################################################
> 
> from vllm import LLM
> from vllm.sampling_params import SamplingParams
> model_id = "mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf"
> 
> llm = LLM(model=model_id, gpu_memory_utilization=0.80)
> sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=1024)
> outputs = llm.generate(["What is the capital of Germany?"], sampling_params)
> print(outputs[0].outputs[0].text)

Thank you very much! I will try this!

### mobicham · 2025-02-10

I have already talked to them actually via Slack, it's a problem with `ReplicatedLinear`, the hack above that I put up should work.

### mobicham · 2025-02-11

By the way, I added this in the master branch, you can simply use it like this: 
```Python
from hqq.utils.vllm import patch_mixtral
patch_mixtral()

model_id = "mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf"
llm = LLM(model=model_id, gpu_memory_utilization=0.80) 
...
```

### ZeleiShao · 2025-02-12

I just try your code and it shows that the config.json is not a valid JSON file. Besides, I wonder do they have a plan for adding a quant loader for ReplicatedLinear?

### mobicham · 2025-02-13

Strange, have you tried with the master branch of vllm? I tried on 2 instances and it was working fine as of Tuesday

### ZeleiShao · 2025-02-13

I need to do some kernel work, so I download the whole vllm repo and test the code you provide... Then maybe I should check the calling stack and check whether I have wrongly changed some files in vllm.

Besides, I have one thing to confirm, I gitclone your model and check the config.json, it shows,"  version https://git-lfs.github.com/spec/v1
   oid sha256:cfb08824b884670cacbca3e7384dbe53b70a179898c1eaa55131b3a8406c77df
  size 1269". I checked that it's the same as yours... Would this be the reason?

### mobicham · 2025-02-13

if you do `cat config.json`, it should show <a href="https://shorturl.at/XQr4q">this</a>. Normally vllm will throw that error if there's a problem with the json format, but as you can see in the link, it looks fine.



### ZeleiShao · 2025-02-13

Thank you! I correctly download the model now.

### ZeleiShao · 2025-02-19

Sorry, I have another question, can I get your python script to quantize the mixtral model and get [Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf](https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1_4bitgs64_hqq_hf)? I quantize a model on my own and it doesn't work.... 

### mobicham · 2025-02-20

I used hqq's lib call to save the model, hf's `save_pretrained` is kinda broken sometimes:
```Python
from hqq.models.hf.base import AutoHQQHFModel
AutoHQQHFModel.save_to_safetensors(quantized_model, target_dir)
```
