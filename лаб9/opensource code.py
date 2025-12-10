import json
import csv

def save_to_txt(books):
    with open("books.txt", "w", encoding="utf-8") as f:
        for b in books:
            f.write(f"{b['title']} | {b['author']} | {b['year']}\n")
    print("\nДанные сохранены в books.txt")

def save_to_json(books):
    with open("books.json", "w", encoding="utf-8") as jf:
        json.dump(books, jf, ensure_ascii=False, indent=4)
    print("\nДанные сохранены в books.json")

def save_to_csv(books):
    with open("books.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ['title', 'author', 'year']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for b in books:
            writer.writerow(b)
    print("\nДанные сохранены в books.csv")

def load_from_txt():
    try:
        with open("books.txt", "r", encoding="utf-8") as f:
            books = []
            for line in f:
                title, author, year = line.strip().split(" | ")
                books.append({"title": title, "author": author, "year": int(year)})
            return books
    except FileNotFoundError:
        print("Файл books.txt не найден.")
        return []

def load_from_json():
    try:
        with open("books.json", "r", encoding="utf-8") as jf:
            books = json.load(jf)
            return books
    except FileNotFoundError:
        print("Файл books.json не найден.")
        return []

def filter_books_by_year(books, min_year):
    return [b for b in books if b["year"] >= min_year]

def display_books(books):
    if not books:
        print("Нет данных для отображения.")
        return
    for b in books:
        print(f"«{b['title']}» — {b['author']} ({b['year']})")

def main():
    books = []
    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Сохранить данные (TXT, JSON, CSV)")
        print("4. Фильтровать по году издания")
        print("5. Загрузить данные из JSON")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                n = int(input("Введите количество книг: "))
                for i in range(n):
                    title = input(f"Название книги {i+1}: ")
                    author = input("Автор: ")
                    year = int(input("Год издания: "))
                    books.append({"title": title, "author": author, "year": year})
            except ValueError:
                print("Ошибка ввода! Пожалуйста, введите корректные данные.")

        elif choice == "2":
            display_books(books)

        elif choice == "3":
            print("\nСохранить как:")
            print("1. TXT")
            print("2. JSON")
            print("3. CSV")
            format_choice = input("Выберите формат: ")

            if format_choice == "1":
                save_to_txt(books)
            elif format_choice == "2":
                save_to_json(books)
            elif format_choice == "3":
                save_to_csv(books)
            else:
                print("Неверный выбор.")

        elif choice == "4":
            try:
                min_year = int(input("Введите минимальный год издания: "))
                filtered_books = filter_books_by_year(books, min_year)
                print(f"\nКниги, изданные после {min_year} года:")
                display_books(filtered_books)
            except ValueError:
                print("Ошибка ввода! Введите число.")

        elif choice == "5":
            books = load_from_json()
            print("Данные загружены из books.json")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
