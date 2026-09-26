source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/fault-tolerance/graceful-shutdown
lastmod: 2026-09-24T19:58:16.636Z

# Graceful Shutdown

Let workers finish in-flight requests and release resources cleanly when a pod is terminated.

When Kubernetes terminates a pod (rollout, scale-down, node drain), Dynamo workers stop accepting new requests, keep serving in-flight ones through a grace period, then release engine and connection resources before exiting. This is **on by default** — every component handles `SIGTERM`

/`SIGINT`

and drains automatically. The steps below tune *how long* it waits and make sure interrupted requests are recovered.

The knobs are three timeouts plus enabling migration. The default flow: endpoints unregister from discovery immediately, workers serve for a short grace period, then endpoints drain (bounded by a timeout) before resources are cleaned up.


How it works:the signal handlers, the`graceful_shutdown()`

sequence, per-backend`cleanup()`

code, and error-initiated shutdown are documented in[Graceful Shutdown Architecture].

### Set the pod termination grace period

Kubernetes gives a terminating pod `terminationGracePeriodSeconds`

to exit before it sends `SIGKILL`

.
Dynamo operator-created pods default to **60 seconds**. Set a longer value when expected generation
time or high utilization can keep admitted requests active beyond that window:

Rough guidance:

### Tune the drain windows

Three environment variables control Dynamo’s internal draining. Set the HTTP timeout on the Frontend and the runtime values on worker components:

The defaults are sound for most deployments. Raise the relevant timeout only for long generations or sustained high utilization. Keep every internal timeout below `terminationGracePeriodSeconds`

so Dynamo can finish its own cleanup before Kubernetes force-kills the pod.

### Enable migration so drained requests retry

Draining lets *current* requests finish, but a request interrupted by an unexpected worker loss still needs somewhere to go. Enable [request migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration) on the Frontend so disconnected streams are retried on healthy workers. Set `DYN_MIGRATION_LIMIT`

in the Frontend `env:`

(or `--migration-limit`

in its `args:`

):

Backend workers always drain with `graceful_shutdown=True`

; they don’t need any migration configuration themselves. See [Request Migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration) for the full walkthrough.

### Verify graceful shutdown

Trigger a shutdown (for example `kubectl delete pod <worker-pod>`

or a rollout) and watch the worker logs for the shutdown sequence:

During Frontend shutdown, `/health`

returns 503 so readiness routing stops, while `/live`

remains
200 so Kubernetes does not restart the process during the drain. New OpenAI-compatible requests return
503, but admitted response bodies and accepted `/v1/realtime`

WebSocket sessions continue until they
finish or `DYN_HTTP_GRACEFUL_SHUTDOWN_TIMEOUT_SECS`

expires.

During worker shutdown, endpoints unregister and stop receiving new work while admitted requests
complete. If a pod receives `SIGKILL`

before draining finishes, increase
`terminationGracePeriodSeconds`

(step 1) or lower the relevant internal timeout (step 2).

## Custom workers

If you author your own worker with the Dynamo SDK, the `graceful_shutdown`

parameter on `serve_endpoint()`

controls whether that endpoint waits for in-flight requests (`True`

) or returns immediately (`False`

). Backend workers default to `True`

. For the parameter, the shutdown sequence, and per-backend cleanup patterns, see [Graceful Shutdown Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/graceful-shutdown-architecture) and the [Writing Python Workers](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/writing-python-workers) guide.

## Related Documentation

[Graceful Shutdown Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/graceful-shutdown-architecture)- Signal handling, drain sequence, and resource cleanup internals[Request Migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration)- How interrupted requests migrate to healthy workers[Request Cancellation Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture)- Canceling in-flight requests[Health Check Reference](https://docs.nvidia.com/dynamo/reference/observability/health-checks)- Liveness and readiness endpoints