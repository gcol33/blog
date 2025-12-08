---
layout: post
title: "De Méré's Dice Paradox"
date: 2025-09-06
categories: probability paradox history
toc: true
---

## When $1+1$ Is Not $2$

In 1654, a French nobleman named Antoine Gombaud—better known as the Chevalier de Méré—had a problem. Two gambling wagers that seemed identical by his reasoning behaved differently at the tables. One made money over time. The other slowly drained it.

De Méré was no mathematician. But he knew someone who was. He brought the puzzle to Blaise Pascal, then thirty-one and already famous for his work on vacuum and pressure.

Pascal took the problem seriously. He wrote to Pierre de Fermat, a magistrate in Toulouse who pursued mathematics in his spare time. Over several months, the two exchanged letters dissecting de Méré's wagers.

That correspondence is now remembered as the birth of probability theory. What began as a question about dice became a new branch of mathematics.

---

## The Two Wagers

De Méré described two bets:

1. Roll a single die 4 times. Bet that at least one six appears.
2. Roll two dice 24 times. Bet that at least one double-six appears.

At first sight, they look equivalent.

A single die has probability $1/6$ of showing a six. The expected number of sixes in 4 rolls:

$$
4 \times \frac{1}{6} = \frac{2}{3}
$$

A pair of dice has probability $1/36$ of showing double-six. The expected number of double-sixes in 24 rolls:

$$
24 \times \frac{1}{36} = \frac{2}{3}
$$

Same expectation. De Méré reasoned that if the expected count of successes is the same, the probability of winning should be the same.

The gambling tables disagreed.

---

## The First Wager: One Die, Four Rolls

The probability of *no* six in a single roll is $5/6$. Four independent rolls:

$$
\left(\frac{5}{6}\right)^4 \approx 0.482
$$

So the probability of *at least one* six:

$$
1 - \left(\frac{5}{6}\right)^4 \approx 0.518
$$

Slightly favorable. Bet this long enough, and you win.

---

## The Second Wager: Two Dice, Twenty-Four Rolls

The probability of *no* double-six in a single roll is $35/36$. Twenty-four rolls:

$$
\left(\frac{35}{36}\right)^{24} \approx 0.509
$$

So the probability of *at least one* double-six:

$$
1 - \left(\frac{35}{36}\right)^{24} \approx 0.491
$$

Slightly unfavorable. Bet this long enough, and you lose.

---

## Why the Results Differ

Both wagers give the same expected number of successes: $2/3$. But the probability of winning differs. The reason: two different measures are involved.

**Expectation is linear.** If each trial has probability $p$ of success, then $n$ trials have expected successes $np$. Double the trials, double the expectation. Simple addition.

**Probability of at least one success is nonlinear.** It equals $1 - (1-p)^n$. Failures compound. When $p$ is small, $(1-p)^n$ stays close to 1 even for moderately large $n$.

In the first wager, the event is common enough (probability $1/6$) that one of four trials usually succeeds. In the second wager, the event is rare (probability $1/36$). Twenty-four trials aren't enough to overcome the compounding failures.

De Méré assumed scaling trials would compensate for scaling probabilities. It works for expectation. It fails for the probability of winning.

---

## Try It Yourself

The difference between 51.8% and 49.1% is small. Over a few games, luck dominates. But over hundreds of rounds, the edge becomes visible.

<div id="demere-sim" style="max-width: 720px; margin: 1.5em auto;">
  <div class="sim-controls" style="display: flex; gap: 1em; flex-wrap: wrap; margin-bottom: 1em;">
    <button id="run1">Run 1 round</button>
    <button id="run100">Run 100 rounds</button>
    <button id="run1000">Run 1000 rounds</button>
    <button id="reset">Reset</button>
  </div>

  <div class="sim-results" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5em;">
    <div class="wager-box" style="border: 1px solid #000; padding: 1em; background: #fafafa;">
      <strong>Wager 1: One die, 4 rolls</strong><br>
      <span class="lightText">Target: at least one 6</span>
      <div style="margin-top: 0.5em;">
        Wins: <span id="w1-wins">0</span> / <span id="w1-total">0</span><br>
        Win rate: <strong id="w1-rate">—</strong>
      </div>
      <div style="margin-top: 0.5em; font-size: 0.9em;">
        True probability: 51.77%
      </div>
    </div>
    <div class="wager-box" style="border: 1px solid #000; padding: 1em; background: #fafafa;">
      <strong>Wager 2: Two dice, 24 rolls</strong><br>
      <span class="lightText">Target: at least one double-6</span>
      <div style="margin-top: 0.5em;">
        Wins: <span id="w2-wins">0</span> / <span id="w2-total">0</span><br>
        Win rate: <strong id="w2-rate">—</strong>
      </div>
      <div style="margin-top: 0.5em; font-size: 0.9em;">
        True probability: 49.14%
      </div>
    </div>
  </div>

  <div style="margin-top: 1em; text-align: center;">
    <canvas id="demere-chart" style="width: 100%; height: 200px; border: 1px solid #000; background: #fff;"></canvas>
    <div class="lightText" style="margin-top: 0.5em;">Win rate over time (blue = Wager 1, red = Wager 2, dashed = true values)</div>
  </div>
</div>

