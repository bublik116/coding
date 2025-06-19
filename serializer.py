import json
import os

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"{self.name} ({self.author}, {self.year})"
    
    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["author"], data["year"])

class Library:
    def __init__(self):
        self.books = []
        self.load()  # Автозагрузка при инициализации
    
    def new_book(self, book):
        self.books.append(book)
        print(f"✅ Книга '{book.name}' добавлена")
        self.save()
    
    def del_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                print(f"❌ Книга '{book_name}' удалена")
                self.save()
                return
        print(f"⚠️ Книга '{book_name}' не найдена")
    
    def show_books(self):
        if not self.books:
            print("📚 Библиотека пуста")
        else:
            print("\n📚 Список книг:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book.get_info()}")
    
    def save(self, filename="library.json"):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(
                    [book.to_dict() for book in self.books],
                    f,
                    ensure_ascii=False,
                    indent=2
                )
        except Exception as e:
            print(f"🔥 Ошибка сохранения: {e}")
    
    def load(self, filename="library.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(book) for book in data]
                print(f"🔃 Данные загружены из {filename}")
            else:
                print("🆕 Файл данных не найден, создаём новую библиотеку")
        except FileNotFoundError:
            print("⚠️ Файл не найден, начинаем с пустой библиотеки")
        except json.JSONDecodeError:
            print("⚠️ Ошибка чтения файла, возможно он повреждён")
        except Exception as e:
            print(f"🔥 Неизвестная ошибка при загрузке: {e}")

def main():
    lib = Library()
    
    while True:
        print("\n" + "="*30)
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Показать все книги")
        print("="*30)
        
        choice = input("Выберите действие (1-3): ")
        
        if choice == "1":
            print("\nДобавление книги:")
            name = input("Название: ").strip()
            author = input("Автор: ").strip()
            year = input("Год: ").strip()
            if name and author and year:
                lib.new_book(Book(name, author, year))
            else:
                print("⚠️ Все поля обязательны!")
        
        elif choice == "2":
            if not lib.books:
                print("⚠️ Библиотека пуста!")
            else:
                book_name = input("Название книги для удаления: ").strip()
                if book_name:
                    lib.del_book(book_name)
        
        elif choice == "3":
            lib.show_books()
        
        else:
            print("⚠️ Неверный ввод!")

if __name__ == "__main__":
    main()
        else:
            print("\nОшибка! Пожалуйста, введите 1, 2 или 3")
