# [Issue #1885] Disclose exact pending reason for failed to schedule lora

source: https://github.com/vllm-project/aibrix/issues/1885
state: open | updated: 2026-08-27T06:42:15Z
labels: good first issue, help wanted, area/lora

## 正文

### 🐛 Describe the bug

<img width="1282" height="648" alt="Image" src="https://github.com/user-attachments/assets/3ab980eb-30e0-4f35-b8e8-c6c5195ba6df" />

if we do not have qualified base models, the error message shows like this.

However, the information is not that clear to end users, we need to improve and tell there's no qualified backend pods etc.

<img width="2050" height="84" alt="Image" src="https://github.com/user-attachments/assets/a9c06446-6c1a-4c36-9ee0-5a20e9c068c6" />

### Steps to Reproduce

```
kubectl apply -f samples/adapter/adapter.yaml
```

### Expected behavior

It should expose more information

### Environment

nightly

## 评论 (4)

### VaishnaviOnPC · 2026-01-11

Hi, I would like to work on this issue. May I be assigned?

### Ramshankar07 · 2026-01-20

Can I help in this> @VaishnaviOnPC ?


### VaishnaviOnPC · 2026-01-20

Hi, @Ramshankar07. Thanks for checking in. I’ve been looking through the code and am halfway through the change to improve the LoRA scheduling error message. I just need to test it locally. I'll open a PR shortly for the issue. I’ll reach out if I need any guidance.

### mikemikimike · 2026-08-27

Implemented in PR #2625.

- Changed: Surface actionable Scheduled=False conditions when a ModelAdapter has no ready backend pods or fewer ready pods than required.
- Tests: `go test ./pkg/controller/modeladapter/...`
- Validation: `gofmt`, `go vet ./pkg/controller/modeladapter/...`, and `git diff --check`.

