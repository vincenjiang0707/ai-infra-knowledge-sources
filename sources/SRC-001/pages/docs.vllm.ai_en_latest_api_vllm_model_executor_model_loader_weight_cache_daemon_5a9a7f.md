source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_cache/daemon/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.weight_cache.daemon`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon)

Weight cache daemon for fast engine restarts.

One daemon process per GPU holds the post-quantized, TP-sharded weights of its rank in GPU memory and serves CUDA IPC handles to vLLM engines over a Unix domain socket. Restarting engines map the weights via zero-copy IPC instead of reloading from disk.

Launch one daemon per TP rank with a single command:

```
python -m vllm.model_executor.model_loader.weight_cache.daemon \
--model /path/to/model --tensor-parallel-size 4
```


Engines then load from the daemons with:

```
vllm serve /path/to/model --tensor-parallel-size 4 \
--load-format ipc_cache
```


Tensor, expert and data parallelism are supported; pipeline parallelism is rejected at launch.

For multi-node tensor parallelism, run one launcher per node with a shared rendezvous so the global TP group forms across nodes (CUDA IPC handles are node-local, so each node serves only its local GPUs' shards). Reuse the same `--nnodes`

/`--node-rank`

/`--master-addr`

flags you pass the engine, plus a `--weight-cache-master-port`

distinct from the engine's `--master-port`

:

```
# node 0 (8 local GPUs)
python -m vllm.model_executor.model_loader.weight_cache.daemon \
--model /path/to/model --tensor-parallel-size 16 \
--nnodes 2 --node-rank 0 --master-addr 10.0.0.1 \
--weight-cache-master-port 29600
# node 1 (8 local GPUs)
python -m vllm.model_executor.model_loader.weight_cache.daemon \
--model /path/to/model --tensor-parallel-size 16 \
--nnodes 2 --node-rank 1 --master-addr 10.0.0.1 \
--weight-cache-master-port 29600
```


The global TP rank of local GPU `i`

on node `r`

is `r * (tp_size // nnodes) + i`

, matching vLLM's contiguous per-node rank assignment, so each engine worker maps its shard from the daemon on its own node.

For data parallelism (e.g. a TP1 x DP16 x EP decode fleet) run one launcher per node with the engine's DP placement flags. Local GPU `i`

serves DP rank `start_rank + i // tp_size`

and TP rank `i % tp_size`

, and all `dp_size * tp_size`

daemons form one world group on `--data-parallel-address`

/`--weight-cache-master-port`

so the expert shards are laid out exactly as in the engine:

```
# node r (4 local GPUs)
python -m vllm.model_executor.model_loader.weight_cache.daemon \
--model /path/to/model --tensor-parallel-size 1 --enable-expert-parallel \
--data-parallel-size 16 --data-parallel-size-local 4 \
--data-parallel-start-rank 4r --data-parallel-address 10.0.0.1 \
--weight-cache-master-port 29600
```


Data parallelism also combines with multi-node tensor parallelism: pass both flag sets (`--nnodes`

/`--node-rank`

/`--master-addr`

and the DP flags with a reachable `--data-parallel-address`

). Each node then serves a contiguous block of the `dp_size * tp_size`

global ranks, e.g. TP8 x DP2 on 4 nodes:

```
# node r (4 local GPUs)
python -m vllm.model_executor.model_loader.weight_cache.daemon \
--model /path/to/model --tensor-parallel-size 8 --enable-expert-parallel \
--nnodes 4 --node-rank r --master-addr 10.0.0.1 \
--data-parallel-size 2 --data-parallel-address 10.0.0.1 \
--weight-cache-master-port 29600
```


With MTP, EAGLE or EAGLE3 speculative decoding the launcher additionally starts a draft daemon group that caches the draft model. It uses its own cache key, Unix sockets (`*_draft.sock`

) and rendezvous port (`--weight-cache-draft-master-port`

, default `--weight-cache-master-port + 1`

), so each process serves exactly one model role. Other draft types are not cached and keep loading from disk in the engine.

Classes:

-
–[WeightCacheDaemon](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon)Per-GPU process that loads one TP shard and serves CUDA IPC handles.


Functions:

-
–[export_entries](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.export_entries)Export a model's tensors, preserving tied-parameter aliases.

-
–[get_draft_daemon_config](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.get_draft_daemon_config)VllmConfig for the draft daemon group

-
–[plan_local_ranks](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.plan_local_ranks)`(local_rank, dp_rank, tp_rank)`

for every GPU this launcher serves.

##

`WeightCacheDaemon`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon)

Per-GPU process that loads one TP shard and serves CUDA IPC handles.

Methods:

-
–[get_model](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon.get_model)Load the daemon's model, composed from the configured loader.

-
–[serve_forever](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon.serve_forever)Serve requests until terminated.


## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


|
|

###

`_acquire_gpu_lock(socket_path)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon._acquire_gpu_lock)

Take an exclusive lock guarding this GPU's socket path.

The lock is advisory and released automatically when the daemon exits (or crashes), so a stale socket is only ever removed by whoever owns the lock. A running daemon holding it makes a second daemon fail fast instead of clobbering the live socket.

## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


###

`get_model()`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon.get_model)

Load the daemon's model, composed from the configured loader.

Runs the quantization check after model creation but before the slow weight load, so an unsupported method fails fast. Online quantization always fails the check, so load_model's finalize step for it is unnecessary here.

## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


###

`serve_forever(ready_callback=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon.serve_forever)

Serve requests until terminated.

The socket is only bound once the model is fully cached, so clients get a connection error (and fall back to disk) until the daemon is ready.

Parameters:

-

(`ready_callback`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.WeightCacheDaemon.serve_forever(ready_callback))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[], None] | None`None`

) –Invoked once the socket is bound and listening, so the launcher can report overall readiness.


## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


##

`_reject_unsupported_parallelism(parallel_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon._reject_unsupported_parallelism)

Reject pipeline parallelism and placements the daemon cannot map.

## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


##

`export_entries(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.export_entries)

Export a model's tensors, preserving tied-parameter aliases.

`named_parameters`

/`named_buffers`

are iterated with `remove_duplicate=False`

so tied weights (e.g. `lm_head.weight`

sharing storage with `embed_tokens.weight`

) are not silently dropped. Each unique tensor is exported once per call; every additional name that refers to the same tensor object is recorded in the returned alias map so the client can re-establish the shared identity instead of allocating uninitialized memory for it.

CUDA reduction arguments must be exported separately for each consumer so that PyTorch registers a reference for each IPC mapping's lifetime.

Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[TensorEntry](https://docs.vllm.ai/protocol/#vllm.model_executor.model_loader.weight_cache.protocol.TensorEntry)]A

`(entries, aliases)`

pair where`entries`

maps a canonical name to -

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]its

`TensorEntry`

and`aliases`

maps each duplicate name to its -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[TensorEntry](https://docs.vllm.ai/protocol/#vllm.model_executor.model_loader.weight_cache.protocol.TensorEntry)],[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]canonical name.


## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


##

`get_draft_daemon_config(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.get_draft_daemon_config)

VllmConfig for the draft daemon group

## Source code in `vllm/model_executor/model_loader/weight_cache/daemon.py`


##

`plan_local_ranks(parallel_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.daemon.plan_local_ranks)

`(local_rank, dp_rank, tp_rank)`

for every GPU this launcher serves.

Global ranks enumerate DP then TP: `global = dp_rank * tp_size + tp_rank`

. With `--nnodes`

the engine hands each node a contiguous block of global ranks, so node `r`

serves `node_rank * local + i`

; without it a launcher's block starts at `--data-parallel-start-rank * tp_size`

.