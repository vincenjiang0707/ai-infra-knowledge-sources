# [Issue #1586] why does the plain UCX backend export only one worker address?

source: https://github.com/ai-dynamo/nixl/issues/1586
state: closed | updated: 2026-05-19T14:08:24Z
labels: Network

## 正文

I have a question about the plain UCX backend.

From src/plugins/ucx/ucx_backend.cpp, it seems that when num_workers > 1:

1. The backend creates multiple local UCX workers when num_workers is set.
2. However, it appears to export only a single worker address:

- workerAddr = uws.front()->epAddr();
- getConnInfo() returns only workerAddr

3. On the remote side, loadRemoteConnInfo() seems to take that single exported address and make every local worker connect to it:

- loop over all local workers
- uw->connect(addr.data(), size)
- push each resulting endpoint into conn->eps

Is this intentional by design?

## 评论 (1)

### iyastreb · 2026-05-12

Good question! Yes, I would say this is intentional.
First, we may have different amount of workers on sender and receiver. This is quite typical use case actually, when for example we have 8 dedicated workers on prefill (to parallelize posting large RDMA batches) and a single worker on decode (which is enough, because it does not do any heavy tasks, just get notified once transfer is done).
With RMA the multi‑worker feature is about issuing parallelism on the initiator, not about sharding traffic across the target. Notifications are lightweight and delivered via AM always into worker 0

Regarding num_workers - by increasing this number on the sender side you can get more "shared" workers, that you can use to post transfers from multiple threads (in this case each shared worker is "attached" to a certain thread).
