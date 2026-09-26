# [Issue #1801] Make MLPerf inference results easier to reproduce and reduce the reproducibility burden of submitters 

source: https://github.com/mlcommons/inference/issues/1801
state: closed | updated: 2026-07-24T00:31:22Z
labels: Stale

## 正文

This proposal is to make MLPerf inference results easier to reproduce as well as to reduce the burden on the submitter to support reproducibility.

Currently MLPerf inference submitters follow custom READMEs/automations making it harder for external users to reproduce them and each submitter has to take care to maintain the reproducibility of their submissions. The below proposal is aimed at solving these problems. 

During the review period ensure that the submission works via CM with expected performance and documentation is in the [Inference docs site](https://docs.mlcommons.org/inference/benchmarks/).
After this is done, CM team can ensure reproducibility and answer queries from the public for the following one year (reproducibility support ends after one year).
CM for MLPerf inference can easily support multiple code versions for reproducibility. We are supporting the latest Inference code release (from Nvidia, Intel, Qualcomm, Neural Magic and MLCommons) and the one just preceding it.
We currently have all the Nvidia and Intel MLPerf inference benchmarks from v4.0 and all v3.1 Qualcomm benchmarks in CM - so supporting v4.1 code during the review period is not difficult.

The timeframe needed to support a submitter code depends on the complexity in the submission code (calibration, compilation, run configuration etc.) For submitters using the supported code bases of Nvidia and Intel, we expect to support the submissions in maximum 1-2 days once they share the code with us. For other submitters it can take up to a week. 

## 评论 (1)

### github-actions[bot] · 2026-07-24

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
