source: https://github.com/vllm-project/guidellm/issues/429

**Describe the bug**

The sample prompts section should show prompt snippets used in the benchmark run. A recent update has changed some of the underlying code structure and now the request_args holds much more than the prompt. The prompt is not surfaced in the shown sample.

Visualized (this will go down eventually when the PR is closed): [https://blog.vllm.ai/guidellm/ui/pr/427/](https://blog.vllm.ai/guidellm/ui/pr/427/)

**Expected behavior**

Example of it working (this will go down eventually as well, but for now holds the previous working state) [https://blog.vllm.ai/guidellm/ui/pr/391/](https://blog.vllm.ai/guidellm/ui/pr/391/)

**Additional context**

The change comes from an update to what request_args holds in the benchmark report. Previously the UI data relied on request_args holding the prompt value, but now the prompt text is nested within. Something like: `request_args.method.body.model.messages[0].content[0].text`


See: [https://github.com/vllm-project/guidellm/blob/main/src/guidellm/presentation/data_models.py#L120](https://github.com/vllm-project/guidellm/blob/main/src/guidellm/presentation/data_models.py#L120)

Describe the bugThe sample prompts section should show prompt snippets used in the benchmark run. A recent update has changed some of the underlying code structure and now the request_args holds much more than the prompt. The prompt is not surfaced in the shown sample.

Visualized (this will go down eventually when the PR is closed): https://blog.vllm.ai/guidellm/ui/pr/427/

Expected behaviorExample of it working (this will go down eventually as well, but for now holds the previous working state) https://blog.vllm.ai/guidellm/ui/pr/391/

Additional contextThe change comes from an update to what request_args holds in the benchmark report. Previously the UI data relied on request_args holding the prompt value, but now the prompt text is nested within. Something like:

`request_args.method.body.model.messages[0].content[0].text`

See: https://github.com/vllm-project/guidellm/blob/main/src/guidellm/presentation/data_models.py#L120