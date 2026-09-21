import os
import numpy as np
import matplotlib.pyplot as plt

# Solved constants: a = 0, b = 2  =>  a + b = 2 (Option C)
a = 0.0
b = 2.0
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b} -> Option (C)\n")

# Domain ranges
x_left = np.linspace(-2, 0, 200)
x_right = np.linspace(0, 3, 300)
x_tangent = np.linspace(-2, 2, 400)

# Function definitions
y_left = a + b * x_left          # 2x
y_right = np.sin(2 * x_right)    # sin(2x)
y_tangent = 2 * x_tangent        # Tangent line: y = 2x

# Plotting
plt.figure(figsize=(7, 4.5))

# Different curves plotted for x<0 and x>0curves
plt.plot(x_left, y_left, color="tab:blue", lw=2.2, label=r"$f(x) = 2x$ ($x \leq 0$)" )
plt.plot(x_right, y_right, color="tab:blue", lw=2.2, label=r"$f(x) = \sin(2x) \quad (x > 0)$")

# Tangent line at x = 0 
plt.plot(x_tangent, y_tangent, color="crimson", linestyle="--", lw=1.5, label="Tangent: $y = 2x$")

# Mark origin
plt.scatter([0], [0], color="black", zorder=5)
plt.annotate("(0, 0)", (0, 0), textcoords="offset points", xytext=(8, -14), fontsize=10)

plt.axhline(0, color="gray", lw=0.8, alpha=0.5)
plt.axvline(0, color="gray", lw=0.8, alpha=0.5)

plt.title("Differentiable Piecewise Function at $x=0$")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.xlim(-2, 3)
plt.ylim(-2.5, 2.5)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

pdf_path = "piecewise_tangent_plot.pdf"
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

# Open in Termux
os.system(f"termux-open {pdf_path}")

