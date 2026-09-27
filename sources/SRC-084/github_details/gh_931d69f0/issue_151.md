# [Issue #151] Error when trying to load PEFT model after v0.2.3 release

source: https://github.com/dropbox/hqq/issues/151
state: closed | updated: 2025-02-20T11:12:55Z
labels: 

## 正文

Since the v0.2.3 release, a PEFT unit test involving HQQ is failing. I could boil down the reproducer to this:

```python
import tempfile
from transformers import AutoModelForCausalLM, HqqConfig
from peft import get_peft_model, LoraConfig, PeftModel

model_id = "facebook/opt-125m"  # other models also fail
config = LoraConfig(
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM",
    init_lora_weights=False,
)
quant_config = HqqConfig(nbits=4, group_size=64)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quant_config,
)
model = get_peft_model(model, config)

with tempfile.TemporaryDirectory() as tmp_dir:
    model.save_pretrained(tmp_dir)
    del model

    quant_config = HqqConfig(nbits=4, group_size=64)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=quant_config,
    )
    model = PeftModel.from_pretrained(model, tmp_dir)
```

The error is:

```
Traceback (most recent call last):
  File "/home/name/work/forks/peft/foo.py", line 29, in <module>
    model = PeftModel.from_pretrained(model, tmp_dir)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/peft/src/peft/peft_model.py", line 538, in from_pretrained
    load_result = model.load_adapter(
                  ^^^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/peft/src/peft/peft_model.py", line 1220, in load_adapter
    load_result = set_peft_model_state_dict(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/work/forks/peft/src/peft/utils/save_and_load.py", line 432, in set_peft_model_state_dict
    load_result = model.load_state_dict(peft_model_state_dict, strict=False)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/anaconda3/envs/peft/lib/python3.11/site-packages/torch/nn/modules/module.py", line 2561, in load_state_dict
    load(self, state_dict)
  File "/home/name/anaconda3/envs/peft/lib/python3.11/site-packages/torch/nn/modules/module.py", line 2549, in load
    load(child, child_state_dict, child_prefix)  # noqa: F821
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/anaconda3/envs/peft/lib/python3.11/site-packages/torch/nn/modules/module.py", line 2549, in load
    load(child, child_state_dict, child_prefix)  # noqa: F821
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/name/anaconda3/envs/peft/lib/python3.11/site-packages/torch/nn/modules/module.py", line 2549, in load
    load(child, child_state_dict, child_prefix)  # noqa: F821
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  [Previous line repeated 5 more times]
  File "/home/name/anaconda3/envs/peft/lib/python3.11/site-packages/torch/nn/modules/module.py", line 2532, in load
    module._load_from_state_dict(
  File "/home/name/anaconda3/envs/peft/lib/python3.11/site-packages/hqq/core/quantize.py", line 685, in _load_from_state_dict
    layer_state_dict['W_q'] = nn.Parameter(layer_state_dict['W_q'], requires_grad=False)
                                           ~~~~~~~~~~~~~~~~^^^^^^^
KeyError: 'W_q'
```

The commit that caused this is most likely this one: https://github.com/mobiusml/hqq/commit/73cb373f4df7efd698c13471ca17d2b867636b2a.

I jumped into the debugger for a bit more context:

```
666  	    def _load_from_state_dict(
667  	        self,
668  	        state_dict,
669  	        prefix,
670  	        local_metadata,
671  	        strict,
672  	        missing_keys,
673  	        unexpected_keys,
674  	        error_msgs,
675  	    ):
676  	
677  	        layer_state_dict = {}
678  	        for key in self.state_dict_keys():
679  	            if(prefix + key in state_dict):
680  	                layer_state_dict[key] = state_dict.pop(prefix + key)
681  	            else:
682  	                if(key not in ['bias']):
683  	                    missing_keys.append(prefix + key)
684  	
685  ->	        layer_state_dict['W_q'] = nn.Parameter(layer_state_dict['W_q'], requires_grad=False)
686  	
687  	        self.load_state_dict(layer_state_dict, strict=strict)
(Pdb) state_dict
{}
(Pdb) self.state_dict_keys()
{'scale', 'quant_scale', 'W_q', 'offload_meta', 'encoded_state_dict', 'view_as_float', 'compute_dtype', 'stores_quant_config', 'group_size', 'channel_wise', 'round_zero', 'unpack_view_dtype', 'quant_zero', 'zero', 'optimize', 'packing', 'bias', 'nbits', 'axis', 'shape'}
(Pdb) prefix
'base_model.model.model.decoder.layers.0.self_attn.k_proj.'
(Pdb) strict
True
```

Note that the `base_model.model.` part of the `prefix` stems from PEFT wrapping the original model. I don't really have enough knowledge about HQQ to debug further from here.

## 评论 (4)

### mobicham · 2025-02-19

Hey,  thanks for reporting. Strange, because `W_q` is actually in the state dict. 

Also this works fine, but the output is not the same with peft, **but the output is the same without:** 

