---
layout: post
title: "De Méré's Dice Paradox"
date: 2025-09-06
categories: probability paradox history
---

## When $1+1$ Is Not $2$

In seventeenth century France, Antoine Gombaud, better known as Chevalier de Méré, took a serious interest in games of chance. He observed that certain wagers with dice behaved differently from what simple reasoning suggested. His questions reached Blaise Pascal, who discussed them with Pierre de Fermat in 1654. The exchange between these two mathematicians is now seen as the starting point of modern probability theory.

---

## The Two Wagers

De Méré described two forms of play:

1. Roll a single die $4$ times. The wager is that at least one six appears.  
2. Roll two dice $24$ times. The wager is that at least one double six appears.

At first sight they look the same. A single die has probability $1/6$ of showing a six. The expected number of sixes in $4$ rolls is  

$$
4 \times \frac{1}{6} = \frac{2}{3}.
$$

A pair of dice has probability $1/36$ of showing double six. The expected number of double sixes in $24$ rolls is  

$$
24 \times \frac{1}{36} = \frac{2}{3}.
$$

Both wagers seem to offer the same expectation of successes. It is natural to think they should have the same chance of winning.

## The First Wager: One Die, Four Rolls

The probability of no six in a single roll is $5/6$. Four independent rolls give  

$$
\left(\frac{5}{6}\right)^4 \approx 0.482.
$$

So the probability of at least one six is  

$$
1 - \left(\frac{5}{6}\right)^4 \approx 0.518.
$$

This wager is slightly favorable.

## The Second Wager: Two Dice, Twenty Four Rolls

The probability of no double six in a single roll is $35/36$. Twenty four rolls give  

$$
\left(\frac{35}{36}\right)^{24} \approx 0.509.
$$

So the probability of at least one double six is  

$$
1 - \left(\frac{35}{36}\right)^{24} \approx 0.491.
$$

This wager is slightly unfavorable.

## Why the Results Differ

The expectation of successes in both cases is the same, $\;2/3\;$. What differs is the probability of at least one success.  

Expectation counts the average number of favorable outcomes, but probability of winning counts the chance that one occurs at all. The second wager involves a rarer event. It is more likely to cluster or to be missed entirely, which lowers the chance of success.

## The Historical Impact

De Méré’s questions showed how unreliable intuition can be when dealing with chance. Pascal and Fermat worked out the correct probabilities in their correspondence of 1654. That exchange is remembered as a turning point: from practical puzzles about gambling to the foundations of probability as a field of mathematics.
