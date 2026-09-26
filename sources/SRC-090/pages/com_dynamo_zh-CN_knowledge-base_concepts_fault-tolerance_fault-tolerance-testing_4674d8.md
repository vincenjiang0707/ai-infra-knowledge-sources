source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/concepts/fault-tolerance/fault-tolerance-testing
lastmod: 2026-09-24T19:58:16.636Z

# Fault Tolerance Testing

This document describes the test infrastructure for validating Dynamo’s fault tolerance mechanisms. The testing framework supports request cancellation, migration, etcd HA, and hardware fault injection scenarios.

## Overview

Dynamo’s fault tolerance test suite is located in `tests/fault_tolerance/`

and includes:

## Test Directory Structure

## Request Cancellation Tests

Test that in-flight requests can be properly canceled.

### Running Cancellation Tests

### Cancellation Test Utilities

The `cancellation/utils.py`

module provides:

#### CancellableRequest

Thread-safe request cancellation via TCP socket manipulation:

#### send_completion_request / send_chat_completion_request

Send cancellable completion requests:

#### poll_for_pattern

Wait for specific patterns in logs:

## Migration Tests

Test that requests migrate to healthy workers when failures occur.

### Running Migration Tests

### Migration Test Utilities

The `migration/utils.py`

module provides:

- Frontend wrapper with configurable request planes
- Long-running request spawning for migration scenarios
- Health check disabling for controlled testing

### Example Migration Test

## etcd HA Tests

Test system behavior during etcd failures and recovery.

### Running etcd HA Tests

### Test Scenarios

**Leader failover**: etcd leader node fails, cluster elects new leader**Network partition**: etcd node becomes unreachable**Recovery**: System recovers after etcd becomes available

## Hardware Fault Injection

The fault injection service enables testing under simulated hardware failures.

**Test harness only — never deploy in production.** The fault injection service ships with a `ClusterRole`

(`fault-injection-api`

) granting `patch`

on nodes/pods/services, `create`

/`delete`

on `NetworkPolicy`

, and full control on chaos-mesh CRDs (`NetworkChaos`

, `PodChaos`

, `StressChaos`

, `IoChaos`

). It also deploys a privileged kernel-mode `DaemonSet`

capable of synthesizing GPU XID errors. Any caller reachable to the API can cause arbitrary pod kills, network partitions, IO faults, and GPU XID errors across the cluster. Deploy only into dedicated test clusters that you are willing to disrupt, never expose the API externally, and tear down with `kubectl delete -f deploy/`

after each test run. See [ tests/fault_tolerance/hardware/fault_injection_service/README.md](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/tests/fault_tolerance/hardware/fault_injection_service/README.md) for the full security posture.

### Fault Injection Service

Located at `tests/fault_tolerance/hardware/fault_injection_service/`

, this FastAPI service orchestrates fault injection:

### Supported Fault Types

#### GPU Faults

#### Network Faults

### Fault Injection API

#### Inject GPU Fault

#### Inject Specific XID Error

Supported XID codes: 43, 48, 74, 79, 94, 95, 119, 120

#### Inject Network Partition

#### Recover from Fault

#### List Active Faults

### GPU Fault Injector Agent

The GPU fault injector runs as a DaemonSet on worker nodes:

The agent injects fake XID messages via `/dev/kmsg`

to trigger NVSentinel detection.

## Deployment Testing Framework

The `deploy/`

directory contains an end-to-end testing framework.

### Test Phases

Tests run through three phases:

### Scenario Configuration

Define test scenarios in `scenarios.py`

:

### Running Deployment Tests

### Validation Checkers

The framework includes pluggable validators:

### Results Parsing

Parse test results for analysis:

## Client Utilities

The `client.py`

module provides shared client functionality:

### Multi-Threaded Load Generation

### Request Options

## Running the Full Test Suite

### Prerequisites

- Kubernetes cluster with GPU nodes
- Dynamo deployment
- etcd cluster (for HA tests)
- Fault injection service (for hardware tests)

### Environment Setup

### Run All Tests

### Test Markers

## Best Practices

### 1. Isolate Test Environments

Run fault tolerance tests in dedicated namespaces:

### 2. Clean Up After Tests

Ensure fault injection is recovered:

### 3. Collect Logs

Preserve logs for debugging:

### 4. Monitor During Tests

Watch system state during tests:

## Related Documentation

[Request Migration](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-migration-architecture)- Migration implementation details[Request Cancellation](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture)- Cancellation implementation[Health Check Reference](https://docs.nvidia.com/dynamo/reference/observability/health-checks)- Health monitoring[Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)- Available metrics for monitoring