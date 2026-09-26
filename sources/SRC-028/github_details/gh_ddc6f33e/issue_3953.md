# [Issue #3953] Failed build: MaxText Package Tests

source: https://github.com/AI-Hypercomputer/maxtext/issues/3953
state: closed | updated: 2026-06-11T22:51:00Z
labels: build failed

## 正文

GitHub Actions workflow [MaxText Package Tests #13171](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26133987009) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [814208fb19b5a0d6f6821fc9ddb5da027b0f4af8](https://github.com/AI-Hypercomputer/maxtext/commit/814208fb19b5a0d6f6821fc9ddb5da027b0f4af8)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

## 评论 (22)

### github-actions[bot] · 2026-05-20

### 🤖 CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline (specifically the "MaxText Package Tests" workflow) and identified two likely root causes introduced in recent merges.

#### 🔍 What Failed
* **Job/Matrix**: `tpu-integration tests` (Flavor: `tpu-integration`)
* **Failing Test**: `tests/integration/aot_identical_test.py::AotHloIdenticalTest::test_default_hlo_match`
* **Error**: `AssertionError: HLO file is not identical...`

* **Job/Matrix**: `maxtext_tpu_pathways_integration_tests`
* **Failing Test**: `tests/integration/checkpointing_test.py` (and potentially other NNX training tests)
* **Error**: Likely `TypeError: int() argument must be... not 'Variable'` or `Orbax already exists` (Double-Save race condition).

#### 🪵 Error Details & Stack Trace
**Failure Mode 1: AOT HLO Mismatch**
The HLO headers containing debug metadata (source mappings) differ between AOT and Real runs. Recent JAX/XLA nightly introduced `parent_frame_id`, which is not filtered by the current regex.
```python
# tests/integration/aot_identical_test.py
location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id)=[^}]*\}\s*$")
# If line contains parent_frame_id, it doesn't match and the line is NOT skipped, causing hash mismatch.
```

**Failure Mode 2: NNX Checkpointing Logic Error**
The `maybe_save_checkpoint` function incorrectly attempts to cast an `nnx.Variable` to an integer without accessing its value.
```python
# src/maxtext/common/checkpointing.py
if config.pure_nnx:
    actual_step = int(state.optimizer.step) - 1  # BUG: should be state.optimizer.step.get_value()
```

#### 💡 Root Cause Analysis & Context
**Confidence:** High

1.  **Incomplete Regex in PR #3947**: PR #3947 intended to fix AOT false-positives on JAX nightly by adding `file_location_id` to the HLO header filter. However, the PR description explicitly mentioned `parent_frame_id` as a new field, but the committed regex missed it. This causes failures in environments with newer JAX/XLA where this field is present.
2.  **TypeError in PR #3945**: PR #3945 introduced a check to prevent double-saving checkpoints. In the NNX path, it uses `int(state.optimizer.step)`. While this might pass in some local environments or unit tests (where the state is mocked), in a real sharded training run, `state.optimizer.step` is a Variable/Array that requires proper value access. Furthermore, the check is racy for **asynchronous** saves because `checkpoint_manager.latest_step()` only updates after the save commits.

#### 🛠️ Recommended Fix
**1. Fix AOT Regex in `tests/integration/aot_identical_test.py`:**
```python
<<<<
    location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id)=[^}]*\}\s*$")
====
    location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id|parent_frame_id)=[^}]*\}\s*$")
>>>>
```

**2. Fix Step Calculation in `src/maxtext/common/checkpointing.py`:**
```python
<<<<
    if config.pure_nnx:
      actual_step = int(state.optimizer.step) - 1
====
    if config.pure_nnx:
      actual_step = int(state.optimizer.step.get_value()) - 1
>>>>
```

### github-actions[bot] · 2026-05-20

GitHub Actions workflow [MaxText Package Tests #13188](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26143050268) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [154e9b75c89ad5a6e31e763720c5d87ed2b56bb7](https://github.com/AI-Hypercomputer/maxtext/commit/154e9b75c89ad5a6e31e763720c5d87ed2b56bb7)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-20

GitHub Actions workflow [MaxText Package Tests #13209](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26152675668) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [154e9b75c89ad5a6e31e763720c5d87ed2b56bb7](https://github.com/AI-Hypercomputer/maxtext/commit/154e9b75c89ad5a6e31e763720c5d87ed2b56bb7)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-20

GitHub Actions workflow [MaxText Package Tests #13211](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26163596282) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [154e9b75c89ad5a6e31e763720c5d87ed2b56bb7](https://github.com/AI-Hypercomputer/maxtext/commit/154e9b75c89ad5a6e31e763720c5d87ed2b56bb7)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-20

GitHub Actions workflow [MaxText Package Tests #13223](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26177559817) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [154e9b75c89ad5a6e31e763720c5d87ed2b56bb7](https://github.com/AI-Hypercomputer/maxtext/commit/154e9b75c89ad5a6e31e763720c5d87ed2b56bb7)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-21

GitHub Actions workflow [MaxText Package Tests #13332](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26216547649) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [b30b2d27a83f6d3c1cdd21ee580faf90e740c523](https://github.com/AI-Hypercomputer/maxtext/commit/b30b2d27a83f6d3c1cdd21ee580faf90e740c523)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-21

GitHub Actions workflow [MaxText Package Tests #13342](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26240318519) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [ee8f49c92a719040e6c28a61fcb6937d71b7a370](https://github.com/AI-Hypercomputer/maxtext/commit/ee8f49c92a719040e6c28a61fcb6937d71b7a370)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-21

### 🤖 CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline and identified the following:

#### 🔍 What Failed
* **Job/Matrix**: `tpu-integration tests`
* **Failing Test**: `tests/integration/aot_identical_test.py::AotHloIdenticalTest::test_default_hlo_match`
* **Error**: `AssertionError: HLO file is not identical...` (Hash mismatch)

* **Job/Matrix**: `maxtext_tpu_pathways_integration_tests`
* **Failing Test**: NNX training tests (e.g., in `tests/integration/checkpointing_test.py`)
* **Error**: `TypeError: int() argument must be a string, a bytes-like object or a real number, not 'Variable'`

#### 🪵 Error Details & Stack Trace
```python
# Failure 1 (AOT HLO Mismatch)
# The HLO header mappings have changed in recent JAX/XLA nightlies,
# adding 'parent_frame_id' which is not captured by the current cleanup regex.

# Failure 2 (NNX Checkpointing Logic Error)
# File "src/maxtext/common/checkpointing.py", line 791, in maybe_save_checkpoint
#   actual_step = int(state.optimizer.step) - 1
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'Variable'
```

#### 💡 Root Cause Analysis & Context
**Confidence:** high

1. **AOT HLO Mismatch**: A recent update to JAX/XLA nightly introduced a new field `parent_frame_id` in the HLO metadata headers. The `location_map_pattern` regex in `tests/integration/aot_identical_test.py` only accounts for `file_name_id` and `file_location_id`, causing it to miss the new field during cleanup. This results in inconsistent hashes between AOT-compiled HLOs and real-run HLOs.

2. **NNX Checkpointing Logic Error**: In the newly introduced `src/maxtext/common/checkpointing.py` (via PR #3960), the code attempts to convert `state.optimizer.step` to an integer using `int()`. In Flax NNX, `optimizer.step` is an `nnx.Variable` object, which cannot be directly cast to an integer. It must be accessed via `.value` or `.get_value()`.

#### 🛠️ Recommended Fix
```python
# Fix 1: Update regex in tests/integration/aot_identical_test.py (Line 88)
# location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id|parent_frame_id)=[^}]*\}\s*$")

# Fix 2: Access .value in src/maxtext/common/checkpointing.py (Line 791)
# actual_step = int(state.optimizer.step.value) - 1
```


### github-actions[bot] · 2026-05-21

GitHub Actions workflow [MaxText Package Tests #13371](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26251548708) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [fb79a9e8b2c465248874212202dc27a9e38363e4](https://github.com/AI-Hypercomputer/maxtext/commit/fb79a9e8b2c465248874212202dc27a9e38363e4)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-22

GitHub Actions workflow [MaxText Package Tests #13380](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26261425692) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [a8be563d9c30b0e42f522e3017fa638d2b0ccebb](https://github.com/AI-Hypercomputer/maxtext/commit/a8be563d9c30b0e42f522e3017fa638d2b0ccebb)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-22

### 🤖 CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline and identified two primary root causes introduced in recent merges.

#### 🔍 What Failed
* **Job/Matrix**: `tpu-integration tests`
* **Failing Test**: `tests/integration/aot_identical_test.py::AotHloIdenticalTest::test_default_hlo_match`
* **Error**: `AssertionError: HLO file is not identical...` (Hash mismatch)

* **Job/Matrix**: `maxtext_tpu_pathways_integration_tests`
* **Failing Test**: NNX training tests (e.g., in `tests/integration/checkpointing_test.py`)
* **Error**: `TypeError: int() argument must be a string, a bytes-like object or a real number, not 'Variable'`

#### 🪵 Error Details & Stack Trace
```python
# Failure 1 (AOT HLO Mismatch)
# The HLO header mappings have changed in recent JAX/XLA nightlies,
# adding 'parent_frame_id' which is not captured by the current cleanup regex.
# File: tests/integration/aot_identical_test.py, Line 88

# Failure 2 (NNX Checkpointing Logic Error)
# File: src/maxtext/common/checkpointing.py", line 791, in maybe_save_checkpoint
#   actual_step = int(state.optimizer.step) - 1
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'Variable'
```

#### 💡 Root Cause Analysis & Context
**Confidence:** High

1.  **AOT HLO Mismatch**: PR #3947 updated the HLO header filter to include `file_location_id` but missed `parent_frame_id`, which was also introduced in recent JAX/XLA nightly versions. This causes the AOT identical test to fail when comparing sharded vs. unsharded HLO graphs because the debug metadata remains in the "cleaned" files, leading to hash mismatches.
2.  **NNX Checkpointing Logic Error**: A recent transition to Flax NNX introduced a check in `maybe_save_checkpoint` to prevent double-saving. However, it incorrectly attempts to cast `state.optimizer.step` (which is an `nnx.Variable` in the pure NNX path) directly to an `int`. This fails in real integration tests where the variable must be accessed via `.get_value()` (as correctly done in `src/maxtext/trainers/pre_train/train.py`).

#### 🛠️ Recommended Fix
**1. Update regex in `tests/integration/aot_identical_test.py`:**
```python
<<<<
    location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id)=[^}]*\}\s*$")
====
    location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id|parent_frame_id)=[^}]*\}\s*$")
>>>>
```

**2. Access `.get_value()` in `src/maxtext/common/checkpointing.py`:**
```python
<<<<
    if config.pure_nnx:
      actual_step = int(state.optimizer.step) - 1
====
    if config.pure_nnx:
      actual_step = int(state.optimizer.step.get_value()) - 1
>>>>
```


### github-actions[bot] · 2026-05-22

GitHub Actions workflow [MaxText Package Tests #13394](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26278762638) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [7c8d6586f057cd8b2b8ae3ea74db1d74d93a837a](https://github.com/AI-Hypercomputer/maxtext/commit/7c8d6586f057cd8b2b8ae3ea74db1d74d93a837a)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-22

GitHub Actions workflow [MaxText Package Tests #13397](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26288607638) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [7c8d6586f057cd8b2b8ae3ea74db1d74d93a837a](https://github.com/AI-Hypercomputer/maxtext/commit/7c8d6586f057cd8b2b8ae3ea74db1d74d93a837a)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-23

GitHub Actions workflow [MaxText Package Tests #13435](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26318571434) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [6c2701d59263455d73822bdfc1f72eef00f02525](https://github.com/AI-Hypercomputer/maxtext/commit/6c2701d59263455d73822bdfc1f72eef00f02525)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-23

GitHub Actions workflow [MaxText Package Tests #13439](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26337679382) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-23

GitHub Actions workflow [MaxText Package Tests #13440](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26342524741) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-24

GitHub Actions workflow [MaxText Package Tests #13441](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26347586169) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-24

GitHub Actions workflow [MaxText Package Tests #13444](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26356798212) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-24

GitHub Actions workflow [MaxText Package Tests #13447](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26371752035) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-25

GitHub Actions workflow [MaxText Package Tests #13448](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26377271143) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-25

GitHub Actions workflow [MaxText Package Tests #13469](https://github.com/AI-Hypercomputer/maxtext/actions/runs/26410733291) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [4110d139cc2a8a3d4fab53cd5568028a7897568f](https://github.com/AI-Hypercomputer/maxtext/commit/4110d139cc2a8a3d4fab53cd5568028a7897568f)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-05-25

### 🤖 CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline (specifically the "MaxText Package Tests" workflow) and identified two primary root causes introduced in recent merges to `main`.

#### 🔍 What Failed
* **Job/Matrix**: `tpu-integration tests` (Flavor: `tpu-integration`)
* **Failing Test**: `tests/integration/aot_identical_test.py::AotHloIdenticalTest::test_default_hlo_match`
* **Error**: `AssertionError: HLO file is not identical...` (Hash mismatch due to incomplete metadata filtering)

* **Job/Matrix**: `maxtext_tpu_pathways_integration_tests`
* **Failing Test**: NNX training tests (e.g., in `tests/integration/checkpointing_test.py`)
* **Error**: `TypeError: int() argument must be a string, a bytes-like object or a real number, not 'Variable'`

#### 🪵 Error Details & Stack Trace
**Failure 1: AOT HLO Mismatch**
The HLO headers containing debug metadata (source mappings) differ between AOT and Real runs. Recent JAX/XLA nightly introduced `parent_frame_id`, which is not filtered by the current regex, causing hash mismatches.
```python
# tests/integration/aot_identical_test.py
location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id)=[^}]*\}\s*$")
# Misses parent_frame_id, so the line is NOT skipped.
```

**Failure 2: NNX Checkpointing Logic Error**
The `maybe_save_checkpoint` function incorrectly attempts to cast an `nnx.Variable` to an integer without accessing its value.
```python
# src/maxtext/common/checkpointing.py (Line 791)
actual_step = int(state.optimizer.step) - 1
# TypeError: int() argument must be ... not 'Variable'
```

#### 💡 Root Cause Analysis & Context
**Confidence:** High

1.  **Incomplete Regex**: PR #3947 updated the HLO header filter to include `file_location_id` but missed `parent_frame_id`, which was also introduced in recent JAX/XLA versions. This causes the AOT identical test to fail when comparing sharded vs. unsharded HLO graphs because the debug metadata remains in the \"cleaned\" files.
2.  **NNX Checkpointing Regression**: PR #3945 (or similar recent NNX transitions) introduced a check to prevent double-saving checkpoints. In the pure NNX path, `state.optimizer.step` is an `nnx.Variable` object, which cannot be directly cast to an integer. It must be accessed via `.get_value()` or `.value`.

#### 🛠️ Recommended Fix

**1. Update regex in `tests/integration/aot_identical_test.py` (Line 88):**
```python
<<<<
    location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id)=[^}]*\}\s*$")
====
    location_map_pattern = re.compile(r"^\s*\d+\s+\{(file_name_id|file_location_id|parent_frame_id)=[^}]*\}\s*$")
>>>>
```

**2. Correct step access in `src/maxtext/common/checkpointing.py` (Line 791):**
```python
<<<<
      actual_step = int(state.optimizer.step) - 1
====
      actual_step = int(state.optimizer.step.get_value()) - 1
>>>>
```
