import numpy as np
from matplotlib.patches import Circle

import style

HOUSE = {"p": (0, 0), "q": (1.6, 0), "r": (1.6, 1.6), "s": (0, 1.6), "t": (0.8, 2.5)}
HX, HY = (style.WIDTH - 1.6) / 2, 0.25
fig, ax = style.canvas(3.0)
for e in ("pq", "qr", "rs", "sp", "pr", "qs", "st", "tr"):
    (x1, y1), (x2, y2) = HOUSE[e[0]], HOUSE[e[1]]
    ax.plot([HX + x1, HX + x2], [HY + y1, HY + y2], color=style.BLACK, linewidth=2.0,
            solid_capstyle="round")
for x, y in HOUSE.values():
    ax.add_patch(Circle((HX + x, HY + y), 0.06, facecolor=style.BLACK,
                        edgecolor="none", zorder=3))
style.save(fig, "the-map-always-knows-house")

H = 3.1
fig, ax = style.canvas(H)

NODES = {"a": (0, 0), "b": (3, 0), "c": (2, 2 * np.sqrt(3)), "d": (5, 2 * np.sqrt(3))}
EDGES = ("ab", "cd", "ac", "bd", "ad", "bc")
LABELS = {"ab": "3", "cd": "3", "ac": "4", "bd": "4", "ad": r"$\sqrt{37}$", "bc": r"$\sqrt{13}$"}
MATCHINGS = (("ab", "cd"), ("ac", "bd"), ("ad", "bc"))
ALONG = {"ad": 0.72, "bc": 0.25}
NODE_OFFSET = {"a": (0, -0.2), "b": (0, -0.2), "c": (0, 0.2), "d": (0, 0.2)}

SCALE = 0.4
PANEL = style.WIDTH / 3
Y0 = 1.05
NODE_R = 0.06


def dist(e):
    return np.hypot(*np.subtract(NODES[e[0]], NODES[e[1]]))


def panel(x0, pair):
    def at(k):
        x, y = NODES[k]
        return x0 + SCALE * x, Y0 + SCALE * y

    for e in EDGES:
        (x1, y1), (x2, y2) = at(e[0]), at(e[1])
        on = e in pair
        ax.plot([x1, x2], [y1, y2], color=style.BLACK if on else style.LIGHT,
                linewidth=2.6 if on else 1.0, solid_capstyle="round", zorder=2 if on else 1)
        if on:
            nx, ny = -(y2 - y1), x2 - x1
            n = np.hypot(nx, ny)
            side = -1 if e in ("ab", "bd") else 1
            t = ALONG.get(e, 0.5)
            k = 0.24 if e in ALONG else 0.17
            ax.text(x1 + t * (x2 - x1) + side * k * nx / n, y1 + t * (y2 - y1) + side * k * ny / n,
                    LABELS[e], ha="center", va="center", fontsize=12)
    for k in NODES:
        x, y = at(k)
        ax.add_patch(Circle((x, y), NODE_R, facecolor=style.BLACK, edgecolor="none", zorder=3))
        dx, dy = NODE_OFFSET[k]
        ax.text(x + dx, y + dy, k, ha="center", va="center", fontsize=12, fontweight="bold")

    extra = sum(dist(e) for e in pair)
    cx = x0 + SCALE * 2.5
    ax.text(cx, 0.52, f"extra {extra:.2f}", ha="center", va="center", fontsize=12)
    ax.text(cx, 0.22, f"total {42 + extra:.2f}", ha="center", va="center", fontsize=12)


for i, pair in enumerate(MATCHINGS):
    panel(i * PANEL + (PANEL - SCALE * 5) / 2, pair)

style.save(fig, "the-map-always-knows-matchings")
