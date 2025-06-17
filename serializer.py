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
