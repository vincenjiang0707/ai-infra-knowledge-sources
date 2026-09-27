# [Issue #405] Setting up Grafana on MacOS

source: https://github.com/ROCm/rocprofiler-compute/issues/405
state: closed | updated: 2025-08-06T18:26:04Z
labels: question, Under Investigation

## 正文

Hello, 

I have been following the documentation to get Grafana working with Omniperf profiles, and am currently stuck on this step of the installation phase - https://rocm.github.io/omniperf/installation.html#build-and-launch

I receive the following error on MacOS. Is the Grafana interface expected to work on MacOS?

```
/Applications/omniperf-2.0.1/grafana sharmaas@HPE-C77H3JMHJP% sudo docker-compose build
Password:
WARN[0000] /Applications/omniperf-2.0.1/grafana/docker-compose.yml: `version` is obsolete
[+] Building 0.3s (1/2)                                                                                                                                                                                                       docker:desktop-linux
[+] Building 0.4s (2/2) FINISHED                                                                                                                                                                                              docker:desktop-linux
 => [web internal] load build definition from Dockerfile                                                                                                                                                                                      0.0s
 => => transferring dockerfile: 3.22kB                                                                                                                                                                                                        0.0s
 => ERROR [web internal] load metadata for docker.io/library/ubuntu:22.04                                                                                                                                                                     0.3s
------
 > [web internal] load metadata for docker.io/library/ubuntu:22.04:
------
failed to solve: ubuntu:22.04: failed to resolve source metadata for docker.io/library/ubuntu:22.04: error getting credentials - err: exit status 1, out: ``
```


## 评论 (11)

### nartmada · 2024-08-13

Internal ticket has been created to track this issue.

### ashesh2512 · 2024-09-04

@nartmada Any further developments on this?

### feizheng10 · 2024-09-05

May we know any specific reason you'd like to setup Grafana on MacOS? Would you consider the standalone GUI?

### ashesh2512 · 2024-09-05

> May we know any specific reason you'd like to setup Grafana on MacOS? Would you consider the standalone GUI?

MacOS is what me and most of my colleagues use. I am not sure what you mean by the standalone GUI. Are you referring to the web browser? My understanding is that Grafana can provide a much more interactive experience such as choosing the normalization options as well as baseline comparison. Additionally, please correct me if I am wrong, but to run the web browser, I need to have Omniperf installed, which is not possible on the latest Mac systems. And browsing web on remote clusters is very inefficient more often than not.

To be clear, I do not expect to run an omniperf profile on Mac. I want to run a GUI that can analyze a profile copied over from a remote Linux cluster where the application is usually run. I am trying to achieve a workflow similar to Nsight Compute GUI.

### feizheng10 · 2024-09-05

> > May we know any specific reason you'd like to setup Grafana on MacOS? Would you consider the standalone GUI?
> 
> MacOS is what me and most of my colleagues use. I am not sure what you mean by the standalone GUI. Are you referring to the web browser? My understanding is that Grafana can provide a much more interactive experience such as choosing the normalization options as well as baseline comparison. Additionally, please correct me if I am wrong, but to run the web browser, I need to have Omniperf installed, which is not possible on the latest Mac systems. And browsing web on remote clusters is very inefficient more often than not.
> 
> To be clear, I do not expect to run an omniperf profile on Mac. I want to run a GUI that can analyze a profile copied over from a remote Linux cluster where the application is usually run. I am trying to achieve a workflow similar to Nsight Compute GUI.

Right, the web browser one. "the standalone GUI", I mean omniperf --gui.
Technically, all what Grafana GUI provide we should be able to provide in the standalone GUI, and even better.
Right now, for sure the standalone GUI is not good as the Grafana one. We are working on improving it.

I totally understand your workflow: copy data back to local, and just do post-analysis locally. Personally, I have no chance to try it on Mac yet.
May I know any difficulty to block you install Omniperf on Mac? So far, my understanding would be: Omniperf post-analysis part only has a few python 3rd party dependency.   

### feizheng10 · 2024-09-05

BTW, both "choosing the normalization" and "baseline comparison" can be done in CLI as well. We are trying to improve the visualization on CLI to catch up GUI. Let us know if your team expects more interactive mode in CLI. 

### ashesh2512 · 2024-09-06

> I totally understand your workflow: copy data back to local, and just do post-analysis locally. Personally, I have no chance to try it on Mac yet.

Please allow me to rephrase my original issue/question. Is the Grafana/MongoDB workflow supported for MacOS?

### coleramos425 · 2024-09-09

@ashesh2512 the Grafana/MongoDB workflow is only officially supported, and tested, on Linux. That being said, since the Grafana/MongoDB workflow is 100% containerized via Docker, it shouldn't make a difference what OS you use to launch the instance.

Revisiting your original logs, it seems to me like your error is instead related to your Docker credentials:

> ```shell
> /Applications/omniperf-2.0.1/grafana sharmaas@HPE-C77H3JMHJP% sudo docker-compose build
> Password:
> WARN[0000] /Applications/omniperf-2.0.1/grafana/docker-compose.yml: `version` is obsolete
> [+] Building 0.3s (1/2)                                                                                                                                                                                                       docker:desktop-linux
> [+] Building 0.4s (2/2) FINISHED                                                                                                                                                                                              docker:desktop-linux
>  => [web internal] load build definition from Dockerfile                                                                                                                                                                                      0.0s
>  => => transferring dockerfile: 3.22kB                                                                                                                                                                                                        0.0s
>  => ERROR [web internal] load metadata for docker.io/library/ubuntu:22.04                                                                                                                                                                     0.3s
> ------
>  > [web internal] load metadata for docker.io/library/ubuntu:22.04:
> ------
> failed to solve: ubuntu:22.04: failed to resolve source metadata for docker.io/library/ubuntu:22.04: error getting credentials - err: exit status 1, out: ``
> ```

Omniperf uses `ubuntu:22.04` as base image for our container, and your Docker installation logs seem to indicate Docker is failing to validate your credentials on that pull. My suggestion would be to do some debugging around this...

### ashesh2512 · 2024-09-29

> May I know any difficulty to block you install Omniperf on Mac? So far, my understanding would be: Omniperf post-analysis part only has a few python 3rd party dependency.

Doesn't omniperf require ROCm for installation? https://rocm.docs.amd.com/projects/omniperf/en/latest/install/core-install.html#core-installation

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/50

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
