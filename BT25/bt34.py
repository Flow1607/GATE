import os
import matplotlib.pyplot as plt
import numpy as np

#Coefficient matrix 
A = np.array([[2.0, 3.0], [4.0, 6.0]])
r_A = np.linalg.matrix_rank(A)

print("--- Coefficient Matrix Analysis ---")
print("Matrix A:")
print(A)

#row reduction 
A_echelon = A.copy()
A_echelon[1] = A_echelon[1] - 2 * A_echelon[0]

print("\nRow Echelon Form of A (R2 -> R2 - 2*R1):")
print(A_echelon)
print(f"Rank(A) = {r_A}")

# Input parameter k and generating augmented matrix 
print("\n--- Augmented Matrix Analysis ---")
k = float(input("Enter value for k: "))

b = np.array([[6.0], [3.0 * k]])
aug = np.block([A, b])   #block for matrix

print("\nAugmented Matrix [A | b]:")
print(aug)

# Perform R2 -> R2 - 2*R1 on the augmented matrix
aug_echelon = aug.copy()
aug_echelon[1] = aug_echelon[1] - 2 * aug_echelon[0]

print("\nRow Echelon Form of [A | b]:")
print(aug_echelon) #printing echelon matrix

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

#Plot both lines
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
else:
    plt.plot(
        x, y2, "r-", linewidth=1.5, label=f"$4x + 6y = 3({k:.1f})$ (Parallel)"
    )
    plt.title(f"Parallel Lines: No Solution ($k = {k}$)")

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

# Launch file viewer
os.system(f"termux-open {save_path}")

