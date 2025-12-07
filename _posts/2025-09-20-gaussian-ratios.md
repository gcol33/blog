---
layout: post
title: "Why Dividing Two Random Numbers Reveals π"
date: 2025-09-20
categories: probability statistics
---

### Where more data doesn’t mean more certainty

Take two random numbers and divide them.
Do it again. And again.

Now average the results.
Does the number settle down?

No matter how many times you repeat the experiment, the mean refuses to converge. And hidden inside that chaos is something even stranger, surfacing in a place that seems to have nothing to do with circles...

Try it yourself: collect the slopes, count how many land in a narrow strip around horizontal, then scale by the strip’s width. A circle’s number quietly emerges.

<div id="pi-demo" style="max-width: 720px; margin: 0 auto;">
  <canvas id="hist" style="width:100%; height:300px; background:#fff; border:1px solid #000;"></canvas>

  <!-- Controls: responsive (4 → 2 → 1 columns) -->
  <div class="pi-controls">
    <label>Samples n
      <input type="range" id="nSlider" min="10000" max="1000000" step="10000" value="50000" />
    </label>
    <label>Band half-width h
      <input type="range" id="hSlider" min="0.001" max="0.30" step="0.0005" value="0.10" />
    </label>
    <label>Plot range |Z| ≤ R
      <input type="range" id="rangeSlider" min="2" max="8" step="0.5" value="4" />
    </label>
    <label>Bins
      <input type="range" id="binsSlider" min="21" max="121" step="1" value="81" />
    </label>
  </div>

  <!-- Stats -->
  <div id="stats" class="pi-stats">
    <div class="pi-stat-row"><span>Total samples n:</span><strong id="nOut">0</strong></div>
    <div class="pi-stat-row"><span>Fraction inside band:</span><strong id="fracOut">0</strong></div>
    <div class="pi-stat-row"><span>π-ish =</span><strong id="piOut">—</strong></div>
  </div>

  <p class="pi-note">
    Formula used here:<br/>
    \[
      \pi_{\text{ish}} \;=\; \frac{\text{total width of the band}}{\text{fraction of slopes inside it}}
    \]<br/>
    where total width = \(2h\) (from \(-h\) to \(+h\)).  
    Narrow the band. Increase the samples. The number drifts toward 3.14…
  </p>
</div>

{% raw %}
<style>
#pi-demo { font-variant-numeric: tabular-nums; }
#pi-demo * { box-sizing: border-box; }

/* Canvas tweaks for small screens */
@media (max-width: 560px){
  #pi-demo canvas#hist{ height: 240px !important; }
}

/* Controls: responsive grid */
#pi-demo .pi-controls{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  margin-top: 10px;
}
@media (max-width: 820px){
  #pi-demo .pi-controls{ grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 560px){
  #pi-demo .pi-controls{ grid-template-columns: 1fr; }
}

/* Slider labels */
#pi-demo label{
  display: flex;
  flex-direction: column;
  font-size: 0.95em;
  gap: 4px;
}

/* Sliders */
#pi-demo input[type="range"]{
  width: 100%;
  appearance: none;
  height: 6px;
  background: #eee;
  outline: none;
  touch-action: manipulation;
}
#pi-demo input[type="range"]::-webkit-slider-thumb{
  appearance: none; width: 14px; height: 14px;
  border-radius: 50%; background: #000; cursor: pointer;
}
#pi-demo input[type="range"]::-moz-range-thumb{
  width: 14px; height: 14px; border: none;
  border-radius: 50%; background: #000; cursor: pointer;
}

/* Stats: aligned left */
#pi-demo .pi-stats{
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 6px;
}
#pi-demo .pi-stat-row{
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}
#pi-demo .pi-stat-row span,
#pi-demo .pi-stat-row strong{
  text-align: left;
}

/* Explanatory note */
#pi-demo .pi-note{
  font-size: 0.95em;
  color: #111;
  margin-top: 6px;
  line-height: 1.4;
}
</style>

<script>
// -------- RNG (Box–Muller, polar form) ----------
function randn(){
  let u=0,v=0,s=0;
  do{ u=Math.random()*2-1; v=Math.random()*2-1; s=u*u+v*v; }while(s===0||s>=1);
  return u*Math.sqrt(-2*Math.log(s)/s);
}

// -------- Elements ----------
const canvas = document.getElementById('hist'), ctx = canvas.getContext('2d');
const nSlider = document.getElementById('nSlider');
const hSlider = document.getElementById('hSlider');
const rangeSel = document.getElementById('rangeSlider');
const binsSel  = document.getElementById('binsSlider');

const nOut   = document.getElementById('nOut');
const fracOut= document.getElementById('fracOut');
const piOut  = document.getElementById('piOut');

