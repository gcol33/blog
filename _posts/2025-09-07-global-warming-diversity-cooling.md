---
layout: post
title: "Global Warming and Diversity Cooling"
date: 2025-09-07
categories: ecology thermodynamics
toc: true
---

## The Same Collapse, Twice

When a gas cools, its molecules slow down. They explore fewer states. The number of possible configurations drops. Entropy decreases.

When an ecosystem collapses, species vanish. The community becomes dominated by a few survivors. The number of possible configurations drops. Entropy decreases.

One equation describes both:

$$
H = -\sum_i p_i \log p_i
$$

In physics, $p_i$ is the probability of a microstate. In ecology, $p_i$ is the fraction of individuals belonging to species $i$. The formula doesn't care which world it measures. It counts possibilities.

And here's the twist: global warming doesn't just raise temperatures. It *cools* ecosystems in the entropic sense. As the planet heats up, biological diversity collapses. The living world becomes simpler, more uniform, more predictable.

Thermodynamically, it's getting colder.

---

## Simulation

Remove species one by one. Entropy drops.

<div id="diversity-sim" style="max-width: 720px; margin: 1.5em auto;">
  <div style="display: flex; gap: 1em; flex-wrap: wrap; margin-bottom: 1em;">
    <button id="div-reset">Reset (10 species)</button>
    <button id="div-remove">Remove rarest species</button>
    <button id="div-collapse">Simulate collapse</button>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1em;">
    <div>
      <strong>Community composition</strong>
      <canvas id="div-bars" style="width: 100%; height: 180px; margin-top: 0.5em; background: #fff; border: 1px solid #000;"></canvas>
      <div class="lightText" style="margin-top: 0.5em;">Species abundance (each bar = one species)</div>
    </div>
    <div>
      <strong>Entropy over time</strong>
      <canvas id="div-entropy" style="width: 100%; height: 180px; margin-top: 0.5em; background: #fff; border: 1px solid #000;"></canvas>
      <div class="lightText" style="margin-top: 0.5em;">Shannon entropy H</div>
    </div>
  </div>

  <div style="margin-top: 1em;">
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
    abundances = [];
    for(let i = 0; i < 10; i++){
      abundances.push(80 + Math.random() * 40);
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
    let minIdx = 0;
    for(let i = 1; i < abundances.length; i++){
      if(abundances[i] < abundances[minIdx]) minIdx = i;
    }
    const removed = abundances[minIdx];
    abundances.splice(minIdx, 1);
    if(abundances.length > 0){
      let maxIdx = 0;
      for(let i = 1; i < abundances.length; i++){
        if(abundances[i] > abundances[maxIdx]) maxIdx = i;
      }
      abundances[maxIdx] += removed * 0.7;
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
    const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const pad = 0.875 * rem;
    barsCtx.clearRect(0, 0, W, H);

    // Double border
    barsCtx.strokeStyle = '#000';
    barsCtx.lineWidth = 1;
    barsCtx.strokeRect(pad, pad, W - pad * 2, H - pad * 2);

    if(abundances.length === 0) return;

    const innerPad = pad * 1.5;
    const barW = (W - innerPad * 2) / abundances.length - 2;
    const maxP = Math.max(...abundances);

    for(let i = 0; i < abundances.length; i++){
      const barH = (abundances[i] / maxP) * (H - innerPad * 2);
      const x = innerPad + i * (barW + 2);
      const y = H - innerPad - barH;
      barsCtx.fillStyle = '#fff';
      barsCtx.fillRect(x, y, barW, barH);
      barsCtx.strokeStyle = '#000';
      barsCtx.strokeRect(x, y, barW, barH);
    }
  }

  function drawEntropy(){
    const W = entropyCanvas.clientWidth, H = entropyCanvas.clientHeight;
    const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const pad = 0.875 * rem;
    const leftMargin = 2 * rem;
    const bottomMargin = 0.5 * rem;
    entropyCtx.clearRect(0, 0, W, H);

    // Double border
    entropyCtx.strokeStyle = '#000';
    entropyCtx.lineWidth = 1;
    entropyCtx.strokeRect(pad, pad, W - pad * 2, H - pad * 2);

    const chartLeft = pad + leftMargin;
    const chartRight = W - pad - pad;
    const chartTop = pad + pad;
    const chartBottom = H - pad - bottomMargin;
    const chartW = chartRight - chartLeft;
    const chartH = chartBottom - chartTop;

    // Y-axis labels
    entropyCtx.fillStyle = '#000';
    entropyCtx.font = '11px system-ui, sans-serif';
    entropyCtx.textAlign = 'right';
    const maxH = Math.log(10) + 0.1;
    entropyCtx.fillText('2.3', chartLeft - 4, chartTop + 4);
    entropyCtx.fillText('0', chartLeft - 4, chartBottom + 4);

    if(entropyHistory.length < 1) return;

    entropyCtx.strokeStyle = '#000';
    entropyCtx.lineWidth = 2;
    entropyCtx.beginPath();
    for(let i = 0; i < entropyHistory.length; i++){
      const x = chartLeft + (i / Math.max(entropyHistory.length - 1, 1)) * chartW;
      const y = chartBottom - (entropyHistory[i] / maxH) * chartH;
      if(i === 0) entropyCtx.moveTo(x, y);
      else entropyCtx.lineTo(x, y);
    }
    entropyCtx.stroke();

    entropyCtx.fillStyle = '#000';
    for(let i = 0; i < entropyHistory.length; i++){
      const x = chartLeft + (i / Math.max(entropyHistory.length - 1, 1)) * chartW;
      const y = chartBottom - (entropyHistory[i] / maxH) * chartH;
      entropyCtx.beginPath();
      entropyCtx.arc(x, y, 4, 0, Math.PI * 2);
      entropyCtx.fill();
    }
  }

  document.getElementById('div-reset').addEventListener('click', reset);
  document.getElementById('div-remove').addEventListener('click', () => { removeRarest(); });
  document.getElementById('div-collapse').addEventListener('click', simulateCollapse);

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

In the 1870s, Boltzmann was fighting a lonely battle in Vienna. He believed that thermodynamics—the rules governing heat, work, and efficiency—could be explained by statistics. Count all the ways particles can arrange themselves, he argued, and entropy falls out naturally.

His formula:

$$
S = k \log W
$$

$W$ is the number of microstates compatible with a given macrostate. $k$ is Boltzmann's constant. The more ways a system can be arranged while looking the same from the outside, the higher its entropy.

The physics establishment resisted. Ernst Mach and others denied that atoms even existed. Boltzmann grew isolated and depressed. In 1906, while on vacation in Trieste, he took his own life.

The equation was later carved on his tombstone in Vienna's Zentralfriedhof. Within a decade, atoms were confirmed, and Boltzmann's vision became the foundation of statistical mechanics.

---

## Shannon's Surprise

In 1948, Claude Shannon was not thinking about physics. He was an engineer at Bell Labs, trying to understand the limits of communication.

His question: how much information can you send through a noisy channel? To answer it, he needed a way to measure uncertainty. If you're about to receive a message, how surprised will you be by each symbol?

Shannon defined a quantity he called entropy:

$$
H = -\sum_i p_i \log p_i
$$

If all symbols are equally likely, uncertainty is high. If one symbol dominates, uncertainty is low. The formula captured the average "surprise" of a message source.

When Shannon showed his work to John von Neumann, von Neumann reportedly said: "You should call it entropy, for two reasons. First, the formula is the same as in statistical mechanics. Second, nobody really understands entropy, so in any debate you'll have the advantage."

Whether the story is true or not, Shannon had independently arrived at Boltzmann's formula, starting from completely different premises.

---

## The Formula Doesn't Care

Here is the key insight: the entropy formula measures *possibilities*, regardless of what those possibilities represent.

In a gas, $p_i$ is the probability of microstate $i$. Entropy measures how spread out the system is across configurations.

In a message, $p_i$ is the probability of symbol $i$. Entropy measures average surprise per symbol.

In an ecosystem, $p_i$ is the fraction of individuals belonging to species $i$. Entropy measures how evenly distributed the community is.

Same formula in each case. Entropy measures *counting*—specifically, how many equivalent configurations produce the same observable outcome. The subject matter is irrelevant to the mathematics.

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

Both have the same *richness* (4 species). Their entropies differ dramatically.

For Forest A:

$$
H_A = -4 \times \left(\frac{1}{4} \log \frac{1}{4}\right) = \log 4 \approx 1.386
$$

For Forest B:

$$
H_B = -\left(0.85 \log 0.85 + 3 \times 0.05 \log 0.05\right) \approx 0.543
$$

Forest A has more than twice the entropy of Forest B.

What does this mean? Pick a random tree. In Forest A, you genuinely don't know what species you'll get. In Forest B, guess "Oak" and you're right 85% of the time. The community is predictable, uniform, simple.

The "effective number of species"—defined as $e^H$—captures this:
- Forest A: $e^{1.386} = 4.0$ effective species
- Forest B: $e^{0.543} = 1.7$ effective species

Forest B has 4 species on paper. It has 1.7 species worth of diversity.

---

## What Heat Does to Diversity

Now consider what happens as climate changes.

Species have thermal tolerances. As temperatures rise, some can't cope:
- They fail to reproduce
- They're outcompeted by heat-tolerant generalists
- Their food sources disappear
- Their habitats shrink

The species that survive tend to be the same everywhere: widespread, adaptable, generalist species. Ecologists call this *biotic homogenization*.

The pattern is consistent across ecosystems:
- Coral reefs lose specialist species; weedy corals take over
- Forests lose endemic understory plants; invasive grasses spread
- Streams lose sensitive mayflies; pollution-tolerant midges dominate

In each case, the community shifts from Forest A toward Forest B. Richness drops. The remaining species become dominant. Entropy falls.

---

## The Thermodynamic Irony

Here is the irony that gives this post its title.

In the physical sense, global warming adds heat to the Earth system. Temperatures rise. You might expect entropy to increase—hotter systems explore more states.

But in the biological sense, the opposite happens. Ecosystems become simpler. Communities lose species. The number of possible ecological configurations shrinks. Shannon entropy—applied to species abundances—decreases.

**Global warming causes diversity cooling.**

The planet heats up. Life cools down.

This is not a contradiction. Physical entropy and ecological entropy measure different things. But the parallel is instructive. Both measure possibilities. A loss of possibilities means a loss of structure, complexity, and resilience.

---

## Energy Flow and Order

There's a deeper connection still.

Life on Earth doesn't run on heat. It runs on the *flow* of energy from high-quality (low entropy) to low-quality (high entropy).

Sunlight arrives as concentrated, high-frequency photons. Plants capture it, store it in chemical bonds, and pass it up the food chain. Eventually, the same energy radiates back to space as diffuse infrared—same total energy, but spread across many more photons, much higher entropy.

This flow—from order to disorder—powers every living thing. Schrödinger called it "negentropy." Living systems maintain their structure by exporting entropy to their environment.

Global warming disrupts this flow. Greenhouse gases trap outgoing infrared, reducing the rate at which Earth can shed entropy. The gradient flattens.

A healthy ecosystem is a dissipative structure—it maintains complexity by channeling energy flow. When the flow is disrupted, the structure simplifies. Species drop out. Communities homogenize. Entropy, in the ecological sense, falls.

---

## What We Lose

A species is not just a name on a list. It's a node in a network of interactions, a repository of genetic information, a way of making a living that took millions of years to evolve.

When diversity collapses, we lose more than species:

- **Functional redundancy**: Multiple species doing similar jobs means the ecosystem can absorb shocks
- **Ecosystem services**: Pollination, decomposition, water filtration, carbon storage
- **Evolutionary potential**: The raw material for future adaptation
- **Information**: Each species encodes solutions to survival problems we may never understand

The entropy formula captures something real: the number of ways an ecosystem can be configured while still functioning. When that number drops, the system becomes brittle. It loses its ability to respond to further change.

A low-entropy ecosystem is like a language with only a few words. You can still communicate, but you've lost the capacity for nuance, precision, and adaptation.

---

## The Equation on the Tombstone

Boltzmann's formula links microscopic chaos to macroscopic order. Shannon's formula links symbol frequencies to information content. The same formula, applied to species abundances, links community structure to ecological complexity.

When we burn fossil fuels and heat the planet, we trigger a cascade that runs through physics, chemistry, and biology. Temperatures rise. Species shift and vanish. Communities simplify. The number of possible configurations—the entropy of the living world—falls.

Boltzmann saw that entropy measures how many ways a system can be arranged. The living world is losing its arrangements, one species at a time.

Global warming and biodiversity loss are connected through the same mathematics. Physical entropy and ecological entropy measure different quantities, but both track the number of possible configurations. The formula on Boltzmann's tombstone appears in ecology textbooks for a reason.
