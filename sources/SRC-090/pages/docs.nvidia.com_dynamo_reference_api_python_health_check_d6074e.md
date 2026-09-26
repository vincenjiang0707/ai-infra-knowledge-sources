source: https://docs.nvidia.com/dynamo/reference/api/python/health_check
lastmod: 2026-09-24T19:58:16.636Z

dynamo.health_check


dynamo.health_check

Health-check payload types and environment-driven configuration.

`dynamo.health_check`

publishes 1 classes and 1 functions. Source: `lib/bindings/python/src/dynamo/health_check.py`


###### HealthCheckPayload (class)


Base class for managing health check payloads.

Each backend should extend this class and set self.default_payload
in their **init** method.

Environment variable DYN_HEALTH_CHECK_PAYLOAD can override the default.

`lib/bindings/python/src/dynamo/health_check.py#L75`


**Public methods**

**init**

Initialize health check payload.

Subclasses should call super().**init**() after setting self.default_payload.

#### to_dict

Get the health check payload as a dictionary.

Returns the environment override if DYN_HEALTH_CHECK_PAYLOAD is set, otherwise returns the default payload.

###### load_health_check_from_env (function)


Load health check payload from environment variable.

Supports two formats:

- JSON string: export DYN_HEALTH_CHECK_PAYLOAD=’{“prompt”: “test”, “max_tokens”: 1}’
- File path: export DYN_HEALTH_CHECK_PAYLOAD=’@/path/to/health_check.json’

**Parameters**

Name of the environment variable to check (default: DYN_HEALTH_CHECK_PAYLOAD)

**Returns**

`Optional[Dict[str, Any]]`

— Dict containing the health check payload, or None if not set.