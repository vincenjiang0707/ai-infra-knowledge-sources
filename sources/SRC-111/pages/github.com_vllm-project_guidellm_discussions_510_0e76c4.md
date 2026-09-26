source: https://github.com/vllm-project/guidellm/discussions/510

# Vast.io - help with custom authentication headers (Cloudflare Tunnel, API Tokens) #510

## Problem SummaryGuideLLM v0.4.0 fails to authenticate when connecting to backends protected by Cloudflare Tunnel or other custom authentication mechanisms that require specific HTTP headers or non-standard authentication tokens. I use the vast.io service to try to perform benchmarks to compare GPU models. ## Expected BehaviorAccording to the v0.3.0 release notes, PR However, the correct CLI syntax for passing custom authentication headers does not appear to be documented in:
## Current Behavior
## Questions
## Examples
## Environment
|

[sjmonson](https://github.com/sjmonson)

Feb 17, 2026

## Replies: 1 comment

|
For GuideLLM v0.5.3: |

[sjmonson](https://github.com/sjmonson)

For GuideLLM v0.5.3:

`--request-formatter-kwargs '{"extras": {"headers": "X-Auth-Token": "xxxtokenxxx"}}'`

For main (v0.6.0):

`--backend-kwargs '{"extras": {"headers": "X-Auth-Token": "xxxtokenxxx"}}'`