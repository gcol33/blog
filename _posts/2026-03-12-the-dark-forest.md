---
layout: post
title: "The Dark Forest"
date: 2026-03-12
categories: probability paradox
toc: true
excerpt: "In 1950, a physicist asked why the galaxy is silent. The answer may be game theory: when the cost of contact is extinction and every encounter is one-shot, silence is the only rational strategy."
---

## Where Is Everybody?

In the summer of 1950, four physicists at Los Alamos walked to lunch. The conversation drifted to a recent New Yorker cartoon about flying saucers, and someone joked about aliens stealing trash cans. Mid-meal, one of them turned serious: "Where is everybody?"

It was a simple calculation. The Milky Way contains roughly $10^{11}$ stars. A conservative fraction have planets. Life has had billions of years to arise and spread. Even if interstellar travel is slow, a single civilization expanding at a fraction of the speed of light would colonize the entire galaxy in a few million years, a blink on cosmic timescales.

The galaxy should be teeming. But no signal, no probe, no artifact, nothing. The physicist who asked was Enrico Fermi, and the question outlived the lunch by decades, because every proposed answer forces you to state what you believe about the nature of life and what happens to civilizations that survive long enough to be visible.

---

## The Arithmetic of Contact

Fermi's question stayed in the air. Over the next decade, radio astronomy matured, and the search for extraterrestrial intelligence became something that could be funded rather than joked about. By 1961, enough serious people cared that the National Academy of Sciences sponsored a small meeting at Green Bank, West Virginia, to discuss how one might detect alien civilizations. An astronomer at the meeting tried to organize the guesswork by breaking the question into a chain of factors: how many stars form per year, what fraction have planets, how often life arises, how often it becomes intelligent, how often it builds radios, and how long such civilizations last. He wrote the product on a blackboard.

$$
N = R_* \cdot f_p \cdot n_e \cdot f_l \cdot f_i \cdot f_c \cdot L
$$

His name was Frank Drake, and the equation bears his name, though he would be the first to say that none of the values on the right side are known. Plug in pessimistic estimates ($R_* = 1$, $f_p = 0.2$, $n_e = 1$, $f_l = 0.1$, $f_i = 0.1$, $f_c = 0.1$, $L = 10{,}000$ years) and you get $N = 2$. We are one. There should be at least one other.

With optimistic estimates ($f_l = 0.5$, $f_i = 0.5$, $L = 10^6$), $N$ reaches into the tens of thousands, and yet every radio telescope ever built has recorded nothing but static, which brings us back to the question Fermi asked at lunch.

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

And you have no data. You have never met an alien civilization. Your prior on $p$ comes from nothing but your own speculation.

---

## Play the Game

<div id="contact-sim" style="max-width: 720px; margin: 0 auto;">
  <canvas id="contact-canvas" style="width: 100%; height: 260px; background: #fff; border: 1px solid #000;"></canvas>

  <div class="contact-controls">
    <label>Hostility probability p = <strong id="p-display">5%</strong>
      <input type="range" id="p-slider" min="1" max="50" value="5" />
    </label>
    <label>Extinction cost C = <strong id="c-display">100</strong>
      <input type="range" id="c-slider" min="2" max="500" value="100" />
    </label>
  </div>

  <div class="contact-mode">
    <label><input type="radio" name="contact-mode" value="repeated" checked /> Same civilization (repeated)</label>
    <label><input type="radio" name="contact-mode" value="oneshot" /> New civilization each round (one-shot)</label>
  </div>

  <div class="contact-actions">
    <button id="btn-signal">Signal</button>
    <button id="btn-hide">Stay Silent</button>
    <button id="btn-auto">Auto-run 100 rounds</button>
    <button id="btn-reset">Reset</button>
  </div>

  <div class="contact-stats">
    <div class="contact-stat-row"><span>Round:</span><strong id="ct-round">0</strong></div>
    <div class="contact-stat-row"><span>Your score:</span><strong id="ct-score">0</strong></div>
    <div class="contact-stat-row"><span>Contacts made:</span><strong id="ct-contacts">0</strong></div>
    <div class="contact-stat-row"><span>Extinctions:</span><strong id="ct-extinct">0</strong></div>
    <div class="contact-stat-row"><span>Signal threshold:</span><strong id="ct-threshold">p &lt; 0.99%</strong></div>
  </div>

  <div id="contact-narrative" class="contact-narrative">
    You have detected a signal from another star system. Do you respond?
  </div>
</div>

{% raw %}
<style>
#contact-sim { font-variant-numeric: tabular-nums; }
#contact-sim * { box-sizing: border-box; }

