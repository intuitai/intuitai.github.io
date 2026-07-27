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
| `/eai/` | *Everyday AI*, a second book site (`_eaibook/`) |

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
  stylesheets. The path and the `ep-` prefix are historical — that file dresses
  the landing page and `/eai/` too, and it is the site's only stylesheet.
  Moving it to `assets/` would put it in the same tree the remote theme copies
  its own assets into, which is the sort of collision `_config.yml` warns
  about at length; leave it where it is.
- There is **no site JavaScript of our own**. `js/` held two Pico.css utilities
  (a theme switcher and a modal handler) and was deleted with Pico; the theme
  ships its own font and theme controls. Anything under `assets/gitbook/` comes
  from the remote theme — do not edit it, shadow the include instead.
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

The generators need Python 3.9 or later (`Path.is_relative_to`). Nothing in the
workflow pins a version, because CI never runs them: their output is committed.

To regenerate *Everyday Programming*'s pages from its LaTeX manuscript (both
scripts default `--manuscript` to `../manuscripts/everyday-programming` and
`--site` to `.`):

```console
$ ./tools/extract_exercises.py --manuscript ../manuscripts/everyday-programming
$ ./tools/generate_toc.py      --manuscript ../manuscripts/everyday-programming
```

And *Everyday AI*'s, from its own manuscript:

```console
$ ./tools/generate_toc.py     --manuscript ../manuscripts/everyday-ai \
      --stem everyday-ai --out eai/toc.yml --min-chapters 7
$ ./tools/build_eai_sample.py --manuscript ../manuscripts/everyday-ai
```

Both manuscripts live outside this repository. Without them the generators
cannot run — but the generated output is committed, so the site builds fine
without either.

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

`generate_toc.py` emits a data file rather than a finished page, so the
table-of-contents page owns the prose and merely loops over the data. It reuses
`extract_exercises.py`'s LaTeX→Markdown converter by importing it, and it
serves **both** books: `--stem`, `--out` and `--min-chapters` are what the
second one passes. Both books are typeset with `sicp-style.tex`, so both emit
the same `\contentsline` grammar and one parser is enough. Changing the parser
changes both books' contents pages — regenerate and diff both.

Note that front matter never reaches the data: `parse_toc` drops any entry whose
page number will not `int()`, and roman numerals will not. That is why *Everyday
AI*'s contents listing shows no preface, and why the unnumbered back-matter
*Index* — an arabic page number — does show. (*Everyday Programming* has no
`Preface` line in its `.toc` at all, so nothing is being dropped there.)

Dropping a chapter clears `current_chapter` as well, so that a dropped entry's
sections are discarded with it rather than silently refiled under the chapter
before it. Both books happen to avoid that case today; *Everyday AI*'s preface
is still lorem ipsum and will not always.

## The second book at /eai/

*Everyday AI* is a much smaller site than `/ep/`: no exercises, no solutions,
no downloadable code. Four hand-written pages in `_eaibook/` (home, contents,
sample, errata), one generated data file, and five committed assets.

**Write the pages from `content/*.tex`, not from `outline.md`.** The manuscript
carries a planning document that reads like a description of the book and is
not one — it promises a *When It Goes Wrong* sidebar on stale facts (only three
sidebars exist, and none is that), says every chapter opens on a real person
(two open on no one, and two carry the author's own footnote saying the person
is a composite), and says the book names model versions (it names products and
one price, and deliberately avoids version numbers). An adversarial review
caught five false claims on these pages, all traceable to that file. There is
also a superseded 16-chapter `everyday-ai.md` in the manuscript root; the
current book has seven chapters.

- `_data/eai/toc.yml` is **generated**; `_data/eai/errata.yml` is
  hand-maintained, with its schema in its own header comment. The nesting under
  `_data/eai/` is not decoration: the flat name `eai-toc.yml` would be reached
  as `site.data.eai-toc`, which Liquid parses as a *subtraction*.
- The pages' titles carry the book's name — "Everyday AI: Errata", not
  "Errata". The theme's sidebar lists every collection's page titles in one
  flat column separated only by dividers, with no group headings, so both books
  would otherwise contribute an identically-labelled "Errata" and "Table of
  Contents". This is deliberate; `_config.yml` says so next to
  `ordered_collections`, which is also where the collection ordering is
  explained.
- **The book is not published.** Its copyright page reserves all rights (unlike
  *Everyday Programming*, which is Apache 2.0), its ISBN is still LaTeX's
  example number, and its preface is still lorem ipsum. The site says
  "forthcoming", the JSON-LD omits `isbn`, `datePublished` and `license`, and
  only the sample carries `isAccessibleForFree`. Do not let any of those drift
  into claiming more than is true — and revisit all of them together when the
  book actually ships.

### build_eai_sample.py

