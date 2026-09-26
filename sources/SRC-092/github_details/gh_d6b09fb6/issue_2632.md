# [Issue #2632] [Bug]: When Mooncake Store is running with offload enabled, offloading works correctly but a large number of offloading tasks expire after 600s, producing "Offloading task expired" warnings.

source: https://github.com/kvcache-ai/Mooncake/issues/2632
state: open | updated: 2026-09-25T03:14:16Z
labels: bug, stale

## 正文

### Bug Report

When Mooncake Store is running with offload enabled, offloading works correctly but a large number of offloading tasks expire after 600s, producing "Offloading task expired" warnings.

I tried to find the cause of the problem, but I haven't been able to pinpoint it.
```
W20260624 06:46:06.259191 381518 master_service.cpp:4716] Offloading task expired for key: a4c19c15ae875bfc15ae72d0ee8e79dc0a4b44678aac35b025d7407682fee187_3_v
W20260624 06:46:06.259195 381518 master_service.cpp:4716] Offloading task expired for key: 87b17efc3475633055bdabba14c2e5604d2bfb6dccb5ae680b3ed2a2ba46e168_3_k
W20260624 06:46:06.259200 381518 master_service.cpp:4716] Offloading task expired for key: 30e3c4277dcec6c441329500295f0a512330318cd14c9213641bba673d5d5cc3_3_v
W20260624 06:46:06.259205 381518 master_service.cpp:4716] Offloading task expired for key: 0e05a4c4854a1346768028d1f9426eed9539be61de24de721f1a0378a73a722e_2_k
W20260624 06:46:06.259209 381518 master_service.cpp:4716] Offloading task expired for key: de4e52aa62013c8f66a806d5ed957ab05cbd59160e88552c23e193467b3df224_2_v
W20260624 06:46:06.259214 381518 master_service.cpp:4716] Offloading task expired for key: 6722a24e361b4d398ef7c9ced19e13badc6e6d9f8f0da8b394784241d0d366cb_0_v
W20260624 06:46:06.259218 381518 master_service.cpp:4716] Offloading task expired for key: e86accfebc712b34f1c7412dd7c552d9b450c7743947bdae668d3e24b7af6a35_1_v
W20260624 06:46:06.259222 381518 master_service.cpp:4716] Offloading task expired for key: 746e9ac98efbbbe2bd523ef0814f9bc2c1eebb0847ab879145c68a253375f8fa_0_v
W20260624 06:46:06.259227 381518 master_service.cpp:4716] Offloading task expired for key: 109fba12aedd15db207d26b1c73a766428a89e61422237c798eff54605bcf80d_2_v
W20260624 06:46:06.259232 381518 master_service.cpp:4716] Offloading task expired for key: 1d892b63241624aa4e393496a5bad9bdc7c3a24f4843453323e2f182c6535327_2_k
W20260624 06:46:06.259236 381518 master_service.cpp:4716] Offloading task expired for key: f652d924bcb15a3406c4e0282c72811431b4e00b8e91982e0201334f64ae7500_3_v
W20260624 06:46:06.275416 381518 master_service.cpp:4716] Offloading task expired for key: f86e91a717815ebd6ac761433404548dc911c37e10c5fb20134c58ab9fff5f90_2_v
W20260624 06:46:06.275429 381518 master_service.cpp:4716] Offloading task expired for key: 4ca19d0a1f69800ab41c2214a31a20659c7ae031c71efa61fb7bf8aac363fc30_2_v
W20260624 06:46:06.275436 381518 master_service.cpp:4716] Offloading task expired for key: e1eb22b8e76c7ef0338938f8315fab6956d809d73fe945815cd0dd168c9075d6_0_v
W20260624 06:46:06.275441 381518 master_service.cpp:4716] Offloading task expired for key: d5115a486c3989e4a24f3bfeb347e1975beaa823d6c14a001a1badd4fc3275b2_3_v
W20260624 06:46:06.275446 381518 master_service.cpp:4716] Offloading task expired for key: cb6a3ecd20fb91eb79a15de0d59c7a2faeec8fc57b4235bf2f2965c5d811ef9a_0_v
W20260624 06:46:06.275450 381518 master_service.cpp:4716] Offloading task expired for key: cea4a8c000f00d9789723aade34e9afec959647ed85d921bc541c6cc35469566_3_k
W20260624 06:46:06.275455 381518 master_service.cpp:4716] Offloading task expired for key: 07c754e1846bb2a92dbf4c7c162dae024dfc272cec160aed39034bc9e63e6dd1_0_v
W20260624 06:46:06.275460 381518 master_service.cpp:4716] Offloading task expired for key: 2a73466e6f95babe6fbe844eaa6c8919d86eac7059fa94ee3e50fb1055333be7_2_v
W20260624 06:46:06.275466 381518 master_service.cpp:4716] Offloading task expired for key: 636bb02ed6068232790029db294389fdc64175ade42d6e82c0c1145a7e8b77e0_0_v
W20260624 06:46:06.275470 381518 master_service.cpp:4716] Offloading task expired for key: 445ab274b56d3edb271a6473c953fd56a14b9271d6b0eb3c44c7db56b305e0d0_3_k
W20260624 06:46:06.275475 381518 master_service.cpp:4716] Offloading task expired for key: d1c79d997eef5825590847291dd102e470852f18d49f419e81ca731f121c61e3_1_k
```



