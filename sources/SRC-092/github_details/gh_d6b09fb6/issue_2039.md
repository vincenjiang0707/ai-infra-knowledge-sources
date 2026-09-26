# [Issue #2039] [Bug]: Massive performance degradation when a replica fails in multi-node SGLang HiCache with Mooncake backend

source: https://github.com/kvcache-ai/Mooncake/issues/2039
state: open | updated: 2026-09-20T03:15:19Z
labels: bug, stale

## 正文

Hello!
We are constantly facing issues with multi-node SGLang HiCache deployments using the Mooncake backend.
Different root causes lead to the same behavior: massive performance degradation across all replicas.

## What can trigger the issue

### Replica tries to allocate previously used metadata port

We start up to 14 replicas with 8 clients each.

If any replica tries to use a port that was allocated earlier but is now free, or a port that is currently allocated, the following happens:

1. Mooncake on the client that failed to allocate the requested port correctly selects another port.
2. However, all other clients start performing put / get operations against the unacquired port on the host that attempted to acquire it, constantly producing logs like:

```
E0428 09:59:43.129539 12445 transfer_metadata.cpp:1154] Failed to find location of localhost:13292
E0428 09:59:43.129846 13043 transfer_metadata_plugin.cpp:290] GET http://commodity-llm-qwen35-397b-a17b-fp8-mooncake-58vblr.api-tinkoff-ai.mlc.region.local:8080/metadata?key=mooncake%2Frpc_meta%2Flocalhost%3A13292 http=404 body: metadata not found
E0428 09:59:43.130234 11886 worker_pool.cpp:244] Worker: Cannot make connection for endpoint: localhost:13292@mlx5_0, mark it inactive
```

We mitigated this behavior by limiting the port range in https://github.com/kvcache-ai/Mooncake/pull/2008.
We also noticed that this issue can sometimes resolve itself after approximately 15 minutes.

### Short-term RDMA failure

In our cluster metrics, we observe a momentary increase in TX Discards up to 30k and Buffer Overrun up to 5 on one of the IB connections.

At the same time, all SGLang clients produce several errors like this with fixed peer_nic:
```
E0505 16:29:11.891577 12891 worker_pool.cpp:296] Worker: Process failed for slice (opcode: 0, source_addr: 0x7f204ae9c000, length: 65536, dest_addr: 0x7f6bad588000, local_nic: mlx5_9, peer_nic: localhost:14278@mlx5_5, dest_rkey: 2099456, retry_cnt: 0): transport retry counter exceeded

E0505 16:29:11.910105 12891 transfer_metadata_plugin.cpp:961] SocketHandShakePlugin: connect()10.178.54.150:16031: Connection refused [111]

E0505 16:29:11.911362 12891 worker_pool.cpp:244] Worker: Cannot make connection for endpoint: localhost:14278@mlx5_6, mark it inactive

E0505 16:30:08.311306 13626 transfer_task.cpp:372] Failed to complete transfers after 60000 milliseconds for batch 139733003265520
```

Sometimes this failure does not trigger long-term degradation: the affected replica simply terminates, and after about a minute of degradation, everything returns to normal.

## How exactly everything fails

During any of the listed failures, all SGLang clients start producing logs like:

```
E0505 16:28:08.311199 13628 transfer_task.cpp:372] Failed to complete transfers after 60000 milliseconds for batch 140292222114192
Transfer failed for key: 9225425a53e4adc63ce56594f07801a848f485a091e78d1dfa8ea96e04daece0_1_v with error: -800

W0505 16:28:08.311417 13634 client_service.cpp:1125] lease_expired_before_data_transfer_completed key=127f0a721940725feec6e971654aa6dd8e0421cba46d2aa17a18433a15cfe305_5_v
E0505 16:28:08.311813 13634 real_client.cpp:3770] BatchGet failed for key '40bb36978db6ee7051e1d854166570d784e545f4f9a69bfb1fbd4c78bf3ad360_5_k': TRANSFER_FAIL

E0505 16:29:57.696182 13638 client_service.cpp:1705] Failed to finalize put for key 150ebb8c92561b506acbecc08d7e7f2b8887c580658e3bee9a0e70b1b1325b06_7_k: OBJECT_NOT_FOUND
E0505 16:29:57.696235 13638 client_service.cpp:1882] Operation for key b5b8bd39b8606db5da4ba5e17e7def2a20dd19f5d6092d381070104f835a2822_7_k failed: OBJECT_NOT_FOUND (OBJECT_NOT_FOUND: BatchPutEnd failed; )
[2026-05-05 16:29:57 TP7] Write page to storage: 128 pages failed.

E0506 07:34:31.795542 14256 real_client.cpp:3718] Query failed for key '6779a594949ce55c621e5a7fd9661f08a498f019f68778b49770943dd8263852_4_v': RPC_FAIL
```

