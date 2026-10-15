import os
import matplotlib.pyplot as plt
import numpy as np

# Set random seed
np.random.seed(42)

# 1. Theoretical density parameters
C = 1 / 21
num_samples = 15000

# 2. Inverse transform sampling: X = (63*U + 1)^(1/3)
u = np.random.uniform(0, 1, num_samples)
samples = (63 * u + 1) ** (1 / 3)

# 3. Discretize into bins to get empirical PDF
num_bins = 25
counts, bin_edges = np.histogram(samples, bins=num_bins, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# 4. Dense grid for theoretical curve
x_curve = np.linspace(1, 4, 400)
pdf_curve = C * (x_curve**2)

# 5. Plotting
plt.figure(figsize=(9, 5))

# Stem plot for sampled distribution
markerline, stemlines, baseline = plt.stem(
    bin_centers,
    counts,
    linefmt="b-",
    markerfmt="bo",
    basefmt="k-",
    label="Sampled Empirical PDF (Stem)",
)
plt.setp(stemlines, linewidth=1.5, alpha=0.7)
plt.setp(markerline, markersize=5)

# Theoretical curve
plt.plot(
    x_curve,
    pdf_curve,
    color="red",
    linewidth=2.5,
    label=r"Theoretical PDF: $P(x) = \frac{1}{21}x^2$",
)

plt.title(r"Sampled vs. Theoretical PDF for $P(x) = \frac{1}{21}x^2$", fontsize=13)
plt.xlabel("$x$", fontsize=11)
plt.ylabel("Probability Density", fontsize=11)
plt.xlim(0.8, 4.2)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()


filename = "stem_plot.pdf"
plt.savefig(filename)
plt.close()

os.system(f"termux-open {filename}")

