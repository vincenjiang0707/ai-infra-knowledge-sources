# [Issue #911] Support nsys profiler upload in all cases

source: https://github.com/AI-Hypercomputer/maxtext/issues/911
state: open | updated: 2026-06-27T22:23:55Z
labels: bug, good first issue

## 正文

For both `jax.profiler` (`profiler=xplane` in maxtext) and a GPU nsys profiler (`profiler=nsys` in maxtext) we upload the profile to the `base_output_directory` ([source](https://github.com/AI-Hypercomputer/maxtext/blob/0a919c19911ea2d99445e72a59e838f466b962c6/MaxText/pyconfig.py#L317)) 

Typically this directory is GCS, it can also be local. However for the nsys profiler we hardcode the uploader to use gsutil [source](https://github.com/AI-Hypercomputer/maxtext/blob/0a919c19911ea2d99445e72a59e838f466b962c6/MaxText/profiler.py#L64), which has two problems
1. Output directory may not be GCS, so gsutil is not applicable
2. Hosts may not have gsutil installed, since gsutil is not in requirements.txt

We should modify the nsys profile upload to work in all cases.

Additional context - https://github.com/AI-Hypercomputer/maxtext/pull/909 was added as a temporary fix for 2 - we won't upload the profile when gsutil is missing, so training may continue

## 评论 (1)

### SakshieP · 2026-06-27

Hi @hengtaoguo, I'm an independent user interested in working on this 'good first issue' to fix the nsys upload path. Are you currently working on this, or would it be alright if I take a crack at it?
