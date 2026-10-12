---
layout: post
title: "Simpson's Paradox"
date: 2026-01-12
categories: probability statistics paradox
toc: true
---

## A Drug Trial Gone Wrong

A hospital tests a new drug. Among patients who received it, 78% recovered. Among those who didn't, 82.6% recovered. The drug appears harmful.

But look at the breakdown by severity:

**Mild cases:**
- Drug group: 81 of 87 recovered (93%)
- Control group: 234 of 270 recovered (87%)

**Severe cases:**
- Drug group: 192 of 263 recovered (73%)
- Control group: 55 of 80 recovered (69%)

The drug improves recovery in mild cases. It improves recovery in severe cases. Yet when you combine the groups, recovery is worse with the drug.

This is Simpson's Paradox: a trend that appears in subgroups can reverse or disappear when the subgroups are combined.

---

## The Arithmetic

The numbers aren't a trick of rounding. They follow from how the patients were distributed.

|  | Drug | Control |
|--|------|---------|
| Mild | 81 of 87 (93%) | 234 of 270 (87%) |
| Severe | 192 of 263 (73%) | 55 of 80 (69%) |
| **Total** | **273 of 350 (78%)** | **289 of 350 (82.6%)** |

The drug wins in both subgroups but loses overall.

The key is patient allocation. Most drug patients had severe cases (263 of 350, or 75%), while most control patients had mild cases (270 of 350, or 77%). Severe cases have lower recovery rates regardless of treatment. When you pool the data, this imbalance drags down the drug group's overall rate.

Verify the totals:

$$
\text{Drug: } \frac{81 + 192}{87 + 263} = \frac{273}{350} = 78\%
$$

$$
\text{Control: } \frac{234 + 55}{270 + 80} = \frac{289}{350} = 82.6\%
$$

The aggregate reverses the subgroup pattern because severity—which affects both treatment assignment and outcome—isn't held constant.

---

## See It Happen

The subgroup recovery rates stay fixed at the trial's values. Only the split of patients between mild and severe cases changes, with 350 patients per arm.

{% include figure.html src="simpsons-paradox-allocation.svg" alt="Three panels of recovery percentages for drug (filled circles) and control (open circles) in mild cases, severe cases and all patients. Mild: 93 vs 87 and severe: 73 vs 69 in every panel. All patients: 83 vs 78 with equal allocation, 78 vs 83 when most drug patients are severe, 89 vs 73 when most drug patients are mild." %}

With 175 mild and 175 severe patients in each arm, the drug wins overall as well, 83.1% against 77.7%. There is no paradox when the groups are balanced.

With the trial's allocation, 263 of 350 drug patients (75%) are severe against 80 of 350 (23%) in control, and the drug loses overall, 78.0% against 82.6%.

Swapping the allocation, so that most drug patients are mild, gives 88.5% against 73.2%. The drug now looks far better overall than it does in either subgroup. The aggregate comparison moves with the allocation while the subgroup comparisons stay where they are.

---

## Berkeley, 1973

The paradox made headlines in a 1975 paper by Bickel, Hammel, and O'Connell examining graduate admissions at UC Berkeley.

The aggregate numbers looked damning:

|  | Applicants | Admitted |
|--|------------|----------|
| Men | 8,442 | 44% |
| Women | 4,321 | 35% |

A nine-point gap. The university faced accusations of discrimination.

But when the researchers examined individual departments, the pattern reversed. In most departments, women were admitted at equal or higher rates than men. Four of the six largest departments favored women.

The explanation: women applied disproportionately to competitive departments (English, History) with low acceptance rates for everyone. Men applied more often to less competitive departments (Engineering, Chemistry) with high acceptance rates for everyone.

The admissions process within each department showed no bias. The aggregate showed a gap because of where candidates chose to apply.

---

## Kidney Stones, 1986

A study compared two treatments for kidney stones: open surgery (Treatment A) and a newer, less invasive procedure (Treatment B).

|  | Treatment A | Treatment B |
|--|-------------|-------------|
| Small stones | 93% success (81/87) | 87% success (234/270) |
| Large stones | 73% success (192/263) | 69% success (55/80) |
| **Overall** | **78% success (273/350)** | **83% success (289/350)** |

Treatment A wins in both categories but loses overall.

The reason: doctors assigned the newer, gentler Treatment B to easier cases (small stones). Treatment A, being more invasive, was reserved for difficult cases (large stones). When you ignore stone size and just count successes, Treatment B looks better because it was given to patients who would have done well anyway.

This matters for medical decisions. A patient with large kidney stones should prefer Treatment A, despite its worse aggregate numbers.

---

## The Confounding Variable

Simpson's Paradox arises when a third variable influences both the grouping and the outcome.

In the drug example, severity determines both which treatment patients receive (sicker patients get the drug) and how likely they are to recover (sicker patients do worse). Severity is a **confounding variable**.

Graphically:

{% include figure.html src="simpsons-paradox-confounding.svg" alt="Causal diagram: Severity causes both Treatment and Recovery; Treatment causes Recovery." %}

Severity affects treatment assignment. Severity affects recovery. If you ignore severity, you conflate its effect with the treatment's effect.

The solution is **stratification**: analyze within levels of the confounder. The drug works in mild cases and works in severe cases. That's the real story. The aggregate is misleading because it mixes two different populations.

---

## When to Pool, When to Split

The paradox raises a practical question: which answer is right? Should we trust the subgroup analysis or the aggregate?

There's no universal rule. It depends on the causal structure.

**Pool when** the subgroups are arbitrary divisions that don't affect the outcome. If you split patients by birth month and find different treatment effects in each month, you should probably pool—birth month isn't a cause of recovery.

**Split when** the subgroups reflect a genuine confounder that affects both treatment and outcome. If sicker patients systematically receive one treatment and do worse regardless of treatment, you need to control for severity.

The Berkeley case is instructive. Should we pool across departments or not? It depends what question you're asking. If you're asking "Are admissions committees biased?", split by department—that's where decisions happen. If you're asking "Do women face barriers to graduate education at Berkeley?", the aggregate might matter, because whatever steered women toward competitive departments is part of the system.

---

## Simpson, Yule, and the History

The paradox carries Edward Simpson's name from his 1951 paper, but the phenomenon was known earlier.

Udny Yule noted in 1903 that correlations could reverse when populations were combined, and Karl Pearson described similar reversals around the same time. Some call it the Yule-Simpson effect.

The name "paradox" overstates the case. Once you understand confounding, the reversal is arithmetically inevitable under certain conditions. The surprise comes from expecting aggregates to preserve subgroup relationships—an expectation that probability doesn't guarantee.

---

## Aggregation and Interpretation

Averages are summaries, and summaries discard information. When the discarded information matters, the summary misleads. The same numbers support opposite conclusions depending on which comparisons you make, and choosing the right comparison requires understanding the causal structure: what causes what, and what you're trying to learn.
