# [Issue #1284] [Docs] Discussion: Where to put provider specific docs in the guides

source: https://github.com/llm-d/llm-d/issues/1284
state: closed | updated: 2026-09-25T01:19:41Z
labels: lifecycle/rotten

## 正文

## Description:

### Context 
Currently, the "Google TPU optimized baseline Deployment Guide" ([README.tpu.md](https://github.com/llm-d/llm-d/blob/main/guides/optimized-baseline/README.tpu.md)) lists the following as the first two installation steps:

Step 1: Prepare the GCS Bucket and Model (Run:ai Model Streamer) ([link](https://github.com/llm-d/llm-d/blob/main/guides/optimized-baseline/README.tpu.md?content_ref=step+1+prepare+the+gcs+bucket+and+model+run+ai+model+streamer))
Step 2: Configure Workload Identity for GCS Access ([link](https://github.com/llm-d/llm-d/blob/main/guides/optimized-baseline/README.tpu.md?content_ref=step+2+configure+workload+identity+for+gcs+access))

### The Dilemma 
We have two conflicting user experiences that we need to balance:

1. Simplicity and Quick Start (The "Getting Started" path): Steps 1 and 2 are infrastructure optimizations and are not strictly required to get a TPU stack up and running. Having them at the very beginning of the TPU guide makes the setup confusing and adds friction for users who just want to test things out. Ideally, a user should be able to directly follow the main Optimized Baseline guide ([ README.md](https://github.com/llm-d/llm-d/blob/main/guides/optimized-baseline/README.tpu.md?content_ref=for+broader+context+on+optimized+baseline+gateway+options+and+architecture+refer+to+the+main+optimized+baseline+guide)) and successfully run a TPU stack out of the box (e.g., pulling weights directly from Hugging Face).

2. Practicality and Production Readiness (The "Day 2" path): On the other hand, anyone actually running llm-d for real workloads (not just giving it a try) should absolutely be caching the model weights in GCS. Downloading massive FP8 models from Hugging Face every time  is slow and inefficient. In practice, setting up the Run:ai Model Streamer to load weights from GCS is highly recommended.

### Open for Discussion: 
Where should this live? How can we best restructure the documentation so that new users aren't blocked by infrastructure setup, but production users still easily find this critical optimization?

Some potential options:
* Move to a generalized "Production Best Practices" guide. 

Thoughts and feedback on the best approach are highly appreciated!

## 评论 (4)

### yangligt2 · 2026-04-29

cc: @liu-cong 

### amacaskill · 2026-05-08

 @liu-cong @ahg-g Hi all, I see that @yangligt2 removed the RunAI model streamer support that I added in   https://github.com/llm-d/llm-d/pull/1102 in the PR https://github.com/llm-d/llm-d/pull/1286. This runai model streamer guide was requested by a specific customer, so I would have appreciated the heads up before it was deleted. 

Where should I add it now?  

### liu-cong · 2026-05-09

Can we point them to the GCP docs for model streamer? @amacaskill 

We are still trying to figure out the best way to combine GCP specific docs with llm-d docs. While we would like to recommend GKE specific best practices, we also need to balance the doc complexity as not every user needs them. I have raised this to GKE PMs and we should come up with some guidelines.

### github-actions[bot] · 2026-08-25

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
