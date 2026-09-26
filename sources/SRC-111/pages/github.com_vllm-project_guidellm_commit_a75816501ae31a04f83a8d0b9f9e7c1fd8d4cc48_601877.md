source: https://github.com/vllm-project/guidellm/commit/a75816501ae31a04f83a8d0b9f9e7c1fd8d4cc48

`10`

`10`



`11`

`11`

from __future__ import annotations


`12`

`12`




`13`

+ import contextlib


`13`

`14`

from typing import Any , Generic , TypeVar


`14`

`15`



`15`

`16`

from disdantic import PydanticClassRegistryMixin



`17`

+ from disdantic .exceptions import AutoPopulationError


`16`

`18`

from pydantic import BaseModel , ConfigDict , Field


`17`

`19`



`18`

`20`

__all__ = [


@@ -144,7 +146,7 @@ class StatusBreakdown(BaseModel, Generic[SuccessfulT, ErroredT, IncompleteT, Tot


`144`

`146`

)


`145`

`147`



`146`

`148`



`147`


- class _PydanticClassRegistryMixin (PydanticClassRegistryMixin ):



`149`

+ class _PydanticClassRegistryMixin (PydanticClassRegistryMixin [ BaseModelT ] ):


`148`

`150`

def __new__ (cls , * args , ** kwargs ): # noqa: ARG004


`149`

`151`

"""


`150`

`152`

Prevent direct instantiation of base classes that use this mixin.


@@ -155,3 +157,19 @@ def __new__(cls, *args, **kwargs): # noqa: ARG004


`155`

`157`

if cls is base_type :


`156`

`158`

raise TypeError (f"only children of '{ cls .__name__ } ' may be instantiated" )


`157`

`159`

return super ().__new__ (cls )



`160`

+



`161`

+ @classmethod



`162`

+ def registered_names (cls ) -> tuple [str , ...]:



`163`

+ """



`164`

+ Get all registered names from the registry.



`165`

+



`166`

+ Automatically triggers auto-discovery if it is enabled



`167`

+ to ensure all available implementations are included.



`168`

+



`169`

+ :return: Tuple of all registered names including auto-discovered ones



`170`

+ """



`171`

+ with cls ._registry_lock :



`172`

+ if cls .is_auto_discovery_enabled ():



`173`

+ with contextlib .suppress (AutoPopulationError ):



`174`

+ cls .auto_populate_registry ()



`175`

+ return tuple (cls .registry .keys ())


## 0 commit comments