# [Issue #418] Provide Grafana + Omniperf plugin as Docker image in a public registry like Dockerhub

source: https://github.com/ROCm/rocprofiler-compute/issues/418
state: closed | updated: 2025-08-06T18:25:39Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
no

**Describe the solution you'd like**
I would like do be able to pull an image of grafana with the omniperf plug-in so can I can `docker pull omniperf-grafana` as an example.

**Describe alternatives you've considered**
Currently I am using the Dockerfile provided in the repo 
in https://github.com/ROCm/omniperf/blob/amd-staging/grafana/Dockerfile
However, I need to modify it to add my secret sauce, which makes it more difficult to maintain.

**Additional context**
Currently other omniperf images are being hosted under Mr. Ramos account at
https://hub.docker.com/u/colramos  


## 评论 (11)

### coleramos425 · 2024-08-29

This should be a straightforward task. I'll need to confirm with the project PM to sign off on publishing this container. Expect an update shortly...

### ELCapitanLLNL · 2024-10-01

hi @coleramos425 , any update on this straightforward task?  thank you!

### coleramos425 · 2024-10-01

CC: @njobypet 

For approval on container publishing

### njobypet · 2024-10-01

grafana with the omniperf plug-in is a good idea. Can we use Rocprof-compute instead of Omniperf ?

### coleramos425 · 2024-10-02

> grafana with the omniperf plug-in is a good idea. Can we use Rocprof-compute instead of Omniperf ?

Yes we can, we'll just need to wait for #428 to merge. @njobypet I am creating a subtask in Xuan's PR to make sure this is included.

### njobypet · 2024-10-03

@coleramos425 , Please check grafana licensing requirements as well. Just to ensure that we are good to re-distribute. 

### coleramos425 · 2024-10-03

Unfortunately, that's outside of my domain @njobypet. You'll need to reach out to the legal team. Licencing info can be found [here](https://github.com/ROCm/omniperf/tree/amd-staging/grafana/plugins/omniperf_plugin). I'll note that in Xuan's ticket.

### ELCapitanLLNL · 2024-11-25

Happy Monday!  
Any update on this now that the rename happened.
Thanks! 

### coleramos425 · 2024-11-25

> Happy Monday! Any update on this now that the rename happened. Thanks!

CC: @njobypet 

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/51

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
