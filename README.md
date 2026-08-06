# IntuitAI

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fintuitai.org)](https://intuitai.org)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.4-red?logo=jekyll&logoColor=white)](https://jekyllrb.com)
[![Deployed with GitHub Actions](https://img.shields.io/badge/Deployed%20with-GitHub%20Actions-blue?logo=githubactions&logoColor=white)](.github/workflows/pages.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)

> **The reliability layer for multi-agent AI.**

Source for [intuitai.org](https://intuitai.org) — the website of IntuitAI, a
research-driven venture studio incubating startups in agentic and multi-agent
AI.

---

## What is on the domain

| Path | What it is |
|---|---|
| [`/`](https://intuitai.org/) | Landing page — thesis, incubation model, portfolio, contact |
| [`/ml-powered-text-recovery.html`](https://intuitai.org/ml-powered-text-recovery.html) | Research note on ML-powered OCR text recovery |

Two pages of prose, and that is nearly all of it. Also served, and worth
knowing about because they are easy to forget: `resource/` (a DOCX and a PDF,
copied through verbatim, linked from nothing, and the PDF is in the sitemap)
and `assets/search.html`, which the theme generates — it is kept out of the
sitemap and marked `noindex` by a `defaults` entry in `_config.yml`.

Until August 2026 the domain also hosted two books, at
`/ep/` and `/eai/`, with their own collections, LaTeX-driven generators and
JSON-LD branches; those were removed when the organization was repositioned,
and the books moved out of this repository. If you find a comment anywhere in
here that mentions `/ep/`, `/eai/`, `_book/` or `tools/`, it is stale — fix it
or delete it.

Every page renders through the
[`jekyll-gitbook`](https://github.com/sighingnow/jekyll-gitbook) remote theme,
landing page included.

---

## Local development

Requires Ruby 3.x and Bundler.

```bash
bundle install
bundle exec jekyll serve      # http://localhost:4000/
```

To reproduce what CI does before pushing:

```bash
bundle exec jekyll build
bundle exec htmlproofer ./_site --disable-external --allow-hash-href \
    --no-ignore-empty-alt --ignore-files "/assets\/search\.html/"
```

html-proofer is the only gate — there is no test suite, no linter, and no
package manager beyond Bundler.

Two things it does **not** catch, both worth knowing:

- `--disable-external` means outbound links are never fetched. Three links to
  `github.com/intuitai/*` sat on the landing page returning 404 for months
  because of this. If you add a link off-site, open it yourself.
- Analytics is emitted only when `JEKYLL_ENV=production`, so serving locally
  never reports into the live property — and never proves the tag works either.

---

## Repository layout

```
index.html                     Landing page (front matter + gitbook layout)
_research/                     Research write-ups; a collection, so the theme
                               sidebar has something to list
_includes/  _layouts/          Overrides of theme files (see below)
styles/site.css                The site's only stylesheet, loaded site-wide
img/  resource/                Images and downloadable documents
.github/workflows/pages.yml    Build, check, and deploy
```

Two placement decisions look arbitrary and are not:

- **`styles/`, not `assets/`.** `jekyll-remote-theme` copies the theme's own
  `assets/` tree into `_site/assets/`. Putting site files in the same tree
  invites a collision with theme assets. The stylesheet lived at
  `ep/assets/css/site.css` (with an `ep-` class prefix, from the first book)
  until August 2026; path and prefix were renamed together, to `styles/` and
  `ia-`.
- **`_research/`, not the site root.** The gitbook sidebar is built by walking
  `ordered_collections` and printing each page's title. With the book
  collections deleted and nothing in their place, the sidebar renders as a lone
  link back to the site root. The write-up keeps its original
  `/ml-powered-text-recovery.html` URL through a page-level `permalink`, which
  overrides the collection's.

### Theme overrides

The site shadows four of the theme's files by defining files of the same name
in `_includes/` and `_layouts/`. **Each one is a copy-and-diverge, so diff it
against upstream whenever the theme updates:**

- **`head.html`** — the upstream version emits a single site-wide description
  and no canonical, Open Graph or Twitter tags. This one resolves them per page.
  It reproduces everything upstream emits, stylesheet list included — the
  stylesheet list is the part that drifts.
- **`structured-data.html`** — JSON-LD, branched by page: `Organization`
  (with the investor and business-development `contactPoint`s the page
  advertises), `Person`, `WebSite`, `WebPage` and four `SoftwareSourceCode`
  nodes on `/`; an `Article` plus breadcrumbs on research pages. Only four of
  the thirteen projects appear, and none carries a maturity property —
  describing a design-stage repository as software would tell a crawler more
  than the repository supports.
- **`mathjax.html`** — loads nothing. Upstream treats `$` as a maths delimiter.
- **`_layouts/post.html`** — copied verbatim and changed in two marked places.
  Upstream's prev-page fallback assumes no page is ever the site root, so on
  the landing page it emitted a `rel="prev"` and a visible back-arrow both
  pointing at the page you are already on. Both are suppressed at `/`.

Front matter a page can set, all optional:

| Key | Effect |
|---|---|
| `description` | Meta/OG/Twitter description. Falls back to the page excerpt, then `site.description`. |
| `seo_title` | Overrides `<title>` only. The landing page uses it because its `<h1>` is just "IntuitAI", which alone wins nothing. |
| `image` / `image_alt` | Share image. Defaults to the logo. |
| `og_type` | Defaults to `article` for collection pages, `website` otherwise. |
| `order` | Sidebar sort key within a collection. |
| `twitter_card` | Defaults to `summary`, because the default share image is a square logo and `summary_large_image` crops it. Set it only with a genuinely wide image. |
| `noindex` | Emits `noindex, follow`. Set through `defaults` for the theme's generated `assets/search.html`. |
| `date_published` | If set, emitted as `datePublished` in a research page's JSON-LD. **Not `date`** — Jekyll auto-assigns `date` to every collection document from the file's mtime, so guarding on it published the build timestamp. |

---

## Deployment

Pushing to `main` triggers
[`.github/workflows/pages.yml`](.github/workflows/pages.yml), which builds the
site, runs html-proofer over it, and publishes to GitHub Pages.

The build runs on Actions rather than Pages' built-in Jekyll for two reasons,
both downstream of the built-in build pinning the `github-pages` gem
(Jekyll 3.10 at the time of writing): collection `sort_by` is a Jekyll 4
feature and would be silently ignored, and there is nowhere in the built-in
build to run html-proofer as a gate. `jekyll-remote-theme` is *not* one of the reasons — Pages supports it.
A failed run means intuitai.org stops updating.

No `--baseurl` override is passed, and `_config.yml`'s `baseurl` is empty on
purpose: intuitai.org is an apex custom domain served from the root, and a
non-empty value would make the theme request its stylesheets from a path that
404s.

---

## Incubator projects

All thirteen are public and Apache 2.0. Maturity is labelled because four of
them are a problem statement in a repository rather than a running system, and
the label is the only thing standing between a reader and a wasted click — see
the landing page for the same list with fuller descriptions. `resilience4py`'s
own README badge says MIT; its `LICENSE` file and GitHub's detection both say
Apache-2.0, and the badge is the stale one.

| Project | Language | Stage | What it does |
|---|---|---|---|
| [Tangle](https://github.com/nobelk/tangle) | Python | Shipping | Deadlock and livelock detection for multi-agent workflows; embedded library or FastAPI sidecar, with LangGraph and OpenTelemetry integration |
| [MultiTrust](https://github.com/nobelk/multitrust) | Python | Shipping | Inter-agent trust as a Subjective Logic opinion — belief, disbelief, uncertainty — rather than a scalar score |
| [Reverb](https://github.com/nobelk/reverb) | Go | Shipping | Two-tier semantic response cache with knowledge-aware invalidation; library, HTTP/gRPC service, and OpenAI-compatible reverse proxy |
| [llmsim](https://github.com/nobelk/llmsim) | Python | Active | Parallel discrete-event simulation for Python 3.14+, gated on same-seed determinism across every backend |
| [RAGsearch](https://github.com/nobelk/RAGsearch) | Python + Flutter | Active | Fully local RAG search over your own PDFs, via Qdrant and Ollama |
| [Random Number MCP Server](https://github.com/nobelk/random-number-server) | Python | Active | MCP server seeding random numbers from national weather data |
| [claude-tools](https://github.com/nobelk/claude-tools) | Python | Active | The studio's coding-agent skills for review, security scanning and docs |
| [resilience4py](https://github.com/nobelk/resilience4py) | Python | Shipping | Circuit breaker, rate limiter, retry and bulkhead as composable decorators — a port of resilience4j |
| [BMSSP shortest paths](https://github.com/nobelk/single-source-shortest-path) | Python | Active | Reference implementation of Duan et al. (2025); states in its own README which substitutions cost it the paper's asymptotic bound |
| [Oculon](https://github.com/nobelk/oculon) | — | Design stage | Observability and attribution for agent fleets |
| [Cogmux](https://github.com/nobelk/cogmux) | — | Design stage | Cognitive multiplexer routing work across slow, fast and reactive agents |
| [Agentic Workflow](https://github.com/nobelk/agentic-workflow) | — | Design stage | Working notes on agent architecture |
| [QuranLLM](https://github.com/nobelk/quranllm) | — | Design stage | Semantic search over the Quran |

**A note on where these live.** The repositories are under
`github.com/nobelk`, not `github.com/intuitai` — the organization currently
holds only this site, its profile repo, and a private research repo. The
landing page and the JSON-LD both link to the URLs that actually resolve. If
the repositories are moved under the organization, update
[`index.html`](index.html), [`_includes/structured-data.html`](_includes/structured-data.html)
and this table together.

---

## Contributing

Issues and pull requests are welcome. Before opening a PR, run the build and
html-proofer commands above — CI runs the same checks and will reject a broken
link or missing asset.

---

## License

Licensed under the Apache License 2.0 — see [LICENSE](LICENSE). This covers the
site's own code and prose. Each project listed above carries its own licence.

Icons by [Becris via Flaticon](https://www.flaticon.com/free-icons/machine-learning).
The attribution on the landing page is a condition of that licence, not
decoration: do not remove it while `img/neural.png` is in use.

---

## Contact

- **Website**: [intuitai.org](https://intuitai.org)
- **Email**: [nobel@outlook.com](mailto:nobel@outlook.com)
- **GitHub**: [@intuitai](https://github.com/intuitai) · [@nobelk](https://github.com/nobelk)
