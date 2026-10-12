---
layout: post
title: "De Méré's Dice Paradox"
date: 2025-09-06
categories: probability paradox history
toc: true
excerpt: "In 1654, a French nobleman had a problem. Two gambling wagers that seemed identical by his reasoning behaved differently at the tables. One made money over time. The other slowly drained it."
---

## When $1+1$ Is Not $2$

In 1654, a French nobleman named Antoine Gombaud—better known as the Chevalier de Méré—had a problem. Two gambling wagers that seemed identical by his reasoning behaved differently at the tables. One made money over time. The other slowly drained it.

De Méré was no mathematician. But he knew someone who was. He brought the puzzle to Blaise Pascal, then thirty-one and already famous for his work on vacuum and pressure.

Pascal took the problem seriously. He wrote to Pierre de Fermat, a magistrate in Toulouse who pursued mathematics in his spare time. Over several months, the two exchanged letters dissecting de Méré's wagers.

That correspondence laid the foundations of probability theory.

---

## The Two Wagers

De Méré described two bets:

1. Roll a single die 4 times. Bet that at least one six appears.
2. Roll two dice 24 times. Bet that at least one double-six appears.

At first sight, they look equivalent.

A single die has probability $1/6$ of showing a six. The expected number of sixes in 4 rolls:

$$
4 \times \frac{1}{6} = \frac{2}{3}
$$

A pair of dice has probability $1/36$ of showing double-six. The expected number of double-sixes in 24 rolls:

$$
24 \times \frac{1}{36} = \frac{2}{3}
$$

Same expectation. De Méré reasoned that if the expected count of successes is the same, the probability of winning should be the same.

The gambling tables disagreed.

---

## The First Wager: One Die, Four Rolls

The probability of *no* six in a single roll is $5/6$. Four independent rolls:

$$
\left(\frac{5}{6}\right)^4 \approx 0.482
$$

So the probability of *at least one* six:

$$
1 - \left(\frac{5}{6}\right)^4 \approx 0.518
$$

Slightly favorable. Bet this long enough, and you win.

---

## The Second Wager: Two Dice, Twenty-Four Rolls

The probability of *no* double-six in a single roll is $35/36$. Twenty-four rolls:

$$
\left(\frac{35}{36}\right)^{24} \approx 0.509
$$

So the probability of *at least one* double-six:

$$
1 - \left(\frac{35}{36}\right)^{24} \approx 0.491
$$

Slightly unfavorable. Bet this long enough, and you lose.

---

## Why the Results Differ

Both wagers give the same expected number of successes: $2/3$. But the probability of winning differs. The reason: two different measures are involved.

**Expectation is linear.** If each trial has probability $p$ of success, then $n$ trials have expected successes $np$. Double the trials, double the expectation. Simple addition.

**Probability of at least one success is nonlinear.** It equals $1 - (1-p)^n$. Failures compound. When $p$ is small, $(1-p)^n$ stays close to 1 even for moderately large $n$.

In the first wager, the event is common enough (probability $1/6$) that one of four trials usually succeeds. In the second wager, the event is rare (probability $1/36$). Twenty-four trials aren't enough to overcome the compounding failures.

De Méré assumed scaling trials would compensate for scaling probabilities. Expectation scales linearly, but the probability of winning does not.

---

## Ten Thousand Rounds

The difference between 51.8% and 49.1% is small. Over a few games, luck dominates. But over hundreds of rounds, the edge becomes visible.

The figure follows both wagers through 10,000 simulated rounds, plotting each wager's running win rate (solid: one die, 4 rolls; dashed: two dice, 24 rolls) against the exact probabilities shown as thin horizontal lines.

{% include figure.html src="de-mere-dice-win-rate.svg" alt="Running win rate of both wagers over 10,000 simulated rounds on a logarithmic axis, with horizontal lines at the exact probabilities 51.77% and 49.14%" %}

After 100 rounds the losing wager is still ahead, 51% against 46%. Only after several hundred rounds do the two curves separate in the right order, and after 10,000 rounds they sit at 52.2% and 49.6%, close to their exact values.

---

## The Same Trap Today

The confusion between expectation and probability appears far beyond dice.

**Lotteries.** A ticket costing &#36;2 with a 1-in-10-million chance at &#36;10 million has expected value near &#36;1. Buy a million tickets and your expected return is about &#36;1 million. But your probability of winning even once is still only about 10%. Expectation scales; probability does not.

**Medical screening.** A test with 99% sensitivity and 1% false positive rate sounds reliable. If the disease prevalence is 0.1%, most positive results are false positives. The expected number of true positives per thousand tests is about 1. The probability that *your* positive result is correct is only about 9%. Doctors routinely confuse these.

**Rare risks.** The expected number of fatal accidents on a commute might be 0.0001 per trip. Over 10,000 trips, the expectation is 1. But the probability of at least one fatal accident is about 63% (by $1 - e^{-1}$), not 100%. Expectation and probability diverge most sharply for rare events repeated many times.

The linear intuition that works for averages misleads when applied to probabilities, and the confusion is as common now as it was in 1654.

---

## The Pascal-Fermat Correspondence

Pascal's letters to Fermat did more than resolve a gambling puzzle. They introduced methods for counting arrangements, dividing stakes fairly, and reasoning systematically about future outcomes. Within a generation, Christiaan Huygens had turned that correspondence into the first textbook on probability, and Jacob Bernoulli would use Pascal's methods to prove the law of large numbers. By the eighteenth century, Laplace had extended these ideas to astronomy, insurance, and the theory of errors.

De Méré himself never understood the mathematics, but the letter he prompted Pascal to write traveled further than any of his wagers.