```Python
#import tempfile

import torch, os
from transformers import AutoModelForCausalLM, HqqConfig
from peft import get_peft_model, LoraConfig, PeftModel

device = 'cuda:0'
enable_peft = True

torch.manual_seed(0)
x = torch.randint(0, 100, (1, 100), device=device) 


model_id = "facebook/opt-125m"  # other models also fail

model = AutoModelForCausalLM.from_pretrained(model_id,
                                            torch_dtype=torch.bfloat16,
                                            device_map=device,
                                            quantization_config=HqqConfig(nbits=4, group_size=64),
                                            ).eval()


if(enable_peft):
    config = LoraConfig(
        target_modules=["q_proj", "v_proj"],
        task_type="CAUSAL_LM",
        init_lora_weights=False,
    )

    model = get_peft_model(model, config)


# layers = model.model.model.decoder.layers
# for i in range(len(layers)):
# 	assert 'W_q' in layers[i].self_attn.q_proj.base_layer.state_dict()
# 	assert 'W_q' in layers[i].self_attn.k_proj.state_dict()
# 	assert 'W_q' in layers[i].self_attn.v_proj.base_layer.state_dict()
# 	assert 'W_q' in layers[i].self_attn.out_proj.state_dict()
# 	assert 'W_q' in layers[i].fc1.state_dict()
# 	assert 'W_q' in layers[i].fc2.state_dict()

with torch.no_grad():
	out = model(x).logits



quant_path = 'quant_model'
os.system('rm -R ' + quant_path)
model.save_pretrained(quant_path)

############################################################################################################
#from hqq.models.hf.base import AutoHQQHFModel
#AutoHQQHFModel.save_to_safetensors(model, quant_path, num_blocks_per_file=10000)

model_loaded = AutoModelForCausalLM.from_pretrained(quant_path,
                                            torch_dtype=torch.bfloat16,
                                            device_map=device,
                                            ).eval()


if(enable_peft):
    model_loaded = PeftModel.from_pretrained(model_loaded, quant_path).eval()

with torch.no_grad():
	out_loaded = model_loaded(x).logits

print((out_loaded - out).abs().mean()) #0.3691
```

### mobicham · 2025-02-19

It turns out, peft loading is not working properly, it doesn't seem to load HQQLinear layers when there's no peft applied:

```Python
In [16]: model.model.model.decoder.layers[i].self_attn.k_proj
Out[16]: HQQLinear(in_features=768, out_features=768, bias=True)

In [17]: model_loaded.model.model.decoder.layers[i].self_attn.k_proj
Out[17]: Linear(in_features=768, out_features=768, bias=True)
```

I don't really know what's going since I didn't implement this. Do you what could be the issue?

### mobicham · 2025-02-19

It seems that the issue is caused by the adapter files located in the same folder, which is strange. 
If I manually save the adapter in another folder and manually load the weights, it works fine. So I guess it's a problem with transofrmers or peft:

```Python
import torch, os
from transformers import AutoModelForCausalLM, HqqConfig
from peft import get_peft_model, LoraConfig, PeftModel, PeftConfig

######################################################################################################
def load_adapter(model_loaded, adapter_dir):
	from safetensors import safe_open

	#Load config
	model_loaded = get_peft_model(model_loaded, PeftConfig.from_pretrained(adapter_dir))

	#Load weights 
	tensors = {}
	with safe_open(adapter_dir + "/adapter_model.safetensors", framework="pt", device=model_loaded.device.type) as f:
		for key in f.keys():
			base, param = '.'.join(key.split('.')[:-1]) + '.default', key.split('.')[-1]
			if(base not in tensors):
				tensors[base] = {}
			tensors[base][param] = torch.nn.Parameter(f.get_tensor(key))

	#Full module name
	for name, module in model_loaded.named_modules():
		module.name = name

	#Assign weights
	def _patch(model_loaded):
		for name, layer in model_loaded.named_children():
			if(layer.name in tensors):
				for p,v in tensors[layer.name].items():
					setattr(layer, p, v)
			_patch(layer)

	_patch(model_loaded)

######################################################################################################
device = 'cuda:0'
enable_peft = True

torch.manual_seed(0)
x = torch.randint(0, 100, (1, 100), device=device) 

quant_path = 'quant_model'
os.system('rm -R ' + quant_path)


model_id = "facebook/opt-125m" 

model = AutoModelForCausalLM.from_pretrained(model_id,
                                            torch_dtype=torch.bfloat16,
                                            device_map=device,
                                            quantization_config=HqqConfig(nbits=4, group_size=64),
                                            )

#Save base model
model.save_pretrained(quant_path)

if(enable_peft):
    config = LoraConfig(target_modules=["q_proj", "v_proj"], task_type="CAUSAL_LM", lora_dropout=0.)

    model = get_peft_model(model, config)

    #Save adapter
    model.save_pretrained('adapter')


model = model.eval()
with torch.no_grad():
	out = model(x).logits

############################################################################################################

model_loaded = AutoModelForCausalLM.from_pretrained(quant_path, torch_dtype=torch.bfloat16, device_map=device)

if(enable_peft):
	load_adapter(model_loaded, 'adapter')

model_loaded = model_loaded.eval()
with torch.no_grad():
	out_loaded = model_loaded(x).logits

print((out_loaded - out).abs().mean()) 
#tensor(0., device='cuda:0', dtype=torch.bfloat16)
```

### mobicham · 2025-02-20

Resolved https://github.com/mobiusml/hqq/releases/tag/0.2.3.post1
