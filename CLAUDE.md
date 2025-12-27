# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages repository for intuitai.org - a simple static website for IntuitAI, a non-profit research organization dedicated to democratizing artificial intelligence. The site is a single-page application with a clean, minimalist design featuring sections for mission, research, projects, and contact information.

## Architecture

The website follows a simple static HTML structure:
- **Single-page layout**: All content sections are in `index.html` with smooth scrolling navigation
- **CSS-only styling**: No JavaScript framework dependencies, pure CSS with modern features (CSS Grid, Flexbox, CSS custom properties/variables)
- **Responsive design**: Mobile-first approach with breakpoints at 768px and 480px
- **Fixed navigation**: Header with logo and navigation that stays visible while scrolling with backdrop blur effect
- **Modern system fonts**: Uses native font stack for optimal performance and native feel
- **Accessibility-first**: Includes focus states, ARIA-compliant markup, and print-optimized styles

## Repository Structure

- `index.html` - Main website content with hero, mission, research, projects, and contact sections
- `styles.css` - Complete styling with CSS custom properties, responsive design, animations, and accessibility features
- `intuitailogo.jpg` - Company logo (JPEG format) used in header with grayscale filter
- `CNAME` - Custom domain configuration pointing to intuitai.org
- `resource/` - Directory containing downloadable documents:
  - `unlocking-real-world-solutions-with-ai.pdf` - Main whitepaper
  - `unlocking-real-world-solutions-with-ai.docx` - Word version of whitepaper

## Development Workflow

Since this is a static GitHub Pages site:
- **No build process required** - Direct HTML/CSS editing
- **No local server needed** - Files can be opened directly in browser for testing
- **Live deployment** - Changes pushed to main branch automatically deploy to intuitai.org
- **No package.json or dependencies** - Pure HTML/CSS implementation

## Key Design Elements

### Color System
- **CSS Custom Properties**: All colors defined as CSS variables in `:root` for consistency
  - `--primary-black: #1a1a1a` - Main headings and primary elements
  - `--secondary-black: #333333` - Body text
  - `--accent-gray: #666666` - Subdued text
  - `--light-gray: #f5f5f5` - Alternating section backgrounds
  - `--border-gray: #e0e0e0` - Borders and dividers
  - `--pure-white: #ffffff` - White backgrounds

### Typography
- **System font stack**: Modern native fonts (`-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, etc.)
- **Hierarchy**: Clear typographic scale with h1 (1.5rem), h2 (2.75rem), h3 (1.75rem)
- **Enhancement details**: Letter spacing, line height, and weight variations for visual hierarchy
- **Section headers**: Centered with decorative underline using `::after` pseudo-element

### Visual Effects
- **Hero section**: Subtle grid pattern overlay using CSS gradients
- **Logo treatment**: Grayscale filter with hover scale transform
- **Navigation**: Animated underline effect on hover using CSS transitions
- **Buttons**: Inverted hover state with elevation (transform + box-shadow)
- **Header**: Backdrop blur filter for glassmorphism effect
- **Smooth scrolling**: Native CSS `scroll-behavior: smooth`

### Interactive Elements
- **Navigation links**: Animated underline effect that expands on hover
- **Call-to-action buttons**: Transform on hover with shadow elevation, includes icons (emoji)
- **Logo**: Subtle scale transform on hover
- **Focus states**: Visible outline for keyboard navigation accessibility

## Content Structure

### Sections
1. **Hero**: Full viewport height with tagline "Unlocking Real-World Solutions with AI"
2. **Mission** (id: `goal`): Detailed description of IntuitAI's non-profit mission and approach
3. **Research** (id: `whitepaper`): Whitepaper download with description
4. **Projects** (id: `projects`): Link to GitHub organization (github.com/intuitai)
5. **Contact** (id: `contact`): Email contact (nobel@intuitai.org)

### Navigation Labels
- Mission (links to #goal)
- Research (links to #whitepaper)
- Projects (links to #projects)
- Contact (links to #contact)