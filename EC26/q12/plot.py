import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# -------------------------------------------------------------
# 1. Built-in Gradient Computation with SymPy
# -------------------------------------------------------------
x, y, z = sp.symbols("x y z", real=True)
f = 2 * x**2 - y**2 - z**2

# sp.derive_by_array is SymPy's built-in multi-variable gradient function
grad_sym = sp.derive_by_array(f, (x, y, z))

# Evaluation at P = (1, 0, sqrt(2))
point = {x: 1, y: 0, z: sp.sqrt(2)}
grad_val = np.array([float(g.subs(point)) for g in grad_sym], dtype=float)

# Unit normal vector
unit_normal = grad_val / np.linalg.norm(grad_val)

print(f"Implicit surface: {f} = 0")
print(f"Symbolic gradient: {grad_sym}")
print(f"Gradient at P: {grad_val}")
print(f"Unit normal vector: {unit_normal}")

# -------------------------------------------------------------
# 2. Parametric Surface Generation (y^2 + z^2 = 2x^2)
# -------------------------------------------------------------
# Parameterizing the circular cone along the x-axis avoids NaN boundary artifacts
x_range = np.linspace(0, 1.6, 60)
theta = np.linspace(0, 2 * np.pi, 80)
X, Theta = np.meshgrid(x_range, theta)

Y = np.sqrt(2) * X * np.cos(Theta)
Z = np.sqrt(2) * X * np.sin(Theta)

# Point P coordinates
p_x, p_y, p_z = 1.0, 0.0, np.sqrt(2)

# -------------------------------------------------------------
# 3. 3D Plotting
# -------------------------------------------------------------
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

# Plot cone surface
surf = ax.plot_surface(
    X, Y, Z, cmap="coolwarm", alpha=0.65, edgecolor="none", rstride=2, cstride=2
)

# Plot point P
ax.scatter([p_x], [p_y], [p_z], color="black", s=50, label=r"$P(1, 0, \sqrt{2})$")

# Plot normal vector at P
arrow_scale = 0.8
ax.quiver(
    p_x,
    p_y,
    p_z,
    unit_normal[0],
    unit_normal[1],
    unit_normal[2],
    length=arrow_scale,
    color="darkred",
    linewidth=2.5,
    arrow_length_ratio=0.25,
    label=r"Unit Normal $\vec{n}$",
)

# Plot tangent plane at P for visual confirmation of orthogonality
plane_grid = np.linspace(-0.5, 0.5, 10)
U, V = np.meshgrid(plane_grid, plane_grid)
# Tangent plane equation: 4*(x - 1) + 0*(y - 0) - 2*sqrt(2)*(z - sqrt(2)) = 0
# => z = sqrt(2) + sqrt(2)*(x - 1)
X_tan = p_x + U
Y_tan = p_y + V
Z_tan = p_z + np.sqrt(2) * U
ax.plot_wireframe(
    X_tan,
    Y_tan,
    Z_tan,
    color="gray",
    alpha=0.35,
    linewidth=0.8,
    label="Tangent Plane",
)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(r"Surface $z^2 = 2x^2 - y^2$ and Normal Vector at $P$")
ax.legend(loc="upper left")
ax.view_init(elev=22, azim=-55)

# -------------------------------------------------------------
# 4. Save and Launch in Termux
# -------------------------------------------------------------
output_file = "surface_normal.png"
plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.close()

# termux-open passes the file intent to the Android system image viewer
try:
    subprocess.run(["termux-open", output_file], check=True)
except FileNotFoundError:
    # Fallback to standard xdg-open if executed outside Android Termux
    os.system(f"xdg-open {output_file} 2>/dev/null")

