# [Issue #196] Can not reproduce the results of EAGLE3-DeepSeek-R1-Distill-LLaMA-8B

source: https://github.com/SafeAILab/EAGLE/issues/196
state: open | updated: 2025-06-27T11:10:34Z
labels: 

## 正文

Hi,

I am trying to reproduce the results of EAGLE3-DeepSeek-R1-Distill-LLaMA-8B model. I use the command `python -m gen_ea_answer_llama3chat --ea-model-path yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B --base-model-path deepseek-ai/DeepSeek-R1-Distill-Llama-8B --bench-name gsm8k --model-id deepseek_llama_8B` for reproducing on GSM8K and print the new_tokens and idx for every single question. However, I can only achieve an average new_tokens/idx value of less than 3. In my unstanding, it means that the acceptance length is less than 3, which has a large gap to the reported number in EAGLE3 paper. Could you kindly share me some insights to solve this problem? Thank you!

## 评论 (9)

### Qinghao-Hu · 2025-03-27

same problem


### Elisabethhui · 2025-03-28

the speedup of DSL  on mt-bench  in  the paper eagle3 is  4.05x, but i only get ration 1.38.  compare two scripts of gen_baseline_answer_llama3chat.py and gen_ea_answer_llama3chat.py with main args like --question-begin 0 --question-end 50 --max-new-token 50 --top-k 10 --num-choices 1 --temperature 0 --tree-choice mc_sim_7b_63 . 

### Liyuhui-12 · 2025-03-28

The template of DeepSeek R1 differs from LLaMA3, so different models should be used. `gen_ea_answer_llama3chat.py` applies the LLaMA3-Chat template, which is incompatible with DeepSeek’s weights. Instead, `eagle/evaluation/gen_ea_answer_ds.py` should be used for testing.

### Qinghao-Hu · 2025-04-03

> The template of DeepSeek R1 differs from LLaMA3, so different models should be used. `gen_ea_answer_llama3chat.py` applies the LLaMA3-Chat template, which is incompatible with DeepSeek’s weights. Instead, `eagle/evaluation/gen_ea_answer_ds.py` should be used for testing.

Thanks for the clarification! I followed `gen_ea_answer_ds.py` to use an empty system prompt, but the acceptance length is still less than 3 (only 2.2). Could you please have a check?

### Liyuhui-12 · 2025-04-22

Did you directly use `gen_ea_answer_ds.py`?

### Dongximing · 2025-05-05

Thanks for your work! Could you please provide a script when using the Deepseek-R1 model?:)

### junghye01 · 2025-05-07

@Qinghao-Hu 
Did you verify whether d2t (the mapping from draft to target vocab indices) is working correctly,
especially given that the target vocab size and draft vocab size are different in DeepSeek-R1-Distill-Llama-8B?

### littlewhitebee · 2025-06-14

Thanks for your work! Could you please provide a script when using the Deepseek-R1 model?When I tested it on a 4090 GPU, the speedup based on `mt_bench` data was only 3.17。I use the command `python -m gen_ea_answer_ds --ea-model-path yuhuili/EAGLE3-DeepSeek-R1-Distill-LLaMA-8B --base-model-path deepseek-ai/DeepSeek-R1-Distill-Llama-8B --bench-name mt_bench --model-id speed_up`.

### smart-lty · 2025-06-27

@Liyuhui-12 I get the same results with @Qinghao-Hu when using DeepSeek-R1-Distill-LLaMA-8B as the target model. (the accept length is less than 3 with correct chat templates). I have verified that d2t is activated. In the first step, `print(self.d2t)` gives the results:

`tensor([    0,     0,     0,  ..., 96015, 96015, 96015], device='cuda:0') `

Could you please provide a script to reproduce the results in the paper?
