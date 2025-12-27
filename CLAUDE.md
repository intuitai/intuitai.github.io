# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages repository for intuitai.org - a static website for IntuitAI, a non-profit research organization dedicated to democratizing artificial intelligence. The site is a single-page application with a modern, vibrant teal/cyan design featuring comprehensive sections: hero, mission, research, team, projects, testimonials, and contact form. The design emphasizes accessibility, SEO optimization, and a professional, engaging user experience.

## Architecture

The website follows a simple static HTML structure:
- **Single-page layout**: All content sections are in `index.html` with smooth scrolling navigation
- **CSS-only styling**: No JavaScript framework dependencies, pure CSS with modern features (CSS Grid, Flexbox, CSS custom properties/variables)
- **Responsive design**: Mobile-first approach with breakpoints at 768px and 480px
- **Fixed navigation**: Header with logo and navigation that stays visible while scrolling with backdrop blur effect
- **Modern system fonts**: Uses native font stack for optimal performance and native feel
- **Accessibility-first**: Includes focus states, ARIA-compliant markup, and print-optimized styles

## Repository Structure

- `index.html` - Main website content with hero, mission, research, team, projects, testimonials, and contact sections
- `styles.css` - Complete styling with CSS custom properties, responsive design, animations, and accessibility features
- `intuitailogo.jpg` - Company logo (JPEG format) used in header with subtle scale transform on hover
- `CNAME` - Custom domain configuration pointing to intuitai.org
- `resource/` - Directory containing downloadable documents:
  - `unlocking-real-world-solutions-with-ai.pdf` - Main whitepaper
  - `unlocking-real-world-solutions-with-ai.docx` - Word version of whitepaper
- `images/` - Directory containing all website images:
  - `hero-background.png` - Gradient background for hero section
  - `icon-democratizing.png` - Mission section feature icon
  - `icon-solutions.png` - Mission section feature icon
  - `icon-integration.png` - Mission section feature icon
  - `research-illustration.png` - Research section illustration
  - `team/team-placeholder.png` - Team member photo placeholder
  - `testimonials/testimonial-placeholder.png` - Testimonial avatar placeholder
  - Additional SVG sources for all icons
- `generate_images.py` - Python script for AI-powered image generation using Hugging Face API
- `generate_images_v2.py` - Updated version of image generation script

## Development Workflow

Since this is a static GitHub Pages site:
- **No build process required** - Direct HTML/CSS editing
- **No local server needed** - Files can be opened directly in browser for testing
- **Live deployment** - Changes pushed to main branch automatically deploy to intuitai.org
- **No package.json or dependencies** - Pure HTML/CSS implementation

## Key Design Elements

### Color System
- **CSS Custom Properties**: All colors defined as CSS variables in `:root` for consistency
- **Primary Teal/Cyan Palette**:
  - `--primary-teal: #00BCD4` - Main brand color, buttons, accents
  - `--primary-teal-dark: #0097A7` - Darker teal for hover states
  - `--primary-teal-light: #4DD0E1` - Lighter teal for gradients
  - `--primary-teal-pale: #B2EBF2` - Pale teal for borders and highlights
- **Accent Colors**:
  - `--accent-teal: #00ACC1` - Secondary accent color
  - `--accent-orange: #FF6B35` - Optional accent (not currently used)
- **Neutral Colors**:
  - `--text-dark: #1A2332` - Main headings and primary text
  - `--text-medium: #4A5568` - Body text
  - `--text-light: #718096` - Subdued text
  - `--bg-white: #FFFFFF` - White backgrounds
  - `--bg-teal-tint: #F0FDFF` - Light teal background tint
  - `--bg-teal-light: #E0F7FA` - Alternating section backgrounds
  - `--border-teal: #B2EBF2` - Borders and dividers
- **Shadows and Effects**:
  - `--shadow-sm`, `--shadow-md`, `--shadow-lg` - Layered shadows with teal tint
  - `--overlay-teal` - Semi-transparent teal overlay

