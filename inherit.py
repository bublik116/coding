from abc import ABC, abstractmethod
from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = True  # Защищённый атрибут с доступом через property
    
    # Свойства только для чтения
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def author(self) -> str:
        return self._author
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    @property
    def available(self) -> bool:
        return self._available
    
    @available.setter
    def available(self, value: bool):
        self._available = value
    
    def __str__(self):
        status = "Доступна" if self._available else "На руках"
        return f"'{self._title}' - {self._author} (ISBN: {self._isbn}) [{status}]"


class Library:
    def __init__(self):
        self._books: List[Book] = []
    
    @property
    def books(self) -> List[Book]:
        return self._books.copy()
    
    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise ValueError("Можно добавлять только объекты класса Book")
        
        if book in self._books:
            print(f"Книга '{book.title}' уже есть в библиотеке")
            return
        
        self._books.append(book)
        print(f"Книга добавлена: {book.title}")
    
    def remove_book(self, book: Book) -> None:
        if book in self._books:
            if not book.available:
                print(f"Невозможно удалить: книга '{book.title}' на руках")
                return
            self._books.remove(book)
            print(f"Книга удалена: {book.title}")
        else:
            print(f"Книга '{book.title}' не найдена в библиотеке")
    
    def find_book_by_title(self, title: str) -> Optional[Book]:
        title_lower = title.lower()
        for book in self._books:
            if book.title.lower() == title_lower:
                return book
        return None
    
    def list_available_books(self) -> None:
        available_books = [b for b in self._books if b.available]
        if not available_books:
            print("Нет доступных книг")
            return
        
        print("\nДоступные книги:")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. {book}")


class LibraryUser(ABC):
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self._borrowed_books: List[Book] = []
    
    @property
    def borrowed_books(self) -> List[Book]:
        return self._borrowed_books.copy()
    
    @abstractmethod
    def borrow_book(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass
    
    def list_borrowed_books(self) -> None:
        if not self._borrowed_books:
            print(f"{self.name} не имеет взятых книг")
            return
        
        print(f"\nКниги на руках у {self.name}:")
        for i, book in enumerate(self._borrowed_books, 1):
            print(f"{i}. {book}")


class Student(LibraryUser):
    MAX_BOOKS = 3

    def borrow_book(self, book: Book) -> None:
        if not book.available:
            print(f"Книга '{book.title}' недоступна")
            return
        
        if len(self._borrowed_books) >= self.MAX_BOOKS:
            print(f"Лимит книг ({self.MAX_BOOKS}) превышен")
            return
        
        self._borrowed_books.append(book)
        book.available = False
        print(f"Студент {self.name} взял книгу: '{book.title}'")

    def return_book(self, book: Book) -> None:
        if book not in self._borrowed_books:
            print(f"Ошибка: книга '{book.title}' не была взята")
            return
        
        self._borrowed_books.remove(book)
        book.available = True
        print(f"Студент {self.name} вернул книгу: '{book.title}'")


class Teacher(LibraryUser):
    MAX_BOOKS = 5

    def borrow_book(self, book: Book) -> None:
        if not book.available:
            print(f"Книга '{book.title}' недоступна")
            return
        
        if len(self._borrowed_books) >= self.MAX_BOOKS:
            print(f"Лимит книг ({self.MAX_BOOKS}) превышен")
            return
        
        self._borrowed_books.append(book)
        book.available = False
        print(f"Преподаватель {self.name} взял книгу: '{book.title}'")

    def return_book(self, book: Book) -> None:
        if book not in self._borrowed_books:
            print(f"Ошибка: книга '{book.title}' не была взята")
            return
        
        self._borrowed_books.remove(book)
        book.available = True
        print(f"Преподаватель {self.name} вернул книгу: '{book.title}'")


# Пример использования
def main():
    # Создаём библиотеку
    library = Library()

    # Добавляем книги
    books_data = [
        ("Война и мир", "Лев Толстой", "978-5-389-06256-6"),
        ("Преступление и наказание", "Фёдор Достоевский", "978-5-17-067678-0"),
        ("Философия Python", "Лучано Рамальо", "978-5-496-01127-3"),
        ("Чистый код", "Роберт Мартин", "978-5-496-00487-9"),
        ("1984", "Джордж Оруэлл", "978-5-17-080115-2")
    ]

    for title, author, isbn in books_data:
        library.add_book(Book(title, author, isbn))

    # Создаём пользователей
    student = Student("Иван Петров", "S123")
    teacher = Teacher("Анна Иванова", "T456")

    # Демонстрация работы
    print("\n=== Начало работы ===")
    library.list_available_books()

    # Студент берёт книги
    print("\n=== Студент берёт книги ===")
    war_and_peace = library.find_book_by_title("Война и мир")
    crime = library.find_book_by_title("Преступление и наказание")
    python_book = library.find_book_by_title("Философия Python")

    if war_and_peace and crime and python_book:
        student.borrow_book(war_and_peace)
        student.borrow_book(crime)
        student.borrow_book(python_book)
        student.borrow_book(war_and_peace)  # Попытка взять уже взятую книгу

    # Преподаватель берёт книги
    print("\n=== Преподаватель берёт книги ===")
    clean_code = library.find_book_by_title("Чистый код")
    orwell = library.find_book_by_title("1984")

    if clean_code and orwell:
        teacher.borrow_book(clean_code)
        teacher.borrow_book(orwell)

    # Показываем статус
    print("\n=== Текущий статус ===")
    student.list_borrowed_books()
    teacher.list_borrowed_books()
    library.list_available_books()

    # Возврат книг
    print("\n=== Возврат книг ===")
    if war_and_peace and crime and clean_code:
        student.return_book(war_and_peace)
        teacher.return_book(clean_code)
        student.return_book(crime)  # Возвращаем ещё одну книгу

    # Пытаемся удалить книгу
    print("\n=== Попытка удаления книги ===")
    if orwell:
        library.remove_book(orwell)  # Не удалится, так как книга на руках

    # Финальный статус
    print("\n=== Финальный статус ===")
    student.list_borrowed_books()
    teacher.list_borrowed_books()
    library.list_available_books()


if __name__ == "__main__":
    main()
