class Book:
    def set_data(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f'"{self.title}" - {self.author} ({self.year} год)'

class BankAccount:
    def set_data(self, account_number, balance=0):
        self.__account_number = account_number  # Приватное поле
        self.__balance = balance               # Приватное поле
    
    def deposit(self, amount):
        """Пополнение счета с проверками"""
        if not isinstance(amount, (int, float)):
            return "Ошибка: сумма должна быть числом"
        if amount <= 0:
            return "Ошибка: сумма должна быть положительной"
        self.__balance += amount
        return f"Успешно: пополнено {amount} руб. Новый баланс: {self.__balance} руб."
    
    def withdraw(self, amount):
        """Снятие средств с проверками"""
        if not isinstance(amount, (int, float)):
            return "Ошибка: сумма должна быть числом"
        if amount <= 0:
            return "Ошибка: сумма должна быть положительной"
        if amount > self.__balance:
            return "Ошибка: недостаточно средств"
        self.__balance -= amount
        return f"Успешно: снято {amount} руб. Остаток: {self.__balance} руб."
    
    def get_balance(self):
        """Получить текущий баланс"""
        return self.__balance
    
    def get_account_number(self):
        """Получить номер счета"""
        return self.__account_number
    
    def get_account_info(self):
        """Получить полную информацию о счете"""
        return f"Счет: {self.__account_number}, Баланс: {self.__balance} руб."

# Создаем и тестируем книги
print("1. Тестирование класса Book:")
book1 = Book()
book1.set_data("Война и мир", "Лев Толстой", 1869)
print(book1.get_info())

# Создаем и тестируем банковский счет
print("\n2. Тестирование класса BankAccount:")
account = BankAccount()
account.set_data("40817810123456789000", 1000)

# Тестируем методы
print(account.get_account_info())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))  # Попытка снять больше, чем есть

# Тестируем доступ к полям
print("\n3. Тестирование доступа к полям:")
try:
    print("Попытка получить __balance напрямую:", account.__balance)
except AttributeError as e:
    print(f"Ошибка доступа: {e}")

try:
    print("Попытка получить __account_number напрямую:", account.__account_number)
except AttributeError as e:
    print(f"Ошибка доступа: {e}")

print("\n4. Корректный доступ через методы:")
print("Баланс через метод:", account.get_balance())
print("Номер счета через метод:", account.get_account_number())
print("Информация о счете:", account.get_account_info())
