# [Issue #3029] [FEA] Add CopyReduceBulkS2G

source: https://github.com/NVIDIA/cutlass/issues/3029
state: open | updated: 2026-09-24T03:19:56Z
labels: feature request, ? - Needs Triage, inactive-90d, CuTe DSL

## 正文

### Which component requires the feature?

CuTe DSL

### Feature Request

**Is your feature request related to a problem? Please describe.**
There's already CopyBulkS2G and CopyReduceBulkTensorS2G, but there's no CopyReduceBulkS2G (i.e. `cp.reduce.async.bulk.global.share` ptx instruction). 

We use this in Flashattention for dQ reduction. Currently the workaround is to call ptx directly but it would be much better to have a CopyOp for this.
https://github.com/Dao-AILab/flash-attention/blob/c4d8b0630eb81cf88206e0cc9e9bff4e7806d88f/flash_attn/cute/flash_bwd_sm100.py#L2563

## 评论 (5)

### Edenzzzz · 2026-02-16

Sometimes I feel adding another layer of abstraction makes it more complicated

### github-actions[bot] · 2026-03-18

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### BlueArchive-Sensei · 2026-04-10

Thanks for your report. Let us have a discussion for this issue.

### github-actions[bot] · 2026-07-09

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### 0z5a · 2026-09-24

Hi @tridao ,I'd like to pick this up.

I'll scope the first pass around adding a proper `CopyReduceBulkS2G` path for the non-tensor-map `cp.reduce.async.bulk.global.shared` use case, starting with the reduction mode needed by the existing dQ reduction consumer.

The implementation/validation scope would be:

* add the corresponding CuTe CopyOp / lowering path without changing the existing tensor-map reduction path;
* cover the required alignment, size, async-group commit/wait, and proxy-fence semantics;
* add focused lowering tests that check the generated PTX;
* validate correctness against an equivalent direct-PTX reference implementation;
* run the primitive on SM120 as an additional hardware validation target.

I'll keep the initial PR focused on the primitive/API rather than expanding it into a broader FlashAttention or collective change.

Additionally, as a GPU programmer, I do really appreciate your previous work of FlashAttention.

