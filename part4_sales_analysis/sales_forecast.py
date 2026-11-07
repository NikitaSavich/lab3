import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

possible_paths = [
    "data/sales_data.csv",
    os.path.join("..", "part3_synthetic_data", "data", "sales_data.csv")
]
csv_path = next((p for p in possible_paths if os.path.exists(p)), None)

if not csv_path:
    raise FileNotFoundError("Датасет sales_data.csv не найден. Проверьте наличие данных.")

print(f"Загрузка данных из: {csv_path}")
df = pd.read_csv(csv_path)
df["date"] = pd.to_datetime(df["date"])

weekly_sales = (
    df.groupby(["category", pd.Grouper(key="date", freq="W-SUN")])["total_cost"]
    .sum()
    .unstack(level="category", fill_value=0.0)
    .sort_index()
)

TEST_WEEKS = 8
train_df = weekly_sales.iloc[:-TEST_WEEKS]
test_df = weekly_sales.iloc[-TEST_WEEKS:]

print(f"Всего недель: {len(weekly_sales)} (Обучение: {len(train_df)}, Тест: {len(test_df)})\n")

def calc_metrics(actual, pred):
    mae = np.mean(np.abs(actual - pred))
    non_zero = actual != 0
    mape = np.mean(np.abs((actual[non_zero] - pred[non_zero]) / actual[non_zero])) * 100
    return mae, mape

categories = weekly_sales.columns
fig, axes = plt.subplots(nrows=len(categories), ncols=1, figsize=(12, 3.5 * len(categories)), sharex=True)

if len(categories) == 1:
    axes = [axes]

print(f"{'Категория':<15} | {'Метод':<20} | {'MAE (руб.)':<12} | {'MAPE (%)':<10}")
print("-" * 65)

for ax, cat in zip(axes, categories):
    train_series = train_df[cat]
    test_actual = test_df[cat].values
    test_dates = test_df.index

    rolling_full = weekly_sales[cat].rolling(window=4).mean().shift(1)
    pred_rolling = rolling_full.loc[test_dates].values

    x_train = np.arange(len(train_series))
    coeffs = np.polyfit(x_train, train_series.values, deg=1)
    x_test = np.arange(len(train_series), len(train_series) + TEST_WEEKS)
    pred_trend = np.polyval(coeffs, x_test)

    mae_roll, mape_roll = calc_metrics(test_actual, pred_rolling)
    mae_trend, mape_trend = calc_metrics(test_actual, pred_trend)

    print(f"{cat:<15} | {'Скользящее среднее':<20} | {mae_roll:<12.2f} | {mape_roll:<10.2f}")
    print(f"{cat:<15} | {'Линейный тренд':<20} | {mae_trend:<12.2f} | {mape_trend:<10.2f}")

    ax.plot(train_series.index, train_series.values, label="Факт (Train)", color="#1f77b4", marker="o", markersize=3)
    ax.plot(test_dates, test_actual, label="Факт (Test)", color="#2ca02c", marker="o", markersize=4, linewidth=2)
    ax.plot(test_dates, pred_rolling, label=f"Скользящее среднее (MAE: {mae_roll:,.0f})", color="#ff7f0e", linestyle="--", marker="s", markersize=4)
    ax.plot(test_dates, pred_trend, label=f"Линейный тренд (MAE: {mae_trend:,.0f})", color="#d62728", linestyle=":", marker="^", markersize=4)

    ax.set_title(f"Категория: {cat}", fontsize=11, fontweight="bold")
    ax.set_ylabel("Выручка (руб.)", fontsize=10)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left", fontsize=8)

plt.xlabel("Дата (Недели)", fontsize=11)
plt.xticks(rotation=45)
plt.tight_layout()

output_img = "sales_forecast.png"
plt.savefig(output_img, dpi=300)
print(f"\nГрафик сохранен в файл: {output_img}")
plt.show()