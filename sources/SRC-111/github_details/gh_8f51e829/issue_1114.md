# [Issue #1114] Trace hash_ids are not properly scoped

source: https://github.com/vllm-project/guidellm/issues/1114
state: closed | updated: 2026-09-11T22:34:12Z
labels: internal, priority-critical

## 正文

### Bug Description

In Mooncake datasets hash_ids are shared across all dataset rows so that a block of text which exists in one row can be matched to other rows. This is to ensure that the prefix hash hit rate stays similar to the original traced data while still allowing for the use of synthetic data. In WEKA hash ids may either be global or local to a row, since rows can contain multiple request unlike Mooncake. 

As currently implemented WEKA support does not respect the global/local hash_ids indicator and performs a halfway in-between that does not properly implement either mode. The code currently uses the same globally scoped storage as Mooncake, but then resets the storage between rows.

### Expected Behavior

The "reset" mechanism should be removed and instead WEKA should use the following logic for each row:

1. If `row.hash_id_scope == "global"` or unset, use the same global storage method as Mooncake
2. If `row.hash_id_scope == "local"` use a temporary local variable for hash storage and discard after the row is emitted.

### Steps to Reproduce

Run any WEKA dataset with a mix of local/global scoped items.

### Operating System

Fedora 44

### Python Version

Python 3.13.15

### GuideLLM Version

main

### Installation Method

Other

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell

```

### Additional Context

_No response_

## 评论 (1)

### jaredoconnell · 2026-09-11

Fixed by #1134 
