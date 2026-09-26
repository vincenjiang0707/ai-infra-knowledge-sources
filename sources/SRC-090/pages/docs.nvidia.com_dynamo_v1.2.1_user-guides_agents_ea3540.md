source: https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents
lastmod: 2026-09-24T19:58:16.636Z

# Agents

Agent-aware serving features in Dynamo

Dynamo provides a small set of request extensions and trace utilities for serving agentic workloads. The harness remains responsible for the semantic agent trajectory. Dynamo receives lightweight metadata and uses it for serving telemetry, routing hints, and backend-specific cache behavior.

## Core Concepts

## Backend-Specific Guides

Agent features are exposed through common request metadata, but backend support varies by runtime.

## Request Surface

Agent-facing request metadata lives under `nvext`

on OpenAI-compatible request
bodies:

Use `agent_context`

when you want traceability across LLM calls, tool calls, and
external trajectory files. Use `agent_hints`

only when the harness has
serving-relevant intent that Dynamo can act on.