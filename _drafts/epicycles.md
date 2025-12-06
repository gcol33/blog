---
layout: post
title: "Epicycles"
date: 2025-12-06
categories: [TBD]
toc: true
---

## DRAFT - Open Questions

This post is not yet written. These are notes on possible angles.

---

## The Core Idea

Ptolemy explained planetary motion with circles on circles (epicycles). It worked - predictions were accurate for centuries. Copernicus put the Sun at the center and simplified the model.

But here's the thing: **Ptolemy wasn't wrong in a mathematical sense.** Any periodic motion can be decomposed into circles. That's what Fourier proved 1700 years later. Epicycles are a valid Fourier decomposition.

So what was wrong with Ptolemy? Not his predictions. His *basis*.

---

## Possible Angles

### 1. Overfitting

Epicycles are the original overfit. Add enough circles and you can trace any curve - including an elephant. The model fits perfectly but explains nothing.

Same trap in regression: add enough polynomial terms and R² goes to 1. You've memorized the data, not learned the pattern.

**Punchline:** A model can predict without understanding.

### 2. Model Selection / Occam's Razor

Copernicus won not because his predictions were better (they weren't, initially) but because his model was *simpler*. Fewer parameters for the same fit.

This is AIC/BIC before AIC/BIC existed. Penalize complexity. Prefer parsimony.

**Punchline:** The simplest model that fits is often the truest.

### 3. Basis Choice

Fourier: sines and cosines.
Wavelets: localized bumps.
PCA: principal components.

The "right" basis makes the signal sparse. Ptolemy's basis (Earth-centered circles) required many terms. Kepler's basis (Sun-centered ellipses) required few.

**Punchline:** Your choice of basis reveals your assumptions - and determines your complexity.

### 4. Prediction vs Understanding

A model can predict perfectly and still be "wrong" about the underlying structure. Epicycles predicted eclipses. They said nothing true about gravity, orbits, or physics.

Modern parallel: neural networks predict but don't explain. Are they epicycles?

**Punchline:** Prediction is not understanding.

---

## Historical Thread

- Ptolemy (150 AD): Epicycles work
- Copernicus (1543): Sun-centered, still circles, still needed epicycles
- Kepler (1609): Ellipses. Finally the right basis. No epicycles needed.
- Fourier (1822): Any periodic function = sum of sines/cosines
- Modern ML: Back to epicycles? Overparameterized models that predict but don't explain

---

## Stats Connections to Develop

- Fourier transform as basis change
- Overfitting and the bias-variance tradeoff
- AIC/BIC as Occam's razor formalized
- PCA as finding the "natural" basis
- Sparse representations (why do some bases need fewer terms?)

---

## Interactive Element Ideas

- Draw any curve, show its Fourier decomposition as epicycles
- Slider: add more epicycles, watch the fit improve (overfitting visual)
- Compare Ptolemy orbit vs Kepler orbit - same prediction, different complexity

---

## Open Questions

1. What's the surprising insight that ties this together?
2. How to connect to stats beyond "overfitting is bad"?
3. Is there a modern example where we're using epicycles without knowing it?
4. What's the punchline?

---

## Notes

- "Epicycles" has become a pejorative - but they *worked*
- The problem was never accuracy, it was insight
- Fourier showed epicycles are mathematically legitimate
- So the lesson isn't "epicycles bad" - it's something subtler about basis, complexity, and understanding
