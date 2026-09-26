# [Issue #1252] Validate llm-d with shared storage across multiple vendors

source: https://github.com/llm-d/llm-d/issues/1252
state: open | updated: 2026-09-11T01:17:11Z
labels: lifecycle/rotten

## 正文

## Summary

Validate and document llm-d running with shared storage across multiple vendors. The [tiered prefix cache storage guide](https://github.com/llm-d/llm-d/blob/main/guides/tiered-prefix-cache/storage/README.md) shows how to connect a storage connector (llm-d FS / LMCache) to a shared POSIX volume, but today only covers **GCP Lustre** as a concrete backend. We want to guide how llm-d works on other POSIX-backed storage systems, surface any implementation gaps, and extend the guide with a path per backend. Beyond functional validation, each backend should be configured for high-bandwidth access so the storage can sustain the throughput required for KV-cache reuse 

## Backends

- [ ] GCP Lustre - [existing guide](https://github.com/llm-d/llm-d/blob/main/guides/tiered-prefix-cache/storage/manifests/backends/lustre/README.md)
- [ ] IBM Storage Scale
- [ ] Azure
- [ ] AWS 
- [ ] VAST
- [ ] CephFS

## Scope per backend

- Provisioning (StorageClass / CSI) + RWX PVC.
- High-performance configuration for storage to sustain KV-cache reuse bandwidth.
- Smoke test: KV blocks written and reused across vLLM pods.
- Short TTFT + throughput benchmark.
- File any llm-d implementation issues uncovered during bring-up.

## 评论 (3)

### sudoalok · 2026-04-24

Hi @kfirtoledo , I’d like to take this up.
I’m planning to validate llm-d on AWS (EFS) first and document:
RWX PVC setup
vLLM multi-pod KV cache reuse
TTFT + throughput benchmarks
Let me know if that aligns with expectations or if you prefer another backend first.


### kfirtoledo · 2026-04-24

@alok7058 Sounds great, that's exactly the plan: documenting AWS EFS installation and adding performance recommendations like the GCP Lustre guide.

### github-actions[bot] · 2026-08-26

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
