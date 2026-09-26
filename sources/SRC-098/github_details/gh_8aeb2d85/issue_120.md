# [Issue #120] Option to output results in csv and json format

source: https://github.com/NVIDIA/nccl-tests/issues/120
state: open | updated: 2025-11-21T19:14:51Z
labels: 

## 正文

Feature request to add an option to print results in a csv format table or json.


## 评论 (14)

### sjeaugey · 2022-12-02

Fair ask. Might need some work though to format things properly and make them easily accessible without making the file too bloated. I'll think about it.

### BlueCloudDev · 2023-01-24

I would like to second this request. I have automation working for running NCCL tests, but writing a text parser from this output is complicated and brittle. JSON or CSV would provide me more confidence that the output automation won't break in subsequent versions.

### lipovsek-aws · 2023-03-10

I already have a working fork, @sjeaugey are you already done with this or can clean up my fork and open PR here?

### sjeaugey · 2023-03-10

Sorry, I've been underwater and couldn't make progress on this. If you have a patch to propose, feel free to do so. I can't guarantee we'll find time to integrate but if it merges easily and it's a small patch, maybe we can do it.

### jbachan · 2023-03-10

@lipovsek-aws please open a PR.

My preference for a format would be a CSV file structured around independent and dependent variables, with one row per unique tuple of indepedent variables. For nccl-tests the independent vars are: operation, bytes, elements, iters, redop, datatype, etc.... The dependent vars are the measurements: usecs, algbw, busbw, wrongs. The first row of each table would begin with a `#` and follow with a list of variable names. All rows until the next `#` row would be parsed as the values for their ordinal respective variable. A `#` row containing an unrecognized variable name would be invalid. Example.

```
# operation, bytes, elements, iters, redop, datatype, usecs
allreduce, 1024, 256, 20, sum, float, 101
allreduce, 2048, 256, 20, sum, float, 203

# operation, bytes, elements, iters, datatype, usecs, busbw
broadcast, 1024, 256, 20, float, 41, 1.1e0
broadcast, 2048, 256, 20, float, 103, 1.8e0
```

If you have other thoughts for formats that are easier to work with please share. I look forward to the PR.

### sjeaugey · 2023-03-13

@jbachan Can you elaborate on why you wouldn't want to simply convert the current columns to CSV columns?
Extracting a particular column from a CSV is usually quite painless using tools like `cut`, while extracting the same from your proposition would be more complicated.

Besides, mimicking the current columns would make the patch quite limited, while changing the layout would probably mean more complexity.

### jbachan · 2023-03-13

I agree just slipping commas between the columns would be the smallest patch.

Ignoring minimality of patch length, my preference would be for a format that is "concatenative" meaning that we can direct the output of a battery of tests all to one file:
```
all_reduce_perf -dfloat -osum >> rows
all_reduce_perf -dint8 -osum >> rows
all_gather_perf  >> rows
```
This require that each row of measurement be fully described: all independent variables affecting the measurement row are easy to parse.

The format should also allow it easy for a later version of `nccl-tests` to add independent variables without breaking old sripts. For instance, if it occurs to us that adding "nranks" to the independent vars is a good idea, then feeding new output including that var to an old script not expecting that var should still work. This would just require the old script to ignore vars it doesn't know about. The following python script supports such forward compatability:

```
cols = [] # list of strs
rows = [] # list of dicts mapping var names to vals
for line in readlines():
  if line.startswith('#'):
    cols = [x.strip() for x in line[1:].split(',')]
  else:
    vals = [x.strip() for x in line.split(',')]
    rows.append(dict(zip(cols, vals)))

# build a list of (x,y) from all_gather where x='size' y='busbw'
xys = [(float(row['size']), float(row['busbw'])) for row in rows if row['test']=='all_reduce']
```

My CSV format meets the concatenative and compatability requirements. If there exists similar formats that can do the same, or cool tricks with `cut` that obviate their need then I would love to learn about them.

### lipovsek-aws · 2023-03-22

Hi, sorry for delayed response. I added flag "--file" for example "--file=/tmp/results" and then persisted current output to "/tmp/results.csv" and arguments to "/tmp/results.json" - that makes it fully reproducible and machine readable. I added in_place and out_of_place to column names since CSV isn't the best with multi level columns, but I'm more than happy to move it back to multi level if others find this better DX. I should be able to open PR end of next week.
@jbachan I think we can also add all parameters/outputs in each row, my goal was to separate results of the NCCL test with metadata, I could also just put it in CSV file and replicate parameters (algorithm, min/max packet size) over all rows.

### jbachan · 2023-03-23

Much appreciated @lipovsek-aws

Thoughts:
1. I would prefer we not use any JSON since it isn't easy to parse by hand. We should try to cater to the poor C programmer who writhes at the thought of external dependencies.
2. Flattening the column space is good.
3. Replicating everything across rows all in one file is my preference. Dead simple to parse.

### lipovsek-aws · 2023-03-23

I'm on board with dropping JSON and putting all data in CSV, data quantity should be low so data duplication is not a concern for me. I'll open PR late next week.

### lipovsek-aws · 2023-04-12

Lets continue conversation in https://github.com/NVIDIA/nccl-tests/pull/138 , @sjeaugey @jbachan please review.

### AddyLaddy · 2025-10-24

I've just pushed JSON support to the repo. Maybe we can next look to extend it with csv support.


### caio-davi · 2025-11-21

@AddyLaddy is there documentation on how to use the JSON support?

### AddyLaddy · 2025-11-21

Sorry not really, just what's in the help and commit message:

```
commit 00f52811b818e751245303378a97db59fae083c1 (tag: v2.17.3)
    Add support for JSON output to perf test framework
    
    This adds support for writing structured information about the run to a JSON file.
    
    Enable with -J <filename>.json
    
    If the target JSON filename already exists then an incrementing numeric suffix will be
    added to create <filename>.json.<n>
```
I find you have to view the output with a tool such as:

`jq . log.json`
