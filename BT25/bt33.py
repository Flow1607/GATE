import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 500)
y = e**x -2

plt.figure(figsize=(7, 5))
plt.plot(x, y, "b-", linewidth=2, label=r"$f(x) = e^x -2")

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.title(r"Plot of $f(x) = e^x - 2 $")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
save_path = "/sdcard/DCIM/bt33_plot.png"
plt.savefig(save_path, dpi=300)
print(f"Saved plot to: {save_path}")
plt.close()