#contact-sim .contact-controls {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 10px;
}
@media (max-width: 560px) {
  #contact-sim .contact-controls { grid-template-columns: 1fr; }
}

#contact-sim label {
  font-size: 0.95em;
}

#contact-sim input[type="range"] {
  width: 100%;
  appearance: none;
  height: 6px;
  background: #eee;
  outline: none;
}
#contact-sim input[type="range"]::-webkit-slider-thumb {
  appearance: none; width: 14px; height: 14px;
  border-radius: 50%; background: #000; cursor: pointer;
}
#contact-sim input[type="range"]::-moz-range-thumb {
  width: 14px; height: 14px; border: none;
  border-radius: 50%; background: #000; cursor: pointer;
}

#contact-sim .contact-mode {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 10px;
  font-size: 0.95em;
}

#contact-sim .contact-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 10px;
}

#contact-sim button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#contact-sim button:hover {
  background: #eee;
}

#contact-sim .contact-stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 10px;
}
#contact-sim .contact-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}

#contact-sim .contact-narrative {
  border-top: 1px solid #000;
  padding: 10px 0;
  font-size: 0.95em;
}
</style>

<script>
(function(){
  var pPct = 5, C = 100, V = 1;
  var round = 0, score = 0, contacts = 0, extinctions = 0;
  var hist = [0];
  var mode = 'repeated';
  var partnerHostile = null;

  var canvas = document.getElementById('contact-canvas');
  var ctx = canvas.getContext('2d');

  function resizeCanvas() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var rect = canvas.getBoundingClientRect();
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }
  window.addEventListener('resize', resizeCanvas);

  function p() { return pPct / 100; }

  function newPartner() {
    partnerHostile = Math.random() < p();
  }

  function playRound(move) {
    if (mode === 'oneshot' || partnerHostile === null) newPartner();
    round++;
    var delta = 0, msg = '';
    if (move === 'hide') {
      msg = 'You stayed silent. Nothing happens.';
    } else {
      if (partnerHostile) {
        delta = -C;
        extinctions++;
        msg = 'You signaled. They were hostile. Extinction. (' + delta + ')';
        if (mode === 'repeated') newPartner();
      } else {
        delta = V;
        contacts++;
        msg = 'You signaled. They were peaceful. Contact established. (+' + V + ')';
      }
    }
    score += delta;
    hist.push(score);
    if (mode === 'repeated' && move === 'signal' && !partnerHostile) {
      msg += ' (Same partner next round)';
    }
    if (mode === 'oneshot') {
      msg += ' (New civilization next round)';
    }
    document.getElementById('ct-round').textContent = round;
    document.getElementById('ct-score').textContent = score;
    document.getElementById('ct-contacts').textContent = contacts;
    document.getElementById('ct-extinct').textContent = extinctions;
    document.getElementById('contact-narrative').textContent = msg;
    draw();
  }

  function autoRun(n) {
    var thresh = V / (V + C);
    for (var i = 0; i < n; i++) {
      if (mode === 'repeated' && partnerHostile === false) {
        playRound('signal');
      } else if (p() < thresh) {
        playRound('signal');
      } else {
        playRound('hide');
      }
    }
  }

  function resetGame() {
    round = 0; score = 0; contacts = 0; extinctions = 0;
    hist = [0]; partnerHostile = null;
    document.getElementById('ct-round').textContent = '0';
    document.getElementById('ct-score').textContent = '0';
    document.getElementById('ct-contacts').textContent = '0';
    document.getElementById('ct-extinct').textContent = '0';
    document.getElementById('contact-narrative').textContent =
      'You have detected a signal from another star system. Do you respond?';
    draw();
  }

  function updateThreshold() {
    var thresh = (V / (V + C) * 100).toFixed(2);
    document.getElementById('ct-threshold').textContent = 'p < ' + thresh + '%';
  }

  function draw() {
    var W = canvas.clientWidth, H = canvas.clientHeight;
    var rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    var pad = 0.875 * rem;
    var innerW = W - pad * 2, innerH = H - pad * 2;
    var fontSize = Math.max(13, Math.round(rem * 0.85));
    var leftMargin = 3.5 * rem, bottomMargin = 1.25 * rem;

    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = '#000'; ctx.lineWidth = 1;
    ctx.strokeRect(pad, pad, innerW, innerH);

    if (hist.length < 2) return;

    var chartLeft = pad + leftMargin;
    var chartRight = pad + innerW - pad;
    var chartTop = pad + pad;
    var chartBottom = pad + innerH - bottomMargin;
    var chartW = chartRight - chartLeft;
    var chartH = chartBottom - chartTop;

    var minV = Math.min.apply(null, hist);
    var maxV = Math.max.apply(null, hist);
    if (minV === maxV) { minV -= 1; maxV += 1; }
    var range = maxV - minV;
    var xScale = chartW / Math.max(hist.length - 1, 1);

    function yPos(v) { return chartBottom - ((v - minV) / range) * chartH; }

    if (minV < 0 && maxV > 0) {
      ctx.strokeStyle = '#ccc'; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(chartLeft, yPos(0));
      ctx.lineTo(chartRight, yPos(0));
      ctx.stroke();
    }

    var font = fontSize + 'px system-ui, sans-serif';
    ctx.fillStyle = '#000'; ctx.font = font; ctx.textAlign = 'right';
    ctx.fillText(maxV.toString(), chartLeft - 6, chartTop + fontSize * 0.4);
    ctx.fillText(minV.toString(), chartLeft - 6, chartBottom + fontSize * 0.4);
    if (minV < 0 && maxV > 0) {
      ctx.fillText('0', chartLeft - 6, yPos(0) + fontSize * 0.4);
    }

    ctx.strokeStyle = '#000'; ctx.lineWidth = 2;
    ctx.beginPath();
    for (var i = 0; i < hist.length; i++) {
      var x = chartLeft + i * xScale, y = yPos(hist[i]);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Label
    ctx.textAlign = 'left'; ctx.font = font;
    ctx.fillText('Score', chartLeft + 4, chartTop + fontSize);
  }

  document.getElementById('p-slider').addEventListener('input', function() {
    pPct = parseInt(this.value);
    document.getElementById('p-display').textContent = pPct + '%';
    updateThreshold();
  });
  document.getElementById('c-slider').addEventListener('input', function() {
    C = parseInt(this.value);
    document.getElementById('c-display').textContent = C;
    updateThreshold();
  });
  document.querySelectorAll('input[name="contact-mode"]').forEach(function(el) {
    el.addEventListener('change', function() {
      mode = this.value;
      resetGame();
    });
  });
  document.getElementById('btn-signal').addEventListener('click', function() { playRound('signal'); });
  document.getElementById('btn-hide').addEventListener('click', function() { playRound('hide'); });
  document.getElementById('btn-auto').addEventListener('click', function() { autoRun(100); });
  document.getElementById('btn-reset').addEventListener('click', resetGame);

  updateThreshold();
  resizeCanvas();
})();
</script>
{% endraw %}

