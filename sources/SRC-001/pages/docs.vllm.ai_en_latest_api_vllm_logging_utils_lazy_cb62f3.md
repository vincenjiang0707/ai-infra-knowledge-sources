source: https://docs.vllm.ai/en/latest/api/vllm/logging_utils/lazy/
lastmod: 2026-09-24

Wrap a zero-argument callable evaluated only during log formatting.

## Source code in `vllm/logging_utils/lazy.py`


| class lazy:
"""Wrap a zero-argument callable evaluated only during log formatting."""
__slots__ = ("_factory",)
def __init__(self, factory: Callable[[], Any]) -> None:
self._factory = factory
def __str__(self) -> str:
return str(self._factory())
def __repr__(self) -> str:
return str(self)
|