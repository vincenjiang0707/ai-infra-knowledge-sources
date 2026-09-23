source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/dp_supervisor/
lastmod: 2026-09-23

class DPSupervisor:
def __init__(self, args: argparse.Namespace):
validate_multi_port_external_lb_args(args)
self.args = args
self.supervisor_port = args.data_parallel_supervisor_port
self.child_ports = [
args.port + local_rank
for local_rank in range(args.data_parallel_size_local)
]
self._is_ready = False
self._processes: list[BaseProcess] = []
self._shutdown_event = asyncio.Event()
self._shutdown_signal = signal.SIGTERM
@property
def is_ready(self) -> bool:
return self._is_ready and not self._shutdown_event.is_set()
async def run(self) -> None:
loop = asyncio.get_running_loop()
decorate_logs("DPSupervisor")
# K8s sends SIGTERM for shutdown - begin graceful termination.
for sig in (signal.SIGTERM, signal.SIGINT):
loop.add_signal_handler(sig, partial(self._handle_signal, sig))
supervisor_server: uvicorn.Server | None = None
supervisor_server_task: asyncio.Task[None] | None = None
try:
# Launch vLLM DP Servers and begin monitoring them.
self._start_children()
monitor_task = asyncio.create_task(
self._monitor_children(), name="dp-monitor"
)
# Only start the DPSupervisor server once the vLLM DP Servers are
# ready. This avoids the supervisor /health endpoint returning 503
# to external load balancer probes while the engines initialize.
await self._wait_until_ready(monitor_task)
if self.is_ready and not monitor_task.done():
supervisor_server, supervisor_server_task = await self._start_server()
await monitor_task
finally:
self._is_ready = False
await self._shutdown_children()
# Shutdown the DP Supervisor server.
if supervisor_server is not None and supervisor_server_task is not None:
supervisor_server.should_exit = True
await supervisor_server_task
async def _start_server(self) -> tuple[uvicorn.Server, asyncio.Task[None]]:
"""Launch the DPSupervisor HTTP server.
Called only after the vLLM DP Servers are ready so that /health does
not return 503 to external probes while the engines are initializing.
"""
app = _build_dp_supervisor_app(self)
host = self.args.host or "0.0.0.0"
uvicorn_kwargs: dict = {}
log_config = get_uvicorn_log_config(self.args)
if log_config is not None:
uvicorn_kwargs["log_config"] = log_config
config = uvicorn.Config(
app,
host=host,
port=self.supervisor_port,
log_level=self.args.uvicorn_log_level,
access_log=not self.args.disable_uvicorn_access_log,
ssl_keyfile=self.args.ssl_keyfile,
ssl_certfile=self.args.ssl_certfile,
ssl_ca_certs=self.args.ssl_ca_certs,
ssl_cert_reqs=self.args.ssl_cert_reqs,
ssl_ciphers=self.args.ssl_ciphers,
**uvicorn_kwargs,
)
supervisor_server = NoSignalServer(config)
supervisor_server_task = asyncio.create_task(
supervisor_server.serve(),
name="dp-supervisor",
)
supervisor_server_task.add_done_callback(
lambda _task: self._shutdown_event.set()
)
# Ensure DPSupervisor task starts on the event loop.
while not supervisor_server.started:
if supervisor_server_task.done():
supervisor_server_task.result()
raise RuntimeError("DPSupervisor exited before startup.")
await asyncio.sleep(0.05)
logger.info("Started DPSupervisor on %s:%d", host, self.supervisor_port)
return supervisor_server, supervisor_server_task
async def _wait_until_ready(self, monitor_task: asyncio.Task[None]) -> None:
"""Block until the vLLM DP Servers are ready or shutdown is triggered.
Returns early if monitoring stops (e.g. a DP Server dies during
startup), in which case the supervisor server is never started.
"""
logger.info("Waiting for vLLM DP Servers to become ready.")
while not self._is_ready and not self._shutdown_event.is_set():
if monitor_task.done():
return
await asyncio.sleep(0.05)
def _handle_signal(self, signum: int) -> None:
"""Signal handler that is added to the event loop.
This catches the SIGTERM from K8s and begins graceful shutdown,
by setting the _shutdown_event(), which is watched by the main
coroutine monitoring the vLLM DP Servers.
"""
if self._shutdown_event.is_set():
return
self._shutdown_signal = signal.Signals(signum)
logger.info(
"DPSupervisor received %s, shutting down.",
self._shutdown_signal.name,
)
self._shutdown_event.set()
self._is_ready = False
def _start_children(self) -> None:
"""Launch vLLM DP Servers on separate GPUs."""
logger.info("Launching vLLM DP Servers")
context = multiprocessing.get_context("spawn")
for local_rank in range(self.args.data_parallel_size_local):
child_args = _build_vllm_dp_server_args(self.args, local_rank)
process = context.Process(
target=_run_vllm_dp_server,
name=f"APIServer_DPRank_{child_args.data_parallel_rank}",
args=(child_args,),
)
process.start()
self._processes.append(process)
async def _probe_all_children(self) -> None:
"""Background coroutine: probes all child endpoints on each interval.
Exits when any server becomes unhealthy after being ready, signalling
_monitor_children to initiate shutdown.
"""
timeout = aiohttp.ClientTimeout(total=self.args.dp_supervisor_probe_timeout_s)
async with aiohttp.ClientSession(timeout=timeout) as session:
while not self._shutdown_event.is_set():
threshold = (
self.args.dp_supervisor_probe_failure_threshold
if self._is_ready
else 1
)
results = await asyncio.gather(
*(
_probe_endpoint(
session,
self.args,
port,
"/health",
conn_err_failure_threshold=threshold,
conn_err_retry_delay=self.args.dp_supervisor_probe_interval_s,
)
for port in self.child_ports
),
return_exceptions=True,
)
all_healthy = all(r is True for r in results)
if all_healthy:
# If all healthy, we are ready to receive requests.
# This conditional avoids a potential race condition
# where shutdown is set, THEN the probe returns true.
if not self._shutdown_event.is_set():
self._is_ready = True
elif self._is_ready:
# Once ready, any failure in the probe means vLLM is dead.
num_unhealthy = sum(1 for r in results if r is not True)
logger.info(
"DPSupervisor probe found %s unhealthy DP Servers.",
num_unhealthy,
)
self._is_ready = False
self._shutdown_event.set()
return
with contextlib.suppress(asyncio.TimeoutError):
logger.debug(
"Waiting for %s seconds before next probe",
self.args.dp_supervisor_probe_interval_s,
)
await asyncio.wait_for(
self._shutdown_event.wait(),
timeout=self.args.dp_supervisor_probe_interval_s,
)
async def _monitor_children(self) -> None:
"""Main coroutine task that monitors the children vLLM servers.
Before the vLLM servers are /ready:
- if the pid is dead, we will shut down
- if the probe fails, we try again after dp_supervisor_probe_interval_s
After the vLLM servers are /ready:
- if the pid is dead, we will shut down
- if the probe fails, we will shut down
"""
probe_task = asyncio.create_task(
self._probe_all_children(), name="dp-health-probe"
)
try:
while not self._shutdown_event.is_set():
# 1. Check for dead processes
n_failed = len([p for p in self._processes if not p.is_alive()])
if n_failed > 0:
logger.info("DPSupervisor found %s exited DP Servers.", n_failed)
break
# 2. Check if the probe background task crashed or failed.
if probe_task.done():
# Extract exception if it crashed, or log failure
exc = probe_task.exception() if not probe_task.cancelled() else None
logger.info("DPSupervisor probe task stopped. Exception: %s", exc)
break
# Sleep for probe_interval seconds or until a shutdown.
with contextlib.suppress(asyncio.TimeoutError):
logger.debug(
"Waiting for %s seconds before next monitor",
self.args.dp_supervisor_probe_interval_s,
)
await asyncio.wait_for(
self._shutdown_event.wait(),
timeout=self.args.dp_supervisor_probe_interval_s,
)
finally:
# Cleanup probe task if needed.
if not probe_task.done():
probe_task.cancel()
with contextlib.suppress(asyncio.CancelledError):
await probe_task
async def _shutdown_children(self) -> None:
"""Terminate the vLLM DP servers."""
process_timeout = get_engine_process_shutdown_timeout(
self.args.shutdown_timeout, self.args.shutdown_timeout
)
assert process_timeout is not None
timeout = process_timeout + CHILD_EXIT_GRACE_S
try:
logger.info(
"DPSupervisor forwarding %s to DP Servers.",
self._shutdown_signal.name,
)
for process in self._processes:
pid = process.pid
if not process.is_alive() or pid is None:
continue
with contextlib.suppress(ProcessLookupError, OSError):
os.kill(pid, self._shutdown_signal)
try:
await asyncio.to_thread(
_join_processes_with_timeout, self._processes, timeout
)
except asyncio.CancelledError:
logger.warning("Shutdown await cancelled")
raise
finally:
for process in self._processes:
pid = process.pid
if not process.is_alive() or pid is None:
continue
logger.warning(
"DP server %s did not exit within %.1fs; force killing.",
process.name,
timeout,
)
with contextlib.suppress(
ProcessLookupError,
OSError,
psutil.NoSuchProcess,
psutil.AccessDenied,
):
kill_process_tree(pid)