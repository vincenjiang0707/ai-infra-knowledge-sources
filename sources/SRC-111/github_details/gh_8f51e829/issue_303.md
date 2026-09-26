# [Issue #303] html reporter stopped displaying data

source: https://github.com/vllm-project/guidellm/issues/303
state: closed | updated: 2026-09-10T11:39:15Z
labels: UI

## 正文

**Describe the bug**
Few weeks ago, I converted json to html. Today I tried to open html again to see the test results. But html does not load the data. Only template, although there is data in html itself.

**Expected behavior**
I expected that the html report would always be available and in working order for local use. Even without network.

**Environment**
Include all relevant environment information:
1. OS [e.g. Ubuntu 20.04]:-
2. Python version [e.g. 3.12.2]:-

**To Reproduce**
Exact steps to reproduce the behavior:
I created a report a few weeks ago. It's been 2-3 weeks. Now the reporter is not showing the results

**Errors**
Maybe there's a problem with this link, it seems to have changed?
`https://blog.vllm.ai/guidellm/ui/latest/_next/static/chunks/main-app-0a264417b3ef65f5.js -> 404`
<img width="1475" height="47" alt="Image" src="https://github.com/user-attachments/assets/e6807a6c-6b0d-48b7-a2b0-491e7aed71cd" />

**Additional context**

<img width="1397" height="806" alt="Image" src="https://github.com/user-attachments/assets/60e3dc43-35a2-463c-aa86-3559107cefcd" />


## 评论 (8)

### ashishkamra · 2025-09-05

cc @DaltheCow 


### psydok · 2025-09-08

Error when running the script to create an HTML report:
```
Client error '404 Not Found' for url 'https://blog.vllm.ai/guidellm/ui/latest/index.html'
```

Code:
```
from pathlib import Path

from guidellm.benchmark import GenerativeBenchmarksReport


def generate_html_report(benchmark_file: Path):
    output_name = benchmark_file.name.replace(benchmark_file.suffix, ".html")
    output_file = benchmark_file.parent / f"{output_name}"
    report = GenerativeBenchmarksReport.load_file(
        path=str(benchmark_file),
    )
    report.save_html(output_file)
    return output_file
```

### sjmonson · 2025-09-09

As a temporary workaround, please follow the steps in [option 2 here](https://github.com/vllm-project/guidellm/blob/main/README.md#-generating-an-html-report-with-a-benchmark-run) to host the UI resources locally

### DaltheCow · 2025-09-09

There was a bug in the workflow that caused the current build to be deleted, a fix has been pushed to prevent that. There is another issue at play that I haven't resolved yet though.

The default html pathway relies on http://vllm-project.github.io/guidellm/ui/latest to be static/unchanging, but when a new release comes out, this build will be updated. Versioned releases will help with this but if the user didn't rely on a versioned release in the first place and used the default (latest), then there isn't a great way to update to use the versioned build so their html will still break.

The simplest solution I see going forward is to update: https://github.com/vllm-project/guidellm/blob/main/src/guidellm/config.py#L34 to point to the latest versioned build (http://vllm-project.github.io/guidellm/ui/v0.3.0 for example). As long as the versioned builds are never updated then this shouldn't happen again.

The build version will need to be incremented in config.py after every release. Will work on a PR for this.

### DaltheCow · 2025-09-09

As a side note, the only way to get the html report to work without network is to locally host the UI, but I'm aware we want it to work offline as well so I'll work on that as well

### markurtz · 2025-09-18

I don't think requiring network, at least for the first load, is unreasonable to display these, otherwise we'll increase the size of those reports significantly. I think a balanced solution here would be to setup a proper PWA so it can be installed locally on the browser and get away from always needing network

### DaltheCow · 2025-10-08

> I don't think requiring network, at least for the first load, is unreasonable to display these, otherwise we'll increase the size of those reports significantly. I think a balanced solution here would be to setup a proper PWA so it can be installed locally on the browser and get away from always needing network

PWA set up could be cool.

For now the "archive" should be easy to implement, just have to decide on the best way to do it.

Two best options in my mind are to stick with the current hosted build for the top level benchmarks.html (with potential PWA implementation in the future), and then save a separate archived build that will be self-contained. Both will have the injected data and be the same but the archived version will work offline. The other, simplest option, is that we don't have a top level benchmarks.html as the default. We just refer users to a "UI Report" directory or something that contains the build and benchmarks.html.

Is there any benefit to having a top level benchmarks.html rather than just a self contained UI Report directory? Or do we prefer the UI report to always go through this pathway of relying on the locally saved build?

### dbutenhof · 2026-09-10

Fixed by #1032 for 0.8
