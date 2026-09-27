# [Issue #265] vila15_demo.py need deepspeed installed in Orin

source: https://github.com/mit-han-lab/llm-awq/issues/265
state: open | updated: 2025-03-19T05:30:28Z
labels: 

## 正文

I want to run VILA-1.5-13b-AWQ using TinyChat on an NVIDIA Jetson Orin, but encountered two issues during execution:

ModuleNotFoundError: No module named 'deepspeed' when running the model.
AttributeError: module 'torch.distributed' has no attribute 'ReduceOp' when attempting to install DeepSpeed.
According to this NVIDIA forum thread, PyTorch v1.11+ no longer compiles distributed functionality by default. Given this, how should I properly run VILA-1.5-13b-AWQ on the Orin platform?

## 评论 (2)

### StephenChou0119 · 2025-03-05

The version of PyTorch I am using is torch-2.3.0a0+6ddf5cf85e.nv24.04.14026654-cp310-cp310-linux_aarch64.whl, and the version of VILA is c8f603b49f5dcfca8c2ee18d7979897a83aa5fa6

### Louym · 2025-03-19

If you are only using TinyChat for inference, you can simply comment out all the VILA code related to DeepSpeed. Based on my experience, commenting out the problematic code in the VILA repository often resolves the issue. Additionally, the amount of code that needs to be commented out is minimal.
