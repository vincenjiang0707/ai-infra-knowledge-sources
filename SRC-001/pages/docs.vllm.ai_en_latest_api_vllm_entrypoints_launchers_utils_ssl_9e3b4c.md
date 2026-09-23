source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/utils/ssl/
lastmod: 2026-09-23

#

`vllm.entrypoints.launchers.utils.ssl`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.utils.ssl)

Classes:

-
–[SSLCertRefresher](https://docs.vllm.ai#vllm.entrypoints.launchers.utils.ssl.SSLCertRefresher)A class that monitors SSL certificate files and


##

`SSLCertRefresher`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.utils.ssl.SSLCertRefresher)

A class that monitors SSL certificate files and reloads them when they change.

Methods:

-
–[stop](https://docs.vllm.ai#vllm.entrypoints.launchers.utils.ssl.SSLCertRefresher.stop)Stop watching files.


## Source code in `vllm/entrypoints/launchers/utils/ssl.py`


###

`_watch_files(paths, fun)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.utils.ssl.SSLCertRefresher._watch_files)

Watch multiple file paths asynchronously.

## Source code in `vllm/entrypoints/launchers/utils/ssl.py`


###

`stop()`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.utils.ssl.SSLCertRefresher.stop)

Stop watching files.