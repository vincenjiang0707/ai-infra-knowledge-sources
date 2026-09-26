# [Issue #577] Use NIXL Logging in nixlbench

source: https://github.com/ai-dynamo/nixl/issues/577
state: open | updated: 2026-09-03T09:50:19Z
labels: Test

## 正文

(empty)

## 评论 (1)

### cyclinder · 2026-09-03

Hi, I'd like to work on this issue.
 
I confirmed that nixlbench still uses std::cout/std::cerr extensively.
Before starting, could you clarify the intended scope?
 
My proposed approach is:
1. Keep benchmark result tables and explicitly requested output on stdout.
2. Move diagnostics, warnings, errors, and initialization messages to
  NIXL logging with appropriate severity levels.
3. Add focused tests where output behavior is externally observable.

Should nixlbench consume the existing internal nixl_log.h, or should this
work first expose a supported logging interface for external NIXL tools?
