source: https://github.com/vllm-project/guidellm/commit/613dc9a5839f461f3781bda9aca11e5c446ae887

`1`

`1`

from __future__ import annotations


`2`

`2`




`3`

+ import json


`3`

`4`

import re


`4`

`5`

from collections import defaultdict


`5`

`6`

from typing import Any , ClassVar , Literal , TypeAlias , cast


`6`

`7`



`7`


- from datasets import Dataset , IterableDataset



`8`

+ from datasets import Dataset , DatasetDict , IterableDataset , IterableDatasetDict


`8`

`9`

from pydantic import Field


`9`

`10`



`10`

`11`

from guidellm .data .preprocessors .preprocessor import (


`29`

`30`

DatasetColumnValue : TypeAlias = tuple [int , str ]


`30`

`31`



`31`

`32`




`33`

+ def _unwrap_dataset_dict (



`34`

+ dataset : Dataset | IterableDataset | DatasetDict | IterableDatasetDict ,



`35`

+ ) -> Dataset | IterableDataset :



`36`

+ """Unwrap a DatasetDict/IterableDatasetDict into a single split.



`37`

+



`38`

+ Prefers the ``"train"`` split if available, otherwise picks the first split.



`39`

+ Returns the input unchanged if it is already a single Dataset/IterableDataset.



`40`

+



`41`

+ :param dataset: The dataset or dataset dict to unwrap.



`42`

+ :return: A single Dataset or IterableDataset.



`43`

+ """



`44`

+ if isinstance (dataset , DatasetDict | IterableDatasetDict ):



`45`

+ if "train" in dataset :



`46`

+ return dataset ["train" ]



`47`

+ return dataset [next (iter (dataset ))]



`48`

+ return dataset



`49`

+



`50`

+



`51`

+ def _detect_json_wrapper (



`52`

+ dataset : Dataset | IterableDataset , dataset_columns : list [str ]



`53`

+ ) -> str | None :



`54`

+ """Check if a dataset has a single string column containing JSON dicts.



`55`

+



`56`

+ :param dataset: The dataset to inspect.



`57`

+ :param dataset_columns: The column names present in the dataset.



`58`

+ :return: The wrapper column name if detected, or None.



`59`

+ """



`60`

+ if len (dataset_columns ) != 1 :



`61`

+ return None



`62`

+



`63`

+ candidate = dataset_columns [0 ]



`64`

+ sample = next (iter (dataset ))



`65`

+ value = sample [candidate ]



`66`

+ if not isinstance (value , str ):



`67`

+ return None



`68`

+



`69`

+ try :



`70`

+ parsed = json .loads (value )



`71`

+ except (json .JSONDecodeError , TypeError ):



`72`

+ return None



`73`

+



`74`

+ if isinstance (parsed , dict ) and parsed :



`75`

+ return candidate



`76`

+ return None



`77`

+



`78`

+



`79`

+ def _resolve_virtual_columns (



`80`

+ dataset : Dataset | IterableDataset , wrapper_column : str



`81`

+ ) -> list [str ]:



`82`

+ """Parse the first row's JSON wrapper and return its inner keys.



`83`

+



`84`

+ :param dataset: The dataset to peek at.



`85`

+ :param wrapper_column: The name of the column containing the JSON string.



`86`

+ :return: List of inner key names from the parsed JSON dict.



`87`

+ """



`88`

+ sample = next (iter (dataset ))



`89`

+ parsed = json .loads (sample [wrapper_column ])



`90`

+ return list (parsed .keys ())



`91`

+



`92`

+



`93`

+ def _extract_json_field (



`94`

+ row_data : dict [str , Any ], wrapper_column : str , field : str



`95`

+ ) -> Any :



`96`

+ """Parse a JSON wrapper column and extract a specific inner field.



`97`

+



`98`

+ :param row_data: The raw row dict from the dataset.



`99`

+ :param wrapper_column: The column name containing the JSON string.



`100`

+ :param field: The key to extract from the parsed JSON dict.



`101`

+ :return: The value of the requested field, or None if not present.



`102`

+ """



`103`

+ raw = row_data .get (wrapper_column )



`104`

+ if not isinstance (raw , str ):



`105`

+ return None



`106`

+ try :



`107`

+ parsed = json .loads (raw )



`108`

+ except (json .JSONDecodeError , TypeError ):



`109`

+ return None



`110`

+ return parsed .get (field )



`111`

+



`112`

+


`32`

`113`

@DataPreprocessorArgs .register (


`33`

`114`

[


`34`

`115`

"generative_column_mapper" ,


@@ -117,6 +198,9 @@ class GenerativeColumnMapper(DataDependentPreprocessor):


`117`

`198`

"tool_result" ,


`118`

`199`

"tool_output" ,


`119`

`200`

],



`201`

+ "turn_type_column" : [



`202`

+ "turn_type" ,



`203`

+ ],


`120`

`204`

"relative_timestamp_column" : ["relative_timestamp" ],


`121`

`205`

"requeue_delay_column" : ["requeue_delay" ],


`122`

`206`

}


@@ -163,31 +247,38 @@ def datasets_mappings(


`163`

`247`

cls ,


`164`

`248`

datasets : list [Dataset | IterableDataset ],


`165`

`249`

input_mappings : dict [str , str | list [str ]] | None = None ,


`166`


- ) -> dict [DatasetColumnKey , list [DatasetColumnValue ]]:



`250`

+ ) -> tuple [ dict [DatasetColumnKey , list [DatasetColumnValue ]], dict [ int , str ]]:


