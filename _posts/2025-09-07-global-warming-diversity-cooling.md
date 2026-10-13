---
layout: post
title: "Global Warming and Diversity Cooling"
date: 2025-09-07
categories: ecology thermodynamics
toc: true
---

## The Same Collapse, Twice

When a gas cools, its molecules slow down. They explore fewer states. The number of possible configurations drops, and entropy decreases.

Something similar happens when an ecosystem collapses. Species vanish, the community becomes dominated by a few survivors, and the system settles into a smaller set of possible configurations. The entropy of the living community falls, though the mechanism is competition and extinction rather than thermodynamics.

One equation describes both:

$$
H = -\sum_i p_i \log p_i
$$

In physics, $p_i$ is the probability of a microstate. In ecology, $p_i$ is the fraction of individuals belonging to species $i$. In both cases the formula counts possibilities.

Global warming raises temperatures, and it also *cools* ecosystems in this entropic sense: as the planet heats up, biological diversity declines and communities become simpler and more uniform.

---

## Removing Species

Start with 10 species of roughly equal abundance and remove the rarest one at each step. Most of its share (70%) goes to the most abundant species, the rest is spread evenly over the survivors. Entropy drops with every removal.

{% include figure.html src="global-warming-diversity-cooling-collapse.svg" alt="Top: species shares in a community of 10, 7, 4 and 2 species after repeatedly removing the rarest species. Bottom: Shannon entropy H against the number of species remaining, from 10 down to 2, with the curve log S for equal shares shown dashed." %}

The community starts at $H = 2.30$, about 9.9 effective species ($e^H$). By the time two species remain, one of them holds 82% of all individuals, and $H = 0.47$, or 1.6 effective species. The gap to the dashed curve grows as dominance builds up: the entropy falls faster than the species count alone would explain.

---

## Boltzmann's Tombstone

The connection between entropy and counting goes back to Ludwig Boltzmann.

In the 1870s, Boltzmann argued in Vienna that the laws of heat, work, and efficiency could be explained by statistics. Count all the ways particles can arrange themselves, he argued, and entropy falls out naturally.

His formula:

$$
S = k \log W
$$

$W$ is the number of microstates compatible with a given macrostate. $k$ is Boltzmann's constant. The more ways a system can be arranged while looking the same from the outside, the higher its entropy.

The physics establishment resisted. Ernst Mach and others denied that atoms even existed. Boltzmann grew isolated and depressed. In 1906, while on holiday in Duino near Trieste, he took his own life.

The equation was later carved on his tombstone in Vienna's Zentralfriedhof. Within a few years, Jean Perrin's experiments on Brownian motion confirmed that atoms exist.

---

## Shannon's Surprise

In 1948 Claude Shannon, an engineer at Bell Labs, was working on the limits of communication.

His question: how much information can you send through a noisy channel? To answer it, he needed a way to measure uncertainty. If you're about to receive a message, how surprised will you be by each symbol?

Shannon defined a quantity he called entropy:

$$
H = -\sum_i p_i \log p_i
$$

If all symbols are equally likely, uncertainty is high. If one symbol dominates, uncertainty is low. The formula captured the average "surprise" of a message source.

When Shannon showed his work to John von Neumann, von Neumann reportedly said: "You should call it entropy, for two reasons. First, the formula is the same as in statistical mechanics. Second, nobody really understands entropy, so in any debate you'll have the advantage."

Whether or not the story is true, Shannon had arrived at the entropy of statistical mechanics from entirely different premises.

---

## Same Formula, Different Systems

The entropy formula measures *possibilities*, regardless of what those possibilities represent.

In a gas, $p_i$ is the probability of microstate $i$, and entropy measures how spread out the system is across configurations. In a message, $p_i$ is the probability of symbol $i$, so entropy captures average surprise per symbol. Apply the same formula to an ecosystem, where $p_i$ is the fraction of individuals belonging to species $i$, and you get a measure of how evenly the community is distributed.

