# [Issue #2583] RoleSet and StormService should reject invalid role specs during admission

source: https://github.com/vllm-project/aibrix/issues/2583
state: closed | updated: 2026-08-22T23:31:36Z
labels: help wanted

## 正文

### Bug description

While smoke-testing the latest upstream `main` controller and CRDs on minikube, I found several RoleSet / StormService spec validation gaps that can produce misleading Ready status or a repeated controller reconcile loop.

The most important cases are:

1. Duplicate `RoleSet.spec.roles[*].name` is accepted.
   - Observed: only one Pod is created for the duplicated role name, but RoleSet status contains two entries with the same role name and both are reported ready.
   - Impact: status aggregation becomes misleading and can confuse users or higher-level automation.

2. Invalid role names such as `bad_role` are accepted.
   - Observed: the controller tries to create Pods with names derived from the invalid role name, Kubernetes rejects those Pod names, and the RoleSet is reconciled repeatedly.
   - Impact: a bad spec can create a stable reconcile loop and unnecessary API/controller load.

3. Empty roles are accepted.
   - `RoleSet.spec.roles: []` is accepted and the RoleSet can become `Ready=True` with no workload Pods.
   - `StormService.spec.template.spec.roles: []` is accepted, creates an empty RoleSet, and StormService can report `replicas=1`, `readyReplicas=1` with no workload Pods.
   - Impact: this creates a false positive Ready signal.

4. Negative per-role replicas are accepted in RoleSet.
   - Observed: a role with `replicas: -1` is accepted and can become `Ready=True` with the role effectively treated as zero replicas.
   - Impact: invalid configuration is silently normalized instead of being rejected.

### Steps to reproduce

1. Deploy the latest upstream `main` CRDs and controller to minikube.
2. Create a RoleSet with duplicate role names.
3. Create a RoleSet with a role named `bad_role`.
4. Create a RoleSet with `spec.roles: []`.
5. Create a StormService whose `spec.template.spec.roles` is empty.
6. Create a RoleSet role with `replicas: -1`.
7. Check the resulting Pods, RoleSet / StormService status, events, and controller logs.

### Expected behavior

These invalid specs should be rejected during admission instead of being accepted and left for controllers to handle.

Recommended validation coverage:

- Reject empty `RoleSet.spec.roles`.
- Reject empty `StormService.spec.template.spec.roles`.
- Reject invalid role names, ideally using DNS-1123-compatible validation because role names are used to derive child resource names.
- Reject duplicate role names.
- Reject negative per-role replicas.

This can be addressed with validating webhook logic and/or CRD schema/CEL validation where appropriate. The same RoleSetSpec validation should be reused for direct RoleSet resources and nested StormService RoleSet templates.

Please also add integration tests covering these invalid specs, especially:

- Direct RoleSet admission tests.
- StormService admission tests for nested RoleSet template validation.
- Regression coverage for duplicate role names and invalid role names.

### Environment

- AIBrix version: upstream `main`, commit `136197c8db5ab353052234749a53d0534b3590de`
- Deployment environment: minikube
- Controller image: `aibrix/controller-manager:nightly`
- CRDs and controller deployed from `config/crd` and `config/default`


## 评论 (1)

### original4422 · 2026-08-20

I’d like to work on this. I plan to add shared RoleSetSpec schema validation for empty/duplicate/invalid role names and negative replicas, with envtest coverage for both direct RoleSets and nested StormService templates.
