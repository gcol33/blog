"""Shared style for the static blog figures.

Every figure script imports this module, draws with matplotlib, and calls
`save(fig, name)`. Output goes to assets/figures/<name>.svg with text
converted to paths, so the SVG renders identically without the font.

The double border is drawn by CSS around the image (see
assets/css/11-figures.css); figures themselves carry no outer frame.
"""

from pathlib import Path

import matplotlib

matplotlib.use("svg")

import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "figures"

WIDTH = 7.2  # inches; 720 px at the 100 px/inch SVG scale below

BLACK = "#000"
DARK = "#555"
MID = "#999"
LIGHT = "#ccc"
PALE = "#eee"
WHITE = "#fff"

for ttf in (HERE / "fonts").glob("*.ttf"):
    font_manager.fontManager.addfont(str(ttf))

plt.rcParams.update({
    "font.family": "Cousine",
    "font.size": 13,
    "mathtext.fontset": "cm",
    "svg.fonttype": "path",
    "svg.hashsalt": "null-hypothesis-accepted",
    "figure.dpi": 100,
    "savefig.dpi": 100,
    "figure.facecolor": WHITE,
    "axes.facecolor": WHITE,
    "savefig.facecolor": WHITE,
    "text.color": BLACK,
    "axes.edgecolor": BLACK,
    "axes.labelcolor": BLACK,
    "axes.linewidth": 0.8,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelsize": 13,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.prop_cycle": matplotlib.cycler(color=[BLACK, DARK, MID]),
    "xtick.color": BLACK,
    "ytick.color": BLACK,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "lines.linewidth": 1.4,
    "patch.edgecolor": BLACK,
    "patch.linewidth": 0.8,
    "hatch.color": BLACK,
    "hatch.linewidth": 0.6,
    "legend.frameon": False,
    "legend.fontsize": 12,
    "figure.constrained_layout.use": True,
    "figure.constrained_layout.h_pad": 0.12,
    "figure.constrained_layout.w_pad": 0.12,
})


def figure(height, ncols=1, nrows=1, **kwargs):
    """Full-width figure of the given height (inches) with a grid of axes."""
    return plt.subplots(nrows, ncols, figsize=(WIDTH, height), **kwargs)


def canvas(height):
    """Full-width figure with one axes in data units = inches, no frame.

    For diagrams: (0, 0) is the bottom-left corner, (WIDTH, height) the
    top-right, so shapes and text are placed at exact positions.
    """
    fig = plt.figure(figsize=(WIDTH, height), layout="none")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def save(fig, name):
    """Write assets/figures/<name>.svg deterministically and close the figure."""
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.svg"
    fig.savefig(path, format="svg", metadata={"Date": None, "Creator": None})
    plt.close(fig)
    print(f"wrote {path.relative_to(HERE.parent)}")
    return path
