# [Issue #2632] [BUG] GPTQModel.push_to_hub fails due to token not being passed correctly

source: https://github.com/ModelCloud/GPTQModel/issues/2632
state: closed | updated: 2026-04-02T00:39:57Z
labels: bug

## 正文

This doesn't work it keep throwing error.  GPTQModel.push_to_hub fails. due to token not being passed. Looks like no one tested it or was using env variables.

HfHubHTTPError: Client error '401 Unauthorized' for url 'https://huggingface.co/api/repos/create' (Request ID: Root=1-69cb3964-6d83573c136795bd0d12086a;19ffaf14-2475-4f1e-b862-8f204f6e89bc)
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
Invalid username or password

Past issue:
https://github.com/ModelCloud/GPTQModel/issues/1211

**Solution**

There is bug when otherwise upload_large_folder fails.
https://github.com/ModelCloud/GPTQModel/blob/8fb2e3154cf1d9b18969c231a990eeb8763d2648/gptqmodel/models/auto.py#L579

api = HfApi()
should be
api = HfApi(token=token)

## 评论 (4)

### Qubitium · 2026-03-31

@djaffer This feature was tested long ago but not with token passed via `arg`.  Also HfApi has undergone a lot of changes since this feature was introduced. Due to the expansion of complexity within GPT-QModel, I have decided to fullly remove and deprecated this feature. User should call HFAPi standlone outside of GPTQ-QMOel and point to the checkpoint path. I believe this is the best way forward to reduce complexity in the codebase.

### djaffer · 2026-04-01

Maybe we need updated documentation.

### Qubitium · 2026-04-01

> Maybe we need updated documentation.

Do you still references to gptqmodel.upload_to_hub() api usage in docs/code?

### djaffer · 2026-04-02

Looks you recently removed all references on from code base https://github.com/ModelCloud/GPTQModel/commit/cf0c3e57c46e11087b4c7f741686aaddcfc8f39d. That's good.
