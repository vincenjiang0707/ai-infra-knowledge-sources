# [Issue #3646] Refactor: Decouple GMM kernel backend dispatch from quantization logic in MoE sparse_matmul

source: https://github.com/AI-Hypercomputer/maxtext/issues/3646
state: open | updated: 2026-04-14T15:32:11Z
labels: feature request

## 正文

### Feature or Model Request


  ## Problem

  The current MoE `sparse_matmul` implementation (`layers/moe.py`) and the underlying `megablox/ops.py` conflate two orthogonal concerns:

  1. **Quantization orchestration** — obtaining QWIX rules, quantizing lhs/rhs tensors
  2. **Kernel backend dispatch** — choosing between megablox Pallas, tokamax Pallas, or `jax.lax.ragged_dot`

  This leads to confusing control flow where `mblx.gmm()` acts as both a "quantization-aware GMM wrapper" and a "backend router" via the
  `use_tokamax_backend` flag. The megablox module shouldn't need to know about tokamax at all.

  ### Current call paths in `sparse_matmul` (simplified)

  ```python
  if use_tokamax_gmm:
      if quantization:
          mblx.gmm(..., use_tokamax_backend=True)   # megablox wraps tokamax?
      else:
          tokamax.ragged_dot(...)                     # direct tokamax call
  elif megablox:
      mblx.gmm(..., use_tokamax_backend=False)        # megablox native
  else:
      jax.lax.ragged_dot(...)                         # JAX fallback
  ```
  Issues:
  - mblx.gmm imports and calls tokamax_backend internally — megablox shouldn't depend on tokamax
  - Quantization logic is buried inside ops.py fwd/bwd functions (qpl.get_current_rule, qpl.quantize) rather than being a composable layer
  - 4 code paths in sparse_matmul with subtle differences in tiling, quantization, and dtype handling
  - Adding a new backend (e.g., Mosaic, Triton) requires modifying megablox internals

  Proposed Direction

  Separate the three concerns into composable layers:

  1. Backend interface — a common GmmBackend protocol with gmm() / tgmm() methods, implemented by megablox, tokamax, and ragged_dot backends
  independently
  2. Quantization wrapper — a standalone layer that handles qpl.get_current_rule / qpl.quantize and delegates the actual matmul to any backend
  3. sparse_matmul — selects backend based on config, wraps it with quantization if needed, calls it

  # Desired flow (conceptual)
  backend = get_backend(config)           # tokamax / megablox / ragged_dot
  if quantization:
      backend = QuantizedGmm(backend)     # wraps any backend with FP8 quantization
  output = backend.gmm(inputs, kernel, group_sizes, tiling)

  This would:
  - Remove tokamax imports from megablox
  - Make quantization composable with any backend
  - Simplify sparse_matmul from 4 branches to ~2 lines
  - Make adding new backends trivial

### Additional Context

_No response_

## 评论 (1)

### gobbleturk · 2026-04-14

These are great ideas, we will work on improving/refactoring, thank you! I agree with your desired flow
