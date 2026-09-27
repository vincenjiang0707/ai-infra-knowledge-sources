# [Issue #227] the name DCGM_FI_DEV_XID_ERRORS is confusing in dcgm

source: https://github.com/NVIDIA/DCGM/issues/227
state: open | updated: 2025-05-21T16:21:10Z
labels: 

## 正文

The name xid_errors makes it look like a counter for number of xid_errors instead of the value of the xid_error.
DCGM_FI_DEV_XID_ERRORS
Should it be renamed to DCGM_FI_DEV_XID_ERROR to reflect the nature of the value?

## 评论 (1)

### bstollenvidia · 2025-05-21

The value of DCGM_FI_DEV_XID_ERROR is the actual XID number:
https://github.com/NVIDIA/DCGM/blob/6e947dcac9b3160d61d98fea4741d51d4bec5c1f/dcgmlib/src/DcgmCacheManager.cpp#L6800
