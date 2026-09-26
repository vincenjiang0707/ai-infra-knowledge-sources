# [Issue #1430] [Issue]: why does it take several hours to : Linking CXX shared library librccl.so    when make rccl ?   

source: https://github.com/ROCm/rccl/issues/1430
state: closed | updated: 2025-02-18T16:05:36Z
labels: Under Investigation

## 正文

### Problem Description

[Issue]: why does it take several hours to : Linking CXX shared library librccl.so    when make rccl ?    

### Operating System

ubuntu-24.04

### CPU

Intel(R) Core(TM) i7-14700K

### GPU

2x AMD Radeon RX GPU 7900XT

### ROCm Version

ROCm 6.2.3

### ROCm Component

HIPCC

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (6)

### thananon · 2024-11-22

Did you use `./install.sh` script?
You can cut a lot of build time by using `./install -l`, which will build RCCL only for your local GPU. Please make sure you use head of development branch as we just recently made a huge improvement in build time. For example, my build for local GPU is now ~2 minutes.

More info can be found with `./install.sh -h`.

### Jadenxxx-l · 2024-11-24

> Did you use `./install.sh` script? You can cut a lot of build time by using `./install -l`, which will build RCCL only for your local GPU. Please make sure you use head of development branch as we just recently made a huge improvement in build time. For example, my build for local GPU is now ~2 minutes.
> 
> More info can be found with `./install.sh -h`.

I have the same issue as well. I have tried using the ./install.sh -l script, and it did reduce some of the compile time, but the linking still takes around 10 minutes. You mentioned that there's been a recent improvement in build time; could you please let me know which specific commit this was implemented in? I'd like to give it a try. Thank you for your help!

### thananon · 2024-11-26

> the linking still takes around 10 minutes.

This is what we expected out of the current version for some GPU models. More build time optimization is our ongoing effort.


> could you please let me know which specific commit this was implemented in? 

There is a couple. The one I remembered is: https://github.com/ROCm/rccl/pull/1371. The general idea is that we were building kernels for every combination possible, some has multiple unroll variations and that takes a lot of time to link them together. We identified some of the kernels that were unnecessary and remove them. 

Another side note is that, if you are building for only a few collective ops, you can select to only rebuild those ops instead of all of them. You can also rebuild only for one datatype (say 32bits allreduce).


### etoilestar · 2024-12-24

I also encountered this issue. It keeps getting stuck when I compile inside the container. Have you resolved it?

### zichguan-amd · 2025-01-24

Hi @etoilestar, can you share more details about your container, GPU, and installation method? Using `./install.sh -l` in `rocm/dev-ubuntu-24.04:6.3.1-complete` with a 7900XTX takes approximately 5 minutes for me.

### zichguan-amd · 2025-02-18

Closing due to lack of recent activity. Please update if the issue persists.
