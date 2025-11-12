import math
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - ERROR - %(message)s"
)

def calculate_compound_interest(P, r, t, n=12):
    try:
        # Проверка на отрицательные значения
        if P <= 0 or r <= 0 or t <= 0:
            raise ValueError("Все значения должны быть положительными.")

        # Расчёт сложных процентов
        amount = P * (1 + (r / 100) / n) ** (n * t)
        return amount

    except Exception as e:
        logging.error(f"Ошибка при расчете: {e}")
        raise  # повторно выбрасываем исключение для обработки выше

def main():
    try:
        print("=== Финансовый калькулятор ===")

        # Ввод данных
        P = float(input("Введите сумму вклада (тг): "))
        r = float(input("Введите годовую процентную ставку (%): "))
        t = float(input("Введите срок вклада (в годах): "))

        # Расчёт
        result = calculate_compound_interest(P, r, t)

        # Вывод результата
        print(f"Итоговая сумма через {t} лет: {result:.2f} тенге")

        # Запись в result.txt
        with open("result.txt", "w", encoding="utf-8") as f:
            f.write(f"Вклад: {P} тг\nСтавка: {r}%\nСрок: {t} лет\nИтоговая сумма: {result:.2f} тг\n")

        print("Работа программы завершена.")

    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        logging.error(f"Общая ошибка программы: {e}")
    finally:
        print("Программа завершила выполнение.")

if __name__ == "__main__":
    main()

