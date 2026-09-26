source: https://github.com/vllm-project/guidellm/commit/f848ceb2a4abb68c61e1a5a36921514f4acf80eb

File tree Expand file tree Collapse file tree

Expand file tree Collapse file tree Original file line number Diff line number Diff line change `15`

`15`

import asyncio


`16`

`16`

import time


`17`

`17`

from collections .abc import AsyncIterator



`18`

+ from dataclasses import dataclass


`18`

`19`

from typing import Any , Literal


`19`

`20`



`20`

`21`

from pydantic import Field , SecretStr


@@ -93,9 +94,10 @@ class LiteLLMBackend(Backend):


`93`

`94`

await backend.process_shutdown()


`94`

`95`

"""


`95`

`96`




`97`

+ _args : LiteLLMBackendArgs



`98`

+


`96`

`99`

def __init__ (self , args : LiteLLMBackendArgs ):


`97`

`100`

super ().__init__ (args )


`98`


- self ._args = args


`99`

`101`

self ._in_process = False


`100`

`102`



`101`

`103`

async def process_startup (self ):


@@ -302,23 +304,9 @@ def _build_response(


`302`

`304`

)


`303`

`305`



`304`

`306`




`307`

+ @dataclass (frozen = True , kw_only = True , slots = True )


`305`

`308`

class _ChunkResult :


`306`


- __slots__ = (


`307`


- "first_token" ,


`308`


- "input_tokens" ,


`309`


- "output_tokens" ,


`310`


- "response_id" ,


`311`


- )


`312`


-


`313`


- def __init__ (


`314`


- self ,


`315`


- * ,


`316`


- response_id : str | None ,


`317`


- input_tokens : int | None ,


`318`


- output_tokens : int | None ,


`319`


- first_token : bool ,


`320`


- ):


`321`


- self .response_id = response_id


`322`


- self .input_tokens = input_tokens


`323`


- self .output_tokens = output_tokens


`324`


- self .first_token = first_token



`309`

+ response_id : str | None



`310`

+ input_tokens : int | None



`311`

+ output_tokens : int | None



`312`

+ first_token : bool



Original file line number Diff line number Diff line change `1`


- from litellm import acompletion as acompletion


`2`


- from litellm import completion as completion



`1`

+ from litellm import acompletion , completion



`2`

+



`3`

+ __all__ = ["acompletion" , "completion" ]



You can’t perform that action at this time.


## 0 commit comments