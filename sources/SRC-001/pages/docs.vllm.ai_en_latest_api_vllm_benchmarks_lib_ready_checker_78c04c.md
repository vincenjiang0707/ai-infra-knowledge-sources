source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/lib/ready_checker/
lastmod: 2026-09-23

Wait for an endpoint to become available before starting benchmarks.

Parameters:

-
### `request_func`


(`RequestFunc`

) – The async request function to call

- (
[RequestFuncInput](../endpoint_request_func/#vllm.benchmarks.lib.endpoint_request_func.RequestFuncInput)

) – The RequestFuncInput to test with

-
### `session`


([ClientSession](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession)

) – The aiohttp session used to issue the probe requests

-
### `timeout_seconds`


([int](https://docs.python.org/3/builtins/functions.html#int)

, default: `600`

) – Maximum time to wait in seconds (default: 10 minutes)

-
### `retry_interval`


([int](https://docs.python.org/3/builtins/functions.html#int)

, default: `5`

) – Time between retries in seconds (default: 5 seconds)


Returns:

Raises:

-
[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)

– If the endpoint doesn't become available within the timeout


## Source code in `vllm/benchmarks/lib/ready_checker.py`


| async def wait_for_endpoint(
request_func: RequestFunc,
test_input: RequestFuncInput,
session: aiohttp.ClientSession,
timeout_seconds: int = 600,
retry_interval: int = 5,
) -> RequestFuncOutput:
"""Wait for an endpoint to become available before starting benchmarks.
Args:
request_func: The async request function to call
test_input: The RequestFuncInput to test with
session: The aiohttp session used to issue the probe requests
timeout_seconds: Maximum time to wait in seconds (default: 10 minutes)
retry_interval: Time between retries in seconds (default: 5 seconds)
Returns:
RequestFuncOutput: The successful response
Raises:
ValueError: If the endpoint doesn't become available within the timeout
"""
deadline = time.perf_counter() + timeout_seconds
output = RequestFuncOutput(success=False)
print(f"Waiting for endpoint to become up in {timeout_seconds} seconds")
with tqdm(
total=timeout_seconds,
bar_format="{desc} |{bar}| {elapsed} elapsed, {remaining} remaining",
unit="s",
) as pbar:
while True:
# update progress bar
remaining = deadline - time.perf_counter()
elapsed = timeout_seconds - remaining
update_amount = min(elapsed - pbar.n, timeout_seconds - pbar.n)
pbar.update(update_amount)
pbar.refresh()
if remaining <= 0:
pbar.close()
break
# ping the endpoint using request_func
try:
output = await request_func(
request_func_input=test_input, session=session
)
if output.success:
pbar.close()
return output
else:
err_last_line = str(output.error).rstrip().rsplit("\n", 1)[-1]
logger.warning("Endpoint is not ready. Error='%s'", err_last_line)
except aiohttp.ClientConnectorError:
pass
# retry after a delay
sleep_duration = min(retry_interval, remaining)
if sleep_duration > 0:
await asyncio.sleep(sleep_duration)
return output
|