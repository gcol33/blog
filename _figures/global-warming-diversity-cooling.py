import numpy as np

import matplotlib.pyplot as plt

import style

rng = np.random.default_rng(7)
p = rng.uniform(80, 120, 10)
p /= p.sum()


def entropy(p):
    return -np.sum(p * np.log(p))


def remove_rarest(p):
    i = np.argmin(p)
    lost = p[i]
    p = np.delete(p, i)
    p[np.argmax(p)] += 0.7 * lost
    p += 0.3 * lost / len(p)
    return p / p.sum()


stages = [p]
while len(stages[-1]) > 2:
    stages.append(remove_rarest(stages[-1]))
richness = np.array([len(s) for s in stages])
H = np.array([entropy(s) for s in stages])

for s, h in zip(richness, H):
    print(f"S={s:2d}  H={h:.3f}  e^H={np.exp(h):.2f}  max p={stages[10 - s].max():.3f}")

fig = style.figure(5.0)[0]
fig.clear()
grid = fig.add_gridspec(2, 4, height_ratios=(1, 1.25))

shown = (10, 7, 4, 2)
tops = [fig.add_subplot(grid[0, k]) for k in range(4)]
for ax, s in zip(tops, shown):
    q = np.sort(stages[10 - s])[::-1]
    ax.bar(np.arange(10)[:s], q, width=0.75, facecolor=style.LIGHT, edgecolor=style.BLACK)
    ax.set_xlim(-0.7, 9.7)
    ax.set_ylim(0, 0.9)
    ax.set_xticks([])
    ax.set_yticks([0, 0.4, 0.8])
    ax.set_title(f"{s} species", fontweight="normal")
    if ax is tops[0]:
        ax.set_ylabel("share $p_i$")
    else:
        ax.set_yticklabels([])

ax = fig.add_subplot(grid[1, :])
ax.plot(richness, np.log(richness), color=style.MID, linestyle="--", linewidth=1.2)
ax.plot(richness, H, color=style.BLACK, marker="o", markersize=5)
ax.text(1.75, 2.12, r"$\log S$, all species equal", ha="right",
        va="bottom", color=style.DARK)
ax.text(4.25, 1.02, "rarest species removed", ha="right", va="top")
ax.set_xlim(10.3, 1.7)
ax.set_xticks(range(10, 1, -1))
ax.set_ylim(0, 2.5)
ax.set_xlabel("species remaining $S$")
ax.set_ylabel("entropy $H$")

style.save(fig, "global-warming-diversity-cooling-collapse")
