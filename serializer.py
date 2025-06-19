Book_all = []

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    
    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')

class library:
    def new_book(self, book):
        Book_all.append(book)
        print(f"Книга '{book.name}' добавлена в библиотеку.")
    
    def del_book(self, book_name):
        for book in Book_all:
            if book.name == book_name:
                Book_all.remove(book)
                print(f"Книга '{book_name}' удалена из библиотеки.")
                return
        print(f"Книга '{book_name}' не найдена в библиотеке.")
    
    def show_book(self):
        if not Book_all:
            print("В библиотеке нет книг.")
        else:
            print("Список всех книг в библиотеке:")
            for book in Book_all:
                book.get_info()

# Создаем экземпляр библиотеки
lib = library()

# Бесконечный цикл управления
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
