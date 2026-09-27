# [Issue #593] HIddensize alignment can be different in e8m0/non e8m0 mode?

source: https://github.com/deepseek-ai/DeepEP/issues/593
state: closed | updated: 2026-05-20T08:48:29Z
labels: 

## 正文

There is some alignment check in low latency dispatch
```
if (use_fp8) {
        // TODO: support unaligned cases
        EP_HOST_ASSERT(hidden % 512 == 0);
        if (not use_ue8m0) {
            packed_recv_x_scales = torch::empty({num_local_experts, hidden / 128, num_ranks * num_max_dispatch_tokens_per_rank},
                                                torch::dtype(torch::kFloat32).device(torch::kCUDA));
        } else {
            EP_HOST_ASSERT(round_scale);
            packed_recv_x_scales = torch::empty({num_local_experts, hidden / 512, num_ranks * num_max_dispatch_tokens_per_rank},
                                                torch::dtype(torch::kInt).device(torch::kCUDA));
        }
        packed_recv_x_scales = torch::transpose(packed_recv_x_scales.value(), 1, 2);
        packed_recv_x_scales_ptr = packed_recv_x_scales->data_ptr();
    }
```

I think `EP_HOST_ASSERT(hidden % 512 == 0);` can only be checked in `use_ue8m0` branch ?...

## 评论 (0)
