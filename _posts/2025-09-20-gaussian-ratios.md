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
      <input type="range" id="nSlider" min="1000" max="300000" step="1000" value="80000" />
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
      <input type="range" id="binsSlider" min="41" max="181" step="20" value="101" />
    </label>
    <label style="margin-left:auto;">Seed
      <input id="seedInput" type="text" value="demo" style="width:100px; padding:4px 6px; border:1px solid #000; background:#fff;">
    </label>
    <button id="reshuffleBtn" style="padding:6px 10px; border:1px solid #000; background:#fff;">Resample</button>
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
    Formula used here:  
    \[
      \pi_{\text{ish}} \;=\; \frac{\text{total width of the band}}{\text{fraction of slopes inside it}}
    \]  

    where total width = \(2h\) (from \(-h\) to \(+h\)).  
    Narrow the band. Increase the samples. The number drifts toward 3.14…  
    Why should slopes of random points conspire to reveal π?
  </p>
</div>

---

## How a Simple Curve Defied Gauss  

Gauss believed in certainty through numbers. His law of errors — the Gaussian bell curve — promised that mistakes in measurement were well-behaved. The assumptions were clear: errors came from many small independent causes, variance was finite, and averages converged to the truth. The law of large numbers guaranteed stability of the mean, the central limit theorem explained the bell shape, and the method of least squares rested securely on these foundations. With more data, you always approached certainty.  

Cauchy broke that faith. In 1853, before the Académie des Sciences in Paris, he presented a rival law of errors in which variance was infinite and averages refused to settle. Joseph Bienaymé rose to defend Gauss, warning that least squares collapsed without finite variance. But Cauchy insisted that mathematics itself admitted such laws, and that in their presence the Gaussian guarantees failed. With more data, you did not get closer to the truth. You only deepened the confusion.  

The curve he used was not obscure. It had been introduced a century earlier, in 1748, by Maria Gaetana Agnesi in her *Instituzioni Analitiche*. Agnesi was not thinking about probability at all. She worked in the **geometric–analytic tradition** of the 18th century, when curves were defined by geometric constructions and then explored with the new tools of calculus. This tradition served three purposes: it bridged the visual world of geometry with the symbolic power of analysis, it contributed to the encyclopedic catalog of named curves — cycloid, cissoid, lemniscate — and it gave students concrete, visual examples in an age when calculus was still new.  

Agnesi’s *Instituzioni* was written not in Latin but in Italian, aimed at students rather than savants, and designed to systematize analysis in a clear, accessible way. Within this project the *versiera* fit perfectly. It came from a simple construction: a circle, a fixed point on its diameter, a line rotating around it, and a point tracing where it cut an axis. The resulting curve was bounded, symmetric, and easy to draw. Its equation was  

$$
y=\frac{a^3}{x^2+a^2},
$$  

which for $a=1$ reduces to  

$$
y=\frac{1}{1+x^2}.
$$  

Its analytic elegance was undeniable: a rational function whose integral was the arctangent, tying it directly back to circle geometry. For Agnesi, it was an ideal teaching curve — geometry, algebra, and calculus all in one example. Later, through mistranslation, it would acquire the odd name “Witch of Agnesi.”  

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

Cauchy’s conclusion was devastating. Here was a legitimate law of errors with no mean and no variance. Averages wandered instead of converging. The method of least squares lost its justification. The central limit theorem did not apply. The Gaussian promise of certainty was not universal — it was only a special case.  

Only later did mathematicians discover a simpler route to the same law: take two independent Gaussians, divide one by the other, and Cauchy’s distribution reappears. That modern shortcut is where we turn next.  

---

### Geometry of the slope

The pair $(X,Y)$ is rotationally symmetric in the plane. There is no privileged direction: spin the cloud, and it looks the same. That symmetry forces the angle

$$
\theta = \arctan\!\left(\frac{Y}{X}\right)
$$

to be uniform on $(-\tfrac{\pi}{2}, \tfrac{\pi}{2})$. Every angle is equally likely.  

The ratio $Z=Y/X$ is the slope of the line from the origin to the point $(X,Y)$. The problem is nothing more than asking: what happens when a uniform angle is pushed through the tangent function?  

The answer is

$$
f(z) = \frac{1}{\pi(1+z^2)}.
$$

The $1+z^2$ comes from the geometry of tangent. The factor of $\pi$ comes from the length of the interval.  

That is why π appears in the density of the Cauchy distribution. Not from circles, but from uniformity of angle.

---

### A law without an average

This is the Cauchy distribution. It has no mean and no variance. Adding Cauchy variables produces another Cauchy. The central limit theorem does not apply.
