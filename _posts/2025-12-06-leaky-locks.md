---
layout: post
title: "Leaky Locks"
date: 2025-12-06
categories: security information-theory history
toc: true
---

## What Counts as Information?

In 1943, the telephone in Winston Churchill's war room was a problem.

Transatlantic calls to Roosevelt were encrypted by SIGSALY, fifty tons of equipment that digitized speech, scrambled it with one-time pads, and reassembled it on the other end. The voice channel was mathematically unbreakable. The Germans couldn't decode a single word.

But Bell Labs engineer A.B. Clark noticed something troubling. The encryption scrambled the *content* of Churchill's speech. It didn't scramble the *rhythm*. The timing of syllables, the cadence of sentences, the patterns of pauses—all passed through intact.

Clark realized that rhythm alone might be enough to reconstruct words. He was right. The phenomenon would later be called "residual intelligibility."

SIGSALY was redesigned to mask timing patterns. The fix added more equipment. More weight. More complexity. All to hide the rhythm of Churchill's speech.

---

## The Beeping Safe

In the 1980s, hotel room safes used a simple four-digit code. Guests would set their own combination. The safe beeped once for each correct digit as you entered it.

Thieves figured it out immediately.

Start with 0000. If the safe beeps once, the first digit is 0. If not, try 1000. Work through 0-9 until you hear a beep. Then move to the second digit.

A four-digit safe has 10,000 combinations. These safes fell in 40 tries.

The safe protected the code. It didn't protect *information about* the code.

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

The longer the secret, the more catastrophic the leak.

---

## The Collapse, Visualized

{% include figure.html src="leaky-locks-collapse.svg" alt="Attempts needed against secret length n on a log scale, k to the n without leak and k times n with leak, for alphabet sizes k = 10, 26 and 62" %}

---

## Paul Kocher's Discovery

For decades, cryptographers believed they had learned the lesson. Don't leak partial information. Make verification all-or-nothing.

For decades, cryptographers assumed side channels meant things like beeps and blinking lights. Then Paul Kocher, twenty-three years old and fresh from his Stanford thesis, published a 1996 paper showing that even when software reveals nothing explicitly, the *time it takes to compute* is itself a channel.

Consider password verification:

```
def check(input, stored):
    for i in range(len(stored)):
        if input[i] != stored[i]:
            return False
    return True
```

This code returns as soon as it finds a mismatch. A wrong first character fails in one microsecond. A wrong last character takes eight microseconds, and that timing difference plays the same role as the beeping safe.

Kocher demonstrated the attack against RSA implementations. By measuring how long decryption took for different inputs, he could extract private keys bit by bit. The attack worked remotely. It worked through noise. It worked against code that had been audited for security and revealed nothing through any official channel.

The cryptographic community was stunned. They had protected the message. They hadn't thought to protect the *duration* of the computation.

---

## The Expanding Boundary

If timing is information, what else might be?

**1998: Power analysis.** Kocher again. The power consumed by a chip varies with the operations it performs. Different instructions draw different current. By measuring power consumption during cryptographic operations, attackers could extract keys from smart cards.

**1985 (published much later): Van Eck radiation.** Every wire is an antenna. CRT monitors emit electromagnetic radiation proportional to what they display. Wim van Eck showed you could reconstruct screen contents from across the street. Later researchers demonstrated the same for LCD screens, keyboards, and network cables.

**2003: Cache timing.** Modern CPUs have memory caches. Accessing cached data is fast; uncached data is slow. An attacker who shares your CPU can deduce what memory addresses you're touching, including cryptographic key material.

**2018: Spectre and Meltdown.** Modern CPUs speculate. When they hit a conditional branch, they guess which way it will go and start executing down that path. If the guess is wrong, they roll back. This is speculative execution, and it makes processors fast.

Meltdown exploited the fact that Intel chips performed speculative memory accesses before checking permissions. A user program could speculatively read kernel memory. The CPU would eventually realize the access was forbidden and discard the result—but not before the data had touched the cache. By measuring which cache lines were now fast to access, attackers could reconstruct the forbidden bytes.

Spectre was subtler. It trained the branch predictor to mispredict, then used that misprediction to speculatively access memory through the victim's own code. The victim's program would briefly touch memory it shouldn't, leaving cache traces the attacker could read.

Both attacks crossed boundaries that were supposed to be inviolable: user to kernel, guest to host, process to process. The CPU's architecture guaranteed isolation, but its microarchitecture leaked it through timing, cache state, and speculative execution.

