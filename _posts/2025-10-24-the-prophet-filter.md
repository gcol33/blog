---
layout: post
title: "The Prophet Filter"
date: 2025-10-24
categories: probability perception history
toc: true
---

## Ten Correct Predictions

You receive an email from someone you've never heard of. The subject line: "The market will close up tomorrow."

You ignore it. But the next day, you check, and it did close up.

A week later, another email: "Tech stocks will drop on Friday." You're skeptical. Friday comes. Tech stocks drop.

This keeps happening. Five predictions. Six. Seven. All correct. By the eighth email, you're paying attention. The sender offers access to a "premium service" for $500. After all, this person has never been wrong.

Would you pay?

Before you answer, look at the same emails from the sender's side. You are one of a million people receiving them.

---

## See It Happen

Each round, the sender splits the remaining list in half. One half is told the market will rise, the other half that it will fall. Whatever happens, one half has just seen a correct prediction. The other half is never contacted again.

{% include figure.html src="the-prophet-filter-split.svg" alt="Tree of the first three rounds: one million recipients split into halves told up and told down; the half told the correct outcome continues with 500,000, 250,000 and 125,000 people, the half told the wrong outcome stops." %}

Repeating the split for ten rounds halves the list ten times. The number of people who have seen only correct predictions falls from 1,000,000 to 31,250 after five rounds and to 976 after ten.

{% include figure.html src="the-prophet-filter-survivors.svg" alt="Recipients remaining on a logarithmic axis against the number of correct predictions seen, from 0 to 10, falling in a straight line from 1,000,000 to 976." %}

To those 976 people, the prophet seems infallible. To everyone else, the prophet doesn't exist.

---

## The Arithmetic of Prophecy

The trick requires nothing but scale and selection.

Start with $M$ recipients. Send half a prediction that the market will rise, half that it will fall. Whatever happens, half are correct. Discard the rest.

After $N$ rounds, the expected number of survivors:

$$
M \times \left(\frac{1}{2}\right)^N
$$

With one million initial targets and ten rounds:

$$
10^6 \times \left(\frac{1}{2}\right)^{10} = 976
$$

Nearly a thousand people witness a perfect streak. Not because the prophet knows anything, but because selection guarantees survivors.

---

## The Scam in the Wild

In the 1990s and 2000s, "stock-picking" newsletters ran exactly this scheme. Some were prosecuted; many were not. The scheme works because victims never see the full picture. They see only their own experience of ten correct predictions.

Variations appear everywhere:

**Psychics and mediums.** A cold reader throws out dozens of guesses. Hits are remembered; misses rationalized or forgotten. After an hour, the client recalls only the "impossible" accuracies.

**Sports tipsters.** Betting services send different picks to different subscribers. After a few weeks, a subset has received only winners. Those are the ones who pay for the premium tier.

**Hedge fund incubation.** A firm launches twenty funds with different strategies. After five years, most have failed. The survivors are marketed based on their "track record," even though selection, not skill, explains the performance.

The mechanism is survivorship bias, applied deliberately.

---

## Aristotle Saw It First

In *On Divination in Sleep*, Aristotle observed that people who dream of disasters and later learn of matching events believe they foresaw them. They forget the thousands of dreams that matched nothing.

> "The principle is the same as in the case of mentioning a particular person, and then that person appearing. For there is nothing strange in this: the cause is that one has had a thousand dreams, and something happens that corresponds to one of them."

If the probability of a dream matching reality is $p$, and you have $N$ dreams over a lifetime, the chance of at least one match:

$$
P(\text{at least one match}) = 1 - (1-p)^N
$$

For small $p$, this approximates $Np$. Dream thousands of dreams, and coincidences become inevitable.

---

## The Poisson Limit

When events are rare but trials are many, the binomial approaches a Poisson distribution with rate $\lambda = Np$:

$$
P(X = 0) = e^{-\lambda}, \qquad P(X \ge 1) = 1 - e^{-\lambda}
$$

Once $\lambda > 1$, at least one occurrence is more likely than none.

Consider a one-in-a-million event. Across eight billion people:

$$
\lambda = 8 \times 10^9 \times 10^{-6} = 8000
$$

The probability of at least one occurrence:

$$
1 - e^{-8000} \approx 1
$$

Every day, things happen to people that had a one-in-a-million chance of happening to them. Given the scale, such occurrences are inevitable.

---

## Why We Fall For It

The prophet filter exploits three cognitive biases at once.

**Survivorship bias.** We see the winners, not the losers. The 976 believers are vocal; the 999,024 who saw failures have no story to tell.

**Confirmation bias.** Once we suspect someone has a gift, we weight hits more heavily than misses. Each correct prediction strengthens belief; each miss is explained away.

**Base rate neglect.** We ask "What are the odds this person got ten predictions right?" instead of "What are the odds *someone* got ten predictions right, given a million attempts?"

The second question has an easy answer: near certainty.

---

## The Meaning of Evidence

A track record of ten correct predictions is genuinely impressive if you know you were the only recipient. But if a million people received the first email, your experience proves nothing.

The evidence that would update your beliefs is not "I saw ten correct predictions" but "Ten correct predictions, and I know no one else was receiving different predictions."

The scam works because you cannot see the counterfactual. The failed recipients don't complain; they simply stopped receiving emails. From your vantage point, the prophet has always been right, and that is exactly the problem with evaluating evidence when you don't know the selection process that produced it.
