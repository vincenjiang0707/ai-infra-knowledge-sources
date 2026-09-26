# [Issue #1091] Repository-wide audit: clean up stale docstrings, dead exports, and deprecated script references

source: https://github.com/vllm-project/speculators/issues/1091
state: open | updated: 2026-09-08T08:02:47Z
labels: documentation, good first issue

## 正文

### Motivation.

As the codebase has evolved across recent refactors, various docstrings, module comments, exports, and documentation references have become outdated. 

A general audit across the repository is needed to identify and clean up stale references, dead symbols, and obsolete script paths to maintain high documentation integrity and prevent newcomer confusion.

Below is a **preliminary, non-exhaustive list of examples** discovered during an initial sweep that illustrate the avenues for cleanup:

1. **Dead exports in `__all__` causing runtime import errors**:
   - In [`src/speculators/utils/__init__.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/utils/__init__.py), `__all__` contains `"AutoImporterMixin"`, which was removed and no longer exists anywhere in the repository. As a result, wildcard imports fail:
     ```python
     >>> from speculators.utils import *
     AttributeError: module 'speculators.utils' has no attribute 'AutoImporterMixin'
     ```

2. **Stale class/method references and typos in docstrings**:
   - In [`src/speculators/utils/registry.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/utils/registry.py):
     - Lines 15–16: The module docstring mentions `AutoClassRegistryMixin`, which has been completely removed from the file.
     - Lines 170–173: The docstring for `registered_classes()` refers to a non-existent `auto_populate_registry` method.
     - Lines 139–140: Missing trailing space in `TypeError` string concatenation (`"without invocation." f"Got improper clazz arg {clazz}."` becomes `"without invocation.Got improper..."`).
     - Line 149: Typo in `ValueError` message: `"Got imporoper name arg {name}."` (`imporoper` -> `improper`).

3. **Docstring parameter mismatches causing documentation build warnings**:
   - When running `uv run mkdocs build`, the Griffe docstring parser reports multiple parameter mismatch warnings across Pydantic configuration models because fields are documented with Sphinx `:param:` tags rather than class `Attributes:` or field descriptions:
     - [`src/speculators/models/eagle3/config.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/eagle3/config.py): `transformer_layer_config`, `draft_vocab_size`, `norm_before_residual`
     - [`src/speculators/models/dflash/config.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/dflash/config.py): `transformer_layer_config`, `draft_vocab_size` (also docstring states `draft (64K)`, whereas the code default is `32000`)
     - [`src/speculators/models/mtp/config.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/mtp/config.py): `transformer_layer_config`, `num_nextn_predict_layers`
     - [`src/speculators/models/peagle/config.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/peagle/config.py): `mask_token_id`

4. **Stale references to deprecated `scripts/*.py` entrypoints**:
   - Following the CLI unification, execution of individual runner scripts in `scripts/` (e.g. `scripts/train.py`, `scripts/prepare_data.py`, `scripts/data_generation_offline.py`, `scripts/stitch_mtp.py`) is deprecated in favor of `speculators <command>` or `torchrun -m speculators.train`. However, multiple docstrings, comments, and documentation pages still refer to the deprecated script names:
     - [`src/speculators/train/config/__init__.py:1`](https://github.com/vllm-project/speculators/blob/main/src/speculators/train/config/__init__.py#L1): `"Config-file-first configuration for ``scripts/train.py``."`
     - [`src/speculators/train/config/artifacts.py:70`](https://github.com/vllm-project/speculators/blob/main/src/speculators/train/config/artifacts.py#L70): `"Called at rank 0 by ``scripts/train.py``..."`
     - [`src/speculators/train/config/schema.py:815`](https://github.com/vllm-project/speculators/blob/main/src/speculators/train/config/schema.py#L815): `"``scripts/train.py`` calls."`
     - [`src/speculators/train/cli.py:1`](https://github.com/vllm-project/speculators/blob/main/src/speculators/train/cli.py#L1): `"Training entrypoint — core logic moved from scripts/train.py."`
     - [`docs/cli/prepare_data.md:8`](https://github.com/vllm-project/speculators/docs/cli/prepare_data.md#L8): `"For natural-language conversations, prepare_data.py asks..."`
     - [`tests/unit/train/test_draft_config_init.py:1`](https://github.com/vllm-project/speculators/tests/unit/train/test_draft_config_init.py#L1): `"Tests for the draft-model initialization sources in ``scripts/train.py``."`
     - [`docs/cli/index.md:47-54`](https://github.com/vllm-project/speculators/docs/cli/index.md#L47-L54): Mermaid workflow links point to directory-style paths rather than the corresponding `.md` pages.

### Proposed Change.

1. **Audit & Cleanup**:
   - Perform a sweep across docstrings, comments, and module exports to identify and remove obsolete references to deleted classes, methods, and deprecated runner scripts.
   - Address the known preliminary items outlined in the motivation.
   - Clean up `__all__` in `src/speculators/utils/__init__.py` and add a unit test in [`tests/unit/utils/test_registry.py`](https://github.com/vllm-project/speculators/blob/main/tests/unit/utils/test_registry.py) ensuring all exported symbols can be imported cleanly without `AttributeError`.
   - Update model config docstrings to align with Google-style `Attributes:` blocks so that `uv run mkdocs build` runs with zero Griffe parameter warnings.
   - Update mentions of deprecated `scripts/*.py` in docstrings, test headers, and documentation to reference the corresponding modern CLI command (`speculators <command>` or `torchrun -m speculators.train`).

2. **Validation**:
   - Verify wildcard imports: `uv run python -c "from speculators.utils import *"`
   - Verify docs build: `uv run mkdocs build`
   - Verify code formatting and linting: `uv run ruff check` and `uv run ruff format --check`
   - Verify unit tests: `uv run pytest tests/unit/utils/`

### Any Other Things.

- The items listed above serve as starting points from an initial scan; contributors are encouraged to audit other packages under `src/speculators/` for similar stale docstrings or dead references.


## 评论 (2)

### Adityarya11 · 2026-09-08

hi @rahul-tuli 
can i get assigned for this one? 

### rahul-tuli · 2026-09-08

Hi @Adityarya11, Thanks for your interest, this issue has been assigned to you!