**Environment**: RDMA mode, sglang with 2 Store nodes, `enable_offload=true`, latest main branch.

Mooncake master：
```
nohup \
mooncake_master \
--eviction_high_watermark_ratio=0.95 \
--eviction_ratio=0.1 \
--rpc_address ${MASTER_IP} \
--rpc_port 50051 \
--rpc_thread_num=32 \
--enable_offload=true \
--enable_http_metadata_server=true \
--http_metadata_server_port=8080 \
--enable_metric_reporting=true \
--metrics_port 9013 \
 > mooncake_master.log 2>&1 &
```

Mooncake store:
```
export MOONCAKE_LOCAL_HOSTNAME="${NODE_IP}"
export MOONCAKE_TE_META_DATA_SERVER="http://${MASTER_IP}:8080/metadata"
export MOONCAKE_MASTER="${MASTER_IP}:50051"
export MOONCAKE_PROTOCOL="rdma"
export MOONCAKE_DEVICE="mlx5_0,mlx5_1"
export MOONCAKE_GLOBAL_SEGMENT_SIZE="8gb"

export MOONCAKE_OFFLOAD_FILE_STORAGE_PATH=/data1/mooncake_offload_test/
export MOONCAKE_OFFLOAD_STORAGE_BACKEND_DESCRIPTOR=bucket_storage_backend
export MOONCAKE_BUCKET_MAX_TOTAL_SIZE=$((512 * 1024 * 1024 * 1024))  
export MOONCAKE_OFFLOAD_TOTAL_SIZE_LIMIT_BYTES="${MOONCAKE_BUCKET_MAX_TOTAL_SIZE}"
export MOONCAKE_BUCKET_EVICTION_POLICY=fifo
export MOONCAKE_USE_URING=true
export MOONCAKE_OFFLOAD_LOCAL_BUFFER_SIZE_BYTES=$((2048 * 1024 * 1024))  
export MOONCAKE_OFFLOAD_HEARTBEAT_INTERVAL_SECONDS=2

nohup \
mooncake_client \
--master_server_address="${MOONCAKE_MASTER}" \
--host="${NODE_IP}" \
--port=10002 \
--protocol="rdma" \
--device_names="mlx5_0,mlx5_1" \
--global_segment_size="50GB" \
--enable_offload="true" \
--metadata_server="${MOONCAKE_TE_META_DATA_SERVER}" \
 > mooncake_store.log 2>&1 &
```

sglang:
```
python -m sglang.launch_server \
--model /data_merged/models/Qwen3-32B-FP8 \
--port 30000 \
--tp 4 \
--enable-metrics \
--enable-hierarchical-cache \
--enable-request-time-stats-logging \
--schedule-policy lpm \
--hicache-storage-prefetch-policy timeout \
--hicache-storage-backend mooncake \
--hicache-size 100 \
--host 0.0.0.0 \
--hicache-storage-backend-extra-config '{
  "master_server_address": "10.15.56.208:50051",
  "local_hostname": "10.15.56.196",
  "metadata_server": "http://10.15.56.208:8080/metadata",
  "global_segment_size": "17179869184",
  "protocol": "rdma",
  "device_name": "mlx5_0,mlx5_1"
}' 
```


### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (6)

### github-actions[bot] · 2026-06-26

Thanks for opening this issue, @Colors-111!

| Field | Value |
|-------|-------|
| **Issue** | #2632 |
| **GitHub user ID** | `70190328` |
| **Reporter** | @Colors-111 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### LujhCoconut · 2026-06-26

