source: https://github.com/vllm-project/guidellm/issues/1152

### Bug Description

If a server acts improperly and does not close connections at the end of cancelled requests it can result in a stall at the end of each benchmark as GuideLLM waits for final status.

### Expected Behavior

GuideLLM should forcefully close request a certain amount of time after it cancels them.

### Steps to Reproduce

TODO

### Operating System

Any

### Python Version

Any

### GuideLLM Version

main

### Installation Method

Official Container Image (Docker)

### Installation Details

*No response*

### Error Messages or Stack Traces

### Additional Context

*No response*

## Bug Description

If a server acts improperly and does not close connections at the end of cancelled requests it can result in a stall at the end of each benchmark as GuideLLM waits for final status.

## Expected Behavior

GuideLLM should forcefully close request a certain amount of time after it cancels them.

## Steps to Reproduce

TODO

## Operating System

Any

## Python Version

Any

## GuideLLM Version

main

## Installation Method

Official Container Image (Docker)

## Installation Details

No response## Error Messages or Stack Traces

## Additional Context

No response