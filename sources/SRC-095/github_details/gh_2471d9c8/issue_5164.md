# [Issue #5164] [Bug] `kubectl ray session` leaves its child `kubectl port-forward` running after the session is terminated

source: https://github.com/ray-project/kuberay/issues/5164
state: closed | updated: 2026-09-22T22:12:38Z
labels: bug

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

kubectl-plugin

### KubeRay Version

v1.7.0-rc.0

### Ray Version

2.52.0

### Environment

- Kubernetes version: v1.31.0
- Kubernetes cluster type: kind v0.24.0, single node
- Helm chart version (if applicable): helm-chart/kuberay-operator @ v1.7.0-rc.0
- Installation method: Helm
- OS: Linux


### What happened + What you expected to happen

`kubectl ray session` spawns `kubectl port-forward` as a child process via `exec.CommandContext`. When the session process is terminated by a signal sent to its PID alone, the child survives, is reparented to the subreaper, and keeps all four listeners on 8265/10001 open — the dashboard still answers 200 after the session is gone, and the next `kubectl ray session` cannot bind those ports.

The context handed to `exec.CommandContext` can never be cancelled: `cmd/kubectl-ray.go` calls `root.Execute()`, so cobra supplies `context.Background()`, and there is no signal handling anywhere under `kubectl-plugin/`. Interactive `Ctrl-C` only cleans up today because the terminal signals the whole foreground process group — which is also why `test/e2e/kubectl_ray_session_test.go` kills by
pgid and never exercises this path.

Expected: terminating the session tears down its port-forward child.

There is a second, independent problem in the same area: the retry loop at `session.go` treats `address already in use` the same as a transient connection drop, so a session that collides with a leftover forward hangs in a 3s retry loop instead of failing with an error that names the conflict.

### Reproduction script

```bash
kubectl ray create cluster raycluster-sample
kubectl wait --for=condition=RayClusterProvisioned raycluster/raycluster-sample --timeout=300s

kubectl ray session raycluster-sample &
SPID=$!
until ss -ltn | grep -q ':8265'; do sleep 2; done

ss -ltnp | grep -E ':8265|:10001'     # note the pid holding the listeners
kill "$SPID"                          # SIGTERM to the session PID only, not the process group
wait "$SPID" 2>/dev/null

ss -ltnp | grep -E ':8265|:10001'     # same pid, still holding all four listeners
curl -s -o /dev/null -w '%{http_code}\n' localhost:8265   # 200
kubectl ray session raycluster-sample # cannot bind; retries forever
```

Observed (plugin + operator v1.7.0-rc.0, kind, K8s v1.31.0):

```bash
### before the kill                              (ss columns trimmed for width)
$ ss -ltnp | grep -E ':8265|:10001'
LISTEN 127.0.0.1:8265   users:(("kubectl",pid=36163,fd=8))
LISTEN 127.0.0.1:10001  users:(("kubectl",pid=36163,fd=11))
LISTEN     [::1]:8265   users:(("kubectl",pid=36163,fd=9))
LISTEN     [::1]:10001  users:(("kubectl",pid=36163,fd=12))
$ ps -o pid=,ppid= -p 36163
  36163   36137                                 # parent is the session

### kill the session PID only, then re-check
$ kill 36137; ps -p 36137
    PID TTY          TIME CMD                   # session gone
$ ss -ltnp | grep -E ':8265|:10001'
LISTEN 127.0.0.1:8265   users:(("kubectl",pid=36163,fd=8))
LISTEN 127.0.0.1:10001  users:(("kubectl",pid=36163,fd=11))
LISTEN     [::1]:8265   users:(("kubectl",pid=36163,fd=9))
LISTEN     [::1]:10001  users:(("kubectl",pid=36163,fd=12))
$ ps -o pid=,ppid= -p 36163
  36163      17                                 # ppid changed -> orphaned, reparented to the subreaper
$ curl -s -o /dev/null -w '%{http_code}\n' localhost:8265
200                                             # still served by the orphan
```

A following `kubectl ray session` never recovers — it does not fail fast, it retries forever:

```console
Unable to listen on port 8265: ... bind: address already in use
Unable to listen on port 10001: ... bind: address already in use
error: unable to listen on any of the requested ports: [{8265 8265} {10001 10001}]
failed to port-forward: exit status 1. Retrying in 3s ...
```

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!


## 评论 (3)

### omkar619-dev · 2026-08-19

Hi @CheyuWu — are you already working on this one? Happy to leave it with you
since it's your component; asking before I start anything. While reading the code I turned up on two things that seem worth recording here
either way:

**1. The `job submit` comparison doesn't hold as a signal-handling precedent.** `job_submit.go:447-457` uses `portforward.NewCmdPortForward` — the in-process cobra command, no child process at all. Its `defer cancel()` is skipped on
SIGTERM exactly like `session`'s deferrals are; it just has nothing to orphan. So the difference isn't "cancellable context vs not", it looks like "in-process vs shelling out".

The root cause looks upstream of `session.go`: `cmd/kubectl-ray.go` calls `root.Execute()`, and cobra's `ExecuteC` sets                                               `c.ctx = context.Background()` when no context was supplied (`command.go:1085` in v1.10.2). There's no `signal.NotifyContext` anywhere in `kubectl-plugin`, so the `ctx` reaching `exec.CommandContext` can never fire and the kill path is unreachable. Interactive `Ctrl-C` only works today because the terminal signals the whole foreground process group, which is also why `test/e2e/kubectl_ray_session_test.go` kills by `pgid` and never exercises this path.

**2. Fixing the context surfaces a second bug in the retry loop.** Once `ctx` is genuinely cancellable, the `for {}` at `session.go:194-209` keeps
going: `exec.CommandContext` on a cancelled context returns immediately, so the loop becomes sleep-3s-retry forever instead of exiting. It needs a `ctx.Err() != nil` check before the retry.

One scoping thought btw: the second half of your report — failing fast on `address already in use` rather than retrying it as a transient drop — is independent of the process-lifecycle half and needs no change to `cmd/kubectl-ray.go`. If you're taking the lifecycle part, I'd be glad to pick up the fail-fast part separately so the two don't collide. Also worth noting #2987 is still an open draft covering the programmatic-port-forward direction.

### omkar619-dev · 2026-08-20

Thanks @win5923 — picking this up. @CheyuWu shout if you'd already started locally and I'll back off.
Quick note on direction before I write anything, since #2987 is still open on the same file. My plan is to leave the `kubectl port-forward` shell-out exactly as it is and just add the signal handling that isn't there yet — `signal.NotifyContext` in `cmd/kubectl-ray.go` plus `ExecuteContext`, so the ctx reaching `exec.CommandContext` can actually fire. That looks orthogonal to the programmatic-vs-shell-out question: if #2987 lands later the signal handling is still correct and still needed either way, so I don't think this has to settle that debate.

Two things I'll handle in the same PR: the first signal needs to cancel and then restore default disposition, so a second Ctrl-C still hard-kills anything that ignores ctx; and the retry loop at `session.go:194-209` needs a `ctx.Err()` check, because once ctx is genuinely cancellable `exec.CommandContext` returns immediately and the loop turns into a 3s spin forever.

I'll leave the fail-fast-on-`address already in use` half out of this PR to keep it single-concern, and follow up separately unless you'd rather have both together. Does that split sound right btw?

### CheyuWu · 2026-08-20

Hi @omkar619-dev — I haven't started anything locally, so it's all yours. 
