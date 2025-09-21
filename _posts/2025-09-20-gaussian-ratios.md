---
layout: post
title: "Why Dividing Two Random Numbers Reveals π"
date: 2025-09-20
categories: probability statistics
---

## Where more data doesn’t mean more certainty

Take two random numbers, both drawn from the bell curve.  
Divide one by the other, and something strange happens.  

The result does not behave like an average.  
No matter how much data you collect, the numbers swing wildly.  
And hiding inside the pattern is a constant that seems to have nothing to do with probability at all: π.  

Why π?  
And why does more data fail to bring certainty?  

You can try it yourself. Watch what happens when you collect slopes, check how many fall inside a thin band around horizontal, and then rescale by the band’s width:

<div id="pi-demo" style="max-width: 720px; margin: 0 auto;">
  <canvas id="hist" style="width:100%; height:300px; background:#fff; border:1px solid #000;"></canvas>

  <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:10px; margin-top:10px;">
    <label>Samples n
      <input type="range" id="nSlider" min="1000" max="100000" step="1000" value="40000" />
    </label>
    <label>Band half-width h (slopes with |Z| ≤ h)
      <input type="range" id="hSlider" min="0.02" max="0.30" step="0.005" value="0.10" />
    </label>
    <label>Plot range |Z| ≤ R
      <input type="range" id="rangeSlider" min="2" max="8" step="0.5" value="4" />
    </label>
  </div>

  <div style="display:flex; gap:10px; align-items:center; margin:8px 0;">
    <label>Bins
      <input type="range" id="binsSlider" min="21" max="281" step="20" value="81" />
    </label>
  </div>

  <div id="stats" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:10px;">
    <div style="border-top:1px solid #000; padding:6px 0; display:flex; justify-content:space-between;">
      <span>Total samples n</span><strong id="nOut">0</strong>
    </div>
    <div style="border-top:1px solid #000; padding:6px 0; display:flex; justify-content:space-between;">
      <span>Fraction inside band</span><strong id="fracOut">0</strong>
    </div>
    <div style="border-top:1px solid #000; padding:6px 0; display:flex; justify-content:space-between;">
      <span>π-ish (width ÷ fraction)</span><strong id="piOut">—</strong>
    </div>
  </div>

  <p style="font-size:0.95em; color:#111; margin-top:6px;">
    Formula used here:<br/>
    \[
      \pi_{\text{ish}} \;=\; \frac{\text{total width of the band}}{\text{fraction of slopes inside it}}
    \]<br/>
    where total width = \(2h\) (from \(-h\) to \(+h\)).  
    Narrow the band. Increase the samples. The number drifts toward 3.14…  
    Why should slopes of random points conspire to reveal π?
  </p>
</div>

{% raw %}
<style>
#pi-demo input[type="range"]{ width:100%; appearance:none; height:6px; background:#eee; outline:none; }
#pi-demo input[type="range"]::-webkit-slider-thumb{ appearance:none; width:14px; height:14px; border-radius:50%; background:#000; cursor:pointer; }
</style>

<script>
// standard normal via Box-Muller
function randn(){
  let u=0,v=0,s=0;
  do{ u=Math.random()*2-1; v=Math.random()*2-1; s=u*u+v*v; }while(s===0||s>=1);
  return u*Math.sqrt(-2*Math.log(s)/s);
}

// elements
const canvas=document.getElementById('hist'), ctx=canvas.getContext('2d');
const nSlider=document.getElementById('nSlider'), hSlider=document.getElementById('hSlider');
const rangeSlider=document.getElementById('rangeSlider'), binsSlider=document.getElementById('binsSlider');
const nOut=document.getElementById('nOut'), fracOut=document.getElementById('fracOut'), piOut=document.getElementById('piOut');

// DPR-aware canvas
function resizeCanvas(){ const dpr=Math.min(window.devicePixelRatio||1,2);
  const rect=canvas.getBoundingClientRect(); canvas.width=Math.round(rect.width*dpr);
  canvas.height=Math.round(rect.height*dpr); ctx.setTransform(dpr,0,0,dpr,0,0); }
window.addEventListener('resize',()=>{ resizeCanvas(); simulateAndDraw(); });
resizeCanvas();

