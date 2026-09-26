# [Issue #153] How to reproduce average acceptance length?

source: https://github.com/SafeAILab/EAGLE/issues/153
state: closed | updated: 2025-09-25T06:30:39Z
labels: 

## 正文

Hello,

Thank you for your work and contribution to the community.

I've been reproducing the numbers from the EAGLE-2 paper, particularly Table 1 for the L2-7B model. However, I haven't been able to find the code that calculates $\tau$ (average acceptance length). While I found that it's possible to compute acceptance length by modifying evaluation/gen_ea_answer_llama2chat.py and model/ea_model.py (as mentioned in this issue https://github.com/SafeAILab/EAGLE/issues/146), I am concerned that this approach may introduce inaccuracies due to discrepancies with your approach to measure $\tau$. Could you please confirm whether this is how you measured $\tau$ and provide your code for measuring average acceptance length, along with a smaller example of how to run it?

Thank you!

## 评论 (5)

### Liyuhui-12 · 2024-11-04

The average acceptance length can be calculated by dividing the total number of generated tokens by the number of steps, which can be obtained from the output files.

### Lyn-Lucy · 2024-11-18

Thank you for your answer! I calculated the sum of all new_tokens and divided it by the sum of idxs from the output file to get acceptance_length. I calculated the result of the Llama-2-7b-chat model, but it was still lower than the result in the report. The device I used was also A100 40G*4
```python
file_path = './Llama-2-7b-chat-ea-temperature-0.0.jsonl'

new_tokens_sum = 0
idxs_sum = 0

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 解析JSON数据
        data = json.loads(line.strip())
        if "choices" in data:
            for choice in data["choices"]:
                new_tokens_sum += sum(choice.get("new_tokens", []))
                idxs_sum += sum(choice.get("idxs", []))

result = new_tokens_sum / idxs_sum if idxs_sum != 0 else None

print(f"New Tokens Sum: {new_tokens_sum}")
print(f"Idxs Sum: {idxs_sum}")
print(f"Result (New Tokens / Idxs): {result}")
```
output
```bash
New Tokens Sum: 48354
Idxs Sum: 10670
Result (New Tokens / Idxs): 4.531771321462043
```

### Lihui-Gu · 2025-05-24

My experiment on EAGLE-3
model : Llama-3.1-8B-Instruct
dataset : mt_bench
accept_length ($\tau$) in paper : 6.14，my result : 5.66

### ekagra-ranjan · 2025-05-30

@Lihui-Gu how many draft are you generating? Is it chain draft or tree draft?

### KerwinKai · 2025-09-25

> Thank you for your answer! I calculated the sum of all new_tokens and divided it by the sum of idxs from the output file to get acceptance_length. I calculated the result of the Llama-2-7b-chat model, but it was still lower than the result in the report. The device I used was also A100 40G*4
> 
> file_path = './Llama-2-7b-chat-ea-temperature-0.0.jsonl'
> 
> new_tokens_sum = 0
> idxs_sum = 0
> 
> with open(file_path, 'r', encoding='utf-8') as file:
>     for line in file:
>         # 解析JSON数据
>         data = json.loads(line.strip())
>         if "choices" in data:
>             for choice in data["choices"]:
>                 new_tokens_sum += sum(choice.get("new_tokens", []))
>                 idxs_sum += sum(choice.get("idxs", []))
> 
> result = new_tokens_sum / idxs_sum if idxs_sum != 0 else None
> 
> print(f"New Tokens Sum: {new_tokens_sum}")
> print(f"Idxs Sum: {idxs_sum}")
> print(f"Result (New Tokens / Idxs): {result}")
> output
> 
> New Tokens Sum: 48354
> Idxs Sum: 10670
> Result (New Tokens / Idxs): 4.531771321462043

I think `idxs_sum += sum(choice.get("idxs", []))` ought change to `idxs_sum += sum(choice.get("idxs", [])) + 2`, in llama3.1 8b instruct case(when t=0, benchmark=gsm8k, alpaca), I reproduced the results in Table 1 of the Eagle3 paper by modifying this line of code. However, this is only a numerical match; I'm still trying to understand why this modification is necessary.
