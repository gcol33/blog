---
layout: post
title: "The Prophet Filter"
date: 2025-10-24
categories: probability perception history
toc: true
---

## The Email That Knew Tomorrow

You receive an email from someone you've never heard of. The subject line: "The market will close up tomorrow."

You ignore it. But the next day, you check—and it did close up.

A week later, another email: "Tech stocks will drop on Friday." You're skeptical. Friday comes. Tech stocks drop.

This keeps happening. Five predictions. Six. Seven. All correct. By now you're paying attention. The eighth email offers you access to a "premium service" for just $500. After all, this person has never been wrong.

Would you pay?

Before you answer, try the simulation below. You are one of a million people receiving these emails. Watch what happens.

---

## See It Happen

<div id="prophet-sim" style="max-width: 720px; margin: 0 auto;">
  <canvas id="prophet-canvas" style="width: 100%; height: 200px; background: #fff; border: 1px solid #000;"></canvas>

  <div class="prophet-controls">
    <button id="prophet-next">Send Next Prediction</button>
    <button id="prophet-auto">Auto-run to Round 10</button>
    <button id="prophet-reset">Reset</button>
  </div>

  <div class="prophet-stats">
    <div class="prophet-stat-row"><span>Round:</span><strong id="prophet-round-num">0</strong></div>
    <div class="prophet-stat-row"><span>Recipients remaining:</span><strong id="prophet-remaining">1,000,000</strong></div>
    <div class="prophet-stat-row"><span>Correct predictions seen:</span><strong id="prophet-streak">0</strong></div>
  </div>

  <div id="prophet-narrative" class="prophet-narrative">One million people receive the first email...</div>

  <div id="prophet-reveal" class="prophet-reveal">
    <strong>The trick revealed:</strong> The "prophet" sent <em>both</em> predictions each round—"up" to half, "down" to the other half. No matter what happened, half the recipients saw a correct prediction. The wrong half was simply never contacted again.
    <div style="margin-top: 0.5em;">
      After 10 rounds, <span id="prophet-final">~976</span> people have seen 10 perfect predictions. To them, the prophet seems infallible. To everyone else, the prophet doesn't exist—they stopped receiving emails long ago.
    </div>
  </div>
</div>

