# [Issue #1976] Promote tracing plugin contract (src/core/tracing/trace_plugin.h) to a public installed header

source: https://github.com/ai-dynamo/nixl/issues/1976
state: open | updated: 2026-08-25T14:58:59Z
labels: 

## 正文

`src/core/tracing/trace_plugin.h` defines the tracing plugin contract but
lives under `src/core/`, not an installed public header. `docs/tracing.md`
notes that promoting it from internal to public is a non-breaking change
"if an external consumer appears."

We're that consumer: we're building an out-of-tree trace backend plugin
(for a KV-transfer observability pipeline) that needs to implement this
contract from outside the NIXL source tree, against an installed NIXL
package rather than a private in-tree checkout.

Ask: install `trace_plugin.h` (and whatever transitive headers it depends
on) alongside NIXL's other public headers in the packaged
install/CMake-export output, and document it as a supported extension
point. Happy to help validate against our out-of-tree plugin once it's
available.


## 评论 (2)

### brminich · 2026-08-04

can you please provide a bit more details on what this plugin is and why it can't be in-tree?

### brminich · 2026-08-25

@catyans can you pls provide some details on what this plugin is?
