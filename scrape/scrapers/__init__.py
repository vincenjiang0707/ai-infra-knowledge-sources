from . import github, site, sitemap, hf, menu, js, blog

HANDLERS = {
    'github_repo': github.run,
    'site': site.run,
    'reference': site.run,
    'github_org': site.run,
    'hf': hf.run,
    'academic': site.run,
    'js': js.run,
    'blog': blog.run,
}
