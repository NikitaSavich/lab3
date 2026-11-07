import numpy as np

def input_float_array(prompt):
    while True:
        try:
            raw = input(prompt).strip()
            arr = np.array([float(x) for x in raw.split()])
            if len(arr) == 0 or np.any(arr <= 0):
                print("Ошибка: введите положительные числа через пробел.")
                continue
            return arr
        except ValueError:
            print("Ошибка: введены некорректные символы. Ожидаются числа через пробел.")

def main():
    while True:
        lengths = input_float_array("Длины:    ")
        speeds = input_float_array("Скорости: ")
        if len(lengths) == len(speeds):
            break
        print(f"Ошибка: количество длин ({len(lengths)}) не совпадает с количеством скоростей ({len(speeds)}). Повторите ввод.")

    n = len(lengths)

    while True:
        try:
            k_input = input("k = ").strip()
            p_input = input("p = ").strip()
            k = int(k_input)
            p = int(p_input)

            if not (1 <= k <= n and 1 <= p <= n):
                print(f"Ошибка: номера участков должны лежать в диапазоне от 1 до {n}.")
                continue
            if k > p:
                print("Ошибка: начальный участок k не может быть больше конечного участка p.")
                continue
            break
        except ValueError:
            print("Ошибка: k и p должны быть целыми числами.")

    sub_lengths = lengths[k - 1 : p]
    sub_speeds = speeds[k - 1 : p]

    total_s = np.sum(sub_lengths)
    times_per_segment = sub_lengths / sub_speeds
    total_t = np.sum(times_per_segment)
    avg_v = total_s / total_t

    while True:
        try:
            t_input = input("t = ").strip()
            t = float(t_input)
            if t < 0:
                print("Ошибка: время t не может быть отрицательным.")
                continue
            if t > total_t:
                print(f"Ошибка: t ({t:.2f} ч) превышает общее время пути T ({total_t:.2f} ч).")
                continue
            break
        except ValueError:
            print("Ошибка: t должно быть числом.")

    cum_times = np.cumsum(times_per_segment)
    idx_in_sub = int(np.searchsorted(cum_times, t, side="right"))

    if idx_in_sub == 0:
        time_spent_in_prev = 0.0
    else:
        time_spent_in_prev = cum_times[idx_in_sub - 1]

    if idx_in_sub >= len(sub_lengths):
        current_segment_num = p
        dist_from_start = sub_lengths[-1]
    else:
        current_segment_num = (k - 1) + idx_in_sub + 1
        time_in_current_segment = t - time_spent_in_prev
        dist_from_start = time_in_current_segment * sub_speeds[idx_in_sub]
        
    print(f"S = {total_s:g} км, T = {total_t:.2f} ч, V = {avg_v:.2f} км/ч")
    print(f"Через {t:g} ч автомобиль на участке {current_segment_num}, в {dist_from_start:.1f} км от его начала")

if __name__ == "__main__":
    main()