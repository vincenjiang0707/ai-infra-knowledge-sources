# [Issue #1595] [automation and reproducibility taskforce] progress report for 20240130

source: https://github.com/mlcommons/inference/issues/1595
state: closed | updated: 2026-05-08T00:40:46Z
labels: Stale

## 正文

Many thanks to MLPerf submitters and MLCommons members for their feedback during the past 2 weeks 
to help us improve the [MLCommons CM automation for MLPerf inference](https://github.com/mlcommons/ck):

## Improvements and extensions to general [CM automation recipes](https://github.com/mlcommons/ck/blob/master/docs/list_of_scripts.md) 
that all submitters can reuse to automate their benchmarking:

#### Download models

- [x] `cmr "get ml-model gptj"`
- [x] `cmr "get ml-model stable-diffusion"`
- [x] `cmr --tags=get,ml-model,llama2-70b`

#### Download datasets

- [x] `cmr "get dataset cnndm _validation"`
- [x] `cmr "get dataset coco2014 _validation"`
- [x] `cmr "get preprocessed dataset openorca _validation"`


#### Detect/install frameworks

- [x] `cmr "get generic-python-lib _package.onnxruntime" --version_min=1.16.0`
- [x] `cmr "get generic-python-lib _package.torch" --version=2.1.1`<br>
- [x] `cmr "get generic-python-lib _package.torchvision" --version=0.16.2`

## Continue [repeatibility study for v3.1](https://github.com/mlcommons/ck/issues/1052)

- [x] GPT-J from Intel - thanks to feedback we are nearly done and have CM automation
- [x] GPT-J from Nvidia - re-testing it because of some reports about potential issues
- [ ] Google submission is under testing

Feel free to report issues or suggest submissions [here](https://github.com/mlcommons/ck/issues/1052) or via our [Discord server](https://discord.gg/JjWNWXKxwT).

## Suggestions that we may include to the new CM v1.6.1 release before the next meeting:

- [x] Substitute current complex docs with a CM GUI to select implementation, target, model and then generate CM commands or show the current state with automation and reproducibility 
  - we started prototyping this GUI and will hopefully show it next time.
- [ ] Develop high-level CM script to run different MLPerf implementations with all models for a given target in sequence similar to SPEC benchmarks ([in progress](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/benchmark-any-mlperf-inference-implementation)).
- [ ] Update inference v4.0 READMEs with CM commands to download/detect/install models, datasets and frameworks

## Longer term:

- [x] [Suggestion for MLPerf repetability/reproducibility badges from ACM/IEEE/NeurIPS](https://github.com/mlcommons/ck/issues/1080)
- [ ] Sugestion to restart Automation and Reproducibility TF - contact us if you would like to participate, chair, develop ...

CM is a collaborative engineering effort based on your feedback - please don't hesitate to get in touch via our [Discord server](https://discord.gg/JjWNWXKxwT) or open a ticket [here](https://github.com/mlcommons/ck/issues). Thank you!


## 评论 (1)

### github-actions[bot] · 2026-05-08

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