---

## Shannon's Definition

Shannon defined information as reduction in uncertainty. A message conveys information because it tells you something you didn't know.

By this definition, *anything* that reduces uncertainty is information, whether or not it was intended to communicate.

The safe's beep narrows down which digit is correct. Computation timing reveals which code branch was taken, and a chip's power draw tells you which operations occurred. Even the radiation from a cable carries information about what flows through it.

---

## The Shape of Everything

**Netflix and traffic analysis.** Your video stream is encrypted. An eavesdropper sees only noise. But the *pattern* of the traffic (packet sizes, timing, bitrate changes) correlates with what you're watching. Researchers have identified specific movies from encrypted Netflix streams with over 99% accuracy.

**Keystroke dynamics.** The rhythm of your typing (how long you hold each key, the gaps between keystrokes) identifies you as reliably as a fingerprint. This works through encryption, through Tor, through any anonymizing layer.

**Website fingerprinting.** HTTPS hides which page you're viewing but not the pattern of requests: how many resources, what sizes, what timing. The pattern is enough to identify the site with high accuracy.

---

## Two Rhythms

The figure below shows inter-key intervals for two typists, each typing the phrase "open the safe" three times. The data are synthetic and only illustrative: each simulated typist has a fixed timing profile over the letter pairs, plus small random variation from one attempt to the next. The phrase is the same for both, so the content carries no information about who typed it, while the interval pattern stays similar across each typist's repetitions and differs between the two typists.

{% include figure.html src="leaky-locks-rhythm.svg" alt="Synthetic inter-key intervals in milliseconds for each consecutive key pair of the phrase open the safe, three repetitions each for typist A and typist B" %}

Different people produce different patterns. The text vanishes into encryption. The signature persists.

---

## The Arms Race

The natural response: fix the leaks. Cryptographers have tried.

**Constant-time code.** Compare all characters, even after finding a mismatch. Make every branch take the same time. Never let computation depend on secret data. This is surprisingly hard to get right; optimizing compilers routinely reintroduce the very branches that constant-time code tries to eliminate.

**Blinding.** Add random noise to inputs before computing. The answer is the same, but intermediate steps are randomized, masking power and timing patterns.

**Shielding.** Faraday cages block electromagnetic radiation. The NSA calls their standard TEMPEST and has classified its specifications since the 1960s. Even with shielding, a well-funded adversary can still get through.

Each fix addresses one channel. Physics guarantees there are always more.

Computation requires energy. Energy dissipates as heat, radiation, vibration. Any physical process leaves traces. The question is not whether information leaks, but whether an adversary can detect it.

For the NSA, the threshold is low. For a random thief, high. But the threshold keeps falling as sensors improve and analysis gets cheaper.

---

## The Lesson

The twentieth century forced a definition: **information is whatever can be inferred from what you do, regardless of what you intended to reveal.**

The boundary between "the secret" and "information about the secret" is not fixed. It moves as our ability to measure improves. What leaked undetectably in 1980 leaks detectably in 2000. What seems safe today will leak tomorrow.

Churchill's engineers thought they were protecting speech. They were forced to protect rhythm. Cryptographers thought they were protecting keys. They were forced to protect timing, power, radiation, cache access, and speculative execution.

What counts as "information about the secret" keeps expanding as measurement tools improve.

---

## Privacy, Anonymity, AI

Every digital action has a shape: timing, size, frequency. Encryption hides content but not shape, which is why metadata analysis has become as valuable to intelligence agencies as content interception.

Behavioral patterns compound the problem. How you type, how you move your mouse, how you browse; these persist across contexts and serve as fingerprints. True anonymity requires suppressing not just identity but behavior, and behavior is hard to fake. Machine learning has made this worse: patterns too subtle for a human analyst to spot become tractable with enough data and compute. The attacker's threshold keeps dropping.

---

## Why Leaks Persist

The beeping safe from the 1980s had an obvious fix: remove the beep. But the beep was not the problem. The problem was that the mechanism processed each digit separately, and that separation was detectable.

Silence the electronics and timing still leaks. Equalize timing, and power consumption gives you away. Shield power, and electromagnetic radiation escapes. Even fully shielded, the fact that you're standing in front of the safe reveals something.

Every physical process is a broadcast, and security requires ensuring that the broadcast conveys nothing useful. You cannot stop the broadcast; you can only try to make it uninformative, and that has turned out to be harder than any cryptographic problem.
