---
layout: post
title: "Pushforwards and Pullbacks"
date: 2025-09-04
categories: category-theory measure-theory probability
toc: true
---

## The Die and the Question

Roll a die. You get a 4.

Now I ask: "Is it even?"

Something just happened that's easy to miss. The randomness *moved*. It started in a space of six faces, then traveled to a space of two labels: odd and even. The uniform distribution on faces became a fair coin on parity.

This movement has a direction. The die doesn't care about parity—parity is something we impose *after* the roll. But once we ask the question, probability flows forward through our question, landing in a simpler space.

What if we reverse direction? Suppose I define a reward: \$1 if even, \$0 if odd. That function lives in parity-space. But to compute your expected winnings, you need to pull it back to die-space, where the probability lives.

Two directions. Measures push forward. Functions pull back.

The pattern extends far beyond dice—it's the grammar of how mathematics moves structure from one space to another.

---

## See It Happen

<div id="transport-demo" style="max-width: 720px; margin: 1.5em auto;">
  <svg id="transport-svg" viewBox="0 0 700 320" style="width: 100%; height: auto; border: 1px solid #000; background: #fff;">
    <!-- Left space: Die faces -->
    <g id="die-space">
      <text x="120" y="30" text-anchor="middle" font-size="16" font-weight="bold">Die Faces (Ω)</text>
      <g id="die-faces" transform="translate(60, 50)">
        <!-- Six circles for faces -->
        <circle cx="0" cy="0" r="22" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="0" y="6" text-anchor="middle" font-size="16">1</text>

        <circle cx="60" cy="0" r="22" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="60" y="6" text-anchor="middle" font-size="16">2</text>

        <circle cx="120" cy="0" r="22" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="120" y="6" text-anchor="middle" font-size="16">3</text>

        <circle cx="0" cy="60" r="22" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="0" y="66" text-anchor="middle" font-size="16">4</text>

        <circle cx="60" cy="60" r="22" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="60" y="66" text-anchor="middle" font-size="16">5</text>

        <circle cx="120" cy="60" r="22" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="120" y="66" text-anchor="middle" font-size="16">6</text>
      </g>
      <text x="120" y="175" text-anchor="middle" font-size="14" fill="#666">P(each) = 1/6</text>
    </g>

    <!-- Right space: Parity -->
    <g id="parity-space">
      <text x="580" y="30" text-anchor="middle" font-size="16" font-weight="bold">Parity Space</text>
      <g transform="translate(520, 70)">
        <circle cx="0" cy="0" r="35" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="0" y="6" text-anchor="middle" font-size="16">Odd</text>

        <circle cx="120" cy="0" r="35" fill="#fff" stroke="#000" stroke-width="2"/>
        <text x="120" y="6" text-anchor="middle" font-size="16">Even</text>
      </g>
      <text x="580" y="145" text-anchor="middle" font-size="14" fill="#666" id="parity-prob">P(each) = 1/2</text>
    </g>

    <!-- Arrow between spaces -->
    <g id="main-arrow">
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill="#000"/>
        </marker>
        <marker id="arrowhead-back" markerWidth="10" markerHeight="7" refX="1" refY="3.5" orient="auto">
          <polygon points="10 0, 0 3.5, 10 7" fill="#000"/>
        </marker>
      </defs>
      <line x1="250" y1="90" x2="450" y2="90" stroke="#000" stroke-width="2" marker-end="url(#arrowhead)" id="forward-arrow"/>
      <text x="350" y="75" text-anchor="middle" font-size="14" id="arrow-label">f: face → parity</text>
    </g>

    <!-- Controls -->
    <g transform="translate(180, 210)">
      <rect x="0" y="0" width="150" height="36" rx="4" fill="#fff" stroke="#000" stroke-width="1" style="cursor:pointer" id="btn-push"/>
      <text x="75" y="24" text-anchor="middle" font-size="14" style="pointer-events:none">Push measure →</text>

      <rect x="170" y="0" width="150" height="36" rx="4" fill="#fff" stroke="#000" stroke-width="1" style="cursor:pointer" id="btn-pull"/>
      <text x="245" y="24" text-anchor="middle" font-size="14" style="pointer-events:none">← Pull function</text>
    </g>

    <!-- Explanation box -->
    <text x="350" y="280" text-anchor="middle" font-size="14" id="explanation" fill="#000">Click a button to see how structure moves.</text>
    <text x="350" y="300" text-anchor="middle" font-size="13" id="explanation2" fill="#000"></text>
  </svg>
