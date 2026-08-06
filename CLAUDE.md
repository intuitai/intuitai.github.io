# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## What this repository is

The source of intuitai.org, the website of **IntuitAI, a research-driven
venture studio incubating startups in agentic and multi-agent AI**. It is a
small Jekyll site rendered end to end through the `sighingnow/jekyll-gitbook`
remote theme.

| Path | What it is |
|---|---|
| `/` | The landing page (`index.html`) — thesis, incubation model, portfolio, contact |
| `/ml-powered-text-recovery.html` | A research note (`_research/`) |

Two pages of prose. Two more things are served and are easy to forget:
`resource/` (a DOCX and a PDF, copied through verbatim, linked from no page,
with the PDF in the sitemap) and the theme's generated `assets/search.html`,
which a `defaults` entry in `_config.yml` marks `noindex` and keeps out of the
sitemap.

### What was removed, and what that means for stale comments

Until August 2026 this domain also hosted two books — *Everyday Programming* at
`/ep/` and *Everyday AI* at `/eai/` — with four collections, three Python
generators reading LaTeX manuscripts, 445 generated exercise pages, committed
PDFs and covers, and two `Book` branches in the JSON-LD. **All of it is gone**,
along with the organization's previous description of itself as a non-profit.

Consequences:

- Any comment, in any file, that mentions `/ep/`, `/eai/`, `_book/`,
  `_eaibook/`, `_exercises/`, `_solutions/`, `tools/`, `site.data.toc`,
  Intramotev Press, or IntuitAI as a non-profit is **stale**. Fix it or delete
  it; do not preserve it out of caution.
- Git history still contains all of it, so nothing is lost by deleting a
  reference rather than updating it.

## Editing the pages

- **Do not open a page's content with an `<h1>`.** The theme's `body.html`
  already emits `<h1>{{ page.title }}</h1>`; a second one gives the page two.
- **Section headings must be `h2`.** `_config.yml` caps the sidebar's in-page
  contents at level 2, so demoting a section to `h3` removes it from the
  navigation. `index.html` sets explicit `id`s because Jekyll does not run
  kramdown's `auto_ids` over `.html` files.
- Styling comes from the theme plus **`styles/site.css`**, loaded site-wide via
  `extra_css`. Reuse its `.ia-*` classes rather than adding stylesheets.
  - The file must **not** move under `assets/`. `jekyll-remote-theme` copies the
    theme's own `assets/` tree into `_site/assets/`, and mixing site files into
    that tree is the collision `_config.yml` warns about.
  - Every length is in `em`, never `rem`. GitBook sets `html{font-size:62.5%}`,
    making 1rem ten pixels rather than sixteen; anything in `rem` renders at
    about five-eighths its intended size.
  - The path was `ep/assets/css/site.css` and the prefix was `ep-`, from the
    first book. Both were renamed in August 2026.
- There is **no site JavaScript of our own.** Anything under `assets/gitbook/`
  comes from the remote theme — do not edit it, shadow the include instead.
- The **Flaticon credit** at the bottom of `index.html` is a licence condition
  on `img/neural.png`, not decoration. The theme's `footer.html` emits scripts
  and nothing visible, so the credit lives in page content. Do not drop it
  while that logo is in use.

### Why `_research/` is a collection

The gitbook sidebar is built by `toc-date.html` walking `ordered_collections`
and printing each page's title. With no collection at all it renders as a lone
link back to the site root, which reads as broken. The write-up therefore lives
in a collection, and keeps its original `/ml-powered-text-recovery.html` URL
through a **page-level `permalink`**, which overrides the collection's.

Keep Liquid comment blocks in a collection document **free of blank lines**:
Jekyll cuts a document's excerpt at the first `\n\n`, and a break inside a
Liquid block makes it warn on every build that it had to close the tag for you.

## The project list is the load-bearing part

