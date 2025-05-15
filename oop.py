class Book:
    def set_data(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f'"{self.title}" - {self.author} ({self.year} год)'

class BankAccount:
    def set_data(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            return "Ошибка: сумма должна быть числом"
        if amount <= 0:
            return "Ошибка: сумма должна быть положительной"
        self.__balance += amount
        return f"Успешно: пополнено {amount} руб. Новый баланс: {self.__balance} руб."
    
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            return "Ошибка: сумма должна быть числом"
        if amount <= 0:
            return "Ошибка: сумма должна быть положительной"
        if amount > self.__balance:
            return "Ошибка: недостаточно средств"
        self.__balance -= amount
        return f"Успешно: снято {amount} руб. Остаток: {self.__balance} руб."
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number

# 1. Базовый класс Animal
class Animal:
    def make_sound(self):
        return "Некоторые звуки животного"

# 2. Подклассы Dog и Cat
class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"

# 3. Создаем список животных и вызываем make_sound()
def test_animals():
    print("\nТестирование классов животных:")
    animals = [Dog(), Cat(), Animal(), Dog()]
    
    for animal in animals:
        print(f"Животное издает звук: {animal.make_sound()}")

# Основной код
if __name__ == "__main__":
    # Тестирование книг
    print("1. Тестирование класса Book:")
    book1 = Book()
    book1.set_data("Война и мир", "Лев Толстой", 1869)
    print(book1.get_info())

    # Тестирование банковского счета
    print("\n2. Тестирование класса BankAccount:")
    account = BankAccount()
    account.set_data("40817810123456789000", 1000)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Текущий баланс: {account.get_balance()} руб.")

    # Тестирование животных
    test_animals()
