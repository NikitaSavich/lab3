import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

f1 = lambda x: x * np.sin(x)
exact_1 = np.pi
res_1, _ = integrate.quad(f1, 0, np.pi)
err_1 = np.abs(res_1 - exact_1)

print("1. Однократный интеграл ∫[0, π] x * sin(x) dx:")
print(f"   SciPy quad: {res_1:.8f}")
print(f"   Точное:     {exact_1:.8f}")
print(f"   Погрешность: {err_1:.2e}\n")

f2 = lambda y, x: x + y
exact_2 = 0.5
res_2, _ = integrate.dblquad(f2, 0, 1, lambda x: 0, lambda x: x)
err_2 = np.abs(res_2 - exact_2)

print("2. Двойной интеграл ∬ (x + y) dy dx (0 <= y <= x <= 1):")
print(f"   SciPy dblquad: {res_2:.8f}")
print(f"   Точное:        {exact_2:.8f}")
print(f"   Погрешность:   {err_2:.2e}\n")

np.random.seed(42)
N_values = np.array([10**3, 10**4, 10**5, 10**6])
mc_errors = []

print("3. Оценка методом Монте-Карло:")
for N in N_values:
    x_rand = np.random.uniform(0, 1, N)
    y_rand = np.random.uniform(0, 1, N)
    
    inside_region = y_rand <= x_rand

    integrand_values = np.where(inside_region, x_rand + y_rand, 0.0)
    
    mc_estimate = np.mean(integrand_values)
    mc_err = np.abs(mc_estimate - exact_2)
    mc_errors.append(mc_err)
    
    print(f"   N = 10^{int(np.log10(N))}: интеграл ≈ {mc_estimate:.6f}, погрешность = {mc_err:.2e}")


plt.figure(figsize=(8, 5))
plt.loglog(N_values, mc_errors, "o-", color="darkorange", linewidth=2, label="Погрешность Монте-Карло")

theoretical_trend = mc_errors[0] * np.sqrt(N_values[0]) / np.sqrt(N_values)
plt.loglog(N_values, theoretical_trend, "--", color="gray", alpha=0.7, label=r"Теоретический тренд $O(1/\sqrt{N})$")

plt.title("Зависимость погрешности метода Монте-Карло от числа точек N", fontsize=12)
plt.xlabel("Число точек N", fontsize=11)
plt.ylabel("Абсолютная погрешность", fontsize=11)
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()