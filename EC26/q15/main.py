import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Parameter Definitions & Sample Computation
Fs = 40  # Sampling frequency in Hz
Ts = 1 / Fs  # Sampling period: 0.025 s
N = 10  # First 10 samples (n = 0 to 9)

n = np.arange(N)
t_samples = n * Ts

# Discrete sample values
x1_samples = np.cos(20 * np.pi * t_samples)
x2_samples = np.cos(100 * np.pi * t_samples)

# Print comparison table to terminal
print(f"{'Sample (n)':<12}{'Time t (s)':<14}{'x1[n]':<12}{'x2[n]':<12}{'Equal?'}")
print("-" * 55)
for i in range(N):
    is_eq = np.isclose(x1_samples[i], x2_samples[i])
    print(
        f"{i:<12}{t_samples[i]:<14.4f}{x1_samples[i]:<12.4f}{x2_samples[i]:<12.4f}{is_eq}"
    )

# 2. Option Verification
opt_A = np.all(x1_samples[:3] > x2_samples[:3])
opt_B = np.all(x1_samples[-3:] > x2_samples[-3:])
opt_C = np.all(x2_samples > x1_samples)
opt_D = np.all(np.isclose(x1_samples[3:7], x2_samples[3:7]))

print("\n--- Option Check ---")
print(f"Option (A) [First 3: x1 > x2]: {opt_A}")
print(f"Option (B) [Last 3: x1 > x2]:  {opt_B}")
print(f"Option (C) [All: x2 > x1]:     {opt_C}")
print(f"Option (D) [4th to 7th: x1 == x2]: {opt_D}")
print(f"--> Correct Answer: {'(D)' if opt_D else 'Check manually'}")

# 3. Plotting
t_dense = np.linspace(0, (N - 1) * Ts, 1000)
x1_dense = np.cos(20 * np.pi * t_dense)
x2_dense = np.cos(100 * np.pi * t_dense)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

# Continuous waveforms
ax1.plot(
    t_dense,
    x1_dense,
    label=r"$x_1(t) = \cos(20\pi t)$ (10 Hz)",
    color="tab:blue",
    linewidth=2,
)
ax1.plot(
    t_dense,
    x2_dense,
    label=r"$x_2(t) = \cos(100\pi t)$ (50 Hz)",
    color="tab:orange",
    alpha=0.65,
    linestyle="--",
    linewidth=1.2,
)
ax1.set_ylabel("Amplitude")
ax1.set_title(r"Continuous Signals vs. Aliased Sampling at $F_s = 40\text{ Hz}$")
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(loc="upper right")

# Discrete stems showing identical sample values
markerline1, stemlines1, _ = ax2.stem(
    t_samples,
    x1_samples,
    linefmt="C0-",
    markerfmt="C0o",
    basefmt="k-",
    label=r"Samples $x_1[n]$",
)
markerline2, stemlines2, _ = ax2.stem(
    t_samples,
    x2_samples,
    linefmt="C3--",
    markerfmt="rx",
    basefmt="k-",
    label=r"Samples $x_2[n]$",
)
plt.setp(markerline1, markersize=9, fillstyle="none", markeredgewidth=2)
plt.setp(markerline2, markersize=8, markeredgewidth=2)

# Highlight samples 4 to 7
ax2.axvspan(
    3 * Ts - 0.005,
    6 * Ts + 0.005,
    color="lightgreen",
    alpha=0.25,
    label="Samples 4 to 7 (Option D)",
)

ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Sample Value")
ax2.set_xticks(t_samples)
ax2.set_xticklabels([f"n={i}\n{t_samples[i]:.3f}s" for i in range(N)], fontsize=8)
ax2.set_title("Discrete Samples $x_1[n]$ and $x_2[n]$ (Identical Values)")
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(loc="upper right")

plt.tight_layout()

# 4. Save and Open via termux-open
output_file = "sampling_aliasing_q15.pdf"
plt.savefig(output_file, dpi=300)
plt.close()

os.system(f"termux-open {output_file}")

