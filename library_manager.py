import json
from typing import List, Dict

# Путь к файлу хранения данных
DATA_FILE = "books.json"

# Инициализация файла данных
def initialize_data_file():
    try:
        with open(DATA_FILE, "r") as file:
            json.load(file)  # Проверяем JSON на корректность
    except (FileNotFoundError, json.JSONDecodeError):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

# Загрузка данных
def load_books() -> List[Dict]:
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Сохранение данных
def save_books(books: List[Dict]):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Генерация ID
def generate_id(books: List[Dict]) -> int:
    return max((book["id"] for book in books), default=0) + 1

# Добавление книги
def add_book(title: str, author: str, year: int):
    books = load_books()
    book = {
        "id": generate_id(books),
        "title": title,
        "author": author,
        "year": year,
        "status": "available"
    }
    books.append(book)
    save_books(books)
    print(f"Книга '{title}' успешно добавлена!")

# Удаление книги
def delete_book(book_id: int):
    books = load_books()
    updated_books = [book for book in books if book["id"] != book_id]
    if len(books) == len(updated_books):
        print(f"Книга с ID {book_id} не найдена.")
        return
    save_books(updated_books)
    print(f"Книга с ID {book_id} успешно удалена!")

# Поиск книги
def search_books(query: str) -> List[Dict]:
    books = load_books()
    results = [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    return results

# Изменение статуса книги
def update_status(book_id: int, new_status: str):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            book["status"] = new_status
            save_books(books)
            print(f"Статус книги с ID {book_id} обновлен на '{new_status}'!")
            return
    print(f"Книга с ID {book_id} не найдена.")

# Отображение всех книг
def list_books():
    books = load_books()
    if not books:
        print("Библиотека пуста.")
        return
    print("Список всех книг:")
    for book in books:
        print_book(book)

# Вывод информации о книге
def print_book(book: Dict):
    print(f"[ID: {book['id']}] '{book['title']}' - {book['author']} ({book['year']}) | Статус: {book['status']}")

# Основное меню
def main():
    initialize_data_file()
    while True:
        print("\n=== Library Manager ===")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")
        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                add_book(title, author, year)
            elif choice == "2":
                book_id = int(input("Введите ID книги: "))
                delete_book(book_id)
            elif choice == "3":
                query = input("Введите название или автора для поиска: ")
                results = search_books(query)
                if results:
                    print("Найденные книги:")
                    for book in results:
                        print_book(book)
                else:
                    print("Книг не найдено.")
            elif choice == "4":
                list_books()
            elif choice == "5":
                book_id = int(input("Введите ID книги: "))
                new_status = input("Введите новый статус ('available' или 'issued'): ")
                if new_status not in ["available", "issued"]:
                    print("Недопустимый статус.")
                else:
                    update_status(book_id, new_status)
            elif choice == "0":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: Введены некорректные данные.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
