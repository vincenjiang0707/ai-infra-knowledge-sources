source: https://docs.vllm.ai/en/latest/api/vllm/compilation/breakable_cudagraph/
lastmod: 2026-09-23

#

`vllm.compilation.breakable_cudagraph`

[¶](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph)

Breakable CUDA graph capture/replay.

This is an alternative to :class:`CUDAGraphWrapper`

that replaces vLLM's torch.compile-based FX graph splitting with runtime stream-capture breaks.

The idea (inspired by sgl-project/sglang#19102): instead of pre-splitting the model into many pieces at attention boundaries, a single capture context drives the whole forward and intercepts attention / kv-cache custom ops at the dispatcher to end the current stream capture, run the op eagerly, and resume capture.

The captured artifact is a list of zero-arg callables -- the bound `CUDAGraph.replay`

for graph segments, or the user fn for eager segments -- replayed in order at inference time.

Eager segments must operate on the same static buffers used during capture so subsequent graph segments read the same memory addresses.

Classes:

-
–[BreakableCUDAGraphCapture](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphCapture)Stream-capture context that supports eager breaks via :meth:

`add_eager`

. -
–[BreakableCUDAGraphWrapper](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphWrapper)Drop-in replacement for :class:

`CUDAGraphWrapper`

that uses

Functions:

-
–[eager_break_during_capture](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.eager_break_during_capture)Decorator that turns a custom-op Python kernel into a "break point"


##

`BreakableCUDAGraphCapture`

[¶](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphCapture)

Stream-capture context that supports eager breaks via :meth:`add_eager`

.

Usage::

```
cap = BreakableCUDAGraphCapture(pool=...)
with cap:
output = model(*static_inputs)
# Later, after copying new inputs into the static buffers:
cap.replay()
# Output tensors live at the same addresses as during capture.
```


Thread-local: only one capture may be active per thread.

Methods:

-
–[add_eager](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphCapture.add_eager)End the current capture segment, run

`fn`

eagerly on the

## Source code in `vllm/compilation/breakable_cudagraph.py`


|
|

###

`add_eager(fn)`

[¶](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphCapture.add_eager)

End the current capture segment, run `fn`

eagerly on the capture stream, record `fn`

for replay, and start a new segment.

Returns whatever `fn`

returned during this (capture-time) call. Replay does not return values; callers should propagate any downstream dependencies via static output buffers.

## Source code in `vllm/compilation/breakable_cudagraph.py`


##

`BreakableCUDAGraphWrapper`

[¶](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphWrapper)

Drop-in replacement for :class:`CUDAGraphWrapper`

that uses :class:`BreakableCUDAGraphCapture`

instead of a single monolithic `torch.cuda.graph()`

capture.

Same dispatch contract as `CUDAGraphWrapper`

: * If no `forward_context`

is available, run the underlying callable eagerly. * If runtime mode mismatch / NONE, run eagerly. * Otherwise, lazily capture per `batch_descriptor`

and replay on subsequent invocations with the same descriptor.

When `runtime_mode`

is given, only that mode is captured/replayed; other non-NONE modes fall through, so the wrapper can be nested under a `CUDAGraphWrapper`

for another mode.

## Source code in `vllm/compilation/breakable_cudagraph.py`


|
|

###

`_collect_tensor_addresses(args, kwargs)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.BreakableCUDAGraphWrapper._collect_tensor_addresses)

Flatten tensor data_ptrs from positional and keyword args in a stable order (positionals first, then kwargs in insertion order).

Used for the DEBUG-mode address-stability check; covers both call styles since vLLM models are typically invoked with kwargs.

## Source code in `vllm/compilation/breakable_cudagraph.py`


##

`eager_break_during_capture(fn)`

[¶](https://docs.vllm.ai#vllm.compilation.breakable_cudagraph.eager_break_during_capture)

Decorator that turns a custom-op Python kernel into a "break point" for the breakable cudagraph capture.

When the decorated function is invoked outside of a :class:`BreakableCUDAGraphCapture`

context, it executes normally.

When invoked inside a capture context, it ends the current cudagraph segment, runs the function eagerly on the capture stream, records the callable for replay, and starts a fresh segment.

**In-place output buffer required.** Decorated ops must write into a caller-provided output tensor; a fresh tensor returned by `fn`

would change address each replay and break downstream graph segments.

**Decorator order matters.** Apply as the *outermost* decorator if there are other decorators that introduce host-side side effects around the call -- the canonical example is `@maybe_transfer_kv_layer`

for PD-disaggregation, whose `wait_for_layer_load`

and `save_kv_layer`

calls must run in the eager segment, not inside the captured cudagraph. Putting `@eager_break_during_capture`

*inside* such a decorator would record those side effects into the graph and hang on replay.

The correct order is::

```
@eager_break_during_capture # outermost
@maybe_transfer_kv_layer
def unified_attention_with_output(...):
...
```