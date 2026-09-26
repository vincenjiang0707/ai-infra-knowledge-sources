source: https://github.com/vllm-project/guidellm/issues/1104

## Problem Statement

The OpenAI HTTP backend accepts only one `api_key`

, so all benchmark requests use the same credential. This makes it difficult to distribute requests across multiple API keys when benchmarking a rate-limited service.

## Proposed Solution

Add support for multiple API keys in the OpenAI HTTP backend:

`api_keys`

: supply keys inline through `--backend`

or JSON/YAML configuration.
`api_key_file`

: supply a path to a text file containing one key per line; ignore blank lines.
- Preserve the existing
`api_key`

option for backward compatibility.
- Select one key per generation request and send it as
`Authorization: Bearer <key>`

.
- Rotate keys globally in round-robin order across all worker processes,

## Usage Examples

# Inline configuration
guidellm run --backend '{"kind":"openai_http","target":"https://api.example.com","api_keys":["key-1","key-2"]}'\n\n# One API key per line in ./api-keys.txt\nguidellm run --backend kind=openai_http,target=https://api.example.com,api_key_file=./api-keys.txt\n```\n\n## Additional Context\n\nA backend-local counter is insufficient because GuideLLM uses spawned worker processes; each worker would otherwise have an independent rotation sequence.

## Problem Statement

The OpenAI HTTP backend accepts only one

`api_key`

, so all benchmark requests use the same credential. This makes it difficult to distribute requests across multiple API keys when benchmarking a rate-limited service.## Proposed Solution

Add support for multiple API keys in the OpenAI HTTP backend:

`api_keys`

: supply keys inline through`--backend`

or JSON/YAML configuration.`api_key_file`

: supply a path to a text file containing one key per line; ignore blank lines.`api_key`

option for backward compatibility.`Authorization: Bearer <key>`

.## Usage Examples