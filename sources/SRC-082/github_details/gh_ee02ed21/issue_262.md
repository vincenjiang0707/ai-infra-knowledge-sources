# [Issue #262] Setup.py file - Version Issues

source: https://github.com/mit-han-lab/llm-awq/issues/262
state: open | updated: 2025-03-20T12:14:40Z
labels: 

## 正文


1. **OS:** Linux || Ubuntu 20.04
2. **CUDA version:** 11.4 
3. **Driver:** NVIDIA UNIX Open Kernel Module for aarche 35.4.1
4.  **Device:** Jetson AGX Orion Developer Kit - Jetpack 5.1
5.  **Python 3.8** && **Pytorch 2.0.0**

Issue while running this command: 
**python setup.py install**


I am not able to run the the setup.py file  as the error indicates there's an RuntimeError: Compiling objects for extension

Also, I faced no such issue while setting up my Jetson Orion Nano, so I am not sure what exactly the issue is. 

## 评论 (3)

### Louym · 2025-03-19

Could you please provide more details about the compilation error? Additional information, such as error messages or logs, would be extremely helpful in diagnosing and resolving the issue.

### mattam301 · 2025-03-20

I supposed that he has the same issue as me when setting up AWQ kernel on the machine with CUDA version 11.2:

run:
python setup.py install

get:
RuntimeError: 
The detected CUDA version (11.2) mismatches the version that was used to compile
PyTorch (12.4). Please make sure to use the same CUDA versions.

Previously, I have successfully installed AWQ kernel in 2 other machines with CUDA version 12 installed.

### Louym · 2025-03-20

@mattam301 

To resolve this issue, you can try:
Install the correct CUDA version: Upgrade your CUDA to version 12.4 to match the one used by PyTorch.
or
Install a compatible PyTorch version: Install a version of PyTorch that matches your current CUDA version (11.2). You can find the appropriate version on the [PyTorch website](https://pytorch.org/get-started/previous-versions/).

This issue can sometimes occur if other packages modify the installed PyTorch version. Double-check your environment to ensure consistency between CUDA and PyTorch versions. Anyway， I recommend to compile awq kernels last.
