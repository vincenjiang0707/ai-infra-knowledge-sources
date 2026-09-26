source: https://github.com/vllm-project/guidellm/commit/98f588078fe0a1d3d529f1ae13caabd758c59a34

File tree Expand file tree Collapse file tree

Expand file tree Collapse file tree Original file line number Diff line number Diff line change @@ -165,6 +165,10 @@ docs = "https://github.com/vllm-project/guidellm/tree/main/docs"


`165`

`165`

guidellm = " guidellm.__main__:cli"


`166`

`166`



`167`

`167`




`168`

+ [tool .disdantic ]



`169`

+ schema_rebuild_parents = false



`170`

+



`171`

+


`168`

`172`

# ************************************************


`169`

`173`

# ********** Code Quality Tools **********


`170`

`174`

# ************************************************



Original file line number Diff line number Diff line change `1`

`1`

import os


`2`

`2`




`3`

+ import disdantic


`3`

`4`

import pytest


`4`

`5`



`5`

`6`

from guidellm .settings import (


@@ -27,6 +28,12 @@ def test_default_settings(mocker):


`27`

`28`

assert settings .report_generation .source .startswith (BASE_URL )


`28`

`29`



`29`

`30`




`31`

+ @pytest .mark .sanity



`32`

+ def test_disdantic_global_settings ():



`33`

+ settings = disdantic .get_settings ()



`34`

+ assert settings .schema_rebuild_parents == False



`35`

+



`36`

+


`30`

`37`

@pytest .mark .smoke


`31`

`38`

def test_settings_from_env_variables (mocker ):


`32`

`39`

mocker .patch .dict (



You can’t perform that action at this time.


## 0 commit comments