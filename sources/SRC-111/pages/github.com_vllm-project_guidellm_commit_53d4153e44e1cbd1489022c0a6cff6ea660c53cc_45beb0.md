source: https://github.com/vllm-project/guidellm/commit/53d4153e44e1cbd1489022c0a6cff6ea660c53cc

`5`

`5`

import json


`6`

`6`

import math


`7`

`7`

import multiprocessing



`8`

+ from collections .abc import AsyncGenerator



`9`

+ from contextlib import asynccontextmanager


`8`

`10`



`9`

`11`

import httpx


`10`

`12`

import pytest


@@ -23,56 +25,57 @@ def _start_server_process(config: MockServerConfig):


`23`

`25`

server .run (access_log = False )


`24`

`26`



`25`

`27`



`26`


- @pytest_asyncio .fixture (scope = "class" )


`27`


- async def mock_server_instance ():


`28`


- """Instance-level fixture that provides a running server for HTTP testing."""


`29`


-


`30`


- config = MockServerConfig (


`31`


- host = "127.0.0.1" ,


`32`


- port = 8012 ,


`33`


- model = "test-model" ,


`34`


- ttft_ms = 10.0 ,


`35`


- itl_ms = 1.0 ,


`36`


- request_latency = 0.1 ,


`37`


- )



`28`

+ @asynccontextmanager



`29`

+ async def _run_mock_server (



`30`

+ config : MockServerConfig ,



`31`

+ ) -> AsyncGenerator [str , None ]:


`38`

`32`

base_url = f"http://{ config .host } :{ config .port } "


`39`

`33`

server_process = multiprocessing .Process (


`40`

`34`

target = _start_server_process , args = (config ,)


`41`

`35`

)


`42`

`36`

server_process .start ()


`43`

`37`



`44`


- # Wait for server to start up and be ready


`45`


- async def wait_for_startup ():



`38`

+ async def wait_for_startup () -> None :


`46`

`39`

poll_frequency = 1.0


`47`

`40`

async with httpx .AsyncClient () as client :


`48`

`41`

while True :


`49`

`42`

try :


`50`

`43`

response = await client .get (f"{ base_url } /health" , timeout = 1.0 )


`51`

`44`

if response .status_code == 200 :


`52`


- break



`45`

+ return


`53`

`46`

except (httpx .RequestError , httpx .TimeoutException ):


`54`

`47`

pass


`55`

`48`

await asyncio .sleep (poll_frequency )


`56`

`49`

poll_frequency = min (poll_frequency * 1.5 , 2.0 )


`57`

`50`



`58`


- timeout = 30.0


`59`

`51`

try :


`60`


- await asyncio .wait_for (wait_for_startup (), timeout )


`61`


- except TimeoutError :



`52`

+ try :



`53`

+ await asyncio .wait_for (wait_for_startup (), timeout = 30.0 )



`54`

+ except TimeoutError :



`55`

+ pytest .fail (f"MockServer on port { config .port } failed to start" )



`56`

+ yield base_url



`57`

+ finally :


`62`

`58`

server_process .terminate ()


`63`

`59`

server_process .join (timeout = 5 )


`64`

`60`

if server_process .is_alive ():


`65`

`61`

server_process .kill ()


`66`

`62`

server_process .join (timeout = 5 )


`67`


- pytest .fail (f"Server failed to start within { timeout } seconds" )


`68`

`63`



`69`


- yield base_url , config


`70`

`64`



`71`


- server_process .terminate ()


`72`


- server_process .join (timeout = 5 )


`73`


- if server_process .is_alive ():


`74`


- server_process .kill ()


`75`


- server_process .join (timeout = 5 )



`65`

+ @pytest_asyncio .fixture (scope = "class" )



`66`

+ async def mock_server_instance ():



`67`

+ """Instance-level fixture that provides a running server for HTTP testing."""



`68`

+



`69`