Set the hostility probability to 5% and the extinction cost to 100. The signal threshold reads $p < 0.99\%$: signaling is irrational because 5% far exceeds 0.99%. Click "Auto-run 100 rounds" and watch the score sit flat at zero. Nothing happens. Silence is the equilibrium.

Now lower $C$ to 2 (contact is risky but not existential). The threshold jumps to $p < 33\%$. Run another 100 rounds. The score climbs; contact pays off. The difference between a quiet universe and a noisy one is the ratio of what you stand to lose versus what you stand to gain.

Switch to "Same civilization (repeated)" mode and run 100 rounds with moderate settings. Once you survive the first signal with a peaceful partner, every subsequent round is safe; repetition allows trust to form. Switch back to "New civilization each round" and the extinctions return. The simulation assumes you know $p$, but a real civilization facing a real signal has no way to look up the hostility rate.

---

## The Chain of Suspicion

The calculation above assumes you know $p$. In practice, you know nothing.

Even a civilization that is peaceful today might not be peaceful tomorrow. Technology grows exponentially. A species that poses no threat at your current level of development might surpass you in a thousand years, and a thousand years is nothing on galactic timescales. You cannot verify intentions across interstellar distances, and you cannot monitor compliance with any agreement.

This creates what game theorists call a chain of suspicion. Even if you are peaceful and they are peaceful, you cannot be sure they know you are peaceful. And even if they know, you cannot be sure they know that you know. The uncertainty propagates: each level of "I think they think I think..." adds doubt, and the doubt compounds.

In a one-shot game with no communication channel and existential stakes, the chain of suspicion drives $p$ upward regardless of anyone's actual intentions. A civilization that would cooperate if it could verify the other's nature stays silent because verification is impossible.

---

## Once Versus a Thousand Times

The distinction between one-shot and repeated games changes everything.

In the Cold War, the United States and Soviet Union played a deterrence game repeatedly over four decades. They built channels: the hotline between Washington and Moscow, arms control treaties, summit meetings, the informal rules of engagement that developed after each crisis. Each peaceful resolution added evidence that the other side preferred survival over victory. Reputation accumulated. Trust, or at least predictability, emerged.

