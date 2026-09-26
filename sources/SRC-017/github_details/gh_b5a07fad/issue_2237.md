# [Issue #2237] [Issue]: Add IB GRH support (IBV_QPF_GRH_REQUIRED) for GIN / GDAKI

source: https://github.com/NVIDIA/nccl/issues/2237
state: closed | updated: 2026-08-10T00:11:54Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Share Your Debug Logs

Hello

Recently IB GRH support was commited to support IBV_QPF_GRH_REQUIRED portAttr flag in main NCCL IB network implementation https://github.com/NVIDIA/nccl/commit/a26a9fa96163bcdc4171d54ad7acafa7f0009c58

>  Add IB GRH support

That is sometimes required and documented in man page https://man7.org/linux/man-pages/man3/ibv_modify_qp.3.html

>        If port flag IBV_QPF_GRH_REQUIRED is set then ah_attr and
>        alt_ah_attr must be passed with definition of 'struct ibv_ah_attr
>        { .is_global = 1; .grh = {...}; }'.


I noticed that this support could also be added to GDAKI mode in net_ib/gdaki/gin_host_gdaki.cc.

With NCCL 2.30.7 I have this error on the multi GPU host with IBV_QPF_GRH_REQUIRED bit set on nccl-tests with "-R 2" option:

```
NCCL_DEBUG=INFO NCCL_P2P_DISABLE=1 NCCL_SHM_DISABLE=1 all_reduce_perf_mpi -t 2 -R 2
...
worker-0:862519:862553 [0] transport/net_ib/gdaki/gin_host_gdaki.cc:431 (gdakiConnectQp) NCCL WARN DOCA failure 21
worker-0:862519:862553 [0] NCCL INFO transport/net_ib/gdaki/gin_host_gdaki.cc:683 (ncclGinGdakiCreateContext) -> 2
worker-0:862519:862552 [1] transport/net_ib/gdaki/gin_host_gdaki.cc:431 (gdakiConnectQp) NCCL WARN DOCA failure 21
worker-0:862519:862552 [1] NCCL INFO transport/net_ib/gdaki/gin_host_gdaki.cc:683 (ncclGinGdakiCreateContext) -> 2
worker-0:862519:862553 [0] NCCL INFO transport/net_ib/gin.cc:287 (ncclGinIbGdakiCreateContext) -> 2
worker-0:862519:862553 [0] NCCL INFO gin/gin_host.cc:278 (ncclGinDevCommSetup) -> 2
worker-0:862519:862553 [0] NCCL INFO dev_runtime.cc:1244 (ncclDevrCommCreateInternal) -> 2
worker-0:862519:862553 [0] NCCL INFO sym_kernels.cc:498 (ncclSymkInitOnce) -> 2
worker-0:862519:862553 [0] NCCL INFO dev_runtime.cc:868 (ncclDevrWindowRegisterInGroup) -> 2
worker-0:862519:862552 [1] NCCL INFO transport/net_ib/gin.cc:287 (ncclGinIbGdakiCreateContext) -> 2
worker-0:862519:862552 [1] NCCL INFO gin/gin_host.cc:278 (ncclGinDevCommSetup) -> 2
worker-0:862519:862552 [1] NCCL INFO dev_runtime.cc:1244 (ncclDevrCommCreateInternal) -> 2
```

This unverified patch (change gpunetio address type from DOCA_VERBS_ADDR_TYPE_IB_NO_GRH to DOCA_VERBS_ADDR_TYPE_IB_GRH when port requires: port_attr.flags & IBV_QPF_GRH_REQUIRED) allows me to run nccl-tests in "-R 2" mode on that server:

```
diff --git a/src/transport/net_ib/gdaki/gin_host_gdaki.cc b/src/transport/net_ib/gdaki/gin_host_gdaki.cc
index 5565f64..5f2d409 100644
--- a/src/transport/net_ib/gdaki/gin_host_gdaki.cc
+++ b/src/transport/net_ib/gdaki/gin_host_gdaki.cc
@@ -366,8 +366,15 @@ static ncclResult_t gdakiCreateVerbsAh(struct gdaki_context* ctx, struct ibv_con
   DOCACHECK(doca_verbs_ah_attr_create(ib_context, &ctx->ah));

   if (ctx->port_attr.link_layer == IBV_LINK_LAYER_INFINIBAND) {
+    bool grhRequired = (ctx->port_attr.flags & IBV_QPF_GRH_REQUIRED) != 0;
+    enum doca_verbs_addr_type addrType =
+      grhRequired ? DOCA_VERBS_ADDR_TYPE_IB_GRH : DOCA_VERBS_ADDR_TYPE_IB_NO_GRH;
+
     DOCACHECKGOTO(doca_verbs_ah_attr_set_sl(ctx->ah, ib_sl), status, destroy_verbs_ah);
-    DOCACHECKGOTO(doca_verbs_ah_attr_set_addr_type(ctx->ah, DOCA_VERBS_ADDR_TYPE_IB_NO_GRH), status, destroy_verbs_ah);
+    if (grhRequired) {
+      DOCACHECKGOTO(doca_verbs_ah_attr_set_traffic_class(ctx->ah, ib_tc), status, destroy_verbs_ah);
+    }
+    DOCACHECKGOTO(doca_verbs_ah_attr_set_addr_type(ctx->ah, addrType), status, destroy_verbs_ah);
   } else {
     DOCACHECKGOTO(doca_verbs_ah_attr_set_traffic_class(ctx->ah, ib_tc), status, destroy_verbs_ah);
     DOCACHECKGOTO(doca_verbs_ah_attr_set_addr_type(ctx->ah, DOCA_VERBS_ADDR_TYPE_IPv4), status, destroy_verbs_ah);
```

### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.30.7

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (4)

### xiaofanl-nvidia · 2026-06-22

++ @bureddy @pakmarkthub to take a look if this suggestion makes sense & straight-forward to take in. 

### pakmarkthub · 2026-06-26

Hi @avnf ,

Thank you for reporting this bug. The proposed fix looks good but seems to be incomplete. Some other situations also require GRH. We will fix this issue in a future release.

### avnf · 2026-07-10

Original error was present with 2.30.7 and it is fixed after commit https://github.com/NVIDIA/nccl/commit/33c4db5635f089193f1b2715a70aa357e49d7e6d "Add logic to gin_host_gdaki.cc to detect and support GRH on IB network"

Thank you.



### xiaofanl-nvidia · 2026-08-10

Thanks for confirming. Closing this issue. 
