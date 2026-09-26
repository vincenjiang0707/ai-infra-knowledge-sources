# [Issue #1969] ModelOpt CI is failing with: Windows fatal exception

source: https://github.com/NVIDIA/Model-Optimizer/issues/1969
state: closed | updated: 2026-08-03T06:26:34Z
labels: bug

## 正文

## Describe the bug

ModelOpt CI is failing with: Windows fatal exception:
https://github.com/NVIDIA/Model-Optimizer/actions/runs/29252092124/job/86824842907?pr=1888

```
tests/unit/torch/nas/test_search_space_with_torchvision.py::test_forward[get_tiny_resnet_and_input] PASSED [ 47%]
tests/unit/torch/nas/test_search_space_with_torchvision.py::test_forward[get_tiny_mobilenet_and_input] PASSED [ 47%]
tests/unit/torch/nas/test_search_space_with_torchvision.py::test_forward[<lambda>] PASSED [ 47%]
tests/unit/torch/opt/plugins/test_diffusers_save_load.py::test_unet_save_restore[UNet2DConditionModel] PASSED [ 47%]
tests/unit/torch/opt/plugins/test_hf_patching.py::test_nested_model_save_restore[AutoModelForCausalLM-llama] Windows fatal exception: code 0xc000001d

Thread 0x00001468 (most recent call first):
  File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\threading.py", line 359 in wait
  File "C:\hostedtoolcache\windows\Python\3.12.10\x64\Lib\threading.py", line 655 in wait
```

## 评论 (5)

### jenchen13 · 2026-07-21

Hi @danielkorzekwa does this issue still persist when you re-run the CI?

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: caf1b78768fef0d6794add4cd8b57dcc2b25a72b8ef3d8f646b7f774f248a594

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: e86009db63342db5e36b6f3f8be8aa9c35b1e2f092fcb3078cf97da7eaf28de8

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 48cc9da0972fd476fcfd731060ad2dbbba3deef4bba120e8c5daf79c3ee922d7

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### kevalmorabia97 · 2026-08-03

fClosing as not seeing this issue anywhere. feel free to reopen if you face this issue again
