import numpy as np
from matplotlib.patches import FancyBboxPatch

import style

M = 1_000_000
ROUNDS = 10

H = 2.7
fig, ax = style.canvas(H)

BOX_W, BOX_H = 1.45, 0.62
XS = (0.9, 2.7, 4.5, 6.3)
OUTCOMES = ("up", "down", "up")


def box(x, y, top, bottom, alive):
    ax.add_patch(FancyBboxPatch((x - BOX_W / 2, y - BOX_H / 2), BOX_W, BOX_H,
                                boxstyle="square,pad=0", linewidth=1.0,
                                facecolor=style.WHITE if alive else style.PALE,
                                edgecolor=style.BLACK if alive else style.MID))
    colour = style.BLACK if alive else style.DARK
    ax.text(x, y + 0.13, top, ha="center", va="center", fontsize=12, color=colour)
    ax.text(x, y - 0.15, bottom, ha="center", va="center", fontsize=12, color=colour)


ax.text(XS[0], H - 0.25, "start", ha="center", va="center", fontsize=12, color=style.DARK)
for r, outcome in enumerate(OUTCOMES, start=1):
    ax.text(XS[r], H - 0.25, f"round {r}: {outcome}", ha="center", va="center",
            fontsize=12, color=style.DARK)

y_alive = 1.55
box(XS[0], y_alive, "everyone", f"{M:,}", True)
for r, outcome in enumerate(OUTCOMES, start=1):
    n = M // 2 ** r
    wrong = "down" if outcome == "up" else "up"
    y_next, y_dead = (y_alive + 0.0, 0.55)
    x0, x1 = XS[r - 1] + BOX_W / 2, XS[r] - BOX_W / 2
    ax.plot([x0, x1], [y_alive, y_next], color=style.BLACK, linewidth=1.2)
    ax.plot([x0, x1], [y_alive, y_dead], color=style.MID, linewidth=1.0)
    box(XS[r], y_next, f'told "{outcome}"', f"{n:,}", True)
    box(XS[r], y_dead, f'told "{wrong}"', f"{n:,}", False)

style.save(fig, "the-prophet-filter-split")

rounds = np.arange(ROUNDS + 1)
survivors = M / 2.0 ** rounds

fig, ax = style.figure(3.2)
ax.tick_params(labelsize=12)
ax.xaxis.label.set_size(12)
ax.yaxis.label.set_size(12)
ax.semilogy(rounds, survivors, color=style.BLACK, marker="o", markersize=4.5)
ax.set_xlim(-0.4, ROUNDS + 0.4)
ax.set_ylim(400, 2.5e6)
ax.set_xticks(rounds)
ax.set_yticks([1e3, 1e4, 1e5, 1e6])
ax.set_yticklabels(["1,000", "10,000", "100,000", "1,000,000"])
ax.minorticks_off()
ax.set_xlabel("correct predictions seen")
ax.set_ylabel("recipients remaining")
for k in (0, 5, ROUNDS):
    ax.annotate(f"{M // 2 ** k:,}", (k, survivors[k]), textcoords="offset points",
                xytext=(8, 4) if k < ROUNDS else (-8, -16),
                ha="left" if k < ROUNDS else "right", fontsize=12)

style.save(fig, "the-prophet-filter-survivors")
