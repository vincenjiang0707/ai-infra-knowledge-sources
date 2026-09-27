from . import github, gh_org, site, sitemap, hf, menu, js, blog

HANDLERS = {
    'github_repo': github.run,
    'site': site.run,
    'reference': site.run,
    'github_org': gh_org.run,
    'hf': hf.run,
    'academic': site.run,
    'js': js.run,
    'blog': blog.run,
}
