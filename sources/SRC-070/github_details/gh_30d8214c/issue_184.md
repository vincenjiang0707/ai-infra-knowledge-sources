# [Issue #184] performance optimizations  on CUDA 12.9?

source: https://github.com/deepseek-ai/DeepGEMM/issues/184
state: closed | updated: 2025-09-10T09:56:37Z
labels: 

## 正文

What performance optimizations were added in CUDA 12.9? 
I run test_fp8.py in the H20-96G using CUDA 12.8 and CUDA 12.9, the performance was consistent.
DeepGemm commit f85ec649d76846552cfd637b6c99fb9c985fd9eb
cuda 12.8:

<img width="800" height="515" alt="Image" src="https://github.com/user-attachments/assets/19bee47d-935a-44ed-9350-a19885482e2b" />

cuda12.9:

<img width="897" height="488" alt="Image" src="https://github.com/user-attachments/assets/a1166cb0-da5a-407e-9d42-0cc4664f09ad" />

## 评论 (1)

### LyricZhao · 2025-09-10

NVCC in CUDA 12.9 has an optimization for better tensor core/CUDA core overlapping. This will affect H800 (1979 peak TFLOPS) devices more. I guess as H20 has much lower peak TFLOPS, so it has no effect.
