# [Issue #1798] nixl_ep_cpp fails to load against PyTorch 2.13: undefined symbol c10::impl::cow::materialize_cow_storage (rebuild needed)

source: https://github.com/ai-dynamo/nixl/issues/1798
state: closed | updated: 2026-09-14T12:36:38Z
labels: NIXL EP

## 正文

## Summary
The prebuilt `nixl-cu13` wheel's `nixl_ep_cpp` extension fails to import against **PyTorch 2.13.0**:

```
ImportError: /usr/local/lib/python3.12/dist-packages/nixl_ep/nixl_ep_cpp.cpython-312-x86_64-linux-gnu.so:
  undefined symbol: _ZN3c104impl3cow23materialize_cow_storageERNS_11StorageImplE
```
Demangled: `c10::impl::cow::materialize_cow_storage(c10::StorageImpl&)`.

This breaks every NixlConnector PD lane in vLLM's CI on the torch 2.13 upgrade branch.

## Root cause
- The nixl wheels link libtorch **dynamically** — `contrib/build-wheel.sh` runs `auditwheel repair --exclude 'libtorch*' --exclude 'libc10*' ...`, so torch symbols are resolved from the installed libtorch at load time. The `.so` is therefore tied to the torch ABI it was compiled against.
- `nixl_ep_cpp` (`examples/device/ep/csrc/nixl_ep.cpp`) does not call `materialize_cow_storage` directly; the symbol is **compiler-emitted** from torch's inline `torch::Tensor::data_ptr<T>()` (mutable storage access), used in ~21 places (e.g. `topk_idx.data_ptr<topk_idx_t>()`). On torch <= 2.12 that inline expands to a call to the out-of-line `c10::impl::cow::materialize_cow_storage(StorageImpl&)`.
- PyTorch **removed/renamed that symbol** in pytorch/pytorch#179063 ("Add pluggable MaterializeFn hook to StorageImpl", landed 2026-04-29) — COW materialization is now a pluggable `MaterializeFn` hook (`maybe_materialize()` / `materialize_cow(StorageImpl*)`, new `c10/core/StorageMaterializer.h`). The change landed on `main` (-> torch 2.13) after the `release/2.12` branch cut, so the symbol still exists in torch 2.12.x but is gone in 2.13.
- Result: `nixl-cu13` (built against a <= 2.12 torch ABI) references a symbol that torch 2.13's libtorch no longer exports -> `undefined symbol` at import.

## Affected versions
- nixl: **nixl-cu13 1.3.0** (latest on PyPI; also reproduces on prior releases)
- torch **2.13.0**, torchvision **0.28.0**, triton **3.7.1** (PyTorch **test** channel), CUDA **13.0**, Python **3.12**
- Works fine on torch 2.11/2.12 (symbol present).

## Reproduction
```bash
pip install torch==2.13.0 --index-url https://download.pytorch.org/whl/test/cu130
pip install --no-deps nixl-cu13==1.3.0
python -c "import nixl_ep"   # ImportError: undefined symbol ... materialize_cow_storage
```

## Request
There is currently **no `nixl-cu13` build (stable or nightly) compiled against torch 2.13** on PyPI or in GitHub releases. Could nixl:
1. Publish a build of `nixl-cu13` (`nixl_ep_cpp`) compiled against torch 2.13, and/or
2. Provide a **nightly** wheel built against the PyTorch **test/nightly** channel, so downstreams (vLLM) can validate upcoming torch releases ahead of GA?

No nixl source change is required — rebuilding against torch 2.13 headers routes `data_ptr<T>()` through the new materializer and the symbol resolves. This is purely an ABI/rebuild matter.

## References
- vLLM torch 2.13 test PR: https://github.com/vllm-project/vllm/pull/45731 (branch `atalman:test-pytorch-2.13.0-test`)
- Failing CI: vLLM Buildkite build [#72925](https://buildkite.com/vllm/ci/builds/72925) (2026-06-18) and [#72241](https://buildkite.com/vllm/ci/builds/72241) (2026-06-15)
- PyTorch ABI change: pytorch/pytorch#179063
- PyTorch-side tracking issue: pytorch/pytorch#187727


## 评论 (2)

### itayalroy · 2026-06-22

Thanks for the heads up @atalman, we are migrating NIXL EP to PyTorch stable ABI (https://github.com/ai-dynamo/nixl/pull/1793), which should solve this issue.

cc @ovidiusm @ofirfarjun7 regarding request to provide a test wheel with PyTorch 2.13 support so that vLLM could validate upcoming torch release ahead of GA

### ebarilanM · 2026-09-14

fixed https://github.com/ai-dynamo/nixl/pull/2093
