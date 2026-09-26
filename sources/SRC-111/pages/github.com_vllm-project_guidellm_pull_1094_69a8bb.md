source: https://github.com/vllm-project/guidellm/pull/1094

## Conversation

[git-jxj](https://github.com/git-jxj)

[force-pushed](https://github.com/vllm-project/guidellm/compare/7c2ce9c63dcc67e714cdb9fbadc5f453b60f1cb5..6c3c6d5a1c1335b95dfbd346fce31e03adc87453)the fix/sqlite-file-loading branch from

[to](https://github.com/vllm-project/guidellm/commit/7c2ce9c63dcc67e714cdb9fbadc5f453b60f1cb5)

`7c2ce9c`


`6c3c6d5`

[Compare](https://github.com/vllm-project/guidellm/compare/7c2ce9c63dcc67e714cdb9fbadc5f453b60f1cb5..6c3c6d5a1c1335b95dfbd346fce31e03adc87453)

September 9, 2026 06:50

Generated-by: Codex Signed-off-by: xinjun.jiang <xinjun.jiang@daocloud.io>

[git-jxj](https://github.com/git-jxj)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6c3c6d5a1c1335b95dfbd346fce31e03adc87453..31f947344aa6281b14a8d66d5250f062fcd2632f)the fix/sqlite-file-loading branch from

[to](https://github.com/vllm-project/guidellm/commit/6c3c6d5a1c1335b95dfbd346fce31e03adc87453)

`6c3c6d5`


`31f9473`

[Compare](https://github.com/vllm-project/guidellm/compare/6c3c6d5a1c1335b95dfbd346fce31e03adc87453..31f947344aa6281b14a8d66d5250f062fcd2632f)

September 24, 2026 01:25

[git-jxj](https://github.com/git-jxj)requested review from

[dbutenhof](https://github.com/dbutenhof),

[dfeddema](https://github.com/dfeddema),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)as

[code owners](https://github.com/vllm-project/guidellm/blob/4e2cd400113c0ef005b1376a7ffb44abf416c8cb/CODEOWNERS#L2)

September 24, 2026 01:25

|
I rebased this PR onto the current main branch and moved the dataset guide addition to its new |


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Sep 24, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

My big problem with this solution is that `Datasets.from_sql`

is not strictly limited to sqlite3, and you've forced that restriction. I did some independent experimentation: *in theory* we want to pass a SQLAlchemy URI for the dataset `path`

string, which `Datasets.from_sql`

would read and process using your query string.

There are a couple of problems with this:

- You can't actually pass a SQLAlchemy URI through the
`kind=db_file,path=`

parameter, because`DataFileArgs.path`

is typed as`Path`

. The`Path`

processing removes the "redundant"`/`

characters. - The
`DBFileDatasetDeserializer`

checks that`config.path`

is a file that exists: and that won't work with a URI. - Passing a
`Path`

to`Datasets.from_sql`

won't work: it's expecting a`str`

or a`Connection`

. - Even once we've gotten past those issues, while
`Datasets.from_sql`

is prepared to use SQLAlchemy to open and access the database (of various kinds, like PostgreSQL, etc.), it requires that "someone else" have imported SQLAlchemy, and we don't.

SQLAlchemy is a complicated ecosystem, not a single Python module ... for example to actually use PostgreSQL we'd also need psycopg2, pymysql, etc.

Clearly nobody has used `--data kind=db_file`

, because there's no way to make it work. I don't think we're interested in tackling the entire SQLAlchemy ecosystem to handle the full potential range of databases through `Datasets.from_sql`

at this time, so the core change of your PR is probably fine.

**HOWEVER**:

I want it implemented in a way that can be extended to support the full range later, and that means we can't blindly *assume* a sqlite3 database as you've done.

We want to support the full allowed *syntax*, and that means taking a SQLAlchemy URI to specify the database; something like:

`--data kind=db_file,path=sqlite:///file.db,load_kwargs.sql="SELECT text FROM samples"`


This implies a few additional changes:

- A new
`class SqlDataArgs(DataArgs)`

... since we can be pretty sure nobody's successfully*used*`--data kind=file_db`

, it probably makes sense to change`path`

to`uri`

to clarify the meaning. And it'll be typed as a`str`

... or perhaps as Pydantic`AnyUrl`

(which provides parsing and minimal syntax checking). - In the
`DbFileDatasetDeserializer`

, we can check that`config.uri.scheme == "sqlite"`

and raise a`ValueError`

if something else is specified. (Note, that's the main advantage of using`AnyUrl`

vs`str`

). - Obviously, we remove the file exists & is_file checks from the deserializer.
- If we imported SQLAlchemy (without any additional drivers), we could just pass
`str(config.uri)`

to`Datasets.from_sql`

; but I think that, at least for now, it makes more sense to skip that new dependency and use your simple`sqlite3.connect`

code, with`str(config.uri.path)[1:]`

as the file name. (Because`.path`

includes the leading`/`

.) - The
`db_file`

format should be documented as a bullet in the "Accepted types" list, including the information you added in your separate paragraph. It should say that GuideLLM currently only supports loading from a sqlite3 database.

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Loading a local SQLite dataset with

`kind=db_file`

fails because its filesystem path is passed to`Dataset.from_sql`

as a database URI. The existing success test mocks the database read and hides the failure.## Details

Open the file using a SQLite connection and close it after loading. Replace the mocked read with a real SQLite query, and document how to supply that query through

`load_kwargs.sql`

.## Test Plan

`#`

, and verified SQL filtering returns the expected row.`tox -e lint-check,type-check`

passed.## Related Issues

None.

## Use of AI

## git log

commit

31f9473Author: xinjun.jiang xinjun.jiang@daocloud.io

Date: Sat Sep 5 20:30:02 2026 +0800

Generated-by: Codex

Signed-off-by: xinjun.jiang xinjun.jiang@daocloud.io