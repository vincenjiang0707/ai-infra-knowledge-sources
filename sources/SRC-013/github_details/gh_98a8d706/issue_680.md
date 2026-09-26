# [Issue #680] Add benchmarking templates and update benchmark results for tiered prefix cache guides

source: https://github.com/llm-d/llm-d/issues/680
state: open | updated: 2026-09-20T01:22:56Z
labels: lifecycle/stale

## 正文

- [x] Update the scorer weights (need to match the optimized baseline is 2:2:3) 
- [x] Add CPU offloading nightly CI
- [x] Add benchmark template for CPU offloading
- [x] update benchmark results for CPU: offloading connector
- [ ] update benchmark results for CPU: lmcache connector
- [ ] Add storage offloading nightly CI job
- [ ] Add benchmark template for storage offloading
- [ ] update benchmark results for storage: fs connector
- [ ] update benchmark results for storage: lmcache connector

## 评论 (5)

### liu-cong · 2026-05-06

@dannawang0221 @kfirtoledo Can you help figure this out? I think we should define the same benchmark templates, and perhaps run on various configurations

### dannawang0221 · 2026-05-06

> [@dannawang0221](https://github.com/dannawang0221) [@kfirtoledo](https://github.com/kfirtoledo) Can you help figure this out? I think we should define the same benchmark templates, and perhaps run on various configurations

Thanks Cong! @Sneha-at is going to help out with this.

### kfirtoledo · 2026-06-11

@amirfr3 will work on the CI/CD for storage. 
and @effi-ofer will update the benchmark results for offloading-connector 


### liu-cong · 2026-06-11

@dannawang0221 @Sneha-at can we also add the CI/CD for storage offloading on GKE?

### github-actions[bot] · 2026-09-20

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
