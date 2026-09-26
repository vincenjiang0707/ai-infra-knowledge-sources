source: https://github.com/vllm-project/guidellm/commit/1ee5a53357479337543cf75fa0a017b4527d3d20

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Copy file name to clipboardExpand all lines: docs/examples/custom_workloads.md

+7-1Lines changed: 7 additions & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -1,6 +1,6 @@

1

1

# Benchmarking Different Workload Shapes

2

2

3

-

Not all LLM workloads are the same. A chatbot, a summarization pipeline, and a code generator stress your server in completely different ways. This guide shows how to configure GuideLLM for each specific workload type and explains why metrics behave differently.

3

+

Not all LLM workloads are the same. A chatbot, a summarization pipeline, and a code generator stress your server in completely different ways. This guide shows how to configure GuideLLM for specific workload type and explains why metrics behave differently.

4

4

5

5

## Prerequisites

6

6

@@ -18,6 +18,8 @@ The ratio of input to output tokens shifts which phase dominates. A workload wit

18

18

19

19

## The Four Common Shapes

20

20

21

+

**NOTE:**_Current workloads gear towards a **heavy prefill** (tokens in) due to multiple files, longer system prompts, multiturn etc... so these may not reflect real-world use cases. If you have custom workload, then configure these to your specific use-case_

22

+

21

23

### 1. Chat / Conversational

22

24

23

25

A user sends a short message and expects a medium-length response **(decode-bound)**. Typical of chatbots, customer support, and Q&A interfaces.

@@ -86,13 +88,17 @@ guidellm run \

86

88

87

89

Run all four shapes on the same server and compare the results side by side.

88

90

91

+

**Recommended**: _Change shapes to your custom workload_

-**Summarization has the highest TTFT** because the server processes 2048 input tokens before generating the first output token **(prefill-bound)**. But ITL is the lowest because there are very few tokens to decode.

## 0 commit comments