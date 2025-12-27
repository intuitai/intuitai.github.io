# IntuitAI

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fintuitai.org)](https://intuitai.org)
[![Validate Website](https://github.com/intuitai/intuitai.github.io/workflows/Validate%20Website/badge.svg)](https://github.com/intuitai/intuitai.github.io/actions)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-blue)](https://pages.github.com/)

> **Unlocking Real-World Solutions with AI**

Official website for IntuitAI - a non-profit research organization dedicated to democratizing artificial intelligence through accessible, practical AI solutions for real-world applications.

🌐 **Live Site:** [https://intuitai.org](https://intuitai.org)

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [SEO & Analytics](#seo--analytics)
- [Design System](#design-system)
- [Projects](#projects)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

IntuitAI is a non-profit research organization committed to making advanced artificial intelligence accessible to everyone. We bridge the gap between cutting-edge AI research and practical implementation, enabling organizations across industries to harness the power of AI without requiring extensive technical expertise.

### Our Mission

- **Democratizing AI**: Making advanced AI solutions accessible and practical for real-world applications
- **Real-World Solutions**: Bridging the gap between cutting-edge research and practical implementation
- **Intelligent Integration**: Creating solutions that seamlessly enhance decision-making and augment human capabilities

---

## Features

### Website Highlights

- **Single-Page Application**: Modern, smooth-scrolling design with intuitive navigation
- **Fully Responsive**: Mobile-first design optimized for all devices (desktop, tablet, mobile)
- **SEO Optimized**: Comprehensive meta tags, Open Graph, Twitter Cards, and structured data (Schema.org)
- **Accessibility First**: WCAG-compliant with ARIA labels, skip links, and keyboard navigation
- **Performance**: Pure HTML/CSS (no JavaScript frameworks), optimized images, and fast loading
- **Modern Design**: Vibrant teal/cyan color palette with glassmorphism effects and smooth animations
- **Analytics Ready**: Google Analytics 4 integration for tracking and insights

### Key Sections

1. **Hero** - Eye-catching gradient background with clear call-to-action
2. **Mission** - Three-column feature showcase of our core values
3. **Research** - Whitepaper download and research highlights
4. **Team** - Meet the experts behind IntuitAI
5. **Projects** - Showcase of open-source contributions
6. **Testimonials** - Client success stories and feedback
7. **Contact** - Easy-to-use contact form with direct email option

---

## Technology Stack

### Frontend

- **HTML5** - Semantic markup with accessibility features
- **CSS3** - Modern features including:
  - CSS Grid & Flexbox for layouts
  - CSS Custom Properties (variables) for theming
  - CSS Animations & Transitions
  - Backdrop filters for glassmorphism effects
  - Media queries for responsive design

### Deployment

- **GitHub Pages** - Static site hosting
- **Custom Domain** - intuitai.org via CNAME

### Development Tools

- **GitHub Actions** - Automated validation and CI/CD
- **Lighthouse CI** - Performance and SEO auditing
- **HTML5 Validator** - Markup validation
- **Python Scripts** - AI-powered image generation (Hugging Face)

---

## Repository Structure

```
intuitai.github.io/
├── index.html                  # Main website HTML
├── styles.css                  # Complete styling and responsive design
├── intuitailogo.jpg           # Company logo
├── CNAME                       # Custom domain configuration
├── README.md                   # This file
├── CLAUDE.md                   # AI assistant project instructions
├── .github/
│   └── workflows/
│       ├── validate.yml        # GitHub Actions workflow
│       ├── lighthouserc.json   # Lighthouse CI configuration
│       └── link-check-config.json  # Link checker configuration
├── resource/
│   ├── unlocking-real-world-solutions-with-ai.pdf   # Main whitepaper
│   └── unlocking-real-world-solutions-with-ai.docx  # Word version
├── images/
│   ├── hero-background.png              # Hero section background
│   ├── icon-democratizing.png           # Mission icons
│   ├── icon-solutions.png
│   ├── icon-integration.png
│   ├── research-illustration.png        # Research section image
│   ├── team/
│   │   └── team-placeholder.png         # Team member photos
│   └── testimonials/
│       └── testimonial-placeholder.png  # Testimonial avatars
├── generate_images.py         # Image generation script
└── generate_images_v2.py      # Updated image generation script
```

---

## Getting Started

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- (Optional) Local web server for testing
- (Optional) Python 3.x for image generation scripts

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/intuitai/intuitai.github.io.git
   cd intuitai.github.io
   ```

2. **Open locally**
   - Simply open `index.html` in your web browser
   - Or use a local server:
   ```bash
   # Python 3
   python -m http.server 8000

   # Then visit http://localhost:8000
   ```

3. **Make changes**
   - Edit `index.html` for content
   - Edit `styles.css` for styling
   - Test changes locally

4. **Deploy**
   - Push to `main` branch
   - GitHub Pages automatically deploys changes
   - Visit https://intuitai.org to see live updates

---

## SEO & Analytics

### SEO Features

- **Meta Tags**: Comprehensive description, keywords, robots, language
- **Open Graph**: Full Facebook/social media sharing optimization
- **Twitter Cards**: Twitter-specific meta tags for rich previews
- **Structured Data**: JSON-LD Schema.org Organization markup
- **Canonical URL**: Proper canonicalization
- **Semantic HTML**: Proper heading hierarchy and ARIA labels
- **Image Optimization**: Alt tags, proper dimensions, lazy loading

### Google Analytics

The website includes Google Analytics 4 (GA4) tracking. To activate:

1. Create a GA4 property at [Google Analytics](https://analytics.google.com/)
2. Copy your Measurement ID (format: `G-XXXXXXXXXX`)
3. Replace `G-XXXXXXXXXX` in `index.html` line 106 with your actual ID
4. Deploy changes

Analytics features:
- Anonymized IP addresses
- Cookie consent ready
- Page view tracking
- Event tracking ready

---

## Design System

### Color Palette

The website uses a modern teal/cyan color scheme:

- **Primary Teal**: `#00BCD4` - Main brand color, buttons, accents
- **Primary Teal Dark**: `#0097A7` - Hover states, darker elements
- **Primary Teal Light**: `#4DD0E1` - Gradients, highlights
- **Primary Teal Pale**: `#B2EBF2` - Borders, subtle accents
- **Accent Teal**: `#00ACC1` - Secondary accent color
- **Text Dark**: `#1A2332` - Headings, primary text
- **Text Medium**: `#4A5568` - Body text
- **Text Light**: `#718096` - Subdued text
- **Background White**: `#FFFFFF` - White backgrounds
- **Background Teal Tint**: `#F0FDFF` - Light teal sections

### Typography

- **Font Family**: System font stack (`-apple-system, BlinkMacSystemFont, Segoe UI, Roboto`)
- **Headings**: Bold, with negative letter spacing
- **Body Text**: 1.0625rem (17px), line-height 1.8
- **Hierarchy**: Clear typographic scale

### Visual Effects

- **Glassmorphism**: Backdrop blur on fixed header
- **Shadows**: Layered shadows with teal tint
- **Hover Effects**: Transform and elevation on interactive elements
- **Smooth Scrolling**: Native CSS smooth scrolling
- **Animations**: CSS transitions for all interactive elements

---

## Projects

IntuitAI maintains several open-source projects:

1. **[Model Gateway](https://github.com/nobelk/model-gateway)** (Go)
   - High-performance LLM request routing
   - Multi-provider support with automatic failover
   - Cost optimization and request caching

2. **[Semantic Cache](https://github.com/nobelk/semantic-cache)** (Go)
   - Distributed semantic caching for LLM applications
   - Embedding-based similarity matching
   - 60-80% cache hit rates, 40-70% cost reduction

3. **[Random Number Server](https://github.com/nobelk/random-number-server)** (Python)
   - MCP server for random number generation
   - Uses weather data as entropy source
   - Built with FastMCP framework

4. **[QuranLLM](https://github.com/nobelk/quranllm)** (AI)
   - LLM-powered Quran search application
   - Semantic search capabilities
   - Natural language processing

Visit our [GitHub organization](https://github.com/intuitai) for more projects.

---

## Development

### Image Generation

Generate website images using AI:

```bash
# Install dependencies
pip install requests pillow python-dotenv

# Set up Hugging Face token
export HUGGINGFACE_TOKEN=your_token_here

# Run image generation
python generate_images_v2.py
```

This generates all images with the teal/cyan color palette and modern aesthetic.

### GitHub Actions

The repository includes automated workflows:

- **HTML Validation**: Validates HTML5 markup and CSS
- **Link Checking**: Verifies all internal and external links
- **Lighthouse CI**: Performance, accessibility, and SEO audits
- **SEO Check**: Validates meta tags and structured data
- **Accessibility Check**: ARIA labels and accessibility features

Workflows run on:
- Every push to `main`
- Every pull request
- Weekly schedule (Sundays)
- Manual trigger

---

## Contributing

We welcome contributions to improve the IntuitAI website!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test locally
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Contribution Guidelines

- Follow the existing code style
- Maintain responsive design principles
- Ensure accessibility standards
- Test on multiple browsers and devices
- Update documentation as needed
- Keep the design consistent with the teal/cyan theme

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright © 2025 IntuitAI. All rights reserved.

---

## Contact

- **Website**: [https://intuitai.org](https://intuitai.org)
- **Email**: [nobel@intuitai.org](mailto:nobel@intuitai.org)
- **GitHub**: [@intuitai](https://github.com/intuitai) | [@nobelk](https://github.com/nobelk)

---

<div align="center">

**Made with ❤️ by IntuitAI**

[Website](https://intuitai.org) • [Projects](https://github.com/intuitai) • [Contact](mailto:nobel@intuitai.org)

</div>
