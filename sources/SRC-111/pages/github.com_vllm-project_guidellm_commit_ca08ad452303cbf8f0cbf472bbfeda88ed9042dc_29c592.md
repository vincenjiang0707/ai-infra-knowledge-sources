source: https://github.com/vllm-project/guidellm/commit/ca08ad452303cbf8f0cbf472bbfeda88ed9042dc

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Useful for multiturn dags that embed their own history, rather than using DAG history.
Generated-by: Cursor AI Composor 2.5
Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Copy file name to clipboardExpand all lines: docs/guides/multiturn.md

+1Lines changed: 1 addition & 0 deletions

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -172,6 +172,7 @@ Each per-request entry in `benchmarks.json` includes:

172

172

173

173

-`info.history_len`: the number of prior messages in the assembled history sent to the server with that request. Because history can include messages from diverging paths that merge via `last` edges, `history_len` may jump at merge points rather than increment by one. Branch roots spawned with fresh (`new`) context start at `0`.

174

174

-`info.turn_index`: a simpler path-depth counter. It resets to `0` on `new` edges, increments by one through `full` edges, and treats each `last` edge as adding up to `1` without walking further into that parent’s ancestors. When a node has multiple parents, `turn_index` is the maximum over those contributions (the longest path).

175

+

-`info.preceding_nodes`: the number of graph nodes that precede this request in topological execution order (0-based). Unlike `turn_index` and `history_len`, this is independent of `history_context`. Use it when replay uses `history_context=new` (for example OTEL `history=trace`) and `turn_index` stays at `0` for every request. Recorded tool loops add extra graph nodes (call + injection), so `preceding_nodes` counts DAG nodes, not raw LLM spans. Parallel sub-agent siblings may receive different values based on topological tie-breaking.

175

176

176

177

At a merge after a sub-agent branch, `history_len` often exceeds `turn_index` because merged `last` outputs are counted in assembled history but only add up to a non-recursive `1` toward path depth (and do not increase `turn_index` when the `full` path is already longer).

## 0 commit comments