---
layout: post
title: "Pushforwards and Pullbacks"
date: 2025-09-04
categories: category-theory measure-theory probability
---

## How Maps Move Structure

Roll a die.  

The sample space consists of the six faces, which map to the numbers $1$ through $6$, and those numbers map further to properties such as odd or even. At each step the probability measure is carried along: the uniform measure on faces becomes the uniform measure on numbers, and then the fair distribution on parity.  

Maps can be more abstract too. For example, in Dungeons & Dragons the sample space is the set of character classes. Each class maps to the abilities it grants, and each ability maps to the actions available in combat. Structure travels through these maps: the class a player chooses determines a set of abilities, and those abilities in turn determine the kinds of actions that can occur in play.  

Whether the maps are injective or surjective does not matter. What matters is that structure moves from one space to another along them.  

To capture this movement in general, mathematicians invented **category theory**. A category consists of **objects** (the spaces) and **arrows** (the maps). Arrows compose in sequence, and each object carries an identity arrow that leaves it unchanged.  

This minimal framework is enough to ask a sharp question: once a single arrow $f: X \to Y$ is fixed, how should structures that live on $X$ or on $Y$ be transported along it?


---

## Categories Of Spaces And Arrows

In probability we work in the category of measurable spaces.  
- **Objects** are sets equipped with a σ-algebra of subsets, called events.  
- **Morphisms** are measurable maps, meaning the preimage of every event is an event.  

On this foundation we define measures, random variables, and integrals.

Two categorical notions appear quickly:  
- A **functor** assigns data in a way that respects composition and identities.  
  - If it preserves the direction of morphisms, it is *covariant*.  
  - If it reverses them, it is *contravariant*.  
- An **adjunction** is a pair of functors pointing in opposite directions, connected by a universal property that equates two ways of forming the same object.

## Two Canonical Transports

Fix a measurable map $f: X \to Y$.  
Two mechanisms appear immediately.  

- **Inverse image.** For an event $B$ in $Y$, the set  
  $f^{-1}(B) = \{x \in X : f(x) \in B\}$ is an event in $X$.  
  Inverse images respect the set operations that generate the σ-algebra.  

- **Composition.** For an observable $g: Y \to \mathbb{R}$, the composite  
  $g \circ f : X \to \mathbb{R}$ is an observable on $X$.  
  Composition is how information defined on the target is read on the source.  

Both directions are stable: inverse images preserve events, and composition preserves observables.  
Together they form the core ideas behind the formal definitions.

## Covariant Transport Of Measures

Let $\mu$ be a measure on $X$. Transport it along $f$ by defining a measure on $Y$ through inverse images,

$$
(f_{*}\mu)(B) \;=\; \mu\!\bigl(f^{-1}(B)\bigr) \qquad B \subseteq Y \text{ measurable}.
$$

This is the pushforward of $\mu$. It is covariant because composition is respected:

$$
(g\circ f)_{*} \;=\; g_{*} \circ f_{*}, \qquad (\mathrm{id}_{X})_{*}=\mathrm{id}.
$$

One might wonder why not use direct images instead. If $A_1,A_2,\dots$ are disjoint in $X$, their images $f(A_i)$ need not be disjoint in $Y$, so countable additivity would fail.  
Inverse images preserve exactly the structure a measure needs.  

From a functorial point of view, we can also describe pushforward differently.  
Send each measurable space $X$ to the set of all measures on $X$.  
Then any measurable map $f: X \to Y$ induces a map  
$f_{*}: \mathrm{Measures}(X) \to \mathrm{Measures}(Y)$.  
This makes the assignment a covariant functor from measurable spaces to sets.

## Contravariant Transport Of Observables

Let $g: Y \to \mathbb{R}$ be measurable.  
Transport it back along $f$ by composition,

$$
f^{*} g \;=\; g \circ f : X \to \mathbb{R}.
$$

This is the pullback of $g$.  
It is contravariant because composition reverses:

$$
(g\circ f)^{*} \;=\; f^{*} \circ g^{*}, \qquad (\mathrm{id}_{Y})^{*} = \mathrm{id}.
$$

From a functorial point of view, fix a target value space such as $\mathbb{R}$.  
Send each measurable space $Y$ to the set  

$$
\mathrm{Obs}(Y) = \{ g: Y \to \mathbb{R} \;\text{measurable} \},
$$  

and send $f: X \to Y$ to $f^{*}: \mathrm{Obs}(Y) \to \mathrm{Obs}(X)$.  
This makes the assignment a contravariant functor.

## Adjunction Via Integration

Pushforward and pullback are not independent tricks. They are tied by the integral. For a measure $\mu$ on $X$ and an observable $g$ on $Y$,

$$
\int_{Y} g(y)\, d\bigl(f_{*}\mu\bigr)(y)
\;=\;
\int_{X} (g\circ f)(x)\, d\mu(x).
$$

On the left the measure moves forward. On the right the observable moves back. The equality says that these two transports fit perfectly. This is the integral form of an adjunction written $f^{*} \dashv f_{*}$: pullback is left adjoint to pushforward with respect to the pairing given by integration.

There is an abstract way to see this. The integral defines a bilinear pairing between observables on a space and measures on that space. Pullback acts on the observable side, pushforward acts on the measure side, and the pairing is preserved.

## Distributions As Transported Measures

A random variable is a measurable map

