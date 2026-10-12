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

### Avoid AI-Sounding Patterns
Do NOT use these clichéd AI writing patterns:
- **"Not X, but Y" / "Not X. It's Y."** - e.g., "This is not a bug. It's a feature."
- **"This is the story of..."** - grandiose framing sentences
- **"The lesson had to be learned"** - pithy transition phrases
- **"X opened a floodgate"** - clichéd metaphors
- **"Each X expanded/revealed/showed..."** - repetitive summary patterns
- **"The boundary is still moving"** - dramatic one-liners
- **"The history of X is a history of Y"** - parallel structure clichés
- **"None of these... All of them..."** - parallel contrast sentences
- **"They were wrong."** - dramatic reveals
- **"This is not paranoia. It is physics."** - false dichotomy closers

Let the content speak for itself. End sections naturally without wrapping up with a punchy takeaway line.

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

## Figures

### Approach
No animation and no interactivity: no `<script>`, `<canvas>`, buttons, sliders or inline demo markup in posts. Every graphic is a static SVG figure. A simulation becomes its result with a fixed seed; a parameter slider becomes small multiples or a curve over the parameter; scenario buttons become panels side by side.

### Pipeline
- `_figures/` (underscore: Jekyll does not publish it) holds one Python script per post, named after the post slug, e.g. `_figures/de-mere-dice.py`.
- Every script imports `_figures/style.py`, the single source of the figure style: Cousine font (bundled in `_figures/fonts/`, text written as paths), black/white/gray only, deterministic SVG output.
  - `style.figure(height, ncols, nrows)`: full-width (7.2 in) figure with axes.
  - `style.canvas(height)`: frameless diagram canvas in inch units, origin bottom-left.
  - `style.save(fig, name)`: checks text clearance, then writes `assets/figures/<name>.svg`. It raises `OverlapError` if any text (tick labels, axis labels, titles, annotations, legends) touches other text, a line, marker, bar or arrow, or the figure edge; text may sit inside a closed shape but not cross its outline. The build exits non-zero and writes nothing for that figure; move the label until it passes.
  - Colours: `style.BLACK`, `DARK`, `MID`, `LIGHT`, `PALE`, `WHITE`; hatching for further distinction.
- Build: `python _figures/build.py` (all) or `python _figures/build.py <slug>`. Commit the generated SVGs.

### In a Post
```liquid
{% include figure.html src="<name>.svg" alt="What is plotted." %}
```
No captions; the prose around the figure explains it. Alt text states what is plotted.

### Double Border
Drawn by CSS (`assets/css/11-figures.css`): the `figure.plot` wrapper has `1px solid #000` and `0.875rem` padding, the image inside has its own `1px solid #000`. Figures therefore carry no outer frame of their own.

### Style Guidelines
- Black and white only: `#000`, `#fff` and grays. No colour.
- Axis labels; panel titles only when panels need distinguishing; direct labels instead of legends where possible.
- No takeaway text or decorative annotations inside figures.
- Check every figure in a browser screenshot, also at phone width, before publishing.

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
