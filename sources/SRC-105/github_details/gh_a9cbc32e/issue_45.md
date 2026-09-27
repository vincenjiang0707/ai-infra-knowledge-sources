# [Issue #45] Dockerfile for ROCm + Omniperf (and more)

source: https://github.com/ROCm/rocprofiler-compute/issues/45
state: closed | updated: 2025-01-16T08:52:34Z
labels: 

## 正文

Hi again,

Sorry, first of all, if this is the wrong place to post this.

I genuinely wonder whether AMDResearch would be willing to maintain a Dockerfile that ships the following components:

* ROCm
* ROCm-aware MPI
* Omnitrace
* Omniperf

As a developer, this would significantly ease my (our, at @devitocodes/devito) life . At the same time, I think this would greatly benefit your users. Ultimately ROCm-aware MPI, Omnitrace and Omniperf will be part of the ROCm suite, I'm sure, but it feels like it's still a long way to go. Interested in your thoughts.

Here's our Dockerfile :

https://github.com/devitocodes/devito/blob/d4e9dc36ff92299644aada824f0ec3786d2f9fef/docker/Dockerfile.amd

The link above is from a PR, but you get the idea. We test it on CI so we know it does work (aside from MPI which still needs to be refreshed).

Apologies again I know this might not be the best place to have this discussion but happy to delete and move if you have a better place (or remove if not interested -- not a problem!)

EDIT: Just to clarify: basically, I'm wondering whether it would make sense to lift that Dockerfile from our codebase somewhere into one of yours 

## 评论 (10)

### jrmadsen · 2022-12-09

From the omnitrace perspective, I am considering streamlining installation of a pre-built binary with a `omnitrace-docker-install.sh` script _that is a part of the release_, which, from your perspective, would look something like:

```docker
ARG OMNITRACE_VERSION=latest

RUN wget https://github.com/AMDResearch/omnitrace/releases/download/${OMNITRACE_VERSION}/omnitrace-docker-install.sh && \
    chmod +x ./omnitrace-docker-install.sh && \
    ./omnitrace-docker-install.sh && \
    rm ./omnitrace-docker-install.sh
```

And the script would just be something like:

```bash
OS_DISTRIB=$(cat /etc/os-release | grep '^ID=' | sed -r 's/=/ /g' | awk '{print $NF}')
OS_VERSION=$(cat /etc/os-release | grep '^VERSION_ID=' | sed -r 's/[="]/ /g' | awk '{print $NF}')
for i in version version-dev version-hip-libraries version-hip-sdk
do
    if [ -f /opt/rocm/.info/${i} ]; then
        ROCM_VERSION=$(cat /opt/rocm/.info/${i} | sed -r 's/[\.-]/ /g' | awk '{print 10000*$1+100*$2}')
        break
    fi
done
OMNITRACE_INSTALL_SCRIPT=omnitrace-@OMNITRACE_VERSION@-${OS_DISTRIB}-${OS_VERSION}-ROCm-${ROCM_VERSION}-PAPI-OMPT-Python3.sh

wget -O ./omnitrace-install.sh https://github.com/AMDResearch/omnitrace/releases/download/v@OMNITRACE_VERSION@/${OMNITRACE_INSTALL_SCRIPT}
chmod +x ./${OMNITRACE_INSTALL_SCRIPT}
mkdir -p ${OMNITRACE_INSTALL_DIR}
./${OMNITRACE_INSTALL_SCRIPT} --prefix=${OMNITRACE_INSTALL_DIR} --skip-license --exclude-subdir
rm ./${OMNITRACE_INSTALL_SCRIPT}
```

where `@OMNITRACE_VERSION@` is encoded directly (since this will be directly tied to the `omnitrace-docker-install.sh` script in that release).



### jrmadsen · 2022-12-09

Actually, I will probably just call it `omnitrace-install.sh` since this will work outside of docker too.

### FabioLuporini · 2022-12-12

That would be perfect for us!


### jrmadsen · 2022-12-14

@FabioLuporini See https://github.com/AMDResearch/omnitrace/pull/221. It got complicated enough that I used python instead of bash so while that _may_ require installing python in the container, the python script uses only standard libraries so at least it doesn't require any pip installs.

### FabioLuporini · 2022-12-14

Thanks. That's completely fine for us, we apt-get-install python anyway :)

### FabioLuporini · 2023-04-23

Hi, I see a docker folder now. And an amdgpu.deb package for ubuntu? 

### coleramos425 · 2023-04-25

That's right @FabioLuporini. The docker folder contains the 3 images we use for our CI testing. One per supported distro: SLES 15, Ubuntu 20.04, and RHEL 8.

I'm not sure if that's what you're looking for. It satisfies your ROCm requirement, but MPI, Omniperf, and Omnitrace would need to be added. Pretty easy tweak if you wanted to put that in (probably 3-5 lines of code in Dockerfile)

I'm not sure the Omniperf repo would be the place for such a Dockerfile, but if you submit a PR perhaps we could find a place to host it elsewhere. Hope this helps!

### FabioLuporini · 2023-04-26

Gotcha, thanks!

This is how we install ROCm + MPI: https://github.com/devitocodes/devito/blob/master/docker/Dockerfile.amd 
And here's a relatively old PR that attempts to add Omniperf and Omnitrace to our `Dockerfile.amd` https://github.com/devitocodes/devito/pull/2032/files (note that the `Dockerfile.amd` in this PR is fairly older than that linked above)

I must review the Omni* installation instructions to see if anything has changed. One of the reasons I never really completed the PR above is that Omni* is a fast-moving project (which is great!), and perhaps installation instructions would change as well, and I was not particularly willing to maintain that 

### ppanchad-amd · 2025-01-15

Hi @FabioLuporini. Please let us know if we can go ahead and close this ticket. Thanks!

### FabioLuporini · 2025-01-16

Hey, yes I think this can now be closed. Thanks!