Unlike the other two generators, this one *builds* the manuscript rather than
reading it: XeLaTeX over a copy of the tree with the DRAFT watermark, the
placeholder preface and Chapters 3–7 excised, producing
`eai/assets/pdf/everyday-ai-sample-chapters-1-2.pdf`. So it needs a TeX
toolchain and the three OpenType families `sicp-style.tex` selects, installed
system-wide (`make fontcheck` in the manuscript checks them).

Each excision is an exact string asserted to appear exactly once, for the same
reason `extract_exercises.py` asserts the manuscript's shape: a reorganised
preamble should fail loudly rather than quietly ship a sample with the
watermark still on it. Do not relax an assertion into a regex to get a build
through.

**The sample's printed page numbers DO match the finished book's**, and
`_eaibook/02-sample.md` says so. `\mainmatter` resets to arabic 1 after the
front matter, so dropping the preface changes where Chapter 1 sits in the file
without changing its printed number: Chapter 1 is page 1 and Chapter 2 page 7 in
both. (An earlier version of this file and of the builder's docstring claimed
the opposite, and the site copy repeated it; verified entry by entry against
`everyday-ai.toc`.)

The ISBN excision is the one that is easiest to lose and worst to lose. The
manuscript carries LaTeX's example number with a `% replace this with your own`
comment beside it, and unlike the DRAFT watermark it does not *look* like
placeholder text to a reader — it looks like the book's ISBN. It is also the
only edit that lands in `frontmatter/copyrightpage.tex` rather than the master,
which is why `EDITS` entries name their file.

`check_contents` reads the .toc the build itself just wrote and requires exactly
chapters `["1", "2"]`. That is the real guard; the page-count bounds either side
of it only catch a chapter that typeset but came out mangled. A page count alone
would not notice a sample missing Chapter 2.

The five committed assets under `eai/assets/` are the sample PDF, `cover.png`,
`cover-small.png` and two `sample-page-*.png` images. The last two are
Ghostscript renders of pages 8 and 14 of that PDF at 110 dpi — re-render them if
the manuscript's pagination shifts, or they will show the wrong pages.

## SEO

Two shadowed includes carry the whole SEO layer. Both override same-named files
in the remote theme, the same trick `mathjax.html` uses:

- **`_includes/head.html`** — the upstream version emits one
  `<meta name="description">` containing `site.description`, identically on
  every page, and nothing else. The override reproduces everything upstream
  emits (stylesheet list included — **diff this against the theme when it
  updates**) and adds per-page description, canonical, Open Graph, Twitter card,
  robots, and the analytics tag.
- **`_includes/structured-data.html`** — JSON-LD, branched by page so a book is
  not described on a page about LLM routing: the organization graph on `/`, a
  `Book` plus breadcrumbs under `/ep/` and again under `/eai/`, and a
  `LearningResource` on exercise pages. The branches test `page.url contains
  "/ep/"` and `contains "/eai/"`; those prefixes do not overlap as substrings,
  so the two are genuinely exclusive. The author is one `Person` node with a
  site-level `@id` shared by both books — an `@id` under one book's path would
  model the same author as two people.

  **Two publishers, deliberately.** A *book* is published by `#imprint`,
  Intramotev Press — the name on both books' copyright pages and in their
  visible page text. The *website* is published by `#organization`, IntuitAI.
  Pointing a book at `#organization` is the easy mistake and it used to be
  there: it puts two different publishers on one page, one for the reader and
  one for the crawler, which is what Google's "markup must match visible
  content" guidance is about.

  Every `@id` a page references is now defined on that same page, except the two
  bare `{"@id": ".../#book"}` members the landing page lists — kept as a cheap
  statement of what belongs to the site, and inert by design, since consumers
  resolve `@id` within a document rather than across one. Worth re-checking with
  a script if you touch this file; a reference that resolves nowhere is easy to
  introduce and invisible in the rendered page.

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
property. Note it now runs on the books' pages too, which it did not before the
landing page moved into the theme.

`robots.txt` is deliberately front-matter-free so Jekyll copies it verbatim; its
sitemap URL is therefore hardcoded rather than built from `site.url`.

Open-source projects are linked under `github.com/intuitai`: model-gateway,
reverb, tangle, quranllm, random-number-mcp-server.

## Note on README.md

`README.md` was rewritten in July 2026 and is current: it covers the same
architecture, commands and deployment path as this file, aimed at a contributor
rather than an agent. Keep the two in step when either changes.

It had drifted badly before that, describing `styles.css`, `img/intuitailogo.jpg`
and `generate_images*.py` (none of which exist), projects under
`github.com/nobelk`, a "zero build process", and an MIT licence when `LICENSE`
is Apache 2.0. When something here disagrees with a source file, trust the
comments in `_config.yml`, `Gemfile` and `pages.yml` — they sit next to what
they describe and rot more slowly.
