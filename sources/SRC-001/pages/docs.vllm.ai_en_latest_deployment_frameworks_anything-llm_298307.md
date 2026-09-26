source: https://docs.vllm.ai/en/latest/deployment/frameworks/anything-llm/
lastmod: 2026-09-24

# AnythingLLM[¶](https://docs.vllm.ai#anythingllm)

[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) is a full-stack application that enables you to turn any document, resource, or piece of content into context that any LLM can use as references during chatting.

It allows you to deploy a large language model (LLM) server with vLLM as the backend, which exposes OpenAI-compatible endpoints.

## Prerequisites[¶](https://docs.vllm.ai#prerequisites)

Set up the vLLM environment:

## Deploy[¶](https://docs.vllm.ai#deploy)

-
Start the vLLM server with a supported chat-completion model, for example:

-
Download and install

[AnythingLLM Desktop](https://anythingllm.com/desktop). -
Configure the AI provider:

- At the bottom, click the 🔧 wrench icon ->
**Open settings**->**AI Providers**->**LLM**. - Enter the following values:
- LLM Provider: Generic OpenAI
- Base URL:
`http://{vllm server host}:{vllm server port}/v1`

- Chat Model Name:
`Qwen/Qwen1.5-32B-Chat-AWQ`



- At the bottom, click the 🔧 wrench icon ->
-
Create a workspace:

- At the bottom, click the ↺ back icon and back to workspaces.
- Create a workspace (e.g.,
`vllm`

) and start chatting.

-
Add a document.

- Click the 📎 attachment icon.
- Upload a document.
- Select and move the document into your workspace.
- Save and embed it.

-
Chat using your document as context.