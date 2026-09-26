# [Issue #516] Does deepep-tests scripts support nsys profile?

source: https://github.com/deepseek-ai/DeepEP/issues/516
state: closed | updated: 2026-09-18T08:47:29Z
labels: 

## 正文

it uses kineto to capture kernel durations. does it still work along with `nsys profile -t cuda`?

if it doesn't, can we add a command line option or some env variable to by-pass kineto data capturing and calculation, so `nsys profile` can work?

## 评论 (1)

### polarstormx · 2026-09-18

Current main already provides `EP_USE_NVIDIA_TOOLS=1` to bypass the internal Kineto profiling, as documented in the README.
