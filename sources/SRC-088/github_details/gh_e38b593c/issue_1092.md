# [Issue #1092] Add unit tests, type annotations, and docstrings for speculators.train utilities (noise_transforms.py and vocab_mapping.py)

source: https://github.com/vllm-project/speculators/issues/1092
state: open | updated: 2026-09-08T08:04:36Z
labels: good first issue

## 正文

### Motivation.

The training subsystem relies on two lightweight utility modules for data preparation and augmentation: [`src/speculators/train/noise_transforms.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/train/noise_transforms.py) and [`src/speculators/train/vocab_mapping.py`](https://github.com/vllm-project/speculators/blob/main/src/speculators/train/vocab_mapping.py). Both have incomplete test coverage and typing/docstring discrepancies:

1. **`noise_transforms.py`**:
   - Defines `TransformTensors`, `AddGaussianNoise`, and `AddUniformNoise` used for hidden state augmentation.
   - It is a 26-line file that currently lacks docstrings, full type annotations on `__init__` and `__call__`, and does not define `__all__`.
   - There are **zero unit tests** in the entire test suite covering this module.

2. **`vocab_mapping.py`**:
   - `save_token_frequency_distribution()` docstring states:
     ```
     Returns:
         Path to the saved frequency distribution file
     ```
     However, the function returns `None` (either early returning `return` or terminating without returning `path`).
   - `__all__` only lists 2 of the 4 functions defined in the module, omitting `combine_token_frequency_distributions` and `get_target_vocab_size`.
   - In `combine_token_frequency_distributions`, `combined_token_freq` is typed as `Counter[str] = Counter()`, even though token IDs are integers (`Counter[int]`).
   - While `test_vocab_mapping_cli.py` tests CLI argument parsing and caching, there are no direct unit tests validating `build_vocab_mappings_from_distribution()` (verifying offset tensor math, frequency sorting, and fallback padding) or `combine_token_frequency_distributions()`.

Consolidating these into one issue provides a well-rounded contribution to the training pipeline utilities that runs entirely on CPU.

### Proposed Change.

#### Part 1: `src/speculators/train/noise_transforms.py`
- [ ] Add `__all__ = ["TransformTensors", "AddGaussianNoise", "AddUniformNoise"]`.
- [ ] Add docstrings and complete type hints to `__init__` and `__call__`.
- [ ] Create `tests/unit/train/test_noise_transforms.py` with tests:
  - Base class `TransformTensors.transform()` raises `NotImplementedError`.
  - `AddGaussianNoise` mutates specified tensor keys and leaves non-specified keys unmodified; preserves shape, dtype, and device; identity check when `std=0.0`.
  - `AddUniformNoise` generates noise strictly bounded in `[-std, std]`; identity check when `std=0.0`.

#### Part 2: `src/speculators/train/vocab_mapping.py`
- [ ] Align `save_token_frequency_distribution()` return behavior and docstring (either return `path` or update docstring to `Returns: None`).
- [ ] Export all public functions in `__all__`.
- [ ] Fix typing in `combine_token_frequency_distributions` (`Counter[int]`).
- [ ] Add type hints and docstring to `get_target_vocab_size`.
- [ ] Create `tests/unit/train/test_vocab_mapping.py` with tests:
  - `build_vocab_mappings_from_distribution`: verifies ranking by frequency, padding behavior when unique tokens < `draft_vocab_size`, and confirms `draft_idx + draft_to_target[draft_idx]` maps correctly to target token IDs.
  - `combine_token_frequency_distributions`: verifies merging multiple frequency dictionaries saved on disk.

### Any Other Things.

- **Verification Commands**:
  - `uv run pytest tests/unit/train/test_noise_transforms.py tests/unit/train/test_vocab_mapping.py`


## 评论 (1)

### rahul-tuli · 2026-09-08

Hi @YuEfSaEDU, thanks for your interest, this issue has been assigned to you!
