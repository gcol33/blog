---
layout: post
title: "Leaky Locks"
date: 2025-12-06
categories: security information-theory history
toc: true
---

## What Counts as Information?

At DEF CON in 2016, a security researcher who goes by Plore opened high-security safe locks from Sargent and Greenleaf without drilling them and without trying every code.

He tapped the wires that power the lock and watched the current while entering codes. When a digit was correct, the rise in current came about 28 microseconds later, and the more correct digits, the later it came. To stay clear of the lock's penalty, a 10-minute shutdown after five wrong attempts, he cut the power after each guess, and he got the whole attack down to 15 minutes.

A lock that reveals its digits one at a time can be opened one digit at a time. Try 0 through 9 in the first position until the delay appears, then move to the second. A four-digit code has 10,000 combinations; found this way, it falls in at most 40 tries.

The lock protected the code. It didn't protect *information about* the code.

---

## The Collapse

Here is the mathematics of what happens when structure leaks.

A password with $n$ positions, each drawn from an alphabet of size $k$, has $k^n$ possible values. For a 4-digit PIN:

$$
10^4 = 10{,}000 \text{ attempts}
$$

But if the system reveals whether each position is correct independently, the attacker solves each position separately:

$$
k \times n = 10 \times 4 = 40 \text{ attempts}
$$

The exponent becomes a multiplier. Security collapses from $k^n$ to $kn$.

| Secret length | Without leak | With leak | Collapse |
|---------------|--------------|-----------|----------|
| 4 digits      | 10,000       | 40        | 250× |
| 8 lowercase   | 208 billion  | 208       | 1 billion× |
| 12 mixed      | $10^{21}$    | 744       | $10^{18}$× |

---

## The Collapse, Visualized

{% include figure.html src="leaky-locks-collapse.svg" alt="Attempts needed against secret length n on a log scale, k to the n without leak and k times n with leak, for alphabet sizes k = 10, 26 and 62" %}

---

## Paul Kocher's Discovery

In 1996, Paul Kocher published a paper showing that even when software reveals nothing explicitly, the *time it takes to compute* is itself a channel.

Consider password verification:

```
def check(input, stored):
    for i in range(len(stored)):
        if input[i] != stored[i]:
            return False
    return True
```

This code returns as soon as it finds a mismatch. A wrong first character fails in one microsecond. A wrong last character takes eight microseconds, and that timing difference plays the same role as the delayed current in the safe lock.

Kocher demonstrated the attack against RSA implementations. By measuring how long decryption took for different inputs, he could extract private keys bit by bit, from implementations that revealed nothing through any official channel. In 2003, David Brumley and Dan Boneh showed that a timing attack of this kind also works over a network.

---

## The Expanding Boundary

If timing is information, what else might be?

**1985: Van Eck radiation.** Every wire is an antenna. CRT monitors emit electromagnetic radiation that depends on what they display. Wim van Eck showed you could reconstruct screen contents from across the street. Later researchers demonstrated the same for LCD screens, keyboards, and network cables.

**1998: Power analysis.** Kocher again. The power consumed by a chip varies with the operations it performs. Different instructions draw different current. By measuring power consumption during cryptographic operations, attackers could extract keys from smart cards.

**2003: Cache timing.** Modern CPUs have memory caches. Accessing cached data is fast; uncached data is slow. An attacker who shares your CPU can deduce what memory addresses you're touching, including cryptographic key material.

**2018: Spectre and Meltdown.** Modern CPUs speculate. When they hit a conditional branch, they guess which way it will go and start executing down that path. If the guess is wrong, they roll back. This is speculative execution, and it makes processors fast.

Meltdown exploited the fact that Intel chips performed speculative memory accesses before checking permissions. A user program could speculatively read kernel memory. The CPU would eventually realize the access was forbidden and discard the result, but not before the data had touched the cache. By measuring which cache lines were now fast to access, attackers could reconstruct the forbidden bytes.

Spectre was subtler. It trained the branch predictor to mispredict, then used that misprediction to speculatively access memory through the victim's own code. The victim's program would briefly touch memory it shouldn't, leaving cache traces the attacker could read.

Both attacks crossed boundaries that were supposed to be inviolable: user to kernel, guest to host, process to process. The CPU's architecture guaranteed isolation, but its microarchitecture leaked it through timing, cache state, and speculative execution.

---

## Shannon's Definition

Shannon defined information as reduction in uncertainty. A message conveys information because it tells you something you didn't know.

By this definition, *anything* that reduces uncertainty is information, whether or not it was intended to communicate.

The safe's beep narrows down which digit is correct. Computation timing reveals which code branch was taken, and a chip's power draw tells you which operations occurred. Even the radiation from a cable carries information about what flows through it.

---

## The Shape of Traffic

**Netflix and traffic analysis.** Your video stream is encrypted. An eavesdropper sees only noise. But the *pattern* of the traffic (packet sizes, timing, bitrate changes) correlates with what you're watching. Researchers have identified specific movies from encrypted Netflix streams with over 99% accuracy.

**Keystroke dynamics.** The rhythm of your typing (how long you hold each key, the gaps between keystrokes) can identify individual typists, and encrypting the keystrokes does not hide their timing.

**Website fingerprinting.** HTTPS hides which page you're viewing but not the pattern of requests: how many resources, what sizes, what timing. The pattern is enough to identify the site with high accuracy.

---

## Two Rhythms

The figure below shows inter-key intervals for two typists, each typing the phrase "open the safe" three times. The data are synthetic and only illustrative: each simulated typist has a fixed timing profile over the letter pairs, plus small random variation from one attempt to the next. The phrase is the same for both, so the content carries no information about who typed it, while the interval pattern stays similar across each typist's repetitions and differs between the two typists.

{% include figure.html src="leaky-locks-rhythm.svg" alt="Synthetic inter-key intervals in milliseconds for each consecutive key pair of the phrase open the safe, three repetitions each for typist A and typist B" %}

---

## The Arms Race

The natural response: fix the leaks. Cryptographers have tried.

**Constant-time code.** Compare all characters, even after finding a mismatch. Make every branch take the same time. Never let computation depend on secret data. This is surprisingly hard to get right; optimizing compilers can reintroduce the very branches that constant-time code tries to eliminate.

**Blinding.** Add random noise to inputs before computing. The answer is the same, but intermediate steps are randomized, masking power and timing patterns.

**Shielding.** Faraday cages block electromagnetic radiation. The NSA calls their standard TEMPEST and has classified its specifications since the 1960s.

Each fix addresses one channel. Computation requires energy, energy dissipates as heat, radiation and vibration, and any physical process leaves traces. What matters is whether an adversary can detect them. The threshold is low for an intelligence agency and high for a casual thief, and it falls as sensors improve and analysis gets cheaper.

---

## Privacy, Anonymity, AI

Every digital action has a shape: timing, size, frequency. Encryption hides content but not shape, and metadata analysis works on the shape.

Behavioral patterns compound the problem. How you type, how you move your mouse, how you browse; these persist across contexts and serve as fingerprints. Anonymity then requires hiding behavior as well as identity, and behavior is hard to fake. Machine learning makes patterns too subtle for a human analyst tractable with enough data and compute.

---

## Why Leaks Persist

The safe lock has an obvious fix: check the whole code before reacting, so that the timing no longer depends on how many digits are right. The underlying problem was that the lock processed each digit separately, and that separation was measurable.

Silence the electronics and timing still leaks. Equalize timing, and power consumption gives you away. Shield power, and electromagnetic radiation escapes.
