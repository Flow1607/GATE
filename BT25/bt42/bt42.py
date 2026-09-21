import os
import shlex
import shutil
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# System parameters
tau = 40.0  # Time constant in seconds
t_95 = tau * np.log(20.0)  # Exact time to reach 95% steady state (approx 119.83 s)
y_95 = 0.95

# Continuous simulation data (Standard plot)
t_cont = np.linspace(0, 200, 500)
y_cont = 1.0 - np.exp(-t_cont / tau)

# Discrete sampled data (Stem plot)
t_stem = np.arange(0, 201, 10)
y_stem = 1.0 - np.exp(-t_stem / tau)

# Create 1x2 subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# --- Subplot 1: Continuous Standard Plot ---
ax1.plot(t_cont, y_cont, "b-", lw=2, label=r"$y(t) = 1 - e^{-t/40}$")
ax1.axhline(0.95, color="gray", linestyle="--", lw=1, label="95% Steady-State")
ax1.axvline(t_95, color="gray", linestyle="--", lw=1)

# Highlight and label 95% point
ax1.plot(t_95, y_95, "ro", markersize=6, label=f"95% at $t \\approx {round(t_95)}$ s")
ax1.annotate(
    f"({round(t_95)}, 0.95)",
    xy=(t_95, y_95),
    xytext=(-10, 10),
    textcoords="offset points",
    ha="right",
    color="red",
    fontweight="semibold",
)

ax1.set_title("Continuous Response (Standard Plot)")
ax1.set_xlabel("Time $t$ (seconds)")
ax1.set_ylabel(r"Normalized Reading $y(t)/y_{\mathrm{ss}}$")
ax1.set_ylim(-0.05, 1.05)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="lower right")

# --- Subplot 2: Discrete Stem Plot ---
markerline, stemlines, baseline = ax2.stem(
    t_stem, y_stem, linefmt="b-", markerfmt="bo", basefmt="k-"
)
plt.setp(stemlines, "linewidth", 1.2)
plt.setp(markerline, "markersize", 4)

ax2.axhline(0.95, color="gray", linestyle="--", lw=1, label="95% Steady-State")
ax2.axvline(t_95, color="gray", linestyle="--", lw=1)

# Highlight and label 95% point
ax2.plot(t_95, y_95, "ro", markersize=6, label=f"95% at $t \\approx {round(t_95)}$ s")
ax2.annotate(
    f"({round(t_95)}, 0.95)",
    xy=(t_95, y_95),
    xytext=(-10, 10),
    textcoords="offset points",
    ha="right",
    color="red",
    fontweight="semibold",
)

ax2.set_title("Sampled Response (Stem Plot)")
ax2.set_xlabel("Time $t$ (seconds)")
ax2.set_ylabel(r"Normalized Reading $y(t)/y_{\mathrm{ss}}$")
ax2.set_ylim(-0.05, 1.05)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="lower right")

plt.tight_layout()

# Save as vector PDF
output_pdf = "thermometer_response.pdf"
plt.savefig(output_pdf, bbox_inches="tight")
plt.close()
print(f"Saved plot to: {output_pdf}")

# Open viewer
viewer = "xdg-open" if shutil.which("xdg-open") else "termux-open"
if shutil.which(viewer):
    subprocess.run(shlex.split(f"{viewer} {output_pdf}"))
#to open in either termux or ubuntu

