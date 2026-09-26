source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/sharded_rdt_common/
lastmod: 2026-09-24

#

`vllm.distributed.weight_transfer.sharded_rdt_common`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common)

Shared pieces of the sharded-RDT backend: the op-chain allowlist, buffer sizing and the minimum Ray version, plus `RdtRouter`

— consumer-only, since routing is a consumer decision.

The gather-group partition itself is `base.layerwise_groups`

: it defines what a group index means for any `WeightSource`

, not just this transport.

Classes:

-
–[RdtRouter](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter)Decides which producer serves each weight name, and — once bound — sends.


Functions:

-
–[assign_producer_indices](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.assign_producer_indices)Producers (global indices) that consumer

`consumer_idx`

binds. -
–[buffer_alloc_bytes](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.buffer_alloc_bytes)Size a NIXL buffer / ring slot for

`nbytes`

: the max of the request, an -
–[check_ray_rdt_version](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.check_ray_rdt_version)Refuse an installed Ray older than the one this backend is tested on.

-
–[register_nixl_memory](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.register_nixl_memory)Register a tensor with Ray using the platform's NIXL package.


##

`RdtRouter`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter)

Decides which producer serves each weight name, and — once bound — sends.

Ownership is per NAME. `owner_sets`

holds the few distinct producer sets that occur, and `name_owner_class[i]`

indexes it for `names[i]`

; a name determines both its owner set and its gather group, so neither appears in the routing API. Empty tables mean every producer holds everything.

Any placement is expressible this way: a pipeline stage is a set of names sharing one owner set, an expert is a name whose owner set is a single rank, and a group produced by two stages is just two classes inside one group.

Both engines derive the same tables from the same wire data, so they agree on who serves what. Disagreement is not a wrong answer but a hang or a loud misroute: a pull sent to a producer that never gathered the name trips its served-names guard.

Routing is consumer-only. The trainer publishes what it holds and answers whatever arrives; it never asks who serves what.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__)Build the routing tables from the wire data both engines receive.

-
–[bind](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.bind)Attach this consumer's producer handles. Rebuilt wholesale per init,

-
–[class_of](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.class_of)The name's owner class — the planner's bucketing key, since all names

-
–[free_group](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.free_group)Signal the group done at every producer holding any of its names.

-
–[group_owners](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.group_owners)Every producer holding any name of

`group_idx`

. -
–[owners](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.owners)Every producer holding

`name`

. -
–[producer_for](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.producer_for)The single producer

`consumer_id`

pulls`name`

from. -
–[pull](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.pull)Issue one packed pull to

`owner`

. -
–[reserve_serve_buffers](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.reserve_serve_buffers)Ask each producer to pre-register a serve ring sized to the most this

-
–[validate](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.validate)Check the ownership tables can be served.


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


|
|

###

`__init__(num_producers, num_consumers, owner_sets=None, name_owner_class=None, names=None, group_lens=None, workers_per_replica=0)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__)

Build the routing tables from the wire data both engines receive.

The four table arguments travel together and default together: with all of them empty the router degrades to "every producer holds everything".

Parameters:

-

(`num_producers`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(num_producers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Trainer ranks. Owner indices are positions in this range, and

`validate`

rejects any that fall outside it. -

(`num_consumers`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(num_consumers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Inference workers across the whole fleet. Fixes the id space; the block carve uses

`workers_per_replica`

of it. -

(`owner_sets`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(owner_sets))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]] | None`None`

) –The distinct producer sets that occur, one row per owner class; each row is deduplicated and sorted here. Empty means a single class owning every producer.

-

(`name_owner_class`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(name_owner_class))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Parallel to

`names`

—`name_owner_class[i]`

indexes`owner_sets`

for`names[i]`

. A name with no entry falls back to class 0. -

(`names`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(names))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Every parameter name, in group-major order: concatenating the gather groups reproduces this list exactly. The other two tables are keyed by this order.

-

(`group_lens`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(group_lens))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Length of each gather group, consecutive over

`names`

, so they sum to`len(names)`

. Fixes name -> group and the per-group owner union the free barrier fans out to. -

(`workers_per_replica`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.__init__(workers_per_replica))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Consumers per inference DEPLOYMENT. The block carve spreads this many consumers over an owner set and every deployment reuses that carve, so the same worker of each deployment resolves one producer (see

`producer_for`

). 0 means one deployment: carve over the whole fleet.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)`workers_per_replica`

does not divide`num_consumers`

, so the deployments are not uniform and two workers of one deployment would share a block index.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


|
|

###

`bind(actors, produce_methods, consumer_id)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.bind)

