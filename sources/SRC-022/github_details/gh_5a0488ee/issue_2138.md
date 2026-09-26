# [Issue #2138] Is there good support for multiple concurrent GPU models?

source: https://github.com/ROCm/rccl/issues/2138
state: closed | updated: 2026-01-22T02:06:54Z
labels: status: triage

## 正文

I plan to build a type-safe distributed ML API around ROCm/rccl (for https://codeberg.org/joelberkeley/spidr), and I'm now buying GPUs to test it. I'm looking at consumer GPUs, esp. 9060 XT and 9070 XT. What I'd like to know, is if I buy a mix of different models - say one 9060XT and one 9070XT, will ROCm/rccl play nicely with that, or am I best off getting a single model across all GPUs, e.g. all 9060s or all 9070s?

## 评论 (5)

### huanrwan-amd · 2026-01-12

Hi @joelberkeley, thanks for posting. 
The answer depends on your objective, in short, 

- if you want a better performance, it is better to a single model across all GPUs. As the slowest (compute and memory bandwidth) GPU will often bottleneck collective operations

- If you just want to test whether thing is working, GPUs from the same generation/architecture (e.g., both RDNA 3 or both RDNA 4) generally work better together.  

### joelberkeley · 2026-01-12

OK thanks. I don't care about performance, so it sounds like one 9060xt and one 9070xt would do fine

### huanrwan-amd · 2026-01-12

> OK thanks. I don't care about performance, so it sounds like one 9060xt and one 9070xt would do fine

Please be advised that the GPU arch build flag could also be different:
https://github.com/ROCm/rccl/blob/420b3b840e0324ea897db7f04028471a4ea830d7/CMakeLists.txt#L60 
We do not have such a setup to verify the correctness...

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2787

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
