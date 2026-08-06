source "https://rubygems.org"

# Jekyll 4 rather than the github-pages gem: the site uses collection
# `sort_by`, which is a Jekyll 4 feature, and it is deployed by GitHub Actions
# rather than by Pages' own build, so the older pinned toolchain buys nothing.
#
# `~> 4.3` is a floor, not a pin: it admits any 4.x from 4.3 up, and
# Gemfile.lock currently resolves it to 4.4.1. Do not "correct" this to the
# resolved version -- narrowing the constraint forces bundler to re-resolve,
# and CI installs from the committed lock.
gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-remote-theme", "~> 0.4"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jemoji", "~> 0.13"
end

# webrick left Ruby's standard library in 3.0; `jekyll serve` needs it back.
gem "webrick", "~> 1.8"

# Link and asset checking, run the same way locally and in CI. The exact
# invocation lives in .github/workflows/pages.yml and in README.md; run it
# from there rather than from memory.
group :test do
  gem "html-proofer", "~> 5.0"
end
