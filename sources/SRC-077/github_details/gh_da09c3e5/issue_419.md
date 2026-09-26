# [Issue #419] Make it possible to fully release problems in a standalone service that vendors can work on self-serve.

source: https://github.com/gpu-mode/kernelbot/issues/419
state: closed | updated: 2026-03-04T16:46:16Z
labels: 

## 正文

I thought this would require a lot of work but after I did this work https://github.com/gpu-mode/kernelbot/commit/e2ee3d79d3231f900b9975fdac0d405b3ecbd7ca

I think we can just tell a vendor to git clone reference kernels, popcorn-cli and kernelbot, make the changes they need to and let claude validate that everything is working well

So there's still some work left but not a lot

## 评论 (1)

### msaroufim · 2026-02-11

It's possible to now tell people that they can just clone all 3 repos and have claude do the rest

But it's still a challenge for people, although @S1ro1 says it's probably fine if things are not totally self serve
