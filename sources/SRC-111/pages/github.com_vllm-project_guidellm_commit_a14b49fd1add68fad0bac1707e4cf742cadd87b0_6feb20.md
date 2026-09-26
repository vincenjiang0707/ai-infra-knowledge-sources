source: https://github.com/vllm-project/guidellm/commit/a14b49fd1add68fad0bac1707e4cf742cadd87b0

File tree Expand file tree Collapse file tree

Expand file tree Collapse file tree Original file line number Diff line number Diff line change `41`

`41`

__all__ = ["Benchmarker" ]


`42`

`42`



`43`

`43`



`44`


- class BenchmarkerMeta (ABCMeta , SingletonMeta ): ...



`44`

+ class BenchmarkerMeta (ABCMeta , SingletonMeta ):



`45`

+ """Exists to resolves metaclass conflicts in `Benchmarker`."""


`45`

`46`



`46`

`47`



`47`

`48`

class Benchmarker (



Original file line number Diff line number Diff line change `1`


- """


`2`


- Registry system for dynamic object registration and discovery.


`3`


-


`4`


- Provides a flexible object registration system with optional auto-discovery


`5`


- capabilities through decorators and module imports. Enables dynamic discovery


`6`


- and instantiation of implementations based on configuration parameters, supporting


`7`


- both manual registration and automatic package-based discovery for extensible


`8`


- plugin architectures.


`9`


- """


`10`


-


`11`

`1`

from __future__ import annotations


`12`

`2`



`13`

`3`

from typing import TypeVar



You can’t perform that action at this time.


## 0 commit comments