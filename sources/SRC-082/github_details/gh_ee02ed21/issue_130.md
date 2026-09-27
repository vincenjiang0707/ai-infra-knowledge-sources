# [Issue #130] AWQ and SmoothQuant

source: https://github.com/mit-han-lab/llm-awq/issues/130
state: open | updated: 2024-12-04T05:02:08Z
labels: 

## 正文

Hi, first of all congrats for the great work!

I wanted to ask why isn't there a more thorough comparison between AWQ and SmoothQuant in the paper. To my understanding, they both work using a similar intuition, scaling up weights and scaling down activations. SmoothQuant uses W8A8, which according to #56 is faster for large batch sizes since it can use faster matrix multiplication, while AWQ uses W4A16 (FP activations), which is faster for small batch sizes (but slower for larger ones as you have to dequantize the weights every time in order to perform matrix multiplication in FP16).

However how do they compare in perplexity benchmark and why were they not compared in the paper since they come from the same authors? Am I missing something? 

Thank you in advance for your help!

## 评论 (4)

### DavidePaglieri · 2024-01-16

Hi, would it be possible to get an answer on this? Still curious about it...

### tanguofu · 2024-01-19

same question~

### Skyseaee · 2024-10-10

Same question cause I've been observing a slight dip in accuracy with AWQ compared to SmoothQuant across several recent experiments.

### CorbinFoucart · 2024-12-04

Same question
