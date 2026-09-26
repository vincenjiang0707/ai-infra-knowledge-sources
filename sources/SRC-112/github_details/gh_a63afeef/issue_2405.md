# [Issue #2405] In the CSV file for the statistical table download, the display of the ms statistical unit is incorrect; it should all be s (seconds).

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2405
state: closed | updated: 2026-07-31T11:56:35Z
labels: 

## 正文

Mean TTFT (ms)	Median TTFT (ms)	P99 TTFT (ms)	Std TTFT (ms)	Mean TPOT (ms)	Median TPOT (ms)	P99 TPOT (ms)	Std TPOT (ms)
1.615576321	0.403875659	20.67356789	3.964372301	0.048823025	0.0490139	0.061919564	0.005588959
0.950818943	0.265745289	10.50568854	2.045110656	0.032089098	0.031803253	0.042772826	0.003919158

Mean ITL (ms)	Median ITL (ms)	P99 ITL (ms)	Std ITL (ms)	Mean E2E Latency (ms)	Median E2E Latency (ms)	P99 E2E Latency (ms)	Std E2E Latency (ms)
0.048892513	0.02832133	0.190448091	0.091604103	46.55299096	45.77583359	75.47229264	8.356892074
0.03215258	0.021080775	0.183946153	0.08365551	30.55565827	30.07800188	49.12748711	5.16729021

For example, the TPOT value above is clearly incorrect.

## 评论 (1)

### Oseltamivir · 2026-07-31

Thanks, fixed
