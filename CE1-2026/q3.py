import os
import shutil
import subprocess
import matplotlib

# Use a non-interactive backend suited for terminal environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-3, 2, 400)

# Define both functions
y1 = x**2
y2 = -x**2 - 2 * x - 1

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r"$y = x^2$", color="blue", linewidth=2)
plt.plot(x, y2, label=r"$y = -x^2 - 2x - 1$", color="red", linewidth=2)

plt.plot(0, 0, "bo", markersize=6, label="Vertex $(0, 0)$")
plt.plot(-1, 0, "ro", markersize=6, label="Vertex $(-1, 0)$")

plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title(
    "Plot of $y = x^2$ and $y = -x^2 - 2x - 1$\n(0 Intersection Points)",
    fontsize=12,
)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.ylim(-6, 6)
plt.xlim(-3, 2)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()

# Save image to disk
filename = "curves_plot.png"
plt.savefig(filename, dpi=300)
print(f"Plot successfully saved to {filename}")

# Launch directly in Android's default image viewer
if shutil.which("termux-open"):
    subprocess.run(["termux-open", filename])