$$
X: \Omega \to \mathbb{R}.
$$

The base probability $P$ on $\Omega$ is transported along $X$ to a measure on $\mathbb{R}$ given by

$$
P_{X}(B) \;=\; P\!\bigl(X^{-1}(B)\bigr).
$$

This is the distribution of $X$. It is nothing more or less than a pushforward. Marginal distributions are pushforwards along projection maps; for $\pi_{X}: X\times Y\to X$,

$$
(\pi_{X})_{*}(\mu)(A) \;=\; \mu\!\bigl(A\times Y\bigr).
$$

Distributions and marginals both arise as pushforwards of the base measure.  
It is natural to ask whether other familiar operations in probability fit the same pattern.  

A counterexample is conditioning.  
Conditioning is fundamental because it formalises how probabilities update when new information is known.  
It underlies Bayes’ rule, posterior distributions, regression, and conditional expectation.  

Concretely, conditioning means updating probabilities once we know that some event $B$ has occurred.  
The new measure tells us how likely other events $A$ are, given that we restrict attention to outcomes inside $B$.  
Formally, for an event $B$ with positive mass,  

$$
P(\,\cdot\,\mid B) : A \mapsto \frac{P(A\cap B)}{P(B)}.
$$  

This is not transport along a map.  
It is restriction to the slice $B$, followed by renormalisation so that total mass is $1$.

## From Categories To Statistical Practice

The abstract transports reappear in statistics when models carry probability across spaces.  
A statistical model maps parameters and covariates to a distribution for an outcome.  

In a frequentist workflow, one chooses a single estimate $\hat{\boldsymbol{\beta}}$ for the coefficient vector $\boldsymbol{\beta}$.  
Predictions are then read conditionally at fixed covariates, and uncertainty bands describe the sampling distribution of $\hat{\boldsymbol{\beta}}$ under repeated sampling.  

In a Bayesian workflow, by contrast, the entire posterior over $\boldsymbol{\beta}$ is transported through the model.  
With covariates fixed at representative values,  

$$
p(y^{*} \mid \text{data})
\;=\;
\int p\!\bigl(y^{*} \mid \boldsymbol{\beta}\bigr)\, p(\boldsymbol{\beta}\mid \text{data})\, d\boldsymbol{\beta},
$$  

which is exactly a pushforward of the posterior through the model map.  
The curve with credible bands is the image of that transported mass in the outcome space.

## A Discrete Case With Dice

Take  

$$
\Omega = \{\omega_1, \dots, \omega_6\}, \qquad  
P(\{\omega_i\}) = \tfrac{1}{6},
$$  

with the power-set σ-algebra. This is the uniform probability space of a die.  

Map faces to numbers by  

$$
X: \Omega \to \mathbb{R}, \qquad X(\omega_i) = i.
$$  

The distribution of $X$ is the pushforward measure  

$$
P_X(\{k\}) = P\!\bigl(X^{-1}(\{k\})\bigr) = \tfrac{1}{6}, 
\quad k=1,\dots,6.
$$  

Now map faces to parity by  

$$
f: \Omega \to \{\text{odd},\text{even}\}, \qquad f(\omega_i) = \text{parity}(i).
$$  

The pushforward of $P$ along $f$ is the fair distribution on parity:  

$$
f_{*}P(\{\text{even}\}) = P(\{2,4,6\}) = \tfrac{1}{2}, 
\qquad  
f_{*}P(\{\text{odd}\}) = P(\{1,3,5\}) = \tfrac{1}{2}.
$$  

Take an observable on parity,  

$$
g: \{\text{odd}, \text{even}\} \to \mathbb{R}, \qquad 
g(\text{even}) = 1, \; g(\text{odd}) = 0.
$$  

Its pullback is  

$$
f^{*}g = g \circ f : \Omega \to \mathbb{R},
$$  

which is exactly the indicator function of $\{2,4,6\}$.  

Finally, the change-of-variables identity holds:  

$$
\int_{\{\text{odd},\text{even}\}} g \, d(f_{*}P)
\;=\;
\int_{\Omega} f^{*}g \, dP
\;=\; \tfrac{1}{2}.
$$  

## Beyond Probability

The pattern of pushforwards and pullbacks is older and broader than probability.  
In the nineteenth century, Gauss and Riemann studied how curvature and forms behaved under maps between surfaces.  
Pullbacks carried functions or differential forms from one manifold to another, while pushforwards carried tangent vectors along smooth maps.  
The same duality reappeared in analysis as the change-of-variables formula, where Jacobian determinants mark the trace of a pushforward.  

In the twentieth century, probability and computation revived the theme.  
Monte Carlo methods, developed by Stanislaw Ulam and John von Neumann in the 1940s, transported randomness from simple spaces into complex systems.  
Today, generative models push forward latent distributions into images or text, normalizing flows make Jacobians explicit, and variational inference relies on pullbacks to estimate expectations.  
What began as geometry became the machinery of modern statistics and machine learning.  

The unifying view is straightforward. A single map gives rise to two operations.  
One moves mass forward, the other moves observables back, and integration holds them in balance.  
Across centuries and fields, from Gauss’s surfaces to Kolmogorov’s probability, from Shannon’s information to deep learning models, the same structure appears.  
Pushforwards and pullbacks are not just technical devices.  
They are the grammar by which mathematics moves structure from one space to another.
