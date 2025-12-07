# Null Hypothesis Accepted

A minimalist statistics and mathematics blog by Gilles Colling.
URL: https://gcol33.github.io/blog

## Project Structure

- **Jekyll static site** hosted on GitHub Pages
- Posts in `_posts/` with format `YYYY-MM-DD-slug.md`
- Custom layouts in `_layouts/` (no theme, custom CSS)
- Styles in `assets/css/` (modular: fonts, KaTeX, base, layout, syntax highlighting)
- KaTeX for math rendering (not MathJax)

## Writing Style

### Voice and Tone
- Clear, precise, explanatory prose
- Historical context woven into technical content (Gauss, Cauchy, Euler, Shannon, etc.)
- Accessible to educated readers without dumbing down
- No emojis, no casual language, no excessive enthusiasm
- Direct sentences, active voice when possible

### Structure
- Posts open with an intuitive hook or everyday scenario
- Build from concrete examples toward formal definitions
- Use horizontal rules (`---`) to separate major sections
- Headers with `##` for main sections, `###` for subsections
- Short paragraphs, often 2-4 sentences

### Mathematics
- LaTeX via KaTeX: `$inline$` and `$$display$$`
- Define variables clearly in prose before equations
- Provide worked examples with explicit calculations
- Balance rigor with intuition

## Graphics and Interactive Plots

### Approach
Graphics are **inline JavaScript/HTML/CSS** embedded directly in posts using `{% raw %}...{% endraw %}` blocks.

### Technical Details
- Use vanilla JavaScript (no frameworks)
- Canvas API or SVG for visualizations
- Responsive design with CSS media queries
- Interactive controls: sliders (`<input type="range">`), radio buttons, etc.
- Self-contained: all code within the post markdown file

### Style Guidelines
- **Black and white only** - no colored fills, no colored bars, no accent colors. Use `#000` (black), `#fff` (white), and grays (`#fafafa`, `#eee`) only.
- **Borders: `1px solid #000` only** - never use `#ddd` or other gray borders
- **No double borders** - outer container has no border, only inner elements (canvas, boxes) have borders
- Clean, functional UI (no decorative elements)
- Stats/output displayed in tabular-nums font
- Responsive: adapt for mobile (smaller canvas, stacked controls)
- Hover effects for interactive elements

### Standard Layout Pattern

Always use this exact structure for interactive demos:

```html
<div id="demo-name" style="max-width: 720px; margin: 0 auto;">
  <canvas id="demo-canvas" style="width: 100%; height: 200px; background: #fff; border: 1px solid #000;"></canvas>

  <div class="demo-controls">
    <button id="demo-btn">Run</button>
    <button id="demo-reset">Reset</button>
  </div>

  <div class="demo-stats">
    <div class="demo-stat-row"><span>Label:</span><strong id="demo-value">0</strong></div>
    <div class="demo-stat-row"><span>Another:</span><strong id="demo-value2">—</strong></div>
  </div>

  <div id="demo-narrative" class="demo-narrative">Initial text...</div>
</div>

{% raw %}
<style>
#demo-name { font-variant-numeric: tabular-nums; }
#demo-name * { box-sizing: border-box; }

#demo-name .demo-controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 10px;
}

#demo-name button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#demo-name button:hover {
  background: #eee;
}

#demo-name .demo-stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 10px;
}
#demo-name .demo-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}

#demo-name .demo-narrative {
  border-top: 1px solid #000;
  padding: 10px 0;
  font-size: 0.95em;
}
</style>

<script>
(function(){
  // Self-executing, no global pollution
  // DPI-aware canvas rendering
  // Event listeners for controls
})();
</script>
{% endraw %}
```

Key points:
- Outer container: `max-width: 720px; margin: 0 auto;` with **NO border**
- **Double border effect**: wrap canvas/SVG in a div with `border: 1px solid #000`, then draw an inner border inside the canvas/SVG with ~14px padding. The ratio between outer and inner should be consistent.
- Stats rows: `border-top: 1px solid #000` (separator lines, not boxes)
- Always include `font-variant-numeric: tabular-nums` on container
- Always include `box-sizing: border-box` on all children

### Double Border Pattern

```html
<div style="border: 1px solid #000; overflow: hidden;">
  <svg id="chart" style="width:100%; height:260px; background:#fff;"></svg>
</div>
```

Then inside the JS, draw inner border:
```js
const innerPad = 14;
html += `<rect x="${innerPad}" y="${innerPad}" width="${W - innerPad*2}" height="${H - innerPad*2}" fill="none" stroke="#000"/>`;
```

For canvas:
```js
ctx.strokeRect(pad, pad, innerW, innerH);
```

## Common Patterns

### Post Front Matter
```yaml
---
layout: post
title: "Title Here"
date: YYYY-MM-DD
categories: topic1 topic2
toc: true           # optional: show table of contents
series: "Series Name"  # optional: link multi-part posts
---
```

### Mathematical Notation
- Random variables: capital letters ($X$, $Y$, $Z$)
- Parameters: Greek letters ($\beta$, $\theta$, $\lambda$)
- Distributions: named with parameters ($\text{Uniform}(a,b)$, $\mathcal{N}(\mu, \sigma^2)$)
- Expectations: $\mathbb{E}[X]$, variance: $\mathrm{Var}(X)$

## Build and Preview

```bash
bundle exec jekyll serve
```

Site builds to `_site/`. Served at http://localhost:4000/blog/

## Categories

### Guidelines
- Use 1-2 categories per post (rarely 3)
- Prefer existing categories over creating new ones
- Categories are broad topics, not tags

### Approved Categories
| Category | Use for |
|----------|---------|
| `probability` | Core probability theory, distributions, random variables |
| `statistics` | Inference, estimation, hypothesis testing |
| `bayesian` | Bayesian methods, posteriors, priors |
| `measure-theory` | Rigorous foundations, sigma-algebras, Lebesgue |
| `algorithms` | Computational methods, graph theory, optimization |
| `paradox` | Counter-intuitive results, puzzles |
| `everyday-math` | Applications to daily life, intuitive explanations |
| `history` | Historical context, mathematicians' stories |
| `perception` | Psychology of probability, cognitive biases |
| `networks` | Graph theory applications, routing, connectivity |
| `ecology` | Biodiversity, environmental statistics |
| `thermodynamics` | Entropy, information theory connections |

Before adding a new category, check if an existing one fits.

## Drafts

Work-in-progress posts go in `_drafts/` (no date prefix needed).

Preview drafts locally:
```bash
bundle exec jekyll serve --drafts
```

When ready to publish, move to `_posts/` with date prefix.

## Series

For multi-part posts, add `series: "Series Name"` to front matter.
All posts with the same series name will show a navigation box linking them in date order.

## Git Push

This repo uses SSH with a specific key. Push with:

```bash
git push
```

Remote is configured as `git@github.com-gcol33:gcol33/blog.git` (uses `~/.ssh/id_ed25519_gcol33` via SSH config alias).
