# [Issue #1430] [RFC]: Add Integration Tests for CRD Controller

source: https://github.com/vllm-project/aibrix/issues/1430
state: closed | updated: 2026-09-20T14:04:04Z
labels: help wanted, area/testing, area/orchestration

## 正文

### Summary

### Description:

Currently, many CRD controllers rely heavily on unit tests and e2e tests, but lack dedicated integration tests that verify:

Controller behavior when interacting with a real (or simulated) Kubernetes API server
Reconciliation logic under realconditions

I will sort out the controller info later

### Motivation

Add Integration Tests for CRD Controller

### Proposed Change

Add a /integration/controller directory
Write integration tests for core reconciliation paths


### Alternatives Considered

_No response_

## 评论 (4)

### Jeffwan · 2025-08-13

This is great!

### googs1025 · 2025-08-19

Update:  https://github.com/vllm-project/aibrix/pull/1448 has been merged. I will submitted some Integration tests for some controllers later. In the near future, we hope that controller part modifications will not only have unit tests, but also corresponding integration test cases to cover.

### googs1025 · 2025-09-03

As the CRD controller becomes more complete, we need more test cases.



### googs1025 · 2025-09-03

some info can be found here: https://github.com/vllm-project/aibrix/pull/1491#issuecomment-3212932811
