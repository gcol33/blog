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

In physics, $p_i$ is the probability of a microstate. In ecology, $p_i$ is the fraction of individuals belonging to species $i$. The formula doesn't care which world it measures. It counts possibilities.

And here's the twist: global warming doesn't just raise temperatures. It *cools* ecosystems in the entropic sense. As the planet heats up, biological diversity collapses. The living world becomes simpler, more uniform, more predictable.

In the entropic sense, the living world is getting colder.

---

## Removing Species

Start with 10 species of roughly equal abundance and remove the rarest one at each step. Most of its share (70%) goes to the most abundant species, the rest is spread evenly over the survivors. Entropy drops with every removal.

{% include figure.html src="global-warming-diversity-cooling-collapse.svg" alt="Top: species shares in a community of 10, 7, 4 and 2 species after repeatedly removing the rarest species. Bottom: Shannon entropy H against the number of species remaining, from 10 down to 2, with the curve log S for equal shares shown dashed." %}

The community starts at $H = 2.30$, about 9.9 effective species ($e^H$). By the time two species remain, one of them holds 82% of all individuals, and $H = 0.47$, or 1.6 effective species. The gap to the dashed curve grows as dominance builds up: the entropy falls faster than the species count alone would explain.

---

## Boltzmann's Tombstone

The connection between entropy and counting goes back to Ludwig Boltzmann.

In the 1870s, Boltzmann was fighting a lonely battle in Vienna. He believed that thermodynamics—the rules governing heat, work, and efficiency—could be explained by statistics. Count all the ways particles can arrange themselves, he argued, and entropy falls out naturally.

His formula:

$$
S = k \log W
$$

$W$ is the number of microstates compatible with a given macrostate. $k$ is Boltzmann's constant. The more ways a system can be arranged while looking the same from the outside, the higher its entropy.

The physics establishment resisted. Ernst Mach and others denied that atoms even existed. Boltzmann grew isolated and depressed. In 1906, while on vacation in Trieste, he took his own life.

The equation was later carved on his tombstone in Vienna's Zentralfriedhof. Within a decade, atoms were confirmed, and Boltzmann's vision became the foundation of statistical mechanics.

---

## Shannon's Surprise

An engineer at Bell Labs in 1948 was trying to understand the limits of communication, with no interest in physics. His name was Claude Shannon.

His question: how much information can you send through a noisy channel? To answer it, he needed a way to measure uncertainty. If you're about to receive a message, how surprised will you be by each symbol?

Shannon defined a quantity he called entropy:

$$
H = -\sum_i p_i \log p_i
$$

If all symbols are equally likely, uncertainty is high. If one symbol dominates, uncertainty is low. The formula captured the average "surprise" of a message source.

When Shannon showed his work to John von Neumann, von Neumann reportedly said: "You should call it entropy, for two reasons. First, the formula is the same as in statistical mechanics. Second, nobody really understands entropy, so in any debate you'll have the advantage."

Whether the story is true or not, Shannon had independently arrived at Boltzmann's formula, starting from completely different premises.

---

## The Formula Doesn't Care

The entropy formula measures *possibilities*, regardless of what those possibilities represent.

In a gas, $p_i$ is the probability of microstate $i$, and entropy measures how spread out the system is across configurations. In a message, $p_i$ is the probability of symbol $i$, so entropy captures average surprise per symbol. Apply the same formula to an ecosystem, where $p_i$ is the fraction of individuals belonging to species $i$, and you get a measure of how evenly the community is distributed.

Same arithmetic, different subject matter. The formula counts equivalent configurations that produce the same observable outcome.

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

Both have the same *richness* (4 species). Their entropies differ dramatically.

For Forest A:

$$
H_A = -4 \times \left(\frac{1}{4} \log \frac{1}{4}\right) = \log 4 \approx 1.386
$$

For Forest B:

$$
H_B = -\left(0.85 \log 0.85 + 3 \times 0.05 \log 0.05\right) \approx 0.543
$$

Forest A has more than twice the entropy of Forest B.

