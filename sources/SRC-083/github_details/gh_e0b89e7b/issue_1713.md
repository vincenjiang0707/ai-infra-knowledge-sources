# [Issue #1713] Percentile Clipping causes FutureWarning

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1713
state: closed | updated: 2026-02-21T20:27:35Z
labels: Documentation, Contributions Welcome, Optimizers

## 正文

When percentile clipping is set to a value below 100 it triggers a future warning as the underlying method used to calculate the clipping values has been marked as deprecated: https://github.com/bitsandbytes-foundation/bitsandbytes/blob/14147f6f4aacc217f207b11a97b3ef7c7da57763/bitsandbytes/functional.py#L1395

May I ask why this is? Is percentile clipping itself slated for removal?

## 评论 (2)

### matthewdouglas · 2025-07-21

Thanks for the feedback!

Yes, percentile clipping itself is deprecated. We could make this more clear with a warning in the optimizers. Setting `block_wise=False` is a similar situation where we have marked a function it uses as deprecated in `bitsandbytes.functional` but it may be more clear if we warned when initializing an optimizer with it.

### TimDettmers · 2026-02-21

Closing this as resolved. As matthewdouglas confirmed, percentile clipping is deprecated, which is why the underlying function triggers a FutureWarning. This is by design. A clearer deprecation warning at optimizer initialization time would improve the UX, but the behavior is intentional.
