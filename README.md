# IntuitAI

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fintuitai.org)](https://intuitai.org)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Pico.css](https://img.shields.io/badge/Pico.css-2.1.1-blue)](https://picocss.com)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-blue)](https://pages.github.com/)

> **AI solutions for real world applications.**

Official website for IntuitAI - a non-profit research organization dedicated to democratizing artificial intelligence through accessible, practical AI solutions.

🌐 **Live Site:** [https://intuitai.org](https://intuitai.org)

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Projects](#projects)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

IntuitAI is a non-profit research organization committed to making advanced artificial intelligence accessible to everyone. We bridge the gap between cutting-edge AI research and practical implementation, enabling organizations across industries to harness the power of AI.

### Our Mission

IntuitAI is led by a team of AI researchers, engineers, and industry experts dedicated to making artificial intelligence accessible and practical for everyone. Our diverse expertise spans machine learning, software engineering, and business strategy.

---

## Features

### Website Highlights

- **Minimalist Design**: Clean, simple layout using Pico.css framework
- **Fully Responsive**: Mobile-first design optimized for all devices
- **Fast Loading**: Minimal dependencies, CDN-hosted CSS, small JavaScript files
- **Theme Support**: Light/dark theme switcher with localStorage persistence
- **Zero Build Process**: Pure HTML with CDN resources
- **Accessibility**: Semantic HTML with Pico.css accessibility defaults

### Key Sections

1. **Mission** - Brief introduction to IntuitAI's team and goals
2. **Projects** - Showcase of open-source contributions

---

## Technology Stack

### Frontend

- **HTML5** - Semantic markup
- **Pico.css v2.1.1** - Minimal CSS framework
  - Loaded from jsdelivr CDN
  - Provides responsive design
  - Built-in light/dark theme support
  - No custom CSS needed

### JavaScript

- **minimal-theme-switcher.js** - Pico.css official theme switcher
- **modal.js** - Pico.css official modal handler
- Both vanilla JavaScript, no dependencies

### Deployment

- **GitHub Pages** - Static site hosting
- **Custom Domain** - intuitai.org via CNAME

---

## Repository Structure

```
intuitai.github.io/
├── index.html                  # Main website HTML
├── styles.css                  # Legacy custom CSS (not currently used)
├── img/
│   └── intuitailogo.jpg        # Company logo
├── js/
│   ├── minimal-theme-switcher.js  # Theme switcher utility
│   └── modal.js                   # Modal handler utility
├── intuitailogo.jpg           # Company logo (duplicate)
├── CNAME                      # Custom domain configuration
├── README.md                  # This file
├── CLAUDE.md                  # AI assistant project instructions
├── LICENSE                    # MIT License
├── .github/                   # GitHub configuration (workflows removed)
├── resource/
│   ├── unlocking-real-world-solutions-with-ai.pdf   # Main whitepaper
│   └── unlocking-real-world-solutions-with-ai.docx  # Word version
├── generate_images.py         # Image generation script (legacy)
└── generate_images_v2.py      # Updated image generation script (legacy)
```

---

## Getting Started

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- (Optional) Local web server for testing

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
   - Pico.css provides all styling automatically
   - Test changes locally

4. **Deploy**
   - Push to `main` branch
   - GitHub Pages automatically deploys changes
   - Visit https://intuitai.org to see live updates

---

## Projects

IntuitAI maintains several open-source projects:

1. **[Model Gateway](https://github.com/nobelk/model-gateway)** (Go)
   - High-performance LLM request routing and management
   - Multi-provider support with automatic failover
   - Cost optimization and request caching

2. **[Random Number MCP Server](https://github.com/nobelk/random-number-server)** (Python)
   - MCP server for random number generation
   - Uses weather data as entropy source
   - Built with FastMCP framework

3. **[QuranLLM](https://github.com/nobelk/quranllm)** (AI)
   - LLM-powered Quran search application
   - Semantic search capabilities
   - Natural language processing

Visit our [GitHub organization](https://github.com/intuitai) for more projects.

---

## Development

### Design Philosophy

The current website follows a minimalist approach:
- **Content first**: Focus on information over elaborate design
- **Framework defaults**: Use Pico.css styling without customization
- **Minimal dependencies**: Only CDN-hosted CSS and two small JS files
- **Fast and simple**: No build process, no package management

### Legacy Files

Some files from previous versions remain in the repository:
- `styles.css` - Custom CSS from earlier version (not currently used)
- `generate_images.py` and `generate_images_v2.py` - Image generation scripts for the previous design

### Pico.css Integration

The website uses Pico.css v2.1.1 for styling:
- Loaded from jsdelivr CDN
- Provides semantic HTML styling
- Responsive design built-in
- Light/dark theme support via JavaScript

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

- Follow the existing minimalist approach
- Maintain responsive design principles
- Test on multiple browsers and devices
- Keep dependencies minimal
- Update documentation as needed

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