</div>

{% raw %}
<script>
(function(){
  const svg = document.getElementById('transport-svg');
  const btnPush = document.getElementById('btn-push');
  const btnPull = document.getElementById('btn-pull');
  const explanation = document.getElementById('explanation');
  const explanation2 = document.getElementById('explanation2');

  const dieFaces = document.querySelectorAll('#die-faces circle');
  const parityCircles = document.querySelectorAll('#parity-space circle');

  function reset(){
    dieFaces.forEach(c => c.setAttribute('fill', '#fff'));
    parityCircles.forEach(c => c.setAttribute('fill', '#fff'));
  }

  btnPush.addEventListener('click', function(){
    reset();
    // Highlight odd faces (1,3,5) with diagonal lines, even faces (2,4,6) solid
    [0, 2, 4].forEach(i => dieFaces[i].setAttribute('fill', '#fff'));
    [1, 3, 5].forEach(i => dieFaces[i].setAttribute('fill', '#ccc'));

    // Highlight parity space
    parityCircles[0].setAttribute('fill', '#fff'); // odd
    parityCircles[1].setAttribute('fill', '#ccc'); // even

    explanation.textContent = 'Pushforward: The measure moves forward through f.';
    explanation2.textContent = 'P({odd}) = P({1,3,5}) = 1/2, P({even}) = P({2,4,6}) = 1/2';
  });

  btnPull.addEventListener('click', function(){
    reset();
    // Define g(even)=1, g(odd)=0, show it pulled back
    parityCircles[0].setAttribute('fill', '#fff'); // odd = 0
    parityCircles[1].setAttribute('fill', '#ccc'); // even = 1

    // Pull back to die space
    [0, 2, 4].forEach(i => dieFaces[i].setAttribute('fill', '#fff')); // odd faces get 0
    [1, 3, 5].forEach(i => dieFaces[i].setAttribute('fill', '#ccc')); // even faces get 1

    explanation.textContent = 'Pullback: The function g moves backward through f.';
    explanation2.textContent = 'g(even)=1, g(odd)=0 pulls back to the indicator of {2,4,6}';
  });

  // Hover effects
  [btnPush, btnPull].forEach(btn => {
    btn.addEventListener('mouseenter', () => btn.setAttribute('fill', '#eee'));
    btn.addEventListener('mouseleave', () => btn.setAttribute('fill', '#fff'));
  });
})();
</script>
{% endraw %}

---

## Why Two Directions?

This asymmetry puzzled mathematicians long before probability theory existed.

In the nineteenth century, Bernhard Riemann studied how geometric objects behave when you stretch or bend a surface. He noticed something curious: when you map one surface to another, certain quantities move *with* the map, while others move *against* it.

**Tangent vectors push forward.** If you have a direction at a point and you stretch the surface, the direction stretches along with it. Vectors ride the map.

**Functions pull back.** If you have a function defined on the target surface (say, temperature), you can read its values on the source by composing with the map. Functions resist the map's direction.

This duality appeared again in physics (contravariant vs. covariant tensors), in algebra (homomorphisms vs. cohomomorphisms), and eventually in probability.

The pattern is universal: whenever you have a map between spaces, two operations arise. One follows the map. One opposes it.

---

## The Formal Definitions

Fix a measurable map $f: X \to Y$.

