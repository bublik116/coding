class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# 2. Функция print_area
def print_area(shape):
    """Функция для вывода площади фигуры"""
    print(f"Площадь фигуры: {shape.area():.2f}")

# Демонстрация работы
def test_shapes():
    print("\nТестирование классов геометрических фигур:")
    
    # Создаем объекты разных классов
    shapes = [
        Rectangle(5, 10),
        Circle(7),
        Rectangle(2, 3),
        Circle(5.5)
    ]
    
    # Вызываем функцию для каждого объекта
    for shape in shapes:
        print_area(shape)
        print(f"Тип объекта: {type(shape).__name__}")

# Основной код
if __name__ == "__main__":
    # Предыдущие тесты (Book, BankAccount, Animal) остаются без изменений
    
    # Тестирование геометрических фигур
    test_shapes()
