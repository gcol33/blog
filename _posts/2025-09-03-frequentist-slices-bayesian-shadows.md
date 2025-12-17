---
layout: post
title: "Frequentist Slices, Bayesian Shadows"
date: 2025-09-03
categories: probability measure-theory bayesian
---

## The Same Model, Two Different Answers

You fit a regression model predicting tree growth from elevation and soil moisture. You want to know: how does elevation affect growth?

A frequentist hands you a plot with a line and a confidence band. A Bayesian hands you a plot with a line and a credible band. The lines are similar. The bands look similar. But they mean completely different things.

The frequentist band says: if we repeated this experiment many times, 95% of such bands would contain the true line.

The Bayesian band says: given what we observed, there's a 95% probability the true value lies here.

Same data. Same model. Different answers to different questions. The difference comes down to a choice: do you slice through uncertainty, or let it cast a shadow?

---

## A Mountain of Uncertainty

Picture the joint posterior distribution of two regression coefficients—$\beta_1$ for elevation, $\beta_2$ for soil moisture. This distribution forms a three-dimensional mountain rising over the $(\beta_1, \beta_2)$ plane. The peak sits where the parameters are most plausible; the slopes fall away toward less likely combinations.

Now suppose you want to report just the effect of elevation, $\beta_1$. You have two options.

**Slice.** Take a vertical cut through the mountain at some fixed value of $\beta_2$—say, the point estimate. You're left with a one-dimensional curve: the distribution of $\beta_1$ *given that* $\beta_2$ equals exactly that value. This is conditioning. It's what frequentists typically do.

**Shadow.** Shine light along the $\beta_2$ axis so the entire mountain casts a shadow onto the $\beta_1$ axis. At each point, you accumulate all the probability mass across every possible $\beta_2$. This is marginalizing. It's what Bayesians typically do.

The slice is sharp. It pretends $\beta_2$ is known. The shadow is diffuse. It admits $\beta_2$ could be many things.

---

## Pushforwards: The Machinery Behind Both

Measure theory provides the language for what's happening here. A probability distribution is a **pushforward**—a way of transferring measure from one space to another through a function.

Start with a probability space $(\Omega, \mathcal{F}, P)$: outcomes $\Omega$, measurable sets $\mathcal{F}$, and a measure $P$. A random variable $X: \Omega \to \mathbb{R}$ maps outcomes to numbers. The distribution of $X$ is defined by pushing $P$ forward through $X$:

$$
P_X(B) = P\big(X^{-1}(B)\big)
$$

The probability that $X$ lands in $B$ equals the probability of all outcomes that map into $B$.

Roll a die. Let $X$ assign the number on the top face. The pushforward of the uniform measure on six faces is the uniform distribution on $\{1, \ldots, 6\}$. The function $X$ transfers the measure from physical faces to abstract numbers.

---

## Frequentist Predictions: Conditioning on the Slice

In frequentist regression, parameters $\boldsymbol{\beta}$ are fixed but unknown. We estimate them from data, then plug those estimates into the model.

Consider:

$$
Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon
$$

To visualize the effect of elevation $x_1$, we fix soil moisture at a reference value—say $x_2 = 0.2$—and plot:

$$
\mathbb{E}[Y \mid x_1, x_2 = 0.2] = \hat\beta_0 + \hat\beta_1 x_1 + \hat\beta_2 \cdot 0.2
$$

The hat marks estimates. The line is conditional on two things: fixed covariate values *and* fixed parameter estimates.

The confidence band comes from the sampling distribution of $\hat{\boldsymbol{\beta}}$. It answers a hypothetical question: if we repeated this experiment infinitely many times, how often would such bands contain the true line?

This is a slice through parameter space—a single point, plus the variation from sampling.

---

## Bayesian Predictions: Casting the Shadow

In Bayesian regression, parameters are uncertain quantities with a posterior distribution. Predictions integrate over this entire distribution rather than conditioning on a single point.

Same model:

$$
Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon
$$

Same goal: the effect of elevation at $x_2 = 0.2$. But now we average:

$$
p(y^* \mid x_1, x_2 = 0.2, \text{data}) = \int p(y^* \mid x_1, x_2 = 0.2, \boldsymbol{\beta}) \, p(\boldsymbol{\beta} \mid \text{data}) \, d\boldsymbol{\beta}
$$

The posterior $p(\boldsymbol{\beta} \mid \text{data})$ weights each parameter combination by its plausibility. The integral sums their contributions.

The credible band has a direct interpretation: given the data, there's a 95% probability the outcome lies within this range. No hypothetical repetitions required.

This is the shadow—the full uncertainty of the parameter mountain, projected onto the prediction.

---

## What the Plots Actually Show

Both approaches produce a curve with a band. The visual similarity obscures a deep difference.

|   | Frequentist | Bayesian |
|:--|:--|:--|
| **Parameters** | Fixed unknowns | Random variables |
| **Band meaning** | Coverage under repetition | Direct probability |
| **Uncertainty source** | Sampling variability | Posterior distribution |
| **Metaphor** | Slice | Shadow |

The frequentist slices through the mountain at a single point, then asks how that slice might wobble across repeated samples. The Bayesian lets the whole mountain cast its shadow, incorporating every plausible parameter combination.

---

## The Same Machinery, Different Inputs

Seen through measure theory, both traditions construct pushforwards. The difference lies in what they push forward.

Frequentists push a single slice of parameter space—estimates held fixed—into the outcome space. Bayesians push the entire posterior, letting its uncertainty propagate into predictions.

The regression line you plot, whether adorned with confidence or credible bands, traces the image of this pushforward. The question is whether you sliced first, or let the shadow fall.
