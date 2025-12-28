# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages repository for intuitai.org - a minimalist static website for IntuitAI, a non-profit research organization dedicated to democratizing artificial intelligence. The site uses the Pico.css framework for a clean, simple design with minimal dependencies.

## Architecture

The website follows a simple static HTML structure:
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

Since this is a static GitHub Pages site:
- **No build process required** - Direct HTML editing with CDN-hosted CSS
- **No local server needed** - Files can be opened directly in browser for testing
- **Live deployment** - Changes pushed to main branch automatically deploy to intuitai.org
- **Minimal dependencies** - Only Pico.css loaded from CDN, two small vanilla JavaScript files
- **No GitHub Actions** - Validation workflows have been removed

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
