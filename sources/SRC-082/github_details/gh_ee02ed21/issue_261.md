# [Issue #261] Killed: Out of Memory on Jetson Orion

source: https://github.com/mit-han-lab/llm-awq/issues/261
state: closed | updated: 2025-04-10T01:18:27Z
labels: 

## 正文

Thank you for the great work, I really appreciate it.

1. **Conda Environment:** 3.10
2. **Device:** Jetson Orin Nano Developer Kit 8GB - Jetpack 6.0
3. **Model:** [llama-2-7b-chat-hf ] [https://huggingface.co/meta-llama/Llama-2-7b-chat-hf](url) as mentioned in the Readme

I followed the steps as mentioned, but when running **Tinychat** I repeatedly encountered an issue:

1. Initially, I tried to "Perform the AWQ search" but ran **Out of Memory** & the process was **"Killed".** 
2. Then I tried to run the pre-saved results instead to run Tiny Chat [ .pt files provided in awq_cache] but eventually ran into the same issue (**"Killed"**)

I have tried these solutions to resolve the issue, but none were helpful:

1. I added **swap space** of 16GB and then 64GB, but the process was still killed. I suspect that it may have timed out and was eventually terminated.
2. I then reduced the **quantization group size** from 128 to 64, but this did not resolve the issue either.

Sometimes these solutions work but eventually get killed after a few conversations.Could you please suggest the possible solution or optimization to resolve this memory issue? I've attached a screen shot for better understanding. 

![Image](https://github.com/user-attachments/assets/42e635e7-240e-4fdc-927b-7b6a931be090)



## 评论 (2)

### ys-2020 · 2025-02-18

Hi, it seems you did not activate flash attention here. The memory of Nano is very restricted. When sequence length gets larger , the memory consumption of attention grows quadratically (if flash_attention is not enabled). That's why the program runs into OOM after several rounds of conversation. We also do not suggest doing quantization on Jetson Orin Nano.

### sfatimakhan · 2025-04-10

Thanks for your reply. I had activated the flash attention but faced a set of different issuea. Instead, used a 1TB SSD to make it work. 
