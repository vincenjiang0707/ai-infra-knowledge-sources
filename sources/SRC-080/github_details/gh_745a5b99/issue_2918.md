# [Issue #2918] [Bug]: compressed-tensors version insatisfiable

source: https://github.com/vllm-project/llm-compressor/issues/2918
state: closed | updated: 2026-07-14T05:24:55Z
labels: bug

## 正文

### ⚙️ Your current environment

script does not run, same error

```
[project]
name = "quantr"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "transformers>=4.45",
    "accelerate>=1.0",
    "datasets>=2.20",
    "torch>=2.11",
    "tqdm>=4.66",
    "pyyaml>=6.0",
    "compressed-tensors>=0.17",
    "llmcompressor>=0.12",
    "vllm==0.24",
    "lm-eval>=0.4.5",
]

[tool.uv]
environments = ["sys_platform == 'linux'"]
# override-dependencies = [
#     "compressed-tensors==0.17.0",
# ]
```

### 🐛 Describe the bug

```
$ uv sync                                                                                                                               [18:00:08]
  × No solution found when resolving dependencies for split (markers: python_full_version >= '3.14' and sys_platform == 'linux'):
  ╰─▶ Because vllm==0.24.0 depends on compressed-tensors==0.17.0 and llmcompressor==0.12.0 depends on compressed-tensors==0.17.1, we can conclude
      that llmcompressor==0.12.0 and vllm==0.24.0 are incompatible.
      And because only llmcompressor<=0.12.0 is available, we can conclude that llmcompressor>=0.12.0 and vllm==0.24.0 are incompatible.
      And because your project depends on llmcompressor>=0.12 and vllm==0.24, we can conclude that your project's requirements are unsatisfiable.

hint: While the active Python version is 3.12, the resolution failed for other Python versions supported by your project. Consider limiting your project's supported Python versions using `requires-python`.
hint: Pre-releases are available for `llmcompressor` in the requested range (e.g., 0.12.1a20260710), but pre-releases weren't enabled (try: `--prerelease=allow`)% 
```

### 🛠️ Steps to reproduce

I'm having numerous issues getting vllm + llmcompressor + lm_eval setup with flash attention for Qwen35

Any insights or help here would be appreciated

## 评论 (9)

### dsikka · 2026-07-13

Please install llm-compressor and vLLM in separate environments. They often have conflicting requirements. Alternatively, you can update the compressed-tensors version used in vLLM and it should work fine.

### verdverm · 2026-07-13

yeah, but then I hit other issues, is there a way to have a single git repo with multiple environments? I don't really want to have to separate them because of python dependency issues

### dsikka · 2026-07-13

Unfortunately this is not supported 

### verdverm · 2026-07-13

I'm not so sure, it looks like `uv venv` + `uv --config-file` may partition things. Will report back

appreciating Go philosophies today lol

### verdverm · 2026-07-13

I suppose I still have a question, re: vllm / llmcompressor...

If vllm is a backend for llmcompressor, shouldn't they be installable in the same env? How else are we supposed to make this work? 

or maybe i'm getting wires crossed and llmcompressor does not need vllm?

### dsikka · 2026-07-13

vLLM is not a backend for llm-compressor. LLM Compressor applies quantization / compression algorithms and then saves models in the compresed-tensors format. Once saved, the model can be served using vLLM. 

Consider reading through our step-by-step compression guide: https://docs.vllm.ai/projects/llm-compressor/en/latest/steps/why-llmcompressor/ 

### verdverm · 2026-07-13

I think I have it working now, tl;dr until I push the repo to github (do you have a place where community users can share example workflows)

you can put each half (llmcompressor & lm-eval) in a subdir with pyproject files. Looks to be working now. 

```
.PHONY: FORCE
FORCE:;

uv.sync: uv.sync.quant uv.sync.evals
uv.sync.quant: FORCE
	uv sync --project quant
uv.sync.evals: FORCE
	uv sync --project evals

quant.qwen:
	uv run --project quant quant/qwen36-27b.py
evals.qwen:
	uv run --project evals evals/qwen36-27b.sh
```

### dsikka · 2026-07-14

No as using one env for both is not suggested or tested. I would highly recommend keeping them separate. Please open another issue if you run into issues with separate envs

### verdverm · 2026-07-14

Here is how to have two uv envs (projects) in one git repo, and some wrappers around `llm-compressor` + `lm-evaluation-harness`

https://github.com/verdverm/quantr
