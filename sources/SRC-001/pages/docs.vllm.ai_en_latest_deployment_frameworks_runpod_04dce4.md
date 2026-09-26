source: https://docs.vllm.ai/en/latest/deployment/frameworks/runpod/
lastmod: 2026-09-24

# RunPod[¶](https://docs.vllm.ai#runpod)

vLLM can be deployed on [RunPod](https://www.runpod.io/), a cloud GPU platform that provides on-demand and serverless GPU instances for AI inference workloads.

## Prerequisites[¶](https://docs.vllm.ai#prerequisites)

- A RunPod account with GPU pod access
- A GPU pod running a CUDA-compatible template (e.g.,
`runpod/pytorch`

)

## Starting the Server[¶](https://docs.vllm.ai#starting-the-server)

SSH into your RunPod pod and launch the vLLM OpenAI-compatible server:

Note

Use `--host 0.0.0.0`

to bind to all interfaces so the server is reachable from outside the container.

## Exposing Port 8000[¶](https://docs.vllm.ai#exposing-port-8000)

RunPod exposes HTTP services through its proxy. To make port 8000 accessible:

- In the RunPod dashboard, navigate to your pod settings.
- Add
`8000`

to the list of exposed HTTP ports. -
After the pod restarts, RunPod provides a public URL in the format:


## Troubleshooting 502 Bad Gateway[¶](https://docs.vllm.ai#troubleshooting-502-bad-gateway)

A `502 Bad Gateway`

error from the RunPod proxy typically means the server is not yet listening. Common causes:

**Model still loading**— Large models take time to download and load into GPU memory. Check the pod logs for progress.**Wrong host binding**— Ensure you passed`--host 0.0.0.0`

. Binding to`127.0.0.1`

(the default) makes the server unreachable from the proxy.**Port mismatch**— Verify the`--port`

value matches the port exposed in the RunPod dashboard.**Out of GPU memory**— The model may be too large for the allocated GPU. Check logs for CUDA OOM errors and consider using a larger instance or adding`--tensor-parallel-size`

for multi-GPU pods.

## Verifying the Deployment[¶](https://docs.vllm.ai#verifying-the-deployment)

Once the server is running, test it with a curl request:

Command

Response

You can also check the server health endpoint: