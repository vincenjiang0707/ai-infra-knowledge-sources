source: https://docs.nvidia.com/dynamo/zh-CN/reference/api/python/mocker
lastmod: 2026-09-23T23:30:39.914Z

# dynamo.mocker

`dynamo.mocker`

publishes 12 classes and 18 functions. Source: `components/src/dynamo/mocker/__init__.py`


###### AicEngineConfig (class)


AIC model/backend identity used by native forward-pass estimates.

`lib/bindings/python/src/dynamo/_core.pyi#L1742`


**Public methods**

**init**

No summary available.

###### EngineCapacity (class)


###### EngineCapacityRequest (class)


Request shape and SLA policy for find_engine_capacity_rps.

`lib/bindings/python/src/dynamo/_core.pyi#L1799`


**Public methods**

**init**

No summary available.

###### EnginePerfLimits (class)


Engine limits used by engine-level helper queries and default correction bounds.

`lib/bindings/python/src/dynamo/_core.pyi#L1766`


**Public methods**

**init**

No summary available.

###### MockEngineArgs (class)


###### OptimizationTarget (class)


###### ProfileDataResult (class)


Result of processing —planner-profile-data argument. Cleans up tmpdir on deletion.

`components/src/dynamo/mocker/args.py#L51`


**Public methods**

**init**

No summary available.

###### ReasoningConfig (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L2031`


**Public methods**

**init**

No summary available.

###### RustEnginePerfModel (class)


Engine-level performance model backed by AIC forward-pass modeling.

`lib/bindings/python/src/dynamo/_core.pyi#L1823`


**Public methods**

#### best_available

Build from all available inputs; explicit AIC config is preferred, then engine args, then regression-only.

#### from_regression

Build a regression-only model that learns from observed FPM wall times.

#### from_native

Build a strict native AIC model; unsupported AIC configs raise an error.

#### estimate_forward_pass_time

Estimate one scheduled forward-pass iteration in seconds from current-version FPMs.

#### tune_with_fpms

Tune with current-version observed FPMs: outer list is iterations, inner list is attention-DP ranks.

#### diagnostics

Return AIC diagnostics as a JSON string.

#### get_min_correction_factor

Return the minimum ready native correction factor, or None if no factor is ready.

#### get_max_correction_factor

Return the maximum ready native correction factor, or None if no factor is ready.

#### get_avg_correction_factor

Return the average ready native correction factor, or None if no factor is ready.

#### get_queued_prefill_time

Estimate queued prefill drain time; adjust queued tokens outside the shim for KV reuse.

#### get_scheduled_decode_itl

Estimate scheduled decode ITL in seconds; aggregated workers include scheduled or learned average prefill load.

#### find_engine_capacity_rps

Search sustainable per-engine RPS; inspect eligible to see whether eligible SLA metrics passed.

###### RustEnginePerfOptions (class)


Online tuning options for RustEnginePerfModel.

`lib/bindings/python/src/dynamo/_core.pyi#L1781`


**Public methods**

**init**

No summary available.

###### SglangArgs (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L2040`


**Public methods**

**init**

No summary available.

###### TrtllmArgs (class)


No summary available.

`lib/bindings/python/src/dynamo/_core.pyi#L2052`


**Public methods**

**init**

No summary available.

###### apply_worker_engine_args_overrides (function)


###### build_mocker_engine_args (function)


###### build_runtime_config (function)


###### compute_stagger_delay (function)


Compute the stagger delay based on worker count to give the frontend time to process registrations. Returns the delay in seconds between worker launches.

###### graceful_shutdown (function)


Shutdown dynamo distributed runtime instances. The endpoints will be immediately invalidated so no new requests will be accepted.

###### launch_workers (function)


Launch mocker worker(s) with isolated DistributedRuntime instances.

Each worker gets its own DistributedRuntime, which means:

- Separate etcd/NATS connections
- Separate Component instances (no shared overhead)
- Independent service registration and stats scraping
- But still sharing the same tokio runtime (efficient)

###### load_mocker_engine_args (function)


###### main (function)


###### non_negative_float (function)


###### non_negative_int (function)


###### parse_args (function)


Parse command-line arguments for the Dynamo mocker engine.

**Returns**

`argparse.Namespace`

— argparse.Namespace: Parsed command-line arguments.

###### parse_bootstrap_ports (function)


Parse comma-separated bootstrap ports string into list of integers.

###### positive_int (function)


###### prefetch_model (function)


Pre-fetch model from HuggingFace to avoid rate limiting with many workers.

###### resolve_planner_profile_data (function)


Resolve —planner-profile-data to an NPZ file path.

Handles backward compatibility by accepting either:

- A mocker-format NPZ file (returned as-is)
- A profiler-style results directory (converted to mocker-format NPZ)

**Parameters**

Path from —planner-profile-data argument.

**Returns**

`ProfileDataResult`

— ProfileDataResult with npz_path and optional tmpdir for cleanup.

**Raises**

`FileNotFoundError`

— If path doesn’t contain valid profile data in any supported format.

###### run_mocker_trace_replay (function)


###### validate_worker_type_args (function)


Resolve disaggregation mode from —disaggregation-mode or legacy boolean flags. Raises ValueError if validation fails.

###### worker (function)


Main worker function that launches mocker instances.

Each mocker gets its own DistributedRuntime instance for true isolation, while still sharing the same event loop and tokio runtime.