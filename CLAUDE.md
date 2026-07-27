# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## One site, one theme

intuitai.org is a single Jekyll site. **Every page renders through the
`sighingnow/jekyll-gitbook` remote theme**, including the landing page.

| Path | What it is |
|---|---|
| `/` | The IntuitAI landing page (`index.html`) |
| `/ml-powered-text-recovery.html` | Project write-up |
| `/ep/` | *Everyday Programming*, a book site, from generated Markdown |

This was not always true, and the older comments in `_config.yml` still describe
the previous arrangement. Until July 2026 the landing page and the project page
were hand-written HTML on CDN-hosted Pico.css with **no front matter**, which
made Jekyll copy them through byte-for-byte; the book was the only themed part
of the domain. Both pages now carry front matter and `layout: post`, so they get
the theme's chrome and the book's left sidebar. Pico.css is gone from the site
entirely.

Consequences worth knowing before editing either page:

- **Do not open a page's content with an `<h1>`.** The theme's `body.html`
  already emits `<h1>{{ page.title }}</h1>`; a second one gives the page two.
- Content is styled by the theme plus `ep/assets/css/site.css`, which is loaded
  site-wide via `extra_css`. Reuse its `.ep-*` classes rather than adding
  stylesheets.
- `js/minimal-theme-switcher.js` and `js/modal.js` are **dead code**. They were
  Pico.css utilities; nothing references them now, and the theme supplies its
  own font/theme controls.
- The Flaticon credit at the bottom of `index.html` is a **licence condition**
  on `img/neural.png`, not decoration. The theme's `footer.html` emits scripts
  and nothing visible, so the credit lives in page content. Do not drop it while
  that logo is in use.

## Commands

```console
$ bundle install
$ bundle exec jekyll serve            # http://localhost:4000/  (whole domain)
$ bundle exec jekyll build
```

The one check that matters, run identically here and in CI:

```console
$ bundle exec htmlproofer ./_site --disable-external --allow-hash-href \
    --no-ignore-empty-alt --ignore-files "/assets\/search\.html/"
```

There is no test suite, no linter, and no package manager beyond Bundler.
html-proofer is the only gate, and it covers the landing page too — so a broken
image path in hand-written HTML fails the deploy rather than reaching
production.

To regenerate the book's pages from the LaTeX manuscript (both scripts default
`--manuscript` to `../manuscripts/everyday-programming` and `--site` to `.`):

```console
$ ./tools/extract_exercises.py --manuscript ../manuscripts/everyday-programming
$ ./tools/generate_toc.py      --manuscript ../manuscripts/everyday-programming
```

The manuscript lives outside this repository. Without it, the generators cannot
run — but the generated output is committed, so the site builds fine without it.

## Deployment

`.github/workflows/pages.yml` builds and publishes on every push to `main`.
Deployment is **by Actions, not by Pages' built-in Jekyll**, which supports
neither collection `sort_by` nor `jekyll-remote-theme` — hence Jekyll 4 in the
`Gemfile` rather than the pinned `github-pages` gem. The workflow builds the
whole domain, so **a red run means intuitai.org stops updating, not just the
book.**

No `--baseurl` override is passed: intuitai.org is an apex custom domain served
from the root, and `_config.yml`'s empty `baseurl` is already correct.

## The book at /ep/ — read before touching

- `_exercises/`, `_solutions/`, `_data/toc.yml`, `_data/downloads.yml` and
  `ep/assets/code/` are **generated** by `tools/extract_exercises.py` and
  `tools/generate_toc.py`. Never hand-edit them; fix the manuscript and re-run.
- **`_book/` is hand-written prose and is safe to edit** — the pitch, contents,
  sample, exercises intro, author and errata pages. It only *reads* generated
  data (`site.data.toc`, `site.data.downloads`). Earlier versions of this file
  wrongly listed `_book/` as generated; the generators never write it.
  `_data/errata.yml` is likewise hand-maintained, with its schema documented in
  its own header comment.
- `baseurl` is deliberately empty. Setting it to `/ep` is the obvious-looking
  move and it breaks the theme: remote-theme assets land in `_site/assets`, and
  every stylesheet URL the theme emits gets the `baseurl` prefix, so the CSS
  would be requested from `/ep/assets/gitbook/` and 404. The book's location
  lives in **permalinks** instead.
