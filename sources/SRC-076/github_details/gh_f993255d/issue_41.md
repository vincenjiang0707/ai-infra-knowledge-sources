# [Issue #41] Generate samples resulting in function execution timeout

source: https://github.com/ScalingIntelligence/KernelBench/issues/41
state: closed | updated: 2025-10-14T23:50:48Z
labels: 

## 正文

I am running Kevin-32b by cognition-ai to generate samples for benchmarking. However, for kernels taking longer than 8k tokens keeps showing me following error: 

Error generating sample 14 0: modal-http: internal error: function execution timed out


I have deployed my model via sglang using modal infrastructure. I have increased the timeout in the OpenAI client but it keeps coming again and again. Can anyone help me? 



## 评论 (1)

### simonguozirui · 2025-10-14

@agokrani very cool that you tried evaluating Kevin 32B kernels with KernelBench set up. 

It seems to me this error is from the modal side, and my hypothesis is that the kernel code / program is very long (8k tokens), which might contain some error that either hung or crashed in the Modal instance during execution. A quick sanity check is to run the same kernel code on a bare-metal machine and see if that behavior still persists.

Increasing the timeout for OpenAI client (for LLM generating kernel won't help), but I would recommend increasing time out for the eval function. Does this only happen on a select few kernels for problems or on all of them?

