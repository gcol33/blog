---
layout: post
title: "Removing the Steering Wheel"
date: 2026-03-12
categories: algorithms paradox
toc: true
---

## Two Cars, One Road

Two cars face each other on a narrow road. Both drivers accelerate. The first to swerve loses face; the one who holds steady wins. If neither swerves, they crash.

Game theorists call this Chicken. Each player chooses simultaneously: swerve or hold steady. The payoffs depend on what both players do.

Assign numbers. Holding steady while the other swerves pays $+1$. Swerving while the other holds steady pays $-1$. Both swerving is a draw: $0$ each. Both holding steady means a crash, costing $-C$ for some large number $C$.

$$
\begin{array}{c|cc}
 & \text{Swerve} & \text{Straight} \\
\hline
\text{Swerve} & 0,\; 0 & -1,\; +1 \\
\text{Straight} & +1,\; -1 & -C,\; -C
\end{array}
$$

Two outcomes are stable. If you know your opponent will hold steady, you should swerve (getting $-1$ beats $-C$). If you know your opponent will swerve, you should hold steady (getting $+1$ beats $0$). These are the game's two pure Nash equilibria.

The problem is symmetry. Nothing in the rules says who should swerve. Each player prefers the equilibrium where the *other* backs down, and there is no mechanism to coordinate.

---

## The Mixed Equilibrium

When neither pure equilibrium is reachable by agreement, both players randomize.

Let each player hold steady with probability $q$. For the randomization to be stable, each player must be indifferent between swerving and holding steady.

The expected payoff from swerving:

$$
0 \cdot (1-q) + (-1) \cdot q = -q
$$

The expected payoff from holding steady:

$$
1 \cdot (1-q) + (-C) \cdot q = 1 - (1+C)q
$$

Setting these equal:

$$
-q = 1 - (1+C)q \implies Cq = 1 \implies q = \frac{1}{C}
$$

Both players hold steady with probability $1/C$. At $C = 10$ each driver holds steady 10% of the time; at $C = 100$, just 1%.

The probability of a crash is $q^2 = 1/C^2$. Making the crash worse reduces the frequency of crashes, but never eliminates them. At $C = 10$, the crash probability per round is 1%. At $C = 100$, it drops to 0.01%, but it never reaches zero.

The expected payoff for each player is $-1/C$. Both expect to lose, on average. The mixed equilibrium is worse for both sides than coordinating on either pure equilibrium, but coordination requires trust, and Chicken is a game built on the absence of it.

---

## Play the Game

<div id="chicken-sim" style="max-width: 720px; margin: 0 auto;">
  <canvas id="chicken-canvas" style="width: 100%; height: 220px; background: #fff; border: 1px solid #000;"></canvas>

  <div class="chicken-controls">
    <label>Crash cost C = <strong id="c-display">10</strong>
      <input type="range" id="c-slider" min="2" max="50" value="10" />
    </label>
    <label style="display:flex; align-items:center; gap:6px;">
      <input type="checkbox" id="remove-wheel" /> Remove steering wheel
    </label>
  </div>

  <div class="chicken-actions">
    <button id="btn-swerve">Swerve</button>
    <button id="btn-straight">Straight</button>
    <button id="btn-auto">Run 100 rounds (both Nash)</button>
    <button id="btn-reset">Reset</button>
  </div>

  <div class="chicken-stats">
    <div class="chicken-stat-row"><span>Round:</span><strong id="ch-round">0</strong></div>
    <div class="chicken-stat-row"><span>Your score:</span><strong id="ch-your-score">0</strong></div>
    <div class="chicken-stat-row"><span>Opponent score:</span><strong id="ch-opp-score">0</strong></div>
    <div class="chicken-stat-row"><span>Crashes:</span><strong id="ch-crashes">0</strong></div>
    <div class="chicken-stat-row"><span>Nash P(Straight):</span><strong id="ch-nash">10.0%</strong></div>
  </div>

  <div id="chicken-narrative" class="chicken-narrative">
    Choose Swerve or Straight. Your opponent plays the Nash mixed strategy.
  </div>
</div>

