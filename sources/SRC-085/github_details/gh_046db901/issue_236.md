# [Issue #236] size mismatch when load yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B model

source: https://github.com/SafeAILab/EAGLE/issues/236
state: closed | updated: 2025-06-10T03:46:46Z
labels: 

## 正文

i use terminal command

HF_ENDPOINT=https://hf-mirror.com python -m eagle.application.webui --ea-model-path yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B --base-model-path deepseek-ai/DeepSeek-R1-Distill-Llama-8B --total-token 3

LlamaForCausalLM has generative capabilities, as `prepare_inputs_for_generation` is explicitly defined. However, it doesn't directly inherit from `GenerationMixin`. From 👉v4.50👈 onwards, `PreTrainedModel` will NOT inherit from `GenerationMixin`, and this model will lose the ability to call `generate` and other related functions.
  - If you're using `trust_remote_code=True`, you can get rid of this warning by loading the model with an auto class. See https://huggingface.co/docs/transformers/en/model_doc/auto#auto-classes
  - If you are the owner of the model architecture code, please modify your model class such that it inherits from `GenerationMixin` (after `PreTrainedModel`, otherwise you'll get an exception).
  - If you are not the owner of the model architecture class, please contact the model code owner to update it.
Loading checkpoint shards: 100%|████████████████████████████████████████████████████| 2/2 [00:03<00:00,  1.93s/it]
LlamaForCausalLM has generative capabilities, as `prepare_inputs_for_generation` is explicitly defined. However, it doesn't directly inherit from `GenerationMixin`. From 👉v4.50👈 onwards, `PreTrainedModel` will NOT inherit from `GenerationMixin`, and this model will lose the ability to call `generate` and other related functions.
  - If you're using `trust_remote_code=True`, you can get rid of this warning by loading the model with an auto class. See https://huggingface.co/docs/transformers/en/model_doc/auto#auto-classes
  - If you are the owner of the model architecture code, please modify your model class such that it inherits from `GenerationMixin` (after `PreTrainedModel`, otherwise you'll get an exception).
  - If you are not the owner of the model architecture class, please contact the model code owner to update it.
LlamaForCausalLM has generative capabilities, as `prepare_inputs_for_generation` is explicitly defined. However, it doesn't directly inherit from `GenerationMixin`. From 👉v4.50👈 onwards, `PreTrainedModel` will NOT inherit from `GenerationMixin`, and this model will lose the ability to call `generate` and other related functions.
  - If you're using `trust_remote_code=True`, you can get rid of this warning by loading the model with an auto class. See https://huggingface.co/docs/transformers/en/model_doc/auto#auto-classes
  - If you are the owner of the model architecture code, please modify your model class such that it inherits from `GenerationMixin` (after `PreTrainedModel`, otherwise you'll get an exception).
  - If you are not the owner of the model architecture class, please contact the model code owner to update it.
Traceback (most recent call last):
  File "/home/diyuan.pb/miniconda3/envs/eagle3/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/diyuan.pb/miniconda3/envs/eagle3/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/diyuan.pb/eagle/application/webui.py", line 274, in <module>
    model = EaModel.from_pretrained(
  File "/home/diyuan.pb/eagle/model/ea_model.py", line 131, in from_pretrained
    model = cls(
  File "/home/diyuan.pb/eagle/model/ea_model.py", line 75, in __init__
    load_=self.ea_layer.load_state_dict(ea_layer_state_dict, strict=False)
  File "/home/diyuan.pb/miniconda3/envs/eagle3/lib/python3.9/site-packages/torch/nn/modules/module.py", line 2581, in load_state_dict
    raise RuntimeError(
RuntimeError: Error(s) in loading state_dict for Model:
        size mismatch for fc.weight: copying a param with shape torch.Size([4096, 12288]) from checkpoint, the shape in current model is torch.Size([4096, 8192]).

## 评论 (1)

### thuBingo · 2025-06-10

use code to inference succesfully

from eagle.model.ea_model import EaModel
from fastchat.model import get_conversation_template
import torch

model = EaModel.from_pretrained(
    base_model_path='deepseek-ai/DeepSeek-R1-Distill-Llama-8B',
    ea_model_path='yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B',
    # base_model_path='Qwen/Qwen2-7B-Instruct',
    # ea_model_path= 'yuhuili/EAGLE-Qwen2-7B-Instruct',
    torch_dtype=torch.float16,  
    low_cpu_mem_usage=True,
    device_map="auto",
    total_token=-1,
    # use_eagle3=False
)
model.eval()
your_message="tell me a story"
conv = get_conversation_template("llama3")
conv.append_message(conv.roles[0], your_message)
conv.append_message(conv.roles[1], None)
prompt = conv.get_prompt()
print(prompt)
print('-------------------------')
input_ids=model.tokenizer([prompt]).input_ids
input_ids = torch.as_tensor(input_ids).cuda()
output_ids=model.eagenerate(input_ids,temperature=0.5,max_new_tokens=512)
output=model.tokenizer.decode(output_ids[0])
print(output)
