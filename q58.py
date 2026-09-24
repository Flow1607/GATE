#By Jaideep
# 23/09/26


import numpy as np
import sympy as sp

# Define LHS and RHS coefficient matrices using exact fractions
A_LHS = sp.Matrix( #LHS matrix
    [
        [6, 0, 0],  # C
        [0, 1, 0],  # N
        [12, 3, 0],  # H
        [6, 0, 2],  # O
    ]
)

A_RHS = sp.Matrix( #RHS matrix
    [
        [1, 1, 0],  # C
        [sp.Rational(1, 5), 0, 0],  # N (0.2)
        [sp.Rational(9, 5), 0, 2],  # H (1.8)
        [sp.Rational(1, 2), 2, 1],  # O (0.5)
    ]
)

#Construct stoichiometric matrix A = [A_LHS | -A_RHS]
A = A_LHS.row_join(-A_RHS)

print("--- System Stoichiometric Matrix A ---")
sp.pprint(A)

# Row Reduced Echelon Form (RREF)
rref_A, pivot_cols = A.rref()
rank = len(pivot_cols)
dof = A.shape[1] - rank

#checking rank and producing row reduced matrix
print(f"\nRank of A = {rank}")
print(f"Degrees of freedom (Nullity) = {dof}")
print("\nRow Reduced Echelon Form (RREF):") 
sp.pprint(rref_A)

#Nullspace basis vectors (spanning the complete solution space)
null_basis = A.nullspace()
print("\n--- Nullspace Basis Vectors ---")
for idx, v in enumerate(null_basis, 1):
    print(f"Basis Vector v_{idx}:")
    sp.pprint(v)

# Symbolic solution in terms of substrate (x1) and biomass (x4)
x1, x2, x3, x4, x5, x6 = sp.symbols("x1 x2 x3 x4 x5 x6")
eqs = [
    6 * x1 - (x4 + x5),
    x2 - sp.Rational(1, 5) * x4,
    12 * x1 + 3 * x2 - (sp.Rational(9, 5) * x4 + 2 * x6),
    6 * x1 + 2 * x3 - (sp.Rational(1, 2) * x4 + 2 * x5 + x6),
    x4- (sp.Rational(2,5)* (6 * x1)),
]

sol_terms = sp.solve(eqs, (x1,x2, x3, x5, x6)) #directly solves eqns listed as above

print("\n--- Parametric Solution in terms of (x1, x4) ---")
for var, expr in sol_terms.items():
    print(f"{var} = {expr}")

# Example Numerical Evaluation on a basis of 1 mole of glucose (x1 = 1)
print("\n--- Sample Numerical Values (Basis: x1 = 1 mole glucose, x4 = 2) ---")
subs_dict = {x4: 5.0} #iniializing x4 = 5.0
x_vals = {
    "x1": float(sol_terms[x1].subs(subs_dict)),
    "x2": float(sol_terms[x2].subs(subs_dict)),
    "x3": float(sol_terms[x3].subs(subs_dict)),
    "x4": subs_dict[x4],
    "x5": float(sol_terms[x5].subs(subs_dict)),
    "x6": float(sol_terms[x6].subs(subs_dict)),
}

for k, val in x_vals.items():
    print(f"{k} = {val:.4f}") #printing final ans
