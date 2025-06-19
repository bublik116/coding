import json
import os

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
    def __init__(self):
        self.books = []
        self.load()  # Загружаем данные при создании экземпляра
    
    def new_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.name}' добавлена в библиотеку.")
        self.save()
    
    def del_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                print(f"Книга '{book_name}' удалена из библиотеки.")
                self.save()
                return
        print(f"Книга '{book_name}' не найдена в библиотеке.")
    
    def show_book(self):
        if not self.books:
            print("В библиотеке нет книг.")
        else:
            print("Список всех книг в библиотеке:")
            for book in self.books:
                book.get_info()
    
    def save(self, filename="library.json"):
        """Сохраняет все книги в файл"""
        data = []
        for book in self.books:
            data.append(book.to_dict())
        try:
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
    
    def load(self, filename="library.json"):
        """Загружает книги из файла"""
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding='utf-8') as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(book_data) for book_data in data]
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")

# Основной цикл программы
if __name__ == "__main__":
    lib = library()

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
            if not lib.books:
                print("\nВ библиотеке нет книг для удаления.")
            else:
                print("\nУдаление книги:")
                name = input("Введите название книги для удаления: ")
                lib.del_book(name)
        
        elif action == "3":
            lib.show_book()
        
        else:
            print("\nОшибка! Пожалуйста, введите 1, 2 или 3")
