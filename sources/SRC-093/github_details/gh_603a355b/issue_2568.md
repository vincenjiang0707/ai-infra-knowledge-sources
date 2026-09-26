# [Issue #2568] Request-aware automatic config profile selection

source: https://github.com/vllm-project/aibrix/issues/2568
state: closed | updated: 2026-08-21T02:03:34Z
labels: area/gateway

## 正文

### Feature Description and Motivation

AIBrix gateway already supports config profiles. User can define multiple profiles in `model.aibrix.ai/config`, and select one profile by `config-profile` header. This is useful, but it still requires the request sender to know which profile should be used.

I want to propose a request-aware automatic config profile selection layer. The idea is: gateway can select a user-defined profile by request features when the request does not explicitly set `routing-strategy` or `config-profile`.

This does not replace config profiles. It reuses config profiles. Config profiles define what profiles exist, and this feature decides which profile should be selected for this request.

The main motivation is online serving. In many online platforms, application users should not need to understand internal routing strategies such as `pd`, `prefix-cache`, `throughput` or `slo`. The platform/gateway owner may want to control these routing policies centrally.

### Use Case

For one model, different request shapes may need different routing behavior:

- normal short chat request can use `least-request`
- large input request can use a PD related profile
- cache-friendly workload can use `prefix-cache`
- non-streaming long generation can use `throughput`

Today the client can send `config-profile` header, for example `config-profile: large-input`. But this means client must know the profile name and must choose it correctly.

With request-aware profile selection, client can just send normal OpenAI-compatible request. Gateway evaluates request features and chooses profile automatically.

Example:

```json
{
  "defaultProfile": "default",
  "profiles": {
    "default": {
      "routingStrategy": "least-request"
    },
    "large-input": {
      "routingStrategy": "pd",
      "routingConfig": {
        "promptLenBucketMinLength": 8192,
        "prefillScorePolicy": "prefix_cache",
        "decodeScorePolicy": "load_balancing"
      }
    },
    "cache-friendly": {
      "routingStrategy": "prefix-cache"
    },
    "offline-generation": {
      "routingStrategy": "throughput"
    }
  },
  "requestClassRouter": {
    "enabled": true,
    "rules": [
      {
        "name": "large-input",
        "when": {
          "promptTokensGte": 8192
        },
        "profile": "large-input"
      },
      {
        "name": "cache-friendly",
        "when": {
          "headerEquals": {
            "x-aibrix-workload": "cache-friendly"
          }
        },
        "profile": "cache-friendly"
      },
      {
        "name": "offline-generation",
        "when": {
          "stream": false,
          "maxTokensGte": 2048
        },
        "profile": "offline-generation"
      }
    ],
    "fallbackProfile": "default"
  }
}
```

Request class names are not built-in by AIBrix. They are user-defined. The gateway only provides rule matching and profile selection.

### Proposed Solution

Add a request-aware selection step after config profile is loaded, but before routing strategy is derived.

Current flow is roughly:

```go
applyConfigProfile(routingCtx, pods)
deriveRoutingStrategyFromContext(routingCtx)
```

Proposed flow:

```go
applyConfigProfile(routingCtx, pods)
applyRequestClassPolicy(routingCtx, pods)
deriveRoutingStrategyFromContext(routingCtx)
```

When a rule matches, gateway should select the target profile and update both:

```go
routingCtx.ReqConfigProfile = selectedProfileName
routingCtx.ConfigProfile = selectedProfile
```

This is important because some later logic, for example PD bucketing, may resolve profile again by `ReqConfigProfile`.

Suggested priority:

```text
routing-strategy header
  > config-profile header
  > requestClassRouter automatic selection
  > defaultProfile
  > ROUTING_ALGORITHM
```

So explicit user choice is not overwritten.

Suggested first version conditions:

- `promptTokensGte`
- `promptTokensLt`
- `maxTokensGte`
- `maxTokensLt`
- `stream`
- `headerEquals`
- `pathEquals`

I think regex, contains, semantic classifier, and complex expression can be future work. First version should be simple and deterministic.

### Observability

It will be useful to expose selection result in logs or response headers, for example:

```text
x-aibrix-request-class: large-input
x-aibrix-config-profile: large-input
routing-strategy: pd
```

This helps user debug why one request used a specific profile.

### Expected Behavior

- If request has `routing-strategy` header, use it and skip automatic selection.
- If request has `config-profile` header, use it and skip automatic selection.
- If no explicit header is set, evaluate `requestClassRouter` rules in order.
- First matched rule selects its profile.
- If no rule matches, use `fallbackProfile` or `defaultProfile`.
- If selected profile does not exist, gateway should not crash. It can fallback to `defaultProfile` and log warning.

### Value

This feature makes config profiles easier to use in real online serving. It changes profile selection from client-driven to gateway-policy-driven.

Benefits:

- clients do not need to know internal routing strategies
- platform owner can control routing policy centrally
- reduce wrong profile usage
- same model can better serve mixed traffic types
- existing routing algorithms and config profile mechanism can be reused

I think this is a small extension on top of config profiles, but it gives more practical value for production traffic.


## 评论 (7)

### googs1025 · 2026-08-16

cc @varungup90 

### varungup90 · 2026-08-16

To simplify things, should we add an option where the user passes config-profile="auto", allowing the gateway to automatically select the best config profile from the available options?

### googs1025 · 2026-08-16

Thanks, I agree with this direction. I’ll adjust the proposal to make `config-profile: auto` the explicit opt-in trigger for automatic profile selection.

I think the cleanest shape is to keep the selection policy inside the existing `model.aibrix.ai/config`, alongside `profiles`, for example:

