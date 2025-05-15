class Book:
    # Одна функция для установки всех данных книги
    def set_data(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f'"{self.title}" - {self.author} ({self.year} год)'

# Создаем и настраиваем 3 объекта класса Book
book1 = Book()
book1.set_data("Война и мир", "Лев Толстой", 1869)

book2 = Book()
book2.set_data("Преступление и наказание", "Фёдор Достоевский", 1866)

book3 = Book()
book3.set_data("Мастер и Маргарита", "Михаил Булгаков", 1967)

# Выводим описание книг
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
