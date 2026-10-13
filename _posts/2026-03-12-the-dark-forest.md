---
layout: post
title: "The Dark Forest"
date: 2026-03-12
categories: probability paradox
toc: true
excerpt: "In 1950, a physicist asked why the galaxy is silent. The answer may be game theory: when the cost of contact is extinction and every encounter is one-shot, silence can be the rational strategy."
---

## Where Is Everybody?

In the summer of 1950, Enrico Fermi and three colleagues at Los Alamos were on their way to lunch. They had been discussing reports of flying saucers and a recent *New Yorker* cartoon showing aliens stealing trash cans from the streets of New York. At lunch, the conversation moved on to other subjects. Fermi then asked: "Where is everybody?" His colleagues understood that he meant extraterrestrial civilizations.

This account rests on recollections that Edward Teller, Emil Konopinski and Herbert York wrote down in 1984, collected in Eric M. Jones's 1985 Los Alamos report [“Where Is Everybody?” An Account of Fermi's Question](https://digital.library.unt.edu/ark:/67531/metadc1096088/). The exact wording is uncertain, and 1950 is the most likely year rather than a documented one.

Fermi reportedly followed his question with rough calculations about the likelihood of life on other planets and the development of technological civilizations. If such civilizations were common, some might have existed long before humanity. And if interstellar travel were possible, at least some might have reached Earth by now. Yet there was no evidence that any had.

Today, we know that the Milky Way contains roughly 100 billion stars and that planets are common. A civilization capable of travelling between stars could, in principle, spread across the galaxy in a few million years, far less than its age. Even if only a small proportion of civilizations attempted this, there has been ample time for some to reach our part of the galaxy.

Yet we have found no confirmed evidence of extraterrestrial technology. Perhaps technological life is extremely rare. Perhaps civilizations rarely survive long enough to spread, or have little reason to do so. It is also possible that evidence exists but that we have not recognized it.

This is the Fermi paradox: given the size and age of the galaxy, why have we found no evidence of other civilizations?

---

## The Arithmetic of Contact

Fermi's question stayed in the air. Over the next decade, radio astronomy matured, and the search for extraterrestrial intelligence became something that could be funded rather than joked about. By 1961, enough serious people cared that the National Academy of Sciences sponsored a small meeting at Green Bank, West Virginia, to discuss how one might detect alien civilizations. Frank Drake, one of the astronomers at the meeting, tried to organize the guesswork by breaking the question into a chain of factors: how many stars form per year, what fraction have planets, how often life arises, how often it becomes intelligent, how often it builds radios, and how long such civilizations last. He wrote the product on a blackboard.

$$
N = R_* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L
$$

None of the values on the right side are known. Plug in pessimistic estimates ($R_* = 1$, $f_p = 0.2$, $n_e = 1$, $f_l = 0.1$, $f_i = 0.1$, $f_c = 0.1$, $L = 10{,}000$ years) and you get $N = 2$. We are one. There should be at least one other.

With optimistic estimates ($f_l = 0.5$, $f_i = 0.5$, $L = 10^6$), $N$ reaches 5,000, and yet no radio search has found a confirmed signal, which brings us back to the question Fermi asked at lunch.

---

## The Contact Game

Suppose two civilizations discover each other across interstellar space. Each faces a choice: **signal** (reveal yourself, attempt communication) or **stay silent** (hide, observe, do nothing).

If both signal and both are peaceful, they trade knowledge, share science, and both gain. Call this payoff $V$. But if you signal and the other civilization turns out to be hostile, you have revealed your location to something that wants you gone, and the cost of that mistake is extinction: $-C$. Staying silent guarantees a payoff of $0$ regardless of what the other side does or is.

The expected value of signaling depends on the probability $p$ that the other civilization is hostile:

$$
\mathbb{E}[\text{signal}] = (1-p) \cdot V - p \cdot C
$$

$$
\mathbb{E}[\text{silent}] = 0
$$

Signaling is rational only when $(1-p) \cdot V > p \cdot C$, which gives:

$$
p < \frac{V}{V + C}
$$

When the benefit of contact is modest ($V = 1$, say, representing scientific exchange) and the cost of being wrong is extinction ($C = 1000$), the threshold is $p < 0.001$. You need better than 99.9% confidence that the other civilization is peaceful before signaling makes sense.

And there is no data on $p$: no civilization we know of has ever met another.

---

## Playing It Out

{% include figure.html src="the-dark-forest-threshold.svg" alt="Signal threshold p = V/(V+C) against extinction cost C on log axes, with V = 1; the region below the curve, where signaling is rational, is shaded; points mark p = 5% at C = 2 and C = 100, and p = 20% at C = 2." %}

The curve is the threshold $p = V/(V+C)$ with $V = 1$. Below it signaling has positive expected value; above it silence wins. At a hostility probability of 5% and an extinction cost of 100, the threshold is $p < 0.99\%$, and 5% lies far above it. A civilization that does the arithmetic stays silent, and its score sits at zero round after round.

{% include figure.html src="the-dark-forest-rounds.svg" alt="Cumulative score over 100 rounds of the contact game with V = 1 and a fixed random seed, extinctions marked by open circles. Left: p = 5% with a new civilization each round, for C = 100 (flat at zero) and C = 2 (rising to 91). Right: p = 20% and C = 2, for the same civilization every round (rising to 94) and a new civilization each round (rising to 40)." %}

Lower $C$ to 2 (contact is risky but not existential) and the threshold jumps to $p < 33\%$. Now signaling is rational at 5% hostility, and over 100 rounds against a new civilization each time the score climbs to 91, despite three extinctions along the way. The difference between a quiet universe and a noisy one is the ratio of what you stand to lose to what you stand to gain.

The right panel raises the hostility probability to 20%, still under the 33% threshold. Facing the same civilization every round, both extinctions happen in the first two rounds; once a peaceful partner is found, every later round is safe, and the score reaches 94. Facing a new civilization each round, the extinctions keep coming, 20 of them in 100 rounds, and the score ends at 40.

---

## The Chain of Suspicion

The calculation above assumes you know $p$. In practice, $p$ is unknown.

Even a civilization that is peaceful today might not be peaceful tomorrow. A species that poses no threat at your current level of development might surpass you in a thousand years, and a thousand years is nothing on galactic timescales. You cannot verify intentions across interstellar distances, and you cannot monitor compliance with any agreement.

Liu Cixin, whose novel gives this post its title, calls the result a chain of suspicion. Even if you are peaceful and they are peaceful, you cannot be sure they know you are peaceful. And even if they know, you cannot be sure they know that you know. The uncertainty propagates: each level of "I think they think I think..." adds doubt, and the doubt compounds.

In a one-shot game with no communication channel and existential stakes, the chain of suspicion drives $p$ upward regardless of anyone's actual intentions. A civilization that would cooperate if it could verify the other's nature stays silent because verification is impossible.

---

## Once Versus a Thousand Times

In the Cold War, the United States and Soviet Union played a deterrence game repeatedly over four decades. They built channels: the hotline between Washington and Moscow, arms control treaties, summit meetings, the informal rules of engagement that developed after each crisis. Each peaceful resolution added evidence that the other side preferred survival over victory. Reputation accumulated. Trust, or at least predictability, emerged.

The folk theorem of repeated games formalizes this. When two players expect to interact indefinitely and value future payoffs enough, cooperation can be sustained as an equilibrium. Strategies like tit-for-tat (cooperate until the other defects, then punish, then forgive) stabilize cooperation because the future cost of losing a cooperative partner exceeds the one-time gain from defection.

Cosmic contact has none of these features. The distances are measured in light-years, a signal takes decades or centuries to cross the gap, and the civilizations on either end may not even exist in the same millennium. Iteration requires proximity, and proximity is exactly what interstellar space denies. Each contact event is, for practical purposes, a one-shot game with a stranger.

In a one-shot Prisoner's Dilemma, the dominant strategy is to defect. In the contact game, where the cost of being wrong is extinction and the benefit of being right is modest, the one-shot version collapses to silence for any civilization that has done the arithmetic. The Fermi Paradox may be what a universe of such civilizations looks like from the outside.

---

## The Dark Forest

In his 2008 novel *The Dark Forest*, the Chinese science fiction writer Liu Cixin gave this reasoning its best-known image. The universe, in his telling, is a dark forest. Every civilization is a hunter moving through the trees, unable to know whether the shadow ahead is a deer or another hunter with a rifle. Revealing your position, by signaling, by broadcasting, by doing anything that makes you visible, invites destruction from anyone who has done the expected-value calculation and drawn the rational conclusion.

Liu grounded the metaphor in two axioms: survival is the primary need of every civilization, and civilizations grow continuously while the total matter in the universe does not. Under these conditions, any other civilization is a potential competitor for finite resources, and the safest response to detection is a preemptive strike.

In the novel, the civilizations that broadcast were eliminated by selection at a cosmic scale, and the ones that survived learned to hide. If that picture were right, the silence we observe would be the equilibrium of this process, which raises a question about what humans have already done.

---

## What METI Risks

When the Arecibo radio telescope in Puerto Rico was upgraded in 1974, a group of astronomers celebrated by aiming it at the globular cluster M13 and transmitting a three-minute encoded message. It was a symbolic gesture, since M13 is 25,000 light-years away, but it was a deliberate announcement of our presence.

More recently, a project called METI (Messaging Extraterrestrial Intelligence) has advocated sending targeted signals to nearby star systems, which are close enough that a reply could arrive within a human lifetime. If the contact game is a reasonable model, this is a decision with asymmetric consequences. The benefit of a response is scientific knowledge. The cost of attracting the wrong attention is unbounded, and the decision is made by a handful of people on behalf of everyone else.

One of the most vocal advocates for transmission, a Russian physicist named Alexander Zaitsev who spent decades operating the Evpatoria planetary radar, has argued that a civilization advanced enough to threaten us would already know we are here from our television signals, our radar emissions, the atmospheric composition of our planet. Deliberate transmission adds little to what we already leak. The counter-argument: leaked signals are faint and transient, while a targeted transmission at high power toward a specific star is a qualitatively different act, one that says "we are here and we want to be found."

No treaty governs interstellar transmission.

---

## The Uncomfortable Ratio

Return to the threshold:

$$
p < \frac{V}{V + C}
$$

For signaling to be rational, the probability of hostility must be less than $V/(V+C)$. When $C$ is large relative to $V$, this threshold is tiny.

The formula encodes an asymmetry. Contact with a peaceful civilization yields knowledge, trade, cultural exchange, all finite goods. Getting it wrong yields extinction, which is permanent and total. When one side of a bet is finite and the other is unbounded, the expected-value calculation is dominated by the unbounded side regardless of how small its probability.

This is the same structure that makes Pascal's Wager compelling and simultaneously suspicious. The argument works whenever $C$ can be made arbitrarily large. In the contact game, $C$ stands for a physical outcome, extinction, rather than a stipulated infinite reward.

Every proposed resolution to the Fermi Paradox encodes an assumption about what civilizations value and what they fear. The contact game encodes one specific assumption: that extinction is permanent and cooperation with strangers is unverifiable. Under those conditions, the expected-value calculation points toward silence for any $C$ large enough relative to $V$, and the threshold is low enough that most reasonable priors on hostility exceed it. Whether the universe actually works this way depends on quantities we cannot measure from a single data point, which is all we have.
