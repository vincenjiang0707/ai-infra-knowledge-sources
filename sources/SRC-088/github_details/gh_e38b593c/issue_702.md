# [Issue #702] [RFC]: Make speculators import-cheap

source: https://github.com/vllm-project/speculators/issues/702
state: open | updated: 2026-09-08T07:49:17Z
labels: RFC

## 正文

### Motivation.

**1. Importing the package is heavy, and its registry auto-discovery is advertised but never implemented.**
Any `import speculators` — even for a lightweight helper — eagerly pulls in the full model stack (torch/transformers), because the top-level package does all model/proposal registration and schema-building at import time. It has to: the registry classes advertise auto-discovery, but that machinery was never actually implemented, so registration silently depends on those eager imports happening in a specific order. The result is a package that's slow and noisy to import, relies on an import side-effect it doesn't admit to, and is fragile to circular imports. The fix in either case is to implement the auto-discovery the registry already claims to have (register + build schemas on first use) so the eager imports can go away. That leaves one decision — what happens to the top-level API:

- **Option A (non-breaking):** make the top-level import lazy (PEP 562 `__getattr__`, as `transformers` does). Importing a submodule no longer drags in torch, and `from speculators import X` keeps working unchanged.
- **Option B (breaking):** drop the top-level re-exports entirely (empty `__init__`, slime-style) and import from submodules everywhere (`from speculators.config import X`). Simpler package init, but it breaks the public API and every existing call site.

I personally prefer option B, while my claude code opus 4.8 votes for A 🤯 

**2. The dataset registry is defined twice, and de-duplicating it is blocked by (1).**
There are two `DATASET_CONFIGS`: a plain-dict one in `scripts/response_regeneration/script.py` (magpie/ultrachat/gsm8k) and a `DatasetConfig` dataclass one in `src/speculators/data_generation/configs.py` (sharegpt/ultrachat/gsm8k/sharegpt4v_coco). `ultrachat` and `gsm8k` are defined in both, so adding or changing a dataset means editing two places in two formats (drift risk). 

The natural fix — have the regen script consume the shared registry — is **non-trivial today precisely because of (1)**: importing the shared registry drags the full torch/transformers stack into a standalone HTTP script. So (1) is a prerequisite; once the package is import-cheap, the unification becomes a small, torch-free change.


### Proposed Change.

see above

### Any Other Things.

_No response_

## 评论 (3)

### orestis-z · 2026-07-02

Thanks for the detailed write-up — I verified all three claims and they check out.

**On the import weight:** The chain is `__init__.py` → `.config`/`.model`/`.models`/`.proposals` → top-level `import torch` / `from transformers import ...`, plus `reload_schemas()` at init. The `.models/__init__.py` alone eagerly pulls in all 5 model implementations. Only 8 symbols are re-exported via `__all__`, so the cost-to-value ratio is poor.

**On auto-discovery:** Confirmed dead code. `ClassRegistryMixin` declares `registry_auto_discovery`, `auto_package`, and documents `auto_populate_registry` in docstrings, but `auto_populate_registry` is never defined. Three classes (`TokenProposalConfig`, `SpeculatorModelConfig`, `SpeculatorModel`) set `registry_auto_discovery = True` — it does nothing. Registration only works because the eager imports happen to trigger side-effect registration.

**On DATASET_CONFIGS:** The two registries overlap on `ultrachat` and `gsm8k` but use different schemas (`DatasetConfig` dataclass vs plain dicts) and serve different pipelines, so unification isn't trivial even after (1) is resolved — the schemas would need to be reconciled too.

**On Option A vs B:** I'd vote for **A** (PEP 562 `__getattr__`). It preserves the public API, follows the pattern used by `transformers`/`numpy`, and the real fix is implementing auto-discovery regardless — once `auto_populate_registry` actually works and registration is on-first-use, the eager imports in `__init__.py` become lazy `__getattr__` lookups with no behavior change for users.

### fynnsu · 2026-07-08

For context, some form of auto-discovery did exist at some point but it was removed to simplify import / setup logic.

I'd be okay with doing some kind of lazy import of the different algorithms using something like "Option A". I'd prefer not to re-introduce complex auto-discovery logic. The way vllm handles this is with large static [registry dicts](https://github.com/vllm-project/vllm/blob/a5d19cbb95872c4b426c06735733568542fa33db/vllm/model_executor/models/registry.py#L71) with the package name and model name, which can then be imported on demand. Something like that for our algorithms might make sense. 

### LOGO127 · 2026-09-08

Would a compatibility-first implementation of this still be welcome? I would be interested in taking it on if nobody is already working on it.

An AI-assisted source audit and real subprocess probe against `3419401a380db305ed6493ba4680ad8a3c3e0e45` confirmed that importing just `speculators.utils.registry` loads torch, transformers, and all six current model families. There is a second eager boundary in `utils/__init__.py` through `pydantic_utils`, so changing only the root package would not make that helper import cheap.

The main compatibility constraint seems to be schema initialization: `PydanticClassRegistryMixin` captures registered choices in its tagged union, and an empty registry falls back to an any-schema. Deferring imports must not accidentally weaken validation or omit supported model types.

Proposed acceptance checks:

- Fresh-process root and registry-helper imports do not load torch/transformers.
- All eight public exports retain their identity and from-import behavior.
- Fresh-process config parsing, JSON schema choices, and save/load round-trips retain all six model families; unknown discriminator values still fail.
- Explicit custom registration plus `reload_schemas()` continues to work, with import-order and concurrent-first-use coverage.

Would you prefer a first stage that defers the existing complete registration/schema initialization until a model/config API is used, or static per-algorithm dispatch in this change as well? I would avoid package scanning/complex auto-discovery as requested above. I would also keep #1083's inherited-registry fix separate and would not reopen the dataset-unification work from #777.

Only baseline export/schema/custom-proposal checks have been run so far; there is no implementation, model-loading validation, or measured speedup yet. Happy to align scope and wait for assignment before implementing.

