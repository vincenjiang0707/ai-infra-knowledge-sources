# [Issue #2051] Bug Report: Server freezes when installing/compiling flash-attn with torch==2.9.0+cu128

source: https://github.com/Dao-AILab/flash-attention/issues/2051
state: closed | updated: 2026-07-17T10:55:22Z
labels: 

## 正文

Hi, thanks for the great work on FlashAttention.

I encountered a server freeze issue when installing flash-attn under PyTorch 2.9.0 + CUDA 12.8.
The problem occurs during compilation, and the machine becomes completely unresponsive (SSH disconnects and the server needs a hard reboot).

Environment

OS: Ubuntu 20.04
CUDA: 12.8
PyTorch: 2.9.0+cu128 (official wheels)
flash-attn version: latest from GitHub (also tried pip install)
GPU: NVIDIA RTX 5880 Ada Generation
Driver Version: 570.133.07
Compiler: default nvcc from CUDA 12.8
Python: 3.12

Build command:
```bash 
MAX_JOBS=4 pip install flash-attn --no-build-isolation
```
also tried installing from source
```bash
MAX_JOBS=4 python setup.py install
```
What happened

* During flash-attn compilation, CPU load spikes, and after some time the entire server freezes.
* SSH connection drops abruptly.
* No kernel logs are available because the machine becomes unresponsive.
* The only recovery method is hardware reboot.

I have successfully built flash-attn many times in other environments, including CUDA 11.x and PyTorch ≤ 2.7, so this issue seems specifically related to PyTorch 2.9 + CUDA 12.8.

## 评论 (18)

### rjmehta1993 · 2025-12-09

+1

### Yanko-7 · 2025-12-11

+1

### Romanio1997 · 2025-12-12

+1

### Qubitium · 2025-12-12

@SharlotAway Most likely your system ran out of memory due to too many threads. You can check this by compiling in a docker or vm and limiting the cpu cores/memory assigned to the docker and see if it crashes. Once there is no more memory, kernel is forced to kill processes left and right and usually unpredicatble what happens next. 

### Ration-Lee · 2025-12-13

+1

### qmzpg · 2025-12-14

+1

### qmzpg · 2025-12-14

@Qubitium My computer has 56 CPU cores, I used 1/4 of them，but the compilation still freezes .

### Qubitium · 2025-12-15

@qmzpg Can you monitor the ram usage using top/htop and post the screenshot before it crashes? This will give a sense if nvcc is running away with threads (nvcc spawns threads outside the num_jobs control). 

### SharlotAway · 2025-12-15

@Qubitium Actually I have tried to limit CPU numbers (16 of 64) and set MAX_JOBS=1 but the compilation still freeze. Viewing htop and top it seems nvcc is running away with threads. Moreover, my operation system is broken now. 

### Qubitium · 2025-12-15

@SharlotAway Can you post a screenshot? This would at least give us a snapshot of shape/kernel is causing the runaway. 

Also test `export NVCC_THREADS=1` to see if it fixes it for torch 2.9.0/cuda128 combo. By default it should only set nvcc threads to 4 in code if there is no NVCC_THREADS env.

### SharlotAway · 2025-12-15

@Qubitium Thanks for your suggestion. I'm unable to provide a screenshot at the moment because the server is currently undergoing maintenance. Once the maintenance is complete, I'll conduct `NVCC_THREADS` and test. If similar issues persist, I'll provide the relevant screenshots.

### Yanko-7 · 2025-12-15

> [@qmzpg](https://github.com/qmzpg) Can you monitor the ram usage using top/htop and post the screenshot before it crashes? This will give a sense if nvcc is running away with threads (nvcc spawns threads outside the num_jobs control).

Thank you, after setting `MAX_JOBS=4`, I was able to compile and install normally on my server. However, using htop to monitor, I found that the actual compilation used 8 cores and allocated up to 80GB of memory.

### Qubitium · 2025-12-15

@Yanko-7 @SharlotAway @qmzpg In addition to core count, please also let me know how much `ram` is in the `vm` or `host`.  I believe the issue is threads but the actual death of host os is result of oom. 

### Qubitium · 2025-12-15

> > [@qmzpg](https://github.com/qmzpg) Can you monitor the ram usage using top/htop and post the screenshot before it crashes? This will give a sense if nvcc is running away with threads (nvcc spawns threads outside the num_jobs control).
> 
> Thank you, after setting `MAX_JOBS=4`, I was able to compile and install normally on my server. However, using htop to monitor, I found that the actual compilation used 8 cores and allocated up to 80GB of memory.

`MAX_JOBS` is ninja job value and each job which triggers `NVCC` can spawn up to 4 threads in current code. So yes, `MAX_JOBS` * `NVCC_THREADS` is the worst case scenario. 

### ilyesbenaissa · 2025-12-16

+1

### Qubitium · 2025-12-17

@SharlotAway  Everyone, I have confirmed the memory usage is over 2x the above the previous estimate causing too many MAX_JOBS to be auto-assigned during default build (if you did not override the MAX_JOBS value). PR #2079 should fix this going forward. However, the minumum is MAX_JOBS=1 paired with NVCC_THREADS=4 so you still need a 20GB free ram which should be less of an issue. If you still get memory pressure with MAX_JOBS=1, reduce NVCC_THREADS from 4 to 1. 

The core cause is during the first 2 minutes of build, there is a massive spike in cicc/nvcc memory usage that is on the order of 5GB of memory per NVCC_THREAD and many of you have too many cores but not enough memory. 

Pull the PR code and just run:

`pip install -v . --no-build-isolation`

It will now auto set good/better MAX_JOBS than you can manually, most of the time. 

Peak total threads = MAX_JOBS * NVCC_THREADS (default to 4). Assume 5GB of worst case memory usage per thread. Use this formula, and your system/spec, to create a sane MAX_JOBS + NVCC_THREADS value. 

### rongjxxx · 2026-01-21

You can install built wheels from [Flash Attention Prebuilt Wheels](https://flashattn.dev). I succeeded with it.

### daniil-lyakhov · 2026-07-17

+1