`167`

`251`

"""


`168`

`252`

Resolve column mappings across one or more datasets.


`169`

`253`



`170`

`254`

For each dataset, matches actual column names against the requested


`171`

`255`

mapping names (or :attr:`defaults`) using regex patterns that account


`172`

`256`

for pluralisation and turn suffixes (e.g. ``prompt-0``, ``prompt-1``).


`173`

`257`




`258`

+ When a dataset has no direct column matches but contains a single



`259`

+ JSON-string column, the inner keys of that JSON are used as virtual



`260`

+ column names and matching is retried.



`261`

+


`174`

`262`

:param datasets: The loaded datasets to inspect for column names.


`175`

`263`

:param input_mappings: Optional explicit column mappings. When ``None``,


`176`

`264`

:attr:`defaults` is used. Values may be a single name or a list of


`177`

`265`

candidate names in priority order.


`178`


- :return: A dict keyed by ``(column_type, turn_index)`` whose values are


`179`


- lists of ``(dataset_index, column_name)`` pairs indicating where


`180`


- each logical column can be found. Categories with no matching


`181`


- columns are silently omitted from the result.



`266`

+ :return: A tuple of (mappings, json_wrappers) where mappings is a dict



`267`

+ keyed by ``(column_type, turn_index)`` whose values are lists of



`268`

+ ``(dataset_index, column_name)`` pairs, and json_wrappers is a dict



`269`

+ mapping dataset_index to the wrapper column name for datasets that



`270`

+ required JSON unwrapping.


`182`

`271`

"""


`183`

`272`

mappings : dict [DatasetColumnKey , list [DatasetColumnValue ]] = defaultdict (list )



`273`

+ json_wrappers : dict [int , str ] = {}


`184`

`274`

input_map : dict [str , list [str ]] = cls .defaults


`185`

`275`

if input_mappings :


`186`

`276`

input_map = {


`187`

`277`

k : v if isinstance (v , list ) else [v ] for k , v in input_mappings .items ()


`188`

`278`

}


`189`

`279`



`190`


- for index , dataset in enumerate (datasets ):



`280`

+ for index , raw_dataset in enumerate (datasets ):



`281`

+ dataset = _unwrap_dataset_dict (raw_dataset )


`191`

`282`

