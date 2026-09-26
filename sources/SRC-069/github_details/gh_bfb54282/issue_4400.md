# [Issue #4400] [Bug][v0.6.18]tests/attention/test_cute_dsl_hca_dsv4.py AttributeError: module 'cutlass.cute.nvgpu.cpasync' has no attribute 'CopyBulkTensor2DGather4G2SOp'.

source: https://github.com/flashinfer-ai/flashinfer/issues/4400
state: closed | updated: 2026-09-21T04:30:59Z
labels: needs-triage, ci: health

## 正文

### Summary
Found this issue in FlashInfer CI.

### CI metadata
Test case: tests/attention/test_cute_dsl_hca_dsv4.py
FlashInfer commit: https://github.com/flashinfer-ai/flashinfer/commit/f363ec4e06f0cb112a1815d86c25ef3d529a49ec
Pipeline: [pipeline](https://nv/flashinfer-ci/-/pipelines/61492812)
Job name(s): unit_test_b300: [cu130], [cu129]
Branch: release-v0.6.18
Environment: b300

### Failed Jobs
[unit_test_b300](https://nv/flashinfer-ci/-/jobs/388041914): b300 / cu129
[unit_test_b300](https://nv/flashinfer-ci/-/jobs/388041915): b300 / cu130
### Failure
```shell
 E   AttributeError: module 'cutlass.cute.nvgpu.cpasync' has no attribute 'CopyBulkTensor2DGather4G2SOp'. Did you mean: 'CopyBulkTensorTileG2SOp'?
 /workspace/flashinfer/flashinfer/cute_dsl/attention/dsa/hca_fp8.py:691: AttributeError: module 'cutlass.cute.nvgpu.cpasync' has no attribute 'CopyBulkTensor2DGather4G2SOp'. Did you mean: 'CopyBulkTensorTileG2SOp'?
``` 
### Likely root cause
cutlass-dsl version dismatch.
https://github.com/flashinfer-ai/flashinfer/commit/985302cb8
### Reproduction command
```python
pytest 'tests.attention.test_cute_dsl_hca_dsv4'
``` 






## 评论 (1)

### bkryu · 2026-08-17

Thanks @nvamyt , the issue should have been fixed with #4368 which is merged. Closing as complete
