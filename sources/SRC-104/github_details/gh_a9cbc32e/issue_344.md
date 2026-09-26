# [Issue #344] Kernel menu items are too big (web GUI)

source: https://github.com/ROCm/rocprofiler-compute/issues/344
state: closed | updated: 2025-08-06T18:29:36Z
labels: bug

## 正文

**Describe the bug**
The height of the items in the Kernel dropdown is too big (150 pixels!). 


**To Reproduce**

omniperf analyze -p <path_to_profile> --gui

click Kernel menu drop-down

**Expected behavior**
The height of the items should be the same height as the dropdown (36 pixels).

**Screenshots**

Actual:
![menu_big](https://github.com/ROCm/omniperf/assets/143630488/50c38f4b-084d-4fa2-8f1c-b86ccc836275)

Expected (example, height = 36 pixels):
![menu_small](https://github.com/ROCm/omniperf/assets/143630488/dea6aacd-4050-4c70-a266-e44e7314ca6e)



## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/59

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
