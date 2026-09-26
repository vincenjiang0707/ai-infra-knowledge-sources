source: https://docs.nvidia.com/dynamo/zh-CN/reinforcement-learning/overview
lastmod: 2026-09-24T19:58:16.636Z

# Reinforcement Learning

Use Dynamo as the rollout-serving plane for RL training systems

**Experimental.** Dynamo can serve rollout generation for reinforcement learning systems that need more than a static inference endpoint. RL frameworks remain responsible for the training loop, reward pipeline, policy update logic, and checkpoint production; Dynamo provides the serving plane around rollout workers.

Use Dynamo when your RL system needs low-latency generation, backend-aware routing, worker discovery, rollout metadata, weight refreshes, fault tolerance, and autoscaling as part of the training loop. The goal is to let RL engineers operate the rollout path with production serving primitives while still integrating with the framework that owns training.

## Where Dynamo Fits

A typical RL setup has three planes:

Dynamo sits between the RL orchestrator and inference backends such as vLLM, SGLang, and TensorRT-LLM. For SGLang rollouts, use Dynamo’s SGLang-compatible `POST /generate`

or `PUT /generate`

API. This API routes token-input requests through Dynamo. It preserves SGLang’s native streaming response objects. The OpenAI-compatible frontend remains available for cross-backend integrations. Use backend-specific control surfaces to manage workers.

## What Dynamo Adds

## Integration Pattern

- Deploy Dynamo with the inference backend you want to use for rollouts.
- For SGLang, enable the SGLang-compatible
`/generate`

API. - Send native token-input requests through the Dynamo frontend.
- For cross-backend clients, use the OpenAI-compatible completion or chat routes.
- When you use the OpenAI-compatible routes, request token and log probability fields through NVIDIA request extensions.
- Discover live rollout workers when the orchestrator needs direct worker administration.
- Pause selected workers, refresh weights, validate the update, and resume generation.
- Use Dynamo’s routing, autoscaling, and fault-tolerance features to keep rollout serving aligned with training demand.

For the concrete API shapes, environment variables, and command examples, see the [RL Implementation Guide](https://docs.nvidia.com/dynamo/reinforcement-learning/rl-implementation-guide).

## Framework Integrations

Use Dynamo as the rollout-serving plane behind an RL framework. The framework remains responsible for the training loop and policy updates; Dynamo serves rollout generation and provides production serving capabilities around the rollout workers.

## Backend Support Snapshot

## Start Here

Use the [RL Implementation Guide](https://docs.nvidia.com/dynamo/reinforcement-learning/rl-implementation-guide) when you are ready to wire an orchestrator to Dynamo. It covers:

- The vLLM happy path for token-in rollouts, worker discovery, and weight updates.
- The recommended SGLang
`/generate`

path for native token-in/token-out rollouts. - NVIDIA request extensions for token IDs, log probabilities, routed expert data, and SGLang metadata uploads.
- The
`/v1/rl/workers`

discovery API and direct`/engine/`

administration routes. - How to register custom engine routes for framework-specific rollout control.