# [Issue #1665] Note on submission creator scripts: Non-conformant directory structure? #54

source: https://github.com/mlcommons/inference/issues/1665
state: closed | updated: 2026-05-06T00:40:53Z
labels: Stale

## 正文

# Cross Posting From Review Committee on behalf of the original authors.

According to [MLCommons policies, submission rules](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#inference-1) the structure of a submission should conform to:

measurements/
<system_desc_id>/
<benchmark>/
<scenario>
<system_desc_id>_<implementation_id>_<scenario>.json
README.md
user.conf
mlperf.conf
calibration_process.adoc
code
<benchmark>
<implementation_id>
<code file|dir>
<code file|dir>
...
It appears as if the common usage is

to not have a _<implementation_id>_ part in the name of the json file in the measurement section and that the submission UI is not looking for this to be present.
To include a reference to the that "sort of indicates" the <implementation_id> in the code/ section of the submission in the \system_desc_id>, but not necessarily verbatim replicates the implementaion ID
To allow for a submitter to easily submit runs on more than one implementation of the same benchmark I would suggest that a stronger adherence to the rules are encouraged and that the directory structure is slightly updated to fully support what I believe was originally intended and make the structure more similar between the two sections. I suggest that

!) An implementation ID level is added to the results section
2) This is also added to the measurements section
3) The <system_desc_id>_<implementation_id>_<scenario>.json is removed from the required files. For benchmarks where is is of value a config.json file is added to the requirements that contain any relevant parameters that are needed.

results/
<system_desc_id>/
<benchmark>/
<implementation_id>
<scenario>
performance/
measurements/
<system_desc_id>/
<benchmark>/
<implementation_id>
<scenario>
Remove: <system_desc_id>_<implementation_id>_<scenario>.json
README.md
user.conf
mlperf.conf
calibration_process.adoc
I believe that the original json file was introduced to create a link between the system, the code and the implementation used for a benchmark. With the suggested directory structure this is not needed any longer.

It appears that some data is sometimes provided in a json file with an arbitrary(?) name is used to convey some parameter settings to the UI, but I have not seen where the required(?) content of this file is described.


-------------------

This is a very good suggestion. Currently we manage this by encoding implementation id in the system_desc_id. We can discuss more on this during the post-mortem time.

But the <system_desc_id>_<implementation_id>_<scenario>.json is currently giving information like 'quantization' and model parameters which are not available elsewhere in a structured format. [This](https://github.com/mlcommons/submissions_inference_v4.0/blob/main/closed/CTuning/measurements/PCSPECIALIST_AMD_AM5_with_Nvidia_RTX_4090-cpp-gpu-onnxruntime-vdefault-default_config/resnet50/offline/PCSPECIALIST_AMD_AM5_with_Nvidia_RTX_4090-cpp-gpu-onnxruntime-vdefault-default_config.json) is an example.

Here, system_desc includes the implementation tag - 'cpp', the device tag gpu, the framework tag onnxruntime, framework version tag vdefault and also the config tag default_config (configs are needed if someone wants to submit results with say different batchsizes).

## 评论 (2)

### bitfort · 2024-03-17

The above is a cross post of an issue we didn't resolve during the review committee for 4.0 inference - original authors please follow up here. 

### github-actions[bot] · 2026-05-06

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
