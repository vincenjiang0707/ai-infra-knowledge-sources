# [Issue #2245] nixlBackendEngine constructor dereferences customParams, which defaults to nullptr

source: https://github.com/ai-dynamo/nixl/issues/2245
state: closed | updated: 2026-09-18T07:16:13Z
labels: 

## 正文

`nixlBackendEngine`'s constructor dereferences `init_params->customParams` without checking it, while the field defaults to `nullptr`:

```cpp
// src/api/cpp/backend/backend_aux.h
class nixlBackendInitParams {
public:
    std::string localAgent;
    nixl_backend_t type;
    nixl_b_params_t *customParams = nullptr;   // <-- default
    ...
};

// src/api/cpp/backend/backend_engine.h
explicit nixlBackendEngine(const nixlBackendInitParams *init_params)
    : backendType(init_params->type),
      customParams(*init_params->customParams),   // <-- unchecked
      localAgent(init_params->localAgent),
      enableTelemetry_(init_params->enableTelemetry_) {}
```

`nixlAgent` always fills the field, so this never fires in normal use. It fires immediately for anyone constructing a backend engine directly, which is what a backend's own unit tests do:

```cpp
nixlBackendInitParams p{};
p.localAgent = "test";
p.type = "MYBACKEND";
nixlMyEngine eng(&p);   // segfault at 0x8
```

```
Caught signal 11 (Segmentation fault: address not mapped to object at address 0x8)
==== backtrace ====
 3  nixlMyEngine::nixlMyEngine()
 4  main()
```

The fix is `p.customParams = &some_empty_params;`, which is easy once you know, and not discoverable from the declaration: a field with a default of `nullptr` reads as optional.

Two options, either of which would do:

- treat it as optional in the constructor, e.g. `customParams(init_params->customParams ? *init_params->customParams : nixl_b_params_t{})`
- or make it non-optional: drop the `= nullptr` default, or take a reference, so the requirement is visible at the declaration

Found while writing unit tests for an out-of-tree storage backend. Happy to send a patch for whichever shape you prefer.

Version: `main` at 992b0a8, GCC 14.3.1, C++20.


## 评论 (1)

### hgichon · 2026-09-13

Correcting my own suggestion above: **"drop the `= nullptr` default" does not work**, and I should have checked it before writing it down.

With `nixlBackendInitParams p{};` the member is value-initialized either way, so removing the default member initializer leaves it null exactly as before and fixes nothing. Worse, it makes `nixlBackendInitParams p;` leave an indeterminate pointer, which turns a reliable segfault into an unpredictable one. Forcing the field to be supplied would need a real interface change — a reference, or a constructor parameter — not the removal of a default.

The other half of what I wrote still stands, and is the part worth doing:

```cpp
customParams(init_params->customParams ? *init_params->customParams
                                       : nixl_b_params_t{}),
```

One thing I did not account for: this stops the base constructor from crashing, but it does not make a null `customParams` generally safe. Several backends dereference the pointer directly in their own constructors, before or independently of any check:

- `src/plugins/gpunetio/gpunetio_backend.cpp:52` — `custom_params->count("network_devices")`
- `src/plugins/obj/obj_backend.cpp:37` — `custom_params->find("type")`
- `src/plugins/obj/s3_accel/dell/engine_impl.cpp:318` — `init_params->customParams->emplace(...)`

Those backends genuinely require parameters, so tolerating null there is a separate question about what an absent-parameters backend should do. I have kept the PR to the base-class crash and have not touched them.

PR: #2246

