source: https://docs.vllm.ai/en/latest/api/vllm/distributed/mooncake_store/
lastmod: 2026-09-23

Configuration for MooncakeDistributedStore.

`mode`

selects the topology: `embedded`

(each rank contributes `global_segment_size`

in-process) or `standalone-store`

(rank contributes 0; an external `mooncake_client`

process owns the pool and the SSD tier).

## Source code in `vllm/distributed/mooncake_store.py`


| @dataclass
class MooncakeStoreConfig:
"""Configuration for MooncakeDistributedStore.
``mode`` selects the topology: ``embedded`` (each rank contributes
``global_segment_size`` in-process) or ``standalone-store`` (rank
contributes 0; an external ``mooncake_client`` process owns the pool
and the SSD tier).
"""
metadata_server: str
master_server_address: str
protocol: str
device_name: str
mode: MooncakeMode = "embedded"
global_segment_size: int = DEFAULT_GLOBAL_SEGMENT_SIZE
local_buffer_size: int = DEFAULT_LOCAL_BUFFER_SIZE
enable_offload: bool = False
tenant_id: str = DEFAULT_TENANT_ID
def __post_init__(self) -> None:
if self.mode not in ("embedded", "standalone-store"):
raise ValueError(f"unknown Mooncake mode: {self.mode!r}")
if self.local_buffer_size <= 0:
raise ValueError("local_buffer_size must be > 0")
if self.mode == "embedded" and self.global_segment_size == 0:
raise ValueError("embedded mode requires global_segment_size > 0")
if self.mode == "standalone-store" and self.global_segment_size != 0:
raise ValueError("standalone-store mode requires global_segment_size == 0")
@staticmethod
def from_file(file_path: str) -> "MooncakeStoreConfig":
with open(file_path) as file:
config = json.load(file)
return MooncakeStoreConfig(
metadata_server=config.get("metadata_server", ""),
master_server_address=config.get("master_server_address", ""),
protocol=config.get("protocol", "rdma"),
device_name=config.get("device_name", ""),
mode=config.get("mode", "embedded"),
global_segment_size=_parse_size(
config.get("global_segment_size", DEFAULT_GLOBAL_SEGMENT_SIZE)
),
local_buffer_size=_parse_size(
config.get("local_buffer_size", DEFAULT_LOCAL_BUFFER_SIZE)
),
enable_offload=bool(config.get("enable_offload", False)),
tenant_id=_normalize_tenant_id(config.get("tenant_id", DEFAULT_TENANT_ID)),
)
@staticmethod
def load_from_config() -> "MooncakeStoreConfig":
config_path = os.getenv("MOONCAKE_CONFIG_PATH")
if not config_path:
raise ValueError(
"The environment variable 'MOONCAKE_CONFIG_PATH' is not set."
)
return MooncakeStoreConfig.from_file(config_path)
|