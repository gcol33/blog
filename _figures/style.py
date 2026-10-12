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
import numpy as np
from matplotlib import font_manager
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.collections import Collection, PathCollection
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.path import Path as MPath
from matplotlib.text import Annotation, Text
from matplotlib.transforms import Bbox

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


CLEARANCE = 2  # px of white space required between text and anything else


class OverlapError(RuntimeError):
    pass


def _label(artist):
    if isinstance(artist, Text):
        return f"text {artist.get_text()!r}"
    if isinstance(artist, Legend):
        return "legend"
    return f"{type(artist).__name__} {artist.get_label()!r}"


def _drawn_texts(canvas):
    """Draw the figure and return the Text artists that actually rendered.

    Tick labels outside the view limits exist as objects but are never
    drawn, so the list comes from the draw itself rather than findobj.
    """
    drawn = []
    draw = Text.draw

    def recording(self, renderer):
        if self.get_visible() and self.get_text().strip():
            drawn.append(self)
        return draw(self, renderer)

    Text.draw = recording
    try:
        canvas.draw()
    finally:
        Text.draw = draw
    return list({id(t): t for t in drawn}.values())


def _text_blocks(fig, texts, renderer):
    """Every rendered text item as (artist, display bbox).

    A legend counts as one block (handles and labels together), so its own
    entries are not checked against each other.
    """
    legends = [a for a in fig.findobj(Legend) if a.get_visible()]
    in_legend = {id(t) for lg in legends for t in lg.findobj(Text)}
    blocks = [(lg, lg.get_window_extent(renderer)) for lg in legends]
    blocks += [(t, t.get_window_extent(renderer)) for t in texts if id(t) not in in_legend]
    return blocks


def _marks(fig):
    """Data marks text must stay clear of: lines, patches, collections."""
    skip = set()
    for ax in fig.axes:
        skip.add(id(ax.patch))
        for axis in (ax.xaxis, ax.yaxis):
            skip.update(id(a) for a in axis.findobj())
        skip.update(id(s) for s in ax.spines.values())
    for lg in fig.findobj(Legend):
        skip.update(id(a) for a in lg.findobj())
    for a in fig.findobj(Annotation):
        if a.arrow_patch is not None:
            skip.add(id(a.arrow_patch))
    marks = []
    for a in fig.findobj(lambda a: isinstance(a, (Line2D, Patch, Collection))):
        if id(a) in skip or a is fig.patch or not a.get_visible():
            continue
        if a.axes is not None and not a.axes.get_visible():
            continue
        marks.append(a)
    return marks


def _pt_to_px(fig, points):
    return points * fig.dpi / 72


def _shapes(artist):
    """A mark as (display path, radius) pairs: radius 0 is a stroked outline,
    radius > 0 a set of markers of that radius centred on the vertices."""
    fig = artist.figure
    if isinstance(artist, Line2D):
        path = artist.get_transform().transform_path(artist.get_path())
        shapes = []
        if artist.get_linestyle() not in ("None", "none", "", " "):
            shapes.append((path, 0.0))
        if artist.get_marker() not in (None, "None", "none", "", " "):
            radius = _pt_to_px(fig, artist.get_markersize()) / 2
            shapes.append((MPath(path.vertices), radius))
        return shapes
    if isinstance(artist, Patch):
        return [(artist.get_transform().transform_path(artist.get_path()), 0.0)]
    if isinstance(artist, PathCollection):
        offsets = artist.get_offsets()
        if not len(offsets):
            return []
        points = artist.get_offset_transform().transform(offsets)
        sizes = artist.get_sizes()
        radius = _pt_to_px(fig, np.sqrt(sizes.max() if len(sizes) else 36)) / 2
        return [(MPath(points), radius)]
    transform = artist.get_transform()
    return [(transform.transform_path(p), 0.0) for p in artist.get_paths()]


def _hits(path, radius, bbox):
    if radius > 0:
        box = bbox.padded(radius)
        v = path.vertices
        return bool(((v[:, 0] >= box.x0) & (v[:, 0] <= box.x1)
                     & (v[:, 1] >= box.y0) & (v[:, 1] <= box.y1)).any())
    return any(MPath(poly).intersects_bbox(bbox, filled=False)
               for poly in path.to_polygons(closed_only=False))


def check_overlaps(fig):
    """Raise OverlapError if any text touches other text, a data mark, or
    the figure edge. Text may sit inside a closed shape but not cross it."""
    canvas = FigureCanvasAgg(fig)
    texts = _drawn_texts(canvas)
    renderer = canvas.get_renderer()
    blocks = _text_blocks(fig, texts, renderer)
    padded = [(a, b.padded(CLEARANCE)) for a, b in blocks]
    halves = [(a, b.padded(CLEARANCE / 2)) for a, b in blocks]
    problems = []

    edge = fig.bbox
    for a, b in blocks:
        if b.x0 < edge.x0 or b.y0 < edge.y0 or b.x1 > edge.x1 or b.y1 > edge.y1:
            problems.append(f"{_label(a)} is cut off by the figure edge")

    for i, (a, b) in enumerate(halves):
        for c, d in halves[i + 1:]:
            if b.overlaps(d):
                problems.append(f"{_label(a)} overlaps {_label(c)}")

    for mark in _marks(fig):
        shapes = _shapes(mark)
        clip = mark.get_clip_box() if mark.get_clip_on() else None
        for a, b in padded:
            if isinstance(a, Text) and a.get_bbox_patch() is mark:
                continue
            if clip is not None:
                b = Bbox.intersection(b, clip)
                if b is None:
                    continue
            if any(_hits(p, r, b) for p, r in shapes):
                problems.append(f"{_label(a)} overlaps {_label(mark)}")

    if problems:
        raise OverlapError("\n  ".join(["text overlaps in figure:", *problems]))


def save(fig, name):
    """Check text clearance, then write assets/figures/<name>.svg
    deterministically and close the figure."""
    try:
        check_overlaps(fig)
    except OverlapError as err:
        plt.close(fig)
        raise OverlapError(f"{name}: {err}") from None
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.svg"
    fig.savefig(path, format="svg", metadata={"Date": None, "Creator": None})
    plt.close(fig)
    print(f"wrote {path.relative_to(HERE.parent)}")
    return path
