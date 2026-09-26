source: https://github.com/vllm-project/guidellm/pull/1148

# Fix multimodal data drop when combined with synthetic text in one message - #1148

[mergify[bot]](https://github.com/mergify[bot])merged 5 commits into

## Conversation

|
Hi |


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 15, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

A few comments before looking into the code changes:

- You haven't added any test cases, which would be nice...
- It's often helpful in complex scenarios for the PR description to include more specifics about the manual testing ... for example, the exact GuideLLM commands / datasets you used. (But don't include real host names for the LLM target.)

|
"You haven't added any test cases, which would be nice..." |

The PR should include a new test case added to the unit test suite to cover the new code.
"Common practice" is a loose term ... but when there's specific setup that's not necessarily obvious to the reader, including sample commands to help demonstrate the effect of the change can help with reviewing. |


**requested changes**

[sjmonson](https://github.com/sjmonson)Sep 15, 2026

[src/guidellm/data/finalizers/conversation_graph.py](https://github.com/vllm-project/guidellm/pull/1148/files#diff-78a63a9e262dfeb613ef927d40c36b7089d91647a5b524ba1b5fcc9888ad07ae)

Assisted-by: Claude Sonnet 5 Signed-off-by: Sharon Hezy <shezy@redhat.com>

…ended existing multimodal benchmarks tests for multimodal inputs with validation of constructed structure Signed-off-by: Sharon Hezy <shezy@redhat.com>

[sharonh24](https://github.com/sharonh24)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ccca2fbff7b500fbfa3e95154d49e137f8aa7ddd..c3d59f48028e69846d3c6f872f5408cfe8fb8995)the bugfix/fix_other_data_drop_in_synth_text_msg branch from

[to](https://github.com/vllm-project/guidellm/commit/ccca2fbff7b500fbfa3e95154d49e137f8aa7ddd)

`ccca2fb`


`c3d59f4`

[Compare](https://github.com/vllm-project/guidellm/compare/ccca2fbff7b500fbfa3e95154d49e137f8aa7ddd..c3d59f48028e69846d3c6f872f5408cfe8fb8995)

September 16, 2026 11:13

Signed-off-by: Sharon Hezy <shezy@redhat.com>

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I just have one minor comment about the comments.

[tests/integration/data/test_synthetic_multimodal_benchmark.py](https://github.com/vllm-project/guidellm/pull/1148/files/30f4a44f1e107c913b8c6d7e4533159c704479ef#diff-45ac47c933c513a05df100002b18874f47f65486408e24d5812e97fdd713b4cf)Outdated

Signed-off-by: Sharon Hezy <shezy@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 18, 2026

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I noticed Sam's review, and realized I'd never actually submitted my review yesterday. I have one minor comment on wording, but it's not really that important -- I'll log it anyway, but I'll resolve it and let this merge.

[src/guidellm/data/finalizers/conversation_graph.py](https://github.com/vllm-project/guidellm/pull/1148/files/5d3a6075b1b01858b58e6302ad8269e0c7a0aa49#diff-78a63a9e262dfeb613ef927d40c36b7089d91647a5b524ba1b5fcc9888ad07ae)

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Fix multimodal synthetic text requests - prevent multimodal content from being dropped. Sibling image, video, or audio data provided through separate dataset sources (separate

--data) is preserved when the text dataset emits a pre-built conversation_turn data structure.The sibling data is now merged into the root conversation turn before request generation, preventing multimodal content from being dropped.

## Details

## Test Plan

Finalizer - added unit tests to verify that conversation turn which contains synthetic text and image/video - indeed combines them together. Run it:


`python3 -m pytest tests/unit/data/test_finalizers.py -q`

Expanded multimodal benchmark testing, to verify that image/video metrics are added to the output report when the passed multimodal data combines synthetic text with synthetic image and/or video data. To verify, run:


`python3 -m pytest -q tests/integration/data/test_synthetic_multimodal_benchmark.py`

To manually test end-to-end with mock-server:

Open 2 terminal windows (or tmux)

In first terminal type:


`python3 -m guidellm mock-server --host 127.0.0.1 --port 8000 \ --model gpt2 --request-latency 0.05 --ttft-ms 20 --itl-ms 2 --output-tokens 3 \ --image-tokens 576 --video-tokens 1024 --audio-tokens-per-second 25`

Wait for the server to start, then run in the second terminal:


`python3 -m guidellm run --data-loader kind=pytorch,num_workers=0 \ --backend kind=openai_http,target=http://127.0.0.1:8000 \ --profile kind=synchronous --constraint kind=max_requests,count=3 \ --data kind=synthetic_text,prompt_tokens=64,output_tokens=32 \ --data kind=synthetic_image,resolution=720p,format=jpeg,seed=11 \ --data kind=synthetic_video,resolution=720p,frames=2,fps=1,seed=23`

To perform more comprehensive tests, on multiple profiles - use the attached script.

The script will create

`./output_reports/`

subdirectory from your current location. Enter the desired parent location before running the script, or change its behavior.run_multiple_guidellm_tests_save_output.sh

## Related Issues

#1124 - vLLM OMNI support

#1125 - OMNI TTS

#1056 - Add multimodal support to the mock server

## Resolves

#1147 - Fix dropped modalities in client, when passed synthetic_text data kind

## Use of AI

## git log

commit

e345364Author: Sharon Hezy shezy@redhat.com

Date: Tue Sep 15 14:58:32 2026 +0300

commit

c3d59f4Author: Sharon Hezy shezy@redhat.com

Date: Wed Sep 16 14:09:32 2026 +0300

commit

30f4a44Author: Sharon Hezy shezy@redhat.com

Date: Wed Sep 16 18:39:29 2026 +0300

commit

beb5800Author: Sharon Hezy shezy@redhat.com

Date: Thu Sep 17 11:03:53 2026 +0300

Assisted-by: Claude Sonnet 5

Signed-off-by: Sharon Hezy shezy@redhat.com