**Pushforward of measures.** Let $\mu$ be a measure on $X$. Define a measure on $Y$ by:

$$
(f_{*}\mu)(B) \;=\; \mu\!\bigl(f^{-1}(B)\bigr) \qquad \text{for } B \subseteq Y \text{ measurable}.
$$

This is covariant: $(g \circ f)_* = g_* \circ f_*$.

**Pullback of functions.** Let $g: Y \to \mathbb{R}$ be measurable. Define a function on $X$ by:

$$
f^{*}g \;=\; g \circ f : X \to \mathbb{R}.
$$

This is contravariant: $(g \circ f)^* = f^* \circ g^*$.

The notation reflects the direction. Subscript $*$ for pushforward (following the arrow). Superscript $*$ for pullback (against the arrow).

---

## Why Inverse Images?

A natural question: why define pushforward using *inverse* images? Why not just push sets forward directly?

Measure theory demands additivity. If $A_1, A_2, \dots$ are disjoint sets in $X$, their direct images $f(A_1), f(A_2), \dots$ need not be disjoint in $Y$. Two different points in $X$ might land on the same point in $Y$.

But inverse images behave perfectly:

$$
f^{-1}(B_1 \cup B_2) = f^{-1}(B_1) \cup f^{-1}(B_2), \qquad f^{-1}(B^c) = f^{-1}(B)^c.
$$

Inverse images preserve the set operations that σ-algebras need. Pushforward uses inverse images even though the measure moves "forward."

---

## The Adjunction: Where the Two Directions Meet

Pushforward and pullback aren't independent tricks. They're married by the integral.

For a measure $\mu$ on $X$ and a function $g$ on $Y$:

$$
\int_{Y} g(y)\, d(f_{*}\mu)(y) \;=\; \int_{X} (g \circ f)(x)\, d\mu(x).
$$

On the left, the measure moves forward to $Y$, where $g$ lives. On the right, the function moves backward to $X$, where $\mu$ lives. Both integrals compute the same number.

This is the change-of-variables formula. But seen through category theory, it's something more: an **adjunction**. The integral defines a pairing between functions and measures, and pushforward/pullback preserve that pairing.

Written symbolically: $f^* \dashv f_*$. Pullback is left adjoint to pushforward.

---

## Category Theory: The General Framework

The pattern of pushforwards and pullbacks is captured by category theory's language of functors.

A **category** consists of:
- **Objects**: the spaces (sets, measurable spaces, manifolds)
- **Morphisms**: the maps between them
- **Composition**: maps can be chained, and identity maps exist

A **functor** assigns objects to objects and morphisms to morphisms, respecting composition.
- **Covariant** functors preserve direction: $F(g \circ f) = F(g) \circ F(f)$
- **Contravariant** functors reverse direction: $F(g \circ f) = F(f) \circ F(g)$

In probability:
- Sending each space $X$ to its measures, and each map $f$ to $f_*$, is a covariant functor.
- Sending each space $Y$ to its observables, and each map $f$ to $f^*$, is a contravariant functor.

The integral formula is the adjunction that ties them together.

This abstraction earns its keep. Once you see the pattern, you recognize it everywhere: in topology (homology vs. cohomology), in algebra (extension vs. restriction of scalars), in logic (existential vs. universal quantifiers).

---

## Back to the Die

Let's make this concrete with the full calculation.

**The spaces:**

$$
\Omega = \{1, 2, 3, 4, 5, 6\}, \qquad P(\{i\}) = \tfrac{1}{6}.
$$

$$
Y = \{\text{odd}, \text{even}\}, \qquad f(i) = \text{parity of } i.
$$

**Pushforward of $P$:**

$$
f_*P(\{\text{odd}\}) = P(\{1, 3, 5\}) = \tfrac{1}{2}, \qquad f_*P(\{\text{even}\}) = P(\{2, 4, 6\}) = \tfrac{1}{2}.
$$

The uniform distribution on faces becomes the fair coin on parity.

