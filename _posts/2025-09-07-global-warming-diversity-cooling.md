---
layout: post
title: "Global Warming and Diversity Cooling"
date: 2025-09-07
categories: ecology thermodynamics
toc: true
---

## The Same Collapse, Twice

Here is a strange fact: the mathematics of a cooling gas and the mathematics of a dying ecosystem are identical.

When a gas cools, its molecules slow down. They explore fewer states. The number of possible configurations drops. Entropy decreases.

When an ecosystem collapses, species vanish. The community becomes dominated by a few survivors. The number of possible configurations drops. Entropy decreases.

This is not a metaphor. The same equation describes both:

$$
H = -\sum_i p_i \log p_i
$$

In physics, $p_i$ is the probability of a microstate. In ecology, $p_i$ is the fraction of individuals belonging to species $i$. The formula doesn't care which world it's measuring. It counts possibilities.

And here's the twist: global warming doesn't just raise temperatures. It *cools* ecosystems in the entropic sense. As the planet heats up, biological diversity collapses. The living world becomes simpler, more uniform, more predictable. Thermodynamically, it's getting colder.

---

## See It Happen

The simulation below shows how diversity entropy changes as species disappear. Start with a balanced ecosystem, then remove species one by one. Watch the entropy drop.

<div id="diversity-sim" style="max-width: 720px; margin: 1.5em auto;">
  <div style="display: flex; gap: 1em; flex-wrap: wrap; margin-bottom: 1em;">
    <button id="div-reset">Reset (10 species)</button>
    <button id="div-remove">Remove rarest species</button>
    <button id="div-collapse">Simulate collapse</button>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1em;">
    <div style="border: 1px solid #000; padding: 1em; background: #fafafa;">
      <strong>Community composition</strong>
      <canvas id="div-bars" style="width: 100%; height: 180px; margin-top: 0.5em;"></canvas>
      <div class="lightText" style="margin-top: 0.5em;">Species abundance (each bar = one species)</div>
    </div>
    <div style="border: 1px solid #000; padding: 1em; background: #fafafa;">
      <strong>Entropy over time</strong>
      <canvas id="div-entropy" style="width: 100%; height: 180px; margin-top: 0.5em;"></canvas>
      <div class="lightText" style="margin-top: 0.5em;">Shannon entropy H</div>
    </div>
  </div>

  <div style="margin-top: 1em; border: 1px solid #000; padding: 1em; background: #fff;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1em; text-align: center;">
      <div>
        <div class="lightText">Species count</div>
        <div id="div-species" style="font-size: 1.5em; font-weight: bold;">10</div>
      </div>
      <div>
        <div class="lightText">Shannon entropy H</div>
        <div id="div-H" style="font-size: 1.5em; font-weight: bold;">2.303</div>
      </div>
      <div>
        <div class="lightText">Effective species (e^H)</div>
        <div id="div-effective" style="font-size: 1.5em; font-weight: bold;">10.0</div>
      </div>
    </div>
  </div>
</div>

