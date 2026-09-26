# [Issue #1599] Report list: group same-model reports for display, without merging report directories

source: https://github.com/modelscope/evalscope/issues/1599
state: closed | updated: 2026-09-10T08:17:59Z
labels: 

## 正文

### Context

Our eval workflow runs one model against datasets incrementally—often as separate invocations (different dataset, different day) rather than one big run. The report list therefore ends up with N rows per model. For example, a model evaluated on 6 datasets across 3 separate runs appears as 3 unrelated rows, with no way to see the model's full picture without opening each report individually.

We tried solving this by physically merging report directories in #1570. @Yunnglin correctly closed it:

> I'm closing this because the feature mutates/deletes source evaluation runs, which conflicts with EvalScope treating reports as immutable audit records. The merged `task_config.yaml` only keeps the first source run's config, so the report claims one setup produced scores that came from different settings; logs and `collection_detailed_report.json` are also dropped. The underlying need—seeing one model across multiple datasets—is better solved in the viewer layer, and the framework already supports it: resuming an existing run with an extended dataset list via `use_cache` writes everything into one directory with honest provenance.
>
> Could you open an issue describing the original scenario instead?

This is that issue, along with a working alternative.

### Going forward vs. already-split history

For *new* runs, `use_cache` + an extended `datasets` list already does the right thing (confirmed).

However, this doesn't help with runs that are already split across directories, nor does it provide a fast way to see cross-dataset coverage per model in the list UI generally. Using `use_cache` in this case would mean re-evaluating every dataset that isn't already present in whichever single directory you resume from, since `use_cache`'s cache lookup is scoped to one `work_dir`.

### Proposed / implemented: view-layer grouping, no file mutation

We put together a display-only alternative and would like feedback before opening a PR:

* `GET /api/v1/reports?group_by=model` rolls same-model report-list items into one row each, entirely in memory, using metadata the endpoint already loads for the flat list (`_build_report_meta` results grouped by `model_name`). No report is read, written, moved, or merged.
* Each group carries `children`: every constituent report exactly as the flat list describes it, with its own `run_id`, `model_id`, and `primary_metrics`. This means a group never shows a fabricated combined score.
* If a dataset appears in more than one of the model's reports, there is no silent "winner"; both remain visible under their respective reports when the group is expanded.
* The report list UI adds a **Group by model** toggle that renders these as expandable rows, reusing the existing `ReportsTable` / `ReportCard` components for the expanded children, so no new row-rendering logic is needed.
* The group's **Compare all** action reuses the existing multi-report Compare flow (`report=` query params), which is already used by `/api/v1/reports/charts/<type>`.

We have this working end-to-end against a real multi-run output directory, with backend and frontend tests passing and `tsc` / `eslint` clean.

Happy to open a PR, reusing the `SelectionTray` / list UI pieces from #1570 where relevant. We wanted to confirm first that the shape of `group_by=model`—including the field names and duplicate-dataset display—is agreeable, per your comment on #1570.


## 评论 (3)

### Dhru1001 · 2026-08-19

@Yunnglin 

### linhongyu510 · 2026-09-01

Thanks for keeping this open. I rebased the design against the current report-list API and would like to confirm the contract before opening a PR:

1. Omitting `group_by` keeps the flat response unchanged except for an additive `kind="report"` discriminator.
2. `group_by=model` groups the filtered report summaries by exact `model_name`, before pagination.
3. The grouped page returns `kind="model_group"` items with:
   - `group_key`
   - `model_name`
   - `report_count`
   - `dataset_count`
   - `latest_timestamp`
   - `children: ReportSummary[]`
4. A group carries no aggregate score or merged task config. Every score remains on its original child with its own `run_id` and `model_id`.
5. Duplicate datasets remain as separate children. "Compare all" passes every child report reference to the existing compare flow.
6. `total` counts groups in grouped mode; filters are applied to children before grouping; pagination is applied after grouping.

Does this response shape and ordering semantics match the intended viewer-only solution?

### Dhru1001 · 2026-09-04

Thanks for taking the time to work through this — really appreciate it. Here's how it maps to what we ended up building (opened as #1703), so we can compare against the real diff rather than descriptions:

1. Agreed: omitting `group_by` leaves the flat response unchanged. We took a slightly different path and didn't add a `kind` discriminator to flat items — the flat and grouped listings are two separate response models (`ListReportsResponse` vs `ListReportsGroupedResponse`), called as two separate client functions. Mainly so the flat endpoint's contract stays untouched, especially now that #1658 made API contracts derive from Pydantic.
2. Agreed on grouping by exact `model_name`, filter-then-group, paginate-after-group, `total` counting groups in grouped mode.
3. Our `ReportGroup` shape ended up a little different:
   - `timestamp` (not `latest_timestamp`) — same field name `ReportSummary` already uses, so the existing sort-by-time logic works for both flat and grouped rows without changes.
   - `dataset_name` — comma-joined string of the group's distinct dataset names, same field/type as a flat row.
   - `num_samples` — sum across children, used by the existing `ReportCard`/`ReportsTable`.
   - `refs` — list of `"run_id/model_id"` per child, which feeds the existing multi-report Compare flow for the group's "Compare all" action.
   - No `kind` or `group_key` field.
4–6. Match what you described: no aggregate/merged score, duplicate datasets stay as separate children, Compare-all passes every child ref, filters applied before grouping / pagination after.

Would you mind taking a look at #1703 when you get a chance? Would love your thoughts on it, and happy to adjust based on your feedback.
