# [Issue #178] m_grouped_fp8_gemm_nt_contiguous stuck on matrix shape (1, 1,24576, 1536)

source: https://github.com/deepseek-ai/DeepGEMM/issues/178
state: closed | updated: 2025-09-01T08:56:47Z
labels: 

## 正文

Hi, there,

I am testing the kernel **m_grouped_fp8_gemm_nt_contiguous** with [group, m per group, N ,K ] = [1, 1, 24576, 1536] on H200. However, the program is stuck. Could you please advise on how to resolve this?

Many thanks!

## 评论 (3)

### LyricZhao · 2025-08-29

cc @zheanxu 

### zheanxu · 2025-08-29

Hi @lizhiqihhh, I tested m_grouped_fp8_gemm_nt_contiguous with the matrix shape [1, 1, 24576, 1536] and found it didn’t get stuck. In addition, this kernel assumes that the m of each group is aligned to 128; otherwise, it could cause low performance or other unexpected issues.

### lizhiqihhh · 2025-09-01

Thanks
