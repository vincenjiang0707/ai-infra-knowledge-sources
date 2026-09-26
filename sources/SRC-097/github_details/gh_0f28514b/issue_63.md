# [Issue #63] Correctly resolve UCX/UCX_MO dependencies

source: https://github.com/ai-dynamo/nixl/issues/63
state: closed | updated: 2026-08-19T15:54:17Z
labels: enhancement

## 正文

With the introduction of Multi-Object (MO) UCX backend (PR #58) that depends on UCX backend we need to make sure the dependency is properly handled for all static/dynamic plugin configurations.

Initial thoughts to consider:
* UCX is a plugin => UCX MO is a plugin and it just includes the code from UCX backend and not have plugin-to-plugin dependency
* UCX is static => 2 options
  * UCX_MO has to be static as well
  * UCX_MO can be whatever, but if it's a plugin:
     * Either it relies on libnixl for UCX backend functionality
     * OR we build UCX_MO plugin so such that UCX symbols are not conflicting with UCX backend code that is part of libnixl. This would require some investigation

## 评论 (2)

### ANormalMan12 · 2025-05-15

I am really curious about why it is essential to introduce UCX_MO in NIXL. Any explanations over this issue would be appreciated. Thanks.

### rakhmets · 2026-08-19

UCX_MO plugin has been removed. https://github.com/ai-dynamo/nixl/pull/898
