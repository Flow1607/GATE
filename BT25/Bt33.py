import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 400)
r = float(np.log(2))

plt.plot(x, np.exp(x) - 2, "b", label=r"$f(x) = e^x - 2$")
plt.plot(r, 0, "ro", label=f"Root: {r:.4f}")
plt.text(r - 0.15, 0.8, f"({r:.4f}, 0)", color="red", ha="right")

plt.axhline(0, color="k", lw=1)
plt.axvline(0, color="k", lw=1)
plt.title(r"Plot of $f(x) = e^x - 2$")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.grid(True, ls="--", alpha=0.6)
plt.legend()

plt.savefig("bt33_plot.pdf", bbox_inches="tight")
print("Saved plot to bt33_plot.pdf")

