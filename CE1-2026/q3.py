import shutil
import subprocess
import matplotlib

# Non-interactive backend for Termux / headless environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# 1. Print Radical Axis to console
print("Radical Axis: 2x + 2y + 1 = 0")

# 2. Define domain and functions
x = np.linspace(-3.5, 2.5, 500)
y1 = x**2
y2 = -x**2 - 2 * x - 1
y_radical = -x - 0.5  # 2x + 2y + 1 = 0  =>  y = -x - 1/2

# 3. Create plot
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y1, label=r"$y = x^2$", color="#1f77b4", linewidth=2)
ax.plot(x, y2, label=r"$y = -x^2 - 2x - 1$", color="#d62728", linewidth=2)
ax.plot(
    x,
    y_radical,
    label=r"Radical Axis: $2x + 2y + 1 = 0$",
    color="#2ca02c",
    linewidth=2,
    linestyle="--",
)

# Mark vertices
ax.plot(0, 0, "bo", markersize=5)
ax.plot(-1, 0, "ro", markersize=5)

# Plot formatting
ax.axhline(0, color="black", linewidth=0.8, linestyle=":")
ax.axvline(0, color="black", linewidth=0.8, linestyle=":")
ax.set_xlim(-3.5, 2.5)
ax.set_ylim(-6, 6)
ax.set_title("Plot of Curves & Radical Axis", fontsize=13, fontweight="bold")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="lower right", framealpha=0.9)

plt.tight_layout()

# 4. Save as PDF and open in Termux
output_pdf = "curves_plot.pdf"
plt.savefig(output_pdf, format="pdf")
print(f"File saved as {output_pdf}")

if shutil.which("termux-open"):
    subprocess.run(["termux-open", output_pdf])

