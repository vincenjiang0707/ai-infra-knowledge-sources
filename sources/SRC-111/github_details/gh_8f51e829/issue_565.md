# [Issue #565] Support multimodal synthetic data

source: https://github.com/vllm-project/guidellm/issues/565
state: open | updated: 2026-08-04T14:14:12Z
labels: priority-medium, internal

## 正文

**Is your feature request related to a problem? Please describe.**

Need to support synthetic generation of audio (video?) synthetic data

**Describe the solution you'd like**

Tie in mechanisms to synthesize data; e.g., text-to-speech.

## 评论 (2)

### ushaket · 2026-02-18

Adding some thoughts (specifically for ASR)

Adding a TTS capabilities doesn't seem like a viable option, for 2 reasons
1. It will introduce serious latencies
2. We'll probably need to save audio files with the report for reproducibility (not sure TTS is deterministic, if it is, maybe this is avoidable) 

As I see it there are 3 related features missing:
1. Concatenate audio inputs to get a longer data points - probably a real pain for users that want to benchmark on long inputs but their dataset contains short samples
2. Do something similar to text synthesis and bring "our own" audio file (or a few to get different speakers) to create datasets - Not sure why we need this other than ease of use
3. Augmentations -  noise, cross talk, reverb, frequencies filtering, pitch shift and more - This can give different "types" of synthetic datasets and can have presets like: "market", "office", "big hall", "telephone" etc..

### sjmonson · 2026-02-18

Neither of the TTS concerns seem valid to me. We do not need to use "AI" for TTS. Some TTS implementations date back to the 1950s and are extremely efficient. Plus there would be no concern for reproducibility.

For the missing features, these seem like preprocessing and not synthetic data. We have a `preprocess` submodule in GuideLLM which can do (1) and (2) for text so it may make sense to extend that to audio as well. However, I do not see these as blockers to synthetic (I also would like to lean away from building these kind of things into GuideLLM rather than in its own tool, but that is a separate debate).
