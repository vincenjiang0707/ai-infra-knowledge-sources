# [Issue #376] system prompt in genai-perf

source: https://github.com/triton-inference-server/perf_analyzer/issues/376
state: open | updated: 2025-05-15T23:09:06Z
labels: 

## 正文

I was asked to run some load tests with genai-perf using a system prompt. When I use the synthetic-input-tokens option, I’m wondering if there is a default system prompt applied behind the scenes, because I don’t see any system prompt listed in the output JSON file.
Is there a hidden or default system prompt that’s being used for synthetic inputs?
If not, is there a way to add a system prompt for every request, whether I’m using synthetic input tokens or my own dataset?
Any clarification on this behavior would be greatly appreciated. Thank you!

## 评论 (5)

### debermudez · 2025-05-13

System prompt is not controllable via genai-perf today. 
We would need to investigate the effort to add this. 
@ganeshku1 for viz

### debermudez · 2025-05-13

@gotSomeCola can you provide some guidance on what the system prompt would look like?
A sample of the payload would be very helpful for understanding.

### gotSomeCola · 2025-05-15

@debermudez, it is basically telling the model to use simple sentences or expressions for the output so that the response is easy to understand. There are several rules we want the model to follow. For example: 
1) Use only one sentence for each piece of information. 
2) Use fewer than 15 words per sentence, with a maximum of 25 words. 
We have decided to simply add these system prompts into the user prompt while testing with our own dataset by using the "--input-file" option. We hope it will work similarly to system prompts.
Thanks for the reply.


### debermudez · 2025-05-15

1. I just want to confirm, for now, you are good and I can close this issue.

2. I would like to get a spec for what this feature would look like for you in the future. 


### ganeshku1 · 2025-05-15

@gotSomeCola  Could you please share a sample cURL request—including the system prompt—you intend to send to the endpoint? This will help us ensure we have the correct information in place.
