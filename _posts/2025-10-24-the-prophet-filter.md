---
layout: post
title: "The Prophet Filter"
date: 2025-10-24
categories: probability perception history
---

## From Omens to Equations

For most of history, randomness was not random.  
The flight of birds, the pattern of smoke, the turn of dice, all were seen as signs of intent.  
Uncertainty was interpreted, not measured.

This began to change in the seventeenth century.  
Games of chance turned belief into arithmetic.  
Jacob Bernoulli showed that repeating a random experiment brings its outcomes closer to fixed proportions, a principle later known as the *law of large numbers*.  
Laplace extended these ideas to astronomy and population data, showing that chance could describe both error and prediction.  
In the twentieth century, Andrey Kolmogorov gave probability its modern form: a mathematical measure on a space of events.  
Randomness no longer needed divine explanation.  

---

## The Prophet Experiment

Consider a modern oracle who sends predictions by email.  
Each message claims perfect accuracy.  
At first, thousands receive it. After every event, half of the recipients are removed, those who saw the wrong prediction.  
The next message goes only to those who received the correct one.  

After several rounds, a small group remains who have *never* seen the oracle fail.  
To them, the sender appears infallible.  
The illusion requires no foresight, only scale and elimination.  

---

## The Mathematics of the Filter

Let each prediction be a Bernoulli trial with success probability $p = 1/2$.  
After $N$ independent rounds, the number of perfect streaks follows a binomial law:

$$
P(X = k) = \binom{N}{k} p^k (1 - p)^{N - k}.
$$

The expected number of people with an unbroken streak of $N$ correct predictions is  

$$
E[X] = M p^N,
$$

where $M$ is the initial number of recipients.  
If $M = 10^6$ and $N = 10$, then  

$$
E[X] = 10^6 \times \left(\frac{1}{2}\right)^{10} \approx 976.
$$

Almost a thousand people will see ten perfect predictions, not because of prophecy, but because of simple arithmetic.  

Each round halves the population and doubles their certainty.  
The “prophet” survives statistical pruning.  

---

## Forgetting the Failures

The same effect governs memory.  
Aristotle noted that people who dream of a shipwreck and later hear of one think they foresaw it, forgetting countless dreams that never matched reality.  
This is a failure of counting: remembered hits are few, forgotten misses are many.

If the probability of a match is $p$ and there are $N$ independent dreams, the chance of at least one match is

$$
P(X \ge 1) = 1 - (1 - p)^N.
$$

For small $p$, this approximates to $Np$.  
Even when $p$ is tiny, large $N$ makes coincidences inevitable.

---

## Rare Events at Scale

When $p$ is small and $N$ large, the binomial distribution approaches a Poisson law with rate $\lambda = Np$.  
In this case,

$$
P(X = 0) = e^{-\lambda}, \qquad P(X \ge 1) = 1 - e^{-\lambda}.
$$

Once $\lambda > 1$, the probability of at least one event rises sharply toward certainty.

A one-in-100,000 event ($p = 10^{-5}$) across eight billion independent trials ($N = 8\times10^9$) gives  

$$
\lambda = Np = 80{,}000,
$$  

and  

$$
P(X \ge 1) = 1 - e^{-80{,}000} \approx 1.
$$  

Coincidences of enormous improbability must occur somewhere simply because there are enough chances for them to happen.

---

## The Meaning of Certainty

The “prophet filter” describes a simple mechanism: selection without replacement.  
False cases vanish; surviving ones appear perfect.  
The same principle drives scams, forecasts, and even published research, where visible success hides invisible failure.

Probability does not explain belief, but it shows why belief can arise so easily.  
Remove what disproves it, and what remains looks inevitable.
