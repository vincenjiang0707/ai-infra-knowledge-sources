# [Issue #1261] Wrong doc and function signature for 8-bit optim

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1261
state: open | updated: 2026-08-28T04:45:27Z
labels: Documentation, Contributions Welcome, Optimizers

## 正文

### System Info

NA

### Reproduction

Argument `optim_bits` and `amsgrad` is not used for 8-bit Adam

https://github.com/TimDettmers/bitsandbytes/blob/dada530149212d64d4b69534716202659ef37ec8/bitsandbytes/optim/adam.py#L77-L95

The document for `optim_bits` is also wrong in this case, because we are using 8 bits here.

https://github.com/TimDettmers/bitsandbytes/blob/dada530149212d64d4b69534716202659ef37ec8/bitsandbytes/optim/adam.py#L107-L110

I'm thinking of 2 ways to solve this:
- Remove `optim_bits` and `amsgrad` arguments (actually even 32-bit Adam also doesn't use `amsgrad` argument)
- If we want to keep the function signature the same, there should be a check that `optim_bits == 8` and `amsgrad == False`

### Expected behavior

NA

## 评论 (5)

### nighting0le01 · 2024-10-24

? so does it always run in 8 bit?? @gau-nernst 

### gau-nernst · 2024-10-24

Yes, `Adam8bit` will always run in 8 bit. The `optim_bits` argument has no effect

### nighting0le01 · 2024-10-24

@gau-nernst i see, thanks also, did you notice any difference varying min_8bit_size? would it make sense to start with such a high value if your hidden dim ==4096 and only goes above in projection layers?

### gau-nernst · 2024-10-24

I didn't play around with that parameter.

### kritikagarg · 2026-08-28

Hi! I'd like to work on this issue.

Looking at the current state of the code, `Adam8bit` (and `AdamW8bit`, `PagedAdam8bit`, `PagedAdamW8bit`) already have validation guards that reject non-default values for `optim_bits` and `amsgrad`. However, the docstrings are still misleading — they describe these as functional parameters with a small "Note:" appended, rather than clearly marking them as deprecated.

I'm planning to:
1. Replace the misleading docstring entries with proper `.. deprecated::` directives that clearly state these params exist only for signature compatibility and will be removed
2. Add test coverage for the Adam8bit/AdamW8bit parameter guards (currently only LAMB8bit and Adagrad8bit have guard tests)

No breaking changes — the params stay in the signature for backwards compatibility, just properly documented as deprecated.

Happy to adjust the approach based on feedback.
