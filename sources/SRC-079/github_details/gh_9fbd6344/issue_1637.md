# [Issue #1637] Puzzletron README initial setup fails with number of issues

source: https://github.com/NVIDIA/Model-Optimizer/issues/1637
state: open | updated: 2026-06-05T18:28:00Z
labels: bug, documentation, triaged

## 正文

Using: https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/puzzletron/README.md

Doing an initial puzzletron setup up to this sanity check fails with number of issues: `python -m pytest tests/gpu/torch/puzzletron/test_puzzletron.py -k "Qwen3-8B"`

1) Why in Nemo 26_02 there is nvidia-modelopt                             0.43.0rc1 installed and not 0.44?

To reproduce:
```
enroot import --output ./docker/nemo_26_02.sqsh docker://nvcr.io/nvidia/nemo:26.02

export EXPERIMENT_DIR=.../dkorzekwa/experiments/6_5_qwen_35_moments_lab

submit_job (srun wrapper) --partition interactive --time 4 --image  $EXPERIMENT_DIR/docker/nemo_26_02.sqsh --mounts $EXPERIMENT_DIR:/workspace --interactive --gpu 8

 python -m pip list |grep modelopt
```

after calling python -m pip install -e ".[hf,puzzletron,dev-test]":

```
nvidia-modelopt                             0.45.0.dev164+g115cae258
```

2) “...Once inside the container with the repo available, install dependencies from the repo root: …” - unclear what is “repo root”, I assume it is ModelOpt source repo, can we clarify it?

3) Why is it required to install modelopt from sources given it is already installed in the nemo container? is similar approach needed for other compression algorithms in modelopt?

```
python -m pip install -e ".[hf,puzzletron,dev-test]"
```

4) `python -m pytest tests/gpu/torch/puzzletron/test_puzzletron.py -k "Qwen3-8B` fails, adding  `-o addopts=""` makes it working.

5) Why are both needed?
```
python -m pip install -e ".[hf,puzzletron,dev-test]"
python -m pip install -r examples/puzzletron/requirements.txt
```
can we simplify it?

6) python -m pip install -e ".[hf,puzzletron,dev-test]" shows an error:
```
Uninstalling nvidia-modelopt-0.43.0rc1:
      Successfully uninstalled nvidia-modelopt-0.43.0rc1
  Attempting uninstall: peft
    Found existing installation: peft 0.13.2
    Uninstalling peft-0.13.2:
      Successfully uninstalled peft-0.13.2
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
nemo-export-deploy 0.4.0rc0 requires peft<0.14.0, but you have peft 0.19.1 which is incompatible.
tensorrt-llm 1.1.0 requires fastapi<=0.121.3,>=0.120.1, but you have fastapi 0.135.1 which is incompatible.
tensorrt-llm 1.1.0 requires nvidia-cutlass-dsl==4.2.1; python_version >= "3.10", but you have nvidia-cutlass-dsl 4.4.2 which is incompatible.
tensorrt-llm 1.1.0 requires setuptools<80, but you have setuptools 81.0.0 which is incompatible.
tensorrt-llm 1.1.0 requires transformers==4.56.0, but you have transformers 4.57.6 which is incompatible.
tensorrt-llm 1.1.0 requires wheel<=0.45.1, but you have wheel 0.46.3 which is incompatible.
Successfully installed deepspeed-0.19.1 dependency-groups-1.3.1 fire-0.7.1 hjson-3.1.0 humanize-4.15.0 lru-dict-1.4.1 nox-2026.4.10 nvidia-modelopt-0.45.0.dev164+g115cae258 peft-0.19.1 pytest-cov-7.1.0 pytest-instafail-0.5.0 termcolor-3.3.0 torch-geometric-2.7.0 wonderwords-3.0.1
```

7) python -m pytest tests/gpu/torch/puzzletron/test_puzzletron.py -o addopts="" -k "Qwen3-8B" fails with

```
 File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/workspace/Model-Optimizer/tests/_test_utils/torch/distributed/utils.py", line 53, in init_process
    job(rank, size)
  File "/workspace/Model-Optimizer/tests/gpu/torch/puzzletron/test_puzzletron.py", line 202, in _test_puzzletron_multiprocess_job
    pytest.fail(
  File "/opt/venv/lib/python3.12/site-packages/_pytest/outcomes.py", line 163, in __call__
    raise Failed(msg=reason, pytrace=pytrace)
Failed: 2 assertion(s) failed for Qwen/Qwen3-8B:
  - Teacher memory mismatch for Qwen/Qwen3-8B: expected 395.63, got 1582.13720703125
  - Teacher num_params mismatch for Qwen/Qwen3-8B: expected 6096640, got 24189184
```

8) To use puzzletron on a slurm based cluster, I had to figure out what enroot command to use to download the image and then learn how to use slurm. Is there some wiki in modelopt that shows how to use modelopt using different types of infrastructures, e.g. in my case slurm-based on-prem.

## 评论 (1)

### ChenhanYu · 2026-06-05

## Triage Analysis

| Field | Value |
|-------|-------|
| Classification | Docs |
| Severity | Medium |
| Complexity | Simple |
| Auto-fixable | No |

### Summary
The Puzzletron README initial setup instructions have multiple issues: unclear language about 'repo root', version mismatch between container's modelopt and source install, pytest command fails without `-o addopts=""`, redundant pip install steps, and dependency conflicts with the NeMo container. These collectively prevent users from successfully following the getting-started guide.

### Root Cause / Approach
The README documentation has multiple clarity and correctness issues: (1) It doesn't explain why installing from source is necessary over the pre-installed container version. (2) 'repo root' is ambiguous. (3) The pytest command fails because conftest.py adds custom options (like --run-manual, --run-release) that conflict with default addopts in pytest config, requiring `-o addopts=""` to work. (4) The two separate pip install commands (editable install + requirements.txt) are confusing and could be consolidated. (5) Dependency conflicts arise because the editable install pulls newer versions incompatible with other NeMo container packages.

### Suggested Fix
1. Clarify in README that 'repo root' means the root of the cloned Model-Optimizer repository. 2. Explain why source install is needed (puzzletron extras not included in container's pre-installed modelopt). 3. Add `-o addopts=""` to the pytest smoke check command. 4. Consider merging examples/puzzletron/requirements.txt into the puzzletron optional dependency in pyproject.toml to eliminate the second pip install step. 5. Add a note about expected dependency conflict warnings being non-fatal, or pin compatible versions. 6. Optionally add a version compatibility note about NeMo 26.02 shipping modelopt 0.43.0rc1.

### Relevant Files
- `examples/puzzletron/README.md`
- `examples/puzzletron/requirements.txt`
- `pyproject.toml`
- `tests/conftest.py`
- `tests/gpu/torch/puzzletron/test_puzzletron.py`

---
_Auto-triaged by pensieve `/magic-triage`_
