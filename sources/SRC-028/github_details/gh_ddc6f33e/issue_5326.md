# [Issue #5326] Failed build: MaxText Package Tests

source: https://github.com/AI-Hypercomputer/maxtext/issues/5326
state: closed | updated: 2026-09-23T01:22:58Z
labels: build failed

## 正文

GitHub Actions workflow [MaxText Package Tests #8045](https://github.com/AI-Hypercomputer/maxtext/actions/runs/35671041446) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [c28166ca7de7f3b3cbca34ea3989fe50bb8c8c46](https://github.com/AI-Hypercomputer/maxtext/commit/c28166ca7de7f3b3cbca34ea3989fe50bb8c8c46)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

## 评论 (3)

### github-actions[bot] · 2026-09-22

### CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline and identified the following:

#### What Failed
* **Job/Matrix**: CPU Pretrain Tests (cpu-integration) / Execute Tests (1) / cpu-integration
* **Failing Test**: tests/integration/train_tests.py::TrainTests::test_moe_nanoo_fp8
* **Error**: google.api_core.exceptions.PreconditionFailed: 412 POST https://storage.googleapis.com/upload/storage/v1/b/runner-maxtext-logs/o?uploadType=multipart&ifGenerationMatch=...

#### Error Details and Stack Trace
```python
Exception ignored in atexit callback: <function FileWriter.__init__.<locals>.cleanup at 0x7d4f90162a20>
Traceback (most recent call last):
  File "/__w/maxtext/maxtext/.venv/lib/python3.12/site-packages/tensorboardX/writer.py", line 122, in cleanup
    self.event_writer.close()
  File "/__w/maxtext/maxtext/.venv/lib/python3.12/site-packages/tensorboardX/event_file_writer.py", line 153, in close
    self.flush()
  ...
  File "/__w/maxtext/maxtext/.venv/lib/python3.12/site-packages/google/cloud/storage/blob.py", line 2875, in _prep_and_do_upload
    _raise_from_invalid_response(exc)
  File "/__w/maxtext/maxtext/.venv/lib/python3.12/site-packages/google/cloud/storage/blob.py", line 5240, in _raise_from_invalid_response
    raise exceptions.from_http_status(response.status_code, message, response=response)
google.api_core.exceptions.PreconditionFailed: 412 POST https://storage.googleapis.com/upload/storage/v1/b/runner-maxtext-logs/o?uploadType=multipart&ifGenerationMatch=1789978520387600
```

#### Root Cause Analysis and Context
**Confidence:** high
**Category**: Infrastructure/Environment Flake (GCS Concurrency Conflict)

* **Analysis**:
  The failure is caused by an **optimistic concurrency control conflict (HTTP 412 Precondition Failed)** when uploading TensorBoard logs to Google Cloud Storage (GCS).
  During parallel execution of `cpu-integration` tests with `pytest-xdist`, both `test_moe_fp8` and `test_moe_nanoo_fp8` run `train_main` using downscaled MoE model configurations. Unlike `test_moe_nanoo_fp8_sparse_matmul`, `test_moe_nanoo_fp8` does not have `"enable_tensorboard=False"` in its arguments. 
  When multiple tests run concurrently and write event logs to the same shared directory inside the GCS bucket `runner-maxtext-logs`, they step on each other us toes. During the `atexit` writer cleanup, `tensorboardX` flushes files to GCS using precondition-guarded upload requests (e.g. `ifGenerationMatch`). Because another worker has already modified the destination blob, the precondition fails, raising a fatal `PreconditionFailed` exception.

#### Recommended Fix
To stabilize the parallel CI pipeline and permanently prevent GCS concurrency conflicts during integration testing, we should disable TensorBoard logging in these tests.

Apply the following change in `tests/integration/train_tests.py`:

```diff
diff --git a/tests/integration/train_tests.py b/tests/integration/train_tests.py
index b0a84e5..8c199db 100644
--- a/tests/integration/train_tests.py
+++ b/tests/integration/train_tests.py
@@ -525,7 +525,7 @@ class TrainTests(unittest.TestCase):
 
   @pytest.mark.integration_test
   def test_moe_nanoo_fp8(self):
-    train_main(TrainTests.CONFIGS["moe"] + ["quantization=nanoo_fp8"])
+    train_main(TrainTests.CONFIGS["moe"] + ["quantization=nanoo_fp8", "enable_tensorboard=False"])
 
   @pytest.mark.integration_test
   def test_moe_fp8_token_dropping(self):
```


### github-actions[bot] · 2026-09-22

GitHub Actions workflow [MaxText Package Tests #8081](https://github.com/AI-Hypercomputer/maxtext/actions/runs/35725280580) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [a6ff7038d42e8b5c5308e3a3bf14eac8d0f862e2](https://github.com/AI-Hypercomputer/maxtext/commit/a6ff7038d42e8b5c5308e3a3bf14eac8d0f862e2)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

### github-actions[bot] · 2026-09-22

GitHub Actions workflow [MaxText Package Tests #8098](https://github.com/AI-Hypercomputer/maxtext/actions/runs/35777903542) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [449365d1632f6b4743f7cb81809980c5587bf912](https://github.com/AI-Hypercomputer/maxtext/commit/449365d1632f6b4743f7cb81809980c5587bf912)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>
