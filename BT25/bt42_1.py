import os
import numpy as np
import matplotlib.pyplot as plt

# Parameters from question
tau = 40.0  # time constant 
target = 0.95  # 95% steady state

# t = -tau * ln(0.05)
t_val = -tau * np.log(1.0 - target)
ans = round(t_val)

print("Thermometer equation: y(t) = y_ss * (1 - e^(-t / 40))")
print(f"Time to reach 95%: {t_val:.2f} s")
print(f"Rounded answer: {ans} s -> Option (C)\n")

# Step response curve
t = np.linspace(0, 200, 500)
y = 1.0 - np.exp(-t / tau)

plt.figure(figsize=(7, 4.5))
plt.plot(t, y, label=r"$y(t) = 1 - e^{-t/40}$", color="tab:blue")
plt.axvline(t_val, color="red", linestyle="--", alpha=0.6)
plt.axhline(target, color="red", linestyle="--", alpha=0.6)
plt.scatter([t_val], [target], color="red", zorder=4)

plt.text(t_val + 4, target - 0.06, f"t = {ans}s (95%)", color="red", fontsize=10)
plt.title("Thermometer First-Order Step Response")
plt.xlabel("Time (s)")
plt.ylabel(r"$y(t) / y_{ss}$")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower right")

pdf_path = "thermometer_response.pdf"
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

# Opening in Termux
os.system(f"termux-open {pdf_path}")

