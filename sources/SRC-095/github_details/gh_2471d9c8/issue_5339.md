# [Issue #5339] [CI] History Server E2E fails on every run: `quay.io/minio/minio` returns 401 for anonymous pulls

source: https://github.com/ray-project/kuberay/issues/5339
state: open | updated: 2026-09-25T11:58:09Z
labels: ci, P0, triage

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.

### KubeRay Component

ci, historyserver

### KubeRay Version

`master` 

### Environment

Buildkite job `test-history-server-e2e-nightly-operator` on kind ([build #17301](https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/17301#01a0d7a6-94a8-417d-9936-c750d23d3cf7))

### What happened + What you expected to happen

`TestCollector` and `TestHistoryServer` time out waiting for the MinIO pod to become Ready ([s3.go#L160](https://github.com/ray-project/kuberay/blob/3849337fde7f8429710b8a479e542c49125d2a2e/historyserver/test/support/s3.go#L160)):

```
s3.go:161: 
    Timed out after 300.001s.
    The function passed to Eventually failed at /workdir/historyserver/test/support/s3.go:160 with:
    Expected
        <bool>: false
    to be true
```

[`minio.yaml`](https://github.com/ray-project/kuberay/blob/3849337fde7f8429710b8a479e542c49125d2a2e/historyserver/config/minio.yaml#L50) uses `quay.io/minio/minio:latest`, which quay.io no longer serves to anonymous clients. On kind the pod stays in `ImagePullBackOff`:

```
Failed to pull image "quay.io/minio/minio:latest": ... unexpected status from HEAD request to https://quay.io/v2/minio/minio/manifests/latest: 401 UNAUTHORIZED
```

Master passed on 2026-09-22 ([#17282](https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/17282#01a0cb48-4b3f-46f5-a5c5-ed22bed6a59d)) and failed on 2026-09-25 ([#17301](https://buildkite.com/ray-project/ray-ecosystem-ci-kuberay-ci/builds/17301#01a0d7a6-94a8-417d-9936-c750d23d3cf7)). PRs fail the same way (e.g. #5200).

Expected: MinIO starts and the tests run.

### Reproduction script

```bash
docker pull quay.io/minio/minio:latest   # 401 Unauthorized
```

### Anything else

Proposed fix: swap the image in `minio.yaml`. The new image must include `sh`, `minio` and `mc` (the tests exec `mc` in the MinIO container), and it must be able to write `/data`. On kind, with only `image:` changed, both of these work with the `mc` commands the tests use. I haven't run the full e2e with them yet.

- `cgr.dev/chainguard/minio:latest-dev`
- `pgsty/minio:latest`

Or we can change to other s3 like storage

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!


## 评论 (3)

### chungen0126 · 2026-09-25

Hi @CheyuWu , would you be interested in switching to Apache Ozone as the S3-compatible storage backend?

​Apache Ozone provides full S3 compatibility, high scalability, and well-maintained container images that work well in CI/kind environments.

​If you'd like to explore this option, the Ozone community is very glad to collaborate and assist with any integration issues or requirements to make it work seamlessly for your tests.

See: https://ozone.apache.org/docs/quick-start/installation/docker

### CheyuWu · 2026-09-25

@machichima @win5923 WDYT

### machichima · 2026-09-25

I think Ozone is a good choice! Let's discuss with history server maintainer and hear their thoughts.

cc @KunWuLuan @chiayi 
