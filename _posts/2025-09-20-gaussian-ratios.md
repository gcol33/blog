---
layout: post
title: "Why Dividing Two Random Numbers Reveals π"
date: 2025-09-20
categories: probability statistics
---

## Where more data doesn’t mean more certainty

In 1748 Maria Gaetana Agnesi published her *Instituzioni Analitiche*, a vast treatise on analysis written in Italian rather than Latin. Among its pages was a curve she called the *versiera*. Later, through mistranslation, it became the “Witch of Agnesi.” Its equation was

$$
y = \frac{1}{1+x^2}.
$$

For Agnesi it was geometry: a curve traced by a moving line, elegant and symmetric. Nothing about probability.  

In 1824 Siméon-Denis Poisson examined the same curve while studying errors in measurement. He noted something unusual: if data followed this law, the average would not behave as Laplace and Gauss expected. Variance diverged. Even the mean refused to converge.  

By 1853 the Académie des Sciences in Paris was the stage for a clash. Laplace’s Gaussian doctrine ruled: errors were bell-shaped, and certainty came from averaging. Augustin-Louis Cauchy stood against it. He argued that some errors were too erratic for averages to exist at all. To press his case, he revived Agnesi’s curve. Joseph Bienaymé protested that without variance least squares collapsed. Cauchy persisted. The curve became a distribution, and his challenge gave it a name: the Cauchy law.

---

### Ratios of Gaussians

The paradox appears in the simplest experiment. Take two independent standard Gaussians $X$ and $Y$, and form the ratio

$$
Z = \frac{Y}{X}.
$$

The histogram of $Z$ shows a sharp peak at zero and tails that decay too slowly to vanish.  

Average ten samples, and the result swings wildly. Increase to thousands or millions and it still swings. The mean does not converge.

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
