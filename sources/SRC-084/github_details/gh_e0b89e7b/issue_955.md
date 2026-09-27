# [Issue #955] Prodigy Optimizer

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/955
state: open | updated: 2026-03-31T16:32:48Z
labels: Feature Request, Optimizers

## 正文

### Feature request

Want to know if it is possible to implement [Prodigy](https://github.com/konstmish/prodigy) optimizer into bnb with 8bit support.

### Motivation

Prodigy is now widely used in FT since it is more user friendly especially for not-expert users. Who are also most not likely to have lot of knowledge about NN and good GPUS. 
And since Prodigy have 4 full size state, means it will consume a lot of vram. I think it is crucial to implement some kind of space optimization for prodigy. And I think bnb's 8bit optimizers are good  way for this goal.

### Your contribution

None, sry
I have read the source code and I think we will need to add a new "4state"(or even 5state) optimizer class. And since the thing need to be done is related to some CUDA things which is out of my ability.

If we can have some general template for optimizer which let us to just fill the logic inside of it. It may be ok for me to make PR for Prodigy or other optimizers.

## 评论 (4)

### DarkAlchy · 2024-03-07

Sure would be nice to get this as 8bit for sure as it is greatly needed.

### betterftr · 2024-04-02

Yes please!

### umarbutler · 2024-04-17

+1 I'd find this immensely useful seeing as Prodigy is already slower than AdamW.

### Xynonners · 2024-08-03

+1
