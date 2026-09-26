# [Issue #724] Refactor CLI/Config in v0.7.0

source: https://github.com/vllm-project/guidellm/issues/724
state: closed | updated: 2026-07-01T17:08:20Z
labels: priority-high, internal, feature, cli

## 正文

> [!NOTE]
> This proposal is human written.

The goal of this proposal is to define a new standard CLI and config (previously known as scenario) format which solves many usability issues and allows us to implement new features which are prohibitively difficult to add to the existing design.

## Usability Improvements

Here are a few issues that often crop up in the current design and how this proposal addresses them.

### Better data configuration

One critical limitation of the existing (<=v0.6.0) design for the `--data` argument is it is really hard to determine what a user intended when something is entered incorrectly. Most users of GuideLLM are likely familiar with some variant of this error (truncated to avoid taking up an entire page):

```python
ValueError: Data deserialization failed, likely because the input doesn't match any of the input formats. See the 15 error(s) that occurred while attempting to deserialize the data prompt_tokens=e,output_tokens=50:
  - Deserializer 'huggingface': (HFValidationError) Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'prompt_tokens=100,output_tokens=50'.
...
```

This is because a data string like `prompt_tokens=100,output_tokens=50` contains no information on what kind of dataset it is. GuideLLM will attempt to parse it as every kind of dataset and if they all fail, it will return the error of every dataset type. With this proposal we have eliminated this ambiguity by adding a `type` field to configure explicitly which kind of dataset is being requested. This also has the added benefit of making it possible to have multiple dataset formats which closely match. Such as mookcake dataset which would normally conflict with plain jsonl.

### Built-in option documentation

The current GuideLLM CLI is very limited in what is documented, but internally every field has a description. Since the run CLI exposes users to the internal type lookup tables we can make a very intuitive help system for describing available options (note final format will differ):

```
$ guidellm describe backend openai_http
HTTP backend for OpenAI-compatible servers.

Supports OpenAI API, vLLM servers, and other compatible endpoints with
text/chat completions, streaming, authentication, and multimodal inputs.
Handles request formatting, response parsing, error handling, and token
usage tracking with flexible parameter customization.

Fields:
  - target: str
    Base URL of the OpenAI-compatible server
  - model: str | None
    Model identifier for generation requests
  - request_format: Literal["/v1/completions"] (default "/v1/completion")
    Request format for OpenAI-compatible server. 
```

### Config layering

While the GuideLLM CLI/Config format is very powerful, often there are times where a pair or multiple options should always be configured together. For instance, with the recent addition of Geospatial model support The existing CLI requires both `--request-format /pooling` and `--data-column-mapper pooling_column_mapper`. These multi-component workloads will most likely become more common with Mooncake and tool-calling additions in the future. Currently GuideLLM already has the concept of a builtin scenario to help address this problem, however only one scenario (builtin or custom) can be passed. 

By allowing multiple configs and implementing rules for layering we can embed common use-cases as configs that can be layered into a benchmark. For example:

```sh
guidellm run \
    --config well-lit/geospatial \
    --config special/trace_data \
    --config custom.yaml
```

could enable the Geospatial model arguments, configure the profile for trace data, and run the users custom config.


## New Features

Here are a few new features this redesign will enable.

### Per-benchmark randomness

Randomness plays a few different roles in GuideLLM; likely the most important role is in generating synthetic data. In the current design of GuideLLM the randomness of synthetic data suffers due to a compromise made with real datasets. If given a series of rates (e.g. `--rate 1,2,4,8`) GuideLLM always starts each rate at the same location in the dataset. For pre-created datasets this means replaying the exact same requests in the exact same order for each rate. For synthetic data this means reinitializing the dataset using the same random seed which results in the same requests. This is fine for use-cases that don’t involve any sort of server-side caching and is necessary for use-cases where the goal is to evaluate response quality at each rate. However once caching is introduced this can cause issues if the previous rate’s requests are not evicted from the cache. To work around this the synthetic data generator inserts an index marker at the beginning of the prompt which matches the index of the current rate. This approach has at least 3 problems:

1. `prefix_tokens` are unaffected by this index and are thus shared across all rates
2. If `--data-samples` is set, the dataset is generated once before all benchmarks which results in the index marker being a static 1.
3. The order of rates affects the values in the dataset even when random is static

To fix these problems (and a few others) the new configuration is designed to give control over randomness at a per-benchmark level. For example:

