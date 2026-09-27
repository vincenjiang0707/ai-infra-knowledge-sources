source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/utils/server_utils/
lastmod: 2026-09-27

Get the uvicorn log config based on the provided arguments.

Priority: 1. If log_config_file is specified, use it 2. If disable_access_log_for_endpoints is specified, create a config with the access log filter 3. Otherwise, return None (use uvicorn defaults)

## Source code in `vllm/entrypoints/launchers/utils/server_utils.py`


| def get_uvicorn_log_config(args: Namespace) -> dict | None:
"""Get the uvicorn log config based on the provided arguments.
Priority:
1. If log_config_file is specified, use it
2. If disable_access_log_for_endpoints is specified, create a config with
the access log filter
3. Otherwise, return None (use uvicorn defaults)
"""
# First, try to load from file if specified
logging_config = getattr(args, "logging_config", None)
log_config_file = (
logging_config.pylogging_config_file
if logging_config is not None
else getattr(args, "log_config_file", None)
)
log_config = load_log_config(log_config_file)
if log_config is not None:
return log_config
# If endpoints to filter are specified, create a config with the filter
if args.disable_access_log_for_endpoints:
from vllm.logging_utils import create_uvicorn_log_config
# Parse comma-separated string into list
excluded_paths = [
p.strip()
for p in args.disable_access_log_for_endpoints.split(",")
if p.strip()
]
return create_uvicorn_log_config(
excluded_paths=excluded_paths,
log_level=args.uvicorn_log_level,
)
return None
|