function simulateAndDraw(){
  const n=parseInt(nSlider.value,10);
  const R=parseFloat(rangeSlider.value);
  const B=parseInt(binsSlider.value,10);
  const binWidth = (2*R)/B;
  let h=parseFloat(hSlider.value);
  if(h<binWidth) h=binWidth;

  const hist=new Array(B).fill(0), mid=(B-1)/2; let count=0;

  for(let i=0;i<n;i++){
    const x=randn(), y=randn(), z=y/x;
    if(!Number.isFinite(z)) continue;
    if(Math.abs(z)<=h) count++;
    if(Math.abs(z)<=R){
      const bin=Math.round(mid + (z/R)*mid);
      if(bin>=0&&bin<B) hist[bin]++;
    }
  }

  const fraction = n>0 ? (count/n) : 0;
  const piish = fraction>0 ? (2*h)/fraction : NaN;

  nOut.textContent = n.toLocaleString();
  fracOut.textContent = fraction ? fraction.toFixed(5) : '0';
  piOut.textContent = Number.isFinite(piish) ? piish.toFixed(5) : '—';

  drawHist(hist,R,h);
}

function drawHist(hist,R,h){
  const w=canvas.clientWidth,H=canvas.clientHeight;
  const pad=14, innerW=w-pad*2, innerH=H-pad*2;

  ctx.clearRect(0,0,w,H);
  ctx.strokeStyle='#000'; ctx.lineWidth=1;
  ctx.strokeRect(pad,pad,innerW,innerH);

  const pixPerZ=innerW/(2*R), midX=pad+innerW/2;
  ctx.fillStyle='#ddd';
  ctx.fillRect(midX-h*pixPerZ,pad,2*h*pixPerZ,innerH);

  const maxCount=Math.max(1,...hist), binW=innerW/hist.length;
  ctx.strokeStyle='#000';
  for(let i=0;i<hist.length;i++){
    const x=pad+i*binW;
    const barH=(hist[i]/maxCount)*innerH;
    ctx.strokeRect(x,pad+innerH-barH,binW,barH);
  }

  ctx.setLineDash([4,4]); ctx.strokeStyle='#000';
  ctx.beginPath();
  ctx.moveTo(midX-h*pixPerZ,pad); ctx.lineTo(midX-h*pixPerZ,pad+innerH);
  ctx.moveTo(midX+h*pixPerZ,pad); ctx.lineTo(midX+h*pixPerZ,pad+innerH);
  ctx.stroke();
  ctx.setLineDash([]);
}

[nSlider,hSlider,rangeSlider,binsSlider].forEach(el=>el.addEventListener('input',simulateAndDraw));
simulateAndDraw();
</script>
{% endraw %}

To find out we need to go back to Gauss, to Cauchy, and to a curve first drawn in 1748 by Maria Gaetana Agnesi.


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

is the **Cauchy distribution**. The factor of π here is the same one that appeared in the slope experiment at the very beginning.  

Take the probability of landing near horizontal. For a small band of width $\varepsilon$ around zero,  

$$
\Pr(|Z|\le \tfrac{\varepsilon}{2}) \approx f(0)\,\varepsilon = \frac{\varepsilon}{\pi}.
$$  

So when you count ratios in a narrow strip and rescale by the strip’s width, the number that emerges is $1/\pi$. That is the constant hiding in the data.  

Why π? Because the angle $\theta=\arctan(Y/X)$ is uniform on an interval of length $\pi$. Each slice of angle of width $\varepsilon$ always occupies exactly $\varepsilon/\pi$ of that range. Push that uniform angle through the tangent map, and the same fraction shows up in the density of slopes.  

The surprise is that this law does not behave like Gauss’s bell curve.  

- **No mean.** Averages swing and never settle.  
- **No variance.** The tails are too heavy for second moments to exist.  
- **Stability.** The sum of Cauchy variables is again Cauchy — echoing the Gaussian’s stability but without the comfort of convergence.  
- **Failure of the central limit theorem.** Gauss believed that averages always approach the truth. Cauchy’s law proves otherwise: more data does not guarantee certainty.  

Later developments linked the Cauchy to the wider family of $t$-distributions. In 1908 William Sealy Gosset introduced the $t$ law while working at Guinness. With one degree of freedom, the $t$ reduces exactly to the Cauchy. Among all $t$ distributions, it is the simplest — and the only one without an average.  

So the appearance of π in a random ratio is not a curiosity. It marks the boundary between two worlds: the Gaussian world where errors are tame and averages converge, and the Cauchy world where symmetry and geometry reign but certainty never arrives.  
