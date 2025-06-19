import json
import os

Book_all = []

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    
    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')
    
    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["author"], data["year"])

class library:
    def new_book(self, book):
        Book_all.append(book)
        print(f"Книга '{book.name}' добавлена в библиотеку.")
        self.save()
    
    def del_book(self, book_name):
        for book in Book_all:
            if book.name == book_name:
                Book_all.remove(book)
                print(f"Книга '{book_name}' удалена из библиотеку.")
                self.save()
                return
        print(f"Книга '{book_name}' не найдена в библиотеке.")
    
    def show_book(self):
        if not Book_all:
            print("В библиотеке нет книг.")
        else:
            print("Список всех книг в библиотеке:")
            for book in Book_all:
                book.get_info()
    
    def save(self):
        """Сохраняет все книги в файл"""
        try:
            with open('library.json', 'w', encoding='utf-8') as f:
                json.dump([book.to_dict() for book in Book_all], f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
    
    def load(self):
        """Загружает книги из файла"""
        try:
            if os.path.exists('library.json'):
                with open('library.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    Book_all.clear()
                    for book_data in data:
                        Book_all.append(Book.from_dict(book_data))
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")

# Инициализация библиотеки
lib = library()
lib.load()  # Загружаем данные при старте

# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1 - Добавить книгу")
    print("2 - Удалить книгу")
    print("3 - Показать все книги")
    
    action = input("Ваш выбор (1-3): ")
    
    if action == "1":
        print("\nДобавление новой книги:")
        name = input("Название: ")
        author = input("Автор: ")
        year = input("Год издания: ")
        lib.new_book(Book(name, author, year))
    
    elif action == "2":
        if not Book_all:
            print("\nВ библиотеке нет книг для удаления.")
        else:
            print("\nУдаление книги:")
            name = input("Введите название книги для удаления: ")
            lib.del_book(name)
    
    elif action == "3":
        lib.show_book()
    
    else:
        print("\nОшибка! Пожалуйста, введите 1, 2 или 3")
    
    else:
        print("\nОшибка! Пожалуйста, введите 1, 2 или 3")
