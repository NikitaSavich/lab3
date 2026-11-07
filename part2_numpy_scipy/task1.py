import numpy as np

expenses = np.array([3200, 3100, 2600, 1900, 1500, 1300, 1250, 1400, 1800, 2300, 2900, 3500])
winter_indices = np.array([11, 0, 1])
summer_indices = np.array([5, 6, 7])

winter_sum = np.sum(expenses[winter_indices])
summer_sum = np.sum(expenses[summer_indices])

if winter_sum > summer_sum:
    comparison = "больше тратится зимой"
elif summer_sum > winter_sum:
    comparison = "больше тратится летом"
else:
    comparison = "траты зимой и летом одинаковы"

max_expense = np.max(expenses)
peak_months = np.where(expenses == max_expense)[0] + 1

print(f"Расходы: {' '.join(expenses.astype(str))}")
print(f"Зима: {winter_sum}, лето: {summer_sum} -> {comparison}")
print(f"Максимум ({max_expense}) в месяцах: {', '.join(peak_months.astype(str))}")