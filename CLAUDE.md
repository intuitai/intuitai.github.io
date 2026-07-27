# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages repository for intuitai.org. It serves **two independent
sites from one domain**, and most of the guidance below applies only to the first:

| Path | What it is | How it is built |
|---|---|---|
| `/` | The IntuitAI landing page and project pages | Hand-written HTML on Pico.css. No layouts, no front matter. |
| `/ep/` | *Everyday Programming*, a book site | Jekyll + the `jekyll-gitbook` remote theme |

They coexist without interfering because **Jekyll copies any file without front
matter through byte-for-byte**. `index.html`, `ml-powered-text-recovery.html`,
`img/`, `js/` and `resource/` have no front matter, so introducing Jekyll changed
nothing about them. Only the book's pages carry front matter, so only they get a
layout. Editing the landing page is still plain HTML editing.

### The book at /ep/ — read this before touching it

- `_book/`, `_exercises/`, `_solutions/`, `_data/toc.yml`, `_data/downloads.yml`
  and `ep/assets/code/` are **generated** by `tools/extract_exercises.py` and
  `tools/generate_toc.py` from the book's LaTeX manuscript. Never hand-edit them;
  fix the manuscript and re-run. `_data/errata.yml` is hand-maintained.
- The `/ep` prefix is baked into permalinks at generation time
  (`--prefix`), not resolved through Liquid, because Jekyll does not evaluate
  Liquid inside front matter.
- `baseurl` is deliberately empty. Setting it to `/ep` breaks the theme's asset
  URLs — see the comment at the top of `_config.yml`.
- `_includes/mathjax.html` overrides the theme's copy to load nothing. The
  upstream version treats `$` as an inline maths delimiter, which mangles the
  book's many prices ("$0.10 add up to $0.30").

## Architecture

The landing page follows a simple static HTML structure:
- **Single-page layout**: Minimal content in `index.html` with mission and projects sections
- **Pico.css framework**: Uses Pico.css v2.1.1 from CDN for styling (no custom CSS)
- **Responsive design**: Pico.css provides mobile-first responsive design out of the box
- **JavaScript functionality**: Two small utility scripts for theme switching and modal support
- **Minimalist approach**: Focus on content over complex design elements

## Repository Structure

- `index.html` - Main website content with header, mission, and projects sections
- `styles.css` - Legacy custom CSS file (not currently used, Pico.css is used instead)
- `img/` - Directory containing website images:
  - `intuitailogo.jpg` - Company logo used in header
- `js/` - JavaScript utilities:
  - `minimal-theme-switcher.js` - Pico.css theme switcher for light/dark mode
  - `modal.js` - Pico.css modal functionality
- `intuitailogo.jpg` - Company logo (also in img/ directory)
- `CNAME` - Custom domain configuration pointing to intuitai.org
- `README.md` - Project documentation
- `LICENSE` - MIT License file
- `CLAUDE.md` - This file - AI assistant project instructions
- `.github/` - GitHub configuration (workflows removed)
- `resource/` - Directory containing downloadable documents:
  - `unlocking-real-world-solutions-with-ai.pdf` - Main whitepaper
  - `unlocking-real-world-solutions-with-ai.docx` - Word version of whitepaper
- `generate_images.py` - Python script for AI-powered image generation using Hugging Face API
- `generate_images_v2.py` - Updated version of image generation script

## Development Workflow

For the **landing page** nothing has changed: it is still direct HTML editing
against CDN-hosted Pico.css, and the file can be opened straight in a browser.

For anything under **`/ep/`**, or to reproduce what CI does:

```console
$ bundle install
$ bundle exec jekyll serve            # http://localhost:4000/
$ bundle exec jekyll build
$ bundle exec htmlproofer ./_site --disable-external --allow-hash-href \
    --no-ignore-empty-alt --ignore-files "/assets\/search\.html/"
```

To regenerate the book's pages from the manuscript:

