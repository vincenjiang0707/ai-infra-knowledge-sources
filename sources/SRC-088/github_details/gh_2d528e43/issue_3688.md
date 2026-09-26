# [Issue #3688] ray missing as dependency of vllm backend

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3688
state: open | updated: 2026-09-11T09:43:24Z
labels: 

## 正文

[vllm_causallms.py](https://github.com/EleutherAI/lm-evaluation-harness/blob/ee7e8f4fe58e13d6760c066474f0d01477317d1d/lm_eval/models/vllm_causallms.py#L14) imports ray.

So AFAICS using the vllm backend fails unless the environment has ray installed.
But ray is not specified as a required dependency of lm-eval[vllm].


## 评论 (3)

### kvr06-ai · 2026-04-10

Root cause: `lm_eval/models/vllm_causallms.py` has `import ray` at module level (line 14), but `ray` is absent from the `[vllm]` extras in `pyproject.toml`. vllm itself does not pull in `ray` transitively (absent from `vllm/requirements/cuda.txt` and from vllm's PyPI `requires_dist`), so `pip install lm_eval[vllm]` produces an environment that fails on `ImportError` the moment the backend loads.

Fix: Add `"ray"` to the `vllm` extras list in `pyproject.toml`. The three actual uses of `ray` (`@ray.remote`, `ray.get`, `ray.shutdown`) sit inside the `data_parallel_size > 1 and not self.V1` branch, but the top-level import makes ray a hard load-time requirement regardless.

PR incoming.

### omid511 · 2026-09-10

The 2026-04-10 'PR incoming' never materialized (no linked PR, pyproject still lacks ray on main), so I've opened a PR adding ray to the vllm extra. Happy to adjust scope (e.g. version floor, lazy import in vllm_vlms.py) per maintainer preference.

### omid511 · 2026-09-11

Follow-up to #4130: opened a second small PR lazy-importing ray in vllm_vlms (same pattern upstream already uses in vllm_causallms), so the vlm backend also loads without ray outside data-parallel mode.
