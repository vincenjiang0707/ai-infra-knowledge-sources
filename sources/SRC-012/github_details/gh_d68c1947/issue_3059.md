# [Issue #3059] [Question]  

source: https://github.com/mlc-ai/mlc-llm/issues/3059
state: closed | updated: 2026-03-01T20:43:57Z
labels: question

## 正文

## ❓ General Questions

<!-- Describe your questions -->

add the ability to load other models, except for those that are by default. Make a choice from the local storage. Is it possible to somehow limit the level of loading of the graphics core, to at least 90%, since when the model is running, the phone freezes completely, including stopping the interface update (I generally just have a clean screen, white).

## 评论 (3)

### ereish64 · 2024-12-12

I don't think CPU offloading is available at the moment (someone please correct me if I am wrong on this), however you can compile the model quantized so that it takes less memory (and processing power) if you haven't already. Try q4fp16 / 4 bit, floating point 16.

### alexdsh · 2024-12-16

so it's not the processor that's overloaded, but the graphics core., regarding the model, I use gemma2-2B q4fp16.mlc, it's already quantized to the maximum, besides, I also launched gemma2-7B-int1.gguf (though in another application where the processor calculates everything, without a gpu, it's Layla, but although it has an interesting "memory mapping" function implemented, allowing you to intelligently load model segments from swap when there's little physical memory. unfortunately, the model itself works strangely there, it writes outright nonsense. therefore, mlc chat suits me, but alas, it's enough for one, maximum 2 questions-answers, and then the application closes when it runs out of memory, neither zram 4 gb nor swap 4 gb on a flash drive helps. at least implement the same work with memory as Layla, plus the choice of your model and fix the work with the gpu so that the screen doesn't freeze, if you implement this, it would be  would be the best app for running models locally.thanks!

### Mawriyo · 2025-02-21

any relation to what we've experienced with freezes locally? 

https://github.com/mlc-ai/mlc-llm/issues/2894
https://github.com/mlc-ai/mlc-llm/issues/3131  

In terms of running models locally
https://github.com/mlc-ai/mlc-llm/issues/2733