{% raw %}
<script>
(function(){
  const barsCanvas = document.getElementById('div-bars');
  const entropyCanvas = document.getElementById('div-entropy');
  const barsCtx = barsCanvas.getContext('2d');
  const entropyCtx = entropyCanvas.getContext('2d');

  let abundances = [];
  let entropyHistory = [];

  function resizeCanvas(canvas, ctx){
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function resizeAll(){
    resizeCanvas(barsCanvas, barsCtx);
    resizeCanvas(entropyCanvas, entropyCtx);
    draw();
  }

  window.addEventListener('resize', resizeAll);

  function initCommunity(){
    // Start with 10 species, roughly equal abundance with some variation
    abundances = [];
    for(let i = 0; i < 10; i++){
      abundances.push(80 + Math.random() * 40); // 80-120 individuals each
    }
    normalize();
    entropyHistory = [calcEntropy()];
  }

  function normalize(){
    const total = abundances.reduce((a,b) => a + b, 0);
    abundances = abundances.map(x => x / total);
  }

  function calcEntropy(){
    let H = 0;
    for(const p of abundances){
      if(p > 0) H -= p * Math.log(p);
    }
    return H;
  }

  function removeRarest(){
    if(abundances.length <= 1) return;
    // Find smallest
    let minIdx = 0;
    for(let i = 1; i < abundances.length; i++){
      if(abundances[i] < abundances[minIdx]) minIdx = i;
    }
    // Redistribute to dominant species
    const removed = abundances[minIdx];
    abundances.splice(minIdx, 1);
    if(abundances.length > 0){
      // Give most to the largest
      let maxIdx = 0;
      for(let i = 1; i < abundances.length; i++){
        if(abundances[i] > abundances[maxIdx]) maxIdx = i;
      }
      abundances[maxIdx] += removed * 0.7;
      // Rest distributed
      const rest = removed * 0.3 / abundances.length;
      abundances = abundances.map(x => x + rest);
    }
    normalize();
    entropyHistory.push(calcEntropy());
    draw();
    updateStats();
  }

  function simulateCollapse(){
    if(abundances.length <= 1) return;
    const interval = setInterval(() => {
      removeRarest();
      if(abundances.length <= 2) clearInterval(interval);
    }, 300);
  }

  function reset(){
    initCommunity();
    draw();
    updateStats();
  }

  function updateStats(){
    const H = calcEntropy();
    document.getElementById('div-species').textContent = abundances.length;
    document.getElementById('div-H').textContent = H.toFixed(3);
    document.getElementById('div-effective').textContent = Math.exp(H).toFixed(1);
  }

  function draw(){
    drawBars();
    drawEntropy();
  }

  function drawBars(){
    const W = barsCanvas.clientWidth, H = barsCanvas.clientHeight;
    const pad = 10;
    barsCtx.clearRect(0, 0, W, H);

    if(abundances.length === 0) return;

    const barW = (W - pad * 2) / abundances.length - 2;
    const maxP = Math.max(...abundances);

    const colors = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf','#999999','#66c2a5'];

    for(let i = 0; i < abundances.length; i++){
      const barH = (abundances[i] / maxP) * (H - pad * 2);
      const x = pad + i * (barW + 2);
      const y = H - pad - barH;
      barsCtx.fillStyle = colors[i % colors.length];
      barsCtx.fillRect(x, y, barW, barH);
      barsCtx.strokeStyle = '#000';
      barsCtx.strokeRect(x, y, barW, barH);
    }
  }

  function drawEntropy(){
    const W = entropyCanvas.clientWidth, H = entropyCanvas.clientHeight;
    const pad = 30;
    entropyCtx.clearRect(0, 0, W, H);

    // Axes
    entropyCtx.strokeStyle = '#000';
    entropyCtx.lineWidth = 1;
    entropyCtx.beginPath();
    entropyCtx.moveTo(pad, pad);
    entropyCtx.lineTo(pad, H - pad);
    entropyCtx.lineTo(W - pad, H - pad);
    entropyCtx.stroke();

    // Y labels
    entropyCtx.fillStyle = '#000';
    entropyCtx.font = '11px system-ui, sans-serif';
    entropyCtx.textAlign = 'right';
    const maxH = Math.log(10) + 0.1; // ln(10) ≈ 2.3
    entropyCtx.fillText('2.3', pad - 5, pad + 5);
    entropyCtx.fillText('0', pad - 5, H - pad + 5);

    if(entropyHistory.length < 1) return;

    // Draw line
    entropyCtx.strokeStyle = '#2266cc';
    entropyCtx.lineWidth = 2;
    entropyCtx.beginPath();
    const innerW = W - pad * 2;
    const innerH = H - pad * 2;
    for(let i = 0; i < entropyHistory.length; i++){
      const x = pad + (i / Math.max(entropyHistory.length - 1, 1)) * innerW;
      const y = H - pad - (entropyHistory[i] / maxH) * innerH;
      if(i === 0) entropyCtx.moveTo(x, y);
      else entropyCtx.lineTo(x, y);
    }
    entropyCtx.stroke();

    // Draw points
    entropyCtx.fillStyle = '#2266cc';
    for(let i = 0; i < entropyHistory.length; i++){
      const x = pad + (i / Math.max(entropyHistory.length - 1, 1)) * innerW;
      const y = H - pad - (entropyHistory[i] / maxH) * innerH;
      entropyCtx.beginPath();
      entropyCtx.arc(x, y, 4, 0, Math.PI * 2);
      entropyCtx.fill();
    }
  }

  document.getElementById('div-reset').addEventListener('click', reset);
  document.getElementById('div-remove').addEventListener('click', () => { removeRarest(); });
  document.getElementById('div-collapse').addEventListener('click', simulateCollapse);

  // Init
  setTimeout(() => {
    resizeAll();
    initCommunity();
    draw();
    updateStats();
  }, 50);
})();
</script>

<style>
#diversity-sim button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#diversity-sim button:hover {
  background: #eee;
}
</style>
{% endraw %}

