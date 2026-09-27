# [Issue #38] torch cpu only?

source: https://github.com/dropbox/hqq/issues/38
state: closed | updated: 2024-05-13T14:02:58Z
labels: question

## 正文

Hi,

I've tried adding a few `device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')` replacements for `device=device` or `device="cuda"` in `hqq/models/base.py` or `hqq/core/quantize.py`, the main error I am seeing now is that the calls to `self.stream_* = torch.cuda.Stream(*)` in `hqq/core/quantize.py:HQQLinear.__init__()` error out with the `Stream()`'s `super()` call going to a dummy base class.

My guess is that the `Stream` has no practical meaning on `torch_cpu`, so it would be either necessary to persuade the torch maintainers to handle that, or (assuming that streams are just the tip of the iceberg) adapt the HQQ code to work without cuda GPU when there is only torch_cpu?

CPU-only seems a worthwhile objective, especially as the models themselves are increasingly small

## 评论 (5)

### mobicham · 2024-04-02

It was only tested on GPU. It could work on the CPU if you use the ```PYTORCH_COMPILE``` backend and pass ```compute_dtype=torch.float32```, ```device='cpu'``` to ```from_quantized```. 

But that would only work on pre-quantized models, because quantization is solving an optimization problem and the code was designed to do it on the GPU (using fp16 which doesn't work on CPUs). 
Not tested, let me know if that works!



### MarkBenjamin · 2024-04-02

That definitely sounds worth a try, watch this space 🙂

### mobicham · 2024-05-13

By the way, you can run on CPU now: https://github.com/mobiusml/hqq/issues/74

### MarkBenjamin · 2024-05-13

Awesome thanks :-) as you may have noticed I just don't seem to have had the bandwidth recently to try to make the adjustments myself

### mobicham · 2024-05-13

Sure, let me know if you need anything else!
