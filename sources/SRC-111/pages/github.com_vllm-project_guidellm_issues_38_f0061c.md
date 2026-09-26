source: https://github.com/vllm-project/guidellm/issues/38

After running the default flow on Mistral in vLLM, there is a large (>100MB) report json in the directory I ran the commands. This seems quite heavy-weight, especially for a json file.

Instead, I would expect there to be a light csv or something summarizing the report that is displayed in the terminal so I can easily load my results into a spreadsheet or pandas dataframe for post-processing.

Commands:

```
vllm serve mistralai/Mistral-7B-Instruct-v0.3
guidellm --target "http://localhost:8000/v1" --model mistralai/Mistral-7B-Instruct-v0.3
```


Directory output:

guidellm git:(main) ll
total 114M
-rw-rw-r-- 1 mgoin mgoin 3.4K Aug 27 15:56 CODE_OF_CONDUCT.md
-rw-rw-r-- 1 mgoin mgoin 2.4K Aug 27 15:56 CONTRIBUTING.md
-rw-rw-r-- 1 mgoin mgoin 7.1K Aug 27 15:56 DEVELOPING.md
drwxrwxr-x 4 mgoin mgoin 95 Aug 27 15:56 docs
-rw-rw-r-- 1 mgoin mgoin 114M Aug 27 16:19 guidance_report.json <<
-rw-rw-r-- 1 mgoin mgoin 12K Aug 27 15:56 LICENSE
-rw-rw-r-- 1 mgoin mgoin 16 Aug 27 15:56 MANIFEST.in
-rw-rw-r-- 1 mgoin mgoin 7.3K Aug 27 15:56 pyproject.toml
-rw-rw-r-- 1 mgoin mgoin 11K Aug 27 15:56 README.md
drwxrwxr-x 4 mgoin mgoin 59 Aug 27 15:56 src
drwxrwxr-x 6 mgoin mgoin 104 Aug 27 15:56 tests
-rw-rw-r-- 1 mgoin mgoin 1.7K Aug 27 15:56 tox.ini
drwxrwxr-x 2 mgoin mgoin 66 Aug 27 15:56 utils

After running the default flow on Mistral in vLLM, there is a large (>100MB) report json in the directory I ran the commands. This seems quite heavy-weight, especially for a json file.

Instead, I would expect there to be a light csv or something summarizing the report that is displayed in the terminal so I can easily load my results into a spreadsheet or pandas dataframe for post-processing.

Commands:

Directory output: