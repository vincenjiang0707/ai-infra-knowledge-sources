# [Issue #174] A custom tokenizer for the compare command

source: https://github.com/triton-inference-server/perf_analyzer/issues/174
state: closed | updated: 2025-01-03T21:33:13Z
labels: 

## 正文

It looks to me that whereas the `profile` command supports usage of the `--tokenizer` argument, the `compare` command does not have such an option. That leads to a case when you can have a series of experiments run with a tokenizer of your choice and then when trying to compare the results you would get distorted ranges for input and output sequence lengths.

I have experienced that while running on Llama3_2-3B with the included in the model tokenizer.
All my experiments were run with input and output lengths being equal to 256, and when I have tried building plots with the `--generate-plots` argument all ranges were as expected. But when I have tried to `compare` my experiments, inputs became of the size 285 and outputs - of the size 347, all due to the default tokenizer being used.

I have circumnavigated the issue on my side with the following patch:
```
diff --git a/genai-perf/genai_perf/parser.py b/genai-perf/genai_perf/parser.py
index f8be694..72a3502 100644
--- a/genai-perf/genai_perf/parser.py
+++ b/genai-perf/genai_perf/parser.py
@@ -844,6 +844,7 @@ def _parse_compare_args(subparsers) -> argparse.ArgumentParser:
         "this option instead of the `--config` option if they would like "
         "GenAI-Perf to generate default plots as well as initial YAML config file.",
     )
+    _add_other_args(compare)
     compare.set_defaults(func=compare_handler)
     return compare

@@ -880,7 +881,7 @@ def compare_handler(args: argparse.Namespace):
         args.config = output_dir / "config.yaml"

     config_parser = PlotConfigParser(args.config)
-    plot_configs = config_parser.generate_configs()
+    plot_configs = config_parser.generate_configs(args.tokenizer)
     plot_manager = PlotManager(plot_configs)
     plot_manager.generate_plots()
```
which allowed me to pass the tokenizer to the `compare` command and to receive properly formatted plots.

I am not 100% sure that this approach is a way to go, so I would like to get a confirmation.
Also I believe it is worth reviewing other cases of tokenizer usage in the codebase.

## 评论 (4)

### the-david-oy · 2024-11-14

Thank you for identifying and sharing this, Oleg! This looks reasonable, albeit we might want to make sure only the tokenizer arg gets passed to compare, not any other "other_args". You're welcome to create a PR for this case as well or we can make these updates.

CC: @nv-hwoo 

### mosalov · 2024-11-14

Thanks David!
`Other_args` include 3 parameters related to a tokenizer and one for verbosity.
What would be the right way for a pull-request?
1. Add only one `tokenizer` parameter.
2. Add all three tokenizer-related parameters.
3. Keep `other_args`.

### the-david-oy · 2024-11-14

Thanks for checking and proposing solutions! We originally had one tokenizer arg and it looks like it expanded to three over time. 

My suggestion would be 2, so that there are no issues with custom tokenizers. I would recommend creating a separate category and function for the tokenizer args, so you can add those args both to profile and compare. The verbosity can be left in the other_args category and function.

### the-david-oy · 2025-01-03

Merged a PR to resolve this issue. Thanks for bringing it to our attention!
