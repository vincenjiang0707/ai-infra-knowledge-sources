# [Issue #2894] [Bug] Any Model with the Suffix _1 Crashes Android

source: https://github.com/mlc-ai/mlc-llm/issues/2894
state: closed | updated: 2026-03-01T20:44:04Z
labels: bug

## 正文

## 🐛 Bug

I tried this on both the 23 ultra and the 24

## To Reproduce


1.Using any model such as Qwen2_1_5B_q4f16_1 try to send a prompt. 

I've tested many models and it seems to be models with _1 causing the issue.  Can someone explain what _1 is actually doing compared to the _0 or even the _2? I know its mentioned here https://llm.mlc.ai/docs/compilation/configure_quantization.html#quantization-mode but I am new to this

This doesnt happen all the time with very short prompts such as Hi 

![image](https://github.com/user-attachments/assets/9be05e5e-af66-438f-bf18-354fd2b63a01)



## 评论 (1)

### Melgark · 2024-09-12

Looking into it, I came across this https://github.com/mlc-ai/mlc-llm/blob/main/python/mlc_llm/quantization/group_quantization.py#L37

Curious as to how the models take these .bin files and know how to transpose them into a readable model. That Way I can see if maybe its an unsupported operator?  Any pointers would be helpful.
