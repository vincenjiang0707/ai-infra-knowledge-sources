# [Issue #253] [Feature Request] List as input for max-seconds and max-requests

source: https://github.com/vllm-project/guidellm/issues/253
state: closed | updated: 2026-07-01T21:58:18Z
labels: internal, cli

## 正文

We need the ability to do a list of max-seconds or max-requests. The different rates that we set on the --rates parameter need different number of requests or different test durations to get usable results from the test. 

For concurrency of 600, if we require 600 seconds, we are now forced to run concurrency 1 for 600 seconds too. 
The same applies if we were to attempt to use max-requests too. Concurrency 1 test does not require 600 or 1200 requests to get valid data.

## 评论 (1)

### markurtz · 2025-09-18

~This will be enabled in 0.4~

Pushed
