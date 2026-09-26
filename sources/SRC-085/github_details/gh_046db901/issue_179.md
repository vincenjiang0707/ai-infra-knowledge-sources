# [Issue #179] Training on Chinese dataset does not work

source: https://github.com/SafeAILab/EAGLE/issues/179
state: open | updated: 2025-10-01T15:22:57Z
labels: 

## 正文

Hello, thanks for this nice work.

I trained a eagle "English" verison model on qwen2.5, and tested it on mt_bench data. The ratio is about 3.0. I also tested it with `some chinese question task` the ratio droped to about 1.5. 

So I decided to train a "Chinese" version eagle model with a [`Chinese Sharegpt dataset`](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-chinese). The data generation and training works similar to the "English" verison: after 200 epoch, train accuracy : 81.04% test accuracy 79.22% Loss: 0.7023.

But the problem is when i test it using the same `some chinese question task` above, there is no accrracy at all. The speed ratio droped blow 1.0. Does this mean the [`Chinese Sharegpt dataset`](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-chinese) i used is not good? or I missed something? 

Thanks for your help

## 评论 (8)

### Liyuhui-12 · 2025-03-04

Your test accuracy is high, but the actual inference cannot be accelerated. A possible reason is that your training data (including the test set) differs significantly from the actual inference scenario.

### xiaonengmiao · 2025-03-13

> Your test accuracy is high, but the actual inference cannot be accelerated. A possible reason is that your training data (including the test set) differs significantly from the actual inference scenario.

@Liyuhui-12 Thanks for the reply!
Do u have any suggestions on the Chinese data training. For example, which data should i use? And any special things need to do before using `allocation.py` to generate data?

### souyang11 · 2025-03-24

Hello, I am currently using sglang + yuhuili/EAGLE-Qwen2-7B-Instruct for inference, and I noticed that the throughput has slowed down. Do you know the reason for this? thank you.

### liusong1222 · 2025-05-07

@xiaonengmiao  Hello, I have same problem. Have you ever tried testing the acceptance rate directly using the training data? 

### WenXIN-AI · 2025-07-12

qwen‘s tokenizer problem?


### wenqf11 · 2025-08-22

I also  trained qwen3-8b eagle3 using SpecForge on a Chinese dataset(Chinese-DeepSeek-R1-Distill-data-110k)(generated answer using Qwen3-8B), but after 10 epoch only got (Position 0) train acc 0.7. and test using vllm with prompts from training dataset, the acceptance rate is 25%\~30%, speedup 1.3X\~1.4X. Any advice, thanks!

### shhn1 · 2025-09-29

> I also trained qwen3-8b eagle3 using SpecForge on a Chinese dataset(Chinese-DeepSeek-R1-Distill-data-110k)(generated answer using Qwen3-8B), but after 10 epoch only got (Position 0) train acc 0.7. and test using vllm with prompts from training dataset, the acceptance rate is 25%~30%, speedup 1.3X~1.4X. Any advice, thanks!

I got same problem. Any advice, thanks!

### wenqf11 · 2025-10-01

> > I also trained qwen3-8b eagle3 using SpecForge on a Chinese dataset(Chinese-DeepSeek-R1-Distill-data-110k)(generated answer using Qwen3-8B), but after 10 epoch only got (Position 0) train acc 0.7. and test using vllm with prompts from training dataset, the acceptance rate is 25%~30%, speedup 1.3X~1.4X. Any advice, thanks!
> 
> I got same problem. Any advice, thanks!

Just make sure train acc(position 0) is higher around 0.8.( I just make learning rate decay as expected)
