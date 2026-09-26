# [Issue #1047] [CICD] Optimize kv cache image size

source: https://github.com/vllm-project/aibrix/issues/1047
state: open | updated: 2026-08-28T02:56:43Z
labels: help wanted, priority/important-longterm, area/cicd, area/installation, area/kv-cache

## 正文

### 🚀 Feature Description and Motivation

![Image](https://github.com/user-attachments/assets/d4b2c067-ce70-4e62-97e1-775484ea8ac1)

The image size is super large now, we need to reduce the size a little bit.

```
FROM ubuntu:22.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 python3-pip \
    iproute2 net-tools \
    ibverbs-utils libibverbs-dev \
    libnl-3-dev libnl-route-3-dev \
    rdmacm-utils libibverbs1 rdma-core \
    wget \
    && rm -rf /var/lib/apt/lists/*

#RUN pip3 install --no-cache-dir InfiniStore
# 
RUN wget https://test-files.pythonhosted.org/packages/f5/57/7013d0deee8b5a0e8cfd5a51bcc8be2084fc0ab8589586fb5e19687efe99/infinistore-0.2.41-cp310-cp310-manylinux_2_28_x86_64.whl
RUN pip3 install infinistore-0.2.41-cp310-cp310-manylinux_2_28_x86_64.whl

CMD ["infinistore"]
```

### Use Case

Reduce the container image size

### Proposed Solution

_No response_

## 评论 (4)

### Jeffwan · 2025-05-04

![Image](https://github.com/user-attachments/assets/45209eb9-98e0-4e54-9625-7df06ce0e3ae)

Seems the 2nd build for gid patch result in larger image.. But we only install `wget` and download the whl. whl is just 9MiB

### yyzxw · 2025-07-02

hi @Jeffwan  I want to solve this problem, but the describedin the issue is about `InfiniStore`. Is the Dockerfile for KVCache https://github.com/vllm-project/aibrix/blob/main/build/container/Dockerfile.kvcache?

or accturlly want to resolve `InfiniStore` image size?

Could you perhaps give me some guidance? thanks!

### Jeffwan · 2025-07-25

@yyzxw sorry for late response. `Dockerfile.kvcache` is not the right dockerfile. that's the image to sync kv cache information to redis. 

Here, we focus more on the infinistore image itself. I think we didn't check in the Dockerfile earlier. Could you create a new one instead? like `Dockerfile.infinistore`.  Please test the latest version the and version have issues.


### chlins · 2026-08-28

Hi @Jeffwan, I'd like to pick this up and add a `Dockerfile.infinistore` as suggested in the earlier comments.

I did some digging into why the image gets so large: `pip install infinistore` pulls in torch (2GB+) through its declared dependencies, but the server path (`server.py` / `lib.py`) never imports torch. It only needs uvloop / fastapi / uvicorn / numpy plus the bundled pybind extension. So the plan is roughly:

- `python:3.10-slim` base
- runtime-only RDMA packages (`libibverbs1`, `librdmacm1`, `ibverbs-providers`), dropping the `-dev` packages and debug tools
- `pip install --no-deps infinistore`, then install the actual server deps explicitly

That should bring the image from multiple GB down to the 300-400MB range. I'll include a before/after size comparison in the PR.

Two questions before I start:

1. Which version/source should the image track? PyPI latest is 0.2.35, this issue used 0.2.41 from test.pythonhosted, and the regression YAMLs reference an internal `infinistore:v0.2.42` image.
2. Do you want a Makefile/CI build target along with the Dockerfile, or just the Dockerfile for now?
