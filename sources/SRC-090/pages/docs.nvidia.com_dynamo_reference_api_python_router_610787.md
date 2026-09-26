source: https://docs.nvidia.com/dynamo/reference/api/python/router
lastmod: 2026-09-24T19:58:16.636Z

# dynamo.router

Request-router configuration and command-line argument groups.

`dynamo.router`

publishes 2 classes and 3 functions. Source: `components/src/dynamo/router/__init__.py`


###### DynamoRouterArgGroup (class)


CLI argument group for standalone router options.

`components/src/dynamo/router/args.py#L71`


**Public methods**

#### add_arguments

Add router-owned arguments to parser.

###### DynamoRouterConfig (class)


Typed configuration for the standalone KV router (router-owned options only).

`components/src/dynamo/router/args.py#L22`


**Public methods**

#### validate

Validate config invariants (aligned with Rust KvRouterConfig where applicable).

###### build_aic_perf_config (function)


###### build_kv_router_config (function)


###### parse_args (function)


Parse command-line arguments for the standalone router.

**Returns**

`DynamoRouterConfig`

— Parsed and validated configuration.