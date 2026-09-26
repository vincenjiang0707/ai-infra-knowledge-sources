# [Issue #175] Unexpected fluctuations in the prompt size

source: https://github.com/triton-inference-server/perf_analyzer/issues/175
state: closed | updated: 2024-12-17T20:34:45Z
labels: 

## 正文

During my experiments with the Llama3_2-3B model (and its built-in tokenizer) I have noticed the following issue: even if I set `--synthetic-input-tokens-mean 256 --synthetic-input-tokens-stddev 0`, not all inputs have the size of 256, but rather they are distributed around 256.
This plot built for one of such experiments demonstrates the problem:
![time_to_first_token_vs_input_sequence_lengths](https://github.com/user-attachments/assets/ca189965-70e0-4d54-b93a-0ab1f85d54c4)

I believe that the issue happens because of these lines in `genai_perf/inputs/retrievers/synthetic_prompt_generator.py`:
```
        # Final tweaks
        diff = requested_prompt_tokens - get_token_length(prompt)
        for _ in range(diff):
            prompt = "hi " + prompt
```
This code snippet was designed with an assumption that "hi " would be tokenized to exactly one token that is not true for all tokenizers (as I have mentioned above an example is one in Llama3_2-3B).

I have tried to patch the issue like this:
```
diff --git a/genai-perf/genai_perf/inputs/retrievers/synthetic_prompt_generator.py b/genai-perf/genai_perf/inputs/retrievers/synthetic_prompt_generator.py
index 68b77fd..5a8d5d4 100644
--- a/genai-perf/genai_perf/inputs/retrievers/synthetic_prompt_generator.py
+++ b/genai-perf/genai_perf/inputs/retrievers/synthetic_prompt_generator.py
@@ -110,8 +110,7 @@ class SyntheticPromptGenerator:
         prompt += final_line

         # Final tweaks
-        diff = requested_prompt_tokens - get_token_length(prompt)
-        for _ in range(diff):
+        while requested_prompt_tokens > get_token_length(prompt):
             prompt = "hi " + prompt

         return prompt
```
but obviously it is not ideal. While this approach allows me to have the constant input size, it still assumed that "hi " cannot be tokenized in more than one token, otherwise the size would be larger than expected.

I think a good solution would be using the `while` approach to guarantee that the factual size is either above or below the desired value, and if it is still not equal to it, throwing a warning.

Another way could be using the pad token instead of "hi ", but it can limit the usage of some tokenizers and models.

I have not yet come up with a bullet-proof solution to built a prompt that would be tokenized to the desired number of token for any given tokenizer.

## 评论 (2)

### the-david-oy · 2024-11-14

That bullet-proof solution would be appreciated. :D We spent some time thinking through the best way to get an exact number of tokens while trading off for efficiency. Since the sum of tokens in fragments is not equal to the number of tokens in the combined prompt, there was not a clear way to guarantee a token count, and it would be inefficient to randomly remove and add words until the right count was achieved. This was the approach that seemed to be balance the tradeoffs. We include that token counts may not be exact in the [known issues](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/README.md#known-issues) in the README.

Since the table includes the input sequence length, I think a warning might end up being redundant.

We'd be open to looking at the approach for generating tokens again, but there might not be a good way to generate an exact token count.

CC: @nicolasnoble

### the-david-oy · 2024-12-17

[This pull request](https://github.com/triton-inference-server/perf_analyzer/pull/202) updated the approach and should make the token counts more consistent. It's on the main branch and will be included in the next release.

This approach was tested across tokenizers, though it's possible there are still edge cases. It's no longer dependent on whether hi is tokenized as one token or not.
