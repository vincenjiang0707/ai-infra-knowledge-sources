# [Issue #1611] Why is the gpu memory still occupied after deleting the model and calling torch.cuda.empty_cache() when using 4-bit quantization?

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1611
state: closed | updated: 2026-02-16T11:47:27Z
labels: 

## 正文

### System Info

os: linux
gpu: a100

### Reproduction



```
import gc
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, TextIteratorStreamer
import torch
from threading import Thread

# 模型名称
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

def stream_generate(prompt, max_new_tokens=512):
    # 构建对话消息
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    
    # 应用聊天模板
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    
    # 准备模型输入
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    
    # 创建流式生成器
    streamer = TextIteratorStreamer(tokenizer, skip_special_tokens=True)
    
    # 在后台线程中运行生成
    generation_kwargs = dict(
        **model_inputs,
        max_new_tokens=max_new_tokens,
        streamer=streamer,
    )
    
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()
    
    # 流式输出生成的文本
    print("Generated text: ", end="", flush=True)
    for text in streamer:
        print(text, end="", flush=True)
    print("\n")
    
    thread.join()

def init_model(model_name):
    from transformers import BitsAndBytesConfig
    tokenizer = AutoTokenizer.from_pretrained(model_name)
        
    model = AutoModelForCausalLM.from_pretrained(
        model_name, device_map='cuda:0', attn_implementation='flash_attention_2',
        torch_dtype=torch.bfloat16,
        quantization_config=BitsAndBytesConfig(
            load_in_4bit=True,
            # llm_int8_threshold=5.0,
            llm_int8_skip_modules=["lm_head"],
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True
        )
    )
    return model, tokenizer

if __name__ == "__main__":
    # 加载模型和分词器
    model, tokenizer = init_model(MODEL_NAME)
    # 测试流式生成
    prompt = "请用中文介绍一下大语言模型。"
    stream_generate(prompt)
    del model
    del tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    
    
    model, tokenizer = init_model("prithivMLmods/Qwen-UMLS-7B-Instruct")
    # 测试多轮对话
    prompt = "请详细解释一下Transformer架构。"
    stream_generate(prompt) 
    del model
    del tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    
    
    model, tokenizer = init_model("Qwen/Qwen2.5-7B-Instruct")
    prompt = "请详细解释一下你是谁。"
    stream_generate(prompt) 
    del model
    del tokenizer
    gc.collect()
    torch.cuda.empty_cache()
    print("done")
```

### Expected behavior

When the model is loaded for the first time, after deleting the model and calling torch.cuda.empty_cache(), the occupied GPU memory is not cleaned. However, the newly occupied GPU memory during the second and third model loading can be cleaned normally.

What can be done to fully reclaim the GPU memory?

## 评论 (2)

### hychiang-git · 2025-08-22

I have the same issue. I have the test code at this issue.

https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1141#issuecomment-3215045004

### TimDettmers · 2026-02-16

Closing this issue. The behavior you're seeing — GPU memory not being fully released after deleting a 4-bit quantized model and calling `torch.cuda.empty_cache()` — is a known characteristic of how PyTorch and CUDA manage memory, not a bitsandbytes bug.

The first model load initializes the CUDA context, which allocates a fixed amount of GPU memory that persists for the lifetime of the process. This is why the first load leaves a memory footprint that subsequent `del` + `empty_cache()` cannot reclaim, while later loads/deletes appear to work correctly (the CUDA context already exists).

Additionally, bitsandbytes registers some global state (quantization lookup tables, optimizer dispatch tables) on first import that remain in GPU memory. This is by design for performance.

If you need to fully reclaim GPU memory between models, the reliable approach is to run each model in a separate subprocess (e.g., using `torch.multiprocessing` or Python's `subprocess` module).

If you're seeing memory growth beyond the initial CUDA context overhead (i.e., memory keeps increasing with each load/delete cycle), that would be a different issue — please open a new issue with memory measurements from multiple cycles.