```console
$ ./tools/extract_exercises.py --manuscript ../manuscripts/everyday-programming
$ ./tools/generate_toc.py      --manuscript ../manuscripts/everyday-programming
```

Deployment is by **GitHub Actions** (`.github/workflows/pages.yml`), not by
Pages' built-in Jekyll, which supports neither collection `sort_by` nor
`jekyll-remote-theme`. The workflow builds the whole domain and runs
html-proofer over it — including the landing page — before publishing, so a
broken image path anywhere fails the deploy rather than reaching production. A
red run means intuitai.org stops updating, not just the book.

## Technology Stack

### Frontend Framework
- **Pico.css v2.1.1**: Minimal CSS framework loaded from jsdelivr CDN
  - Provides semantic HTML styling
  - Built-in responsive design
  - Light/dark theme support
  - No custom CSS needed

### JavaScript
- **minimal-theme-switcher.js**: Pico.css official theme switcher
  - Manages light/dark theme preference
  - Stores preference in localStorage
  - Auto-detects system preference
- **modal.js**: Pico.css official modal handler
  - Opens/closes modal dialogs
  - Handles click-outside and ESC key closing
  - Manages scrollbar width during modal display

### Styling Approach
- **No custom CSS**: Uses Pico.css defaults exclusively
- **Semantic HTML**: Pico.css styles semantic HTML elements directly
- **Container class**: Pico's `.container` class for centered, responsive layout
- **Color scheme meta tag**: Set to "light" in HTML head

## Content Structure

### Header
- Company logo (100px width)
- Site title: "IntuitAI"
- Tagline: "AI solutions for real world applications."

### Sections
1. **Mission** (id: `mission`): Brief description of IntuitAI's team and focus
2. **Projects** (id: `projects`): Introduction and bulleted list of open-source projects:
   - Model Gateway - LLM request routing and management
   - Random Number MCP Server - Weather-based random number generation
   - QuranLLM - AI-powered Quran search

### Footer
- Attribution to Pico.css
- Link to source code example

## SEO and Meta Tags

The website includes basic SEO optimization:
- **Meta tags**:
  - Description, keywords, author
  - Robots directives (index, follow, max-image-preview, max-snippet, max-video-preview)
  - Googlebot directives
  - Language (English)
  - Revisit-after (7 days)
  - Rating (General)
- **No Open Graph tags**: Removed for simplicity
- **No Twitter Card tags**: Removed for simplicity
- **No Structured Data**: Removed for simplicity
- **No Analytics**: Google Analytics removed
- **Color scheme**: Set to "light" mode by default

## Key Files

### index.html
- DOCTYPE html with semantic HTML5 structure
- Uses Pico.css container class for layout
- Minimal sections: header, main (mission, projects), footer
- Loads Pico.css from CDN
- Includes two JavaScript files for theme switching and modals

### JavaScript Files
Both JavaScript files are official Pico.css utilities:
- Licensed under MIT
- Copyright 2019-2024 Pico.css
- Vanilla JavaScript, no dependencies

### Legacy Files
- `styles.css` - Custom CSS from previous version (not currently used)
- `generate_images.py` and `generate_images_v2.py` - Image generation scripts (may not be needed for current minimal design)

## Design Philosophy

The current design emphasizes:
- **Minimalism**: Focus on content, not elaborate styling
- **Simplicity**: Use framework defaults, avoid customization
- **Performance**: Minimal dependencies, fast loading
- **Maintainability**: Less code to maintain
- **Accessibility**: Pico.css provides good accessibility defaults

## Development Notes

- The website previously had extensive custom CSS, multiple sections (hero, research, team, testimonials, contact), and comprehensive SEO. These have been removed in favor of a minimal approach.
- `styles.css` still exists but is not referenced in `index.html`
- GitHub Actions workflows have been removed (`.github/workflows/` is empty)
- The `images/` directory has been replaced with `img/` containing only the logo
- If expanding the site, consider whether to continue with Pico.css defaults or reintroduce custom styling
