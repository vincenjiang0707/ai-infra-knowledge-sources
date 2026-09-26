source: https://github.com/vllm-project/vllm-project.github.io

- Install
`jekyll`

and`bundler`

by running`gem install jekyll bundler`

. Ask ChatGPT for help if you encounter any issues. `bundle install`

to install the necessary gems.`rm ./Gemfile.lock`

if you meet gem error.`bundle exec jekyll server`

to compile and start the server.

To add a new blogpost, please refer to `_posts/2023-06-20-vllm.md`

as an example. Some notes:

- Google Doc can be saved as markdown format which will make your life easier.
- Note that the blogpost will only show when its date is in the past.
- Add
`summary`

front matter for SEO. Keep it concise, specific, and 240 characters or fewer. - Put figures under
`assets/figures/yourblogname/`

. - Make a pull request.

The blog is automatically built and deployed by GitHub Actions when `main`

is pushed to.

The blog supports LaTeX math via [MathJax](https://docs.mathjax.org/en/latest/index.html).

It can be enabled by adding `math: true`

to the document frontmatter. It has been configured to support the standard LaTeX style math notation, i.e.:

`$ inline math $`

```
$$
math block
$$
```

The blog supports GitHub flavored admonitions via [jekyll-gfm-admonition](https://github.com/Helveg/jekyll-gfm-admonitions). It supports the following syntax:

```
> [!NOTE]
> Highlights information that users should take into account, even when skimming.
> And supports multi-line text.
> [!TIP]
> Optional information to help a user be more successful.
> [!IMPORTANT]
> Crucial information necessary for users to succeed.
> [!WARNING]
> Critical content demanding immediate
> user attention due to potential risks.
> [!CAUTION]
> Negative potential consequences of an action.
> Opportunity to provide more context.
```

The theme we are using is [Minima](https://github.com/jekyll/minima). If you need to customise anything from this theme, see [Overriding theme defaults](https://jekyllrb.com/docs/themes/#overriding-theme-defaults).