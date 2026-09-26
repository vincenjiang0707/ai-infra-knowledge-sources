# [Issue #411] `pip install perf-analyzer` is broken

source: https://github.com/triton-inference-server/perf_analyzer/issues/411
state: closed | updated: 2025-07-03T14:41:26Z
labels: 

## 正文

`pip install perf-analyzer` installs the following. 

```
Collecting perf-analyzer
  Using cached perf_analyzer-0.1.0-py3-none-any.whl.metadata (135 bytes)
Using cached perf_analyzer-0.1.0-py3-none-any.whl (2.3 kB)
Installing collected packages: perf-analyzer
Successfully installed perf-analyzer-0.1.0
```

Upon further inspection, it has only `__init__.py` with a print statement, hello world.

The pip install is broken. `pip install genai-perf` is also broken due to this. From my testing `conda` env with `python 3.11.13` is working properly.

My `pip` env is
```
python 3.11.11
pip 25.1.1
```


## 评论 (1)

### mrtpk · 2025-07-03

The wheel is dependent on the Ubuntu version. It worked in Ubuntu 24 but not on 22. The build commands works for Ubuntu 22.