{% raw %}
<script>
(function(){
  let round = 0;
  let remaining = 1000000;
  const history = [1000000];
  const startPop = 1000000;

  const canvas = document.getElementById('prophet-canvas');
  const ctx = canvas.getContext('2d');

  const narratives = [
    "One million people receive the first email...",
    "The prediction was correct! But half received the opposite prediction. They got it wrong and won't hear from the 'prophet' again.",
    "Another correct prediction for you. Another 250,000 people just saw their first miss.",
    "Three in a row. You're starting to pay attention. 125,000 others just lost faith.",
    "Four correct. This is getting hard to ignore. The prophet's track record is perfect—for you.",
    "Five. You've told a friend about this. Meanwhile, 31,000 people just learned the prophet is fallible.",
    "Six consecutive hits. You're seriously considering the premium service.",
    "Seven. The probability of this by chance is less than 1%. Or is it?",
    "Eight correct predictions. You're now in an exclusive group of about 3,900 believers.",
    "Nine. Fewer than 2,000 people remain. Each one is utterly convinced.",
    "Ten perfect predictions. You are one of ~976 people who witnessed an 'impossible' streak. The premium offer arrives tomorrow."
  ];

  function resizeCanvas(){
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener('resize', () => { resizeCanvas(); draw(); });
  resizeCanvas();

  function draw(){
    const W = canvas.clientWidth, H = canvas.clientHeight;
    const pad = 40, innerW = W - pad * 2, innerH = H - pad * 2;

    ctx.clearRect(0, 0, W, H);

    // Axes
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(pad, pad);
    ctx.lineTo(pad, pad + innerH);
    ctx.lineTo(pad + innerW, pad + innerH);
    ctx.stroke();

    // Y-axis labels (log scale)
    ctx.fillStyle = '#000';
    ctx.font = '11px system-ui, sans-serif';
    ctx.textAlign = 'right';
    const yLabels = [1000000, 100000, 10000, 1000, 100];
    yLabels.forEach(v => {
      const y = pad + innerH * (1 - (Math.log10(v) - 2) / 4);
      ctx.fillText(v.toLocaleString(), pad - 5, y + 4);
      ctx.strokeStyle = '#eee';
      ctx.beginPath();
      ctx.moveTo(pad, y);
      ctx.lineTo(pad + innerW, y);
      ctx.stroke();
    });

    // X-axis labels
    ctx.textAlign = 'center';
    ctx.strokeStyle = '#000';
    for(let i = 0; i <= 10; i++){
      const x = pad + (i / 10) * innerW;
      ctx.fillText(i.toString(), x, pad + innerH + 15);
    }

    if(history.length < 2) return;

    // Draw line
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for(let i = 0; i < history.length; i++){
      const x = pad + (i / 10) * innerW;
      const logVal = Math.log10(Math.max(history[i], 100));
      const y = pad + innerH * (1 - (logVal - 2) / 4);
      if(i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Draw points
    ctx.fillStyle = '#000';
    for(let i = 0; i < history.length; i++){
      const x = pad + (i / 10) * innerW;
      const logVal = Math.log10(Math.max(history[i], 100));
      const y = pad + innerH * (1 - (logVal - 2) / 4);
      ctx.beginPath();
      ctx.arc(x, y, 4, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function update(){
    document.getElementById('prophet-round-num').textContent = round;
    document.getElementById('prophet-narrative').textContent = narratives[Math.min(round, narratives.length - 1)];
    document.getElementById('prophet-remaining').textContent = Math.round(remaining).toLocaleString();
    document.getElementById('prophet-streak').textContent = round.toString();

    if(round >= 10){
      document.getElementById('prophet-reveal').style.display = 'block';
      document.getElementById('prophet-final').textContent = '~' + Math.round(remaining).toLocaleString();
    } else {
      document.getElementById('prophet-reveal').style.display = 'none';
    }

    draw();
  }

  function nextRound(){
    if(round >= 10) return;
    round++;
    remaining = remaining / 2;
    history.push(remaining);
    update();
  }

  function autoRun(){
    if(round >= 10) return;
    const interval = setInterval(() => {
      nextRound();
      if(round >= 10) clearInterval(interval);
    }, 400);
  }

  function reset(){
    round = 0;
    remaining = 1000000;
    history.length = 0;
    history.push(1000000);
    update();
  }

  document.getElementById('prophet-next').addEventListener('click', nextRound);
  document.getElementById('prophet-auto').addEventListener('click', autoRun);
  document.getElementById('prophet-reset').addEventListener('click', reset);

  update();
})();
</script>

<style>
#prophet-sim { font-variant-numeric: tabular-nums; }
#prophet-sim * { box-sizing: border-box; }

#prophet-sim .prophet-controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 10px;
}

#prophet-sim button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#prophet-sim button:hover {
  background: #eee;
}

#prophet-sim .prophet-stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 10px;
}
#prophet-sim .prophet-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}

#prophet-sim .prophet-narrative {
  border-top: 1px solid #000;
  padding: 10px 0;
  font-size: 0.95em;
}

#prophet-sim .prophet-reveal {
  display: none;
  border-top: 1px solid #000;
  padding: 10px 0;
  font-size: 0.95em;
}
</style>
{% endraw %}

---

## The Arithmetic of Prophecy

The trick requires nothing but scale and selection.

Start with $M$ recipients. Send half a prediction that the market will rise, half that it will fall. Whatever happens, half are correct. Discard the rest.

After $N$ rounds, the expected number of survivors is

$$
M \times \left(\frac{1}{2}\right)^N.
$$

With one million initial targets and ten rounds:

$$
10^6 \times \left(\frac{1}{2}\right)^{10} = 976.
$$

Nearly a thousand people witness a perfect streak. Not because the prophet knows anything, but because selection guarantees survivors.

---

## The Scam in the Wild

This is not hypothetical. In the 1990s and 2000s, "stock-picking" newsletters ran exactly this con. Some were prosecuted; many were not. The scheme works because the victims never see the full picture—they only see their own experience of ten correct predictions.

Variations appear everywhere:

**Psychics and mediums.** A cold reader throws out dozens of guesses. The hits are remembered; the misses are rationalized or forgotten. After an hour, the client recalls only the "impossible" accuracies.

**Sports tipsters.** Betting services send different picks to different subscribers. After a few weeks, a subset has received only winners. Those are the ones who pay for the premium tier.

**Hedge fund incubation.** A firm launches twenty funds with different strategies. After five years, most have failed. The survivors are marketed based on their "track record," even though selection, not skill, explains the performance.

The prophet filter is survivorship bias weaponized.

---

## Aristotle Saw It First

The insight is ancient. In *On Divination in Sleep*, Aristotle observed that people who dream of disasters and later learn of matching events believe they foresaw them. They forget the thousands of dreams that matched nothing.

> "The principle is the same as in the case of mentioning a particular person, and then that person appearing. For there is nothing strange in this: the cause is that one has had a thousand dreams, and something happens that corresponds to one of them."

If the probability of a dream matching reality is $p$, and you have $N$ dreams over a lifetime, the chance of at least one match is

$$
P(\text{at least one match}) = 1 - (1-p)^N.
$$

For small $p$, this approximates $Np$. Dream thousands of dreams, and coincidences become inevitable.

---

## The Poisson Limit

When events are rare but trials are many, the binomial approaches a Poisson distribution with rate $\lambda = Np$.

$$
P(X = 0) = e^{-\lambda}, \qquad P(X \ge 1) = 1 - e^{-\lambda}.
$$

Once $\lambda > 1$, at least one occurrence is more likely than none.

Consider a one-in-a-million event. Across eight billion people:

$$
\lambda = 8 \times 10^9 \times 10^{-6} = 8000.
$$

The probability of at least one occurrence is

$$
1 - e^{-8000} \approx 1.
$$

Every day, things happen to people that had a one-in-a-million chance of happening to them. That is not remarkable—it is required.

---

## Why We Fall For It

The prophet filter exploits three cognitive biases at once.

**Survivorship bias.** We see the winners, not the losers. The 976 believers are vocal; the 999,024 who saw failures have no story to tell.

**Confirmation bias.** Once we suspect someone has a gift, we weight the hits more heavily than the misses. Each correct prediction strengthens belief; each miss is explained away.

**Base rate neglect.** We ask "What are the odds this person got ten predictions right?" instead of "What are the odds *someone* got ten predictions right, given a million attempts?"

The second question has an easy answer: near certainty.

---

## The Meaning of Evidence

The prophet filter reveals something uncomfortable about evidence itself.

A track record of ten correct predictions is genuinely impressive—if you know you were the only recipient. But if a million people received the first email, your experience proves nothing. The evidence that would update your beliefs is not "I saw ten correct predictions" but "Ten correct predictions, and I know no one else was receiving different predictions."

The scam works precisely because you cannot see the counterfactual. The failed recipients don't complain—they simply stopped receiving emails. From your vantage point, the prophet has always been right.

Selection doesn't just hide failures. It makes success look like proof.