This might be related to the issue identified and resolved in this PR (#2599 ). I am also currently investigating this matter.

### Colors-111 · 2026-06-26

> This might be related to the issue identified and resolved in this PR ([#2599](https://github.com/kvcache-ai/Mooncake/pull/2599) ). I am also currently investigating this matter.

I tried running this PR with `--offloading_queue_limit=500000 --offload_cap_ratio=0.8`, but the problem persists; the logs did't change.
```
W0626 04:53:02.828492 99111 master_service.cpp:5091] Offloading task expired for key: 0561d03902afa675c0b87dd2a48c69ab1a9bbdea152c4fa2c0fb05d8cf839a3d_2_k
W0626 04:53:02.831647 99100 master_service.cpp:5091] Offloading task expired for key: 6b6d893c7bd7e0a90d6c787319d0f8bbcf8dac346fb841e6ac5fa8d4436c6636_3_k
W0626 04:53:02.835598 99104 master_service.cpp:5091] Offloading task expired for key: 83776cb487ea8c3435d50e9eeedb4808d59efb05530cf792f48e4b6df61bc63e_0_v
W0626 04:53:02.841516 99112 master_service.cpp:5091] Offloading task expired for key: 6aaf414b758115ef3abd40c257ef44869f03cafe1a168b475c0dd79c34008ab4_0_v
W0626 04:53:02.842445 99105 master_service.cpp:5091] Offloading task expired for key: a66a5c390979463f103117eff6f290feeedc6c0209c31550429039352567a7f6_1_v
W0626 04:53:02.844302 99108 master_service.cpp:5091] Offloading task expired for key: b982b6568394fa9274e2c41e508f74a94d6ff929de1c926316b00a88755cd879_2_v
W0626 04:53:02.844317 99108 master_service.cpp:5091] Offloading task expired for key: ad0a3ee41430f50d1362b7fce25e8f81aa10696682dd3453d5fa58dbcfc771e0_3_k
```

### LujhCoconut · 2026-06-26

I suspect the root cause may be that `FileStorage` maintains only a single heartbeat thread, while `OffloadObjects` processes each bucket sequentially and synchronously. 

```cpp
    heartbeat_thread_ = std::thread([this]() {
        LOG(INFO) << "Starting periodic task with interval: "
                  << config_.heartbeat_interval_seconds
                  << "s, running is: " << heartbeat_running_.load();
        while (heartbeat_running_.load()) {
            Heartbeat();
            std::this_thread::sleep_for(
                std::chrono::seconds(config_.heartbeat_interval_seconds));
        }
    });
```
>   Sequential heartbeat: a slow Heartbeat() delays the next offload fetch and lets offloading tasks exceed the 600s TTL.

```cpp
  for (const auto& keys : buckets_keys) {
      ...
      auto query_result = BatchQuerySegmentSlices(user_keys, tenant_id, ...);
      ...
      auto offload_res = storage_backend_->BatchOffload(...);
  }
```
> Buckets are processed serially, so a large batch keeps this thread busy and delays NotifyOffloadSuccess past the 600s TTL.

When a heartbeat cycle fetches a substantial volume of data, the processing time significantly exceeds the heartbeat interval, causing tasks to age in the queue and ultimately triggering the 600-second TTL expiration.

### Colors-111 · 2026-06-26

> I suspect the root cause may be that `FileStorage` maintains only a single heartbeat thread, while `OffloadObjects` processes each bucket sequentially and synchronously.
> 
>     heartbeat_thread_ = std::thread([this]() {
>         LOG(INFO) << "Starting periodic task with interval: "
>                   << config_.heartbeat_interval_seconds
>                   << "s, running is: " << heartbeat_running_.load();
>         while (heartbeat_running_.load()) {
>             Heartbeat();
>             std::this_thread::sleep_for(
>                 std::chrono::seconds(config_.heartbeat_interval_seconds));
>         }
>     });
> > Sequential heartbeat: a slow Heartbeat() delays the next offload fetch and lets offloading tasks exceed the 600s TTL.
> 
>   for (const auto& keys : buckets_keys) {
>       ...
>       auto query_result = BatchQuerySegmentSlices(user_keys, tenant_id, ...);
>       ...
>       auto offload_res = storage_backend_->BatchOffload(...);
>   }
> > Buckets are processed serially, so a large batch keeps this thread busy and delays NotifyOffloadSuccess past the 600s TTL.
> 
> When a heartbeat cycle fetches a substantial volume of data, the processing time significantly exceeds the heartbeat interval, causing tasks to age in the queue and ultimately triggering the 600-second TTL expiration.

I might find the root cause. `BatchQuerySegmentSlices` returned `ErrorCode::INVALID_KEY` if **even one key** in a tenant batch had no local memory replica. The caller in `OffloadObjects` skipped the entire tenant batch with `continue`. This is the dominant loss path because keys are queued for offload precisely due to memory pressure — by the time the worker processes them, some have already been evicted through the normal eviction path.

I'll try to validate this fix and submit a PR.

### github-actions[bot] · 2026-09-25

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
