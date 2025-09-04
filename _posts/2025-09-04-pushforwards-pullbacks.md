---
layout: post
title: "Pushforwards and Pullbacks"
date: 2025-09-04
categories: category-theory measure-theory probability
---

## How Maps Move Structure

Category theory organises mathematics around maps and the structures they transport. A category consists of things called objects and directed arrows between them. Arrows compose in sequence, and each object carries an identity arrow that leaves it unchanged. This minimal scaffolding is enough to ask a sharp question: once a single arrow \(f\colon X \to Y\) is fixed, how should structures that live on \(X\) or on \(Y\) travel along that arrow?

Some structures travel with the arrow. Others travel against it. The first kind of transport is called a pushforward. The second is called a pullback. Their direction is not a convention but a consequence of how inverse images and composition behave.

## Categories Of Spaces And Arrows

To speak about probability we use the category whose objects are measurable spaces and whose arrows are measurable maps. A measurable space is a set together with a σ-algebra of subsets called events. A map is measurable when inverse images of events are events. This is the arena where measures, random variables, and integrals live.

There are two further categorical ingredients. A functor is a systematic way of transporting data that respects composition and identities. When arrows keep their direction we call the functor covariant. When arrows reverse we call it contravariant. An adjunction is a pairing of two functors that face one another, tied together by a universal rule that identifies two ways of computing the same quantity.

## Two Canonical Transports

Fix a measurable map \(f\colon X \to Y\). Two mechanisms are available immediately.

The first is inverse image. For an event \(B\) in \(Y\), the set \(f^{-1}(B) = \{x\in X : f(x)\in B\}\) is an event in \(X\). Inverse images commute with the set operations that define the σ-algebra. This direction is reliable.

The second is composition. For an observable \(g\colon Y \to \mathbb{R}\), the composite \(g\circ f\colon X \to \mathbb{R}\) is an observable on \(X\). Composition is how information defined on the target is read on the source. This direction is also reliable.

These two mechanisms—inverse image and composition—are the engines behind the formal definitions.

## Covariant Transport Of Measures

Let \(\mu\) be a measure on \(X\). Transport it along \(f\) by defining a measure on \(Y\) through inverse images,
\[
(f_\*\mu)(B) \;=\; \mu\!\bigl(f^{-1}(B)\bigr) \qquad B \subseteq Y \text{ measurable}.
\]
This is the pushforward of \(\mu\). It is covariant because composition is respected:
\[
(g\circ f)_\* \;=\; g_\* \circ f_\*, \qquad (\mathrm{id}_X)_\*=\mathrm{id}.
\]
Direct images do not work for this purpose. If \(A_1,A_2,\dots\) are disjoint in \(X\), their images \(f(A_i)\) need not be disjoint in \(Y\), so countable additivity would be lost. Inverse images preserve exactly the structure a measure needs.

There is a second, equivalent point of view. Consider the assignment that sends a measurable space \(X\) to the set of all measures on \(X\). Then \(f\colon X\to Y\) induces a map \(f_\*\colon \mathrm{Measures}(X)\to \mathrm{Measures}(Y)\). This assignment is a covariant functor from measurable spaces to sets.

## Contravariant Transport Of Observables

Let \(g\colon Y\to\mathbb{R}\) be measurable. Transport it back along \(f\) by composition,
\[
f^\* g \;=\; g\circ f \colon X \to \mathbb{R}.
\]
This is the pullback of \(g\). It is contravariant because composition reverses:
\[
(g\circ f)^\* \;=\; f^\* \circ g^\*, \qquad (\mathrm{id}_Y)^\*=\mathrm{id}.
\]
Again there is a functorial point of view. Fix a target space of values, say \(\mathbb{R}\). The assignment that sends a measurable space \(Y\) to the set \(\mathrm{Obs}(Y)=\{g\colon Y\to\mathbb{R} \text{ measurable}\}\) and sends \(f\colon X\to Y\) to \(f^\*\colon \mathrm{Obs}(Y)\to \mathrm{Obs}(X)\) is a contravariant functor.

