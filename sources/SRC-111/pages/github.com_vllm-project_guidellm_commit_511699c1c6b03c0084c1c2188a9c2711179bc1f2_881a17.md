source: https://github.com/vllm-project/guidellm/commit/511699c1c6b03c0084c1c2188a9c2711179bc1f2

|
`5` | `5` |
|
`6` | `6` | from pydantic import Field
|
`7` | `7` |
|
`8` |
| `-`from guidellm.schemas import _PydanticClassRegistryMixin, standard_model_config |
| `8` | `+`from guidellm.schemas import PydanticClassRegistryMixin, standard_model_config |
`9` | `9` |
|
`10` | `10` | __all__ = [
|
`11` | `11` | "DataArgs",
|
|
`17` | `17` |
|
`18` | `18` |
|
`19` | `19` | class DataLoaderArgs(
|
`20` |
| `-` _PydanticClassRegistryMixin["DataLoaderArgs"], |
| `20` | `+` PydanticClassRegistryMixin["DataLoaderArgs"], |
`21` | `21` | ABC,
|
`22` | `22` | ):
|
`23` | `23` | """
|
@@ -60,7 +60,7 @@ def __pydantic_schema_base_type__(cls) -> type[DataLoaderArgs]:
|
`60` | `60` |
|
`61` | `61` |
|
`62` | `62` | class DataArgs(
|
`63` |
| `-` _PydanticClassRegistryMixin["DataArgs"], |
| `63` | `+` PydanticClassRegistryMixin["DataArgs"], |
`64` | `64` | ABC,
|
`65` | `65` | ):
|
`66` | `66` | """Base class for data loading and processing argument models.
|
@@ -104,7 +104,7 @@ def __pydantic_schema_base_type__(cls) -> type[DataArgs]:
|
`104` | `104` |
|
`105` | `105` |
|
`106` | `106` | class DataPreprocessorArgs(
|
`107` |
| `-` _PydanticClassRegistryMixin["DataPreprocessorArgs"], |
| `107` | `+` PydanticClassRegistryMixin["DataPreprocessorArgs"], |
`108` | `108` | ABC,
|
`109` | `109` | ):
|
`110` | `110` | """
|
@@ -141,7 +141,7 @@ def __pydantic_schema_base_type__(cls) -> type[DataPreprocessorArgs]:
|
`141` | `141` |
|
`142` | `142` |
|
`143` | `143` | class DataFinalizerArgs(
|
`144` |
| `-` _PydanticClassRegistryMixin["DataFinalizerArgs"], |
| `144` | `+` PydanticClassRegistryMixin["DataFinalizerArgs"], |
`145` | `145` | ABC,
|
`146` | `146` | ):
|
`147` | `147` | """
|
@@ -178,7 +178,7 @@ def __pydantic_schema_base_type__(cls) -> type[DataFinalizerArgs]:
|
`178` | `178` |
|
`179` | `179` |
|
`180` | `180` | class DataTokenizerArgs(
|
`181` |
| `-` _PydanticClassRegistryMixin["DataTokenizerArgs"], |
| `181` | `+` PydanticClassRegistryMixin["DataTokenizerArgs"], |
`182` | `182` | ABC,
|
`183` | `183` | ):
|
`184` | `184` | """
|
|
## 0 commit comments