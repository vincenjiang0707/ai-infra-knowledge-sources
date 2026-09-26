# [Issue #2183] [tests] move benchmark under tests/cute to benchmarks, and maybe reduce prints in tests?

source: https://github.com/Dao-AILab/flash-attention/issues/2183
state: closed | updated: 2026-07-28T18:32:08Z
labels: 

## 正文

Hi, this is just for better engineering / make my life nicer.
* benchmarks under tests/cute: for example https://github.com/Dao-AILab/flash-attention/blob/main/tests/cute/benchmark_block_sparsity.py, which is not a big deal but slightly unexpected
* prints in tests: prints can be excessive. I guess normal pytest would suppress that but I am on some weird pytest https://github.com/Dao-AILab/flash-attention/blob/main/tests/cute/test_block_sparsity.py#L252-L261


cc @reubenconducts 

## 评论 (3)

### reubenconducts · 2026-01-15

The block sparsity and mask mod benchmark scripts are in `tests/cute` for proximity to `mask_mod_definitions` to avoid annoying relative imports. I see no problem with prints in tests, they are ubiquitous. 

### NJX-njx · 2026-03-14

I can take this. I'll propose a PR that moves the benchmark scripts out of 	ests/cute into enchmarks/ while keeping imports clean (no annoying relative paths). I'll keep test prints as-is unless maintainers prefer otherwise.

### NJX-njx · 2026-03-29

Submitted a fix in #2408:
- Moved `benchmark_block_sparsity.py` and `benchmark_mask_mod.py` from `tests/cute/` to `benchmarks/cute/`
- Replaced verbose `print()` in `test_block_sparsity.py` with `logging.debug()` (suppressed by default, visible with `pytest --log-cli-level=DEBUG`)