## Adjunction Via Integration

Pushforward and pullback are not independent tricks. They are tied by the integral. For a measure \(\mu\) on \(X\) and an observable \(g\) on \(Y\),
\[
\int_Y g(y)\, d\bigl(f_\*\mu\bigr)(y)
\;=\;
\int_X (g\circ f)(x)\, d\mu(x).
\]
On the left the measure moves forward. On the right the observable moves back. The equality says that these two transports fit perfectly. This is the integral form of an adjunction written \(f^\* \dashv f_\*\): pullback is left adjoint to pushforward with respect to the pairing given by integration.

There is an abstract way to see this. The integral defines a bilinear pairing between observables on a space and measures on that space. Pullback acts on the observable side, pushforward acts on the measure side, and the pairing is preserved.

## Distributions As Transported Measures

A random variable is a measurable map \(X\colon \Omega \to \mathbb{R}\). The base probability \(P\) on \(\Omega\) is transported along \(X\) to a measure on \(\mathbb{R}\) given by
\[
P_X(B) \;=\; P\!\bigl(X^{-1}(B)\bigr).
\]
This is the distribution of \(X\). It is nothing more or less than a pushforward. Marginal distributions are pushforwards along projection maps; for \(\pi_X\colon X\times Y\to X\),
\[
(\pi_X)_\*(\mu)(A) \;=\; \mu\!\bigl(A\times Y\bigr).
\]
Conditioning is of a different kind. For an event \(B\) with positive mass, the conditional \(P(\,\cdot\,\mid B)\) is \(A \mapsto P(A\cap B)/P(B)\). This is a restriction to a slice followed by renormalisation, not a transport along an arrow.

## From Categories To Statistical Practice

A statistical model sends parameters and covariates to a distribution for an outcome. In a frequentist workflow a single estimate \(\hat{\boldsymbol{\beta}}\) for the coefficient vector \(\boldsymbol{\beta}\) is chosen and predictions are read conditionally at fixed covariates; uncertainty bands describe the sampling distribution of \(\hat{\boldsymbol{\beta}}\) under repeated sampling. In a Bayesian workflow the posterior over \(\boldsymbol{\beta}\) is transported through the model. With covariates fixed at representative values,
\[
p(y^\* \mid \text{data})
\;=\;
\int p\!\bigl(y^\* \mid \boldsymbol{\beta}\bigr)\, p(\boldsymbol{\beta}\mid \text{data})\, d\boldsymbol{\beta},
\]
which is a pushforward of the posterior through the model map. The curve with credible bands is the image of that transported mass in the outcome space.

## A Discrete Case With Dice

Take \(\Omega=\{\omega_1,\dots,\omega_6\}\) with the power-set σ-algebra and the uniform probability \(P(\{\omega_i\})=1/6\). Map faces to numbers by \(X\colon \Omega \to \mathbb{R}\) with \(X(\omega_i)=i\). The distribution is the pushforward \(P_X\) satisfying
\[
P_X(\{k\}) \;=\; P\!\bigl(X^{-1}(\{k\})\bigr) \;=\; \tfrac{1}{6}
\quad\text{for } k=1,\dots,6.
\]

Map faces to parity by \(f\colon \Omega \to \{\text{odd},\text{even}\}\) with \(f(\omega_i)=\text{parity}(i)\). The pushed measure on parity satisfies
\[
f_\*P(\{\text{even}\}) = P(\{2,4,6\}) = \tfrac12,
\qquad
f_\*P(\{\text{odd}\}) = P(\{1,3,5\}) = \tfrac12.
\]

Define an observable on parity \(g\colon \{\text{odd},\text{even}\}\to\mathbb{R}\) by \(g(\text{even})=1\) and \(g(\text{odd})=0\). The pullback \(f^\* g = g\circ f\) is the indicator of \(\{2,4,6\}\) on \(\Omega\). The adjunction through the integral reads
\[
\int_{\{\text{odd},\text{even}\}} g\, d(f_\*P)
\;=\;
\int_\Omega f^\* g \, dP
\;=\;
\tfrac12.
\]