The folk theorem of repeated games formalizes this. When two players expect to interact indefinitely and value future payoffs enough, cooperation can be sustained as an equilibrium. Strategies like tit-for-tat (cooperate until the other defects, then punish, then forgive) stabilize cooperation because the future cost of losing a cooperative partner exceeds the one-time gain from defection.

Cosmic contact has none of these features. The distances are measured in light-years, a signal takes decades or centuries to cross the gap, and the civilizations on either end may not even exist in the same millennium. Iteration requires proximity, and proximity is exactly what interstellar space denies. Each contact event is, for practical purposes, a one-shot game with a stranger.

In a one-shot Prisoner's Dilemma, the dominant strategy is to defect. In the contact game, where the cost of being wrong is extinction and the benefit of being right is modest, the one-shot version collapses to silence for any civilization that has done the arithmetic. The Fermi Paradox may be what a universe of such civilizations looks like from the outside.

---

## The Dark Forest

The game-theoretic reasoning above was not new when a Chinese science fiction writer gave it its most vivid image in 2008. But nobody had dramatized it at planetary scale before. The universe, in his telling, is a dark forest. Every civilization is a hunter moving through the trees, unable to know whether the shadow ahead is a deer or another hunter with a rifle. Revealing your position, by signaling, by broadcasting, by doing anything that makes you visible, invites destruction from anyone who has done the expected-value calculation and drawn the rational conclusion.

The writer was Liu Cixin, and his novel *The Dark Forest* gave the idea its name.

Liu grounded the metaphor in two axioms: survival is the primary need of every civilization, and civilizations grow continuously while the total matter in the universe does not. Under these conditions, any other civilization is a potential competitor for finite resources, and the safest response to detection is a preemptive strike.

The civilizations that broadcast were eliminated by natural selection operating at a cosmic scale. The ones that survived learned to hide. What we observe as silence is the equilibrium state of this process, and it raises an immediate question about what humans have already done.

---

## What METI Risks

When the Arecibo radio telescope in Puerto Rico was upgraded in 1974, a group of astronomers celebrated by aiming it at the globular cluster M13 and transmitting a three-minute encoded message. It was a symbolic gesture; M13 is 25,000 light-years away. But the precedent was set: humans had deliberately announced their presence.

More recently, a project called METI (Messaging Extraterrestrial Intelligence) has advocated sending targeted signals to nearby star systems, which are close enough that a reply could arrive within a human lifetime. If the contact game is a reasonable model, this is a decision with asymmetric consequences. The benefit of a response is scientific knowledge. The cost of attracting the wrong attention is unbounded. And the decision is being made by a handful of people on behalf of every human who has ever lived or ever will.

One of the most vocal advocates for transmission, a Russian physicist named Alexander Zaitsev who spent decades operating the Evpatoria planetary radar, has argued that a civilization advanced enough to threaten us would already know we are here from our television signals, our radar emissions, the atmospheric composition of our planet. Deliberate transmission adds little to what we already leak. The counter-argument: leaked signals are faint and transient, while a targeted transmission at high power toward a specific star is a qualitatively different act, one that says "we are here and we want to be found."

No treaty governs interstellar transmission. Any individual with access to a sufficiently powerful transmitter can make the bet on behalf of eight billion people who were never consulted.

---

## The Uncomfortable Ratio

Return to the threshold:

$$
p < \frac{V}{V + C}
$$

For signaling to be rational, the probability of hostility must be less than $V/(V+C)$. When $C$ is large relative to $V$, this threshold is tiny.

The formula encodes a deep asymmetry. Contact with a peaceful civilization yields knowledge, trade, cultural exchange, all finite goods. Getting it wrong yields extinction, which is permanent and total. When one side of a bet is finite and the other is unbounded, the expected-value calculation is dominated by the unbounded side regardless of how small its probability.

This is the same structure that makes Pascal's Wager compelling and simultaneously suspicious. The argument works whenever $C$ can be made arbitrarily large. And in the contact game, $C$ is not a rhetorical device; it is a physical fact. Civilizations that bet wrong on contact do not get a second chance.

Every proposed resolution to the Fermi Paradox encodes an assumption about what civilizations value and what they fear. The contact game encodes one specific assumption: that extinction is permanent and cooperation with strangers is unverifiable. Under those conditions, the expected-value calculation points toward silence for any $C$ large enough relative to $V$, and the threshold is low enough that most reasonable priors on hostility exceed it. Whether the universe actually works this way depends on quantities we cannot measure from a single data point, which is all we have.
