# [Issue #2579] How Windows compile for 2.8.4 can take more than 7 hours on AMD Ryzen 9 - 9950X CPU with 4 threads?

source: https://github.com/Dao-AILab/flash-attention/issues/2579
state: closed | updated: 2026-06-02T16:58:10Z
labels: 

## 正文

I am compiling for CUDA arch list : 80; 86; 88; 89; 90; 100; 103; 120 for Torch 2.11 and CUDA 13.1 

Flash Attention version 2.8.4

It has been over 7 hours and still not completed

Build file is now 1.8 GB 

<img width="756" height="842" alt="Image" src="https://github.com/user-attachments/assets/c1f2d077-4bfc-49d9-97c3-081c026ccc15" />

<img width="1643" height="872" alt="Image" src="https://github.com/user-attachments/assets/37c80034-3067-49b0-b482-16a35e9d4579" />

<img width="1230" height="367" alt="Image" src="https://github.com/user-attachments/assets/73060cb0-0105-45be-bd01-1794b8460e4a" />



## 评论 (2)

### FurkanGozukara · 2026-05-21

12 hours still not done 

<img width="1653" height="743" alt="Image" src="https://github.com/user-attachments/assets/c37e5702-dafd-43ca-b7b1-a980f5cc619f" />

### FurkanGozukara · 2026-06-02

i compiled all but the issue is now that

when i compile a single package for all gpus, it exceeds 3.2 GB file size and it fails ultimately

this should be fixed

ty