What does this mean? Pick a random tree. In Forest A, you genuinely don't know what species you'll get. In Forest B, guess "Oak" and you're right 85% of the time. The community is predictable, uniform, simple.

The "effective number of species"—defined as $e^H$—captures this:
- Forest A: $e^{1.386} = 4.0$ effective species
- Forest B: $e^{0.543} = 1.7$ effective species

Forest B has 4 species on paper. It has 1.7 species worth of diversity.

---

## What Heat Does to Diversity

Now consider what happens as climate changes.

Species have thermal tolerances. As temperatures rise, some can't cope:
- They fail to reproduce
- They're outcompeted by heat-tolerant generalists
- Their food sources disappear
- Their habitats shrink

The species that survive tend to be the same everywhere: widespread, adaptable, generalist species. Ecologists call this *biotic homogenization*.

The pattern is consistent across ecosystems:
- Coral reefs lose specialist species; weedy corals take over
- Forests lose endemic understory plants; invasive grasses spread
- Streams lose sensitive mayflies; pollution-tolerant midges dominate

In each case, the community shifts from Forest A toward Forest B. Richness drops. The remaining species become dominant. Entropy falls.

---

## The Thermodynamic Irony

In the physical sense, global warming adds heat to the Earth system. Temperatures rise. You might expect entropy to increase—hotter systems explore more states.

But in the biological sense, the opposite happens. Ecosystems become simpler. Communities lose species. The number of possible ecological configurations shrinks. Shannon entropy—applied to species abundances—decreases.

The planet heats up while life, in the entropic sense, cools down.

Physical entropy and ecological entropy measure different things, so there is no contradiction. But both track possibilities, and the parallel is instructive: fewer possible configurations means less structure and less capacity to absorb further disturbance.

---

## Energy Flow and Order

There's a deeper connection still.

Life on Earth doesn't run on heat. It runs on the *flow* of energy from high-quality (low entropy) to low-quality (high entropy).

Sunlight arrives as concentrated, high-frequency photons. Plants capture it, store it in chemical bonds, and pass it up the food chain. Eventually, the same energy radiates back to space as diffuse infrared—same total energy, but spread across many more photons, much higher entropy.

This flow—from order to disorder—powers every living thing. Schrödinger called it "negentropy." Living systems maintain their structure by exporting entropy to their environment.

Global warming disrupts this flow. Greenhouse gases trap outgoing infrared, reducing the rate at which Earth can shed entropy. The gradient flattens.

A healthy ecosystem is a dissipative structure—it maintains complexity by channeling energy flow. When the flow is disrupted, the structure simplifies. Species drop out. Communities homogenize. Entropy, in the ecological sense, falls.

---

## What We Lose

A species is not just a name on a list. It's a node in a network of interactions, a repository of genetic information, a way of making a living that took millions of years to evolve.

When diversity collapses, we lose more than species:

- **Functional redundancy**: Multiple species doing similar jobs means the ecosystem can absorb shocks
- **Ecosystem services**: Pollination, decomposition, water filtration, carbon storage
- **Evolutionary potential**: The raw material for future adaptation
- **Information**: Each species encodes solutions to survival problems we may never understand

The entropy formula captures something real: the number of ways an ecosystem can be configured while still functioning. When that number drops, the system becomes brittle. It loses its ability to respond to further change.

A low-entropy ecosystem is like a language with only a few words. You can still communicate, but you've lost the capacity for precision and adaptation.

---

## The Equation on the Tombstone

Boltzmann's formula links microscopic chaos to macroscopic order. Shannon adapted it to communication. Ecologists applied it to species abundances. The mathematics is the same; the systems are not.

When we burn fossil fuels and heat the planet, we trigger a cascade that runs through physics, chemistry, and biology. Temperatures rise. Species shift and vanish. Communities simplify. The entropy of the living world falls.

That the formula on Boltzmann's tombstone appears in ecology textbooks is not a coincidence. Both track the number of possible configurations a system can occupy. The living world is losing its configurations, one species at a time.
