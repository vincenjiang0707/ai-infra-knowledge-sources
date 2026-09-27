# [Issue #363] Add local dispatch ID filtering

source: https://github.com/ROCm/rocprofiler-compute/issues/363
state: closed | updated: 2025-08-06T18:28:46Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
Currently, filtering by dispatch ID requires global dispatch IDs across all kernel launches of an application, making it difficult to single out the second launch of a specific kernel. To do this currently requires multiple runs of omniperf, or to run rocprof to get the global dispatch ID.
**Describe the solution you'd like**
This will likely require discussion to turn into a full-fledged feature. The solution I'm looking for is some sort of flag that you can add to a `-k 0` to get a "local" dispatch filtering to get any single instance of the kernel already selected by other filtering. Ideally it should be a different flag than `-d`.
**Describe alternatives you've considered**
**Additional context**
This functionality has been mentioned in passing at some DoE hackathons, and internally in my team.


## 评论 (3)

### ashesh2512 · 2024-10-02

Curious if there has been any movement on this front?

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/55

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
