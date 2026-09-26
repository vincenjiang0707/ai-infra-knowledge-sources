# [Issue #5309] [Bug] logStdoutEncoder and logFileEncoder setting from `--config` are ignored

source: https://github.com/ray-project/kuberay/issues/5309
state: closed | updated: 2026-09-22T21:49:35Z
labels: bug, good-first-issue

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### KubeRay Version

main

### Ray Version

_No response_

### Environment

N/A

### What happened + What you expected to happen

The operator supports configuring the log encoder in two ways:

- Command-line flags
- Config file

When using `--config`, the `logStdoutEncoder` and `logFileEncoder` are loaded into config, but `main.go` still uses the flag variables directly when creating the encoders:


https://github.com/ray-project/kuberay/blob/f72fa09812e0412305ee536bc2d28a6a3fe6037d/ray-operator/main.go#L168-L181


The log encoder should consistently use the resolved configuration instead:

```
stdoutEncoder, err := newLogEncoder(config.LogStdoutEncoder)
fileEncoder, err := newLogEncoder(config.LogFileEncoder)
```


### Reproduction script

N/A

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (1)

### Onionssss · 2026-09-17

I’d like to work on this issue, thanks!