```json
{
  "defaultProfile": "default",
  "profiles": {
    "default": {
      "routingStrategy": "least-request"
    },
    "large-input": {
      "routingStrategy": "pd",
      "routingConfig": {
        "promptLenBucketMinLength": 8192
      }
    },
    "offline-generation": {
      "routingStrategy": "throughput"
    }
  },
  "autoProfileSelection": {
    "enabled": true,
    "fallbackProfile": "default",
    "rules": [
      {
        "name": "large-input",
        "when": {
          "promptTokensGte": 8192
        },
        "profile": "large-input"
      },
      {
        "name": "offline-generation",
        "when": {
          "stream": false,
          "maxTokensGte": 2048
        },
        "profile": "offline-generation"
      }
    ]
  }
}
```

The revised behavior would be:

```text
routing-strategy header
  > config-profile header with a concrete profile name
  > config-profile: auto + autoProfileSelection rules
  > defaultProfile
  > ROUTING_ALGORITHM
```

So existing behavior stays unchanged unless the client explicitly sends `config-profile: auto`.

The reason I still think we need a user-defined policy, instead of only adding the `auto` value, is that the gateway should not need to guess profile names, thresholds, or routing intent. For example, there may be multiple profiles using `pd`, or users may name profiles based on their own workload classes. With `autoProfileSelection`, the gateway only evaluates deterministic user-defined rules and resolves `auto` to a concrete profile.

This also keeps the model config structure clear:

```text
profiles = available concrete routing profiles
autoProfileSelection = policy for resolving config-profile: auto
config-profile: auto = request-level opt-in trigger
```

A few fallback cases can be well-defined:

```text
If config-profile is absent:
  keep the current defaultProfile behavior.

If config-profile is a concrete profile name:
  use that profile directly.

If config-profile is auto and autoProfileSelection is enabled:
  evaluate rules in order and use the first matched profile.

If no rule matches:
  use autoProfileSelection.fallbackProfile, or defaultProfile if fallbackProfile is not set.

If a matched rule references a missing profile:
  log a warning and fall back to fallbackProfile/defaultProfile.

If autoProfileSelection is missing or disabled:
  fall back to defaultProfile.
```

Implementation-wise, after auto-selection resolves to a concrete profile, the gateway should update both:

```go
routingCtx.ReqConfigProfile = selectedProfileName
routingCtx.ConfigProfile = selectedProfile
```

This is important because later logic, such as PD bucketing, may resolve the profile again using `ReqConfigProfile`.


### varungup90 · 2026-08-16

I meant that user can pass config-profile = auto and in that case gateway can select any one of the config profile. We do not need to introduce new structure.

### googs1025 · 2026-08-17

 I see. The current design adds autoProfileSelection because without an explicit policy the gateway does not have a deterministic way to know which existing profile should match a request shape.

  For example, a model may define multiple pd profiles with different routingConfig, or profile names may be user-specific. If config-profile:auto simply chooses from profiles without user-defined rules, the selection criteria becomes implicit and hard to reason about.

  Would you prefer:
  1. keeping autoProfileSelection as the explicit request-aware policy, or
  2. removing it and defining a built-in heuristic for selecting from existing profiles? If option 2, what signals should the gateway use to choose among profiles?


### varungup90 · 2026-08-17

I’d prefer to keep the configuration simple, flat, and easy to extend. Rather than introducing a generic when condition layer, we can keep routing-specific knobs inside routingConfig for each profile.

For example, we can start by exposing a small number of signals for the routing algorithms we already support:

* Throughput: maxTokensGte
* Least-KV-Cache: cacheGte
* P/D: promptTokensGte

I think introducing constructs like the following adds unnecessary complexity at this stage:

```
"when": {
  "headerEquals": {
    "x-aibrix-workload": "cache-friendly"
  }
}
```

or:

```
"when": {
  "pathEquals": "/v1/chat/completions",
  "stream": false,
  "maxTokensGte": 2048
}
```

Instead, I’d suggest keeping routing-related configuration consistently under routingConfig for every profile:

```
{
  "defaultProfile": "least-request",
  "profiles": {
    "least-request": {
      "routingStrategy": "least-request",
      "routingConfig": {}
    },
    "cache-friendly": {
      "routingStrategy": "least-kv-cache",
      "routingConfig": {
        "cacheGte": 0.8
      }
    },
    "long-generation": {
      "routingStrategy": "throughput",
      "routingConfig": {
        "maxTokensGte": 2048
      }
    },
    "large-input": {
      "routingStrategy": "pd",
      "routingConfig": {
        "promptLenBucketMinLength": 8192,
        "promptTokensGte": 8192
      }
    }
  }
}
```

This keeps the profile schema consistent and gives each routing algorithm a clear place for its own configuration knobs. We can add more fields under routingConfig as needed without introducing a separate generic condition/matching framework.

If we later have concrete use cases that require matching on headers, paths, streaming mode, or combinations of conditions, we can introduce that abstraction then.

### googs1025 · 2026-08-18

I updated the PR to remove the generic `autoProfileSelection` / `when` layer and move the first-version auto-selection knobs into each profile `routingConfig`.

The current scope is limited to request-local signals that can be evaluated before deriving the concrete routing strategy:

- `promptTokensGte` / `promptTokensLt`
- `maxTokensGte` / `maxTokensLt`

I also removed the header/path/stream matching support and removed the `cacheGte` example from the PR. `cacheGte` is different from the request-local signals because cache match/usage depends on cache-aware routing state and scoring, which is normally available inside the KV-cache routing path after strategy-specific context is available. I think we should define that computation path separately before adding `cacheGte` to auto profile selection.
