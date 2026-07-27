# IntuitAI

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fintuitai.org)](https://intuitai.org)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-red?logo=jekyll&logoColor=white)](https://jekyllrb.com)
[![Deployed with GitHub Actions](https://img.shields.io/badge/Deployed%20with-GitHub%20Actions-blue?logo=githubactions&logoColor=white)](.github/workflows/pages.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)

> **AI solutions for real world applications.**

Source for [intuitai.org](https://intuitai.org) — the website of IntuitAI, a
non-profit research organization building open-source, practical AI tools, and
the home of two books, *Everyday Programming* and *Everyday AI*.

---

## What is on the domain

| Path | What it is |
|---|---|
| [`/`](https://intuitai.org/) | Landing page — mission, projects, books |
| [`/ml-powered-text-recovery.html`](https://intuitai.org/ml-powered-text-recovery.html) | Project write-up on ML-powered OCR text recovery |
| [`/ep/`](https://intuitai.org/ep/) | *Everyday Programming*, a free book on Python for beginners |
| [`/eai/`](https://intuitai.org/eai/) | *Everyday AI*, a forthcoming guide to using AI well |

Every page renders through the
[`jekyll-gitbook`](https://github.com/sighingnow/jekyll-gitbook) remote theme.
This is recent: until July 2026 the landing page was hand-written HTML on
Pico.css with no front matter, and only the book was themed. Pico.css is no
longer used.

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

html-proofer is the only gate — there is no test suite and no linter. It checks
the landing page as well as the book, so a broken image path anywhere fails the
build rather than reaching production.

Analytics is emitted only when `JEKYLL_ENV=production`, so serving locally never
reports into the live property.

---

## Repository layout

```
index.html                     Landing page (front matter + gitbook layout)
ml-powered-text-recovery.html  Project write-up
_book/                         Everyday Programming pages — hand-written prose
_exercises/  _solutions/       GENERATED from the Everyday Programming manuscript
_eaibook/                      Everyday AI pages — hand-written prose
_data/toc.yml downloads.yml    GENERATED; errata.yml is hand-maintained
_data/eai/toc.yml              GENERATED; eai/errata.yml is hand-maintained
_includes/                     Overrides of theme includes (see below)
ep/assets/                     Site-wide CSS, plus Everyday Programming's
                               images, PDF and generated .py files
eai/assets/                    Everyday AI's cover, sample images, sample PDF
tools/                         Generators that read the LaTeX manuscripts
.github/workflows/pages.yml    Build, check, and deploy
```

### Theme overrides

The site shadows three of the theme's includes by defining files of the same
name in `_includes/`:

- **`head.html`** — the upstream version emits a single site-wide description
  and no canonical, Open Graph or Twitter tags. This one resolves them per page.
- **`structured-data.html`** — JSON-LD, branched by page: the organization on
  `/`, a book plus breadcrumbs under `/ep/` and under `/eai/`, a learning
  resource on exercise pages.
- **`mathjax.html`** — loads nothing. Upstream treats `$` as a maths delimiter,
  which mangles the book's many prices ("$0.10 add up to $0.30").

### Generated content

Each book's contents listing — and, for *Everyday Programming*, its exercises,
solutions and downloadable code — is generated from a LaTeX manuscript that
lives outside this repository:

```bash
# Everyday Programming
./tools/extract_exercises.py --manuscript ../manuscripts/everyday-programming
./tools/generate_toc.py      --manuscript ../manuscripts/everyday-programming

# Everyday AI
./tools/generate_toc.py      --manuscript ../manuscripts/everyday-ai \
    --stem everyday-ai --out eai/toc.yml --min-chapters 7
./tools/build_eai_sample.py  --manuscript ../manuscripts/everyday-ai
```

`build_eai_sample.py` is the odd one out: it does not read the manuscript so
much as rebuild it, running XeLaTeX over a copy with the draft watermark, the
placeholder preface and Chapters 3–7 removed. It therefore needs a working TeX
toolchain, which the other two do not.

The generated output is committed, so the site builds without either
manuscript. Do not hand-edit anything the generators write — fix the manuscript
and re-run. `_book/` and `_eaibook/` are *not* generated; those pages are prose
and are edited directly.

---

## Deployment

Pushing to `main` triggers
[`.github/workflows/pages.yml`](.github/workflows/pages.yml), which builds the
site, runs html-proofer over it, and publishes to GitHub Pages.

The build runs on Actions rather than Pages' built-in Jekyll, which supports
neither collection `sort_by` nor `jekyll-remote-theme`. A failed run means
intuitai.org stops updating — not just the book.

---

## Projects

| Project | Language | What it does |
|---|---|---|
| [Model Gateway](https://github.com/intuitai/model-gateway) | Go | Intelligent routing and management of LLM requests across providers, with failover, cost optimization and caching |
| [Reverb](https://github.com/intuitai/reverb) | Go | Semantic response cache with knowledge-aware invalidation; two-tier exact and similarity matching |
| [Tangle](https://github.com/intuitai/tangle) | Python | Deadlock and livelock detection for multi-agent AI workflows, with LangGraph and OpenTelemetry support |
| [Random Number MCP Server](https://github.com/intuitai/random-number-mcp-server) | Python | MCP server generating random numbers from national weather data as an entropy source |
| [QuranLLM](https://github.com/intuitai/quranllm) | Python | LLM-powered semantic search of the Quran |

More at the [GitHub organization](https://github.com/intuitai).

---

## Books

**[Everyday Programming, Volume I: Basics of Computer Programs](https://intuitai.org/ep/)**
by Dr. Nobel Khandaker — a first course in Python for absolute beginners, built
on nothing more than tenth-grade mathematics. Twenty-one chapters in seven
parts, plus [445 *Find the Bug* exercises](https://intuitai.org/ep/book/exercises/)
with full worked solutions, and a
[free sample of Chapters 1–2](https://intuitai.org/ep/book/sample/).

**[Everyday AI, Volume I: Basics of Artificial Intelligence](https://intuitai.org/eai/)**
by Dr. Nobel Khandaker — a practical guide to using AI well for readers with no
technical background: what a language model actually does, how to ask it for
what you want, and how to check the answer before trusting it. Seven chapters,
forthcoming, with a
[free sample of Chapters 1–2](https://intuitai.org/eai/book/sample/) to
download now.

---

## Contributing

Issues and pull requests are welcome. Before opening a PR, run the build and
html-proofer commands above — CI runs the same checks and will reject a broken
link or missing asset.

If your change touches the book's exercises, solutions or contents, edit the
manuscript and re-run the generators rather than editing the generated pages.

---

## License

Licensed under the Apache License 2.0 — see [LICENSE](LICENSE).

The text and code of *Everyday Programming* are likewise Apache 2.0.

*Everyday AI* is not. Its copyright page reserves all rights; the two sample
chapters published here are free to read, and nothing about that book's text is
Apache-licensed. This repository's licence covers the site's own code and
prose, not either manuscript.

Icons by [Becris via Flaticon](https://www.flaticon.com/free-icons/machine-learning);
the attribution on the landing page is a condition of that licence, not
decoration.

---

## Contact

- **Website**: [intuitai.org](https://intuitai.org)
- **Email**: [nobel@outlook.com](mailto:nobel@outlook.com)
- **GitHub**: [@intuitai](https://github.com/intuitai)
