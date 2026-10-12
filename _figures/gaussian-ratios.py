import numpy as np

import style

rng = np.random.default_rng(20250920)
N = 1_000_000
z = rng.standard_normal(N) / rng.standard_normal(N)

R = 4.0
H_BAND = 0.1

fig, ax = style.figure(2.8)
bins = np.linspace(-R, R, 81)
width = bins[1] - bins[0]
counts, _ = np.histogram(z, bins=bins)
ax.axvspan(-H_BAND, H_BAND, color=style.LIGHT, linewidth=0)
ax.bar(bins[:-1], counts / (N * width), width=width, align="edge",
       fill=False, edgecolor=style.MID, linewidth=0.6)
grid = np.linspace(-R, R, 801)
ax.plot(grid, 1 / (np.pi * (1 + grid**2)), color=style.BLACK)
ax.axhline(1 / np.pi, color=style.BLACK, linewidth=0.8, linestyle=(0, (4, 3)))
ax.text(R, 1 / np.pi + 0.008, r"$1/\pi$", ha="right", va="bottom")
ax.set_xlim(-R, R)
ax.set_ylim(0, 0.36)
ax.set_xlabel(r"slope $Z = Y/X$")
ax.set_ylabel("density")
ax.tick_params(axis="y", pad=7)
style.save(fig, "gaussian-ratios-histogram")

fig, (left, right) = style.figure(3.0, ncols=2, sharey=True)

hs = np.logspace(-3, 0, 40)
absz = np.sort(np.abs(z))
frac = np.searchsorted(absz, hs, side="right") / N
left.plot(hs, np.pi * hs / np.arctan(hs), color=style.MID)
left.plot(hs, 2 * hs / frac, "o", color=style.BLACK, markersize=3)
left.set_xscale("log")
left.set_xlabel(r"band half-width $h$")
left.set_ylabel(r"$2h \,/\,$fraction in band")
left.text(0.04, 0.95, r"$n = 10^6$", transform=left.transAxes, va="top")

H_RUN = 0.01
inside = np.cumsum(np.abs(z) <= H_RUN)
ns = np.unique(np.logspace(3, 6, 300).astype(int))
right.plot(ns, 2 * H_RUN * ns / inside[ns - 1], color=style.BLACK, linewidth=1)
right.set_xscale("log")
right.set_xlabel(r"samples $n$")
right.text(0.96, 0.95, r"$h = 0.01$", transform=right.transAxes, va="top", ha="right")

for a in (left, right):
    a.axhline(np.pi, color=style.BLACK, linewidth=0.8, linestyle=(0, (4, 3)))
left.set_ylim(2.6, 4.2)
left.set_yticks([2.75, np.pi, 3.5, 4.0], ["2.75", r"$\pi$", "3.50", "4.00"])
style.save(fig, "gaussian-ratios-estimate")
