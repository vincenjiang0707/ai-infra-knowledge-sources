source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/startup/
lastmod: 2026-09-24

Benchmark the cold and warm startup time of vLLM models.

This script measures total startup time (including model loading, compilation, and cache operations) for both cold and warm scenarios: - Cold startup: Fresh start with no caches (temporary cache directories) - Warm startup: Using cached compilation and model info

Classes:

-
[MetricDesc](#vllm.benchmarks.startup.MetricDesc)

– Descriptor for a metric to collect from each iteration.

-
[MetricStats](#vllm.benchmarks.startup.MetricStats)

– Aggregated statistics for a single benchmark metric.


Functions:

##

`MetricDesc`


Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)


Descriptor for a metric to collect from each iteration.

## Source code in `vllm/benchmarks/startup.py`


| class MetricDesc(NamedTuple):
"""Descriptor for a metric to collect from each iteration."""
iter_key: str # key in the iteration result dict
suffix: str # result key suffix, e.g. "startup", "compilation"
display_name: str
|


##

`MetricStats`


Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)


Aggregated statistics for a single benchmark metric.

## Source code in `vllm/benchmarks/startup.py`


| class MetricStats(NamedTuple):
"""Aggregated statistics for a single benchmark metric."""
key: str # e.g. "cold_startup", "warm_encoder_compilation"
display_name: str
values: list[float]
avg: float
percentiles: dict[int, float]
|


##

`cold_startup()`


Context manager to measure cold startup time: 1. Uses a temporary directory for vLLM cache to avoid any pollution between cold startup iterations. 2. Uses inductor's fresh_cache to clear torch.compile caches.

## Source code in `vllm/benchmarks/startup.py`


| @contextmanager
def cold_startup():
"""Context manager to measure cold startup time:
1. Uses a temporary directory for vLLM cache to avoid any pollution
between cold startup iterations.
2. Uses inductor's fresh_cache to clear torch.compile caches.
"""
from torch._inductor.utils import fresh_cache
# Use temporary directory for caching to avoid any pollution between cold startups
original_cache_root = os.environ.get("VLLM_CACHE_ROOT")
temp_cache_dir = tempfile.mkdtemp(prefix="vllm_startup_bench_cold_")
try:
os.environ["VLLM_CACHE_ROOT"] = temp_cache_dir
with fresh_cache():
yield
finally:
# Clean up temporary cache directory
shutil.rmtree(temp_cache_dir, ignore_errors=True)
if original_cache_root:
os.environ["VLLM_CACHE_ROOT"] = original_cache_root
else:
os.environ.pop("VLLM_CACHE_ROOT", None)
|

##

`run_startup_in_subprocess(engine_args, result_queue)`


Run LLM startup in a subprocess and return timing metrics via a queue. This ensures complete isolation between iterations.

## Source code in `vllm/benchmarks/startup.py`


| def run_startup_in_subprocess(engine_args, result_queue):
"""Run LLM startup in a subprocess and return timing metrics via a queue.
This ensures complete isolation between iterations.
"""
try:
# Import inside the subprocess to avoid issues with forking
from vllm import LLM
# Measure total startup time
start_time = time.perf_counter()
llm = LLM.from_engine_args(engine_args)
total_startup_time = time.perf_counter() - start_time
# Extract compilation time if available
compilation_time = 0.0
encoder_compilation_time = 0.0
if hasattr(llm.llm_engine, "vllm_config"):
vllm_config = llm.llm_engine.vllm_config
if (
hasattr(vllm_config, "compilation_config")
and vllm_config.compilation_config is not None
):
compilation_time = vllm_config.compilation_config.compilation_time
encoder_compilation_time = (
vllm_config.compilation_config.encoder_compilation_time
)
result_queue.put(
{
"total_startup_time": total_startup_time,
"compilation_time": compilation_time,
"encoder_compilation_time": encoder_compilation_time,
}
)
except Exception as e:
result_queue.put(None)
result_queue.put(str(e))
|