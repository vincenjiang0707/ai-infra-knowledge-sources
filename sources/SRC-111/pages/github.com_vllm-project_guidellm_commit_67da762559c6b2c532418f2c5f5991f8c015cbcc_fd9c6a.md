source: https://github.com/vllm-project/guidellm/commit/67da762559c6b2c532418f2c5f5991f8c015cbcc

`12`

`12`

import pytest


`13`

`13`

import pytest_asyncio


`14`

`14`

from pydantic import ValidationError



`15`

+ from transformers import AutoTokenizer


`15`

`16`



`16`

`17`

from guidellm .mock_server .server import MockServer


`17`

`18`

from guidellm .schemas .mock_server .config import MockServerConfig


`18`

`19`

from tests .fixtures .tokenizers import MINIMAL_TOKENIZER_DIR


`19`

`20`



`20`

`21`



`21`

`22`

# Start server in a separate process


`22`


- def _start_server_process (config : MockServerConfig ):



`23`

+ def _start_server_process (



`24`

+ config : MockServerConfig ,



`25`

+ chat_template : str | None = None ,



`26`

+ ):


`23`

`27`

server = MockServer (config )



`28`

+ if chat_template is not None :



`29`

+ server .chat_handler .tokenizer .chat_template = chat_template


`24`

`30`

# Disable Sanic access logs / MOTD so ANSI formatters do not clobber pytest's TTY.


`25`

`31`

server .run (access_log = False )


`26`

`32`



`27`

`33`



`28`

`34`

@asynccontextmanager


`29`

`35`

async def _run_mock_server (


`30`

`36`

config : MockServerConfig ,



`37`

+ chat_template : str | None = None ,


`31`

`38`

) -> AsyncGenerator [str , None ]:


`32`

`39`

base_url = f"http://{ config .host } :{ config .port } "


`33`

`40`

server_process = multiprocessing .Process (


`34`


- target = _start_server_process , args = (config ,)



`41`

+ target = _start_server_process ,



`42`

+ args = (config , chat_template ),


`35`

`43`

)


`36`

`44`

server_process .start ()


`37`

`45`



@@ -1121,6 +1129,28 @@ async def one_request(client: httpx.AsyncClient) -> float:


`1121`

`1129`

assert max (durations ) >= 0.3


`1122`

`1130`



`1123`

`1131`




`1132`

+ @pytest_asyncio .fixture (scope = "module" )



`1133`

+ async def huggingface_mock_server ():



`1134`

+ """MockServer configured with the vendored Hugging Face tokenizer.



`1135`

+



`1136`

+ ## WRITTEN BY AI ##



`1137`

+ """



`1138`

+ chat_template = "{% for message in messages %}{{ message['content'] }}{% endfor %}"



`1139`

+ config = MockServerConfig (



`1140`

+ host = "127.0.0.1" ,



`1141`

+ port = 8015 ,



`1142`

+ model = "huggingface-model" ,



`1143`

+ processor = str (MINIMAL_TOKENIZER_DIR ),



`1144`

+ output_tokens = 1 ,



`1145`

+ ttft_ms = 0 ,



`1146`

+ itl_ms = 0 ,



`1147`

+ )



`1148`

+ async with _run_mock_server (config , chat_template ) as base_url :



`1149`

+ tokenizer = AutoTokenizer .from_pretrained (MINIMAL_TOKENIZER_DIR )



`1150`

+ tokenizer .chat_template = chat_template



`1151`

+ yield base_url , config , tokenizer



`1152`

+



`1153`

+


`1124`

`1154`

@pytest .mark .regression


`1125`

`1155`

def test_initializes_with_huggingface_processor ():


`1126`

`1156`

"""Test all handlers initialize with a Hugging Face tokenizer.


@@ -1135,3 +1165,59 @@ def test_initializes_with_huggingface_processor():


`1135`

`1165`

assert server .completions_handler .tokenizer is not None


`1136`

`1166`

assert server .responses_handler .tokenizer is not None


`1137`

`1167`

assert server .tokenizer_handler .tokenizer is not None



`1168`

+



`1169`

+



`1170`

+ @pytest .mark .regression



`1171`

+ @pytest .mark .asyncio



`1172`

+ @pytest .mark .parametrize (



`1173`

+ ("endpoint" , "input_field" , "max_tokens_field" , "usage_field" ),



`1174`

+ [



`1175`

+ (



`1176`

+ "/v1/chat/completions" ,



`1177`

+ "messages" ,



`1178`

+ "max_tokens" ,



`1179`

+ "prompt_tokens" ,



`1180`

+ ),



`1181`

+ ("/v1/completions" , "prompt" , "max_tokens" , "prompt_tokens" ),



`1182`

+ ("/v1/responses" , "input" , "max_output_tokens" , "input_tokens" ),



`1183`

+ ],



`1184`

+ ids = ("chat_completions" , "completions" , "responses" ),



`1185`

+ )



`1186`

+ async def test_handles_requests_with_huggingface_processor (



`1187`

+ huggingface_mock_server ,



`1188`

+ endpoint ,



`1189`

+ input_field ,



`1190`

+ max_tokens_field ,



`1191`

+ usage_field ,



`1192`

+ ):



`1193`

+ """Test Hugging Face tokenizers handle and count endpoint prompts.



`1194`

+



`1195`

+ ## WRITTEN BY AI ##



`1196`

+ """



`1197`

+ server_url , config , tokenizer = huggingface_mock_server



`1198`

+ prompt = "Hello world " * 20



`1199`

+ messages = [{"role" : "user" , "content" : prompt }]



`1200`

+ is_chat = input_field == "messages"



`1201`

+ input_value = messages if is_chat else prompt



`1202`

+ prompt_text = (



`1203`

+ tokenizer .apply_chat_template (messages , tokenize = False )



`1204`

+ if is_chat



`1205`

+ else prompt



`1206`

+ )



`1207`

+ payload = {



`1208`

+ "model" : config .model ,



`1209`

+ input_field : input_value ,



`1210`

+ max_tokens_field : 1 ,



`1211`

+ }



`1212`

+



`1213`

+ async with httpx .AsyncClient () as client :



`1214`

+ response = await client .post (



`1215`

+ f"{ server_url } { endpoint } " ,



`1216`

+ json = payload ,



`1217`

+ timeout = 10.0 ,



`1218`

+ )



`1219`

+



`1220`

+ assert response .status_code == 200



`1221`

+ assert response .json ()["usage" ][usage_field ] == len (



`1222`

+ tokenizer .encode (prompt_text )



`1223`

+ )


## 0 commit comments