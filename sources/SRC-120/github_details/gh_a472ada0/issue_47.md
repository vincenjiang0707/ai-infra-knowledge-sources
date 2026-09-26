# [Issue #47] Triton Interpreter Mode

source: https://github.com/gpu-mode/lectures/issues/47
state: open | updated: 2025-01-27T14:12:11Z
labels: 

## 正文

lecture001, When I open the interpreter mode,
```
import os
os.environ["TRITON_INTERPRET"] = "1", 
```
Why the calculation result of square_kernel is wrong? my triton==3.1.0

## 评论 (1)

### goriri · 2025-01-27

Same for me. Triton 3.1.0. The result is all 0. Without the interpret, everything is fine.

> /opt/conda/envs/cuda-lecture/lib/python3.12/site-packages/triton/runtime/interpreter.py:412: RuntimeWarning: overflow encountered in multiply
  return TensorHandle(op(lhs.data, rhs.data), lhs.dtype.scalar)

> File "/home/ubuntu/lectures/lecture_001/triton_square.py", line 64, in <module>
    assert torch.allclose(y_triton, y_torch), (y_triton, y_torch)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: (tensor([[0., 0., 0.,  ..., 0., 0., 0.],
        [0., 0., 0.,  ..., 0., 0., 0.],
        [0., 0., 0.,  ..., 0., 0., 0.],
        ...,
        [0., 0., 0.,  ..., 0., 0., 0.],
        [0., 0., 0.,  ..., 0., 0., 0.],
        [0., 0., 0.,  ..., 0., 0., 0.]], device='cuda:0'), tensor([[8.5500e-01, 1.8092e-01, 6.9899e+00,  ..., 1.5783e-01, 1.9638e+00,
         1.7106e-02],
        [1.2770e-02, 1.2625e-01, 4.1180e+00,  ..., 3.6566e+00, 1.1336e-01,
         1.0602e-02],
        [2.8176e-01, 5.6156e-02, 5.1783e-01,  ..., 1.5356e-01, 2.2879e-03,
         8.8451e-01],
        ...,
        [1.0460e+00, 6.2929e-03, 2.6129e+00,  ..., 3.2305e+00, 5.9945e-01,
         5.3665e-01],
        [2.9018e+00, 2.2475e+00, 6.7073e-03,  ..., 7.2602e-02, 4.7163e-02,
         7.0590e-01],
        [2.2400e+00, 8.1350e-01, 6.8923e-01,  ..., 8.4767e-01, 3.7891e-01,
         1.2726e+00]], device='cuda:0'))
