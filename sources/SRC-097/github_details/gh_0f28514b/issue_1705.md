# [Issue #1705] nixl_ep installed to unnamespaced site-packages/nixl_ep/ by both cu12 and cu13 wheels, causing ImportError on CUDA 13 machines after pip upgrade

source: https://github.com/ai-dynamo/nixl/issues/1705
state: closed | updated: 2026-06-19T17:58:19Z
labels: NIXL EP

## 正文

## Bug

Both `nixl-cu12` and `nixl-cu13` write `nixl_ep_cpp.so` to the same unnamespaced `site-packages/nixl_ep/` location. Since the meta-package installs both unconditionally, whichever lands last wins. On CUDA 13 machines, if `nixl-cu12` installs last its binary clobbers the cu13 one, causing:

```
ImportError: libcudart.so.12: cannot open shared object file: No such file or directory
```

This broke all nixl integration CI in vLLM when 1.2.0 was released: vllm-project/vllm#44143

## Where

The clobber: https://github.com/ai-dynamo/nixl/blob/v1.2.0/examples/device/ep/meson.build

```python
py.install_sources(
    'nixl_ep/__init__.py',
    'nixl_ep/buffer.py',
    'nixl_ep/utils.py',
    subdir: 'nixl_ep',  # same destination for both cu12 and cu13
    pure: false,
)
```

## Fix

Change `subdir: 'nixl_ep'` to `subdir: 'nixl_cu12/nixl_ep'` / `subdir: 'nixl_cu13/nixl_ep'` based on CUDA version — same namespacing already used for `_bindings.so`. Or use pip environment markers on the meta-package so only one CUDA variant installs per machine.

## 评论 (1)

### wjabbour · 2026-06-19

Fixed in #1727, shipped in v1.3.0. The meta-dispatcher shim and namespaced install dirs (nixl_ep_cu12/nixl_ep_cu13) are exactly the approach described here.
