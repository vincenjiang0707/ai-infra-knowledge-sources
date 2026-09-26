# [Issue #238] inference time increase after use eagle model

source: https://github.com/SafeAILab/EAGLE/issues/238
state: closed | updated: 2025-06-10T09:01:00Z
labels: 

## 正文

generate 512 token，
inf time 19.605095624923706
original model inf time 14.811357259750366
code 

# step1 deepseek-ai/DeepSeek-R1-Distill-Llama-8B inference with eagle3 model
from eagle.model.ea_model import EaModel
from fastchat.model import get_conversation_template
import torch
import time

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
model = model.to("cuda")
model.eval()
your_message="tell me a story"
conv = get_conversation_template("llama3")
conv.append_message(conv.roles[0], your_message)
conv.append_message(conv.roles[1], None)
prompt = conv.get_prompt()
print(prompt)
print('-------------------------')
start_time = time.time()
input_ids=model.tokenizer([prompt]).input_ids
input_ids = torch.as_tensor(input_ids).cuda()
output_ids=model.eagenerate(input_ids,temperature=0.5,max_new_tokens=512)
output=model.tokenizer.decode(output_ids[0])
end_time = time.time()
print('inf time', end_time - start_time)
print('-------------------------')
print(output)


# step2 deepseek-ai/DeepSeek-R1-Distill-Llama-8B original model inference
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

model_name = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)

model = model.to("cuda")

start_time = time.time()
input_ids = tokenizer([prompt]).input_ids
input_ids = torch.as_tensor(input_ids).cuda()
output_ids = model.generate(input_ids, temperature=0.5, max_new_tokens=512)
output = tokenizer.decode(output_ids[0])
end_time = time.time()
print('original model inf time', end_time - start_time)
print('-------------------------')
print(output)


## 评论 (1)

### thuBingo · 2025-06-10

succes with flowing commend
CUDA_VISIBLE_DEVICES=1 HF_ENDPOINT=https://hf-mirror.com python -m eagle.evaluation.gen_ea_answer_ds --ea-model-path yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B --base-model-path deepseek-ai/DeepSeek-R1-Distill-Llama-8B
