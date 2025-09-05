---
layout: post
title: "How Long Until the Bus?"
date: 2025-09-05
categories: probability paradox everyday-math
---

## Catch It If You Can

You arrive at the stop. The sign promised a bus every $10$ minutes. Your watch says you should be fine. But the street is empty. $5$ minutes. $7$ minutes. A faint growl of an engine, only a truck. Finally, after $9$ long minutes, the bus arrives, already full of tired faces.  

It feels like you are unlucky, always catching the long gaps. Yet the buses really do average $10$ minutes apart. The reason is not bad luck but statistics. A simple effect called the *inspection paradox*.  

Whenever arrivals are irregular, the gaps you fall into are likely to be longer than average. The more irregularity, the longer the wait.

---

## The Simple World: Clockwork Buses

Imagine a city where buses really do run on time. One comes exactly every $T$ minutes. If you arrive at a random instant, you are equally likely to land anywhere in that $T$ minute slot. Your wait $W$ is uniform:  

$$
f_W(w) = \frac{1}{T}, \qquad 0 \leq w \leq T
$$

and the average is  

$$
\mathbb{E}[W] = \tfrac{T}{2}.
$$

The mean interval is $T$ and the mean wait is exactly half of it. Simple and predictable.

## The Chaotic World: Poisson Buses

Now consider the other extreme. Buses arrive at random, following a Poisson process. **The mean gap between buses is still $T$, exactly the same as in the regular case.** What changes is the variability. The gaps are exponential: many are short, some are long, but on average $T$.  

If you arrive at a random instant, your wait $W$ is also exponential:  

$$
P(W > w) = e^{-w/T}, \qquad \mathbb{E}[W] = T.
$$

So the mean interval is still $T$, but the mean wait is not $T/2$: It is the full $T$. The extra variability doubles the expected wait. Same mean interval, different passenger experience.

## The General Rule

Both cases fit a more general formula. Let $S$ be the interval between buses. Then the expected waiting time is  

$$
\mathbb{E}[W] = \frac{\mathbb{E}[S^2]}{2\,\mathbb{E}[S]}.
$$

This shows why variance matters. If the gaps never vary, then $\mathrm{Var}(S) = 0$ and the mean wait is $T/2$. As variability grows, the mean wait grows with it. For exponential gaps, $\mathrm{Var}(S) = T^2$, giving a mean wait of $T$.

## Why This Formula Holds

Suppose the distribution of gaps is given by $S$. To compute the average wait for a random passenger, two facts matter:

1. **Long gaps are more likely to be sampled.** The chance of landing in an interval of length $s$ is proportional to $s$.  
2. **Once inside a gap of length $s$, the wait is uniform on $[0,s]$ with mean $s/2$.**

Formally, the density of the gap containing the arrival is  

$$
P(S=s) \propto s \, f_S(s),
$$  

where $f_S$ is the density of $S$. Normalizing gives  

$$
P(S=s) = \frac{s f_S(s)}{\mathbb{E}[S]}.
$$  

Conditioning on $S=s$, the mean wait is $s/2$. Putting this together:  

$$
\mathbb{E}[W] = \int_0^\infty \frac{s}{\mathbb{E}[S]} \cdot \frac{s}{2} f_S(s)\, ds
= \frac{\mathbb{E}[S^2]}{2 \,\mathbb{E}[S]}.
$$

This is the **inspection paradox formula.**

## A Toy Example

Take ten buses spread across $100$ minutes. Five gaps are $5$ minutes, five are $15$ minutes. The mean gap is still $10$.  

One passenger arrives each minute. That means $25$ of them fall in short gaps and $75$ in long ones. The average wait is  

$$
\frac{5 \cdot (15+14+\dots+1) + 5 \cdot (5+4+\dots+1)}{100} = 6.75.
$$

Instead of $5.5$ minutes from perfect regularity, the average wait increases. Long gaps cover more time, so more people land inside them.

## Not Just Buses

The same effect shows up in many situations.

**Lecture halls.** A department offers one class of $80$, one of $10$, and two of $5$. The true average class size is  

$$
\frac{80+10+5+5}{4} = 25.
$$  

But if you ask the $100$ students, their answers average to $65.5$. Large classes dominate the sample because most students are in them.

**Flights.** Airlines operate plenty of half empty planes, but they carry few passengers. Full planes carry many. If you ask passengers, most will report crowded flights.

**Checkout lines.** In a supermarket, some queues are short, others are long. Pick a random shopper and chances are they are in one of the long queues. Averaging over people makes the waits longer than averaging over queues.

**Servers.** A website responds quickly most of the time but sometimes takes $30$ seconds. The average response time may be $2$ seconds, but most users experience the slow periods. Long delays dominate.

In every case, individuals are more likely to be found in the bigger or longer groups. The result is an average that looks worse than the underlying schedule.

## The Scorecard

Compare the cases:

- **Regular schedule:** mean gap $T$, mean wait $T/2$.  
- **Poisson schedule:** mean gap $T$, mean wait $T$.  
- **Irregular schedule:** mean gap $T$, mean wait between $T/2$ and $T$.  

The schedule average and the passenger average are not the same. Schedules average over intervals. Passengers average over time spent inside them. That difference is why the long gaps are so hard to avoid.
