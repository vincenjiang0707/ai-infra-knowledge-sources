# [Issue #40] 模型推理结果混乱，怎么解决。

source: https://github.com/LLMServe/DistServe/issues/40
state: open | updated: 2025-03-26T07:47:40Z
labels: 

## 正文

我使用的模型是llama-2-7b-chat。分别试了OfflineLLM和onlineLLM。生成的结果存在混乱的情况。

例如
Prompt: 'Life blooms like a flower. Far away or by the road. Waiting',
Generated text: for the right time to blo om . Ћ 
 The sun is sh ining on the earth . 
 The sun is sh ining on the earth . 
 The moon is sh ining on the sea . 
 The sun is sh ining on the sea . 
 The moon is sh ining on the sea . 
 The moon is sh (64 tokens generated).

Prompt: 'I have a cold and a headache. What should I do? ', 
Generated text: 1 . 
 I have a cold and a head ache . I ' m not feeling well . 
 I ' m not feeling well . 
 I ' m not feeling well . 
 I ' m not feeling well . 
 I ' m not feeling well . 
 I ' m feeling sick . 
 I ' m feeling sick (64 tokens generated).
 

 而使用HF原生的代码的结果是：
 Prompt：
I have a cold and a headache. What should I do? 
Generated text: 
You should drink plenty of fluids and take paracetamol. If the headache is severe, you should consult your doctor.

请问下是哪里可能出问题了。

## 评论 (3)

### Avabowler · 2024-08-27

我也遇到了这个情况，我感觉是后端的swifttransformer存在一些bug，你可以试着比较一下HF和distserve的logits看看

### Avabowler · 2024-08-27

另外貌似distserve一旦结尾不是, 或者word，distserve的输出就很奇怪

### LordEdison · 2025-03-26

（我也是遇到了推理结果很混乱的情况，甚至有的时候某些request在prefill结束后直接stop了、没有decode）
