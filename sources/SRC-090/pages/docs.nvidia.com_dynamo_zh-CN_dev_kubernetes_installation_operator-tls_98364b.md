source: https://docs.nvidia.com/dynamo/zh-CN/dev/kubernetes/installation/operator-tls
lastmod: 2026-09-23T23:30:39.914Z

# Operator TLS

Configure TLS once at the platform level and auto-inject it into every deployment

The Dynamo operator can inject TLS configuration into every
`DynamoGraphDeployment`

(DGD) pod automatically, so you don’t have to set the
`DYN_TCP_TLS_*`

and `NATS_TLS_*`

environment variables on each component. TLS
is configured once at the platform level via `InfrastructureConfiguration`

, and
the operator propagates the corresponding env vars to all DGD pods it manages.

For the full list of TLS/mTLS environment variables and CLI flags, and for the
per-component configuration method, see the
[TLS reference](https://docs.nvidia.com/dynamo/dev/reference/components/tls-configuration).

## Frontend HTTP TLS

Operator-level TLS settings inject `DYN_TCP_TLS_*`

and `NATS_TLS_*`

for internal
transports. They do not inject the frontend’s `DYN_TLS_*`

HTTP settings.

To enable HTTPS or HTTP mTLS, explicitly set `DYN_TLS_CERT_PATH`

,
`DYN_TLS_KEY_PATH`

, and, for mTLS, `DYN_TLS_CLIENT_CA_CERT_PATH`

in the frontend
container’s `podTemplate`

environment. Mount the server certificate, private
key, and trusted client CA at those paths. See the
[HTTP TLS reference](https://docs.nvidia.com/dynamo/dev/reference/components/tls-configuration#http-tls-and-mtls)
for the configuration requirements.

## Operator-level TLS configuration

Set the values in the operator Helm chart. When installing the operator as
part of the platform chart, prefix them with `dynamo-operator.`

:

Or pass them via `--set`

during `helm install`

/`helm upgrade`

(platform chart
shown; drop the `dynamo-operator.`

prefix if installing the subchart directly):

Per-component env vars in `podTemplate`

take precedence over operator-level
values when both are set.

When any `natsTLS*`

value is set, `natsAddr`

**must** use the
`tls://`

scheme — the runtime fails closed at startup otherwise. If you are
using the bundled NATS subchart, also enable TLS on the server side (see
[Enabling TLS on the NATS server](https://docs.nvidia.com/dynamo/dev/reference/components/tls-configuration#enabling-tls-on-the-nats-server)).

## Operator-level mTLS configuration

mTLS certificate paths can also be configured at the operator level:

The certificates themselves are typically delivered by a certificate
management system (such as cert-manager) and mounted into the pods at the
paths referenced above. The operator injects the **paths** (via env vars),
not the volumes — the cert files must exist at those paths in every DGD pod.

A common setup is to issue a `Certificate`

with cert-manager, store it in a
Kubernetes `Secret`

, and mount that Secret as a volume in the pod template:

This example shows a single component (`Frontend`

); every component that
receives the TLS env vars needs the same volume mounts. If you are using the
operator’s auto-injection, apply these mounts in each component’s
`podTemplate`

.

For NATS TLS to work, the NATS server itself must also be
configured to listen on TLS. The operator injects the **client-side** env
vars, but enabling TLS on the NATS server subchart is a separate step — see
[Enabling TLS on the NATS server](https://docs.nvidia.com/dynamo/dev/reference/components/tls-configuration#enabling-tls-on-the-nats-server)
in the TLS reference.