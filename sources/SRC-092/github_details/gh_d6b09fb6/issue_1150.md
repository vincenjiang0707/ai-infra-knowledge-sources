# [Issue #1150] [RFC]: [Mooncake - Master] Persistence and Recovery Solution for KV Metadata and Segment Information

source: https://github.com/kvcache-ai/Mooncake/issues/1150
state: closed | updated: 2026-09-17T03:15:01Z
labels: stale, auto-closed

## 正文

### Changes proposed

### Overview
This solution implements a persistence and recovery mechanism for Key information, Segment information, and memory allocator status of the Master node. It addresses the issue where all KVs are lost when a master - slave switchover occurs on the Master.

### Motivation
Currently, the high - availability deployment of the Master node can only ensure the "fast startup" of the service but fails to resolve the continuity problem of cached data. The core performance pain points are as follows:

1. **Performance Avalanche Caused by Cache Invalidation:** After the Master malfunctions, cached indexes such as KV metadata and Segment information are lost. The inference engine has to recalculate all requests in full, resulting in a sudden drop in performance and easily triggering a service avalanche.

2. **Slow Cache Reconstruction:** Even though the Master node can be started within seconds, the inference engine still takes several hours to complete the cache reconstruction.

### Detailed Design

<img width="2020" height="1956" alt="Image" src="https://github.com/user-attachments/assets/419fd8a5-aa2d-4909-9dcb-88ae5ddd99a0" />

This solution achieves the recovery of Master's KV metadata and Segment information through the "snapshot generation - storage - recovery" link. The core design is as follows:

#### Snapshot Generation Mechanism

1. **Efficient COW Copying:** Leveraging the Fork Copy - on - Write (COW) feature, it completes the memory copying of KV metadata and Segment structures within milliseconds without blocking the read and write operations of the core business.
2. **Asynchronous Serialization and Persistence:** The background persistence thread serializes the copied data structures into binary files and writes them to the storage service.
3. **Dirty Data Marking:** Record the evict_latest timestamp and the list of Keys involved in remove operations, and store them in association with the snapshot.

#### Snapshot Recovery Mechanism

1. **Deserialization and Restoration:** Retrieve snapshot files from the storage service and restore KV metadata and Segment information through deserialization.
2. **Dirty Data Cleaning:** Clean up invalid data based on the marked information: 
    Step1:Delete data with a timestamp less than or equal to evict_latest.
    Step2:Delete the Key entries recorded in the remove list.

#### Potential Drawbacks

1. With the method of periodically taking snapshots of all cache index information in the Master, when the Master restarts and recovers based on the snapshot information, the data generated during the interval after the snapshot cannot be recovered, and the newly written data after the snapshot will be lost.
2. For remove operations, a certain Key is immediately deleted from the client's perspective, but the actual release of the corresponding memory is processed asynchronously, which will have a delay.
3. Full - volume persistence is performed every time. As the scale of metadata managed by the Master continues to grow, both the time consumed for persistence and the size of snapshot files will increase.

### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (6)

### cocktail828 · 2025-12-02

@ykwd Could you please review this RFC?

### ykwd · 2025-12-02

Thanks for putting together this RFC. The proposal looks good to me. The snapshot-based persistence and recovery flow seems like a practical way to address cache loss during master failover. While there are some potential drawbacks listed in the proposal, such as full-volume persistence and potential data loss, based on this approach, we can gradually refine and improve the system in the future. For example, by exporting put and evict messages to mitigate these issues.

Looking forward to seeing the implementation in your PR!

### whybeyoung · 2025-12-11

nice work @zhunzhong  . I will follow up on this matter in accordance with our offline discussion in the coming days.

### gitgaoqian · 2026-06-10

I use mooncake v3.11.  Start mooncake master and standalone mooncake_client, And I launch a python client to put some kv.  When restart master，the snapshot would restore the segment,task_manager and metadata. but it would not restore metaserver data, so when i put key cache, it will return error. The error log can  be describe as:

W0609 06:23:22.044703  4115 transfer_metadata.cpp:894] Failed to retrieve segment descriptor, name 192.168.93.15:12352
E0609 06:23:22.044711  4115 transfer_task.cpp:552] Failed to open segment 192.168.93.15:12352


### github-actions[bot] · 2026-09-09

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-17

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.
