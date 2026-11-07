import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("img", exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 8))

ground = patches.Rectangle((-10, -10), 20, 4, color="#557a46")
building_main = patches.Rectangle((-6, -6), 5, 8, color="#7d8597")
building_small = patches.Rectangle((2, -6), 4, 6, color="#a9b4c2")
door = patches.Rectangle((-4.5, -6), 2, 3, color="#5c3d2e")

roof = patches.Polygon([[-6.5, 2], [-3.5, 5], [-0.5, 2]], color="#b84a39")

sun = patches.Circle((6, 6), 1.6, color="#f4a261")
attic_window = patches.Circle((-3.5, 3), 0.6, color="#e0e1dd")

cloud1 = patches.Ellipse((0, 6.5), 3.5, 1.4, color="#dce1e3")
cloud2 = patches.Ellipse((1.5, 7), 2.5, 1.2, color="#edf2f4")

door_arch = patches.Arc((-3.5, -3), 2, 1.5, angle=0, theta1=0, theta2=180, 
                        color="#f1faee", linewidth=2.5)

all_patches = [
    ground, building_main, building_small, door, 
    roof, sun, attic_window, cloud1, cloud2, door_arch
]
for p in all_patches:
    ax.add_patch(p)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect("equal")
ax.set_facecolor("#cfe8ef")
ax.set_title("Городской пейзаж из геометрических примитивов", fontsize=13)
ax.axis("off")

plt.savefig("img/task3.png", dpi=300, bbox_inches="tight")
plt.tight_layout()
plt.show()