dataset_name = (


`192`

`283`

dataset .info .dataset_name


`193`

`284`

if dataset .info and dataset .info .dataset_name


@@ -196,34 +287,72 @@ def datasets_mappings(


`196`

`287`

dataset_columns = dataset .column_names or list (next (iter (dataset )).keys ())


`197`

`288`

dataset_columns_str = "\n " .join (dataset_columns )


`198`

`289`



`199`


- for column_type , names in input_map .items ():


`200`


- filtered_names = cls ._filter_for_dataset (


`201`


- names , str (index ), str (dataset_name )


`202`


- )


`203`


- if not filtered_names :


`204`


- continue



`290`

+ matched = cls ._match_columns (



`291`

+ index , input_map , dataset_name , dataset_columns_str



`292`

+ )


`205`

`293`



`206`


- column_pattern = cls .column_name_pattern .format (


`207`


- name = "|" .join (re .escape (n ) for n in filtered_names )


`208`


- )


`209`


- # Find the first matching column name


`210`


- base_match = re .search (column_pattern , dataset_columns_str , re .M | re .I )


`211`


- if not base_match :


`212`


- continue



`294`

+ # Fallback: if no matches found, try JSON unwrapping



`295`

+ if not matched :



`296`

+ wrapper = _detect_json_wrapper (dataset , dataset_columns )



`297`

+ if wrapper :



`298`

+ virtual_columns = _resolve_virtual_columns (dataset , wrapper )



`299`

+ virtual_columns_str = "\n " .join (virtual_columns )



`300`

+ matched = cls ._match_columns (



`301`

+ index , input_map , dataset_name , virtual_columns_str



`302`

+ )



`303`

+ if matched :



`304`

+ json_wrappers [index ] = wrapper


`213`

`305`



`214`


- turn_pattern = cls .column_name_pattern .format (


`215`


- name = base_match .group ("match_name" ),


`216`


- )


`217`


- turn_columns = cls ._extract_turn_columns (


`218`


- turn_pattern ,


`219`


- dataset_columns_str ,


`220`


- )



`306`

+ for key , values in matched .items ():



`307`

+ mappings [key ].extend (values )


`221`

`308`



`222`


- for turn , column_name in sorted (turn_columns ):


`223`


- column_type = cast ("GenerativeDatasetColumnType" , column_type )


`224`


- mappings [(column_type , turn )].append ((index , column_name ))



`309`

+ return mappings , json_wrappers


`225`

`310`



`226`


- return mappings



`311`

+ @classmethod



`312`

+ def _match_columns (



`313`

+ cls ,



`314`

+ index : int ,



`315`

+ input_map : dict [str , list [str ]],



`316`

+ dataset_name : str | int ,



`317`

+ dataset_columns_str : str ,



`318`

+ ) -> dict [DatasetColumnKey , list [DatasetColumnValue ]]:



`319`

+ """Match input_map names against dataset columns using regex patterns.



`320`

+



`321`

+ :param index: The dataset index in the multi-dataset list.



`322`

+ :param input_map: Mapping of column types to candidate column names.



`323`

+ :param dataset_name: Name or index of the dataset for filtering.



`324`

+ :param dataset_columns_str: Newline-joined string of column names.



`325`

+ :return: Dict of matched (column_type, turn) -> [(index, column_name)].



`326`

+ """



`327`

+ matched : dict [DatasetColumnKey , list [DatasetColumnValue ]] = defaultdict (list )



`328`

+



`329`

+ for column_type , names in input_map .items ():



`330`

+ filtered_names = cls ._filter_for_dataset (



`331`

+ names , str (index ), str (dataset_name )



`332`

+ )



`333`

+ if not filtered_names :



`334`

+ continue



`335`

+



`336`

+ column_pattern = cls .column_name_pattern .format (



`337`

+ name = "|" .join (re .escape (n ) for n in filtered_names )



`338`

+ )



`339`

+ base_match = re .search (column_pattern , dataset_columns_str , re .M | re .I )



`340`

+ if not base_match :



`341`

+ continue



`342`

+



`343`

+ turn_pattern = cls .column_name_pattern .format (



`344`

+ name = base_match .group ("match_name" ),



`345`

+ )



`346`

+ turn_columns = cls ._extract_turn_columns (



`347`

+ turn_pattern ,



`348`

+ dataset_columns_str ,



`349`

+ )



`350`

+



`351`

+ for turn , column_name in sorted (turn_columns ):



`352`

+ column_type = cast ("GenerativeDatasetColumnType" , column_type )



`353`

+ matched [(column_type , turn )].append ((index , column_name ))



`354`

+



`355`

+ return matched


`227`

`356`



`228`

`357`

def __init__ (


`229`

`358`

self ,


@@ -233,6 +362,23 @@ def __init__(


`233`

`362`

self .datasets_column_mappings : (


`234`

`363`

dict [DatasetColumnKey , list [DatasetColumnValue ]] | None


`235`

`364`

)



`365`

+ self ._json_wrappers : dict [int , str ] = {}



`366`

+



`367`

+ def _get_column_value (



`368`

+ self , items : list [dict [str , Any ]], dataset_index : int , dataset_column : str



`369`

+ ) -> Any :



`370`

+ """Read a column value, unwrapping JSON if needed for this dataset.



`371`

+



`372`

+ :param items: The per-dataset row items from the iterator.



`373`

+ :param dataset_index: Index of the dataset to read from.



`374`

+ :param dataset_column: Column name (possibly virtual) to extract.



`375`

+ :return: The column value from the row.



`376`

+ """



`377`

+ row_data = items [dataset_index ]["dataset" ]



`378`

+ wrapper = self ._json_wrappers .get (dataset_index )



`379`

+ if wrapper is not None :



`380`

+ return _extract_json_field (row_data , wrapper , dataset_column )



`381`

+ return row_data [dataset_column ]


`236`

`382`



`237`

`383`

def __call__ (self , items : list [dict [str , Any ]]) -> list [dict [str , list [Any ]]]:


`238`

`384`

if self .datasets_column_mappings is None :


@@ -253,7 +399,7 @@ def __call__(self, items: list[dict[str, Any]]) -> list[dict[str, list[Any]]]:


`253`

`399`

dataset_column ,


`254`

`400`

) in column_mappings :


`255`

`401`

mapped [turn ][column_type ].append (


`256`


- items [ dataset_index ][ "dataset" ][ dataset_column ]



`402`

+ self . _get_column_value ( items , dataset_index , dataset_column )


`257`

`403`

)


`258`

`404`



`259`

`405`

return [dict (m ) for m in mapped if len (m ) > 0 ]


@@ -262,7 +408,7 @@ def setup_data(


`262`

`408`

self ,


`263`

`409`

datasets : list [DatasetType ],


`264`

`410`

):


`265`


- self .datasets_column_mappings = self .datasets_mappings (



`411`

+ self .datasets_column_mappings , self . _json_wrappers = self .datasets_mappings (


`266`

`412`

datasets , self .input_mappings


`267`

`413`

)


`268`

`414`



## 0 commit comments