import os
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# Non-interactive backend to avoid GUI display errors in terminal environments
matplotlib.use("Agg")

# Defining 3D object
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

# Plane 1: x1 + x2 + x3 = 0  -->  x3 = -x1 - x2
x1_grid = np.linspace(-3, 3, 30)
x2_grid = np.linspace(-3, 3, 30)
X1, X2 = np.meshgrid(x1_grid, x2_grid)
X3_1 = -X1 - X2

# Plane 2: x1 + 2*x3 = 0  -->  x1 = -2*x3 
x3_grid = np.linspace(-3, 3, 30)
X2_2, X3_2 = np.meshgrid(x2_grid, x3_grid)
X1_2 = -2 * X3_2

# Rendering both planes
ax.plot_surface(X1, X2, X3_1, alpha=0.35, color="royalblue")
ax.plot_surface(X1_2, X2_2, X3_2, alpha=0.35, color="orange")

# Intersection line: x = k * [2, -1, -1]^T
k = np.linspace(-1.5, 1.5, 100)
x_line = 2 * k
y_line = -1 * k
z_line = -1 * k

(line,) = ax.plot(
    x_line,
    y_line,
    z_line,
    color="red",
    linewidth=3,
    label=r"Line: $\mathbf{x} = k [2, -1, -1]^\top$",
)
origin = ax.scatter(
    [0], [0], [0], color="black", s=50, label="Origin $(0, 0, 0)$"
)

# Setting Different Patch Colours 
patch1 = mpatches.Patch(
    color="royalblue", alpha=0.5, label=r"Plane 1: $x_1 + x_2 + x_3 = 0$"
)
patch2 = mpatches.Patch(
    color="orange", alpha=0.5, label=r"Plane 2: $x_1 + 2x_3 = 0$"
)

# Axis configuration & viewpoint
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$x_3$")
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.view_init(elev=25, azim=45)
ax.legend(handles=[patch1, patch2, line, origin], loc="upper right")
plt.title(r"Intersection of Planes $x_1 + x_2 + x_3 = 0$ and $x_1 + 2x_3 = 0$")

# Save high-resolution PNG
output_file = "planes_and_line.pdf"
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.close(fig)

# Launch native Android viewer through Termux
os.system(f"termux-open {output_file}")

