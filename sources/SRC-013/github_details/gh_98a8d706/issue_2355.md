# [Issue #2355] docs(api): `requestHandler.parser` (object) in the reference vs `requestHandler.parsers` (list) in the gRPC guide

source: https://github.com/llm-d/llm-d/issues/2355
state: closed | updated: 2026-09-11T16:50:03Z
labels: 

## 正文

**Area:** docs / API reference (EndpointPickerConfig)
**Path:** Docs
**Severity:** medium — the two pages describe incompatible YAML shapes for the same field, and a reader has no way to tell which one the EPP accepts. One of them makes the config fail to load.
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`)

## Description

`requestHandler` is documented with two different shapes in the same API reference:

- `docs/api-reference/endpointpickerconfig.md:77`, under `## RequestHandlerConfig`:

  | Field | Description |
  | --- | --- |
  | `parser` | [ParserConfig](#parserconfig) <br/> Specifies the parsing logic for protocol messages. |

  Singular, a single object, with `ParserConfig.pluginRef` **Required**.

- `docs/api-reference/epp-grpc-apis.md:29-32`, in a complete working example:

  ```yaml
  requestHandler:
    parsers:
    - pluginRef: vllmgrpcParser
  ```

  Plural, a list.

A user configuring a gRPC model server follows the second page; a user reading the reference table writes the first. Only one can be right.

## Repro

1. `git checkout v0.9.0`
2. `grep -n 'parser' docs/api-reference/endpointpickerconfig.md` → `parser` (object) at line 77.
3. `grep -n 'parsers:' docs/api-reference/epp-grpc-apis.md` → `parsers:` (list) at line 31.

## Expected

One shape, documented consistently. If both are accepted (for example a deprecated singular form and a current plural one), the reference says so and states the precedence.

## Actual

Two shapes, each presented as correct, with no cross-reference between them.

## Probable root cause

The field appears to have moved from a single parser to a list, and the reference table was not updated — the same pattern as the `saturationDetector` move tracked in llm-d-router#1308.

## Suggested fix

Confirm the current shape against `apix/config/v1alpha1` in `llm-d-router` at the pinned EPP version (`v0.10.0`), then update `docs/api-reference/endpointpickerconfig.md` — including the `ParserConfig` section and its `Required` marker — to match, keeping a deprecation note if the singular form is still accepted.

## Related

Same class of drift as the `saturationDetector` documentation issue filed alongside this one.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree; the two API-reference pages were read against each other. No secrets in this report.


## 评论 (2)

### paulohenriquevn · 2026-08-22

Checked the schema at the pinned EPP version, and it resolves which side is correct: the **list** form is the current one.

```go
// llm-d-router v0.10.0 — apix/config/v1alpha1/endpointpickerconfig_types.go:320-325
// RequestHandlerConfig contains the configuration for incoming request handling.
type RequestHandlerConfig struct {
	// +optional
	// Parsers specifies the parsing plugins used by the EPP to process protocol messages.
	// If unspecified, default parsing behavior will be applied.
	Parsers []ParserConfig `json:"parsers,omitempty"`
```

So `docs/api-reference/endpointpickerconfig.md` is the page to fix: under `## RequestHandlerConfig`, `parser` should become `parsers`, typed as a list of `ParserConfig`. The `epp-grpc-apis.md` example is already right.

One extra wrinkle worth folding into the same fix: the deprecation comment on the old top-level field points at a field name that does not exist either.

```go
// same file, lines 73-78
// Deprecated: use requestHandler.parser instead. If both are set, the new field is used.
Parser *ParserConfig `json:"parser,omitempty"`
```

It says `requestHandler.parser`, singular, while the replacement is `requestHandler.parsers`. Anyone following that deprecation notice lands on the same wrong shape the docs describe, which is probably how the drift propagated. That one is in `llm-d-router`, not here.


### rishabhsinha17 · 2026-08-26

/assign
