# [Issue #3407] [Question] MLC concurrent request handling behavior

source: https://github.com/mlc-ai/mlc-llm/issues/3407
state: closed | updated: 2026-02-18T17:48:49Z
labels: question

## 正文

## ❓ General Questions

I've installed MLC LLM using prebuilt wheels and am running the MLC server with mlc_llm serve. After sending the first request—while the server is streaming output tokens—if I send a second request, token generation for the first pauses. It only resumes after the second request's prefill phase completes and starts token generation. Is this the expected behavior? I expected the two concurrent requests to be handled independently, without the second interfering with the first. Are there any settings that can modify this? Thank you.

## 评论 (2)

### MasterJH5574 · 2026-01-25

Hi @jimmyparadm, thanks for the question.  Yes, this is the expected behavior. While the GPU is computing the prefilling for your second request, the decoding for your first request is affected.

### MasterJH5574 · 2026-01-25

@jimmyparadm As developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
