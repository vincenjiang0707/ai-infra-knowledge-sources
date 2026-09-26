# [Issue #1350] TEST04 update for Inference v3.1

source: https://github.com/mlcommons/inference/issues/1350
state: closed | updated: 2026-05-14T00:45:53Z
labels: Stale

## 正文

Currently TEST04 consists of running performance mode with only one sample as follows:
- Offline scenario, the same sample is repeated as many times as necessary to fill the query
- Single-Stream/MultiStream/Server scenario test works by sending the same query as many times as necessary to satisfy a minimum duration of 10 minutes.

This creates the issue that the test doesn’t apply for benchmarks with a datasets with very unbalanced sample input sizes or very unbalanced processes times. Currently the test only applies for `ResNet50`.

**Requirements:**
- Be more applicable for benchmarks beyond `ResNet50`. This translates into tackling the input size / processing time variation issue.

**Initial Proposal**
- Select one batch (size ~8 or 16) of samples and run performance mode alternating between the samples in the batch.

**Other considerations**
- Is there a specific way of choosing the samples (E.g: choosing random samples, choosing samples close to the average time)
- Experiment with the test to ensure the it passes reliably.
- It is likely that for some models (particularly 3d-Unet) this issue has no solution, due to the fact that the input length varies a lot and there are few samples in the dataset.

This is **not** the final proposal to fix this test. Please feel free to discuss here other possible ways to solve this issue

## 评论 (3)

### arjunsuresh · 2023-04-04

I think we can do something like this. I'm considering retinanet as an example here. Here, `performance_sample_count=64` and so take 64 unique inputs.

Repeat inp1 N times, followed by inp2 N times and so on. Let the time taken be t1. (Maximum cache hits)

Then run inp1 followed by inp2 ... inp64 and repeat this N times. Let the time taken be t2. (Minimum cache hits)

Compare t1 and t2 for compliance. 

Minimum value of N should be 2 to ensure t1 is benefitting from caching. In the worst case, the runtime will be 4 times the accuracy run time as there are two runs and each run is doing twice the performance_sample_count number of inputs. Submitters should be free to increase the value of N on faster devices as a short runtime can cause larger variation and test failure. 

This modification can make TEST04 applicable to all the benchmarks. 

### pgmpablo157321 · 2023-04-18

Ideally this test can be applicable to: `rnnt`, `bert`, `dlrm`, `retinanet`

### github-actions[bot] · 2026-05-14

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
