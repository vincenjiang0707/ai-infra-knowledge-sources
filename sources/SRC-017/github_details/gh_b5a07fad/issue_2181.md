# [Issue #2181] [Question]: Does NCCL have any plan to provide QP counter metrics of GDAKI 's QPs?

source: https://github.com/NVIDIA/nccl/issues/2181
state: open | updated: 2026-09-20T05:46:45Z
labels: question

## 正文

### Question

AFAIK, the QPs of GDAKI are finally created by DEVX, and we could not see any counters of DEVX's QP in `/sys/class/infiniband/mlx5_xxx/ports/1/hw_counters/` such as **out_of_sequence**, **req_cqe_error** and **local_ack_timeout_err**.  If we want to get the counter of DEVX's QPs, we should bind a qp counter set id to the QPs created by DEVX. Does NCCL have any plan to provide the QP counter metrics of GDAKI 's QPs so that we could easily observe the network issues when using GDAKI?

## 评论 (5)

### xiaofanl-nvidia · 2026-05-20

This is an interesting debuggability & observability idea. We will consider this. 

@baymaxhuang could you help describe how you could potentially consume the counters from your software stack and infra? 
E.g. would it be helpful to stream the counters via something like profiler/inspector? 

### baymaxhuang · 2026-05-20

@xiaofanl-nvidia Thanks for your reply. I think the QP counter could be shown like RAS subsystem and it could provide the following ability:
1. The user could observe the overall QP counter of each rank
2.  The user could watch the specific rank's QP counter every second
3.  The GDAKI subsystem could dump all the QP counters when the NCCL aborts so that we could find the relative network issue when the NCCL runs failure.

### xiaofanl-nvidia · 2026-05-20

@baymaxhuang Thanks for sharing the ideas. It is aligned with another debuggability feature we had in mind related to the net_ib NIC counters, which have been helpful in large scale debugging use cases. 

I'm adding @pakmarkthub and @armratner to further review & discuss. Pak/Armen - please file an internal RFE to track the idea if we have actionable & new features from this discussion. Thanks! 

### armratner · 2026-05-20

Hey @baymaxhuang, yes this is a good Idea, thank you, it does align well with another effort we have running to enable debuggability. we'll track internally and I'll make sure to keep you updated.

### nixnew657 · 2026-09-20

Our workaround creates a temporary RC QP through the standard libibverbs interface and transitions it to INIT with the target port. This allows the mlx5 kernel driver to populate the temporary QP’s QPC.counter_set_id with the port default Q-Counter ID.
We then use the QP-scoped DevX QUERY_QP interface, mlx5dv_devx_qp_query(temp_qp, ...), to retrieve counter_set_id from the returned QPC. The temporary QP and CQ are destroyed immediately after the ID is retrieved.
The retrieved ID is cached and explicitly programmed into each GDAKI DevX QP’s QPC during the RST2INIT_QP transition. An optional NCCL_GIN_GDAKI_Q_COUNTER parameter controls this behavior, with graceful fallback to the original DevX QP setup if discovery is disabled or unsupported.
Testing confirms hw_counters like rx_write_requests increasing.
Native DevX support for selecting or inheriting the default Q-Counter would still be preferable
