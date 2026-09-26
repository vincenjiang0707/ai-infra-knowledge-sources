source: https://github.com/vllm-project/guidellm/compare/main...release/0.6

## Summary
Upgrade torch and torchcodec dependencies for RHAI 3.5 compatibility
## Details
We want to release a GuideLLM container image for RHAI 3.5, supporting full multimodal testing. However, RHAI 3.5 provides torch 2.11.0 and torchcodec 0.11.0, while GuideLLM 0.6.0 requires torch 2.10 and torchcodec 0.11.
This upgrades the dependencies.
## Test Plan
Manually run the audio, image, and video workloads against Qwen/Qwen3-0.6B model (which I had running) as well as Qwen/Qwen3-VL-2B-Instruct (referenced by documentation).
- [x] uv run guidellm benchmark --target http://*.example.com --request-type audio_transcriptions --profile synchronous --max-requests 20 --data openslr/librispeech_asr --data-args "{\"name\": \"clean\", \"split\": \"test\"}" --data-column-mapper "{\"audio_column\": \"audio\"}"
- [x] uv run guidellm benchmark --target http://*.example.com --request-type chat_completions --profile synchronous --max-requests 20 --data "lmms-lab/MMBench_EN" --data-args "{\"split\": \"test\"}" --data-column-mapper '{"image_column": "image", "text_column": "question"}'
- [x] uv run guidellm benchmark --target http://*.example.com --request-type chat_completions --profile synchronous --max-requests 50 --data "lmms-lab/Video-MME" --data-args "{\"split\": \"test\"}" --data-column-mapper '{"video_column": "url"}'
In this case the results (and ultimate success) are interesting but not really the point: it does not appear that the torch/torchcodec package upgrade caused problems in GuideLLM orchestration.
## Related Issues
[https://redhat.atlassian.net/browse/AIPCC-16597](https://redhat.atlassian.net/browse/AIPCC-16597)
---
- [x] "I certify that all code in this PR is my own, except as noted below."
## Use of AI
- [ ] Includes code generated or substantially modified by an AI agent
- [ ] Includes tests generated or substantially modified by an AI agent
> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md)) file.
---
# git log
commit `292f458`
Author: David Butenhof <dbutenho@redhat.com>
Date: Tue Jun 23 09:14:27 2026 -0400
Upgrade 0.6.0 torch dependencies
We want to release a GuideLLM container image for RHAI 3.5, supporting full
multimodal testing. However, RHAI 3.5 builds torch 2.11.0 and torchcodec
0.11.0, while GuideLLM 0.6.0 requires torch 2.10 and torchcodec 0.11.
This upgrade the dependencies.
Signed-off-by: David Butenhof <dbutenho@redhat.com>
---------
Signed-off-by: David Butenhof <dbutenho@redhat.com>