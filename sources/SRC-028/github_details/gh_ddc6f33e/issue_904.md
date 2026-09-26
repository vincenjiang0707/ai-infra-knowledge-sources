# [Issue #904] Move maxtext docker images being built to artifact registry

source: https://github.com/AI-Hypercomputer/maxtext/issues/904
state: closed | updated: 2026-04-28T18:10:46Z
labels: enhancement

## 正文

Currently we are using `gcr.io` to store the docker images being generated ref: https://github.com/google/maxtext/blob/main/.github/workflows/build_and_upload_images.sh#L51

But with `gcr.io` being deprecated. We should move to Artifact Registry.

## 评论 (2)

### SauravMaheshkar · 2024-12-13

Might I also suggest moving all `*.Dockerfile` to some `docker/` dir. Might be a little pedantic but it's better code organisation and makes browsing easier.

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.
