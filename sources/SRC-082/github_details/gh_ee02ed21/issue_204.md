# [Issue #204] Add support for GPUs with compute capability lower than 8.0 for awq/kernels installation

source: https://github.com/mit-han-lab/llm-awq/issues/204
state: open | updated: 2024-08-23T17:20:44Z
labels: 

## 正文

I tried to install and run the project on a machine with an NVIDIA Tesla T4 GPU, which has a compute capability of 7.5 (SM 75).

Environment
```
Ubuntu 22.04
CUDA 12.1
Tesla T4 GPU
```

I followed the steps as mentioned here https://github.com/mit-han-lab/llm-awq/tree/main?tab=readme-ov-file#install & encountered the following error during the third step installation process:
```
cd awq/kernels
python setup.py install
```
Following error was reported

```
ptxas /tmp/tmpxft_0000f5ba_00000000-6_gemm_cuda_gen.ptx, line 709; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_0000f5ba_00000000-6_gemm_cuda_gen.ptx, line 713; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_0000f5ba_00000000-6_gemm_cuda_gen.ptx, line 717; error   : Feature '.m16n8k16' requires .target sm_80 or higher
...
txas fatal   : Ptx assembly aborted due to errors
error: command '/usr/local/cuda-12.1/bin/nvcc' failed with exit code 255
Root Cause: Feature '.m16n8k16' requires .target sm_80 or higher
```

Is there a configuration flag or workaround to support GPUs with capacity below 8.0

## 评论 (1)

### maoki109 · 2024-08-23

I have a machine with an NVIDIA V100 GPU, which has a compute capability of 7.0. The following sort of worked for me:

In your terminal, type in the command `python -c "import torch; print(torch.cuda.get_arch_list())"`

Look at the output and check that `'sm_80'` is listed in there. 

If it is, rerun the install command inside `awq/kernels` like this:

`TORCH_CUDA_ARCH_LIST="8.0" python setup.py install`

When I say this "sort of worked" for me, I mean that it helped me get past this error, but then I ran into other (unrelated) issues with the code later on 🙃

I found this other issue to be helpful with this error message: https://github.com/mit-han-lab/llm-awq/issues/93

