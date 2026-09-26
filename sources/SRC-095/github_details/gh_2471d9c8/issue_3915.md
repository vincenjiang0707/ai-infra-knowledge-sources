# [Issue #3915] [Feature] Python Client PyPi Distribution

source: https://github.com/ray-project/kuberay/issues/3915
state: open | updated: 2026-09-22T16:56:10Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Currently a user needs to utilise the Kuberay Git repository, and do a generic `pip install -e .` to install the python client. There already exists a pyproject.toml file in the python_client, so build and pushing to PyPi would be an easy enough task. This issue covers the naming (maybe kuberay-client?) and publication to PyPi.
 of what isn now the `python-client`.

This would provide a much better user experience as they can just do a `pip install kuberay_client`and include it as a dep for their python application. 

### Use case

I want to utilize the python client to create RayClusters / RayJobs inside another python application. To do this neatly, I want to pip install the python client instead of interacting directly with the git repository.

### Related issues

#3829

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (6)

### Future-Outlier · 2025-10-11

cc @kevin85421 
need your help!

### kryanbeane · 2025-12-01

Hey @Future-Outlier @kevin85421 @andrewsykim, sorry for the group ping. Wondering if any of you guys know if the PyPi repo was accepted? We consume it in our SDK, but since it's not released we have to vendor the python client which isn't ideal. I'm happy to work closely with ye to manage releaes of that, although we don't change it often so I would think an initial release would do us for the time being

### Future-Outlier · 2025-12-06

Hi, @kryanbeane 
I'll follow up the progress, thank you!

### roelschr · 2025-12-16

Would be really nice to have this published. I'm also willing to help if needed.

### Future-Outlier · 2025-12-16

I'll follow up this with a maintainer tmr, thank you all

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
