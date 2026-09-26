source: https://github.com/vllm-project/guidellm/commit/cee18403e6bd1f2cfffc12c15c4c84ae74a8a1a4

@@ -238,9 +238,8 @@ def create_fake_text(


`238`

`238`

"""


`239`

`239`

Generate fake text using a tokenizer processor with specified token count.


`240`

`240`



`241`


- Creates text by generating fake tokens and joining them into a string,


`242`


- ensuring the result has the exact number of tokens when processed by


`243`


- the given tokenizer.



`241`

+ Creates text by joining decoded chunks generated for the requested



`242`

+ simulated token count.


`244`

`243`



`245`

`244`

:param num_tokens: Target number of tokens in the generated text


`246`

`245`

:param processor: Tokenizer to use for token generation and validation


@@ -258,17 +257,18 @@ def create_fake_tokens_str(


`258`

`257`

fake : Faker | None = None ,


`259`

`258`

) -> list [str ]:


`260`

`259`

"""


`261`


- Generate fake token strings using a tokenizer processor.



`260`

+ Generate detokenized text chunks using a tokenizer processor.


`262`

`261`



`263`


- Creates a list of token strings by generating fake text and tokenizing it


`264`


- until the desired token count is reached. Uses the provided tokenizer


`265`


- for accurate token boundary detection.



`262`

+ Creates a list of text chunks by generating fake text and tokenizing it until



`263`

+ the desired token count is reached. The complete token sequence is decoded once



`264`

+ and divided into the same number of chunks so tokenizer-specific boundary markers



`265`

+ are not exposed without changing streaming event counts.


`266`

`266`



`267`

`267`

:param num_tokens: Target number of tokens to generate


`268`

`268`

:param processor: Tokenizer to use for token generation and validation


`269`

`269`

:param seed: Random seed for reproducible token generation


`270`

`270`

:param fake: Optional Faker instance for text generation


`271`


- :return: List of token strings with the specified count



`271`

+ :return: List of decoded text chunks matching the specified count


`272`

`272`

"""


`273`

`273`

if not fake :


`274`

`274`

fake = Faker ()


@@ -292,7 +292,20 @@ def create_fake_tokens_str(


`292`

`292`

)


`293`

`293`

tokens += new_tokens


`294`

`294`



`295`


- return tokens



`295`

+ if not tokens :



`296`

+ return []



`297`

+



`298`

+ text = processor .convert_tokens_to_string (tokens )



`299`

+ chunk_size , remainder = divmod (len (text ), len (tokens ))



`300`

+ chunks = []



`301`

+ start = 0



`302`

+ # Split all decoded text across exactly `len(tokens)` transport chunks,



`303`

+ # giving the first `remainder` chunks one extra character.



`304`

+ for index in range (len (tokens )):



`305`

+ end = start + chunk_size + (index < remainder )



`306`

+ chunks .append (text [start :end ])



`307`

+ start = end



`308`

+ return chunks


`296`

`309`



`297`

`310`



`298`

`311`

def times_generator (mean : float , standard_dev : float ) -> Generator [float ]:


## 0 commit comments