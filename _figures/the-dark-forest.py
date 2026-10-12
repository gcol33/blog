import numpy as np
from matplotlib.ticker import FixedLocator, NullLocator

import style

V = 1
ROUNDS = 100


def threshold(C):
    return V / (V + C)


fig, ax = style.figure(3.6)
C = np.logspace(0, 3, 400)
pstar = 100 * threshold(C)
ax.fill_between(C, 0.05, pstar, color=style.PALE, linewidth=0)
ax.plot(C, pstar, color=style.BLACK)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1, 1000)
ax.set_ylim(0.05, 100)
ax.xaxis.set_major_locator(FixedLocator([1, 2, 10, 100, 1000]))
ax.xaxis.set_minor_locator(NullLocator())
ax.set_xticklabels(["1", "2", "10", "100", "1000"])
ax.yaxis.set_major_locator(FixedLocator([0.1, 1, 5, 20, 100]))
ax.yaxis.set_minor_locator(NullLocator())
ax.set_yticklabels(["0.1%", "1%", "5%", "20%", "100%"])
ax.set_xlabel(r"extinction cost $C$ (with $V$ = 1)")
ax.set_ylabel(r"hostility probability $p$")
ax.text(1.6, 0.25, "signal", fontsize=12)
ax.text(1.6, 45, "stay silent", fontsize=12)
for c, p, label in ((100, 5, "p = 5%"), (2, 5, "p = 5%"), (2, 20, "p = 20%")):
    ax.plot([c], [p], "o", color=style.BLACK, markersize=5)
    ax.text(c * 1.12, p * 0.8, label, fontsize=12, va="top", ha="left")
ax.text(300, 100 * threshold(300) * 1.5, r"$p = V/(V+C)$", fontsize=13, ha="left")
style.save(fig, "the-dark-forest-threshold")


def play(rng, p, C, repeated):
    signal = p < threshold(C)
    hostile = None
    score, path, extinct = 0, [0], []
    for t in range(1, ROUNDS + 1):
        if not repeated or hostile is None:
            hostile = rng.random() < p
        if signal:
            if hostile:
                score -= C
                extinct.append(t)
                hostile = None
            else:
                score += V
        path.append(score)
    return np.array(path), extinct


rng = np.random.default_rng(1950)
runs = {
    "silent": play(rng, 0.05, 100, False),
    "low": play(rng, 0.05, 2, False),
    "oneshot": play(rng, 0.20, 2, False),
    "repeated": play(rng, 0.20, 2, True),
}
fig, (a, b) = style.figure(3.4, ncols=2, sharey=True)
t = np.arange(ROUNDS + 1)


def line(ax, key, label, dy=0):
    path, ext = runs[key]
    ax.plot(t, path, color=style.BLACK)
    if ext:
        ax.plot(ext, path[ext], "o", markersize=3.5, markerfacecolor=style.WHITE,
                markeredgecolor=style.BLACK, markeredgewidth=0.9)
    ax.text(ROUNDS - 2, path[-1] + dy, label, fontsize=12, ha="right", va="bottom")


line(a, "silent", "C = 100", 3)
line(a, "low", "C = 2", 3)
a.set_title("p = 5%, new civilization each round", fontweight="normal", fontsize=12)
line(b, "oneshot", "new civilization each round", 3)
line(b, "repeated", "same civilization", 3)
b.set_title("p = 20%, C = 2", fontweight="normal", fontsize=12)
for ax in (a, b):
    ax.set_xlim(0, ROUNDS)
    ax.set_xlabel("round")
    ax.axhline(0, color=style.LIGHT, linewidth=0.8, zorder=0)
a.set_ylabel("cumulative score")
a.set_ylim(-8, 112)
style.save(fig, "the-dark-forest-rounds")
