import numpy as np

import matplotlib.pyplot as plt

import style

n = np.arange(1, 17)
fig, ax = style.figure(4.0)
for k, colour in ((10, style.MID), (26, style.DARK), (62, style.BLACK)):
    ax.plot(n, float(k) ** n, color=colour)
    ax.plot(n, k * n, color=colour, linestyle=(0, (4, 3)))
    ax.text(n[-1] + 0.3, float(k) ** n[-1], f"k = {k}", va="center")
ax.text(8.6, 1e17, "without leak: $k^n$", ha="right")
ax.text(8.5, 1e5, "with leak: $kn$", ha="center")
ax.set_yscale("log")
ax.set_xlim(1, 19.2)
ax.set_ylim(1, 1e30)
ax.set_xticks([1, 4, 8, 12, 16])
ax.set_yticks([1e0, 1e10, 1e20, 1e30])
ax.spines["bottom"].set_bounds(1, 16)
ax.set_xlabel("secret length n")
ax.set_ylabel("attempts needed")
style.save(fig, "leaky-locks-collapse")

phrase = "open the safe"
pairs = [f"{a}{b}".replace(" ", "_") for a, b in zip(phrase, phrase[1:])]
rng = np.random.default_rng(1943)
geometry = rng.lognormal(0.0, 0.35, len(pairs))
typists = (("typist A", 135.0), ("typist B", 185.0))
x = np.arange(len(pairs))

fig, axes = style.figure(4.8, nrows=2, sharex=True, sharey=True)
for ax, (name, base) in zip(axes, typists):
    habit = rng.lognormal(0.0, 0.35, len(pairs))
    profile = base * geometry * habit
    for rep in range(3):
        ax.plot(x, profile * rng.lognormal(0.0, 0.07, len(pairs)),
                color=style.BLACK, linewidth=0.9, marker="o", markersize=3)
    ax.set_title(name, loc="left", fontweight="normal")
    ax.set_ylabel("interval (ms)")
axes[1].set_xticks(x, pairs)
axes[1].set_xlabel("consecutive key pair (_ = space)")
axes[0].set_ylim(0, None)
style.save(fig, "leaky-locks-rhythm")
