# [Issue #3342] [Bug] Phi-3.5-vision-instruct-q4f16_1-MLC runtime ValueError - llm weights are quantized but vision model weights are not

source: https://github.com/mlc-ai/mlc-llm/issues/3342
state: closed | updated: 2026-01-28T01:35:44Z
labels: bug

## 正文

## 🐛 Bug

I'm getting this error at runtime:

`ValueError: Cannot find parameter in cache: vision_embed_tokens.img_processor.vision_model.embeddings.position_embedding.q_weight`

I think this is because only the llm part is quantized, vision model is not. but the code is looking for quantized weights from the vision model.

 ```
grep "model.h.18.mixer.qkv_proj.q_weight" ndarray-cache.json -A10
                    "name": "model.h.18.mixer.qkv_proj.q_weight",
                    "shape": [
                        9216,
                        384
                    ],
                    "dtype": "uint32",
                    "format": "f32-to-bf16",
                    "nbytes": 14155776,
                    "byteOffset": 0
                },
                {

```

 ```
grep "vision_embed_tokens.img_processor.vision_model.encoder.layers.0.self_attn.q_proj.weight" ndarray-cache.json -A10
                    "name": "vision_embed_tokens.img_processor.vision_model.encoder.layers.0.self_attn.q_proj.weight",
                    "shape": [
                        1024,
                        1024
                    ],
                    "dtype": "float16",
                    "format": "f32-to-bf16",
                    "nbytes": 2097152,
                    "byteOffset": 12589056
                },
                {
```


## Environment

Jetson Orin Nano



## 评论 (3)

### tjsheth76 · 2025-09-19

@yashagar-cmu have you had a chance to look at this? any ideas?

### tjsheth76 · 2025-09-30

After further investigation- it is unlikely that this is an actual bug. Most probably, the issue arose bc I was using an outdated version of MLC on my jetson orin nano super. 

I will close it. 

### MasterJH5574 · 2026-01-28

Hi @tjsheth76, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