// -------- Sample cache ----------
let Z = new Float64Array(0);
function regenerateSamples(n){
  Z = new Float64Array(n);
  let j = 0;
  while(j < n){
    const x = randn(), y = randn();
    const z = y / x;
    if(Number.isFinite(z)){ Z[j++] = z; }
  }
}

// -------- DPI-aware canvas ----------
function resizeCanvas(){
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const rect = canvas.getBoundingClientRect();
  canvas.width  = Math.round(rect.width  * dpr);
  canvas.height = Math.round(rect.height * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}
window.addEventListener('resize', () => { resizeCanvas(); redrawOnly(); });
resizeCanvas();

// -------- Helpers ----------
function displayStep(){
  const R = parseFloat(rangeSel.value);
  const B = parseInt(binsSel.value, 10);
  return (2*R)/B;
}
function clamp(val, lo, hi){ return Math.min(hi, Math.max(lo, val)); }
function quantizeToStep(val, step){
  if(step <= 0 || !Number.isFinite(step)) return val;
  const k = Math.max(1, Math.round(val / step));
  return k * step;
}
function updateHSliderBounds(){
  const step = displayStep();
  const R = parseFloat(rangeSel.value);
  hSlider.min = step.toFixed(6);
  hSlider.max = R.toFixed(6);
  hSlider.step = (step/10).toFixed(6);
}

// -------- State for band width ----------
let hCount = parseFloat(hSlider.value);

// -------- Stats ----------
function recomputeStats(){
  const n = Z.length;
  let count = 0;
  for(let i=0;i<n;i++){
    if(Math.abs(Z[i]) <= hCount) count++;
  }
  const pHat = n ? (count/n) : 0;
  const piHat = pHat > 0 ? (2*Math.atan(hCount)) / pHat : NaN;

  nOut.textContent    = n.toLocaleString();
  fracOut.textContent = pHat ? pHat.toFixed(7) : '0';
  piOut.textContent   = Number.isFinite(piHat) ? piHat.toFixed(7) : '—';
}

// -------- Histogram redraw ----------
function redrawOnly(){
  const R = parseFloat(rangeSel.value);
  const B = parseInt(binsSel.value, 10);
  const hist = new Uint32Array(B);
  const mid = (B-1)/2;
  for(let i=0;i<Z.length;i++){
    const z = Z[i];
    if(Math.abs(z) <= R){
      const bin = Math.round(mid + (z/R)*mid);
      if(bin >= 0 && bin < B) hist[bin]++;
    }
  }
  const step = displayStep();
  const hDraw = clamp(quantizeToStep(hCount, step), step, R);
  drawHist(hist, R, hDraw);
}

function drawHist(hist, R, hDraw){
  const w = canvas.clientWidth, H = canvas.clientHeight;
  const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
  const pad = 0.875 * rem, innerW = w - pad*2, innerH = H - pad*2;

  ctx.clearRect(0,0,w,H);
  ctx.strokeStyle = '#000'; ctx.lineWidth = 1;
  ctx.strokeRect(pad, pad, innerW, innerH);

  const pixPerZ = innerW / (2*R), midX = pad + innerW/2;
  ctx.fillStyle = '#ddd';
  ctx.fillRect(midX - hDraw*pixPerZ, pad, 2*hDraw*pixPerZ, innerH);

  const B = hist.length;
  const maxCount = Math.max(1, ...hist), binW = innerW / B;
  ctx.strokeStyle = '#000';
  for(let i=0;i<B;i++){
    const x = pad + i*binW;
    const barH = (hist[i]/maxCount) * innerH;
    ctx.strokeRect(x, pad + innerH - barH, binW, barH);
  }

  ctx.setLineDash([4,4]); ctx.strokeStyle = '#000';
  ctx.beginPath();
  ctx.moveTo(midX - hDraw*pixPerZ, pad); ctx.lineTo(midX - hDraw*pixPerZ, pad + innerH);
  ctx.moveTo(midX + hDraw*pixPerZ, pad); ctx.lineTo(midX + hDraw*pixPerZ, pad + innerH);
  ctx.stroke();
  ctx.setLineDash([]);
}

// -------- Wiring --------
nSlider.addEventListener('input', () => {
  regenerateSamples(parseInt(nSlider.value,10));
  recomputeStats();
  redrawOnly();
});
hSlider.addEventListener('input', () => {
  const step = displayStep();
  const R = parseFloat(rangeSel.value);
  const hRaw = parseFloat(hSlider.value);
  const hSnap = clamp(quantizeToStep(hRaw, step), step, R);
  hCount = hSnap;
  hSlider.value = hSnap.toFixed(6);
  recomputeStats();
  redrawOnly();
});
function onRangeOrBins(){
  updateHSliderBounds();
  const step = displayStep();
  const R = parseFloat(rangeSel.value);
  const hSnap = clamp(quantizeToStep(hCount, step), step, R);
  if (Math.abs(hSnap - hCount) > 1e-12){
    hCount = hSnap;
    hSlider.value = hSnap.toFixed(6);
    recomputeStats();
  }
  redrawOnly();
}
rangeSel.addEventListener('input', onRangeOrBins);
binsSel .addEventListener('input', onRangeOrBins);

// init
updateHSliderBounds();
regenerateSamples(parseInt(nSlider.value,10));
recomputeStats();
redrawOnly();
</script>
{% endraw %}


Why π?
Why does averaging fail, even with mountains of data?
To find out we need to go back to Gauss, to Cauchy, and to a curve first drawn in 1748.


### How a Simple Curve Defied Gauss  

Gauss believed in certainty through numbers. His law of errors, the Gaussian bell curve, promised that mistakes in measurement were well-behaved. The assumptions were clear: errors came from many small independent causes, variance was finite, and averages converged to the truth. The law of large numbers guaranteed stability of the mean, the central limit theorem explained the bell shape, and the method of least squares rested securely on these foundations. With more data, you always approached certainty.  

Cauchy broke that faith. In 1853, before the Académie des Sciences in Paris, he presented a rival law of errors in which variance was infinite and averages refused to settle. Joseph Bienaymé rose to defend Gauss, warning that least squares collapsed without finite variance. But Cauchy insisted that mathematics itself admitted such laws, and that in their presence the Gaussian guarantees failed. With more data, you did not get closer to the truth. You only deepened the confusion.  

The curve he used was not obscure. It had been introduced a century earlier, in 1748, by Maria Gaetana Agnesi in her *Instituzioni Analitiche*. Agnesi was not thinking about probability at all. She worked in the **geometric analytic tradition** of the 18th century, when curves were defined by geometric constructions and then explored with the new tools of calculus. This tradition served three purposes: it bridged the visual world of geometry with the symbolic power of analysis, it contributed to the encyclopedic catalog of named curves such as the cycloid, cissoid, and lemniscate, and it gave students concrete, visual examples in an age when calculus was still new.  

Agnesi’s *Instituzioni* was written not in Latin but in Italian, aimed at students rather than savants, and designed to systematize analysis in a clear, accessible way. Within this project the *versiera* fit perfectly. It came from a simple construction: a circle, a fixed point on its diameter, a line rotating around it, and a point tracing where it cut an axis. The resulting curve was bounded, symmetric, and easy to draw. Its equation was  

$$
y=\frac{a^3}{x^2+a^2},
$$  

which for $a=1$ reduces to  

$$
y=\frac{1}{1+x^2}.
$$  

Its analytic elegance was undeniable: a rational function whose integral was the arctangent, tying it directly back to circle geometry. For Agnesi, it was an ideal teaching curve. Later, through mistranslation, it would acquire the odd name “Witch of Agnesi.”  

Cauchy saw something different. He turned Agnesi’s curve into a probability law of errors, a direct challenge to Gauss’s assumptions. Normalized, it becomes  

$$
f(x)=\frac{1}{\pi(1+x^2)}.
$$  

The total area under the curve is still one:  

$$
\frac{1}{\pi}\int_{-\infty}^{\infty}\frac{dx}{1+x^2}
=\frac{1}{\pi}\Big(\tfrac{\pi}{2}-(-\tfrac{\pi}{2})\Big)=1,
$$  

so it qualifies as a density. But unlike Gauss’s bell curve, its tails decay too slowly. The mean diverges. By symmetry the principal value is zero, but the absolute expectation  

$$
\int_{-\infty}^{\infty} |x|f(x)\,dx
=\frac{2}{\pi}\int_{0}^{\infty}\frac{x}{1+x^2}\,dx
=\frac{1}{\pi}\ln u\Big|_{1}^{\infty}
$$  

is infinite. The variance fares no better. Computing  

$$
\int_{-\infty}^{\infty} x^2 f(x)\,dx
=\frac{2}{\pi}\int_{0}^{\infty}\left(1-\frac{1}{1+x^2}\right)\!dx,
$$  

and truncating at $R$ gives  

$$
\frac{2}{\pi}(R-\arctan R),
$$  

which grows without bound as $R\to\infty$.  

Cauchy’s conclusion was devastating. Here was a legitimate law of errors with no mean and no variance. Averages wandered instead of converging. The method of least squares lost its justification. The central limit theorem did not apply. The Gaussian promise of certainty was not universal. 

Only later did mathematicians discover a simpler route to the same law: take two independent Gaussians, divide one by the other, and Cauchy’s distribution reappears. That modern shortcut is where we turn next.  

---

### Geometry of the slope  

The strange behavior of the ratio becomes clear once you look at the geometry. Start with the pair $(X,Y)$ of independent standard Gaussians. Their joint density  

$$
g(x,y) = \frac{1}{2\pi} e^{-\tfrac{1}{2}(x^2+y^2)}
$$  

depends only on the radius $r=\sqrt{x^2+y^2}$. Spin the plane and nothing changes. The Gaussian cloud is rotationally symmetric: no direction is special.  

That symmetry has a consequence. In polar coordinates $(r,\theta)$ with $x=r\cos\theta$ and $y=r\sin\theta$, the density becomes  

$$
g(r,\theta)\,r\,dr\,d\theta = \frac{1}{2\pi} e^{-r^2/2}\, r\,dr\,d\theta,
$$  

which shows that $\theta$ is uniform on $(-\pi,\pi)$. Slopes $y/x$ correspond to angles in $(-\tfrac{\pi}{2},\tfrac{\pi}{2})$, so  

$$
\theta \sim \text{Uniform}\!\left(-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right).
$$  

Now  

$$
Z = \frac{Y}{X} = \tan\theta,
$$  

the slope of the line through the origin and the random point $(X,Y)$. Picking a Gaussian ratio is the same as picking a random direction and asking how steep it is. Because $\theta$ is uniform, the density of $Z$ comes from the change of variables formula:  

$$
f_Z(z) = \frac{1}{\pi}\cdot \frac{1}{1+z^2}.
$$  

The heavy tails now have a simple explanation. As $\theta$ approaches $\pm\tfrac{\pi}{2}$, the slope shoots to infinity. Vertical directions are not rare — they have the same chance as any other angle — so extreme ratios appear often. This is why averages fail to settle: steep slopes keep intruding.  

---

### Algebraic Proof  

Cauchy himself never used this geometric shortcut; probability theory in 1853 did not yet have the modern language of random variables and transformations. His argument stayed analytic, tied to Agnesi’s curve. The ratio-of-Gaussians view came later, in the early 20th century, as statisticians such as R. A. Fisher formalized distribution theory. It was then recognized that the Cauchy distribution is the law of a Gaussian ratio, in the same way that the $t$-distribution is built from a Gaussian divided by a chi-square.  

Formally, let $X$ and $Y$ be independent standard Gaussians and set $Z=Y/X$. The density is obtained by integrating out $X$:  

$$
f_Z(z) = \int_{-\infty}^\infty f_{X,Y}(x,zx)\,|x|\,dx,
$$  

with $f_{X,Y}(x,y) = \tfrac{1}{2\pi}\exp[-\tfrac{1}{2}(x^2+y^2)]$. Substituting $y=zx$ gives  

$$
f_Z(z) = \int_{-\infty}^\infty \frac{1}{2\pi} \exp\!\left(-\tfrac{1}{2}(1+z^2)x^2\right) |x|\,dx.
$$  

Since the integrand is even,  

$$
f_Z(z) = \frac{1}{\pi}\int_{0}^\infty x \exp\!\left(-\tfrac{1}{2}(1+z^2)x^2\right) dx.
$$  

Let $u=\tfrac{1}{2}(1+z^2)x^2$, so $du=(1+z^2)x\,dx/2$. Then  

$$
f_Z(z) = \frac{1}{\pi}\int_{0}^\infty e^{-u}\,\frac{du}{1+z^2}
       = \frac{1}{\pi(1+z^2)}.
$$  

The density that Cauchy introduced by analytic argument is exactly the one that falls out of this modern calculation.  

### A law without an average  

The density we derived,  

$$
f(z) = \frac{1}{\pi(1+z^2)},
$$  

is the **Cauchy distribution**. Its height at zero is  

$$
f(0) = \frac{1}{\pi}.
$$  

That is exactly the fraction of slopes you expect to land inside a narrow band, once rescaled by the band’s width. Rearranging gives the formula from the opening experiment:  

$$
\pi = \frac{2h}{\Pr(|Z|\le h)} \quad \text{for small } h.
$$  

So the number your slider converges to is **π**. The constant comes not from circles but from the length of the angle interval: $\theta=\arctan(Y/X)$ is uniform on $(-\tfrac{\pi}{2},\tfrac{\pi}{2})$, an interval of length π. Each slice of angle of width $\varepsilon$ always carries probability $\varepsilon/\pi$. Push that uniform angle through the tangent, and π controls the entire distribution of slopes.  

The Cauchy law breaks every Gaussian intuition:

- **No mean**: averages drift endlessly, never converging.  
- **No variance**: tails are too heavy for second moments.  
- **Stable**: sums of Cauchy variables stay Cauchy, but without narrowing.  
- **CLT fails**: with infinite variance, the central limit theorem gives no refuge; more samples bring no certainty.  

Later developments linked the Cauchy to the wider family of $t$-distributions. In 1908 William Sealy Gosset introduced the $t$ law while working at Guinness. With one degree of freedom, the $t$ reduces exactly to the Cauchy. Among all $t$ distributions, it is the simplest and the only one without an average.