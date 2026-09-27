# Getting stupidly good results on my 4x3060ti setup.

source: https://www.reddit.com/r/LocalLLaMA/comments/1wqv9o8/getting_stupidly_good_results_on_my_4x3060ti_setup/
published: 2026-09-26T16:47:48+00:00

About a month ago I was having FOMO and was going to spend coin I don't really have on new graphics cards. Instead of doing that though I decided to spend the money on a new motherboard+cpu and try to utilize my 3060tis I had lying around from my old crypto miner.

Yes, I probably could have just sold the cards, but that would have got me what, $1000 max? Not even enough for a single 3090.

So I built my 4 gpu rig and have spent the past few weeks optimizing it, and found a pretty nice solution.

The key is tensor parallel. Lllama.cpp does not support it, so that led me to Turboderp's wonderful work on Exl3. I was able to get about 70 t/s on this model with MTP+196k context, and it works very well: [https://huggingface.co/erlidev/Swift-Qwen3.8-27B-EXL3/tree/SC_4.00bpw_H5_V6](https://huggingface.co/erlidev/Swift-Qwen3.8-27B-EXL3/tree/SC_4.00bpw_H5_V6)

Then I started getting greedy and was wondering if something better was out there. I found the HyperQwen repo which is meant for Ampere cards, and thankfully it supports TP=4 [https://github.com/syv-ai/HyperQwen](https://github.com/syv-ai/HyperQwen)

So with my new Vllm setup I then found this model which is "The [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) **fast-variant serving shape** of [ukisai/Swift-Qwen3.8-27b](https://huggingface.co/ukisai/Swift-Qwen3.8-27b) (the "reduced reasoning" finetune of Qwen3.8-27B), built entirely from Swift's own weights and outputs:" [https://huggingface.co/liamwh/Swift-Qwen3.8-27B-W4A16-syv-fast](https://huggingface.co/liamwh/Swift-Qwen3.8-27B-W4A16-syv-fast)

The results? At bf16 I can get 150k context window with about 120t/s. If I quantize kv8 it opens up the context to full 262k, but the speeds drop to about what I was getting with Exl3, around 70ish.

In summary, four 3060tis with a measly 8gb vram each, power-limited to 110w, and I can get either 1 agent blazing along at 120 t/s, or 2 concurrent agents with a big context window. Oh and concurrency has barely any slowdown at all.

Thank you for coming to my Ted Talk.