from matplotlib.patches import Circle, FancyArrowPatch

import style

H = 4.8
fig, ax = style.canvas(H)

FACE_R = 0.24
PARITY_R = 0.38
LEFT_X = 0.9     # first die column
STEP = 0.66      # spacing between die faces
RIGHT_X = (5.1, 6.3)
ARROW = (2.95, 4.55)


def disc(x, y, r, label, shaded):
    ax.add_patch(Circle((x, y), r, facecolor=style.LIGHT if shaded else style.WHITE,
                        edgecolor=style.BLACK, linewidth=1.2))
    ax.text(x, y, label, ha="center", va="center", fontsize=11)


def row(y0, title, face_note, parity_note, arrow_label, forward):
    ax.text(0.2, y0 + 1.1, title, fontsize=11, fontweight="bold", va="center")
    for i, face in enumerate(range(1, 7)):
        x = LEFT_X + STEP * (i % 3)
        y = y0 + 0.5 - 0.92 * (i // 3)
        disc(x, y, FACE_R, str(face), face % 2 == 0)
        ax.text(x, y - FACE_R - 0.15, face_note(face), fontsize=10,
                ha="center", va="center", color=style.DARK)
    for x, name, shaded in ((RIGHT_X[0], "odd", False), (RIGHT_X[1], "even", True)):
        disc(x, y0, PARITY_R, name, shaded)
        ax.text(x, y0 - PARITY_R - 0.2, parity_note(name), fontsize=10,
                ha="center", va="center", color=style.DARK)
    start, end = (ARROW[0], ARROW[1]) if forward else (ARROW[1], ARROW[0])
    ax.add_patch(FancyArrowPatch((start, y0), (end, y0), arrowstyle="-|>",
                                 mutation_scale=14, color=style.BLACK, linewidth=1.2))
    ax.text(sum(ARROW) / 2, y0 + 0.2, arrow_label, ha="center", va="bottom", fontsize=11)


row(3.5, "Pushforward of the measure",
    face_note=lambda face: "1/6",
    parity_note=lambda name: r"$f_*\mu$ = 1/2",
    arrow_label=r"$f$: face $\to$ parity",
    forward=True)

ax.plot([0.2, style.WIDTH - 0.2], [2.5, 2.5], color=style.LIGHT, linewidth=0.8)

row(1.05, "Pullback of the function",
    face_note=lambda face: str(int(face % 2 == 0)),
    parity_note=lambda name: rf"$g$ = {int(name == 'even')}",
    arrow_label=r"$f^*g = g \circ f$",
    forward=False)

style.save(fig, "pushforwards-pullbacks-transport")
