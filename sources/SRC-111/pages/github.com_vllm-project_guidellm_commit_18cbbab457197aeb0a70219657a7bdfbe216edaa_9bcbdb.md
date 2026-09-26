source: https://github.com/vllm-project/guidellm/commit/18cbbab457197aeb0a70219657a7bdfbe216edaa

@@ -249,6 +249,8 @@ def __init__(self, config: WEKATraceFormatArgs, dataset: Dataset) -> None:


`249`

`249`

self ._conversations : list [tuple [str , list [dict [str , Any ]], str | None ]] = []


`250`

`250`

self ._tools_json = _serialized_tools (config .tools )


`251`

`251`

self ._tool_response_sampler : Iterator [int ] | None = None



`252`

+ self .discarded_rows = 0



`253`

+ self .discarded_turns = 0


`252`

`254`

self .requests_col = _find_requests_column (dataset )


`253`

`255`

if self .requests_col is None :


`254`

`256`

raise DataNotSupportedError (


@@ -257,6 +259,8 @@ def __init__(self, config: WEKATraceFormatArgs, dataset: Dataset) -> None:


`257`

`259`



`258`

`260`

def __iter__ (self ) -> Iterable [Dataset ]:


`259`

`261`

self ._conversations = []



`262`

+ self .discarded_rows = 0



`263`

+ self .discarded_turns = 0


`260`

`264`

for row in self .dataset :


`261`

`265`

conv_id = str (row [self .config .conversation_id_column ])


`262`

`266`

# File order is spawn/join topology for every request list,


@@ -387,6 +391,9 @@ def build_conversation_graph(


`387`

`391`

raise InvalidRowError (


`388`

`392`

"WEKA format: conversation has no API requests to replay"


`389`

`393`

)



`394`

+ specs = self ._apply_max_context_len (specs , conv_id )



`395`

+ if not specs :



`396`

+ return ConversationGraphData (turns = [])


`390`

`397`

min_t = min (spec .absolute_t for spec in specs )


`391`

`398`

turns : list [ConversationTurnData ] = []


`392`

`399`

for spec in specs :


@@ -426,6 +433,64 @@ def build_conversation_graph(


`426`

`433`

)


`427`

`434`

return ConversationGraphData (turns = turns )


`428`

`435`




`436`

+ def _apply_max_context_len (



`437`

+ self , specs : list [_TurnSpec ], conversation_id : str



`438`

+ ) -> list [_TurnSpec ]:



`439`

+ """Drop turns that would exceed ``max_context_len``, or the whole row.



`440`

+



`441`

+ Walks specs in emit order and accumulates each turn's input+output



`442`

+ tokens. The overflowing turn and every later spec are discarded. If



`443`

+ the first turn already exceeds the budget, all specs are dropped so



`444`

+ the conversation can be skipped.



`445`

+



`446`

+ :param specs: API turn specs from ``_emit_chain``.



`447`

+ :param conversation_id: Conversation UUID used in discard logs.



`448`

+ :return: Kept prefix, or an empty list when the conversation is



`449`

+ discarded.



`450`

+ """



`451`

+ max_len = self .config .max_context_len



`452`

+ if max_len is None :



`453`

+ return specs



`454`

+



`455`

+ total = 0



`456`

+ kept : list [_TurnSpec ] = []



`457`

+ prompt_col = self .config .prompt_tokens_column



`458`

+ output_col = self .config .output_tokens_column



`459`

+ for spec in specs :



`460`

+ turn_tokens = int (spec .row [prompt_col ]) + int (spec .row [output_col ])



`461`

+ if total + turn_tokens > max_len :



`462`

+ remaining = len (specs ) - len (kept )



`463`

+ if not kept :



`464`

+ logger .info (



`465`

+ "WEKA conversation '{}' discarded: first turn at "



`466`

+ "node '{}' input+output tokens {} exceed "



`467`

+ "max_context_len {} (running={}, dropping {} turn(s))" ,



`468`

+ conversation_id ,



`469`

+ spec .node_id ,



`470`

+ turn_tokens ,



`471`

+ max_len ,



`472`

+ total ,



`473`

+ remaining ,



`474`

+ )



`475`

+ self .discarded_rows += 1



`476`

+ return []



`477`

+ logger .info (



`478`

+ "WEKA conversation '{}' truncated: discarding {} "



`479`

+ "turn(s) starting at node '{}' (turn tokens={}, "



`480`

+ "running={}, max_context_len={})" ,



`481`

+ conversation_id ,



`482`

+ remaining ,



`483`

+ spec .node_id ,



`484`

+ turn_tokens ,



`485`

+ total ,



`486`

+ max_len ,



`487`

+ )



`488`

+ self .discarded_turns += remaining



`489`

+ break



`490`

+ total += turn_tokens



`491`

+ kept .append (spec )



`492`

+ return kept



`493`

+


`429`

`494`

def _tool_response_text (


`430`

`495`

self , processor : PreTrainedTokenizerBase , faker : Faker


`431`

`496`

) -> str :


## 0 commit comments