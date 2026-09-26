# [Issue #3170] remove literal list parsing "[...]" form doc_to_target

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3170
state: open | updated: 2026-08-26T12:49:51Z
labels: 

## 正文

Currently we check if the target string can be parsed as a list and parse it if so:
https://github.com/EleutherAI/lm-evaluation-harness/blob/8c05cfe04fafcdd41dd64019f2b3797ef54dcd81/lm_eval/api/task.py#L1332-L1338

However this should be handled at the dataset level as it creates ambiguity, where the target _string_ might be list-like. Tasks that need list targets should explicitly return lists from their doc_to_target implementation rather than relying on string parsing. 

This also causes `bigbench_list_functions_generate_until` to produce incorrect results, as the task expects literal string representations of lists (e.g., "[1, 2, 3]") to be evaluated as strings.

Will need to test, which tasks rely on this condition before removing.

## 评论 (1)

### nata2627 · 2026-08-26

> Will need to test, which tasks rely on this condition before removing.

Counted this on `main` (`64f3d09`) while looking at the issue for other reasons.
312 task configs render a Python list through the template and depend on the
parse to get it back:

| pattern | configs |
| --- | --- |
| `doc_to_target: "{{gold}}"` | 274 (agieval, arabic_leaderboard) |
| `doc_to_target: "{{answers}}"` | 35 (longbench, mlqa) |
| `doc_to_target: "{{answer_nodes}}"` | 2 (graphwalks) |
| `doc_to_target: "{{outputs}}"` | 1 (ruler niah) |

The surface is narrower than the 2267 configs that set `doc_to_target` at all.
Where it names a dataset column, `doc[doc_to_target]` returns before the string
branch is reached, so those tasks already hand back a real list and are
unaffected. Only templated targets reach `literal_eval`.

`bigbench_list_functions_generate_until` behaves as described: it inherits
`doc_to_target: "{{targets[0]}}"` from `generate_until_template_yaml`, and that
subtask's targets are strings like `"[1, 2, 3]"`, so the gold answer is turned
into a list before `exact_match` compares it.

Not working on this — posting the count in case it helps size the change.