{% raw %}
<script>
(function(){
  let w1 = {wins: 0, total: 0, history: []};
  let w2 = {wins: 0, total: 0, history: []};

  const canvas = document.getElementById('demere-chart');
  const ctx = canvas.getContext('2d');

  function resizeCanvas(){
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener('resize', () => { resizeCanvas(); draw(); });
  resizeCanvas();

  function rollDie(){ return Math.floor(Math.random() * 6) + 1; }

  function runWager1(){
    for(let i = 0; i < 4; i++){
      if(rollDie() === 6) return true;
    }
    return false;
  }

  function runWager2(){
    for(let i = 0; i < 24; i++){
      if(rollDie() === 6 && rollDie() === 6) return true;
    }
    return false;
  }

  function runRounds(n){
    for(let i = 0; i < n; i++){
      w1.total++;
      if(runWager1()) w1.wins++;
      w1.history.push(w1.wins / w1.total);

      w2.total++;
      if(runWager2()) w2.wins++;
      w2.history.push(w2.wins / w2.total);
    }
    updateDisplay();
    draw();
  }

  function updateDisplay(){
    document.getElementById('w1-wins').textContent = w1.wins;
    document.getElementById('w1-total').textContent = w1.total;
    document.getElementById('w1-rate').textContent = w1.total ? (100 * w1.wins / w1.total).toFixed(2) + '%' : '—';

    document.getElementById('w2-wins').textContent = w2.wins;
    document.getElementById('w2-total').textContent = w2.total;
    document.getElementById('w2-rate').textContent = w2.total ? (100 * w2.wins / w2.total).toFixed(2) + '%' : '—';
  }

  function draw(){
    const W = canvas.clientWidth, H = canvas.clientHeight;
    const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const pad = 1.875 * rem, innerW = W - pad * 2, innerH = H - pad * 2;

    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 1;

    // Axes
    ctx.beginPath();
    ctx.moveTo(pad, pad);
    ctx.lineTo(pad, pad + innerH);
    ctx.lineTo(pad + innerW, pad + innerH);
    ctx.stroke();

    // Y-axis labels
    ctx.fillStyle = '#000';
    ctx.font = '11px system-ui, sans-serif';
    ctx.textAlign = 'right';
    ctx.fillText('100%', pad - 5, pad + 4);
    ctx.fillText('50%', pad - 5, pad + innerH/2 + 4);
    ctx.fillText('0%', pad - 5, pad + innerH + 4);

    if(w1.history.length === 0) return;

    const n = w1.history.length;
    const xScale = innerW / Math.max(n - 1, 1);

    function drawLine(history, color){
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for(let i = 0; i < history.length; i++){
        const x = pad + i * xScale;
        const y = pad + innerH * (1 - history[i]);
        if(i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
    }

    // True probability lines (dashed)
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = '#66a';
    ctx.beginPath();
    const y1 = pad + innerH * (1 - 0.5177);
    ctx.moveTo(pad, y1); ctx.lineTo(pad + innerW, y1);
    ctx.stroke();

    ctx.strokeStyle = '#a66';
    ctx.beginPath();
    const y2 = pad + innerH * (1 - 0.4914);
    ctx.moveTo(pad, y2); ctx.lineTo(pad + innerW, y2);
    ctx.stroke();
    ctx.setLineDash([]);

    // Actual lines
    drawLine(w1.history, '#2266cc');
    drawLine(w2.history, '#cc4444');
  }

  function reset(){
    w1 = {wins: 0, total: 0, history: []};
    w2 = {wins: 0, total: 0, history: []};
    updateDisplay();
    draw();
  }

  document.getElementById('run1').addEventListener('click', () => runRounds(1));
  document.getElementById('run100').addEventListener('click', () => runRounds(100));
  document.getElementById('run1000').addEventListener('click', () => runRounds(1000));
  document.getElementById('reset').addEventListener('click', reset);

  draw();
})();
</script>

<style>
#demere-sim button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#demere-sim button:hover {
  background: #eee;
}
</style>
{% endraw %}

---

## The Same Trap Today

The confusion between expectation and probability appears far beyond dice.

**Lotteries.** A ticket costing \$2 with a 1-in-10-million chance at \$10 million has expected value near \$1. Buy a million tickets and your expected return is about \$1 million. But your probability of winning even once is still only about 10%. Expectation scales; probability does not.

**Medical screening.** A test with 99% sensitivity and 1% false positive rate sounds reliable. If the disease prevalence is 0.1%, most positive results are false positives. The expected number of true positives per thousand tests is about 1. The probability that *your* positive result is correct is only about 9%. Doctors routinely confuse these.

**Rare risks.** The expected number of fatal accidents on a commute might be 0.0001 per trip. Over 10,000 trips, the expectation is 1. But the probability of at least one fatal accident is about 63% (by $1 - e^{-1}$), not 100%. Expectation and probability diverge most sharply for rare events repeated many times.

The linear intuition that works for averages misleads when applied to probabilities. De Méré stumbled on this in 1654. We still stumble on it today.

---

## The Letters That Changed Mathematics

Pascal's correspondence with Fermat did more than resolve a gambling puzzle. The letters introduced the idea that uncertainty itself could be quantified and computed. They developed methods for counting arrangements, dividing stakes fairly, and reasoning about future outcomes.

Within a generation, Christiaan Huygens published the first textbook on probability. Jacob Bernoulli proved the law of large numbers. By the eighteenth century, Laplace had extended these ideas to astronomy, insurance, and the theory of errors.

All of it traces back to a gambler who noticed two wagers that should have been the same but weren't.

De Méré never understood the mathematics. But his confusion launched a field.
