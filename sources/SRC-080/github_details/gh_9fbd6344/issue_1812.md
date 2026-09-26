# [Issue #1812] Clarify recommended QAD configs for full-quality recovery in diffusers examples

source: https://github.com/NVIDIA/Model-Optimizer/issues/1812
state: open | updated: 2026-06-28T05:41:21Z
labels: question, windows

## 正文

Make sure you already checked the [examples](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples) and [documentation](https://nvidia.github.io/Model-Optimizer/) before submitting an issue.

## How would you like to use ModelOpt

<!-- Description of what you would like to do with ModelOpt. -->
https://github.com/nvidia/model-optimizer/blob/main/examples/windows/diffusers/qad_example/README.md  
I’m looking at the diffusers QAD example here:

examples/windows/diffusers/qad_example

The example config uses:

batch_size: 1
gradient_accumulation_steps: 4
steps: 300
FSDP num_processes: 8

So the effective batch size seems to be 1 × 4 × 8 = 32.

Could you clarify the recommended settings for a real production-quality QAD run, not just a smoke test?

Main questions:

What effective batch size is usually recommended for stable QAD quality recovery? Is 32 enough, or should we target 64 or higher?
Do you have any internal or public successful QAD examples for large Diffusers/DiT models such as LTX-2 or similar-size models? If yes, what batch size, steps, and learning rate were used?
For a full QAD recovery run on large diffusion models, roughly how many B200/B300 GPUs should users expect to need?
Is steps=300 only intended as a demo/smoke-test config, or has it been enough in real QAD recovery cases? 

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): ?
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): ? <!-- If Windows, please add the `windows` label to the issue. -->
- CPU architecture (x86_64, aarch64): ?
- GPU name (e.g. H100, A100, L40S): ?
- GPU memory size: ?
- Number of GPUs: ?
- Library versions (if applicable):
  - Python: ?
  - ModelOpt version or commit hash: ?
  - CUDA: ?
  - PyTorch: ?
  - Transformers: ?
  - TensorRT-LLM: ?
  - ONNXRuntime: ?
  - TensorRT: ?
- Any other details that may help: ?


## 评论 (5)

### ynankani · 2026-06-24

Thank you for the detailed question.

>>What effective batch size is usually recommended for stable QAD quality recovery? Is 32 enough, or should we target 64 or higher?
>>Do you have any internal or public successful QAD examples for large Diffusers/DiT models such as LTX-2 or similar-size models? If yes, what batch size, steps, and learning rate were used?

Yes, we worked on production QAD for LTX-2.3 NvFP4 model please see [Model-LTX2.3-NVFP4](https://huggingface.co/Lightricks/LTX-2.3-nvfp4),  [Distillation Script](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/diffusers/distillation).

We trained W4A4_NvFP4 Quantized LTX-2.3 using knowledge distillation on Blackwell B200 (W4A4 Tensor core), Settings: 
  learning_rate: 2.0e-6
  steps: 10000
  batch_size: 1
  gradient_accumulation_steps: 4
  FSDP machines: 8
  FSDP num_processes: 8
 Effective batch size = 256

>>For a full QAD recovery run on large diffusion models, roughly how many B200/B300 GPUs should users expect to need?
>>Is steps=300 only intended as a demo/smoke-test config, or has it been enough in real QAD recovery cases?

Yes, Steps=300 is demo/smoke-test config setting as mentioned in Readme. 
For LTX-2.3-NVFP4 support we trained for 10000 steps with a high quality video dataset for ~4000GPU hours(8 B200 nodes each with 8GPUs for 2.5days). 

Please let me know if you have any further queries.

cc: @vishalpandya1990 , @jingyu-ml 


### baonudesifeizhai · 2026-06-24

 is that datasets all opensources?      
> Thank you for the detailed question. 
> 
> > > What effective batch size is usually recommended for stable QAD quality recovery? Is 32 enough, or should we target 64 or higher?
> > > Do you have any internal or public successful QAD examples for large Diffusers/DiT models such as LTX-2 or similar-size models? If yes, what batch size, steps, and learning rate were used?
> 
> Yes, we worked on production QAD for LTX-2.3 NvFP4 model please see [Model-LTX2.3-NVFP4](https://huggingface.co/Lightricks/LTX-2.3-nvfp4), [Distillation Script](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/diffusers/distillation).
> 
> We trained W4A4_NvFP4 Quantized LTX-2.3 using knowledge distillation on Blackwell B200 (W4A4 Tensor core), Settings: learning_rate: 2.0e-6 steps: 10000 batch_size: 1 gradient_accumulation_steps: 4 FSDP machines: 8 FSDP num_processes: 8 Effective batch size = 256
> 
> > > For a full QAD recovery run on large diffusion models, roughly how many B200/B300 GPUs should users expect to need?
> > > Is steps=300 only intended as a demo/smoke-test config, or has it been enough in real QAD recovery cases?
> 
> Yes, Steps=300 is demo/smoke-test config setting as mentioned in Readme. For LTX-2.3-NVFP4 support we trained for 10000 steps with a high quality video dataset for ~4000GPU hours(8 B200 nodes each with 8GPUs for 2.5days).
> 
> Please let me know if you have any further queries.
> 
> cc: [@vishalpandya1990](https://github.com/vishalpandya1990) , [@jingyu-ml](https://github.com/jingyu-ml)



### ynankani · 2026-06-25

>>is that datasets all opensources?

The dataset is not open source, it is a curated dataset specifically prepared for training the LTX-2.3 model. Alternatively, a synthetic dataset generated using a base model can also be utilized for training a quantized model.

### baonudesifeizhai · 2026-06-25

<img width="867" height="213" alt="Image" src="https://github.com/user-attachments/assets/92922d65-136a-49c9-9f2c-0049bc341854" />
So when will it coming ...?  
Sad  

> > > is that datasets all opensources?
> 
> The dataset is not open source, it is a curated dataset specifically prepared for training the LTX-2.3 model. Alternatively, a synthetic dataset generated using a base model can also be utilized for training a quantized model.



### ynankani · 2026-06-28

>>So when will it coming ...? Sad

We don't have much update from model developer for the distilled model NVFP4 quantized version.
