import logging
from typing import Iterable, List

# Настройка логирования: файл app.log (в той же папке), INFO+ERROR
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def calculate_average(grades: Iterable[float]) -> float:
    """
    Вычисляет средний балл и возвращает его с округлением до 2 знаков.
    Проверяет: непустой список и числовые значения.
    """
    if grades is None:
        logger.error("Передан None вместо списка оценок")
        raise ValueError("grades не должен быть None")

    grades_list = list(grades)
    if not grades_list:
        logger.error("Список оценок пуст")
        raise ValueError("Список оценок не может быть пустым")

    if not all(isinstance(x, (int, float)) for x in grades_list):
        logger.error("Некорректный тип данных в списке оценок: %s", grades_list)
        raise TypeError("Все оценки должны быть числами (int или float)")

    avg = sum(grades_list) / len(grades_list)
    avg_rounded = round(avg, 2)
    logger.info("Средний балл рассчитан: %s (raw=%s)", avg_rounded, avg)
    return avg_rounded


def determine_grade_letter(avg: float) -> str:
    """
    Преобразует числовой средний балл в буквенную оценку.
    Ожидается, что avg — число в диапазоне [0, 100] (проверка не обязательна).
    """
    try:
        a = float(avg)
    except Exception:
        logger.error("determine_grade_letter: неверный тип avg: %s", avg)
        raise TypeError("avg должен быть числом")

    if a >= 90:
        letter = "A"
    elif a >= 80:
        letter = "B"
    elif a >= 70:
        letter = "C"
    elif a >= 60:
        letter = "D"
    else:
        letter = "F"

    logger.info("Итоговая буквенная оценка для %s: %s", a, letter)
    return letter


def student_report(name: str, grades: Iterable[float]) -> str:
    """
    Формирует итоговый отчёт для студента.
    Возвращает многострочную строку с именем, средним баллом и буквенной оценкой.
    """
    if not isinstance(name, str) or not name.strip():
        logger.error("Неверное имя студента: %r", name)
        raise ValueError("Имя студента должно быть непустой строкой")

    logger.info("Формирование отчёта для студента %s", name)
    avg = calculate_average(grades)
    letter = determine_grade_letter(avg)
    report = f"Студент: {name}\nСредний балл: {avg}\nОценка: {letter}"
    logger.info("Отчёт сформирован для %s: %s", name, report.replace("\n", " | "))
    return report


def parse_grades_from_string(s: str) -> List[float]:
    """
    Парсит строку с оценками (например "90 80 100") в список float.
    Пробел/запятая/точка с запятой разрешены как разделители.
    """
    if s is None:
        logger.error("parse_grades_from_string: None передан вместо строки")
        raise ValueError("Входная строка не задана")

    raw = s.replace(',', ' ').replace(';', ' ')
    parts = [p for p in raw.split() if p]
    if not parts:
        logger.error("parse_grades_from_string: пустая строка")
        raise ValueError("Строка не содержит оценок")

    grades: List[float] = []
    for p in parts:
        try:
            val = float(p)
        except ValueError:
            logger.error("Невозможно преобразовать в число: %s", p)
            raise ValueError(f"Некорректное значение оценки: {p}")
        grades.append(val)

    logger.info("Строка '%s' преобразована в оценки %s", s, grades)
    return grades


if __name__ == "__main__":
    # Интерактивный запуск
    try:
        name = input("Введите имя студента: ").strip()
        raw = input("Введите оценки через пробел (или запятую): ").strip()
        grades = parse_grades_from_string(raw)
        print(student_report(name, grades))
    except Exception as e:
        print("Ошибка:", e)
        logger.exception("Произошло исключение в интерактивном режиме")