The formula counts equivalent configurations that produce the same observable outcome.

---

## A Tale of Two Forests

Consider two forests, each with 1000 trees and 4 species.

**Forest A (balanced):**
- Oak: 250 trees
- Maple: 250 trees
- Birch: 250 trees
- Pine: 250 trees

**Forest B (dominated):**
- Oak: 850 trees
- Maple: 50 trees
- Birch: 50 trees
- Pine: 50 trees

Both have the same *richness* (4 species). Their entropies differ.

For Forest A:

$$
H_A = -4 \times \left(\frac{1}{4} \log \frac{1}{4}\right) = \log 4 \approx 1.386
$$

For Forest B:

$$
H_B = -\left(0.85 \log 0.85 + 3 \times 0.05 \log 0.05\right) \approx 0.543
$$

Forest A has more than twice the entropy of Forest B.

What does this mean? Pick a random tree. In Forest A, each species is equally likely. In Forest B, guess "Oak" and you're right 85% of the time.

The "effective number of species", $e^H$, captures this:
- Forest A: $e^{1.386} = 4.0$ effective species
- Forest B: $e^{0.543} = 1.7$ effective species

Forest B has 4 species but the diversity of 1.7 equally common ones.

---

## What Heat Does to Diversity

Now consider what happens as climate changes.

Species have thermal tolerances. As temperatures rise, some can't cope:
- They fail to reproduce
- They're outcompeted by heat-tolerant generalists
- Their food sources disappear
- Their habitats shrink

The species that survive tend to be the same everywhere: widespread, adaptable, generalist species. Ecologists call this *biotic homogenization*.

Similar shifts have been reported across ecosystems:
- Coral reefs lose specialist species; weedy corals take over
- Forests lose endemic understory plants; invasive grasses spread
- Streams lose sensitive mayflies; pollution-tolerant midges dominate

In each case, the community shifts from Forest A toward Forest B. Richness drops, a few species become dominant, and entropy falls.

---

## The Thermodynamic Irony

In the physical sense, global warming adds heat to the Earth system. Temperatures rise. You might expect entropy to increase, since hotter systems explore more states.

In the biological sense the opposite happens: communities lose species, the number of possible ecological configurations shrinks, and the Shannon entropy of species abundances decreases.

The planet heats up while life, in the entropic sense, cools down.

Physical entropy and ecological entropy measure different things, so there is no contradiction. Both count possible configurations, of molecules in one case and of individuals among species in the other.

---

## Energy Flow and Order

Life on Earth runs on the *flow* of energy from high-quality (low entropy) to low-quality (high entropy).

Sunlight arrives as concentrated, high-frequency photons. Plants capture it, store it in chemical bonds, and pass it up the food chain. Eventually, the same energy radiates back to space as diffuse infrared: the same total energy, spread across many more photons, at much higher entropy.

This flow from order to disorder powers every living thing. Schrödinger described organisms as feeding on "negative entropy": living systems maintain their structure by exporting entropy to their environment.

An ecosystem is a dissipative structure in this sense: it maintains its complexity by channeling that flow of energy.

---

## What We Lose

A species is a node in a network of interactions, a repository of genetic information, and a way of making a living that took millions of years to evolve.

When diversity declines, the losses include:

- **Functional redundancy**: Multiple species doing similar jobs means the ecosystem can absorb shocks
- **Ecosystem services**: Pollination, decomposition, water filtration, carbon storage
- **Evolutionary potential**: The raw material for future adaptation
- **Information**: Each species carries genetic adaptations to its own survival problems

Low abundance entropy often goes with low functional redundancy, which can leave a community less able to absorb further change.

---

## The Equation on the Tombstone

Boltzmann's formula links microscopic chaos to macroscopic order. Shannon adapted it to communication. Ecologists applied it to species abundances.

Heating the planet changes which species can persist. As communities lose species and come to be dominated by a few, the entropy of the living world falls.
