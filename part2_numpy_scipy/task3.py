import numpy as np

A = np.array([
    [4.0, -1.5, 2.0, 0.5],
    [1.0, 5.0, -2.0, 1.2],
    [-2.0, 1.0, 6.0, -1.0],
    [0.5, 2.0, -1.0, 7.0]
])

B = np.array([11.05, -6.82, 11.5, -0.5])

det_A = np.linalg.det(A)
cond_A = np.linalg.cond(A)

print(f"det(A) = {det_A:.4f}")
if np.isclose(det_A, 0.0):
    print("Матрица вырождена: det(A) = 0. Система не имеет единственного решения.")
    exit(1)

print(f"Число обусловленности cond(A) = {cond_A:.4f}")

A_inv = np.linalg.inv(A)
X_inv = A_inv @ B

X_solve = np.linalg.solve(A, B)

diff_norm = np.linalg.norm(X_inv - X_solve)
residual_norm = np.linalg.norm(A @ X_solve - B)

print(f"Норма разности решений ||X_inv - X_solve|| = {diff_norm:.2e}")
print(f"Проверка подстановкой (норма невязки) ||A*X - B|| = {residual_norm:.2e}")

X_rounded = np.round(X_solve, 1)
print(f"Решение системы: {X_rounded}")