Attach this consumer's producer handles. Rebuilt wholesale per init, never appended to: every owner index is a position in these lists, so a rejoining engine that re-inits must not shift them.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


###

`class_of(name)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.class_of)

The name's owner class — the planner's bucketing key, since all names of a chunk must share one producer.

###

`free_group(group_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.free_group)

Signal the group done at every producer holding any of its names.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


###

`group_owners(group_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.group_owners)

Every producer holding any name of `group_idx`

.

The one group-keyed rule, because the free barrier is per group: a consumer signals `free_group(gi)`

at each of these and the producer counts signals against its live-consumer total. Names route; groups free.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


###

`owners(name)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.owners)

###

`producer_for(consumer_id, name)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.producer_for)

The single producer `consumer_id`

pulls `name`

from.

Blocks consumers across the name's owner set with the same rule that binds producers globally, then rotates by the name's GROUP index so a consumer spreads its groups over its block instead of hammering one NIC. Rotating per group (not per name) keeps every name of a chunk on one producer, which is what lets a chunk be a single pull.

The carve is over ONE DEPLOYMENT (this consumer's index within its own deployment, over `workers_per_replica`

of them), so the same worker of every deployment resolves the same producer for every name. Carving over the whole fleet instead spreads the multi-owner names of different deployments onto different producers while single-owner names still route by ownership, so a producer serves several distinct worker indices, each needing its own serve ring, and none of them can share a slot. With one deployment the width is the fleet, so this is the plain block rule.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


###

`pull(owner, keys, seq)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.pull)

Issue one packed pull to `owner`

.

The consumer id keys the producer's serve ring; without it every worker is served out of ring 0 and concurrent pulls overwrite each other's blob. `seq`

is this call's index in the stream to `owner`

(see `_Chunk`

): it selects the serve slot in ISSUE order, so a slot is never repacked while the read of its previous contents is still in flight.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


###

`reserve_serve_buffers(bytes_by_producer, plan_digests=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.reserve_serve_buffers)

Ask each producer to pre-register a serve ring sized to the most this consumer will pull from it.

`plan_digests[p]`

describes the chunks this consumer pulls from producer `p`

, in pull order. A producer that shares one serve ring across the consumers of several deployments compares it across them, so a fleet whose deployments are not identical fails at init instead of stalling mid-sync. A producer that shares nothing ignores it.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


###

`validate()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.RdtRouter.validate)

Check the ownership tables can be served.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)an owner set is empty or out of range, or a class index does not resolve.


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


##

`assign_producer_indices(num_producers, num_consumers, consumer_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.assign_producer_indices)

Producers (global indices) that consumer `consumer_idx`

binds.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


##

`buffer_alloc_bytes(nbytes, presize=0)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.buffer_alloc_bytes)

Size a NIXL buffer / ring slot for `nbytes`

: the max of the request, an optional `presize`

floor, and a coarse 256MB round-up, so the buffer is allocated ONCE and never regrows. Regrowth is a correctness hazard, not just a perf one -- see `buffer_presize_gb`

. Shared by the consumer's receive buffers and the producer's serve rings.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


##

`check_ray_rdt_version()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.check_ray_rdt_version)

Refuse an installed Ray older than the one this backend is tested on.

vLLM does not depend on Ray, so there is no pin to carry this. Without the check the failure is an opaque option-validation error out of `.options(enable_tensor_transport=True)`

(below 2.49) or an ImportError raised deep in the first pull, long after init reported success (below 2.55).

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)the installed Ray predates

`RDT_MIN_RAY_VERSION`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_common.py`


##

`register_nixl_memory(tensor)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_common.register_nixl_memory)

Register a tensor with Ray using the platform's NIXL package.