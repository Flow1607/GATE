import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Guide clause detailing the behavior for values of k
print("=" * 55)
print("             System of Equations Guide")
print("  Equations: x + ky = 1  and  kx + y = -1")
print("=" * 55)
print("  • Enter k = 1          -> No Solution (Parallel)")
print("  • Enter k = -1         -> Infinite Solutions (Coincident)")
print("  • Enter k != 1, -1     -> Unique Solution (e.g., 0, 2, 3)")
print("=" * 55)

# 1. Input parameter k
k = float(input("Enter value of k: "))

# 2. Form coefficient matrix A and augmented matrix [A|b] using np.block
# Equations: x + ky = 1, kx + y = -1
A = np.array([[1.0, k], [k, 1.0]])
b = np.array([[1.0], [-1.0]])  # Column vector (shape: 2x1)

aug = np.block([A, b])  # Horizontal concatenation (shape: 2x3)

# 3. Generate Row Echelon Form (Elementary row operation: R2 -> R2 - k*R1)
factor = aug[1, 0] / aug[0, 0]  # Evaluates to k / 1.0 = k

A_ech = A.copy()
A_ech[1] -= factor * A_ech[0]

aug_ech = aug.copy()
aug_ech[1] -= factor * aug_ech[0]

# Clean up near-zero values due to floating-point rounding
A_ech[np.isclose(A_ech, 0.0)] = 0.0
aug_ech[np.isclose(aug_ech, 0.0)] = 0.0

# 4. Display original and row echelon matrices
print("\n--- Original Matrices ---")
print(f"Coefficient Matrix A:\n{A}")
print(f"\nAugmented Matrix [A|b]:\n{aug}")

print("\n--- Row Echelon Form (after R2 -> R2 - k*R1) ---")
print(f"Echelon Form of A:\n{A_ech}")
print(f"\nEchelon Form of [A|b]:\n{aug_ech}")

# 5. Determine ranks from the non-zero rows of the echelon form
rank_A = int(np.sum(np.any(~np.isclose(A_ech, 0.0), axis=1)))
rank_aug = int(np.sum(np.any(~np.isclose(aug_ech, 0.0), axis=1)))

print(f"\nRank(A)     = {rank_A}")
print(f"Rank([A|b]) = {rank_aug}")

# 6. Check consistency using Rouché–Capelli Theorem
sol_type = ""
sol_point = None

if rank_A == rank_aug == 2:
    sol_type = "Unique Solution"
    sol_point = np.linalg.solve(A, b).flatten()
    print(f"\nCondition: Rank(A) = Rank([A|b]) = 2")
    print(f"Result: {sol_type}")
    print(f"Solution: x = {sol_point[0]:.4f}, y = {sol_point[1]:.4f}")

elif rank_A < rank_aug:
    sol_type = "No Solution (Parallel / Inconsistent)"
    print(f"\nCondition: Rank(A) < Rank([A|b]) ({rank_A} != {rank_aug})")
    print(f"Result: {sol_type}")

elif rank_A == rank_aug < 2:
    sol_type = "Infinite Solutions (Coincident Lines)"
    print(f"\nCondition: Rank(A) = Rank([A|b]) = 1 < 2")
    print(f"Result: {sol_type}")

# 7. Plotting the lines
fig, ax = plt.subplots(figsize=(8, 6))

if sol_point is not None:
    cx, cy = sol_point
    x_vals = np.linspace(cx - 5, cx + 5, 400)
else:
    x_vals = np.linspace(-5, 5, 400)

# Line 1: x + k*y = 1
if np.isclose(k, 0.0):
    ax.axvline(x=1.0, color="blue", linewidth=2, label=r"$x + ky = 1$ ($x = 1$)")
else:
    y1_vals = (1.0 - x_vals) / k
    ax.plot(x_vals, y1_vals, color="blue", linewidth=2, label=r"$x + ky = 1$")

# Line 2: k*x + y = -1
y2_vals = -1.0 - k * x_vals
if np.isclose(k, -1.0):
    ax.plot(
        x_vals,
        y2_vals,
        color="red",
        linestyle="--",
        linewidth=2.5,
        label=r"$kx + y = -1$ (Coincident)",
    )
else:
    ax.plot(x_vals, y2_vals, color="red", linewidth=2, label=r"$kx + y = -1$")

# Highlight unique intersection point if it exists
if sol_point is not None:
    ax.scatter(
        [sol_point[0]],
        [sol_point[1]],
        color="black",
        s=60,
        zorder=5,
        label=f"Intersection ({sol_point[0]:.2f}, {sol_point[1]:.2f})",
    )

ax.axhline(0, color="black", linewidth=0.8, linestyle=":")
ax.axvline(0, color="black", linewidth=0.8, linestyle=":")
ax.set_title(f"System of Equations for k = {k}\nStatus: {sol_type}", fontsize=12)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend(loc="best")

if sol_point is not None:
    ax.set_ylim(cy - 5, cy + 5)
else:
    ax.set_ylim(-6, 6)

# 8. Save figure and display in Termux
output_filename = "system_plot.pdf"
plt.savefig(output_filename, dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"\nPlot saved to: {output_filename}")

try:
    subprocess.run(["termux-open", output_filename], check=True)
    print("Opening plot with termux-open...")
except FileNotFoundError:
    print(
        "Note: 'termux-open' command not found. If running outside Termux, open the image manually."
    )