`index.html` and `README.md` list all thirteen of the studio's repositories
with a maturity label. **The labels are the point.** Four of them — `oculon`,
`cogmux`, `agentic-workflow`, `quranllm` — are a README and a thesis, not a
working system, and are tagged *Design stage*; their prose is deliberately
written in the conditional ("the thread:", "planned:", "there is nothing here
to install") so that the paragraph agrees with the tag. Before promoting one,
read the repository. An investor who clicks a paragraph of capabilities through
to an empty repo has learned something about the studio, not about the project.

The JSON-LD lists **only four projects and carries no maturity property at
all** — marking a design-stage repository up as `SoftwareSourceCode` with a
capability description would tell a crawler more than the repository supports.
That asymmetry between the page and the markup is deliberate; do not "fix" it
by adding the other nine.

All thirteen are Apache-2.0 by GitHub's own detection, including
`resilience4py`, whose README badge says MIT — the badge is the stale artefact,
its `LICENSE` file is Apache. The facts strip near the top of `index.html`
asserts *13 repositories*, *9 with working code* and *licence on all 13*; every
one of those is countable from the list below it, and must stay that way.

**The repositories are under `github.com/nobelk`, not `github.com/intuitai`.**
The organization holds only this site, its `.github` profile repo, and a
private `research` repo. The old landing page linked to
`github.com/intuitai/model-gateway`, `.../quranllm` and
`.../random-number-mcp-server`, all of which 404 — `reverb` and `tangle`
resolved only through GitHub's rename redirect to `nobelk/*`. CI never caught
it because html-proofer runs with `--disable-external`. **If you add an
off-site link, open it yourself.** If the repositories are ever moved under the
organization, update `index.html`, `_includes/structured-data.html` and
`README.md` together.

## Commands

```console
$ bundle install
$ bundle exec jekyll serve            # http://localhost:4000/
$ bundle exec jekyll build
```

The one check that matters, run identically here and in CI:

```console
$ bundle exec htmlproofer ./_site --disable-external --allow-hash-href \
    --no-ignore-empty-alt --ignore-files "/assets\/search\.html/"
```

There is no test suite, no linter, and no package manager beyond Bundler.
`assets/search.html` is excluded because the theme generates it with
`<a href=".">`, which resolves to a directory with no index — an upstream bug
in `sighingnow/jekyll-gitbook`.

## Deployment

`.github/workflows/pages.yml` builds and publishes on every push to `main`.
Deployment is **by Actions, not by Pages' built-in Jekyll**, for two reasons,
both downstream of the built-in build pinning the `github-pages` gem
(Jekyll 3.10 at the time of writing): collection `sort_by` is a Jekyll 4
feature and would be silently ignored, and there is nowhere in the built-in build to run html-proofer as a
gate. **`jekyll-remote-theme` is not one of the reasons** — Pages supports it,
and this file claimed otherwise for a year.

No `--baseurl` override is passed: intuitai.org is an apex custom domain served
from the root, and `_config.yml`'s empty `baseurl` is already correct. Setting
it would make every stylesheet URL the theme emits carry the prefix, so the CSS
would be requested from a path that 404s.

## Theme overrides

Four files shadow same-named files in the remote theme. **Every one is a
copy-and-diverge; diff each against upstream when the theme updates.** Three
are described under SEO below; the fourth is:

- **`_layouts/post.html`** — copied verbatim from upstream and changed in
  exactly two places, both marked `INTUITAI`. Upstream's prev-page fallback
  assumes no page is ever the site root, so when `page.previous` is empty it
  emits `rel="prev"` and a visible back-arrow pointing at `{{site.baseurl}}/`
  — which, on the landing page, is the page you are already on. Both are
  suppressed when `page.url == "/"`. Shadowing a *layout* rather than an
  include is a heavier commitment than the others; it was taken because a
  self-linking navigation control sits on the one page investors land on.

## SEO

Two shadowed includes carry the whole SEO layer, overriding same-named files in
the remote theme — the same trick `mathjax.html` uses:

- **`_includes/head.html`** — the upstream version emits one
  `<meta name="description">` containing `site.description`, identically on
  every page, and nothing else. The override reproduces everything upstream
  emits (stylesheet list included — **diff this against the theme when it
  updates**) and adds per-page description, canonical, Open Graph, Twitter
  card, robots, and the analytics tag.
- **`_includes/structured-data.html`** — JSON-LD, branched by page: an
  `Organization` (with `contactPoint`s for the investor and business-development
  routes the page advertises) + `Person` + `WebSite` + `WebPage` + four
  `SoftwareSourceCode` nodes on `/`, an `Article` plus breadcrumbs on research
  pages. Each project's `author` is the **founder** and its `producer` is the
  organization — the repositories sit under a personal account, and naming
  IntuitAI as `author` asserted something the linked page contradicts.

  Two rules, both inherited from the version that described two books:

  1. **Every `@id` a page references must be defined on that same page.**
     Consumers resolve `@id` within a document, not across documents, so a bare
     `{"@id": "..."}` member pointing elsewhere is inert — a node with no
     `@type` and no properties is dropped.
  2. **Markup must agree with what the reader sees.** The organization is
     described here as a venture studio because that is what the landing page
     says in prose. Both said "non-profit" until August 2026.

  The four project nodes are a deliberate subset of the thirteen on the page:
  marking a design-stage repository up as `SoftwareSourceCode` with a
  capability description would tell a crawler more than the repository
  supports.

Front matter a page can set, all optional:

| Key | Effect |
|---|---|
| `description` | The meta/OG/Twitter description. Falls back to the page excerpt, then `site.description`. |
| `seo_title` | Overrides `<title>` only. The landing page's `<h1>` is "IntuitAI", which alone is useless in a results page. |
| `image` / `image_alt` | Share image. Defaults to the logo. |
| `og_type` | Defaults to `article` for collection pages, `website` otherwise. |
| `order` | Sidebar sort key within a collection. |
| `twitter_card` | Defaults to `summary`. The default share image is a 512×512 logo, and `summary_large_image` is built for 2:1 — it crops or letterboxes a square. Only set it with a genuinely wide image. |
| `noindex` | Emits `noindex, follow` instead of the indexable robots tags. Set through `defaults` for `assets/search.html`. |
| `date_published` | If set, emitted as `datePublished` in a research page's JSON-LD. **Deliberately not `date`:** Jekyll gives every collection document a `date` whether or not its front matter has one, falling back to the file's mtime — so a `{% if page.date %}` guard never fails and quietly published the *build timestamp* as the article's publication date on every deploy. |

**Keep `seo_title` under ~60 characters and `description` under ~160.**
`head.html` truncates descriptions at 300 as a backstop, but search engines cut
around 155–160 — the first draft of the landing page shipped an 89-character
title and a 358-character description that rendered ending mid-word in
"implementa...". Front-matter comments must be YAML `#` comments: Jekyll parses
front matter as YAML *before* Liquid runs, so a `{% comment %}` block up there
is a syntax error, not a comment.

Analytics is `site.google_analytics` in `_config.yml` and is emitted **only
when `JEKYLL_ENV=production`**, so a local `jekyll serve` never reports into
the real property.

`robots.txt` is deliberately front-matter-free so Jekyll copies it verbatim;
its sitemap URL is therefore hardcoded rather than built from `site.url`.

## Note on README.md

`README.md` covers the same architecture, commands and deployment path as this
file, aimed at a contributor rather than an agent. **Keep the two in step when
either changes.** The organization's GitHub profile — a third copy of the
project list and the thesis — lives in a separate repository,
`intuitai/.github`, at `profile/README.md`; keep that in step too.

When something here disagrees with a source file, trust the comments in
`_config.yml`, `Gemfile` and `pages.yml` — they sit next to what they describe
and rot more slowly.