{% raw %}
<style>
#chicken-sim { font-variant-numeric: tabular-nums; }
#chicken-sim * { box-sizing: border-box; }

#chicken-sim .chicken-controls {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  margin-top: 10px;
  align-items: center;
}
@media (max-width: 560px) {
  #chicken-sim .chicken-controls { grid-template-columns: 1fr; }
}

#chicken-sim label {
  font-size: 0.95em;
}

#chicken-sim input[type="range"] {
  width: 100%;
  appearance: none;
  height: 6px;
  background: #eee;
  outline: none;
}
#chicken-sim input[type="range"]::-webkit-slider-thumb {
  appearance: none; width: 14px; height: 14px;
  border-radius: 50%; background: #000; cursor: pointer;
}
#chicken-sim input[type="range"]::-moz-range-thumb {
  width: 14px; height: 14px; border: none;
  border-radius: 50%; background: #000; cursor: pointer;
}

#chicken-sim .chicken-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 10px;
}

#chicken-sim button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#chicken-sim button:hover {
  background: #eee;
}
#chicken-sim button:disabled {
  opacity: 0.3;
  cursor: default;
}
#chicken-sim button:disabled:hover {
  background: #fff;
}

#chicken-sim .chicken-stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 10px;
}
#chicken-sim .chicken-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}

#chicken-sim .chicken-narrative {
  border-top: 1px solid #000;
  padding: 10px 0;
  font-size: 0.95em;
}
</style>

