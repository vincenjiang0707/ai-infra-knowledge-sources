# [Issue #160] genai-perf compare crashes with [ERROR] genai_perf.main:218 - 'Namespace' object has no attribute 'input_file'

source: https://github.com/triton-inference-server/perf_analyzer/issues/160
state: closed | updated: 2024-12-18T00:13:53Z
labels: 

## 正文

Reproducible on the version `24.10` when run against a NIM server serving `meta/llama-3.1-8b-instruct`.

# Steps to reproduce:
## Perform two profiling runs:
```
genai-perf profile \
	-m meta/llama-3.1-8b-instruct \
	--artifact-dir /root/experiments/256 \
	--endpoint-type chat \
	--service-kind openai \
	--streaming \
	-u localhost:8000 \
	--synthetic-input-tokens-mean 256 \
	--synthetic-input-tokens-stddev 0 \
	--output-tokens-mean 256 \
	--extra-inputs max_tokens:256 \
	--extra-inputs min_tokens:256 \
	--tokenizer hf-internal-testing/llama-tokenizer \
	--measurement-interval 10000 \
	--concurrency 1

genai-perf profile \
	-m meta/llama-3.1-8b-instruct \
	--artifact-dir /root/experiments/512 \
	--endpoint-type chat \
	--service-kind openai \
	--streaming \
	-u localhost:8000 \
	--synthetic-input-tokens-mean 512 \
	--synthetic-input-tokens-stddev 0 \
	--output-tokens-mean 512 \
	--extra-inputs max_tokens:512 \
	--extra-inputs min_tokens:512 \
	--tokenizer hf-internal-testing/llama-tokenizer \
	--measurement-interval 10000 \
	--concurrency 1
```
## Try to compare the results
```
genai-perf compare -f experiments/256/profile_export.json experiments/512/profile_export.json
```
# Expectation
The results are compared and plots are generated.

# Reality
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 214, in main
    run()
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 193, in run
    config_options = create_config_options(args)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 65, in create_config_options
    if args.input_file:
AttributeError: 'Namespace' object has no attribute 'input_file'
2024-10-30 11:45 [ERROR] genai_perf.main:218 - 'Namespace' object has no attribute 'input_file'
```
# Local fix that allowed me to run
```
diff --git a/genai-perf/genai_perf/main.py b/genai-perf/genai_perf/main.py
index 916df00..dfb77aa 100755
--- a/genai-perf/genai_perf/main.py
+++ b/genai-perf/genai_perf/main.py
@@ -186,7 +186,6 @@ def run():
     # TMA-1900: refactor CLI handler
     logging.init_logging()
     args, extra_args = parser.parse_args()
-    config_options = create_config_options(args)
     if args.subcommand == "compare":
         args.func(args)
     else:
@@ -196,6 +195,7 @@ def run():
             args.tokenizer_trust_remote_code,
             args.tokenizer_revision,
         )
+        config_options = create_config_options(args)
         generate_inputs(config_options)
         telemetry_data_collector = create_telemetry_data_collector(args)
         args.func(args, extra_args, telemetry_data_collector)
```
# Two more experiments after the fix applied
```
genai-perf profile \
	-m meta/llama-3.1-8b-instruct \
	--artifact-dir /root/experiments_fix/256 \
	--endpoint-type chat \
	--service-kind openai \
	--streaming \
	-u localhost:8000 \
	--synthetic-input-tokens-mean 256 \
	--synthetic-input-tokens-stddev 0 \
	--output-tokens-mean 256 \
	--extra-inputs max_tokens:256 \
	--extra-inputs min_tokens:256 \
	--tokenizer hf-internal-testing/llama-tokenizer \
	--measurement-interval 10000 \
	--concurrency 1

genai-perf profile \
	-m meta/llama-3.1-8b-instruct \
	--artifact-dir /root/experiments_fix/512 \
	--endpoint-type chat \
	--service-kind openai \
	--streaming \
	-u localhost:8000 \
	--synthetic-input-tokens-mean 512 \
	--synthetic-input-tokens-stddev 0 \
	--output-tokens-mean 512 \
	--extra-inputs max_tokens:512 \
	--extra-inputs min_tokens:512 \
	--tokenizer hf-internal-testing/llama-tokenizer \
	--measurement-interval 10000 \
	--concurrency 1
```
# Comparing the results
```
genai-perf compare -f experiments_fix/256/profile_export.json experiments_fix/512/profile_export.json
```
# The output
```
2024-10-30 11:50 [INFO] genai_perf.plots.plot_config_parser:208 - Creating initial YAML configuration file to compare/config.yaml
2024-10-30 11:50 [INFO] genai_perf.plots.plot_config_parser:53 - Generating plot configurations by parsing compare/config.yaml. This may take a few seconds.
2024-10-30 11:50 [INFO] genai_perf.plots.plot_manager:53 - Generating 'Time to First Token' plot
2024-10-30 11:50 [INFO] genai_perf.plots.plot_manager:53 - Generating 'Request Latency' plot
2024-10-30 11:50 [INFO] genai_perf.plots.plot_manager:53 - Generating 'Distribution of Input Sequence Lengths to Output Sequence Lengths' plot
2024-10-30 11:50 [INFO] genai_perf.plots.plot_manager:53 - Generating 'Time to First Token vs Input Sequence Lengths' plot
2024-10-30 11:50 [INFO] genai_perf.plots.plot_manager:53 - Generating 'Token-to-Token Latency vs Output Token Position' plot
```

## 评论 (4)

### the-david-oy · 2024-11-04

Thank you for submitting this fix and providing such a detailed ticket! Would you like to open a pull request with this fix? We'd need a [Contributor License Agreement submitted](https://github.com/triton-inference-server/server/blob/main/CONTRIBUTING.md) to review and merge it.

If not, we can also create a PR on our end.

### mosalov · 2024-11-12

Thanks! We are working on signing the CLA.

### the-david-oy · 2024-11-22

Hi Oleg! Any update on the CLA?

### the-david-oy · 2024-12-18

This should now be working after the code was refactored for the addition of the analyze subcommand. If you have any issues, let me know.
