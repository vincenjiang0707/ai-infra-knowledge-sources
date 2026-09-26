# [Issue #352] low latency test error with "dispatch_use_fp8 and round_scale and use_ue8m0"

source: https://github.com/deepseek-ai/DeepEP/issues/352
state: closed | updated: 2026-09-18T09:14:59Z
labels: 

## 正文

In file DeepEP/tests/test_low_latency.py, I added the code (Line 79-83 ):

 73                             # Check received data
 74                             if current_x is not x_pure_rand:
 75                                 recv_x = recv_x[:num_valid_tokens]
 76                                 recv_x_amin = recv_x[:, :-128].amin(dim=-1)
 77                                 recv_src_info = recv_src_info[:num_valid_tokens]
 78                                 assert torch.equal(recv_x_amin, recv_x[:, :-128].amax(dim=-1))
 **79                                 if dispatch_use_fp8 and round_scale and use_ue8m0 :
 80                                     recv_x_last = recv_x[:, -1]
 81                                     if (recv_x_last < -1).any():
 82                                         print(round_scale,use_ue8m0)
 83                                         print(f"rank {rank}, num_times {num_times}, expert_id: {expert_id}, recv_x_last contains values less than -1!, nu    m_valid_tokens: {num_valid_tokens}, recv_x_last: {recv_x_last}")**

When running the test with dispatch_use_fp8=True, round_scale=True, and use_ue8m0=True on GB200, the condition (recv_x_last < -1).any() is triggered (Line 83 ). This indicates that invalid negative values are appearing in recv_x_last, which should not happen.

Command：python DeepEP/tests/test_low_latency.py --num-processes 4 --num-tokens 768

## 评论 (2)

### shifangx · 2025-08-22

It has be fixed after [PR345](https://github.com/deepseek-ai/DeepEP/pull/345)
by changing from
                        x_scales = x_scales.view(dtype=torch.int8).to(torch.int) << 23
to
                        x_scales = x_scales.view(dtype=torch.uint8).to(torch.int) << 23

Root cause is that the function per_token_cast_back() in test case does not treat scale dtype correctly.
<img width="994" height="304" alt="Image" src="https://github.com/user-attachments/assets/e32f8a67-dbff-480e-9edf-4e13f69258d8" />


### polarstormx · 2026-09-18

This has been addressed in #345 (commit c5facf5), so closing as resolved.
