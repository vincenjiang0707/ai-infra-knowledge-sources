# [Issue #933] Inconsistent and limited handling of `--output` lists

source: https://github.com/vllm-project/guidellm/issues/933
state: closed | updated: 2026-07-20T16:28:27Z
labels: internal, feature, cli

## 正文

### Problem Statement

With the registry type CLI refactoring in 0.7.x, we allow repeating `--output kind=<name>,...`. While the specific intent and benefit is to allow specifying multiple output types like `--output kind=json --output kind=csv`, there's nothing to prevent specifying two "json" outputs, for example, possibly with different file names. Like `--output kind=json,path=json1.json --output kind=json,path=json2.json`. While it's not clear there's much real value in doing this, there's an interesting inconsistency between `guidellm run` and `guidellm benchmark from-file`...

In the former case, we resolve the outputs in `resolve_output_formats`, which *resolves* each output specification but then stores them in a dict by format key: so that we will *resolve* two separate JSON Output instances but the second will overwrite the first in the dict and we'll never actually generate `json1.json`.

In the latter case, we *resolve* the output specifications into another list, but then store the results of `output.finalize(report)` into a dict by output type: which means we'll *generate* both `json1.json` and `json2.json`, but the console output will only confirm creation of `json2.json`.

This becomes potentially more interesting with the new "plot" output type, where the output specification's path specifies the image format and the specification supports an image resolution. So `--output kind=plot,path=plot.pdf,dpi=100 --output kind=plot,path=plot.png,dep=300` would be expected to create a 100dpi PDF plot and a 300dpi PNG plot. `from-file` will actually do this, but will only report the second; while `run` will only generate the second and silently ignore the first.

### Proposed Solution

We should resolve, generate, and report from a list in both cases. This seems most reasonable/obvious, and with the addition of the plot output also provides potential real value to end users.

### Alternatives Considered

The alternative would be to diagnose and fail on repeated output specifications of the same kind; rather than silently ignore one for `run` and generating but failing to report one for `from-file`.

Making this work "as likely expected" is not much more complicated, and seems more reasonable.

### Usage Examples

```markdown
$ guidellm run --backend kind=openai_http,target=http://localhost:8000 --output kind=plot,dpi=72,path=plot.png --output kind=plot,dpi=300,path=plot.pdf
```

### Additional Context

_No response_

## 评论 (2)

### Pragadeesh122 · 2026-07-17

Hi @dbutenhof 👋 — I'd like to pick this up if it's open and no one's already working on it. Happy to open a PR referencing the issue.

### dbutenhof · 2026-07-17

> Hi [@dbutenhof](https://github.com/dbutenhof) 👋 — I'd like to pick this up if it's open and no one's already working on it. Happy to open a PR referencing the issue.

None of us are already working on it; so if you're interested, feel free to pick it up!
