---
layout: post
title: "Global Warming and Diversity Heating"
date: 2025-09-07
categories: ecology thermodynamics
---

## From Temperature to Shannon’s Index  

Before instruments, people gauged heat by sensation. Galileo’s thermoscope in the 1600s showed relative changes, and later scales by Fahrenheit and Celsius made them reproducible. Kelvin gave an absolute zero, tying temperature to physical law.  

A naive view is that temperature measures molecular motion. Faster molecules mean hotter matter. This is true for gases, where translational motion dominates, but too simple elsewhere. Ice at 0 °C still has vibrating molecules but stays solid. Metals with similar average motion conduct heat differently. Something deeper was hidden.  

---

## Carnot, Clausius, and Kelvin  

In 1824, Sadi Carnot showed that the *maximum* efficiency of a steam engine depends only on the *difference* between two temperatures. Rudolf Clausius later defined entropy:  

$$
dS = \frac{\delta Q}{T}
$$  

Entropy was a state function, and temperature a universal quantity. Kelvin then set an absolute scale, defining temperature beyond any chosen substance.  

## Boltzmann and Gibbs: Microstates and Macrostates  

Ludwig Boltzmann provided the missing bridge. A **macrostate** is the bulk description of a system—pressure, volume, energy. A **microstate** is a single detailed arrangement of all particles consistent with that macrostate.  

Entropy counts the multiplicity of microstates:  

$$
S = k \log W
$$  

where \(W\) is the number of microstates.  

Temperature then emerges from:  

$$
\frac{1}{T} = \frac{\partial S}{\partial E}
$$  

So temperature is not motion itself. It is about how quickly the number of microstates grows when energy increases.  

Josiah Willard Gibbs expanded this with ensembles: probability distributions over many possible microstates, providing the modern foundation of statistical mechanics.  

## Shannon: Information as Microstates  

Claude Shannon, in 1948, looked at messages. The **macrostate** is the overall distribution of symbols, the **microstates** are individual sequences of letters. His entropy was:  

$$
H = -\sum_i p_i \log p_i
$$  

This counts the number of possible messages consistent with the observed frequencies. It is the same structure as Boltzmann’s formula.  

## Diversity: Species as Microstates  

Ecologists faced the same challenge. Richness (number of species) is a macrostate. But what matters is also how individuals are distributed among species. Each different way of assigning individuals to species is a microstate.  

Shannon’s index became the natural measure:  

$$
H = -\sum_i p_i \log p_i
$$  

where $p_i$ is the relative abundance of each species.  

## Worked Example: Communities  

- **Community A:** 4 species, each with 25 individuals.  
- **Community B:** 4 species; one with 85 individuals, the rest with 5 each.  

Both macrostates have richness = 4. Their microstate variety differs:  

For A:  

$$
H_A = -\sum_{i=1}^4 0.25 \log 0.25 = 1.386
$$  

For B:  

$$
H_B = -[0.85\log 0.85 + 3 \times 0.05 \log 0.05] = 0.543
$$  

Same richness, very different entropy.  

## Whittaker’s α, β, and γ Diversity  

Robert H. Whittaker, in the 1960s, formalized how diversity scales:  

- **Alpha (α):** diversity within a single community.  
- **Gamma (γ):** total diversity across a whole region.  
- **Beta (β):** turnover, linking them as  

$$
\beta = \frac{\gamma}{\alpha}
$$  

This mirrors physics. A single community’s diversity (α) is like entropy within one subsystem. Regional diversity (γ) is like entropy of the whole ensemble. Beta diversity is the difference between them (the diversity of macrostates across space).  

### Worked Example: Scaling  

Three plots:  

- Plot 1: species A, B  
- Plot 2: species B, C  
- Plot 3: species C, D  

Each plot has α = 2. Regionally, γ = 4. Then:  

$$
\beta = \frac{\gamma}{\alpha} = \frac{4}{2} = 2
$$  

High turnover: each plot contributes new species, just as each subsystem adds distinct microstates in statistical mechanics.  

## Global Warming and Diversity Heating  

Most people think we live from the Sun’s heat. But the Earth is already close to thermal equilibrium with the Sun. What drives life is not raw heat, but the flow of **low entropy energy** (the difference between incoming sunlight and outgoing radiation). That difference builds order. It allows complex structures to exist, from molecules to forests. When species are lost, that order fades. Communities collapse toward uniformity. Diversity heats as entropy rises.
