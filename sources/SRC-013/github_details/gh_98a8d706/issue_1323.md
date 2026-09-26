# [Issue #1323] Figure out how to let kustomize handle strategic match for CRD (LWS)

source: https://github.com/llm-d/llm-d/issues/1323
state: closed | updated: 2026-09-24T01:19:55Z
labels: lifecycle/rotten

## 正文

While working on https://github.com/llm-d/llm-d/pull/1288, using strategic match results in atomic overrides of array fields, instead of a merge.

From gemini: 

For standard Kubernetes resources (like Deployment or Pod), Kustomize has built-in OpenAPI schemas. It knows that the containers list should be merged by matching the name field, and it knows to recursively combine objects like startupProbe.


The solution seems to be that we need to give the OpenAPI schema to kustomize.

## 评论 (4)

### sudoalok · 2026-05-01

 Hey @liu-cong , looks like this is happening because LeaderWorkerSet is a CRD and Kustomize doesn’t know how to merge its list fields.
We might be able to fix it by adding an OpenAPI schema with merge keys (like name) so strategic merge works properly.
Does that sound like the right direction? Happy to try it out.

### liu-cong · 2026-05-01

@alok7058 Hey thanks for looking! Please give it a try.

### sudoalok · 2026-05-01

Hey @liu-cong @robertgshaw2-redhat , I tried this out with a custom OpenAPI schema adding merge keys (name) for the containers field.

But even after that, Kustomize is still replacing the entire containers array instead of merging. When I apply a strategic merge patch, fields like image, env, etc. get dropped and only the patched part remains.

So it looks like just adding the OpenAPI schema isn’t enough for LWS — especially for nested fields like spec.leaderWorkerTemplate.workerTemplate.spec.containers.

I also tried the same change using JSON6902 patch, and that works fine since it directly updates the field without touching the rest.

So I think this might be a limitation of how Kustomize handles CRDs with nested arrays, even when a schema is provided.

Happy to try other approaches if you have something in mind 

### github-actions[bot] · 2026-08-24

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