- The `/ep` prefix is therefore baked into permalinks at generation time
  (`--prefix`), not resolved through Liquid — Jekyll does not evaluate Liquid
  inside front matter.
- `_includes/mathjax.html` overrides the theme's copy to load **nothing**. The
  upstream version treats `$` as an inline maths delimiter, which mangles the
  book's many prices ("$0.10 add up to $0.30").
- In `ep/assets/css/site.css`, every length is in `em`, never `rem`. GitBook
  sets `html{font-size:62.5%}`, making 1rem ten pixels rather than sixteen;
  anything in `rem` renders at about five-eighths its intended size.
- `assets/search.html` is excluded from html-proofer: the theme generates it
  with `<a href=".">`, which resolves to a directory with no index. That is an
  upstream bug in `sighingnow/jekyll-gitbook`.
- `solutions` is a real collection but is deliberately absent from
  `ordered_collections`, so it never appears in the sidebar — solutions are
  reachable only from their exercise page.
- Sidebar in-page TOC is capped at heading level 2 on purpose: exercise pages
  carry an `h3` per exercise, and Chapter 20 alone has 130.

### The generators

`extract_exercises.py` parses 445 "Find the Bug" exercises and their 445 worked
solutions out of twelve chapter `.tex` files plus
`python_snippets_solutions.tex`. It is a **strict parser by design**: the
manuscript's uniformity (one `minted` listing per `\paragraph`, exactly one
solution per exercise number, 445 of each) is **asserted, not worked around**.
A change to the book's conventions is meant to fail loudly here rather than
quietly emit half-parsed pages. If it raises, fix the manuscript or update the
invariant deliberately — do not soften the assertion to get a build through.

Chapter titles are keyed by **exercise number, not source filename**; the two
disagree (`python_list.tex` holds the 6.x exercises, `python_quality.tex`
declares two chapters and holds the 16.x set).

`generate_toc.py` emits `_data/toc.yml` rather than a finished page, so
`_book/02-table-of-contents.md` owns the prose and merely loops over the data.
It reuses `extract_exercises.py`'s LaTeX→Markdown converter by importing it.

## SEO

Two shadowed includes carry the whole SEO layer. Both override same-named files
in the remote theme, the same trick `mathjax.html` uses:

- **`_includes/head.html`** — the upstream version emits one
  `<meta name="description">` containing `site.description`, identically on
  every page, and nothing else. The override reproduces everything upstream
  emits (stylesheet list included — **diff this against the theme when it
  updates**) and adds per-page description, canonical, Open Graph, Twitter card,
  robots, and the analytics tag.
- **`_includes/structured-data.html`** — JSON-LD, branched by page so the book
  is not described on a page about LLM routing: the organization graph on `/`,
  a `Book` plus breadcrumbs under `/ep/`, and a `LearningResource` on exercise
  pages.

Front matter a page can set, all optional:

| Key | Effect |
|---|---|
| `description` | The meta/OG/Twitter description. Falls back to the page excerpt, then `site.description`. |
| `seo_title` | Overrides `<title>` only. Use when the `<h1>` is too bare to compete in results — the landing page's title is "IntuitAI", which alone is useless. |
| `image` / `image_alt` | Share image. `_config.yml` `defaults` already point the three book collections at the cover. |
| `og_type` | Defaults to `article` for collection pages, `website` otherwise. |

Exercise and solution pages need no front matter: their opening paragraph makes
a good excerpt, and the fallback chain picks it up.

Analytics is `site.google_analytics` in `_config.yml` and is emitted **only when
`JEKYLL_ENV=production`**, so a local `jekyll serve` never reports into the real
property. Note it now runs on the book's pages too, which it did not before the
landing page moved into the theme.

`robots.txt` is deliberately front-matter-free so Jekyll copies it verbatim; its
sitemap URL is therefore hardcoded rather than built from `site.url`.

Open-source projects are linked under `github.com/intuitai`: model-gateway,
reverb, tangle, quranllm, random-number-mcp-server.

## Note on README.md

`README.md` predates the Jekyll migration and describes a repository layout
that no longer exists (`styles.css`, `img/intuitailogo.jpg`,
`generate_images*.py`, projects under `github.com/nobelk`, "zero build
process"). Prefer this file and the comments in `_config.yml`, `Gemfile` and
`pages.yml` — which are kept next to what they describe — over the README.
