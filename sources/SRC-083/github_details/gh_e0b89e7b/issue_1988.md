# [Issue #1988] pip wheel ships top-level tests/ directory; shadows consumers tests/ package and breaks python -m unittest discovery

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1988
state: closed | updated: 2026-07-07T16:29:02Z
labels: 

## 正文

## Summary

The `bitsandbytes` PyPI wheel ships a top-level `tests/` directory (verified in 0.44.1 and 0.45.0; likely affects the entire 0.44.x line and may extend earlier). When this wheel is installed into a project that also has a top-level `tests/` package, the wheel's `tests/` directory shadows the project's `tests/` package and **breaks `python -m unittest tests.test_X` discovery entirely** - every test fails with `ModuleNotFoundError: No module named 'tests.test_X'`.

## Environment

- Python: 3.12 (also reproducible on 3.10, 3.11)
- OS: Windows / macOS / Linux (reproduced on GitHub Actions `windows-latest`)
- bitsandbytes: 0.44.1 and 0.45.0 confirmed affected
- Install method: `pip install bitsandbytes` (no special flags)

## Steps to reproduce

```bash
mkdir /tmp/myproj && cd /tmp/myproj
mkdir tests
touch tests/__init__.py
cat > tests/test_foo.py <<'PY'
def test_bar():
    assert 1 + 1 == 2
PY
pip install bitsandbytes==0.45.0
python -m unittest tests.test_foo -v
```

## Expected

`test_foo` is discovered and passes.

## Actual

```
$ python -m unittest tests.test_foo -v
test_foo (unittest.loader._FailedTest.test_foo) ... ERROR

======================================================================
ERROR: test_foo (unittest.loader._FailedTest.test_foo)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_foo
Traceback (most recent call last):
  File ".../Lib/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  ...
ModuleNotFoundError: No module named 'tests.test_foo'

----------------------------------------------------------------------
Ran 1 test in 0.000s
FAILED (errors=1)
```

## Root cause (with evidence)

The wheel contains a top-level `tests/` directory in addition to the `bitsandbytes/` package:

```
$ pip download bitsandbytes==0.45.0 --only-binary=:all: --platform win_amd64 --no-deps -d /tmp/bnb
$ unzip -l /tmp/bnb/bitsandbytes-0.45.0-py3-none-win_amd64.whl | grep -E '(^|[[:space:]])tests/'
        0  2024-09-30 16:15   tests/__init__.py
     1047  2024-09-30 16:15   tests/conftest.py
     1675  2024-09-30 16:15   tests/helpers.py
    21879  2024-09-30 16:15   tests/test_autograd.py
     1626  2024-09-30 16:15   tests/test_cuda_setup_evaluator.py
    87397  2024-09-30 16:15   tests/test_functional.py
     4331  2024-09-30 16:15   tests/test_generation.py
     7912  2024-09-30 16:15   tests/test_linear4bit.py
     8864  2024-09-30 16:15   tests/test_linear8bitlt.py
    28167  2024-09-30 16:15   tests/test_modules.py
    25870  2024-09-30 16:15   tests/test_optim.py
     2648  2024-09-30 16:15   tests/test_triton.py
```

The presence of `tests/__init__.py` makes `tests` a **regular** package (not a PEP 420 namespace package). When Python's import machinery encounters a regular `tests` package on `sys.path` (from the wheel in `site-packages`) and a project-local `tests/` directory, it resolves `tests` to the regular package and **stops searching the other `tests/` directories for submodules** - the project's `tests/test_foo.py` becomes invisible. Hence `ModuleNotFoundError: No module named 'tests.test_foo'`.

Projects whose own `tests/` directory has no `__init__.py` (i.e., they rely on namespace packages) are unaffected because Python merges the two `tests/` directories in that case.

## Impact

- **High severity** for any project using `unittest` (or `pytest` with similar test-package layouts) that has a `tests/` package with an `__init__.py`. This includes the vast majority of Python projects.
- The bug is silent at install time - `pip install bitsandbytes` succeeds with no warning.
- The bug only manifests at test time, which makes it hard to trace back to a transitive dependency.

We hit this in a private consumer project where it broke the entire CI test suite (12 tests failed with `ModuleNotFoundError` on every push). The CI error pattern is `Ran N tests in 0.000s, FAILED (errors=N)` with every test marked as `_FailedTest` - a strong signal that the test loader could not import the test module.

## Suggested fix

The internal test suite should not be packaged into the wheel. Two options:

1. **Move the test suite** from `<repo-root>/tests/` to a non-colliding name (e.g., `<repo-root>/tests_internal/`) and update the CI configuration to use the new path.

2. **Exclude `tests/` from the wheel build** via `pyproject.toml` (hatch) or `MANIFEST.in` (setuptools):

   ```toml
   # pyproject.toml (hatch)
   [tool.hatch.build.targets.wheel]
   exclude = ["tests/"]
   ```

   ```
   # MANIFEST.in (setuptools) - explicit
   exclude tests/*
   ```

   The tests can still be run from the source repo via `pytest tests/` or `python -m unittest discover -s tests`, but they will not be installed into consumers' `site-packages`.

## Workaround for affected users (until fix lands)

Two options for consumers who cannot avoid installing `bitsandbytes` next to their own test package:

- **Remove `bitsandbytes` from CI** if it is only needed at training time. The `bitsandbytes` package is only required when actually using its quantization kernels; tests that mock it out do not need it installed.
- **Switch to `unittest discover`** to bypass the namespace shadow:
  ```bash
  python -m unittest discover -s tests -p "test_*.py" -v
  ```
  This tells the loader to look in the local `tests/` directory explicitly and bypasses the wheel-installed `tests` package.

## Full reproducer with context

A working reproducer on the consumer side is here: https://github.com/jmcloy622-ops/zeno
- Commit `c443e81` documents the consumer-side fix (removing `bitsandbytes` from CI install).
- Commit `6802cd4` documents the unsuccessful defensive `<0.45` pin attempt (which was defeated because 0.44.1 is also affected).
- GHA run `28854253107` is GREEN after the consumer-side fix; GHA run `28853722137` was RED with the same `ModuleNotFoundError` failure mode the proposed fix prevents.


## 评论 (1)

### matthewdouglas · 2026-07-07

This was fixed already since bitsandbytes >= 0.45.1.

We do not typically backport changes like this to older releases. There is no further action to take here. If you still encounter this issue in a newer release, please let me know and we can work on that.

