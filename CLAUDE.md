# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages repository for intuitai.org - a simple static website hosting documentation and resources for Intuit AI. The site is a single-page application with a clean, minimalist design featuring sections for goals, whitepaper downloads, projects, and contact information.

## Architecture

The website follows a simple static HTML structure:
- **Single-page layout**: All content sections are in `index.html` with smooth scrolling navigation
- **CSS-only styling**: No JavaScript framework dependencies, pure CSS with modern features (CSS Grid, Flexbox, animations)
- **Responsive design**: Mobile-first approach with breakpoints at 768px and 480px
- **Fixed navigation**: Header with logo and navigation that stays visible while scrolling

## Repository Structure

- `index.html` - Main website content with hero section, goal, whitepaper, projects, and contact sections
- `styles.css` - Complete styling including responsive design, animations, and modern CSS features
- `intuitailogo.png` - Company logo used in header
- `CNAME` - Custom domain configuration pointing to intuitai.org
- `resource/` - Directory containing downloadable documents:
  - `unlocking-real-world-solutions-with-ai.pdf` - Main whitepaper
  - `unlocking-real-world-solutions-with-ai.docx` - Word version of whitepaper
  - `intuitailogo.png` - Logo copy

## Development Workflow

Since this is a static GitHub Pages site:
- **No build process required** - Direct HTML/CSS editing
- **No local server needed** - Files can be opened directly in browser for testing
- **Live deployment** - Changes pushed to main branch automatically deploy to intuitai.org
- **No package.json or dependencies** - Pure HTML/CSS implementation

## Key Design Elements

- **Color scheme**: Black/white minimalist design with subtle gradients
- **Typography**: Arial/Helvetica with clean spacing and subtle animations
- **Visual effects**: Floating dot patterns in hero section, hover animations on navigation and buttons
- **Interactive elements**: Smooth scrolling navigation, button hover effects with transform and shadow