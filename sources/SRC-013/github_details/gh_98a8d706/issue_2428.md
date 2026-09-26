# [Issue #2428] [omni/diffusion support]: Route the async /v1/videos follow-up requests to the pod that owns the job

source: https://github.com/llm-d/llm-d/issues/2428
state: closed | updated: 2026-09-02T17:35:16Z
labels: 

## 正文

### Feature Area

Inference Scheduling

### Problem Statement

The OpenAI-compatible videos API is asynchronous. One logical operation is four HTTP requests:

1. `POST /v1/videos` creates a job and returns `{"id": "video_...", "status": "queued"}`
2. `GET /v1/videos/{id}` polls until `status` is `completed` or `failed`
3. `GET /v1/videos/{id}/content` downloads the result
4. `DELETE /v1/videos/{id}` cancels or deletes the job

Requests 2 to 4 only work on the pod that served request 1. Currently model servers like vLLM-Omni and SGLang store the video results in the model server itself and do not share them with other replicas.

But llm-d-router sends GET and DELETE to a random pod. These requests have no body. https://github.com/llm-d/llm-d-router/blob/ebc59e514b58eed1e6af796225f5786a3700a715/pkg/epp/handlers/request.go#L61

So with N video-serving pods, a poll is not guaranteed to reach the correct pod.

### Proposed Solution

**1. Track the job in llm-d-router.**

The EPP parses the `POST /v1/videos` response body, extracts the returned video id, and stores an internal map from video id to pod. Follow-up GET and DELETE requests extract the video id from the path and look up the map instead of falling back to a random endpoint.

- No backend change, transparent to clients.
- The map is lost when the router restarts, and running llm-d-router with replicas in active-active mode needs a shared store or client-to-EPP affinity. Entries also need TTL and eviction.
- Fixes routing only. If the backend pod restarts, the job is gone anyway.

**2. Shared job storage in vLLM-Omni and SGLang.**

Both backends persist the job record and the output content in storage shared by all replicas (shared volume, object store, or a small metadata store), so any replica can answer any GET or DELETE. The router keeps routing bodiless requests to any ready endpoint and stays stateless.

- Jobs survive pod restart and rescheduling.
- Needs a change in both backends plus a storage decision at deploy time on the model server side.



## 评论 (3)

### sudoalok · 2026-09-02

/assign


### zetxqx · 2026-09-02

@sudoalok I was meant to create the issue under llm-d-router https://github.com/llm-d/llm-d-router/issues/2663 can you check at there?

### sudoalok · 2026-09-02

sure, picked it up on #2663
