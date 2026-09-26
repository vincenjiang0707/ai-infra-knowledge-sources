# [Issue #8580] [Gluon] per-thread operations in gluon

source: https://github.com/triton-lang/triton/issues/8580
state: open | updated: 2026-09-01T18:09:34Z
labels: enhancement, documentation

## 正文

gluon, as a tile-based low-level GPU programming language, has a core advantage over other similar languages (such as tilelang and tilus): users can perform thread-level operations through **Linear Layout**, for example, softmax partial reduce in attention kernels. However, the current documentation and tutorials completely lack any content related to Linear Layout. Is there any plan from the maintainers to add content about thread-level operations based on Linear Layout?

### Example 1: Partial Reduce

Consider the following layout:

```Python
LinearLayout(
    bases={
    'register': [[0, 1], [8, 0], [0, 8], [0, 16], [0, 32], [64, 0]], 
    'lane': [[0, 2], [0, 4], [1, 0], [2, 0], [4, 0]], 
    'warp': [[16, 0], [32, 0]], 'block': []}, 
    out_dims={'dim0': 128, 'dim1': 64}
)
```

If this layout is a block layout (where each basis has at most one non-zero element), it can be represented as the following tensor (column-major):

```
[['register', 'lane', 'lane', 'register', 'register', 'register'], ['lane', 'lane', 'lane', 'register', 'warp', 'warp', 'register']]
```

This means that if we want to perform a partial reduce, we only need to reshape this tensor into the above shape and then call `gl.sum` on the axis corresponding to `register` in the column. This achieves a reduction only at the thread level. The generated PTX does not include any warp-level reduction.

To implement partial reduce, we also need to multiply the accumulator by the result of the partial reduce. However, broadcasting in Triton is special: the operands for broadcast must come from a reduction of the same tensor. Therefore, we solve this with code like the following:

```Python
@gluon.jit
def inline_reduce_broadcast(x, y, axes: gl.constexpr):
    keep_dims: gl.constexpr = False
    length: gl.constexpr = len(axes)
    # forward, x is only used for layout inference
    x_reduced = x
    for i in gl.static_range(length):
        x_reduced = gl.max(x_reduced, axes[length - i - 1], keep_dims=keep_dims)
    y1 = gl.convert_layout(y.reshape(x_reduced.shape), x_reduced.type.layout, assert_trivial=True)
    # backward
    for i in gl.static_range(length):
        y1 = y1.expand_dims(axes[i])
    return y1
```

The above code reproduces the reduction operation and then uses `expand_dims` to obtain operands that can be broadcast.

Attention example:
```Python
fake_qk = gl.zeros([BLOCK_M, BLOCK_N], dtype=gl.float32, layout=config.mma_qk_layout)
# register_1 means reduce all registers in column (dim 1)
fake_qk_thread_reduced = ll_ops.ll_reduce_sum(fake_qk, gl.constexpr(["register_1"]))
# use partial reduced l_i, final reduce is done after attn loop.
m_i = gl.zeros_like(fake_qk_thread_reduced) - float("inf")
l_i = gl.zeros_like(fake_qk_thread_reduced) + 1.0

...

for i in range(total_cnt):
    qk = ...
    m_ij = gl.maximum(m_i, gl.max(qk, 1))
    alpha = gl.exp2(m_i - m_ij)
    acc = ll_ops.ll_reduce_broadcast_mul(acc, alpha, gl.constexpr(["register_1"]))
    p = gl.exp2(ll_ops.ll_reduce_broadcast_sub(qk, m_ij, gl.constexpr(["register_1"])))
    l_i = l_i * alpha + ll_ops.ll_reduce_sum(p, gl.constexpr(["register_1"]))
    ...
```
### Example 2: Per-Thread Quantization

[Sage Attention](https://arxiv.org/pdf/2411.10958#page=4.80) describes a per-thread quantization method, where each thread maintains only one scale value to reduce the number of multiplications. In SageAttention’s CUDA implementation, the logic is hardcoded to achieve per-thread quantization for specific tensor cores. In gluon, we only need to convert the MMA layout to Linear Layout and then perform partial reduce/broadcast as in Example 1, without needing to understand any tensor core layout details.


## 评论 (6)

### lezcano · 2025-10-30

You are quite right that these are the sort of tricks that you can do in triton (and more!). For example, the layout inference you could implement yourself as a `gl.constexpr` function. Other tricks involve `gl.split` and the like.

This is a feature, in that you can implement all these things in the frontend without the need for more compiler operations, so if I understand your question correctly, then no, we are not going to add more operations to implement these tricks, as they can be implemented in the frontend :)

A different point is that gluon does not present the idea of "warp id" (other than in warp specialisation, but yeah) or "thread id" to the user, and we would like to keep it that way.

### lezcano · 2025-10-30

Oh, you meant indeed add these tricks to the tutorials. Well that's a fair point. cc @Mogball 

### bledden · 2026-02-25

I'd like to take a shot at writing this tutorial. The plan is to add `14-per-thread-ops.py` covering:

1. Converting layouts to `DistributedLinearLayout` via `gl.to_linear_layout` and inspecting them with `format_tensor_view`/`format_hardware_view`
2. Implementing register-only partial reduction by analyzing which tensor dimensions map to registers vs lanes/warps, then reducing only along register dimensions — no warp shuffles needed
3. The reduce-broadcast pattern from the issue (reproducing the reduction shape for broadcast compatibility)
4. Per-thread quantization following the SageAttention approach, where each thread maintains a single scale value

All implemented using existing Gluon primitives (`gl.split`, `gl.reshape`, `gl.reduce`, `gl.convert_layout`, etc.) as frontend-only patterns, consistent with the direction @lezcano outlined.

### ThomasRaoux · 2026-02-25

I'm not sure a tutorial specific to that is necessarily what we want. What is the goal?

### bledden · 2026-02-25

@ThomasRaoux sorry this PR was closed but I forgot to come back and delete the comment - I agree

### LeonxLJX · 2026-09-01

I'd like to take this one (`[Gluon] per-thread operations in gluon`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)
