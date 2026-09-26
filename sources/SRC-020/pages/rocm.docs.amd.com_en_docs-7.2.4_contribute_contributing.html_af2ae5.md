source: https://rocm.docs.amd.com/en/docs-7.2.4/contribute/contributing.html

# Contributing to ROCm documentation[#](https://rocm.docs.amd.com#contributing-to-rocm-documentation)

2026-05-25

2 min read time

ROCm documentation is open source and available on GitHub. You can contribute to ROCm documentation by cloning the appropriate repository, making your changes, and opening a pull request.

Note

To provide feedback on the ROCm documentation without contributing to it, see [Providing feedback about the ROCm documentation](https://rocm.docs.amd.com/feedback.html).

The documentation for ROCm and for all ROCm components is under their respective `docs`

folders. The `docs`

folders for all components across ROCm have the same structure:

Sub-folder name |
Documentation type |
|---|---|
|
Installation instructions, build instructions, and prerequisites |
|
Important concepts |
|
How to implement specific use cases |
|
Tutorials |
|
API references and other reference resources |
|
|

ROCm stack documentation differs from this structure.

Most documentation topics are written in [reStructuredText (rst)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html), with some topics written in Markdown. Only use reStructuredText when adding new topics. Only use Markdown if the topic you are editing is already in Markdown.

To edit or add to the documentation, first clone the appropriate repository, ensuring that you follow the repository recommendations as outlined in their respective README files:

Module |
Repository |
|---|---|
ROCm stack |
|
ROCm libraries |
|
ROCm systems projects |

Note

Individual components in the ROCm libraries and the ROCm systems projects repositories are located under the `projects`

folder. Some components have their own individual repositories. Each component has a link to its GitHub location from its documentation.

Cut a local branch from the `develop`

branch of the repository and make your changes. Your changes must adhere to the [Google developer documentation style guide](https://developers.google.com/style/highlights). If you’re adding a topic, provide a link to it from the `index.rst`

and `_toc.yaml.in`

files.

Build the documentation locally to verify your changes.

Note

If you’re making changes to the Doxygen comments within the source code, delete the `docs/doxygen/xml`

and `docs/doxygen/html`

folders between each build.

From within the `docs`

directory, run:

```
python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

The output will be saved to the `docs/_build`

folder. Open `docs/_build/html/index.html`

to view the documentation.

Note

If your build returns an error due to missing packages, run

`pip3 install -r sphinx/requirements.txt`


This command only needs to be run once.

Once you’ve verified your changes, push your branch and create a pull request. Your pull request will be reviewed by a member of the ROCm documentation team.

For information about how to clone a repository, or how to create and push a local branch, see the [GitHub documentation](https://docs.github.com/en).

For information about ROCm build tools, see [Documentation toolchain](https://rocm.docs.amd.com/toolchain.html).

Important

By creating a pull request (PR), you agree to allow your contribution to be licensed under the terms of the LICENSE.txt file in the corresponding repository. Different repositories can use different licenses.