And mooncake_master starts to produce logs like:
```
E0505 10:30:26.174233   201 rpc_service.cpp:1117] BatchPutRevoke failed for key[0] 'd9b810cc7d1d46ccfba8e614f36d64e3346b8c0de4b0e8b7a8570d7dd4f755bd_3_k': OBJECT_NOT_FOUND
E0505 14:52:10.662626   195 master_service.cpp:896] key=e75fec615b25ef5df84e15d7b718a5a4af102a3adf5e84660e07002cefea3f1d_7_k, error=object_not_found

ERROR    \^[[0m\^[[0K[192] [coro_connection.hpp:279] read error: Connection reset by peer, conn_id 10081

I0505 14:52:17.509413   182 master_service.cpp:3741] client_id=6505391507972573188-9897067433713881278, action=client_expired
```

As far as we understand, this means that cache transfer is effectively dead at this point: all replicas keep trying to send/receive data from a dead endpoint, blocking other activity.

We also suspect that, because the default transfer timeout is 60 seconds [here](https://github.com/kvcache-ai/Mooncake/blob/6487c6bb62952b4a4676654b4f3006457f0cc509/mooncake-store/src/transfer_task.cpp#L334)￼, the KV cache remains locked and cannot be evicted by SGLang. This then causes performance degradation on the SGLang side. 
We will try the patch from https://github.com/kvcache-ai/Mooncake/pull/2036 and check whether it reduces the degradation.

## Start configs

All nodes, except master, are connected via InfiniBands (mlx5_0 to mlx 5_11, where 5_1, 5_2, 5_7 and 5_9 are disabled ethernet)

<details>
  <summary>Our topology</summary>

From `python3 -m sglang.check_env`:

```
NVIDIA Topology: 
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3    NIC4    NIC5    NIC6    NIC7    NIC8    NIC9    NIC10   NIC11   CPU Affinity     NUMA Affinity   GPU NUMA ID
GPU0     X      NV18    NV18    NV18    NV18    NV18    NV18    NV18    PIX     PIX     PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     4,6,8,10,12      0               N/A
GPU1    NV18     X      NV18    NV18    NV18    NV18    NV18    NV18    NODE    NODE    NODE    PIX     NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     4,6,8,10,12      0               N/A
GPU2    NV18    NV18     X      NV18    NV18    NV18    NV18    NV18    NODE    NODE    NODE    NODE    PIX     NODE    SYS     SYS     SYS     SYS     SYS     SYS     4,6,8,10,12      0               N/A
GPU3    NV18    NV18    NV18     X      NV18    NV18    NV18    NV18    NODE    NODE    NODE    NODE    NODE    PIX     SYS     SYS     SYS     SYS     SYS     SYS     4,6,8,10,12      0               N/A
GPU4    NV18    NV18    NV18    NV18     X      NV18    NV18    NV18    SYS     SYS     SYS     SYS     SYS     SYS     PIX     PIX     PIX     NODE    NODE    NODE    1,3,5,7,9,11     1               N/A
GPU5    NV18    NV18    NV18    NV18    NV18     X      NV18    NV18    SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE    PIX     NODE    NODE    1,3,5,7,9,11     1               N/A
GPU6    NV18    NV18    NV18    NV18    NV18    NV18     X      NV18    SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE    NODE    PIX     NODE    1,3,5,7,9,11     1               N/A
GPU7    NV18    NV18    NV18    NV18    NV18    NV18    NV18     X      SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE    NODE    NODE    PIX     1,3,5,7,9,11     1               N/A
NIC0    PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS      X      PIX     PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS
NIC1    PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     PIX      X      PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS
NIC2    PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     PIX     PIX      X      NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS
NIC3    NODE    PIX     NODE    NODE    SYS     SYS     SYS     SYS     NODE    NODE    NODE     X      NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS
NIC4    NODE    NODE    PIX     NODE    SYS     SYS     SYS     SYS     NODE    NODE    NODE    NODE     X      NODE    SYS     SYS     SYS     SYS     SYS     SYS
NIC5    NODE    NODE    NODE    PIX     SYS     SYS     SYS     SYS     NODE    NODE    NODE    NODE    NODE     X      SYS     SYS     SYS     SYS     SYS     SYS
NIC6    SYS     SYS     SYS     SYS     PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS      X      PIX     PIX     NODE    NODE    NODE
NIC7    SYS     SYS     SYS     SYS     PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     PIX      X      PIX     NODE    NODE    NODE
NIC8    SYS     SYS     SYS     SYS     PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     PIX     PIX      X      NODE    NODE    NODE
NIC9    SYS     SYS     SYS     SYS     NODE    PIX     NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE     X      NODE    NODE
NIC10   SYS     SYS     SYS     SYS     NODE    NODE    PIX     NODE    SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE    NODE     X      NODE
NIC11   SYS     SYS     SYS     SYS     NODE    NODE    NODE    PIX     SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE    NODE    NODE     X 

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
  NIC3: mlx5_3
  NIC4: mlx5_4
  NIC5: mlx5_5
  NIC6: mlx5_6
  NIC7: mlx5_7
  NIC8: mlx5_8
  NIC9: mlx5_9
  NIC10: mlx5_10
  NIC11: mlx5_11
```

From `ibstat`:

```
CA 'mlx5_0'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001b2576
        System image GUID: 0x58a2e103001b2576
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 287
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001b2576
                Link layer: InfiniBand
CA 'mlx5_1'
        CA type: MT4125
        Number of ports: 1
        Firmware version: 22.38.1002
        Hardware version: 0
        Node GUID: 0x58a2e10300592a0c
        System image GUID: 0x58a2e10300592a0c
        Port 1:
                State: Down
                Physical state: Disabled
                Rate: 40
                Base lid: 0
                LMC: 0
                SM lid: 0
                Capability mask: 0x00010000
                Port GUID: 0x0000000000000000
                Link layer: Ethernet
CA 'mlx5_10'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001a691e
        System image GUID: 0x58a2e103001a691e
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 284
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001a691e
                Link layer: InfiniBand
CA 'mlx5_11'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001b2542
        System image GUID: 0x58a2e103001b2542
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 254
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001b2542
                Link layer: InfiniBand
CA 'mlx5_2'
        CA type: MT4125
        Number of ports: 1
        Firmware version: 22.38.1002
        Hardware version: 0
        Node GUID: 0x58a2e10300592a0d
        System image GUID: 0x58a2e10300592a0c
        Port 1:
                State: Down
                Physical state: Disabled
                Rate: 40
                Base lid: 0
                LMC: 0
                SM lid: 0
                Capability mask: 0x00010000
                Port GUID: 0x0000000000000000
                Link layer: Ethernet
CA 'mlx5_3'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001a690a
        System image GUID: 0x58a2e103001a690a
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 286
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001a690a
                Link layer: InfiniBand
CA 'mlx5_4'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001b25ae
        System image GUID: 0x58a2e103001b25ae
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 239
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001b25ae
                Link layer: InfiniBand
CA 'mlx5_5'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001b2586
        System image GUID: 0x58a2e103001b2586
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 238
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001b2586
                Link layer: InfiniBand
CA 'mlx5_6'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001b258a
        System image GUID: 0x58a2e103001b258a
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 285
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001b258a
                Link layer: InfiniBand
CA 'mlx5_7'
        CA type: MT4125
        Number of ports: 1
        Firmware version: 22.38.1002
        Hardware version: 0
        Node GUID: 0x58a2e1030059282c
        System image GUID: 0x58a2e1030059282c
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 100
                Base lid: 0
                LMC: 0
                SM lid: 0
                Capability mask: 0x00010000
                Port GUID: 0x0000000000000000
                Link layer: Ethernet
CA 'mlx5_8'
        CA type: MT4125
        Number of ports: 1
        Firmware version: 22.38.1002
        Hardware version: 0
        Node GUID: 0x58a2e1030059282d
        System image GUID: 0x58a2e1030059282c
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 100
                Base lid: 0
                LMC: 0
                SM lid: 0
                Capability mask: 0x00010000
                Port GUID: 0x0000000000000000
                Link layer: Ethernet
CA 'mlx5_9'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.41.1000
        Hardware version: 0
        Node GUID: 0x58a2e103001b25d6
        System image GUID: 0x58a2e103001b25d6
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 457
                LMC: 0
                SM lid: 1024
                Capability mask: 0xa751e848
                Port GUID: 0x58a2e103001b25d6
                Link layer: InfiniBand
```

</details>






SGLang command:
```bash
MOONCAKE_TE_META_DATA_SERVER="http://mooncake_master:8080/metadata" \
MOONCAKE_MASTER="mooncake_master:50051" \
MOONCAKE_PROTOCOL="rdma" \
MOONCAKE_GLOBAL_SEGMENT_SIZE="384gb" \
SGLANG_MOONCAKE_TRANS_THREAD="8" \
MC_LOG_LEVEL="WARNING" \
MC_TE_METRIC="1" \
MC_TRANSFER_TIMEOUT="5" \
MC_STORE_CLIENT_MAX_PORT="12363" \
MC_STORE_CLIENT_MIN_PORT="12348" \
python -m sglang.launch_server \
    --enable-hierarchical-cache \
    --hicache-storage-backend mooncake \
    --hicache-io-backend direct \
    --hicache-mem-layout page_first_direct \
    --hicache-write-policy write_through \
    --model /models/Qwen3.5-397B-A17B-FP8 \
    --enable-metrics \
    --log-level-http=warning \
    --host 0.0.0.0 \
    --port 8000 \
    --tp=8 \
    --kv-cache-dtype fp8_e4m3 \
    --mamba-scheduler-strategy extra_buffer \
    --mamba-full-memory-ratio=0.5 \
    --page-size 64 \
    --tool-call-parser=qwen3_coder \
    --speculative-algorithm=EAGLE \
    --speculative-num-steps=3 \
    --speculative-eagle-topk=1 \
    --speculative-num-draft-tokens=4 \
    --enable-flashinfer-allreduce-fusion \
    --mem-fraction-static=0.8 \
    --model-loader-extra-config='{"enable_multithread_load":"true","num_threads":64}' \
    --enable-cache-report
```

Mooncake master command:
```bash
mooncake_master --enable_http_metadata_server=true --eviction_high_watermark_ratio=0.95 --enable_metric_reporting=true
```

## 评论 (20)

### ykwd · 2026-05-06

Thanks for the detailed description and analysis. Seems like this is a serious bug. We will try to reproduce it. 

### riZZZhik · 2026-05-06

> Thanks for the detailed description and analysis. Seems like this is a serious bug. We will try to reproduce it.

Thanks!
We’re happy to help with anything that might be useful on our side.

### riZZZhik · 2026-05-06

Batch metrics from master during failure:

<img width="885" height="856" alt="Image" src="https://github.com/user-attachments/assets/4dd5f0c1-5328-4d1e-a897-83501fb77dbe" />

### riZZZhik · 2026-05-07

Hello!
We investigated the short-term RDMA failures in more detail, and almost all of them follow the same pattern.

First, according to the infrastructure logs, mlx5_10 InfiniBand on one of the 14 nodes did actually fail for a short time. During this period, TX Discards increased up to an integer overflow.

<img width="2300" height="306" alt="Image" src="https://github.com/user-attachments/assets/1127a962-7a33-4d44-8952-442b69c975f2" />

At that moment, the SGLang pod with the failed IB connection produced logs like:
```
W0506 07:33:46.083428 13050 worker_pool.cpp:419] Worker: Received context async event port error for context mlx5_10
# After 10 seconds
W0506 07:33:54.999851 12660 rdma_endpoint.cpp:325] Re-establish connection: EndPoint: local localhost:13062@mlx5_10, peer localhost:13050@mlx5_6
W0506 07:33:58.189013 2344 worker_pool.cpp:419] Worker: Received context async event client reregistration for context mlx5_10
```

And all other pods starts to produce logs like:
```
E0506 07:33:49.996039 12996 worker_pool.cpp:296] Worker: Process failed for slice (opcode: 0, source_addr: 0x7fb3ce4e8000, length: 65536, dest_addr: 0x7f461d0e0000, local_nic: mlx5_9, peer_nic: localhost:13058@mlx5_10, dest_rkey: 2097920, retry_cnt: 0): transport retry counter exceeded
W0506 07:33:54.808396 13679 rdma_endpoint.cpp:325] Re-establish connection: EndPoint: local localhost:12904@mlx5_3, peer localhost:13062@mlx5_10
```

Then everything goes as described in issue

### riZZZhik · 2026-05-07

Also, we found that about 10 seconds later, the pod with the failed IB connection produced this log 25 times, while other pods produced it 1–10 times:
```
W0506 07:33:57.805462 12572 rdma_endpoint.cpp:124] Outstanding work requests found, CQ will not be generated
```

We will test the patch from https://github.com/kvcache-ai/Mooncake/pull/1903

### riZZZhik · 2026-05-20

@ykwd @alogfans Hello!
Any luck with reproducing?

### riZZZhik · 2026-05-20

We analyzed the logs a bit more and suspect that the issue is related to the fact that all client pairs are handled independently.

In our case, if RDMA fails on a single node, this results in 104 × 8 = 832 unique client pairs, and each pair tries to establish a connection before eventually marking it as failed.

We also checked whether the issue depends on the number of clients and traffic volume.
As expected, the failure does not occur when running with fewer clients or lower traffic.

### alogfans · 2026-05-21

@riZZZhik Thanks for your reporting. We developed a mitigation that enables TTL for RPC meta caches #2173. We also improves TE's fault tolerance trying to prevent 60s delay #2155. We will further find better way to improve the stability if failures occurs.

### riZZZhik · 2026-06-01

@alogfans Hello!

Unfortunately, after updating to the latest main branch with patches from #2155 and #2173 applied, things became worse. Even a 64-GPU cluster started falling apart after very short RDMA failures.

The scenario is similar to what we observed before: InfiniBand briefly fails on 1 out of 8 nodes, starts dropping transfers, and then all clients disconnect from the master and are unable to reconnect.

However, the logs look different this time, and there are a couple of interesting points:

1. Based on our infrastructure dashboard and `async event port error` at 12:27:13.523017 and `Re-establish connection` at 12:27:17.096109 logs, mlx device was down for at most about 3.5 seconds
2. The Rail paused logs start appearing only after the connection has already been re-established
3. There may be a bug in recent commits or patches based on this log:

```
E0601 12:27:13.738561 12761 transfer_task.cpp:673] Failed to submit all transfers, error code is InvalidArgument
```

Logs:
[commodity-llm-qwen35-397b-a17b-fp8-xskbbz_cleared.log](https://github.com/user-attachments/files/28466435/commodity-llm-qwen35-397b-a17b-fp8-xskbbz_cleared.log)

### riZZZhik · 2026-06-01

And the thing that concerns us the most:
Even if everything falls apart and clients get disconnected, why are they unable to reconnect after some time?

SGLang keeps producing logs like:

```
E0601 17:50:09.856653 11657 master_client.cpp:344] RPC call failed: Connection timed out
E0601 21:13:57.370945 12338 client_service.cpp:3199] Reconnect failed to commodity-llm-qwen35-397b-a17b-fp8-mooncake-ty2emg.api-tinkoff-ai.mlc.region.local:50051: RPC_FAIL
E0601 17:50:09.856714 12372 client_service.cpp:3154] Failed to ping master
E0601 21:14:33.791967 12372 client_service.cpp:3194] Failed to ping master for 4 times (non-HA); reconnecting to commodity-llm-qwen35-397b-a17b-fp8-mooncake-ty2emg.api-tinkoff-ai.mlc.region.local:50051

E0601 21:13:51.401496 12788 client_service.cpp:1926] Operation for key ee2dc1951da6c70d8972d9834498411621cdceff03e1609aee2e790d494e7bd2_7_temporal failed: RPC_FAIL (RPC_FAIL: Master failed to start put operation; )
E0601 21:13:13.472844 12797 client_service.cpp:1926] Operation for key c0c5b26b59a1c0c6746b35182e978aea027dfd53643d2bb1a670de7969de04a6_5_v failed: OBJECT_NOT_FOUND (OBJECT_NOT_FOUND: BatchPutEnd failed; )
```

At the same time, the master produces logs like:

```
W0601 21:11:53.676295   190 rpc_service.cpp:1056] BatchPutStart failed for 256 keys due to insufficient space. Consider lowering eviction_high_watermark_ratio or mounting more segments.
E0601 21:12:21.393018   190 master_service.cpp:1369] Illegal client 13997564754658614030-17398728354431992470 to PutEnd key 6ac9acf86f6713f53677012485277366b85fe4c9539d23c185d7f28dbc2d7e60_1_k, was PutStart-ed by 9747701313135022099-5255769832715986316
I0601 21:12:27.651438   177 master_service.cpp:4951] client_id=3767515066912055192-13191642867204265902, action=client_expired
E0601 21:12:27.653406   190 rpc_service.cpp:1095] BatchPutEnd failed for key[215] 'a3e8d8a1e0284419e396eb84815cb30360ac66ba1000410a5b0e4643f9f28d2b_1_v': ILLEGAL_CLIENT
I0601 21:12:47.076556   177 master_service.cpp:5027] client_id=3767515066912055192-13191642867204265902, segment_name=localhost:13347, action=unmount_expired_mem_segment
E0601 21:12:47.076553   190 rpc_service.cpp:1095] BatchPutEnd failed for key[194] '73c774342e940e45974f8be51691f1667438a57c0db73b6ab897236fe542271f_7_k': OBJECT_NOT_FOUND
E0601 21:12:52.672272   188 master_service.cpp:1363] key=22deaaa5d2dac6e6e338c052f8709106fb958e0abb96bafd9e7ce9d4d0b698a2_6_v, error=object_not_found
```

_The full logs are up to 70 MB, so we were unable to attach them directly to GitHub. We can explore other ways to share them if needed._

<img width="906" height="1082" alt="Image" src="https://github.com/user-attachments/assets/b758377b-444c-471f-bce7-7bd67ac195fa" />

### riZZZhik · 2026-06-04

@alogfans @ykwd Hello!

Could you please take a look when you have time?

### Icedcoco · 2026-06-05

Thanks for the additional details. I have not reproduced this locally yet, so I do not want to claim a root cause from the partial logs.

From the snippets in this issue, we can see the following sequence of symptoms:

1. A short `async event port error` on one mlx device.
2. `transport retry counter exceeded` and `Re-establish connection` on other pods.
3. After applying #2155/#2173, `Rail paused` appears after the connection has already been re-established.
4. Clients later report `RPC call failed: Connection timed out`, `Failed to ping master`, and `Reconnect failed`.
5. Master logs then include `client_expired`, `unmount_expired_mem_segment`, `ILLEGAL_CLIENT`, `OBJECT_NOT_FOUND`, and `BatchPutStart ... insufficient space`.

The key missing piece is the exact ordering across the failed pod, other pods, and master. Could you share the logs for one failure window in one of these ways?

- upload a compressed archive to an external link, e.g. `.tar.gz` / `.zip`
- split the compressed log into several GitHub-attachable chunks
- or share only a filtered window from 1 minute before the first `async event port error` to 5-10 minutes after clients start failing to reconnect

The most useful files would be:

1. SGLang/Mooncake logs from the pod where the IB device failed
2. SGLang/Mooncake logs from 1-2 other pods that later failed to reconnect
3. mooncake_master logs for the same time range
4. the exact Mooncake commit used after applying #2155 and #2173
5. values of `MC_RPC_META_CACHE_TTL_SEC`, `MC_STORE_TRANSFER_TIMEOUT` / `MC_TRANSFER_TIMEOUT`, `MC_STORE_CLIENT_MIN_PORT`, `MC_STORE_CLIENT_MAX_PORT`, and whether `MC_RPC_PROTOCOL=rdma` is set
6. if possible, the infrastructure timestamps for IB down/up, TX Discards, and Buffer Overrun for the affected mlx device

For filtering, these patterns would be especially useful:

```bash
grep -E "async event|port error|client reregistration|transport retry counter exceeded|Rail paused|Re-establish connection|Outstanding work requests|Failed to submit all transfers|InvalidArgument|Failed to complete transfers|RPC call failed|Failed to ping master|Reconnect failed|client_expired|unmount_expired_mem_segment|Illegal client|BatchPutStart|BatchPutEnd|OBJECT_NOT_FOUND|ILLEGAL_CLIENT|insufficient space" <log>
```

The specific ordering I would like to verify is:

- first `async event port error`
- first `transport retry counter exceeded`
- first `Re-establish connection`
- first `Rail paused`
- first `Failed to submit all transfers, error code is InvalidArgument`
- first `Failed to ping master`
- first `Reconnect failed`
- first `client_expired`
- first `unmount_expired_mem_segment`
- first `ILLEGAL_CLIENT` / `OBJECT_NOT_FOUND`

This will let us narrow down which component reports failure first, without relying on guesses from partial logs.

### riZZZhik · 2026-06-05

@Icedcoco Hello!
I have attached logs from a recent failure with the latest #2155 commits applied.

1. [SGLang logs from the pod with failed IB](https://github.com/user-attachments/files/28630694/sglang-failed-j6derg_cleared.log.zip)￼
2. SGLang logs from other pods: [1-6qdcii](https://github.com/user-attachments/files/28630717/sglang-other-1-6qdcii_cleared.log.zip)￼, [2-56it2e](https://github.com/user-attachments/files/28630718/sglang-other-2-56it2e_cleared.log.zip)￼, [3-bvkj3j](https://github.com/user-attachments/files/28630719/sglang-other-3-bvkj3j_cleared.log.zip)￼, [4-z2upo8](https://github.com/user-attachments/files/28630720/sglang-other-4-z2upo8_cleared.log.zip) - this one completely failed after a short time
3. Mooncake master logs, split into two files: [part1](https://github.com/user-attachments/files/28630833/master-dqhsc7_cleared_part1.log.zip)￼, [part2](https://github.com/user-attachments/files/28630832/master-dqhsc7_cleared_part2.log.zip)￼
4. Exact commit: https://github.com/somnevaetsya/Mooncake/pull/1/changes
5. Environment variables on the SGLang side (min/max port are different for each serving):
```bash
MC_LOG_LEVEL=WARNING
MC_RETRY_CNT=3
MC_RPC_META_CACHE_TTL_SEC=5
MC_STORE_CLIENT_MAX_PORT=12539
MC_STORE_CLIENT_MIN_PORT=12524
MC_TE_METRIC=1
MC_TRANSFER_TIMEOUT=5
MOONCAKE_GLOBAL_SEGMENT_SIZE=550gb
MOONCAKE_PROTOCOL=rdma
MOONCAKE_MASTER=$address:50051
MOONCAKE_TE_META_DATA_SERVER=http://$address:8080/metadata
SGLANG_MOONCAKE_TRANS_THREAD=8
```
On master side:
```bash
mooncake_master \
  --enable_http_metadata_server=true --eviction_high_watermark_ratio=0.95 --enable_metric_reporting=true \
  --put_start_discard_timeout_sec=10 --put_start_release_timeout_sec=11 --max_retry_attempts=3 --pending_task_timeout_sec=10 --processing_task_timeout_sec=10
```
6. mlx5_5 was marked down around 17:02:30 for at most one minute.

<img width="1019" height="243" alt="Image" src="https://github.com/user-attachments/assets/3b5513ca-9dba-4be9-b585-cb3e2f1023d3" />

---

Mooncake metrics:

<img width="1176" height="1046" alt="Image" src="https://github.com/user-attachments/assets/6cdbcf1c-08bf-42b4-b839-98fc240c40c6" />

### Icedcoco · 2026-06-08

Thanks for the updated logs and the exact branch. I went through the failed pod logs, several peer pod logs, and the master logs for the same failure window.

From the current evidence, this looks like two connected problems rather than a single failure point.

The first part is the RDMA-side trigger. In the failed pod, the local RNIC reports `async event port error` for `mlx5_5`, then the corresponding RDMA context becomes inactive. Shortly after that, `submitTransferTask()` fails with `Device 4 is not active` / `InvalidArgument`.

One concrete issue here is that the submit path can keep using a request-level selected device even after that device has become inactive. In that case, it currently returns `InvalidArgument` instead of falling back to another active local device. We should fix this path so an inactive cached device is discarded and selection is retried against active devices when possible.

The second part is the recovery failure after the short RDMA event. The master logs show a large number of `client_expired` and `unmount_expired_mem_segment` events after the failure, while clients report `RPC_FAIL`, `Failed to ping master`, and `Reconnect failed`. In this run, the dominant remount failure appears to be `RPC_FAIL`; `UNAVAILABLE_IN_CURRENT_STATUS` / `UNMOUNTING` also appears, but it does not look like the main failure mode from the logs.

My current assumption is that the short RDMA failure creates transfer stalls, and the 60s store transfer wait increases RPC pressure on the master. Once some clients expire, master-side cleanup scans object metadata and holds per-shard locks, which can block normal Get/Put processing. With the default master RPC thread count (4), those blocked handlers can occupy the whole RPC thread pool, so even Ping/ReMount (which do not take metadata locks) are delayed and time out on the client side as RPC_FAIL. Since the client TTL (10s) is shorter than the default RPC request timeout (30s), a client whose Ping is stuck gets expired before its remount even returns, which triggers more cleanup and creates a self-sustaining recovery loop.

So the next fixes we are looking at are:

1. RDMA submit fallback when the selected local device is inactive.
2. Avoid sending redispatched slices back to paused rails.
3. Make the store transfer timeout configurable, since `MC_TRANSFER_TIMEOUT=5` does not appear to affect the current store transfer wait path.
4. Reduce the cost of master cleanup after client expiration, or move the expensive cleanup out of the critical recovery path.
5. Add more logs/metrics around cleanup time, remount result, and metadata republish result.

For a short-term validation, could you try running the same workload with a larger master RPC thread count, for example:

```bash
mooncake_master ... --rpc_thread_num=32
```

or another value appropriate for the master CPU count. This is not intended as the final fix, but it would help confirm whether RPC thread starvation is part of the long recovery failure.

If possible, please also run one reproduction with `MC_LOG_LEVEL=INFO`. With `WARNING`, several recovery-path events are hidden, especially successful remount and metadata republish logs. The most useful additional data would be the first `client_expired` timestamp after the RDMA event, the number of objects/keys in master metadata around the failure, and whether increasing `--rpc_thread_num` reduces `RPC_FAIL`, `client_expired`, and the later metadata 404 errors.

### riZZZhik · 2026-06-10

Hello!

We have tried increasing `rpc_thread_num` from default `4` to `32`, but it didn't resolve the issue

### Icedcoco · 2026-06-14

Thanks for testing this and sharing the result.

This is helpful for narrowing things down. It looks like increasing `rpc_thread_num` alone is not sufficient, so we will continue investigating the remaining failure/recovery paths.

We are still actively following this issue, testing the related scenarios, and working on fixes. We will keep this thread updated as we make progress.

Thanks again for the detailed reports and for helping validate the mitigation.

### riZZZhik · 2026-06-14

Hello, some good news.

We updated to a fresh `main` without any additional patches: https://github.com/kvcache-ai/Mooncake/commit/d95a93231ccdad0f0d0cdac7130da7250fabf048
The main issue seems to be resolved now :tada: 

However, the second issue still persists: after some failures, or after a long time without restarts, the master's RPC becomes unhealthy
Existing clients start receiving `RPC_FAIL`, while new clients trying to connect receive `-900`.

Related issue https://github.com/kvcache-ai/Mooncake/issues/456 and pr https://github.com/kvcache-ai/Mooncake/pull/2423

### riZZZhik · 2026-06-21

Hello!
Do you have any ideas why the Mooncake master RPC server can become stuck and stop processing any requests?

### Icedcoco · 2026-06-22

Hi @riZZZhik,

I do not have a confirmed root cause yet, so I would avoid calling this a fix at this point. The most likely direction I would check first is whether the master RPC server is stuck inside long-running handlers, or whether the coro_rpc accept/dispatch path itself becomes unhealthy.

Concretely, there are two cases we want to distinguish:

1. Handler saturation / stuck handlers: `mooncake_master_rpc_in_flight_requests` stays close to `mooncake_master_rpc_thread_pool_size` while clients get timeouts. That would suggest RPC workers are alive but occupied by handlers blocked on some internal path, for example metadata locks, cleanup, eviction, task/drain work, or another shared lock.
2. RPC server / connection path issue: `mooncake_master_rpc_in_flight_requests` stays low, but existing or new clients still fail to call `Ping` / `ServiceReady`. That would point more toward the RPC server dispatch / connection layer, process state, socket backlog, FD exhaustion, or something outside handler execution.

I prepared a small diagnostic branch based on current `main`:

https://github.com/Icedcoco/Mooncake/tree/issue2039-rpc-health-diagnostics

It keeps the existing RPC timeout capability from upstream `main` / #2423 and adds master-side RPC health gauges:

- `mooncake_master_rpc_thread_pool_size`
- `mooncake_master_rpc_in_flight_requests`

It also removes the earlier derived `queue_depth` idea, because that was not a real measurement of coro_rpc's internal queue.

To try it:

```bash
git fetch https://github.com/Icedcoco/Mooncake.git issue2039-rpc-health-diagnostics
git checkout FETCH_HEAD
```

Then build and run your usual deployment from that checkout. On the client / SGLang side, I would suggest setting bounded RPC timeouts so the logs can distinguish slow master responses from hard transport failures:

```bash
export MC_RPC_TIMEOUT_MS=5000
export MC_RPC_CONNECT_TIMEOUT_MS=2000
```

These values are only a starting point for diagnosis, not a recommended final production setting.

During the next reproduction, the most useful data would be:

1. Counts and first timestamps of `RPC_TIMEOUT` vs `RPC_FAIL` on clients.
2. The master metrics around the failure window, especially:
   - `mooncake_master_rpc_thread_pool_size`
   - `mooncake_master_rpc_in_flight_requests`
3. Whether `mooncake_master_rpc_in_flight_requests` stays near the thread pool size when new clients start receiving `-900`.
4. If possible, a `pstack` / `gdb thread apply all bt` from the master while it appears stuck.

This branch is intentionally narrow. It is meant to make the failure mode more observable and may reduce long client waits via the timeout settings, but it does not claim to fix the underlying reason why the master becomes unresponsive.

### github-actions[bot] · 2026-09-20

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
