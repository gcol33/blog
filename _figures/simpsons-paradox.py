from matplotlib.patches import FancyArrowPatch

import style

RATE = {
    ("mild", "drug"): 81 / 87,
    ("mild", "control"): 234 / 270,
    ("severe", "drug"): 192 / 263,
    ("severe", "control"): 55 / 80,
}

SCENARIOS = [
    ("Equal allocation", {"drug": (175, 175), "control": (175, 175)}),
    ("Drug mostly severe", {"drug": (87, 263), "control": (270, 80)}),
    ("Drug mostly mild", {"drug": (270, 80), "control": (87, 263)}),
]


def rates(alloc):
    out = {}
    for arm, (n_mild, n_severe) in alloc.items():
        rec = n_mild * RATE["mild", arm] + n_severe * RATE["severe", arm]
        out[arm] = [100 * RATE["mild", arm], 100 * RATE["severe", arm],
                    100 * rec / (n_mild + n_severe)]
    return out


fig, axes = style.figure(3.4, ncols=3, sharey=True)
X = [0, 1.55, 3.2]

for ax, (title, alloc) in zip(axes, SCENARIOS):
    r = rates(alloc)
    ax.axvline(2.4, color=style.LIGHT, linewidth=0.8)
    for x, d, c in zip(X, r["drug"], r["control"]):
        ax.plot([x, x], [d, c], color=style.MID, linewidth=1.0, zorder=1)
        ax.plot(x, d, "o", color=style.BLACK, markersize=7, zorder=2)
        ax.plot(x, c, "o", markerfacecolor=style.WHITE, markeredgecolor=style.BLACK,
                markeredgewidth=1.2, markersize=7, zorder=2)
        ax.text(x - 0.2, d, f"{d:.0f}", ha="right", va="center", fontsize=12)
        ax.text(x + 0.2, c, f"{c:.0f}", ha="left", va="center", fontsize=12,
                color=style.DARK)
    ax.set_title(title, fontsize=12)
    ax.tick_params(labelsize=12)
    ax.set_xticks(X, ["Mild", "Severe", "All"])
    ax.set_xlim(-0.95, 3.85)
    ax.tick_params(axis="x", length=0)

axes[0].set_ylim(64, 97)
axes[0].set_ylabel("recovered (%)", fontsize=12)
axes[0].text(0.2, 100 * RATE["mild", "drug"] + 2.2, "drug", ha="center", fontsize=12)
axes[0].text(0.2, 100 * RATE["mild", "control"] - 3.2, "control", ha="center",
             fontsize=12, color=style.DARK)

style.save(fig, "simpsons-paradox-allocation")


fig, ax = style.canvas(1.8)
NODES = {"Severity": (3.6, 1.5), "Treatment": (1.6, 0.3), "Recovery": (5.6, 0.3)}
for name, (x, y) in NODES.items():
    ax.text(x, y, name, ha="center", va="center", fontsize=14, fontweight="bold")
for start, end in (((3.15, 1.35), (1.85, 0.5)), ((4.05, 1.35), (5.35, 0.5)),
                   ((2.35, 0.3), (4.85, 0.3))):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14,
                                 color=style.BLACK, linewidth=1.2))

style.save(fig, "simpsons-paradox-confounding")
