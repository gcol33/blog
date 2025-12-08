---
layout: post
title: "How Long Until the Bus?"
date: 2025-09-05
categories: probability paradox everyday-math
---

## Catch It If You Can

You arrive at the stop. The sign says buses come every 10 minutes. Your watch says you should be fine.

But the street is empty. Five minutes pass. Seven. A distant growl—just a truck. Finally, after nine long minutes, the bus arrives, already packed.

It feels like you always catch the long gaps. Bad luck, you think.

But the buses really do average 10 minutes apart. The problem isn't your luck. It's statistics. A phenomenon called the **inspection paradox**: whenever arrivals are irregular, the gaps you land in tend to be longer than average.

The more variability, the longer the wait.

---

## The Clockwork World

Imagine a city where buses run exactly on time. One arrives every $T$ minutes, no exceptions.

If you show up at a random moment, you're equally likely to land anywhere in that $T$-minute slot. Your wait $W$ is uniformly distributed:

$$
f_W(w) = \frac{1}{T}, \qquad 0 \leq w \leq T
$$

The average wait:

$$
\mathbb{E}[W] = \frac{T}{2}
$$

Mean interval $T$, mean wait $T/2$. Half the gap. Clean and predictable.

---

## The Chaotic World

Now consider the opposite extreme. Buses arrive at random, following a Poisson process. The mean gap is still $T$—exactly the same as before. What changes is the variability. Most gaps are short. Some are long. But on average, $T$.

If you arrive at a random moment, your wait is exponentially distributed:

$$
P(W > w) = e^{-w/T}, \qquad \mathbb{E}[W] = T
$$

Same mean interval. But the mean wait is no longer $T/2$. It's the full $T$.

The extra variability doubles your expected wait.

---

## The General Rule

Both cases follow a single formula. Let $S$ be the random interval between buses. The expected wait is:

$$
\mathbb{E}[W] = \frac{\mathbb{E}[S^2]}{2\,\mathbb{E}[S]}
$$

This reveals why variance matters. If gaps never vary ($\mathrm{Var}(S) = 0$), the mean wait is $T/2$. As variability increases, so does the wait. For exponential gaps with $\mathrm{Var}(S) = T^2$, the mean wait reaches $T$.

Variance isn't just noise. It's time stolen from passengers.

---

## Why This Formula Holds

Two facts combine:

**1. Long gaps are more likely to be sampled.** The chance of landing in a gap of length $s$ is proportional to $s$. A 20-minute gap covers twice as much time as a 10-minute gap, so you're twice as likely to arrive during it.

**2. Once inside a gap, your wait is uniform.** If the gap is length $s$, your expected wait is $s/2$.

Formally, the density of the gap containing your arrival is:

$$
f_{\text{sampled}}(s) = \frac{s \, f_S(s)}{\mathbb{E}[S]}
$$

Conditioning on landing in a gap of length $s$, the mean wait is $s/2$. Combining:

$$
\mathbb{E}[W] = \int_0^\infty \frac{s}{\mathbb{E}[S]} \cdot \frac{s}{2} \, f_S(s)\, ds = \frac{\mathbb{E}[S^2]}{2\,\mathbb{E}[S]}
$$

This is the inspection paradox formula.

---

## A Toy Example

Ten buses spread across 100 minutes. Five gaps are 5 minutes long; five are 15 minutes long. The mean gap is $(5 \times 5 + 5 \times 15)/10 = 10$ minutes.

Now imagine 100 passengers, one arriving each minute.

- 25 land in short gaps (5 gaps × 5 minutes each)
- 75 land in long gaps (5 gaps × 15 minutes each)

Three times as many passengers experience the long waits. The average wait across all passengers is 6.75 minutes—not the 5 minutes you'd expect from perfect regularity.

Long gaps cover more time. More people land inside them. The schedule average and the passenger average diverge.

---

## Not Just Buses

The same effect appears wherever people sample processes by being inside them.

**Class sizes.** A department offers four classes: one with 80 students, one with 10, two with 5. The average class size is $(80 + 10 + 5 + 5)/4 = 25$. But ask the 100 students what class size they experience, and their answers average to 65.5. Large classes dominate because most students are in them.

**Flights.** Airlines fly plenty of half-empty planes, but those planes carry few passengers. Full planes carry many. Survey passengers, and most report crowded flights.

**Checkout lines.** Some queues are short, others long. Pick a random shopper and they're probably in one of the long ones. Averaging over people gives longer waits than averaging over queues.

**Server response times.** A website responds in milliseconds most of the time, but occasionally takes 30 seconds. The average response time might be 2 seconds. But most users experience slow periods, because slow periods last longer.

In every case, individuals are more likely to land in bigger or longer groups. The experienced average exceeds the scheduled average.

---

## The Scorecard

| Schedule type | Mean gap | Mean wait |
|---------------|----------|-----------|
| Regular (clockwork) | $T$ | $T/2$ |
| Poisson (random) | $T$ | $T$ |
| Irregular (variable) | $T$ | between $T/2$ and $T$ |

The schedule average and the passenger average measure different things. Schedules average over intervals. Passengers average over time spent inside them.

That's why standing at the bus stop feels worse than the timetable suggests. You're not sampling buses. You're sampling the gaps between them—and long gaps, by definition, take up more of your time.
