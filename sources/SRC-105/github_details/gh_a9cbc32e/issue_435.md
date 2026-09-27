# [Issue #435] Roofline based on dispatch ID

source: https://github.com/ROCm/rocprofiler-compute/issues/435
state: closed | updated: 2025-08-06T18:24:30Z
labels: question, Under Investigation

## 正文

I have profiled an application like so:

```shell
$ omniperf profile -n <case_name> --device=0 -- ./test_binary
```

Now I want, for a given dispatch, draw some rooflines:
```shell
$ # Calling this does not help as it'll generate rooflines only 
$ # on the first dispatched kernel. Even though I specified a non zero dispatch index.
$ omniperf profile -n <case_name> --roof-only --kernel-names --mem-level HBM --dispatch 546 -- ./test_binary
```


## 评论 (13)

### coleramos425 · 2024-09-30

Can you please share what ROCm version you're using? Additionally, could you also attach your `log.txt` file that was generated from this run for debugging purposes.

### etiennemlb · 2024-10-01

I'm using rocm 5.5.1, 5.7.1, 6.1.2.

And, Omniperf 2.1.0

### sohaibnd · 2024-10-31

Hi @etiennemlb, sorry for the delay. Can you try updating to ROCm 6.2.2+Omniperf 2.1.0 and check if the issue is still present? I followed the options you used above and was able to get the roofline analysis for a non-zero dispatch id. 

Commands Used:
`omniperf profile --name ipc_wl2 --roof-only --kernel-names --mem-level HBM --dispatch 5 -- ./ipc`
`omniperf analyze -p workloads/ipc_wl2/MI200/ --gui`

Screenshot of [standalone GUI analyzer](https://rocm.docs.amd.com/projects/omniperf/en/latest/how-to/analyze/standalone-gui.html):
![image](https://github.com/user-attachments/assets/eae66944-ed37-4679-bdc7-d983e603c74c)
![image](https://github.com/user-attachments/assets/9b52f4cd-8f49-4e3a-a137-51d5fc104701)




### etiennemlb · 2024-11-01

In the profile command above, you explicitly tell omniperf to record only for --dispatch=5. 

This is different from me recording without --dispatch specified (and thus having on disk the roofline data of all the kernels) and later trying to draw a roofline for a specific kernel. Also I can't use graphana.

### sohaibnd · 2024-11-01

I'm not sure I understand what you mean. Are you not using these options in profile mode as well?

Also, how are you accessing the roofline plot? Are you using the generated pdf directly?

### etiennemlb · 2024-11-01

I'm using the pdf directly. In fact, using graphana on a super computer tend to be cumbersome.

TLDR; I want to recod a bunch of data, and then, later, analyze it or produce roofline out of it.

My workflow is as follow:

- I profile and gather the performance counters for all the kernels:
```shell
omniperf profile -n <case_name> --device=0 -- ./test_binary
``` 
- Then I want to generate view some metrics so I would do, say:
```shell
omniperf analyze --block 17.2.1 17.2.2 17.5.3 17.5.4 --dispatch 27 --path workloads/<case_name>/MI200/
```
- And then I would want to produce some roofline using the data collected earlier **without** having to profile all over again. This can be done like so:
```
omniperf profile -n <case_name> --roof-only --kernel-names --mem-level HBM --dispatch 0 -- ./test_binary
```

Now, if you try to reproduce that sequence of command you will find that for the last one, the --dispatch option is bugged. You can't choose a kernel other than 0 where as for the analyze command, I can freely choose whatever dispatch id I want.

As a side note, maybe the roofline generation should be in `analyze`.

### coleramos425 · 2024-11-01

@etiennemlb try using the [Standalone GUI](https://rocm.docs.amd.com/projects/omniperf/en/latest/how-to/analyze/standalone-gui.html) which can load roofline charts with your desired dispatch filter - no reprofile required. Based on your comment above, your usage should follow:

```console
$ omniperf analyze -p --path workloads/<case_name>/MI200/ --dispatch 27 --gui
```

I'll also add, knowing you're in an HPC environment, if your cluster doesn't allow port forwarding / ssh tunnel (required by standalone GUI), try copying data to your local workstation for analysis. For more info please read docs:
https://rocm.docs.amd.com/projects/omniperf/en/latest/how-to/analyze/standalone-gui.html

### sohaibnd · 2024-11-01

> I'm using the pdf directly. In fact, using graphana on a super computer tend to be cumbersome.
> 
> TLDR; I want to recod a bunch of data, and then, later, analyze it or produce roofline out of it.
> 
> My workflow is as follow:
> 
> * I profile and gather the performance counters for all the kernels:
> 
> ```shell
> omniperf profile -n <case_name> --device=0 -- ./test_binary
> ```
> 
> * Then I want to generate view some metrics so I would do, say:
> 
> ```shell
> omniperf analyze --block 17.2.1 17.2.2 17.5.3 17.5.4 --dispatch 27 --path workloads/<case_name>/MI200/
> ```
> 
> * And then I would want to produce some roofline using the data collected earlier **without** having to profile all over again. This can be done like so:
> 
> ```
> omniperf profile -n <case_name> --roof-only --kernel-names --mem-level HBM --dispatch 0 -- ./test_binary
> ```
> 
> Now, if you try to reproduce that sequence of command you will find that for the last one, the --dispatch option is bugged. You can't choose a kernel other than 0 where as for the analyze command, I can freely choose whatever dispatch id I want.
> 
> As a side note, maybe the roofline generation should be in `analyze`.

I see, so the `omniperf profile` command cannot be used to draw a roofline plot using data already collected. Omniperf's profile mode is only meant to collect the profiling results (it also does generate a pdf with the roofline plot using the data collected, but if you do not use kernel filtering during profiling it will include data from all kernels).

omniperf's analyze mode is used to view the metrics from data collected in profile mode. You can also generate a plot using the roofline data but you have to use the Standalone GUI analysis or Grafana GUI analysis.

The [Standalone GUI analysis](https://rocm.docs.amd.com/projects/omniperf/en/latest/how-to/analyze/standalone-gui.html) (which I have used above, not Grafana) is very easy to use, simply pass the --gui option in analyze mode as mentioned by @coleramos425 above. This will create a web server for you to access using your web browser.

### etiennemlb · 2024-11-01

@coleramos425 You guessed right about the ssh hurdles.
@sohaibnd the `--gui` only works if I can port forward which.. I can't. So its a no go.

So really, the only viable solution is about copying the profiling data to my personal computer.

Still, the only thing I need would be a way to generate the roofline PDFs for a given kernel after having recorded performance counters for all kernel.

I believe that would be a useful feature because we don't want to re-profile the whole program each time we want a roofline for a different kernel. This feature seems to already exist in the GUI, I would appreciate having the same capabilities built in the CLI.


### coleramos425 · 2024-11-01

> So really, the only viable solution is about copying the profiling data to my personal computer.

Correct.

> Still, the only thing I need would be a way to generate the roofline PDFs for a given kernel after having recorded performance counters for all kernel.

Agreed. I see the value add this feature could bring, especially for the HPC customers. @sohaibnd could you work with @etiennemlb to see about opening a proper feature request for this. Could be Jira or GitHub ticket - whichever you prefer (soon we'll have ability to link the two 🙂)

### gmarkomanolis · 2024-11-10

Hi, as I was on site for a hackathon and I was talking with @etiennemlb about this and some other requests, please point me to the internal ticket. Thanks. 

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/48

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
