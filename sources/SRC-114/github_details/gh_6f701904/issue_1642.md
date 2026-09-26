# [Issue #1642] LlaMa2-70b run_accuracy.sh issue with consolidate_results.py

source: https://github.com/mlcommons/inference/issues/1642
state: closed | updated: 2026-05-07T00:39:54Z
labels: Stale

## 正文

LlaMa2-70b has a run_accuracy.py script that as a last step that calls another script, consolidate_results.py. That last step does not work, it expects to read output pkl files, but those are not being created in previous steps. 

The README marks this step as optional - so we should either remove if not needed, or fix.

@nvzhihanj , please help. 


## 评论 (3)

### nvzhihanj · 2024-02-26

I believe the consolidate_results.py is not needed if the pickle input file already has all the samples (24576). That script is a by-product of preprocessing that @nv-alicheng uses IIRC.

### nv-alicheng · 2024-02-26

consolidate_results.py is an optional step that was used to generate a pickle file for manual viewing / data analysis. It is not required to run the accuracy script. The pkl files that it consumes are generated here (https://github.com/mlcommons/inference/blob/master/language/llama2-70b/dataset.py#L90) during the accuracy inference.

### github-actions[bot] · 2026-05-07

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
