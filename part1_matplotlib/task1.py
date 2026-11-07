import matplotlib.pyplot as plt
import numpy as np

x_deg = np.linspace(-360, 360, 1000)
x_rad = np.deg2rad(x_deg)
p_x = np.exp(np.sin(x_rad)) + np.log(np.sin(0.5 * x_rad) ** 2 + 1) * np.cos(x_rad)
q_x = -np.log((np.sin(x_rad) - np.cos(x_rad)) ** 2 + 2) + 8

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax1.plot(x_deg, p_x, label=r"$p(x) = e^{\sin x} + \ln(\sin^2(0.5x) + 1) \cdot \cos x$", color="royalblue", linewidth=1.8)
ax1.set_title("График функции p(x)", fontsize=13)
ax1.set_ylabel("p(x)", fontsize=11)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right", fontsize=10)

ax2.plot(x_deg, q_x, label=r"$q(x) = -\ln((\sin x - \cos x)^2 + 2) + 8$", color="crimson", linewidth=1.8)
ax2.set_title("График функции q(x)", fontsize=13)
ax2.set_xlabel("x (градусы)", fontsize=11)
ax2.set_ylabel("q(x)", fontsize=11)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right", fontsize=10)
ticks = np.arange(-360, 361, 90)
ax2.set_xticks(ticks)
ax2.set_xticklabels([f"{deg}°" for deg in ticks])
ax2.set_xlim(-360, 360)

plt.tight_layout()
plt.show()