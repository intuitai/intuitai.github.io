source "https://rubygems.org"

# Jekyll 4 rather than the github-pages gem: the site uses collection
# `sort_by`, which is a Jekyll 4 feature, and it is deployed by GitHub Actions
# rather than by Pages' own build, so the older pinned toolchain buys nothing.
gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-remote-theme", "~> 0.4"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jemoji", "~> 0.13"
end

# webrick left Ruby's standard library in 3.0; `jekyll serve` needs it back.
gem "webrick", "~> 1.8"

# Link and asset checking, run the same way locally and in CI:
#   bundle exec htmlproofer ./_site --disable-external --swap-urls "^/everyday-programming:"
group :test do
  gem "html-proofer", "~> 5.0"
end
