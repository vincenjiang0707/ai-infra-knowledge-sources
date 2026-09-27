# [Issue #51] Confuse about the estimated bandwidth on tests/test_internode.py

source: https://github.com/deepseek-ai/DeepEP/issues/51
state: closed | updated: 2026-09-18T10:16:17Z
labels: 

## 正文

We ran tests/test_internode.py on 2/4 H800-IB machines, and found that the estimated bandwidth sometimes can achieve up to 50GBps, which exceed the hardware capacity of NICs. SO we think if there is a mistake on bandwidth calculation. 

Can you confirm this issue or correct any errors in the following analysis?

---

We perform some tests, and it seems that the reason is that test_internode.py count the tokens to themselves as the `num_tokens_per_rdma_rank`, so the estimiated bandwidth is approximate (N_NODES / (N_NODES-1)) times to the real bandwidth.

We use `mlnx_perf -i ib1` to monitor the NIC rx_vport_rdma_unicast_bytes/tx_vport_rdma_unicast_bytes. The results seem to validate our assumption.

For example, in 2-H800 scenario, the program print the following:

```bash
# The original estimated bandwidth
[tuning] SMs 16, NVL chunk 20, RDMA chunk 4: 25.68 GB/s (RDMA), 83.83 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 8: 37.28 GB/s (RDMA), 121.69 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 12: 40.88 GB/s (RDMA), 133.43 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 16: 43.24 GB/s (RDMA), 141.14 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 20: 43.11 GB/s (RDMA), 140.71 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 24: 43.04 GB/s (RDMA), 140.48 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 28: 42.99 GB/s (RDMA), 140.33 GB/s (NVL)
[tuning] SMs 16, NVL chunk 20, RDMA chunk 32: 42.23 GB/s (RDMA), 137.85 GB/s (NVL)
[tuning] Best dispatch (BF16): SMs 16, NVL chunk 20, RDMA chunk 16: 43.24 GB/s (RDMA), 141.14 GB/s (NVL)
```

And the print of `mlnx_perf -i ib1` is the following: 

![Image](https://github.com/user-attachments/assets/1de600a3-60a5-4bee-9708-28a08f784c51)

173098/1024/8 = 21.13 GBps ~= 43.24 / 2

In 4-H800 scenario, we observe the estimated bandwidth is 51.98GBps, and the monitored bandwidth is about 37 GBps. 37/51.98 ~= 3/4.

![Image](https://github.com/user-attachments/assets/1effe0bf-7235-49d4-925d-61d10fe0d15c)

It seems that `dispatch` in internode.py does not utilize RDMA for intra-node communication, so that parts of tokens should not be calculated in num_tokens_per_rdma_rank.

We replace the original code with the following to correct the bandwidth estimation:

```python
# RDMA dispatch counts correction
rdma_idx = topk_idx // (num_experts // num_nodes)
rdma_idx.masked_fill_(topk_idx == -1, -1)
inplace_unique(rdma_idx, num_nodes) 
current_node = rank // num_local_ranks
mask = (rdma_idx != current_node) & (rdma_idx != -1)
num_rdma_token_sent = mask.sum().item()

# original codes
#rdma_idx = topk_idx // (num_experts // num_nodes)
#rdma_idx.masked_fill_(topk_idx == -1, -1)
#inplace_unique(rdma_idx, num_nodes)
#num_rdma_token_sent = rdma_idx.ne(-1).sum().item()
```


## 评论 (0)
