# [Issue #2495] [Bug] Deployment detail page uses hardcoded data and cannot open the real Playground

source: https://github.com/vllm-project/aibrix/issues/2495
state: open | updated: 2026-09-08T06:13:57Z
labels: kind/bug, help wanted, priority/important-soon, area/website

## 正文

The deployment detail page fetches a real Deployment record, but much of the page is still sample UI:

- the inference URL and model ID are [hardcoded](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/web/src/components/DeploymentDetail.tsx#L56-L63);
- account names, description, timestamp, and resource names are [static values](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/web/src/components/DeploymentDetail.tsx#L69-L98);
- Copy, View More, and Open in Playground do not perform their advertised actions.

The Playground is also not connected yet. It [lists catalog models](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/web/src/components/Playground.tsx#L475-L498) and [streams a fixed local response](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/web/src/components/Playground.tsx#L546-L597). A real backend proxy already exists at `POST /api/v1/playground/chat/completions` ([handler](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/api/handler/playground.go#L63-L138)).

The detail page should use real Deployment/Model data and show a usable endpoint and serving model name. The current [Deployment API](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/api/proto/console/v1/console.proto#L55-L70) may need a few additional fields, including creation time and inference metadata.

Open in Playground should carry the selected deployment (or serving name) to `/playground`. The Playground should list callable deployments and send the actual request through the existing proxy instead of using the local timer. Please also wire up the displayed copy actions and avoid showing unsupported code examples as functional.

A local test with the mocked app should cover: create deployment → open detail page → open Playground → receive a real chat completion.

Depends on #2494 for Gateway discovery. Related: #2202, #2198.


## 评论 (1)

### SarnadAbhilash · 2026-09-08

I'll take this one.

Plan: use real Deployment/Model fields on the detail page (inference URL, serving model, creation time, copy actions), pass the selected deployment into `/playground`, and send chat completions through the existing `POST /api/v1/playground/chat/completions` proxy instead of the local timer. I'll keep the change scoped to the console and add a local mocked-app path for create → detail → playground.
