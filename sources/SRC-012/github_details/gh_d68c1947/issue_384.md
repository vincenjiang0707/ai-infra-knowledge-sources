# [Issue #384] [Feature Request] Is there any plan for stable diffusion running  under this project?

source: https://github.com/mlc-ai/mlc-llm/issues/384
state: closed | updated: 2026-03-01T20:42:51Z
labels: feature request

## 正文

## 🚀 Feature
Support stable diffusion models! 
SnapFusion models can run in the phone within 2 seconds!    
[https://arxiv.org/pdf/2306.00980.pdf](https://arxiv.org/pdf/2306.00980.pdf)

## Motivation

Text-to-image diffusion models can create stunning images from natural language descriptions.  It is an important node in large model ecology！

## Alternatives

should we use weapon of tvm unity  to reach the deployment  of stable diffusion model  on any devices with gpu?

## Additional context



## 评论 (6)

### yzh119 · 2023-06-12

Thanks for suggesting the paper, we'll read it and see how can we benefit from SnapFusion.

Yes, TVM Unity could be used to deploy Stable-Diffusion models, we already have a [web-stable-diffusion](https://github.com/mlc-ai/web-stable-diffusion) repo which uses TVM Unity for SD models on web browsers.

### felixslu · 2023-06-12

Thanks for your advise!  I will try this repo.([web-stable-diffusion](https://github.com/mlc-ai/web-stable-diffusion))

 As I known,3-4 bit quantization technology  (such as gptq) have not been used in the web-stable-diffusion project , maybe it could benefit from  the optimization methods in mlc-llm project ? (Maybe your team could support a quantization version for SD to accelerate infer cost time. )

### felixslu · 2023-06-13

Hi,MLC team! I have try to run this repo ,but failed!([web-stable-diffusion](https://github.com/mlc-ai/web-stable-diffusion)).

Firstly, I try to use pre-auto-tuned schedule params in directory of log_db ,but get errors.  ["https://github.com/mlc-ai/web-stable-diffusion/issues/38".](https://github.com/mlc-ai/web-stable-diffusion/issues/38)

Then, I try to do auto-tuning by myself,  but get other errors. ["Did you forget to bind? RuntimeError: Memory verification failed with the following errors".](https://github.com/mlc-ai/web-stable-diffusion/issues/39)

Can I get any furture help from your team? Thanks!


### felixslu · 2023-06-14

hi,MLC Team!
Could you have time to update the stable diffusion log_db ? ([web-stable-diffusion](https://github.com/mlc-ai/web-stable-diffusion))
Because, we can not get auto-tunning params for newly introduced purity flag. We get error below when do "ms.database.create" ops.

/workspace/tvm/src/node/serialization.cc:375: JSONReader: cannot find field purity
https://github.com/mlc-ai/mlc-llm/issues/407




### Jack47 · 2023-07-20

is there any update? it would be really awesome if stable diffusion can be run on mobile phones

### Fcucgvhhhvjv · 2023-08-04

> is there any update? it would be really awesome if stable diffusion can be run on mobile phones

https://github.com/ZTMIDGO/Android-Stable-diffusion-ONNX
here
