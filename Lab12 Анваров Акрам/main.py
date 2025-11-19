import json
import os

# -----------------------------
# Класс Student
# -----------------------------
class Student:
    def __init__(self, name: str, group: str, gpa: float):
        # приватные атрибуты
        self.__name = name
        self.__group = group
        # валидируем GPA при создании
        self.__gpa = self.__validate_gpa(gpa)

    # --- Приватный метод валидации ---
    def __validate_gpa(self, gpa):
        try:
            gpa = float(gpa)
        except ValueError:
            raise ValueError("GPA должен быть числом")
        if 0.0 <= gpa <= 4.0:
            return gpa
        raise ValueError("GPA должен быть в диапазоне [0.0, 4.0]")

    # --- Getters ---
    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_gpa(self):
        return self.__gpa

    # --- Setters ---
    def set_group(self, new_group: str):
        self.__group = new_group

    def set_gpa(self, new_gpa):
        self.__gpa = self.__validate_gpa(new_gpa)

    # --- Методы ---
    def display_info(self):
        print(f"Имя: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa:.2f}")

    def update_gpa(self, new_gpa):
        try:
            self.set_gpa(new_gpa)
            print(f"GPA обновлён для {self.__name}: {self.__gpa:.2f}")
        except ValueError as e:
            print("Ошибка при обновлении GPA:", e)

    # Для сохранения в JSON
    def to_dict(self):
        return {
            "name": self.__name,
            "group": self.__group,
            "gpa": self.__gpa
        }

    # Для восстановления из JSON
    @staticmethod
    def from_dict(d):
        return Student(d["name"], d["group"], d["gpa"])


# -----------------------------
# Класс Group
# -----------------------------
class Group:
    def __init__(self):
        self._students = []  # защищённый атрибут списка студентов

    def add_student(self, student: Student):
        # проверка на уникальность по имени
        if any(s.get_name() == student.get_name() for s in self._students):
            print(f"Студент с именем {student.get_name()} уже есть.")
            return
        self._students.append(student)
        print(f"Добавлен студент: {student.get_name()}")

    def remove_student(self, name: str):
        for s in self._students:
            if s.get_name() == name:
                self._students.remove(s)
                print(f"Студент {name} удалён.")
                return
        print("Студент не найден.")

    def show_all(self):
        if not self._students:
            print("Список студентов пуст.")
            return
        print("Список студентов:")
        for s in self._students:
            s.display_info()

    def get_top_students(self, threshold: float):
        try:
            threshold = float(threshold)
        except ValueError:
            print("Порог GPA должен быть числом")
            return []
        top = [s for s in self._students if s.get_gpa() > threshold]
        if not top:
            print(f"Нет студентов с GPA > {threshold}")
        else:
            print(f"Студенты с GPA > {threshold}:")
            for s in top:
                s.display_info()
        return top

    # Сохранение списка студентов в JSON
    def save_to_file(self, filename="students.json"):
        data = [s.to_dict() for s in self._students]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Сохранено {len(data)} студентов в {filename}")

    # Загрузка студентов из JSON (перезаписывает текущий список)
    def load_from_file(self, filename="students.json"):
        if not os.path.exists(filename):
            print(f"Файл {filename} не найден.")
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._students = [Student.from_dict(d) for d in data]
        print(f"Загружено {len(self._students)} студентов из {filename}")


# -----------------------------
# Пример использования (CLI)
# -----------------------------
def demo():
    group = Group()

    # Примеры добавления студентов
    group.add_student(Student("Алиса", "A-101", 3.5))
    group.add_student(Student("Бахыт", "A-101", 3.9))
    group.add_student(Student("Виктор", "B-201", 2.8))

    # Показать всех
    group.show_all()

    # Топ-студенты
    group.get_top_students(3.6)

    # Обновим GPA
    group.remove_student("Виктор")
    s = Student("Дамир", "B-201", 3.2)
    group.add_student(s)
    s.update_gpa(3.7)

    # Сохранить в файл
    group.save_to_file("students.json")

    # Показать содержимое файла
    print("\n--- содержимое файла students.json ---")
    with open("students.json", "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    demo()