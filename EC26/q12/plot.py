import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# -------------------------------------------------------------
# 1. Gradient Computation with SymPy
# -------------------------------------------------------------
x, y, z = sp.symbols("x y z", real=True)
f = 2 * x**2 - y**2 - z**2

grad_sym = sp.derive_by_array(f, (x, y, z))
point = {x: 1, y: 0, z: sp.sqrt(2)}
grad_val = np.array([float(g.subs(point)) for g in grad_sym], dtype=float)

# Inward and outward unit normals
n_in = grad_val / np.linalg.norm(grad_val)
n_out = -n_in

p_x, p_y, p_z = 1.0, 0.0, np.sqrt(2)

# -------------------------------------------------------------
# 2. Surface Data
# -------------------------------------------------------------
x_vals = np.linspace(0, 1.6, 60)
theta = np.linspace(0, 2 * np.pi, 80)
X, Theta = np.meshgrid(x_vals, theta)
Y = np.sqrt(2) * X * np.cos(Theta)
Z = np.sqrt(2) * X * np.sin(Theta)

fig = plt.figure(figsize=(14, 6))

# -------------------------------------------------------------
# Subplot 1: True-Scale 3D View
# -------------------------------------------------------------
ax1 = fig.add_subplot(121, projection="3d")
ax1.plot_surface(
    X, Y, Z, cmap="coolwarm", alpha=0.55, edgecolor="none", rstride=2, cstride=2
)
ax1.scatter([p_x], [p_y], [p_z], color="black", s=40, label=r"$P(1, 0, \sqrt{2})$")

# Outward normal (pointing cleanly off the surface)
ax1.quiver(
    p_x,
    p_y,
    p_z,
    n_out[0],
    n_out[1],
    n_out[2],
    length=0.9,
    color="darkred",
    linewidth=3,
    arrow_length_ratio=0.25,
    label=r"Outward Normal $-\vec{n}$",
)

# Tangent Plane
plane_grid = np.linspace(-0.4, 0.4, 8)
U, V = np.meshgrid(plane_grid, plane_grid)
ax1.plot_wireframe(
    p_x + U,
    p_y + V,
    p_z + np.sqrt(2) * U,
    color="gray",
    alpha=0.45,
    linewidth=0.9,
    label="Tangent Plane",
)

ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")
ax1.set_title("3D View (True 1:1:1 Scale)")
ax1.legend(loc="upper left", fontsize=8)

# FIX: Set physical box proportions matching the data ranges (no axis stretching)
x_span = 1.6
y_span = 4.0
z_span = 4.0
ax1.set_box_aspect([x_span, y_span, z_span])
ax1.view_init(elev=16, azim=-80)

# -------------------------------------------------------------
# Subplot 2: Cross-Section Profile (y = 0 Plane)
# -------------------------------------------------------------
ax2 = fig.add_subplot(122)
xs = np.linspace(0, 1.6, 100)
zs_upper = np.sqrt(2) * xs
zs_lower = -np.sqrt(2) * xs

ax2.plot(xs, zs_upper, color="tab:blue", linewidth=2.5, label=r"Cone Surface ($z = \sqrt{2}x$)")
ax2.plot(xs, zs_lower, color="tab:blue", linestyle="--", alpha=0.5)
ax2.scatter([p_x], [p_z], color="black", s=60, zorder=5, label=r"$P(1, \sqrt{2})$")

# Plot tangent line
tan_xs = np.linspace(0.6, 1.4, 20)
tan_zs = p_z + np.sqrt(2) * (tan_xs - p_x)
ax2.plot(tan_xs, tan_zs, color="gray", linestyle=":", label="Tangent Line")

# Outward normal vector in 2D
scale = 0.6
ax2.annotate(
    "",
    xy=(p_x + scale * n_out[0], p_z + scale * n_out[2]),
    xytext=(p_x, p_z),
    arrowprops=dict(facecolor="darkred", edgecolor="darkred", width=2, headwidth=8),
)

# Mark the 90-degree angle
corner_size = 0.08
u_surf = np.array([-1, -np.sqrt(2)]) / np.sqrt(3)
u_norm = np.array([n_out[0], n_out[2]])
c1 = np.array([p_x, p_z]) + corner_size * u_surf
c2 = c1 + corner_size * u_norm
c3 = np.array([p_x, p_z]) + corner_size * u_norm
ax2.plot(
    [c1[0], c2[0], c3[0]],
    [c1[1], c2[1], c3[1]],
    color="darkred",
    linewidth=1.2,
)

ax2.set_aspect("equal", adjustable="box")
ax2.set_xlabel("X")
ax2.set_ylabel("Z")
ax2.set_title(r"Cross-Section at $y = 0$ (Slope Product $= -1$)")
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend(loc="upper left")

# -------------------------------------------------------------
# 3. Save and Open
# -------------------------------------------------------------
output_file = "surface_normal_fixed.png"
plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.close()

try:
    subprocess.run(["termux-open", output_file], check=True)
except FileNotFoundError:
    os.system(f"xdg-open {output_file} 2>/dev/null")

