# [Issue #66] [Issue]: rocprofv3 is not working with venv python

source: https://github.com/ROCm/rocprofiler-sdk/issues/66
state: closed | updated: 2025-07-21T19:10:56Z
labels: 

## 正文

### Problem Description

I would like to trace some python examples from ROCm, like this one from aiter project
```
python op_tests/test_layernorm2d.py
```

I am running this in a venv where I have installed a torch for  ROCm. However when I try to run this with a profiler it does not work
```
 rocprofv3 --hip-trace -o result -- python op_tests/test_layernorm2d.py
E20250519 23:11:23.430672 140657861990144 output_stream.cpp:105] Opened result file: <path>/aiter/result_agent_info.csv
E20250519 23:11:24.192884 139891201828608 output_stream.cpp:105] Opened result file: /home/amd/ssolovye/aiter/result_agent_info.csv
Traceback (most recent call last):
  File "<path>/aiter/op_tests/test_layernorm2d.py", line 112, in <module>
    test_layernorm2d_fuseAdd(dtypes.bf16, 128, 8192)
  File "<path>/aiter/op_tests/test_layernorm2d.py", line 88, in test_layernorm2d_fuseAdd
    input = torch.randn(dim, dtype=dtype, device="cuda")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<path>/myenv-py311/lib/python3.11/site-packages/torch/cuda/__init__.py", line 372, in _lazy_init
    torch._C._cuda_init()
RuntimeError: No HIP GPUs are available
```

Running the test by itself works fine
```
python op_tests/test_layernorm2d.py
```

### Operating System

 Ubuntu 22.04.5 LTS

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

 AMD Instinct MI300X (gfx942)

### ROCm Version

ROCk module version 6.12.12 is loaded

### ROCm Component

_No response_

### Steps to Reproduce

python3.11 -m venv ~/myenv-py311
source ~/myenv-py311/bin/activate

pip install --upgrade pip  
pip install --upgrade setuptools  

pip install torch --index-url https://download.pytorch.org/whl/rocm6.3

git clone --recursive https://github.com/ROCm/aiter.git

cd aiter
pip install -r requirements.txt
pip install PyYAML
pip install wheel
python3 setup.py develop

rocprofv3 --hip-trace -o result -- python op_tests/test_layernorm2d.py

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (6)

### jrmadsen · 2025-05-23

Hi @JohnNikolay84 could you try using `python $(which rocprofv3)` instead of just `rocprofv3`? rocprofv3 itself is a Python script and, although I cannot think of anything in particular that we are doing in that script which might alter what which Python is being used to run the script, that may be the source of the issue. If that doesn’t work, try using the full path to `python`. Lastly, are you certain that the rocprofv3 you are using is from ROCm 6.3? It is possible that a newer/older rocprofv3 is causing the newer/older rocm libraries to get loaded and consequently causing issues when PyTorch runs 

### xifengT · 2025-05-27

hi, I also encountered this problem. When I use rocprofv3/v2, it will show "No HIP GPUs are available". May I ask if you have solved this problem?

### JohnNikolay84 · 2025-05-27

Not sure what has changed, but the problem has somehow disappeared for me.

### xifengT · 2025-05-28

Hi @jrmadsen Thank you for your suggestion, but I tried to use `python $(which rocprofv3)` instead of `rocprofv3`, but the result was still the same, Are there any other ways to solve this problem. Does the entire path of the `python` interpreter refer to `rocprofv3` or the python script I want to track ? My rocprofv3 is from ROCm6.4 and my torch is ROCm6.3. This is the latest torch.

### Rowamo · 2025-07-18

Experiencing this issue as well. rocm-smi shows that the GPU is being detected and running the same command without rocprof works fine.

### Rowamo · 2025-07-19

if anyone else is getting this issue with pytorch and/or triton, the fix is to install the nightly pytorch version. This is most likely caused by installing a pytorch or triton version for Nvidia (not AMD/ROCm).
Installing the stable pytorch-rocm version will **not** work: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.3
