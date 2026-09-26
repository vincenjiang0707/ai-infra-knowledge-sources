# [Issue #3791] [Bug]: [ascendDirect] run mooncake-client standalone,--global_segment_size cannot over 32GiB，why?

source: https://github.com/kvcache-ai/Mooncake/issues/3791
state: closed | updated: 2026-09-23T02:07:06Z
labels: bug

## 正文

### Bug Report

**command**
mooncake-client --master=xxx --metadata_server="P2PHANDSHAKE" --host=xxx --global_segment_size="100GB" --port=xxx --protocol=ascend --thread=10

error:
<img width="959" height="327" alt="Image" src="https://github.com/user-attachments/assets/057390b3-366a-4dd6-ad12-45471e466ee1" />

**running health when global_segment_size <= 32GB**

**environment**
export ASCEND_AUTO_CONNECT=1
export ASCEND_GLOBAL_RESOURCE_CONFIG='{"comm_resource_config.protocol_desc": ["roce:device"]}'
export HCCL_INTRA_ROCE_ENABLE=1

910B(A2)，mooncake-master（v0.3.12.post1）、mooncake-client（v0.3.12.post1）

**reference docs**
https://gitcode.com/cann/hixl/wiki/Mooncake%20KVPool%E6%8C%87%E5%8D%97.md





### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-08-31

Thanks for opening this issue, @HyperionAdonis!

| Field | Value |
|-------|-------|
| **Issue** | #3791 |
| **GitHub user ID** | `20439311` |
| **Reporter** | @HyperionAdonis |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ascend-direct-dev · 2026-09-14

This looks like a HOST-memory **MR registration** limit on Device RoCE rather than a `mooncake-client` `--global_segment_size` bug.

On 910B (A2), registering HOST DRAM as RDMA MRs consumes device-side page tables. With older HDK (**< 25.5.0**), those page tables are built at **4KB** granularity, so a single NPU can typically register only ~20–32GB of HOST memory. That matches the symptom here: `global_segment_size` works at **≤32GiB** and fails at **100GB**. HDK **≥ 25.5.0** uses the host page-table granularity (2MB huge pages if available) and can register a much larger pool.

Please refer to:

1. [HIXL FAQ / troubleshooting guide](https://gitcode.com/cann/hixl/wiki/HIXL%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E5%AE%9A%E4%BD%8D%E6%89%8B%E5%86%8C.md) — especially **MR registration failure** and **ROCE HOST memory registration exhausting device system memory**
2. [Mooncake KVPool guide · HOST memory size limit](https://gitcode.com/cann/hixl/wiki/Mooncake%20KVPool%E6%8C%87%E5%8D%97.md#host-%E5%86%85%E5%AD%98%E5%A4%A7%E5%B0%8F%E9%99%90%E5%88%B6)

Could you please provide:

- **HDK version** (`npu-smi info`)
- **plog** from the failing `mooncake-client` process (typically under `$HOME/ascend/log/debug/plog`, or the path configured by `ASCEND_WORK_PATH`)

We currently suspect the HDK is too old to register that much HOST memory. If HDK is older than 25.5.0, please upgrade first. After that, for a very large pool, use huge pages as described in the KVPool guide (`MC_STORE_USE_HUGEPAGE=1` + reserved `nr_hugepages`).

Thanks!
