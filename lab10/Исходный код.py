import json
# --- Ввод данных пользователем ---
workouts = []
n = int(input("Введите количество упражнений: "))
for i in range(n):
    exercise = input(f"\nНазвание упражнения {i+1}: ")
    sets = int(input("Количество подходов: "))
    reps = int(input("Количество повторений в подходе: "))
    weight = float(input("Вес (кг, если есть, иначе 0): "))

    workouts.append({
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight
    })
# --- Сохранение в текстовый файл ---
with open("workouts.txt", "w", encoding="utf-8") as f:
    for w in workouts:
        f.write(f"{w['exercise']} | Подходов: {w['sets']} | Повторений: {w['reps']} | Вес: {w['weight']} кг\n")
# --- Чтение из файла ---
print("\n📄 Данные из файла workouts.txt:")
with open("workouts.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
# --- Сохранение в JSON ---
with open("workouts.json", "w", encoding="utf-8") as jf:
    json.dump(workouts, jf, ensure_ascii=False, indent=4)
# --- Фильтрация по весу ---
min_weight = float(input("\nВведите минимальный вес для фильтрации (в кг): "))
filtered = [w for w in workouts if w["weight"] >= min_weight]
print(f"\n🏆 Упражнения с весом {min_weight} кг и выше:")
for w in filtered:
    print(f"{w['exercise']} — {w['sets']}x{w['reps']} ({w['weight']} кг)")
