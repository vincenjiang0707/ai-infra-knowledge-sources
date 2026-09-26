source: https://github.com/vllm-project/guidellm/commit/61fb74fcb372a701755ba6791bc309df3c7e6e2d

|
`7` | `7` | from __future__ import annotations
|
`8` | `8` |
|
`9` | `9` | import pytest
|
| `10` | `+`from datasets import Dataset |
`10` | `11` |
|
`11` | `12` | from guidellm.data.loaders.loader import DataLoaderRegistry
|
`12` | `13` | from guidellm.data.loaders.torch import TorchDataLoader
|
`13` | `14` | from guidellm.schemas.data import TorchDataLoaderArgs
|
`14` | `15` |
|
`15` | `16` |
|
| `17` | `+`@pytest.mark.regression |
| `18` | `+`@pytest.mark.parametrize("num_workers", [0, 1, 2]) |
| `19` | `+`@pytest.mark.parametrize("samples", [-1, 0, 1]) |
| `20` | `+`def test_loader_allows_workers_without_assigned_rows(num_workers, samples): |
| `21` | `+` """A small dataset must load even when some workers receive no rows. |
| `22` | `+`
|
| `23` | `+` ## WRITTEN BY AI ## |
| `24` | `+` """ |
| `25` | `+` loader = TorchDataLoader( |
| `26` | `+` config=TorchDataLoaderArgs(samples=samples, num_workers=num_workers), |
| `27` | `+` datasets=[Dataset.from_dict({"text": ["hello"]})], |
| `28` | `+` preprocessors=[], |
| `29` | `+` finalizer=list, |
| `30` | `+` ) |
| `31` | `+` |
| `32` | `+` assert list(loader) == [[{"dataset": {"text": "hello"}}]] |
| `33` | `+` |
| `34` | `+` |
| `35` | `+`@pytest.mark.regression |
| `36` | `+`def test_loader_rejects_rows_with_only_empty_results(): |
| `37` | `+` """Rows assigned to a worker must still produce usable results. |
| `38` | `+`
|
| `39` | `+` ## WRITTEN BY AI ## |
| `40` | `+` """ |
| `41` | `+` loader = TorchDataLoader( |
| `42` | `+` config=TorchDataLoaderArgs(samples=0, num_workers=0), |
| `43` | `+` datasets=[Dataset.from_dict({"text": ["hello"]})], |
| `44` | `+` preprocessors=[], |
| `45` | `+` finalizer=lambda _: [], |
| `46` | `+` ) |
| `47` | `+` |
| `48` | `+` with pytest.raises(ValueError, match="processed 1 rows but yielded zero results"): |
| `49` | `+` list(loader) |
| `50` | `+` |
| `51` | `+` |
`16` | `52` | class TestTorchDataLoaderArgs:
|
`17` | `53` | """Tests for TorchDataLoaderArgs schema.
|
`18` | `54` |
|
|
## 0 commit comments