<script>
(function(){
  var C = 10;
  var round = 0, yourScore = 0, oppScore = 0, crashes = 0;
  var yourHist = [0], oppHist = [0];
  var wheelRemoved = false;

  var canvas = document.getElementById('chicken-canvas');
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

  function nashProb() { return 1 / C; }

  function oppMove() {
    if (wheelRemoved) return 'swerve';
    return Math.random() < nashProb() ? 'straight' : 'swerve';
  }

  function playRound(yourMove) {
    var opp = oppMove();
    round++;
    var yP = 0, oP = 0, crashed = false;
    if (yourMove === 'swerve' && opp === 'swerve') { yP = 0; oP = 0; }
    else if (yourMove === 'swerve' && opp === 'straight') { yP = -1; oP = 1; }
    else if (yourMove === 'straight' && opp === 'swerve') { yP = 1; oP = -1; }
    else { yP = -C; oP = -C; crashes++; crashed = true; }

    yourScore += yP; oppScore += oP;
    yourHist.push(yourScore); oppHist.push(oppScore);
    updateUI(yourMove, opp, yP, oP, crashed);
    draw();
  }

  function autoRun(n) {
    for (var i = 0; i < n; i++) {
      var ym = wheelRemoved ? 'straight' : (Math.random() < nashProb() ? 'straight' : 'swerve');
      playRound(ym);
    }
  }

  function updateUI(ym, om, yp, op, crashed) {
    document.getElementById('ch-round').textContent = round;
    document.getElementById('ch-your-score').textContent = yourScore;
    document.getElementById('ch-opp-score').textContent = oppScore;
    document.getElementById('ch-crashes').textContent = crashes;
    document.getElementById('ch-nash').textContent = (100 / C).toFixed(1) + '%';

    var narr = document.getElementById('chicken-narrative');
    if (round === 0) {
      narr.textContent = 'Choose Swerve or Straight. Your opponent plays the Nash mixed strategy.';
      return;
    }
    var ymLabel = ym === 'swerve' ? 'swerved' : 'held steady';
    var omLabel = om === 'swerve' ? 'swerved' : 'held steady';
    var msg = 'You ' + ymLabel + ', opponent ' + omLabel + '. ';
    if (crashed) msg += 'Crash! (' + yp + ', ' + op + ')';
    else if (yp > 0) msg += 'You win. (+' + yp + ', ' + op + ')';
    else if (yp < 0) msg += 'You lose. (' + yp + ', +' + op + ')';
    else msg += 'Draw. (0, 0)';
    if (wheelRemoved && round > 0) msg += ' [Steering wheel removed]';
    narr.textContent = msg;
  }

  function draw() {
    var W = canvas.clientWidth, H = canvas.clientHeight;
    var rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    var pad = 0.875 * rem;
    var innerW = W - pad * 2, innerH = H - pad * 2;
    var leftMargin = 2.5 * rem, bottomMargin = 0.5 * rem;

    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = '#000'; ctx.lineWidth = 1;
    ctx.strokeRect(pad, pad, innerW, innerH);

    if (yourHist.length < 2) return;

    var chartLeft = pad + leftMargin;
    var chartRight = pad + innerW - pad;
    var chartTop = pad + pad;
    var chartBottom = pad + innerH - bottomMargin;
    var chartW = chartRight - chartLeft;
    var chartH = chartBottom - chartTop;

    var allVals = yourHist.concat(oppHist);
    var minV = Math.min.apply(null, allVals);
    var maxV = Math.max.apply(null, allVals);
    if (minV === maxV) { minV -= 1; maxV += 1; }
    var range = maxV - minV;

    var n = yourHist.length;
    var xScale = chartW / Math.max(n - 1, 1);

    function yPos(v) { return chartBottom - ((v - minV) / range) * chartH; }

    // Zero line
    if (minV < 0 && maxV > 0) {
      ctx.strokeStyle = '#ccc'; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(chartLeft, yPos(0));
      ctx.lineTo(chartRight, yPos(0));
      ctx.stroke();
    }

    // Y-axis labels
    ctx.fillStyle = '#000'; ctx.font = '11px system-ui, sans-serif'; ctx.textAlign = 'right';
    ctx.fillText(maxV.toString(), chartLeft - 4, chartTop + 4);
    ctx.fillText(minV.toString(), chartLeft - 4, chartBottom + 4);

    // Your score (solid)
    ctx.strokeStyle = '#000'; ctx.lineWidth = 2;
    ctx.beginPath();
    for (var i = 0; i < yourHist.length; i++) {
      var x = chartLeft + i * xScale, y = yPos(yourHist[i]);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    // Opponent score (dashed)
    ctx.setLineDash([6, 4]);
    ctx.beginPath();
    for (var i = 0; i < oppHist.length; i++) {
      var x = chartLeft + i * xScale, y = yPos(oppHist[i]);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.setLineDash([]);

    // Legend
    var legY = chartTop + 4;
    ctx.fillStyle = '#000'; ctx.textAlign = 'left'; ctx.font = '11px system-ui, sans-serif';
    ctx.beginPath(); ctx.moveTo(chartRight - 6 * rem, legY); ctx.lineTo(chartRight - 4.5 * rem, legY);
    ctx.strokeStyle = '#000'; ctx.lineWidth = 2; ctx.stroke();
    ctx.fillText('You', chartRight - 4.2 * rem, legY + 4);

    ctx.setLineDash([6, 4]); ctx.beginPath();
    ctx.moveTo(chartRight - 6 * rem, legY + 14); ctx.lineTo(chartRight - 4.5 * rem, legY + 14);
    ctx.stroke(); ctx.setLineDash([]);
    ctx.fillText('Opponent', chartRight - 4.2 * rem, legY + 18);
  }

  function resetGame() {
    round = 0; yourScore = 0; oppScore = 0; crashes = 0;
    yourHist = [0]; oppHist = [0];
    updateUI('', '', 0, 0, false);
    draw();
  }

  document.getElementById('c-slider').addEventListener('input', function() {
    C = parseInt(this.value);
    document.getElementById('c-display').textContent = C;
    document.getElementById('ch-nash').textContent = (100 / C).toFixed(1) + '%';
  });

  document.getElementById('remove-wheel').addEventListener('change', function() {
    wheelRemoved = this.checked;
    document.getElementById('btn-swerve').disabled = wheelRemoved;
    var narr = document.getElementById('chicken-narrative');
    if (wheelRemoved) {
      narr.textContent = 'Steering wheel removed. You always hold steady. Opponent always swerves.';
    } else {
      narr.textContent = 'Steering wheel restored. Opponent returns to Nash mixed strategy.';
    }
  });

  document.getElementById('btn-swerve').addEventListener('click', function() { playRound('swerve'); });
  document.getElementById('btn-straight').addEventListener('click', function() { playRound('straight'); });
  document.getElementById('btn-auto').addEventListener('click', function() { autoRun(100); });
  document.getElementById('btn-reset').addEventListener('click', resetGame);

  resizeCanvas();
})();
</script>
{% endraw %}

Try playing a few rounds manually, then click "Run 100 rounds" to watch the scores accumulate under the mixed equilibrium. Both lines drift downward; the expected payoff is negative for both players. Now check "Remove steering wheel" and run another 100 rounds. Your score climbs; the opponent's falls. Zero crashes.

---

## Commitment

The steering wheel trick works because it changes the game's structure, not just the strategy within it.

With the wheel intact, the game has two pure equilibria and one mixed equilibrium, all three of them accessible. Remove the wheel, and only one outcome survives: you hold steady, the opponent swerves. The opponent's rational response to your irrevocable commitment is capitulation.

By destroying your own ability to back down, your payoff jumps from $-1/C$ (the mixed equilibrium average) to $+1$ (a guaranteed win), precisely because the opponent knows you have no choice left.

The commitment must be visible and irreversible. A steering wheel hidden under the seat changes nothing; what matters is not whether you *can* swerve but whether the other driver *believes* you can. And the most convincing way to signal that you won't back down is to make backing down physically impossible.

This is the logic that a game theorist at the RAND Corporation spent the late 1950s formalizing. He was working on nuclear deterrence, and the question he kept returning to was whether the United States *would* retaliate with nuclear weapons, given that retaliation meant self-destruction. A threat to destroy the enemy is only useful if the enemy believes you'll follow through, and following through means destroying yourself in the process.

The strategist realized that governments face the same dilemma as the two drivers. The side that could most convincingly eliminate its own ability to retreat would force the other side to be the one that compromised. His name was Thomas Schelling, and his 1960 book *The Strategy of Conflict* became the intellectual foundation of Cold War deterrence theory. Its central argument was uncomfortable: the rational actor, the one who correctly calculates that retaliation is suicidal and therefore backs down, is the one who gets exploited.

---

## Once Versus a Thousand Times

A single round of Chicken is terrifying because there is no history to consult and no future to protect. Each player randomizes, and crashes happen with probability $1/C^2$ per round. Over many rounds, those small probabilities accumulate.

In $n$ rounds of the mixed equilibrium, the expected number of crashes is $n/C^2$. The probability of *at least one* crash:

$$
1 - \left(1 - \frac{1}{C^2}\right)^n
$$

At $C = 10$, a single round carries 1% crash risk. After 100 rounds, the probability of at least one crash rises to 63%. After 1000 rounds, it is 99.995%. Given enough repetitions, a crash is virtually certain.

This is the arithmetic that haunted Cold War strategists. If the United States and Soviet Union played nuclear Chicken every few years during crises (Berlin 1948, Korea 1950, Cuba 1962, the Yom Kippur War 1973), each individual crisis might carry low risk. But the cumulative probability of catastrophe grows with each confrontation, and there is no mechanism to reset the counter.

Repetition changes the strategy in a second way. In a one-shot game, reputation is irrelevant; there is no future for your reputation to influence. In a repeated game, what you did last time shapes what the opponent expects you to do next time.

A player who swerved in round one will be expected to swerve in round two. A player who held steady and survived has demonstrated a willingness to accept risk, making the opponent more likely to swerve next time. This feedback loop creates a premium on early aggression: establish a reputation for toughness in the first few rounds, and the opponent may swerve for the rest of the game.

The formal result, due to the folk theorem of repeated games, is that repetition expands the set of sustainable outcomes. Strategies like "hold steady until the opponent holds steady, then punish by holding steady for the next $k$ rounds" can sustain cooperation (mutual swerving) as an equilibrium, provided both players value future rounds enough. The discount factor $\delta$ measures this patience: when $\delta$ is close to 1, cooperation is sustainable; when $\delta$ is close to 0, each round is effectively a one-shot game.

The catch: punishment in Chicken means crashing. Unlike the Prisoner's Dilemma, where punishment is merely mutual defection, punishment in Chicken is mutual destruction. This makes credible punishment strategies harder to sustain. A threat to crash if the opponent doesn't cooperate is only credible if the threatener has reason to follow through, and following through is always the worst outcome.

---

## Thirteen Days

In October 1962, American reconnaissance flights discovered Soviet nuclear missiles under construction in Cuba, 90 miles from Florida. President Kennedy assembled his Executive Committee to decide on a response.

The options mapped onto the Chicken matrix. Do nothing (swerve): the missiles stay, Soviet influence expands, Kennedy faces political collapse. Launch airstrikes or invade (hold steady): risk Soviet retaliation and a nuclear exchange.

Kennedy chose a naval blockade, which worked as a partial commitment device. It drew a visible line (Soviet ships approaching Cuba would be stopped) without committing to the irreversible step of a military attack. The burden of the next escalation fell on Khrushchev: Soviet ships were approaching the blockade line, and he had to decide whether to challenge it or turn back.

Kennedy told his brother Robert that he estimated the probability of nuclear war at "between one in three and even." The crisis lasted 13 days. Khrushchev agreed to withdraw the missiles; Kennedy privately removed American missiles from Turkey and pledged not to invade Cuba. Both sides swerved, partially, in a negotiated outcome that the simple payoff matrix cannot express.

The resolution reveals a limitation of the model. Real crises are not simultaneous one-shot games. They unfold over days and weeks, with private channels, partial signals, and the possibility of compromise. But the logic of the standoff is genuine: each side was searching for a way to commit credibly, and each side feared that looking too willing to compromise would invite exploitation.

---

## The Doomsday Machine

Schelling's framework points toward a disturbing endpoint. If credible commitment makes deterrence work, the most effective nuclear posture is to automate retaliation entirely. Remove human judgment from the decision. If the enemy knows that a first strike will trigger unstoppable, automatic retaliation, the deterrent becomes perfectly credible because no one can choose restraint.

Stanley Kubrick dramatized this in *Dr. Strangelove* (1964). The film's Soviet Doomsday Machine automatically destroys all life on Earth if a nuclear attack is detected. Kubrick's punchline: the Soviets built it but forgot to announce it. A commitment device that the opponent doesn't know about is strategically worthless.

The Soviet Union came closer to building a real version than most people realize. Their Perimeter system, operational since the 1980s and known in the West as "Dead Hand," could authorize a retaliatory nuclear launch if it detected the Soviet leadership had been destroyed. The system preserved a thin layer of human judgment rather than being fully automatic, a compromise between strategic credibility and the fear of accidental annihilation.

A fully automated Doomsday Machine is the logical limit of commitment: it removes all possibility of mercy, making the threat as credible as physics allows, and as incapable of restraint as the two-car game with a welded steering column.

---

## Hawks and Doves

The same payoff matrix appears in evolutionary biology under a different name.

Animals competing for territory or mates face the same structure. An individual can escalate (fight) or concede (retreat). If both escalate, both are injured. If one concedes, the other takes the resource.

In the early 1970s, two researchers at the University of Sussex asked what happens when animals playing this game cannot choose strategies at all but simply inherit behavioral tendencies from their parents. John Maynard Smith and George Price showed that natural selection drives the population to a stable mix: a fraction $1/C$ of individuals play Hawk (where $C$ is injury cost relative to resource value), matching the mixed Nash equilibrium exactly. Thousands of generations of differential reproduction, with no strategic reasoning anywhere, arrive at the same probabilities a game theorist would calculate.

Animals cannot remove their steering wheels. They cannot make binding commitments or signal future intentions with certainty. Instead, evolution produces a stable distribution of aggressive and submissive phenotypes, and the population settles into an equilibrium where fights happen at a predictable frequency. Individual animals have no strategy; the population has an equilibrium.

Deterrence in human affairs is built on the assumption that rational agents can choose commitment, choose restraint, choose to signal. Evolutionary Chicken suggests that even without choice, even without intention, conflict at a rate of $1/C^2$ per interaction is the mathematical baseline. Below that rate, aggression pays; above it, concession pays. The equilibrium sits at the boundary where the two pressures cancel, and it is set by the cost of conflict alone.
