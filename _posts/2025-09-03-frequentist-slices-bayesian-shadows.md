---
layout: post
title: "Frequentist Slices, Bayesian Shadows"
date: 2025-09-03
categories: probability measure-theory bayesian
---

## Marginal vs. Conditional Predictions

The central difference between frequentist and Bayesian statistics is how they treat the unknown.  
In the frequentist view, parameters are fixed but unknown constants, and probability describes variation in the data under repeated sampling.  
In the Bayesian view, the data are fixed once observed, and it is the parameters themselves that are uncertain, described by probability distributions.  

This contrast becomes concrete when we make predictions. Frequentists usually condition on fixed parameter estimates, while Bayesians average over the entire range of plausible parameter values. To see why, it helps to return to the foundations of probability in measure theory.

---

## Probability as a Pushforward

A probability space is a triple $(\Omega, \mathcal{F}, P)$, where  

- $\Omega$ is the set of all possible outcomes,  
- $\mathcal{F}$ is a collection of measurable subsets of $\Omega$,  
- $P$ is the probability measure assigning each event a number in $[0,1]$.

A random variable is a measurable function  

$$
X: \Omega \to \mathbb{R}.
$$

Its distribution is the **pushforward** of $P$ through $X$:  

$$
P_X(B) = P\!\big(X^{-1}(B)\big), \quad B \subseteq \mathbb{R}.
$$

In words: the probability that $X$ lands in a set $B$ is the probability of all original outcomes $\omega$ that map into $B$.  

**Example.** If $\Omega$ is the six faces of a die with uniform measure $P$, and $X(\text{face } k) = k$, then the pushforward is the uniform distribution on $\{1,\dots,6\}$. The function $X$ transfers the measure from die faces to numbers.  

Every probability distribution can be seen as the pushforward of a measure through a function. Marginals and conditionals are different ways of doing this.

## Conditionals in Frequentist Predictions

In the frequentist framework, parameters are treated as fixed but unknown constants.  
When we make predictions, we typically insert point estimates of these parameters into the model.  
This produces what is called a **conditional prediction**: we condition on the chosen parameter values and then describe the variability of the outcome.  

Consider a regression model of the form  

$$
Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon.
$$

Suppose we are interested in the effect of elevation $x_1$, while soil moisture $x_2$ is another predictor.  
To visualize the role of elevation, we fix soil moisture at some reference value, for example $x_2 = 20\%$, and plot  

$$
E[Y \mid x_1, x_2 = 0.2] = \beta_0 + \beta_1 x_1 + \beta_2 \cdot 0.2.
$$

The fitted line is conditional on soil moisture being set at 20% and on the estimated parameters $\hat{\boldsymbol{\beta}}$ (the hat denotes that these are estimates of the true but unknown coefficients $\boldsymbol{\beta}$).
The surrounding uncertainty band comes from the sampling distribution of these estimates: if we repeatedly drew new datasets from the same true model, 95% of such bands would contain the true regression line.

Frequentist prediction plots are conditional in two senses:  
they are conditional on fixed values of covariates and conditional on fixed parameter estimates.

## Marginals in Bayesian Predictions

In the Bayesian framework, the parameters are not fixed constants but uncertain quantities.  
Their uncertainty is described by a posterior distribution, which combines the prior and the likelihood.  
Predictions are then obtained by averaging over this full distribution rather than plugging in a single estimate.  

Using the same regression model,  

$$
Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon,
$$

we again want to study the effect of elevation $x_1$ while holding soil moisture at $x_2 = 20\%$.  
Instead of inserting point estimates for $\boldsymbol{\beta}$, we integrate over the entire posterior distribution:

$$
p(y^* \mid x_1, x_2 = 0.2, \text{data})  
= \int p(y^* \mid x_1, x_2 = 0.2, \boldsymbol{\beta}) \, p(\boldsymbol{\beta} \mid \text{data}) \, d\boldsymbol{\beta}.
$$

This is a **marginal prediction**: we marginalize over parameter uncertainty to obtain a predictive distribution for $y^*$.  
From this distribution, we can summarize the mean prediction and a credible interval.  
The credible interval has a direct probability interpretation: given the data and prior, there is a 95% probability that the outcome lies within that range.  

Unlike the frequentist approach, the Bayesian view does not condition on fixed parameter values.  
Instead, it integrates across all plausible parameter values, weighting each according to its posterior probability.  
The resulting prediction plot shows the mean curve with credible bands, reflecting the full uncertainty.

## Slices and Shadows

The difference between conditional and marginal predictions can be pictured with a simple metaphor.  
Imagine the joint posterior distribution of two regression coefficients, say $\beta_1$ for elevation and $\beta_2$ for soil moisture.  
This distribution is a three-dimensional mountain rising over the $(\beta_1, \beta_2)$ plane.  

- A **conditional view** is like taking a vertical slice through the mountain at $\beta_2 = c$.  
  We pretend soil moisture is known exactly and examine how plausible different values of $\beta_1$ are along that slice.  
  This corresponds to the frequentist habit of fixing parameters at chosen values.  

- A **marginal view** is like shining light along the $\beta_2$ axis so the entire mountain casts a shadow onto the $\beta_1$ axis.  
  At each point on the $\beta_1$ axis, we accumulate all the probability mass across $\beta_2$.  
  This corresponds to the Bayesian practice of averaging over parameter uncertainty.  

## Predictions as Pushforwards

Seen through measure theory, both traditions are constructing pushforwards.  
The difference is in what is treated as fixed and what is averaged over.  
Frequentist predictions push forward a single slice of parameter space, holding coefficients fixed at their estimates.  
Bayesian predictions push forward the entire posterior, letting its uncertainty spread into the outcome space.  

What we plot, whether a regression line with a confidence band or a curve with a credible band, is the trace of this pushforward.
