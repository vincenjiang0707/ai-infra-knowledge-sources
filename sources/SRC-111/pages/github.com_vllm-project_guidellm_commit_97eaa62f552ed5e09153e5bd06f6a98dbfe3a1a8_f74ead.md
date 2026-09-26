source: https://github.com/vllm-project/guidellm/commit/97eaa62f552ed5e09153e5bd06f6a98dbfe3a1a8

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Add inline and file-backed API key sources for the OpenAI HTTP backend and coordinate round-robin allocation across worker processes.
Generated-by: Cursor GPT-5.6 Terra
Co-authored-by: Cursor <cursoragent@cursor.com>

Flat settings can be specified using comma-separated key=value pairs; for nested settings use serialized JSON or YAML. Common `openai_http` parameters include `target`, `model`, `request_format`, `api_key`, `stream`, `verify`, `timeout`, and nested `extras` for request body, headers, and query parameters:

19

+

Flat settings can be specified using comma-separated key=value pairs; for nested settings use serialized JSON or YAML. Common `openai_http` parameters include `target`, `model`, `request_format`, `api_key`, `api_keys`, `api_key_file`, `stream`, `verify`, `timeout`, and nested `extras` for request body, headers, and query parameters:

@@ -117,6 +117,24 @@ The API key is used to set the `Authorization: Bearer {api_key}` header in HTTP

117

117

> [!IMPORTANT]\

118

118

> For security, avoid hardcoding API keys in scripts. Consider using environment variables or secure credential management tools when passing API keys via `--backend`.

119

119

120

+

### Configuring Multiple API Keys

121

+

122

+

To rotate credentials across generation requests, provide either `api_keys` as a JSON/YAML list or `api_key_file` as a path to a UTF-8 text file with one key per line. Blank lines are ignored. `api_key`, `api_keys`, and `api_key_file` are mutually exclusive.

GuideLLM assigns generation requests globally in round-robin order across worker processes. Health checks and model discovery use the first configured key and do not advance the rotation. An explicit `Authorization` value in `extras.headers` takes precedence and does not consume a rotating key.

135

+

136

+

Keep key files out of source control, restrict their filesystem permissions, and avoid passing secrets through shell history or committed configuration files.

137

+

120

138

## Passing Sampling Parameters

121

139

122

140

By default, GuideLLM does not set sampling parameters such as `temperature`, `top_p`, or `top_k` in its requests to the backend server. If you need to control these parameters during benchmarking, pass them through the backend `extras` field.

## 0 commit comments