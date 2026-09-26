# [Issue #292] Performance anomaly of 2MBsize under Allreduce ring

source: https://github.com/NVIDIA/nccl-tests/issues/292
state: closed | updated: 2025-03-08T00:57:37Z
labels: 

## 正文

Hello NCCL maintainers and experts,

Thanks for your time! 

I am looking into a performance anomaly when running Allreduce (ring) with only Infiniband interconnect (i.e., NCCL_P2P_DISABLE=1, NCCL_SHM_DISABLE=1, NCCL_NET_DISABLE=0 ).

The testbed is 2 DGX-H100 boxes with 8 * 400G NICs under the same Rack:
<img width="2076" alt="Image" src="https://github.com/user-attachments/assets/1713d028-2900-4b41-a41f-d8f6a280f37e" />

This is my command:
<img width="860" alt="Image" src="https://github.com/user-attachments/assets/49e1f8cd-15d5-42a4-b446-712f95eb76e6" />

Results of NCCL_P2P_DISABLE=1, NCCL_SHM_DISABLE=1, NCCL_NET_DISABLE=0:

<img width="1338" alt="Image" src="https://github.com/user-attachments/assets/7ac7ee05-f03e-4300-a5e4-f5d2f85b2e8c" />

I also tried NCCL_P2P_DISABLE=0, NCCL_SHM_DISABLE=0, NCCL_NET_DISABLE=0:

<img width="1298" alt="Image" src="https://github.com/user-attachments/assets/da3e3031-46d6-4102-8b65-f5836cbafe48" />

When using only Infiniband, the 2MB result was particularly anomalous. After setting `NCCL_P2P_DISABLE=0` and `NCCL_SHM_DISABLE=0`, the 2MB result appeared to normalize, but the 1MB result still seemed somewhat abnormal.

I did not observe similar anomalies in either Allreduce (Tree) or Alltoall. Additionally, this issue does not appear to be caused by the number of QPs, as the same problem persists even when using only a single QP.


Best,
Zhongjie

## 评论 (3)

### kiskra-nvidia · 2025-03-07

What you are seeing are the effects of switching the protocols (NCCL_PROTO). NCCL probably switches from LL to LL128 for buffers larger than 2MB (and to SIMPLE for 128 MB and up). The transitions are determined at run time by a fairly simple model, and it looks like in this case it would've been better to switch over sooner. But, you know, better a little too late than too early -- people hate seeing dips in the above output!

### kiskra-nvidia · 2025-03-07

BTW, you can gain some insight into this process by running with `NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH,TUNING`.

### zhongjiechen · 2025-03-08

Hi, @kiskra-nvidia , Thank you for the clear explanation—it makes sense to me! Appreciate your help!
