import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-8, 8, 2000)
y = 4 / (x**2 - 4)

mask_discontinuity = (np.abs(x - 2) < 0.04) | (np.abs(x + 2) < 0.04)
y[mask_discontinuity] = np.nan

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(x, y, label=r"$y(x) = \frac{4}{x^2 - 4}$", color="navy", linewidth=2)

ax.axvline(x=-2, color="crimson", linestyle="--", linewidth=1.5, label="Асимптоты $x = \pm 2$")
ax.axvline(x=2, color="crimson", linestyle="--", linewidth=1.5)

ax.axhline(y=0, color="gray", linestyle=":", linewidth=1)

ax.set_xlim(-8, 8)
ax.set_ylim(-10, 10)

ax.set_title("График функции с разрывами и асимптотами", fontsize=13)
ax.set_xlabel("x", fontsize=11)
ax.set_ylabel("y", fontsize=11)
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend(loc="upper right", fontsize=10)

plt.tight_layout()
plt.show()