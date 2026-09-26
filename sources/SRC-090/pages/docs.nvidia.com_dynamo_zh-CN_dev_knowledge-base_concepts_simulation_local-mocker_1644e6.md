source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/local-mocker
lastmod: 2026-09-23T23:30:39.914Z

# Simulate a Local Deployment with Mocker

Run a GPU-free frontend and simulated worker from the command line

Mocker is a simulated Dynamo backend. Use it locally to test frontend discovery, routing, KV events,
and worker behavior without loading a model or using GPUs. This is a **live simulation**: you start a
frontend and workers, then send HTTP requests through the Dynamo runtime.

For a faster **offline replay** that drives simulated engines directly without a frontend, worker
registration, or runtime services, see [Run a DynoSim Simulation](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/simulation-runs).

This tutorial uses file-based discovery so that the frontend and worker can run without etcd or
NATS. For Kubernetes, see
[Simulate a Kubernetes Deployment](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/kubernetes-mocker).
For commonly used flags, see the
[Mocker CLI Reference](https://docs.nvidia.com/dynamo/dev/reference/components/mocker-cli-reference).

## Prerequisites

Install Dynamo by following [Install Dynamo](https://docs.nvidia.com/dynamo/dev/cli/installation/install-dynamo). Verify that
the local environment can import the frontend and Mocker modules:

### Start the frontend

In the first terminal, start the OpenAI-compatible frontend:

File-based discovery keeps this tutorial on one machine and selects the local event path.

### Start a Mocker worker

In a second terminal, start one simulated worker with the same discovery backend:

Wait for the worker to register with the frontend.

### Send a request

In a third terminal, send a request to the frontend:

A successful response confirms that local discovery and request routing are working.

### Run multiple simulated workers

Stop the Mocker process and restart it with four workers:

Send several requests and compare the frontend and worker logs. For local scale tests, prefer
`--num-workers`

over launching many separate Mocker processes because the workers share one runtime
and thread pool.

### Simulate disaggregated serving

Stop the aggregated Mocker process. Start a prefill worker:

In another terminal, start a decode worker:

Send another request and inspect both worker logs to confirm that the request moved through prefill and decode.

### Tune the simulation

Restart the worker with settings that match the experiment you want to run. For example:

Use the [Mocker CLI Reference](https://docs.nvidia.com/dynamo/dev/reference/components/mocker-cli-reference) for scheduling,
KV-cache, timing, AIC, and transport settings. Use [Run a DynoSim Simulation](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/simulation-runs) when you want
to replay a complete trace without managing live frontend and worker processes.