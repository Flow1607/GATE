import numpy as np
import matplotlib.pyplot as plt

# 1. Define g(x) = x^3 + x^2 + 1 using NumPy's polynomial module
# Coefficients in descending order: 1*x^3 + 1*x^2 + 0*x + 1
g = np.poly1d([1, 1, 0, 1])
dg = np.polyder(g)

x0 = 1.0
g_val = g(x0)      # g(1) = 3.0
dg_val = dg(x0)    # g'(1) = 5.0

# 2. Formulate the linear system:
# Continuity:      a * x0 + b = g(x0)  -->  [x0,  1] @ [a, b]^T = g(x0)
# Differentiability: a = g'(x0)        -->  [ 1,  0] @ [a, b]^T = g'(x0)
A = np.array([
    [x0, 1.0],
    [1.0, 0.0]
])
B = np.array([g_val, dg_val])

# Solve for a and b via matrix inversion / LU decomposition
a, b = np.linalg.solve(A, B)

print(f"a = {a:.1f}")
print(f"b = {b:.1f}")

# 3. Generate domains and plot
x_left = np.linspace(-2, 1, 300)
x_right = np.linspace(1, 2.5, 300)

y_left = a * x_left + b
y_right = g(x_right)

plt.figure(figsize=(8, 5))
plt.plot(x_left, y_left, 'b-', linewidth=2, label=rf'$f(x) = {a:.0f}x - {abs(b):.0f} \quad (x < 1)$')
plt.plot(x_right, y_right, 'r-', linewidth=2, label=r'$f(x) = x^3 + x^2 + 1 \quad (x \geq 1)$')
plt.plot(x0, g_val, 'ko', markersize=6, label=f'Transition point ({x0:.0f}, {g_val:.0f})')

plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.title(rf'Piecewise Differentiable Function ($a = {a:.1f},\ b = {b:.1f}$)', fontsize=12)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

