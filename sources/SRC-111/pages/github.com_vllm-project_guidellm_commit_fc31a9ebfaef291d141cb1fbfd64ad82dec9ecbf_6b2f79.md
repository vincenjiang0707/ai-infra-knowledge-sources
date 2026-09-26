source: https://github.com/vllm-project/guidellm/commit/fc31a9ebfaef291d141cb1fbfd64ad82dec9ecbf

1 parent 9747d65 commit fc31a9eCopy full SHA for fc31a9e

1 file changed

src/guidellm/settings.py

@@ -31,8 +31,8 @@ class Environment(str, Enum):

31


32

33

ENV_REPORT_MAPPING = {

34

- Environment.PROD: "https://raw.githubusercontent.com/vllm-project/guidellm/refs/heads/gh-pages/ui/v0.6.0/index.html",

35

- Environment.STAGING: "https://raw.githubusercontent.com/vllm-project/guidellm/refs/heads/gh-pages/ui/release/v0.6.0/index.html",

+ Environment.PROD: "https://raw.githubusercontent.com/vllm-project/guidellm/refs/heads/gh-pages/ui/v0.5.3/index.html",

+ Environment.STAGING: "https://raw.githubusercontent.com/vllm-project/guidellm/refs/heads/gh-pages/ui/release/v0.4.0/index.html",

36

Environment.DEV: "https://raw.githubusercontent.com/vllm-project/guidellm/refs/heads/gh-pages/ui/dev/index.html",

37

Environment.LOCAL: "http://localhost:3000/index.html",

38

}

## 0 commit comments