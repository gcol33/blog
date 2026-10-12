import numpy as np

import style

N = 10_000
P1 = 1 - (5 / 6) ** 4
P2 = 1 - (35 / 36) ** 24

rng = np.random.default_rng(1654)
win1 = (rng.integers(1, 7, size=(N, 4)) == 6).any(axis=1)
win2 = ((rng.integers(1, 7, size=(N, 24)) == 6) & (rng.integers(1, 7, size=(N, 24)) == 6)).any(axis=1)
rounds = np.arange(1, N + 1)
rate1 = np.cumsum(win1) / rounds
rate2 = np.cumsum(win2) / rounds

fig, ax = style.figure(3.4)
ax.axhline(P1, color=style.MID, linewidth=0.8)
ax.axhline(P2, color=style.MID, linewidth=0.8)
ax.plot(rounds, rate1, color=style.BLACK)
ax.plot(rounds, rate2, color=style.BLACK, linestyle=(0, (5, 3)))
ax.set_xscale("log")
ax.set_xlim(10, N)
ax.set_ylim(0.25, 0.65)
ax.set_yticks([0.3, 0.4, 0.5, 0.6], ["30%", "40%", "50%", "60%"])
ax.set_xticks([10, 100, 1000, 10000], ["10", "100", "1,000", "10,000"])
ax.tick_params(labelsize=12)
ax.set_xlabel("rounds played", fontsize=12)
ax.set_ylabel("win rate so far", fontsize=12)
ax.text(N, 0.585, f"one die, 4 rolls: {100 * P1:.2f}%", ha="right", va="center", fontsize=12)
ax.text(N, 0.43, f"two dice, 24 rolls: {100 * P2:.2f}%", ha="right", va="center", fontsize=12)
style.save(fig, "de-mere-dice-win-rate")

print(f"final: {100 * rate1[-1]:.2f}% {100 * rate2[-1]:.2f}%")
for n in (10, 100, 1000):
    print(n, f"{100 * rate1[n - 1]:.1f}% {100 * rate2[n - 1]:.1f}%")