+ config = MockServerConfig (



`70`

+ host = "127.0.0.1" ,



`71`

+ port = 8012 ,



`72`

+ model = "test-model" ,



`73`

+ ttft_ms = 10.0 ,



`74`

+ itl_ms = 1.0 ,



`75`

+ request_latency = 0.1 ,



`76`

+ )



`77`

+ async with _run_mock_server (config ) as base_url :



`78`

+ yield base_url , config


`76`

`79`



`77`

`80`



`78`

`81`

class TestMockServerConfig :


@@ -1016,37 +1019,8 @@ async def fail_after_mock_server():


`1016`

`1019`

output_tokens = 4 ,


`1017`

`1020`

fail_after_requests = 2 ,


`1018`

`1021`

)


`1019`


- base_url = f"http://{ config .host } :{ config .port } "


`1020`


- server_process = multiprocessing .Process (


`1021`


- target = _start_server_process , args = (config ,)


`1022`


- )


`1023`


- server_process .start ()


`1024`


-


`1025`


- async def wait_for_startup ():


`1026`


- async with httpx .AsyncClient () as client :


`1027`


- while True :


`1028`


- try :


`1029`


- response = await client .get (f"{ base_url } /health" , timeout = 1.0 )


`1030`


- if response .status_code == 200 :


`1031`


- return


`1032`


- except (httpx .RequestError , httpx .TimeoutException ):


`1033`


- pass


`1034`


- await asyncio .sleep (0.2 )


`1035`


-


`1036`


- try :


`1037`


- await asyncio .wait_for (wait_for_startup (), timeout = 30.0 )


`1038`


- except TimeoutError :


`1039`


- server_process .terminate ()


`1040`


- server_process .join (timeout = 5 )


`1041`


- pytest .fail ("fail_after MockServer failed to start" )


`1042`


-


`1043`


- yield base_url


`1044`


-


`1045`


- server_process .terminate ()


`1046`


- server_process .join (timeout = 5 )


`1047`


- if server_process .is_alive ():


`1048`


- server_process .kill ()


`1049`


- server_process .join (timeout = 5 )



`1022`

+ async with _run_mock_server (config ) as base_url :



`1023`

+ yield base_url


`1050`

`1024`



`1051`

`1025`



`1052`

`1026`

@pytest_asyncio .fixture


@@ -1065,37 +1039,8 @@ async def concurrent_limit_mock_server():


`1065`

`1039`

output_tokens = 4 ,


`1066`

`1040`

max_concurrent_requests = 1 ,


`1067`

`1041`

)


`1068`


- base_url = f"http://{ config .host } :{ config .port } "


`1069`


- server_process = multiprocessing .Process (


`1070`


- target = _start_server_process , args = (config ,)


`1071`


- )


`1072`


- server_process .start ()


`1073`


-


`1074`


- async def wait_for_startup ():


`1075`


- async with httpx .AsyncClient () as client :


`1076`


- while True :


`1077`


- try :


`1078`


- response = await client .get (f"{ base_url } /health" , timeout = 1.0 )


`1079`


- if response .status_code == 200 :


`1080`


- return


`1081`


- except (httpx .RequestError , httpx .TimeoutException ):


`1082`


- pass


`1083`


- await asyncio .sleep (0.2 )


`1084`


-


`1085`


- try :


`1086`


- await asyncio .wait_for (wait_for_startup (), timeout = 30.0 )


`1087`


- except TimeoutError :


`1088`


- server_process .terminate ()


`1089`


- server_process .join (timeout = 5 )


`1090`


- pytest .fail ("concurrency MockServer failed to start" )


`1091`


-


`1092`


- yield base_url


`1093`


-


`1094`


- server_process .terminate ()


`1095`


- server_process .join (timeout = 5 )


`1096`


- if server_process .is_alive ():


`1097`


- server_process .kill ()


`1098`


- server_process .join (timeout = 5 )



`1042`

+ async with _run_mock_server (config ) as base_url :



`1043`

+ yield base_url


`1099`

`1044`



`1100`

`1045`



`1101`

`1046`

class TestMockServerFailAfterAndConcurrency :


## 0 commit comments