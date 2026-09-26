source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/overview
lastmod: 2026-09-23T23:30:39.914Z

# DynoSim

DynoSim is Dynamo’s simulation stack for exploring serving configurations before validating them on real clusters. It is not a separate service; it is the product surface that connects workload-driven simulation runs, configuration sweeps, the mocker engine, Planner simulation, Router simulation, and AIC-backed timing models into one workflow.

Use DynoSim when you want to answer questions such as:

- Which aggregated or disaggregated topology should this workload use?
- How many prefill and decode workers fit within my GPU budget?
- How sensitive is the deployment to startup time, queue pressure, prefix reuse, or router tuning?
- Which candidates should I validate with AIPerf on real GPUs?

## Components

## How the tools differ

The tools overlap in workflow but perform different jobs:

With `timing.type: default`

, DynoSim uses the performance model shipped by AISimulate to estimate how
long model work takes. Mocker and DynoSim simulate how requests move through scheduling, KV-cache,
routing, and Planner behavior. Set `timing.type`

to `fixed`

or `polynomial`

when calibrated timing is
not required.

## Workflow

Start with `aisimulate predict --stack dynamo`

to verify the workload shape and engine configuration.
Use `aisimulate recommend --stack dynamo`

to search the design space. Launch live Mocker workers
when an integration test needs the real Dynamo runtime. Validate the shortlist on real GPUs before
production rollout.

## Where AISimulate Fits

AISimulate provides performance models and candidate-shape information. DynoSim uses those models for default timing and parallelism recommendation. Mocker still owns the scheduler and KV-memory simulation: batching, prefix-cache hits, preemption, block allocation, and request lifecycle are simulated by Dynamo’s Mocker core, while AISimulate-backed timing predicts how long prefill and decode work should take for supported model/backend/GPU combinations.

## Choosing an Entry Point

DynoSim narrows the search space; it does not replace real-hardware validation. Use it to move quickly, find promising candidates, and understand failure modes before spending cluster time.