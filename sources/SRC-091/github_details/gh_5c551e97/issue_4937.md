# [Issue #4937] [good-first-issue] serde: convert f-string log calls in cachegen_basics.py to %-format

source: https://github.com/LMCache/LMCache/issues/4937
state: closed | updated: 2026-09-23T14:02:17Z
labels: 

## 正文

**Label**

`good first issue` — filing under [[Onboarding 2026] Good first issues](https://github.com/LMCache/LMCache/issues/3372).

**Summary**

`lmcache/storage_backend/serde/cachegen_basics.py` still builds five debug log messages with f-strings, so the strings are interpolated even when debug logging is disabled.

**Details**

All five call sites are in `CacheGenGPUEncoderOutput.debug_print_device()`:

```python
logger.debug(f"bytestream device: {self.data_chunks[0].bytestream.device}")
logger.debug(
    f"bytestream_lengths device: "
    f"{self.data_chunks[0].bytestream_lengths.device}"
)
logger.debug(f"cdf device: {self.cdf.device}")
logger.debug(f"max_tensors_key device: {self.max_tensors_key.device}")
logger.debug(f"max_tensors_value device: {self.max_tensors_value.device}")
```

Per @ApostaC's guidance in #3372, `%`-style is preferred so the arguments are formatted only when the record is actually emitted (ruff `G004`).

**Expected Outcome / Goal**

The five calls use `%s` placeholders, and `ruff check --select G004` reports no violations for this file. The rendered log text stays identical — f-string interpolation and `%s` both go through `str()`.

**Additional Context**

- Scope is this one file only, format style only, no behavior change. Whether the (currently uncalled) `debug_print_device` helper should exist at all is a separate question and out of scope here.
- Verification: `ruff check --select G004 <file>` and `pre-commit run --files <file>`.
- Repo-wide there are still 381 `G004` violations (271 under `lmcache/`), so this is one file out of a longer list.

Refs #3372


## 评论 (2)

### Prarthana10 · 2026-09-04

I'd like to work on this!

### migarci2 · 2026-09-14

/claim — picking this up (prior soft claim had no PR). Opening a DCO-signed PR against `dev`.