---

## Boltzmann's Tombstone

The connection between entropy and counting goes back to Ludwig Boltzmann.

In the 1870s, Boltzmann was fighting a lonely battle in Vienna. He believed that the laws of thermodynamics — the rules governing heat, work, and efficiency — could be explained by statistics. Count all the ways particles can arrange themselves, he argued, and entropy falls out naturally.

His formula:

$$
S = k \log W
$$

$W$ is the number of microstates compatible with a given macrostate. $k$ is Boltzmann's constant. The more ways a system can be arranged while looking the same from the outside, the higher its entropy.

The physics establishment resisted. Ernst Mach and others denied that atoms even existed. Boltzmann grew depressed. In 1906, while on vacation in Trieste, he took his own life.

The equation was later carved on his tombstone in Vienna's Zentralfriedhof. Within a decade, atoms were confirmed, and Boltzmann's vision became the foundation of statistical mechanics.

---

## Shannon's Surprise

In 1948, Claude Shannon was not thinking about physics at all. He was an engineer at Bell Labs, trying to understand the limits of communication.

His question: how much information can you send through a noisy channel? To answer it, he needed a way to measure uncertainty. If you're about to receive a message, how surprised will you be by each symbol?

Shannon defined a quantity he called entropy:

$$
H = -\sum_i p_i \log p_i
$$

If all symbols are equally likely, uncertainty is high. If one symbol dominates, uncertainty is low. The formula captured the "surprise" of a message source.

When Shannon showed his work to the mathematician John von Neumann, von Neumann reportedly said: "You should call it entropy, for two reasons. First, the formula is the same as in statistical mechanics. Second, nobody really understands entropy, so in any debate you'll have the advantage."

Whether the story is true or not, the point stands. Shannon had independently arrived at Boltzmann's formula, starting from completely different premises.

---

## The Formula Doesn't Care

Here is the key insight: the entropy formula measures *possibilities*, regardless of what those possibilities represent.

In a gas, $p_i$ is the probability of microstate $i$. Entropy measures how spread out the system is across its possible configurations.

In a message, $p_i$ is the probability of symbol $i$. Entropy measures the average surprise per symbol.

In an ecosystem, $p_i$ is the fraction of individuals belonging to species $i$. Entropy measures how evenly distributed the community is.

Same formula. Same mathematics. Different interpretations.

This is not a coincidence or a loose analogy. Entropy is a measure of *counting* — specifically, it measures how many equivalent configurations produce the same observable outcome. The subject matter is irrelevant to the mathematics.

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

Both have the same *richness* (4 species). But their entropies differ dramatically.

For Forest A:

$$
H_A = -4 \times \left(\frac{1}{4} \log \frac{1}{4}\right) = \log 4 \approx 1.386
$$

For Forest B:

$$
H_B = -\left(0.85 \log 0.85 + 3 \times 0.05 \log 0.05\right) \approx 0.543
$$

Forest A has more than twice the entropy of Forest B.

What does this mean? Imagine picking a random tree. In Forest A, you genuinely don't know what species you'll get — there's real uncertainty. In Forest B, you can guess "Oak" and be right 85% of the time. The community is more predictable, more uniform, less complex.

The "effective number of species" — defined as $e^H$ — captures this intuition:
- Forest A: $e^{1.386} = 4.0$ effective species
- Forest B: $e^{0.543} = 1.7$ effective species

