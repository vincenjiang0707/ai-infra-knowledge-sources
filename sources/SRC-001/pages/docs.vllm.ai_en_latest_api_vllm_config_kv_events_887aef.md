source: https://docs.vllm.ai/en/latest/api/vllm/config/kv_events/
lastmod: 2026-09-24

#

`vllm.config.kv_events`

[¶](https://docs.vllm.ai#vllm.config.kv_events)

Classes:

-
–[KVEventsConfig](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig)Configuration for KV event publishing.


##

`KVEventsConfig`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig)

Configuration for KV event publishing.

Attributes:

-
([buffer_steps](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.buffer_steps)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of steps to cache for replay endpoint. Will only save

-
([enable_kv_cache_events](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.enable_kv_cache_events)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, enable KV cache events for tracking block storage and removal.

-
([endpoint](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.endpoint)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The zmq endpoint to use for publishing kv events.

-
([hwm](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.hwm)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The zmq high water mark for the event publisher. After queueing N events,

-
([max_queue_size](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.max_queue_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The maximum number of events to queue while waiting for publishing.

-
([publisher](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.publisher)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['null', 'zmq']The publisher to use for publishing kv events. Can be "null", "zmq".

-
([replay_endpoint](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.replay_endpoint)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe zmq endpoint to use for replaying kv events.

-
([topic](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.topic)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The topic to use for the event publisher. Consumers can subscribe to


## Source code in `vllm/config/kv_events.py`


###

`buffer_steps = 10000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.buffer_steps)

The number of steps to cache for replay endpoint. Will only save events from the last N steps for the replay endpoint.

###

`enable_kv_cache_events = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.enable_kv_cache_events)

If True, enable KV cache events for tracking block storage and removal. Events can be published externally by zmq using the event publisher config.

###

`endpoint = 'tcp://*:5557'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.endpoint)

The zmq endpoint to use for publishing kv events.

###

`hwm = 100000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.hwm)

The zmq high water mark for the event publisher. After queueing N events, events will start dropping if the consumer is not keeping up.

###

`max_queue_size = 100000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.max_queue_size)

The maximum number of events to queue while waiting for publishing.

###

`publisher = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.publisher)

The publisher to use for publishing kv events. Can be "null", "zmq".

###

`replay_endpoint = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.replay_endpoint)

The zmq endpoint to use for replaying kv events.

###

`topic = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kv_events.KVEventsConfig.topic)

The topic to use for the event publisher. Consumers can subscribe to this topic to receive events.