# [Issue #272] bump numpy version?

source: https://github.com/triton-inference-server/perf_analyzer/issues/272
state: closed | updated: 2025-02-06T04:23:01Z
labels: 

## 正文

Hi Developers,

genai-perf has a limitation on numpy version, which blocks recent version
https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/pyproject.toml#L51

Was this due to the outlines result issue? The community has done a workaround for this and merged in recent release
https://github.com/dottxt-ai/outlines/pull/1265

Thanks, -yuan

## 评论 (2)

### the-david-oy · 2025-02-05

Thanks for raising this concern. We'll take a look at supporting Numpy 2 shortly.

### the-david-oy · 2025-02-06

Done! https://github.com/triton-inference-server/perf_analyzer/pull/275
