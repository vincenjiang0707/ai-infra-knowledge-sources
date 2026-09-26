source: https://github.com/vllm-project/guidellm/blob/main/Containerfile

-
[Notifications](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)You must be signed in to change notification settings -
[Fork 238](https://github.com/login?return_to=%2Fvllm-project%2Fguidellm)


## Expand file tree

/

Copy path# Containerfile

More file actions

97 lines (76 loc) · 3.08 KB

/

Copy path# Containerfile

## File metadata and controls

97 lines (76 loc) · 3.08 KB

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

ARG BASE_IMAGE=quay.io/fedora/python-313-minimal:latest

# Use a multi-stage build to create a lightweight production image

FROM $BASE_IMAGE as builder

# release: take the last version and add a post if build iteration

# candidate: increment to next minor, add 'rc' with build iteration

# nightly: increment to next minor, add 'a' with build iteration

# alpha: increment to next minor, add 'a' with build iteration

# dev: increment to next minor, add 'dev' with build iteration

ARG GUIDELLM_BUILD_TYPE=dev

# Extra dependencies to install

# all: install all extras

# recommended: install recommended extras

ARG GUIDELLM_BUILD_EXTRAS=all

# Switch to root for installing packages

USER root

# Install uv in a temporary venv

RUN /usr/bin/python3 -m venv /tmp/uv \

&& /tmp/uv/bin/pip install --no-cache-dir -U uv \

&& ln -s /tmp/uv/bin/uv /usr/local/bin/uv

# Install build dependencies

RUN --mount=type=cache,sharing=locked,target=/var/cache/dnf \

dnf install -y git

# Set correct build type for versioning

# Configure uv for building guidellm

ENV GUIDELLM_BUILD_TYPE=$GUIDELLM_BUILD_TYPE \

VIRTUAL_ENV=/opt/app-root \

UV_PROJECT="/src" \

UV_LINK_MODE="copy" \

UV_NO_DEV="1" \

UV_NO_EDITABLE="1" \

UV_FROZEN="1" \

UV_CACHE_DIR="/tmp/uv_cache"

# Sync initial environment

RUN --mount=type=cache,target=$UV_CACHE_DIR \

--mount=type=bind,source=uv.lock,target=$UV_PROJECT/uv.lock,relabel=shared \

--mount=type=bind,source=pyproject.toml,target=$UV_PROJECT/pyproject.toml,relabel=shared \

uv sync --active --no-install-project --extra $GUIDELLM_BUILD_EXTRAS

# Copy repository files

# Do this as late as possible to leverage layer caching

COPY / $UV_PROJECT

# Install guidellm

RUN --mount=type=cache,target=$UV_CACHE_DIR \

uv sync --active --extra $GUIDELLM_BUILD_EXTRAS

# Prod image

FROM $BASE_IMAGE

# Switch to root for installing packages

USER root

# Install some helpful utilities and deps

RUN --mount=type=cache,sharing=locked,target=/var/cache/dnf \

dnf install -y --setopt=install_weak_deps=False \

vi tar rsync ffmpeg-free

# Switch back to unpriv user

# Root group for k8s

USER 1001:0

# Add guidellm bin to PATH

# Change the default save directory for results

ENV HOME="/home/guidellm" \

GUIDELLM__DEFAULT_RESULTS_DIR="/results"

# Create the user home dir

WORKDIR $HOME

# Ensure that the user home dir can be used by any user

# (OpenShift Pods can't use the cache otherwise)

RUN chgrp -R 0 "$HOME" && chmod -R g=u "$HOME"

# Create a volume for results

VOLUME /results

# Metadata

LABEL io.k8s.display-name="GuideLLM" \

org.opencontainers.image.description="GuideLLM Performance Benchmarking Container" \

org.opencontainers.image.source="https://github.com/vllm-project/guidellm" \

org.opencontainers.image.documentation="https://blog.vllm.ai/guidellm/stable" \

org.opencontainers.image.license="Apache-2.0"

# Copy the virtual environment from the builder stage

# Do this as late as possible to leverage layer caching

COPY --chown=1001:0 --from=builder /opt/app-root /opt/app-root

ENTRYPOINT [ "/opt/app-root/bin/guidellm" ]

CMD [ "run" ]