### Typography
- **System font stack**: Modern native fonts (`-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, etc.)
- **Hierarchy**: Clear typographic scale with h1 (1.5rem), h2 (2.75rem), h3 (1.75rem)
- **Enhancement details**: Letter spacing, line height, and weight variations for visual hierarchy
- **Section headers**: Centered with decorative underline using `::after` pseudo-element

### Visual Effects
- **Hero section**: Gradient background (teal to cyan) with grid pattern overlay and optional background image
- **Logo treatment**: Subtle scale transform on hover
- **Navigation**: Animated underline effect on hover using CSS transitions
- **Buttons**: Multiple button styles (btn-primary, btn-secondary) with inverted hover states, elevation effects (transform + box-shadow)
- **Header**: Backdrop blur filter for glassmorphism effect with semi-transparent white background
- **Card components**: Hover effects with translateY and shadow transitions on feature cards, team cards, testimonial cards, and project cards
- **Smooth scrolling**: Native CSS `scroll-behavior: smooth`

### Interactive Elements
- **Navigation links**: Animated underline effect that expands on hover
- **Call-to-action buttons**: Transform on hover with shadow elevation, includes icons (emoji)
- **Logo**: Subtle scale transform on hover
- **Focus states**: Visible outline for keyboard navigation accessibility
- **Form inputs**: Teal border on focus with overlay shadow effect
- **Project cards**: Hover effects with teal gradient badges and feature tags
- **Testimonial cards**: Left border accent with decorative quotation marks

## Content Structure

### Sections
1. **Hero** (id: `hero`): Full viewport height gradient hero section with tagline "Unlocking Real-World Solutions with AI", subtitle, and dual call-to-action buttons (Download Whitepaper, View Projects)
2. **Mission** (id: `mission`): Three-column feature grid with icons showcasing:
   - Democratizing AI
   - Real-World Solutions
   - Intelligent Integration
3. **Research** (id: `research`): Two-column layout with research text and illustration, includes whitepaper download button
4. **Team** (id: `team`): Team introduction with three-column grid of team member cards featuring:
   - Dr. Sarah Chen - Founder & Research Director
   - Michael Rodriguez - Lead AI Engineer
   - Emily Watson - Operations Director
5. **Projects** (id: `projects`): Detailed project showcase with individual cards for each project:
   - Model Gateway (Go)
   - Semantic Cache (Go)
   - Random Number Server (Python)
   - QuranLLM (AI)
   - Footer link to view all projects on GitHub
6. **Testimonials** (id: `testimonials`): Three-column grid of testimonial cards with quotes, avatars, and attribution
7. **Contact** (id: `contact`): Contact form with fields for name, email, organization, and message, plus alternative email link (nobel@intuitai.org)

### Navigation Labels
- Mission (links to #mission)
- Research (links to #research)
- Team (links to #team)
- Projects (links to #projects)
- Testimonials (links to #testimonials)
- Contact (links to #contact)

## SEO and Meta Tags

The website includes comprehensive SEO optimization:
- **Meta tags**: Standard meta description, keywords, and author tags
- **Open Graph tags**: Full OG implementation for Facebook sharing with custom image, title, description
- **Twitter Card tags**: Twitter-specific meta tags for better social media sharing
- **Structured Data**: JSON-LD schema.org markup for Organization type, including:
  - Organization name, URL, logo
  - Non-profit status
  - Founding date (2024)
  - Contact email
  - Social media links (GitHub)
  - Area served (Worldwide)
- **Canonical URL**: Proper canonical tag pointing to https://intuitai.org/
- **Theme Color**: Meta theme color set to primary teal (#00BCD4)
- **Favicon**: Logo used as favicon and apple-touch-icon
- **Accessibility**: Skip link for keyboard navigation, ARIA labels on sections and navigation

## Image Generation Tools

Two Python scripts are included for generating website images using AI:
- **generate_images.py**: Uses Hugging Face Inference API with Stable Diffusion XL to generate all website images
  - Generates hero background, feature icons, research illustration, team and testimonial placeholders
  - Supports retry logic and rate limiting
  - Configurable with HUGGINGFACE_TOKEN environment variable
  - Outputs optimized PNG files with custom sizes for each image type
- **generate_images_v2.py**: Updated version with improvements

All generated images follow the teal/cyan color palette and modern, minimal design aesthetic.

## Component Styles

### Feature Cards (Mission Section)
- White background with border-radius and shadow
- Top border accent in primary teal (4px solid)
- Icon images (100x100px) centered at top
- Hover effect: translateY(-8px) with enhanced shadow
- CSS Grid layout: `repeat(auto-fit, minmax(280px, 1fr))`
- Responsive: single column on mobile

### Team Cards
- White background with subtle shadow
- Circular team photos (150px diameter) with teal border
- Team role in uppercase with teal color
- Hover effect: translateY(-5px) with shadow transition
- CSS Grid: 3 columns on desktop, single column on mobile

### Testimonial Cards
- White background with left border accent (4px teal)
- Decorative quotation mark using CSS ::before pseudo-element
- Avatar images (60px circular) with teal border
- Quote in italic style
- Author info with name and organization
- Hover effect: translateY(-5px)

### Project Cards
- White background with left border accent (4px teal)
- Gradient badge for project language/type
- Feature tags with light teal background
- Project link with arrow indicator
- Flexbox layout for vertical spacing
- Links to individual GitHub repositories

### Contact Form
- Full-width form fields with teal borders
- Focus state: teal border with overlay shadow
- Gradient submit button (teal to accent-teal)
- Form fields: name, email, organization, message
- Placeholder text in light gray
- Alternative email link below form
- Responsive: full width on all devices