# [Issue #2479] Typos detected by nightly scan (5 found)

source: https://github.com/llm-d/llm-d/issues/2479
state: closed | updated: 2026-09-24T19:50:03Z
labels: 

## 正文

## Typos Detected

The nightly typo checker found **5** typos.

```
./guides/recipes/observability/grafana/dashboards/llm-d-batch-gateway-processor.json:527: `aimd` -> `aimed`
./guides/recipes/observability/grafana/dashboards/llm-d-batch-gateway-processor.json:531: `AIMD` -> `AIMED`
./guides/recipes/observability/grafana/dashboards/llm-d-batch-gateway-processor.json:556: `aimd` -> `aimed`
./guides/recipes/observability/grafana/dashboards/llm-d-batch-gateway-processor.json:564: `aimd` -> `aimed`
./guides/recipes/observability/grafana/dashboards/llm-d-batch-gateway-processor.json:568: `AIMD` -> `AIMED`
```

### Fix
```bash
cargo install typos-cli  # or: brew install typos-cli
typos --write-changes .
```

Add false positives to `_typos.toml`.

---
*Nightly scan from [llm-d-infra](https://github.com/llm-d/llm-d-infra/actions/runs/34671906571)*

## 评论 (12)

### Kaustubh1235 · 2026-09-12

I will take this issue. Please assign it to me.

The issue reports five typos in a JSON file related to Grafana dashboards. I will first verify these typos in the specified file paths. Then, I will correct them by replacing "aimd" with "aimed" and "AIMD" with "AIMED" at the mentioned lines. After making these changes, I will run the typo checker to ensure no other issues remain.


### clubanderson · 2026-09-16

## New typos found (2026-09-16)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35054004276)

### clubanderson · 2026-09-17

## New typos found (2026-09-17)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35180349629)

### clubanderson · 2026-09-18

## New typos found (2026-09-18)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35305390816)

### VanshikaNavya · 2026-09-18

@clubanderson can I take this up?

### clubanderson · 2026-09-19

## New typos found (2026-09-19)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35420182403)

### clubanderson · 2026-09-20

## New typos found (2026-09-20)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35488079926)

### clubanderson · 2026-09-21

## New typos found (2026-09-21)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35559492404)

### clubanderson · 2026-09-22

## New typos found (2026-09-22)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35685298960)

### varad-ahirwadkar · 2026-09-22

/assign

### clubanderson · 2026-09-23

## New typos found (2026-09-23)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35816641793)

### clubanderson · 2026-09-24

## New typos found (2026-09-24)

```
./guides/workload-autoscaling/kueue-rebalancing/README.md:283: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/README.md:293: `optin` -> `option`
./guides/workload-autoscaling/kueue-rebalancing/guide.yaml:109: `optin` -> `option`
```

Detected by [nightly scan](https://github.com/llm-d/llm-d-infra/actions/runs/35953883610)