**Pullback of a reward function:**

Define $g: Y \to \mathbb{R}$ by $g(\text{even}) = 1$, $g(\text{odd}) = 0$.

$$
f^*g = g \circ f : \Omega \to \mathbb{R}
$$

is the indicator function of $\{2, 4, 6\}$.

**The adjunction in action:**

$$
\int_Y g \, d(f_*P) = 1 \cdot \tfrac{1}{2} + 0 \cdot \tfrac{1}{2} = \tfrac{1}{2}.
$$

$$
\int_\Omega f^*g \, dP = \sum_{i \in \{2,4,6\}} \tfrac{1}{6} = \tfrac{1}{2}.
$$

Both integrals agree. The expected reward is 1/2, computed either by pushing the measure forward or pulling the function back.

---

## Distributions Are Pushforwards

Every probability distribution is a pushforward in disguise.

A random variable is a measurable map $X: \Omega \to \mathbb{R}$. Its distribution is:

$$
P_X(B) = P(X^{-1}(B)) = (X_* P)(B).
$$

The distribution is the pushforward of the base probability through the random variable.

Marginal distributions follow the same pattern. For a joint distribution on $X \times Y$, the marginal on $X$ is the pushforward along the projection $\pi_X$:

$$
(\pi_X)_* \mu (A) = \mu(A \times Y).
$$

Distributions, marginals, transformations—all pushforwards of the same base measure through different maps.

---

## What About Conditioning?

Not everything in probability is a pushforward.

Conditioning is fundamental: it describes how beliefs update when information arrives. Given an event $B$ with $P(B) > 0$:

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}.
$$

This is *not* transport along a map. It's restriction to a slice, followed by renormalization.

Pushforwards move probability between spaces. Conditioning reshapes probability within a single space. Both matter, but they are different operations.

(Disintegration theory can encode conditioning using pushforwards, but the naive picture of "push through a map" doesn't capture what conditioning does.)

---

## From Statistics to Neural Networks

The abstract pattern reappears wherever models transform probability.

**Bayesian inference.** The entire posterior over parameters $\boldsymbol{\beta}$ is pushed through the model:

$$
p(y^* \mid \text{data}) = \int p(y^* \mid \boldsymbol{\beta}) \, p(\boldsymbol{\beta} \mid \text{data}) \, d\boldsymbol{\beta}.
$$

This integral is a pushforward. The posterior on parameters becomes a predictive distribution on outcomes.

**Generative models.** A neural network maps a simple distribution (Gaussian noise in latent space) to a complex distribution (images, text, audio). The generator is a map $G: Z \to X$, and the generated distribution is:

$$
p_X = G_* p_Z.
$$

Every image produced by a diffusion model or GAN is a sample from a pushforward.

**Normalizing flows.** These models make the pushforward explicit. They construct invertible maps with tractable Jacobians, so the density of the pushforward can be computed exactly:

$$
p_X(x) = p_Z(G^{-1}(x)) \cdot |\det \nabla G^{-1}(x)|.
$$

The Jacobian is the trace of the pushforward—Riemann's insight, now running on GPUs.

---

## The Grammar of Structure

In the nineteenth century, Gauss and Riemann studied how curvature behaves under maps between surfaces. Pullbacks carried differential forms; pushforwards carried tangent vectors. The change-of-variables formula, with its Jacobian determinant, was the integral adjunction in differential form.

In the twentieth century, category theory gave the pattern a name and a home. Functors, natural transformations, adjunctions—vocabulary that exists precisely to capture what pushforwards and pullbacks do.

In the twenty-first century, the same structure powers machine learning. Monte Carlo methods push simple randomness into complex simulations. Variational inference pulls expectations back through intractable models. Generative AI pushes latent noise into images and text.

A single map gives rise to two operations. One moves mass forward. The other moves questions back. Integration holds them in balance.

Roll a die. Ask a question. The answer depends on which direction you choose to travel.
