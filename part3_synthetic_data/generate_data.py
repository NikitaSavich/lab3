import argparse
import os
import numpy as np
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(
        description="Генерация синтетического набора данных продаж интернет-магазина."
    )
    parser.add_argument(
        "-n", "--rows",
        type=int,
        default=1000,
        help="Количество генерируемых записей (по умолчанию: 1000)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="data/sales_data.csv",
        help="Путь для сохранения CSV-файла (по умолчанию: data/sales_data.csv)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Сид генератора случайных чисел для воспроизводимости (по умолчанию: 42)"
    )
    parser.add_argument(
        "--start-date",
        type=str,
        default="2025-01-01",
        help="Начальная дата диапазона (ГГГГ-ММ-ДД)"
    )
    parser.add_argument(
        "--end-date",
        type=str,
        default="2025-12-31",
        help="Конечная дата диапазона (ГГГГ-ММ-ДД)"
    )
    return parser.parse_args()

def generate_sales_data(rows: int, seed: int, start_date: str, end_date: str) -> pd.DataFrame:
    np.random.seed(seed)

    categories = ["Смартфоны", "Ноутбуки", "Наушники", "Мониторы", "Клавиатуры"]
    cat_weights = [0.35, 0.20, 0.20, 0.15, 0.10]
    
    price_ranges = {
        "Смартфоны": (15000, 95000),
        "Ноутбуки": (45000, 180000),
        "Наушники": (2500, 22000),
        "Мониторы": (12000, 65000),
        "Клавиатуры": (2000, 16000)
    }

    order_ids = [f"ORD-{i:06d}" for i in range(1, rows + 1)]
    chosen_categories = np.random.choice(categories, size=rows, p=cat_weights)

    prices = np.zeros(rows)
    for cat, (p_min, p_max) in price_ranges.items():
        mask = (chosen_categories == cat)
        count = np.sum(mask)
        if count > 0:
            prices[mask] = np.random.uniform(p_min, p_max, size=count)
    prices = np.round(prices, 2)

    date_start_ts = pd.to_datetime(start_date).value // 10**9
    date_end_ts = pd.to_datetime(end_date).value // 10**9
    random_timestamps = np.random.randint(date_start_ts, date_end_ts, size=rows)
    dates = pd.to_datetime(random_timestamps, unit="s").strftime("%Y-%m-%d")

    quantities = np.random.choice([1, 2, 3, 4], size=rows, p=[0.70, 0.18, 0.08, 0.04])
    discounts = np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], size=rows, p=[0.50, 0.20, 0.15, 0.10, 0.05])
    total_costs = np.round(prices * quantities * (1.0 - discounts), 2)

    payment_methods = np.random.choice(
        ["Банковская карта", "СБП", "Наличные", "Рассрочка"],
        size=rows,
        p=[0.55, 0.25, 0.10, 0.10]
    )

    ratings = np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0], size=rows, p=[0.03, 0.05, 0.12, 0.35, 0.45])
    nan_mask = np.random.binomial(1, 0.05, size=rows).astype(bool)
    ratings[nan_mask] = np.nan

    df = pd.DataFrame({
        "order_id": order_ids,
        "date": dates,
        "category": chosen_categories,
        "price": prices,
        "quantity": quantities,
        "discount": discounts,
        "total_cost": total_costs,
        "payment_method": payment_methods,
        "customer_rating": ratings
    })
    
    return df

def main():
    args = parse_args()

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    print(f"Генерация {args.rows} записей...")
    df = generate_sales_data(args.rows, args.seed, args.start_date, args.end_date)

    df.to_csv(args.output, index=False, encoding="utf-8")
    print(f"Файл успешно сохранен: {args.output}")
    print("\nПервые 5 строк датасета:")
    print(df.head())

if __name__ == "__main__":
    main()