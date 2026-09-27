# [Issue #1690] `bitsandbytes.functional.quantize_4bit`, `bitsandbytes.functional.quantize_blockwise` require contiguous input, fail silently if not

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1690
state: closed | updated: 2026-02-16T20:05:29Z
labels: 

## 正文

### System Info

Python 3.12.3, on an AWS P4 instance.

### Reproduction

Say I call `quantize_4bit` with `x` of shape `(a, b, c, blocksize)`. Call `num_ch = a * b * c`. I am getting `qx`, `state`, so that:

* `state.absmax.shape = (num_ch,)`
* `qx.shape = (num_ch * blocksize // 2,)`, `qx.dtype = torch.uint8`

My best guess was the memory layout of `qx` and `state.absmax` allows me to do `qx.view(a, b, c, blocksize // 2)` and `state.absmax.view(a, b, c)` and then work with that. But this does not seem to work.

```python
# x.shape = (4, 3, 38, 256)
qx, state = quantize_4bit(x, blocksize=256)
absmax_cmp = x.view(-1, 256).abs().max(dim=-1)
torch.testing.assert_close(state.absmax, absmax_cmp)

start, end = 10, 15
partx = x[:, :, start:end, :]
qx_part, state_part = quantize_4bit(partx, blocksize=256)
full = state.absmax.view(4, 3, 38)
part = state_part.absmax(4, 3, 5)
torch.testing.assert_close(full[:, :, start:end], part)

full = qx.view(4, 3, 38, -1)
part = qx_part.view(4, 3, 5, -1)
torch.testing.assert_close(full[:, :, start:end], part)
```

As it stands, this fails with the 2nd assert. But if I replace:

```
partx = x[:, :, start:end, :].contiguous()
```

Then, it all works. This means `quantize_4bit` does not work properly if its input is not contiguous. But it also does not check that, so things just fail silently.

### Expected behavior

I'd expect `quantize_4bit` and also `quantize_blockwise` either to check whether the input is contiguous, or to convert it to contiguous before quantization.

If I find some time, I submit a PR, which should also include a test that the example above works.

## 评论 (1)

### matthewdouglas · 2025-06-30

Thanks for the report. You're correct in that it's expected that the inputs are contiguous, particularly in the CUDA implementation. This is the case for more ops than just `quantize_4bit` and `quantize_blockwise`. I agree that we should either check for this and enforce this constraint, or handle it automatically.

Related issues: #1342 #1185 

Happy to accept a PR like #1187 on this! We'll try to squeeze this in otherwise.
