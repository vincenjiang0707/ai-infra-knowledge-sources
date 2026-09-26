source: https://docs.nvidia.com/dynamo/zh-CN/dev/reference/components/tls-configuration
lastmod: 2026-09-23T23:30:39.914Z

# TLS

Configure HTTPS, HTTP mutual TLS, and internal TCP/NATS encryption

NVIDIA Dynamo supports opt-in TLS encryption for the frontend HTTP API, the TCP
request and response streams between frontends and workers, and connections to
NATS. On the TCP transport, both the **request plane**
(frontend → worker inference requests) and the **response stream** (worker →
frontend inference output) are encrypted using
[rustls](https://github.com/rustls/rustls) with the `ring`

cryptographic
provider. When no TLS configuration is provided, these transports operate in
plaintext exactly as before.

The `DYN_TCP_TLS_*`

environment variables encrypt the frontend↔worker TCP
request and response streams; NATS traffic is encrypted separately via NATS TLS
(see the NATS TLS section below). The KV event plane is a separate transport:
when it runs over ZMQ it is **not** encrypted, and when it runs over NATS it is
encrypted only if NATS TLS is configured.

## HTTP TLS and mTLS

The frontend accepts HTTPS connections from external clients or an API gateway.
Configure these options on the frontend; they are independent of the internal
`DYN_TCP_TLS_*`

and `NATS_TLS_*`

settings.

HTTP mTLS requires both the server certificate and private key. When a client CA is configured, the frontend rejects TLS handshakes from clients that omit a certificate or present one that is not trusted by that CA. Without a client CA, HTTPS authenticates only the server. The client or API gateway configures its own client certificate/key and trust for the frontend’s server certificate.

The frontend loads its HTTP TLS configuration at startup. Its server
certificate and private key hot-reload for subsequent handshakes; changing the
trusted client CA requires a restart. See [Design notes](https://docs.nvidia.com/dynamo/dev/reference/components/tls-configuration#design-notes) for
rotation behavior and the [frontend configuration reference](https://docs.nvidia.com/dynamo/dev/reference/components/frontend-configuration)
for the complete frontend argument list.

## Environment variables

The following variables configure internal TCP TLS. Server configuration is validated when the server starts; client connectors initialize lazily on the first outbound connection.

Both frontends and workers act as TCP server and client depending on the stream direction (response streams: worker dials frontend; request streams: frontend dials worker). Set the internal TCP TLS configuration on every participating pod. HTTP TLS settings apply only to the frontend HTTP server.

### Server role (accepting connections)

### Client role (dialing connections)

## CLI flags

The same configuration is available via command-line flags on all backends
(vllm, sglang, trtllm, tokenspeed) through `DynamoRuntimeArgGroup`

:

The frontend (`dynamo.frontend`

) also accepts `--tcp-tls-cert-path`

,
`--tcp-tls-key-path`

, and `--tcp-tls-ca-cert-path`

.

## Quick start

Generate a self-signed certificate for local testing:

Both frontend and worker need the same flags (both act as server and client):

## Kubernetes deployment

In Kubernetes, TLS certificates are typically delivered by a certificate
management system and mounted into pods. Set the
environment variables on each component’s pod template in the
`DynamoGraphDeployment`

spec:

Both components need the same TLS env vars because each acts as both TCP server and client depending on the stream direction.

For platform-wide TLS that the operator injects into every deployment
automatically — instead of setting env vars on each component — see
[Operator TLS](https://docs.nvidia.com/dynamo/dev/kubernetes/installation/operator-tls).

## NATS TLS

NATS carries JetStream indexer recovery/replay, the audit sink, and — when the
request plane is set to NATS (`--request-plane nats`

) — inference request
distribution. TLS is configured separately from TCP:

When only the `tls://`

URL scheme is used without explicit TLS env vars,
async-nats handles TLS natively with system roots.

The `NATS_SERVER`

URL accepts both `nats://`

and `tls://`

schemes, but setting
any explicit NATS TLS variable (`NATS_TLS_*`

) requires the `tls://`

scheme —
startup fails with a clear error otherwise.

CLI flags (all backends via `DynamoRuntimeArgGroup`

):

The frontend (`dynamo.frontend`

) also accepts `--nats-tls-ca-cert-path`

and
`--nats-tls-insecure`

.

### Enabling TLS on the NATS server

The env vars above configure the **client** side (Dynamo verifying the NATS
server). For TLS to work, the NATS server itself must also be configured to
listen on TLS — otherwise a client that sets `NATS_TLS_CA_CERT_PATH`

(or the
operator-level `natsTLSCAPath`

) will attempt a TLS handshake against a
plaintext port and fail.

When deploying Dynamo’s platform chart, the bundled NATS subchart exposes this
via `nats.config.nats.tls`

. The certificates are typically delivered by a
certificate management system such as cert-manager.

**One-way TLS** (server presents a cert, clients verify it):

Or, if the cert files are mounted into the pod by an external system, use the
`merge`

block to point at the on-disk paths directly:

Then point the Dynamo clients at the TLS endpoint and give them the CA.
These are operator-subchart values, so nest them under `dynamo-operator:`

when
using the platform chart:

**mTLS** (server also verifies client certs) — add `ca_file`

and `verify`

to
the server’s `merge`

block, and present a client identity from the Dynamo side:

See the [NATS TLS documentation](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls)
for the full server-side TLS schema.

## Mutual TLS (mTLS)

By default only the server is authenticated (the client verifies the server’s
certificate). Mutual TLS additionally makes the **client present a certificate**
that the **server verifies**, so both ends of a connection prove their identity.
mTLS is opt-in and layered on top of the TLS configuration above.

For the **TCP** transports (request plane + response stream) Dynamo owns both
ends, so configure two things and — since every component is both TCP client and
server — set both on every pod:

**On the client:**a client certificate/key to present.**On the server:**a CA certificate (`DYN_TCP_TLS_CLIENT_CA_CERT_PATH`

) to verify the presented client certificate. When set, the server**requires**a trusted client certificate and rejects the handshake otherwise.

For **NATS** the broker is external, so Dynamo only presents a client identity —
there is no Dynamo-side “server” half. Whether client certificates are actually
required is enforced by the **NATS server** configuration (e.g.
`tls { ca_file: ...; verify: true }`

), not by Dynamo.

### TCP request/response streams

### NATS


Note:Dynamo cannot detect whether the NATS broker actually requests a client certificate. If you set`NATS_TLS_CLIENT_CERT_PATH`

/`_KEY_PATH`

but the broker is not configured to verify client certs, the connection silently falls back to ordinary one-way TLS. Enable verification on the NATS server (`verify: true`

) to make NATS mTLS effective.

Client certificate and key must be set **together**, and a client identity
requires a server CA (`*_CA_CERT_PATH`

) — or insecure mode for development — so
the server can still be verified. The TCP **servers** and the **NATS** client
validate this at startup and fail closed. The TCP **client** connectors,
however, initialize lazily on the first outbound connection, so an incomplete
TCP client config surfaces as a per-connection handshake failure rather than a
startup crash. The client certificate/key hot-reload from disk on rotation,
exactly like the server certificate (see Design notes).

The same options are available as CLI flags on all backends (via
`DynamoRuntimeArgGroup`

) and the frontend (`dynamo.frontend`

):

## Encrypted paths

When TLS is configured, the following transports are encrypted (the ZMQ event plane is not covered):

## Design notes

- HTTP server certificates and private keys use the shared hot-reload resolver. A background thread checks for file changes every 30 seconds (sooner after a failed reload). Valid updates apply to subsequent handshakes; existing connections remain open, and a failed reload retains the last valid certificate. The HTTP client CA is loaded at startup and requires a frontend restart after rotation.
- Server certificates hot-reload: the request-plane and response-stream servers
serve their leaf cert/key through a resolver that re-reads the files from disk
when their contents change (detected by a content hash, so rotations done by
an atomic symlink swap are handled too), so certificate rotation
takes effect
**without a process restart**. The check is rate-limited (at most once every 30s, sooner after a failed reload) and never blocks a handshake; a failed reload keeps serving the last valid certificate. Client trust anchors (the CA) are still loaded once, so rotating the CA itself requires a restart. - mTLS
**client identity**certificates hot-reload through the same resolver, so a rotated client cert/key is picked up without a restart. The CA used by the server to verify client certificates is loaded once (rotating it needs a restart). - Client TLS connectors are built once and cached via
`OnceCell`

on the first outbound connection. - The TLS handshake is spawned per-connection on both the request plane and response stream servers so the accept loop is never blocked.
- Invalid TLS configuration on the request plane (e.g. bad cert path) prevents server startup rather than silently falling back to plaintext.
- When server and client TLS configurations are mismatched (e.g., server has TLS but client does not), a warning is logged at startup.
- An empty CA certificate file is detected at load time and rejected with a clear error message.