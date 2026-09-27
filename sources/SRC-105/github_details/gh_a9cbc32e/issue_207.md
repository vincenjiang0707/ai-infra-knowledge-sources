# [Issue #207] Omniperf roofline does not display FP64 / General Roofline Datatype Support

source: https://github.com/ROCm/rocprofiler-compute/issues/207
state: closed | updated: 2025-08-06T18:34:51Z
labels: enhancement, Roofline

## 正文

**Is your feature request related to a problem? Please describe.**

The Omniperf roofline plots seem to collate fp32 and fp64 data types, but labels read as FP32 rates only leading to user confusion.  


**Describe the solution you'd like**

It would help if these were separated to help with immediate interpretability or at least have the option for users. Further, it would be nice to have a `--roofline-datatype=${DTYPE}` option to isolate *any* specific datatype ops to its own roofline plot (e.g. FP64 / FP32 / INT32 / FP16 / BF16 /  INT8 / INT4 / etc...). The lower precision datatypes would be useful for profiling future machine learning inference cases.



## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/71

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
