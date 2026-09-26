source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/inc/schemes/inc_ark_ops/
lastmod: 2026-09-24

Return ARK availability, error details, cached module, and QuantLinear.

## Source code in `vllm/model_executor/layers/quantization/inc/schemes/inc_ark_ops.py`


| @lru_cache(maxsize=1)
def get_ark_state() -> tuple[bool, str | None, Any | None, Any | None]:
"""Return ARK availability, error details, cached module, and QuantLinear."""
try:
import auto_round_kernel as ark
from auto_round_kernel.qlinear import QuantLinear
logger.info("Successfully imported auto_round_kernel.")
except ImportError as error:
return False, str(error), None, None
if getattr(ark, "cpu_lib", None) is None and getattr(ark, "xpu_lib", None) is None:
return (
False,
"No ARK backend library is available.",
None,
None,
)
logger.info("Successfully loaded auto_round_kernel backend library.")
return True, None, ark, QuantLinear
|