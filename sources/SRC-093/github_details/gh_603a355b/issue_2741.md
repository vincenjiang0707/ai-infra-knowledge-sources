# [Issue #2741] [Bug] PodArray lazy indexing mutates shared snapshots concurrently

source: https://github.com/vllm-project/aibrix/issues/2741
state: closed | updated: 2026-09-17T23:06:39Z
labels: kind/bug, area/website

## 正文

### Description

`CustomizedRegistry` passes its cached `[]*v1.Pod` snapshot to `valuesProvider`, which stores the same slice in `PodArray.Pods`. `PodArray.initDeployments` later calls `sort.Slice(arr.Pods, ...)` in place while lazily constructing `deployments` and `podsByDeployment`.

A caller of `Indexes` or `ListByIndex` can therefore mutate the shared snapshot while another caller reads it through `All`. The check of `podsByDeployment` in `Indexes` and `ListByIndex` is also outside `arr.mu`, so concurrent first use reads fields while `initDeployments` writes them.

This remains after #2728: exact slice capacity prevents callers from appending into a published Registry snapshot, but it cannot prevent in-place element swaps by `sort.Slice`.

### Reproduction

The existing Ginkgo concurrency case reaches this race, but `pkg/utils/utils_test.go` has `//go:build !race`, so the suite entry is excluded by `go test -race`.

Temporarily remove that build constraint and run:

```console
go test -race -count=1 ./pkg/utils
```

The Ginkgo specs pass functionally, then the race detector reports conflicting accesses between:

- `PodArray.ListByIndex` and `PodArray.initDeployments`
- map reads from `podsByDeployment` and map construction in `initDeployments`
- reads of `deployments` and its publication in `initDeployments`

Production can reach the same pattern: `SLOQueue.Peek` calls `Indexes()` on the result of `ListPodsByModel`, while other request paths can call `All()` on the same `PodArray`.

### Expected behavior

`PodArray` supports concurrent readers without mutating a Registry snapshot that has already been published to other callers. Its lazy indexes are published only after complete initialization.

### Scope for a fix

A regression test should run as a standard Go `testing` test under `-race`, independently of the excluded Ginkgo suite. After the race is fixed, remove `//go:build !race` from `pkg/utils/utils_test.go` and verify the complete utils suite with:

```console
go test -race -count=1 ./pkg/utils/...
```

The other test entry points excluded in #1169 require separate investigation.

## 评论 (1)

### github-actions[bot] · 2026-09-17

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

