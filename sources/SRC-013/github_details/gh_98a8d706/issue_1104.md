# [Issue #1104] Add UCCL to docker image

source: https://github.com/llm-d/llm-d/issues/1104
state: open | updated: 2026-09-14T01:23:41Z
labels: needs-maintainer-triage, lifecycle/stale

## 正文

Currently, The [Docker](https://github.com/llm-d/llm-d/blob/main/docker/Dockerfile.cuda) images contain UCX and NIXL build. 

Would be great to add [UCCL](https://github.com/uccl-project/uccl) transport built-in to the docker images so that vllm's NIXL Connector can be launched with UCCL backend to support efficient RDMA/TCP/TCP-X transfers.

Example Usage: 
```
    vllm serve <MODEL> \
      --port <PORT> \
      --tensor-parallel-size <TP_SIZE> \
      --enforce-eager \
      --block-size <BLOCK_SIZE> \
      --kv-transfer-config \
        '{"kv_connector":"NixlConnector","kv_role":"kv_both","kv_connector_extra_config":
        {"backends":["UCCL"]}}'
```

Refer to UCCL NIXL Support roadmap [here](https://github.com/praveingk/nixl/tree/uccl-local-xfer/src/plugins/uccl) 

## 评论 (3)

### Gregory-Pereira · 2026-04-09

cc @chcost and @maugustosilva were doin this right for 0.7?

### praveingk · 2026-04-14

PR #1136 

### github-actions[bot] · 2026-09-14

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