```yaml
---
global:
    seed:
        type: increment
        start: 42
        step: 2
```

will start the first benchmark with a random seed of 42 and increment the seed by 2 for each subsequent benchmark whereas:

```yaml
---
global:
    seed:
        type: static
        value: 42
```

will use a static seed for each benchmark. With static, the seed can be overwritten by each benchmark to allow more manual control.

### Conditional constraint groups (Future work)

With the new design we can support more advanced combinations of constraints such as logical groups. For example

```yaml
---
global:
    constraints:
      - type: "AND_op"
        constraints:
          - type: "min_requests"
            count: 256
          - type: "OR_op"
            constraints:
              - type: "max_requests"
                count: 512
              - type: "over_saturation"
```

could be used to ensure a minimum number of requests are run and then stop either when a max is hit or when oversaturation occurs.

### Plugins (Future work)

Since v0.4 GuideLLM has been designed as an extendable architecture. Many internal components are implemented as registries. For example the backend registry has the `openai_http` and `python_vllm` backends registered to it. However, the current CLI implementation limits the usefulness of adding to these registries externally. This is due some static type checking as well as the inability for external code to to extend the CLI with new options. With this new CLI design it will be easier to allow plugins to define their own options and the separation of config from functional class will allow argument validation to be handled by plugins.

## Examples

### RHAIIS Regression Workload Example

Common use-case from the PSAP RHAIIS sub-team.

#### YAML

```yaml
---
global:
    backend:
        type: "openai_http"
        target: "http://localhost:8000"
        request_format: "/v1/completions"
    constraints:
      - type: "max_seconds"
        seconds: 600
    data:
      - type: synthetic
        prompt_tokens: 1000
        output_tokens: 1000
    seed:
        type: increment
        start: 42
benchmarks:
  - profile.streams: 1
    constraints[0].seconds: 60
  - profile.streams: 50
    constraints[0].seconds: 120
  - profile.streams: 100
    constraints[0].seconds: 120
  - profile.streams: 200
    constraints[0].seconds: 120
  - profile.streams: 300
  - profile.streams: 500
  - profile.streams: 650
outputs:
  - type: json
    path: benchmarks.json
```

#### CLI

```sh
guidellm run \
    --output json path=./benchmarks.json
    --backend openai_http target=http://host:8000,request_format=/v1/completions \
    --constraint max_seconds seconds=600 \
    --profile concurrent \
    --data synthetic prompt_tokens=1000,output_tokens=1000 \
    --seed auto start=42 \
    --override "profile.streams" 1,50,100,200,300,500,650 \
    --override "constraint[0].seconds" 60,120,120,120,,,
```

### Exhaustive Example

Example with most of the options set.

```yaml
---
global:
    backend:
        type: "openai_http"
        target: "http://localhost:8000"
        request_format: "/v1/chat/completions"
        model: "OpenAI/gpt-oss-120b"
        processor: "OpenAI/gpt-oss-120b"
        validate_backend: true
        verify: false
    profile:
        type: "concurrent"
        rampup: 3
        warmup: 10
        cooldown: 20
    constraints:
      - type: "max_seconds"
        seconds: 50
      - type: "over_saturation"
    data_loader:
        type: "generative"
        sampler: null   # Currently --data-sampler
        samples: 1000   # Currently --data-samples
        start_index: 0  # Index to start the dataset at
        num_workers: 10 # Currently --data-num-workers
    data_column_mapper:
        type: "generative_column_mapper"
        mappings:
            text_column: "article"
            output_tokens_count_column: "output_tokens"
    data_preprocessors:
      - type: "encode_media"
      - type: "custom_pre"
        max_len: 256
    data_finalizer:
        type: "generative"
    data:
      - type: synthetic
        prompt_tokens: 50
        output_tokens: 100
        load_args: ...  # Currently --data-args
    seed: 
        type: increment  # Auto increment based on benchmark index
        start: 56
        by: 1
benchmarks:
  - profile.streams: 50
  - profile.streams: 100
    profile.rampup: 10
    profile.warmup: 0
    profile.cooldown: 0
    constraints[0].seconds: 100
outputs:
  - type: json
    exclude_requests: true
    path: benchmarks.json
  - type: csv
    path: benchmarks.csv
  - type: jsonl_requests
    sample_requests: 50
    path: benchmark.jsonl
```

