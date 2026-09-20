#Must be run inside matgeo/codes/CoordGeo/ along with funcs.py from line/funcs.py and params.py in CoordGeo/
#Dated 10-09-2026
#By Jaideep 

import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Coefficient matrix analysis
A = np.array([[2.0, 3.0], [4.0, 6.0]])
r_A = np.linalg.matrix_rank(A)

print("--- Coefficient Matrix Analysis ---")
print("Matrix A:")
print(A)

# Manual row reduction for display: R2 -> R2 - 2*R1
A_echelon = A.copy()
A_echelon[1] = A_echelon[1] - 2 * A_echelon[0]

print("\nRow Echelon Form of A (R2 -> R2 - 2*R1):")
print(A_echelon)
print(f"Rank(A) = {r_A}")

# 2. Input parameter k and construct augmented matrix with np.block
print("\n--- Augmented Matrix Analysis ---")
k = float(input("Enter value for k: "))

b = np.array([[6.0], [3.0 * k]])
aug = np.block([A, b])

print("\nAugmented Matrix [A | b]:")
print(aug)

# Perform R2 -> R2 - 2*R1 on the augmented matrix
aug_echelon = aug.copy()
aug_echelon[1] = aug_echelon[1] - 2 * aug_echelon[0]

print("\nRow Echelon Form of [A | b]:")
print(aug_echelon)

r_aug = np.linalg.matrix_rank(aug)
print(f"\nRank(A) = {r_A}")
print(f"Rank([A | b]) = {r_aug}")

if r_aug > r_A:
    print(f"\nResult for k = {k}: Inconsistent! Rank(A) < Rank([A | b]).")
    print(
        f"Row 2 indicates 0x + 0y = {aug_echelon[1, 2]:.2f} (Contradiction: No Solution)."
    )
else:
    print(f"\nResult for k = {k}: Consistent! Rank(A) == Rank([A | b]) == 1 < n.")
    print("Row 2 is entirely zeros (Infinitely Many Solutions).")


# 3. Labeling points implementation from funcs.py
def label_pts(G_v, vert_labels):
    for i, txt in enumerate(vert_labels):
        plt.annotate(
            txt,
            (G_v[0, i], G_v[1, i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )


# 4. Plot both lines and annotate key coordinate points
x = np.linspace(-5, 5, 400)
y1 = (6.0 - 2.0 * x) / 3.0
y2 = (3.0 * k - 4.0 * x) / 6.0

plt.figure(figsize=(7, 5))
plt.plot(x, y1, "b-", linewidth=2.5, label=r"$2x + 3y = 6$")

if np.isclose(k, 4.0):
    plt.plot(
        x, y2, "r--", linewidth=1.5, label=f"$4x + 6y = 3({k:.1f})$ (Coincident)"
    )
    plt.title(f"Coincident Lines: Infinite Solutions ($k = {k}$)")

    # Construct coordinate matrix: Row 0 -> x-coords, Row 1 -> y-coords
    pts = np.array([[3.0, 0.0], [0.0, 2.0]])
    labels = ["A(3, 0)", "B(0, 2)"]
    plt.scatter(pts[0, :], pts[1, :], color="red", zorder=5)
    label_pts(pts, labels)
else:
    plt.plot(
        x, y2, "r-", linewidth=1.5, label=f"$4x + 6y = 3({k:.1f})$ (Parallel)"
    )
    plt.title(f"Parallel Lines: No Solution ($k = {k}$)")

    # Intercepts for both lines: Line 1 (A, B) and Line 2 (C, D)
    pts = np.array(
        [[3.0, 0.0, 3.0 * k / 4.0, 0.0], [0.0, 2.0, 0.0, 3.0 * k / 6.0]]
    )
    labels = ["A(3, 0)", "B(0, 2)", f"C({3*k/4:.2g}, 0)", f"D(0, {k/2:.2g})"]
    plt.scatter(pts[0, :], pts[1, :], color="red", zorder=5)
    label_pts(pts, labels)

plt.axhline(0, color="k", lw=0.8)
plt.axvline(0, color="k", lw=0.8)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

save_path = "bt34_plot.pdf"
plt.savefig(save_path, bbox_inches="tight")
plt.close()
print(f"\nPlot saved to: {save_path}")

