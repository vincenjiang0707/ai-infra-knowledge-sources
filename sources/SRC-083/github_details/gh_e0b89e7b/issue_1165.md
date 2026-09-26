# [Issue #1165] Stochastic rounding support for 8-bit optimizers

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1165
state: open | updated: 2026-03-31T16:32:49Z
labels: Low Priority, High Risk, Optimizers

## 正文

### Feature request

It would be extremely helpful to have stochastic rounding support, as described in [Revisiting BFloat16 Training](https://arxiv.org/pdf/2010.06192.pdf), for 8-bit optimizers.  This would require working with a full-precision set of model updates and a half-precision set of model parameters, and to randomly round up or down on the parameter update with a chance determined by the quantization error.  If implemented correctly, this should have minimal additional overhead and should perform similarly to full-precision training.



### Motivation

This would allow even more memory savings, where one could fit the entire set of model parameters and an 8bit optimizer in the same space as one full-precision copy of model parameters, or less than that if using 8bit Lion.

### Your contribution

Unfortunately, I don't know CUDA, and my understanding is that that would be required to implement this, since optimizer gradient transforms and parameter updates are all handled outside of Python in one inseparable process.

## 评论 (3)

### SirTrippsalot · 2024-04-29

I'd love to see this added. Greatly improves BF16 training results on other optimizers.

### wassname · 2025-01-27

example implementation here https://github.com/warner-benjamin/optimi

### TimDettmers · 2025-03-07

I actually tried this in experiments and it did not help. We are happy to bring this back, the implementation is not that complicated.

Right now we are a bit short on people hours for features like this and outside contributions would be very welcome for this.