## Notes

### Open Questions

#### 1. How will well-lit paths / layering work?

Example: `guidellm run --config builtin/geospatial --config custom.yaml` should enable the required options for geospatial models and then layer custom configs on top.

One problem to solve here is how to handle list options (aka data). By default they should probably be fully overwritten but could (and should) we come up with a design that allows merging lists? The previous version of this proposal had a “merge_lists” key at the top of the config but that seems too coarse. Also how do we handle merging the merge option? Does the last one apply to all config layers? Does each “merge_list” config only merge lists with the one before it or the one after it?

Another problem is how to merge incompatible `type`s. Aka if one config has `type: "openai_http"` and the next has `type: "vllm_python"` what happens to all of the configured options since they may not be valid for other types? What happens if a different type is layered in-between two compatible types?  I think the solution here is to build a graph of every type while layering configs and then apply whichever one is seen last.

## Implementation Details (TBD)

Currently YAML and CLI arguments feed into a Pydantic model called `BenchmarkGenerativeTextArgs`. This config model then is passed to the `benchmark_generative_text` function which spawns the required resources. In the new design `BenchmarkGenerativeTextArgs` will be split into multiple layers. For example:

```python
class BenchmarkArgs(StandardBaseModel):
    global: BenchmarkGlobalArgs = Field(
        default_factory=BenchmarkGlobalArgs,
        description="Global benchmark args container",
    )
    benchmarks: list[dict[str, Any] | None] = Field(
        default_factory=list,
        description="Individiual benchmark overrides",
    )
    outputs: list[BenchmarkOutputArgs] = Field(
        default_factory=list,
        description="Benchmark outputs",
    )
    
class BenchmarkGlobalArgs(StandardBaseModel):
    backend: BackendArgs
    profile: ProfileArgs
    constraints: list[ConstraintArgs]
    ...

```

Individual global args will be owned by the related component. For example The backend component will have a `BackendArgs` (this already exists) pydantic registry which is subclassed for each backend. The overlying `BenchmarkGlobalArgs` will implement helper validation and serialization methods that use the provided type field to create the appropriate subclass for each global arg. For example:

```yaml
---
global:
    backend:
        type: openai_http
        target: "http://localhost"
```

will become

```python
BenchmarkArgs(
    global=BenchmarkGlobalArgs(
        backend=OpenAIHttpBackendArgs(
            target="http://localhost",
        ),
    ),
)
```

Note, The existing `BackendArgs` will have to be modified to be a registry and contain a type field.


## 评论 (2)

### sjmonson · 2026-06-18

Some details of this plan have changed; notably: 

- Use of the key `type` has been changed to `kind` since `type` is a reserved Python keyword.
- `global` has been renamed to `spec` and outputs have been nested under it.
- Added separate `tokenizer` section
- The initial implementation will only support `benchmarks` / `--override` for `profile.rate` or `profile.streams`.

```yaml
---
spec:
    backend:
        kind: "openai_http"
        target: "http://localhost:8000"
        request_format: "/v1/chat/completions"
        model: "OpenAI/gpt-oss-120b"
        validate_backend: true
        verify: false
    tokenizer:
        kind: huggingface_auto
        name: "OpenAI/gpt-oss-120b"
    profile:
        kind: "concurrent"
        rampup: 3
        warmup: 10
        cooldown: 20
    constraints:
      - kind: "max_duration"
        seconds: 50
      - kind: "over_saturation"
    data_loader:
        kind: "generative"
        sampler: null   # Currently --data-sampler
        samples: 1000   # Currently --data-samples
        start_index: 0  # Index to start the dataset at
        num_workers: 10 # Currently --data-num-workers
    data_column_mapper:
        kind: "generative_column_mapper"
        mappings:
            text_column: "article"
            output_tokens_count_column: "output_tokens"
    data_preprocessors:
      - kind: "encode_media"
      - kind: "custom_pre"
        max_len: 256
    data_finalizer:
        kind: "generative"
    data:
      - kind: synthetic
        prompt_tokens: 50
        output_tokens: 100
        load_args: ...  # Currently --data-args
    seed: 
        kind: static
        value: 42
    outputs:
      - kind: json
        path: benchmarks.json
      - kind: csv
        path: benchmarks.csv
benchmarks:
  - profile.streams: 50
  - profile.streams: 100
```

### sjmonson · 2026-07-01

Initial design completed
