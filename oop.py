class Book:
    def __init__(self, title="", author="", year=None):
        self.__title = title
        self.__author = author
        self.__year = year
    
    def set_data(self, title, author, year):
        """Установка всех данных книги с проверками"""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги должно быть непустой строкой")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Имя автора должно быть непустой строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год издания должен быть положительным целым числом")
        
        self.__title = title
        self.__author = author
        self.__year = year
    
    def get_info(self):
        """Получение информации о книге"""
        return f'"{self.__title}" - {self.__author} ({self.__year} год)'
    
    # Геттеры для полей
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    # Сеттеры для полей с проверками
    def set_title(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги должно быть непустой строкой")
        self.__title = title
    
    def set_author(self, author):
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Имя автора должно быть непустой строкой")
        self.__author = author
    
    def set_year(self, year):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год издания должен быть положительным целым числом")
        self.__year = year


# Создаем книги с помощью конструктора
try:
    book1 = Book("Война и мир", "Лев Толстой", 1869)
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
    book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    
    # Тестируем доступ к полям через методы
    print("Информация о книгах:")
    print(book1.get_info())
    print(book2.get_info())
    print(book3.get_info())
    
    print("\nТестируем геттеры:")
    print(f"Название первой книги: {book1.get_title()}")
    print(f"Автор второй книги: {book2.get_author()}")
    print(f"Год издания третьей книги: {book3.get_year()}")
    
    print("\nТестируем сеттеры:")
    book1.set_title("Анна Каренина")
    book1.set_year(1877)
    print("После изменения:", book1.get_info())
    
    # Попытка прямого доступа к приватным полям
    print("\nПопытка прямого доступа к приватным полям:")
    try:
        print(book1.__title)  # Вызовет ошибку
    except AttributeError as e:
        print(f"Ошибка: {e}")
    
    # Тестирование валидации
    print("\nТестирование валидации данных:")
    try:
        book1.set_year(-100)  # Неверный год
    except ValueError as e:
        print(f"Ошибка при установке года: {e}")
    
    try:
        book1.set_title("")  # Пустое название
    except ValueError as e:
        print(f"Ошибка при установке названия: {e}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