Forest B has 4 species on paper, but only 1.7 species worth of diversity.

---

## What Heat Does to Diversity

Now consider what happens as climate changes.

Species have thermal tolerances. As temperatures rise, some species can't cope:
- They fail to reproduce
- They're outcompeted by heat-tolerant generalists
- Their food sources disappear
- Their habitats shrink

The species that survive tend to be the same everywhere: widespread, adaptable, generalist species. Ecologists call this *biotic homogenization*.

The pattern is consistent across ecosystems:
- Coral reefs lose specialist species; weedy corals take over
- Forests lose endemic understory plants; invasive grasses spread
- Streams lose sensitive mayflies; pollution-tolerant midges dominate

In each case, the community shifts from Forest A toward Forest B. Richness drops. The remaining species become more dominant. Entropy falls.

---

## The Thermodynamic Irony

Here is the irony that gives this post its title.

In the physical sense, global warming adds heat to the Earth system. The planet's temperature rises. In the thermodynamic sense, you might expect entropy to increase — hotter systems explore more states.

But in the biological sense, the opposite happens. Ecosystems become simpler. Communities lose species. The number of possible ecological configurations shrinks. Shannon entropy — applied to species abundances — decreases.

**Global warming causes diversity cooling.**

The planet heats up. Life cools down.

This is not a contradiction. Physical entropy and ecological entropy measure different things. But the parallel is instructive. Both are measuring possibilities. And in both cases, a loss of possibilities means a loss of structure, complexity, and resilience.

---

## Energy Flow and Order

There's a deeper connection still.

Life on Earth doesn't run on heat. It runs on the *flow* of energy from high-quality (low entropy) to low-quality (high entropy).

Sunlight arrives as concentrated, high-frequency photons. Plants capture it, store it in chemical bonds, and pass it up the food chain. Eventually, the same energy radiates back to space as diffuse infrared — same amount of energy, but spread across many more photons, much higher entropy.

This flow — from order to disorder — is what powers every living thing. Schrödinger called it "negative entropy" or "negentropy." Living systems maintain their structure by exporting entropy to their environment.

Global warming disrupts this flow. Greenhouse gases trap outgoing infrared radiation, reducing the rate at which the Earth can shed entropy. The system backs up. The gradient flattens.

A healthy ecosystem is a dissipative structure — it maintains complexity by channeling energy flow. When the flow is disrupted, the structure simplifies. Species drop out. Communities homogenize. Entropy — in the ecological sense — falls.

---

## What We Lose

A species is not just a name on a list. It's a node in a network of interactions, a repository of genetic information, a way of making a living that took millions of years to evolve.

When diversity collapses, we lose more than species. We lose:

- **Functional redundancy**: Multiple species doing similar jobs means the ecosystem can absorb shocks
- **Ecosystem services**: Pollination, decomposition, water filtration, carbon storage
- **Evolutionary potential**: The raw material for future adaptation
- **Information**: Each species encodes solutions to survival problems that we may never understand

The entropy formula captures something real: the number of ways an ecosystem can be configured while still functioning. When that number drops, the system becomes brittle. It loses its ability to respond to further change.

A low-entropy ecosystem is like a language with only a few words. You can still communicate, but you've lost the capacity for nuance, precision, and adaptation.

---

## The Equation on the Tombstone

Boltzmann's formula links microscopic chaos to macroscopic order. Shannon's formula links symbol frequencies to information content. The same formula, applied to species abundances, links community structure to ecological complexity.

The mathematics doesn't know the difference. It counts possibilities, wherever they arise.

When we burn fossil fuels and heat the planet, we trigger a cascade that runs through physics, chemistry, and biology. Temperatures rise. Species shift and vanish. Communities simplify. The number of possible configurations — the entropy of the living world — falls.

Boltzmann saw that entropy measures how many ways a system can be arranged. He was right. And the living world is losing its arrangements, one species at a time.

Global warming and biodiversity loss are not two crises. They are one crisis, measured in two currencies. The same equation sits on Boltzmann's tombstone and in every ecology textbook. It's telling us something important.

The planet is heating up. Life is cooling down.
