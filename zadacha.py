# cold_calc_console.py
import sqlite3
from sqlite3 import Error

class DBCore:
    def __init__(self, db_file=":memory:"):
        """Инициализация базы данных SQLite в памяти"""
        try:
            self.connection = sqlite3.connect(db_file)
            self.connection.row_factory = sqlite3.Row
            self.initialize_database()
            print("✓ База данных инициализирована")
        except Error as e:
            print(f"✗ Ошибка подключения к БД: {e}")

    def initialize_database(self):
        """Создание и заполнение таблиц тестовыми данными"""
        queries = [
            # Таблица компрессоров
            """CREATE TABLE IF NOT EXISTS compressors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT NOT NULL,
                manufacturer TEXT,
                compressor_type TEXT CHECK(compressor_type IN ('piston_semi', 'piston_herm', 'scroll', 'screw')),
                refrigerant_type TEXT CHECK(refrigerant_type IN ('R404A', 'R22', 'R134a', 'R290', 'R410a')),
                cooling_capacity_kw REAL,
                volumetric_capacity REAL,
                suction_temperature REAL,
                operational_current REAL,
                starting_current REAL
            );""",
            
            # Таблица фреонов
            """CREATE TABLE IF NOT EXISTS refrigerants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                chemical_formula TEXT,
                density_liquid_25c REAL,
                critical_temperature REAL,
                critical_pressure REAL
            );""",
            
            # Заполнение компрессоров
            """INSERT INTO compressors 
                (model_name, manufacturer, compressor_type, refrigerant_type, cooling_capacity_kw, 
                 volumetric_capacity, suction_temperature, operational_current, starting_current)
            VALUES
                ('NT-66', 'Bitzer', 'piston_semi', 'R404A', 5.2, 4.8, -25.0, 10.5, 45.0),
                ('SC-15', 'Copeland', 'scroll', 'R410a', 8.7, 7.9, -20.0, 15.1, 65.0),
                ('P-144', 'RefComp', 'piston_herm', 'R134a', 3.1, 2.8, -10.0, 6.8, 28.0),
                ('S-78', 'Dorin', 'screw', 'R22', 25.0, 22.5, -30.0, 42.0, 180.0),
                ('M-100', 'Maneurop', 'piston_semi', 'R404A', 7.5, 6.9, -25.0, 14.2, 60.0)
            ;""",
            
            # Заполнение фреонов
            """INSERT OR IGNORE INTO refrigerants 
                (name, chemical_formula, density_liquid_25c, critical_temperature, critical_pressure)
            VALUES
                ('R404A', 'R-125/R-143a/R-134a', 1010.0, 72.1, 3730.0),
                ('R22', 'CHClF2', 1190.0, 96.2, 4990.0),
                ('R134a', 'CH2FCF3', 1210.0, 101.1, 4059.0),
                ('R290', 'C3H8', 490.0, 96.7, 4240.0),
                ('R410a', 'R-32/R-125', 1040.0, 72.5, 4900.0)
            ;"""
        ]
        
        for query in queries:
            try:
                self.connection.execute(query)
            except Error as e:
                print(f"Ошибка выполнения запроса: {e}")
        self.connection.commit()

    def execute_read_query(self, query, params=None):
        """Выполнение запроса на чтение"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]
        except Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return []

    def close_connection(self):
        """Закрытие соединения с БД"""
        if self.connection:
            self.connection.close()

class ColdCalculator:
    def __init__(self, db_core):
        self.db = db_core

    def calculate_room_volume(self, length, width, height):
        """Рассчитывает объем помещения"""
        return length * width * height

    def calculate_required_power(self, volume, chamber_type, ambient_temp=32):
        """Рассчитывает требуемую холодильную мощность"""
        # Упрощенный расчет на основе объема и типа камеры
        base_power_per_m3 = {
            'medium_temp': 0.045,  # кВт/м³ для среднетемпературных
            'low_temp': 0.085      # кВт/м³ для низкотемпературных
        }
        
        # Корректировка на разность температур
        if chamber_type == 'medium_temp':
            temp_difference = ambient_temp - (-2)  # Разность с -2°C
        else:
            temp_difference = ambient_temp - (-25)  # Разность с -25°C
            
        temp_factor = temp_difference / 30  # Нормирующий коэффициент
        
        required_power = volume * base_power_per_m3[chamber_type] * temp_factor
        return max(required_power, 0.5)  # Минимальная мощность 0.5 кВт

    def get_compressors_by_power(self, required_power, refrigerant_type=None):
        """Выбирает компрессоры по мощности и типу фреона"""
        query = """
        SELECT * FROM compressors 
        WHERE cooling_capacity_kw BETWEEN ? AND ?
        """
        min_power = required_power * 0.8   # -20%
        max_power = required_power * 1.3   # +30%
        params = [min_power, max_power]

        if refrigerant_type:
            query += " AND refrigerant_type = ?"
            params.append(refrigerant_type)

        query += " ORDER BY cooling_capacity_kw"
        return self.db.execute_read_query(query, params)

    def get_refrigerants_info(self):
        """Возвращает информацию о всех фреонах"""
        query = "SELECT * FROM refrigerants ORDER BY name"
        return self.db.execute_read_query(query)

    def calculate_refrigerant_mass(self, compressor_model, line_length=10, line_diameter=0.022):
        """Упрощенный расчет массы фреона"""
        # Базовая масса для компрессора + масса в трубопроводах
        base_mass = {
            'NT-66': 3.2, 'SC-15': 4.8, 'P-144': 2.1, 'S-78': 12.5, 'M-100': 5.0
        }
        
        # Объем трубопроводов (π * r² * L)
        line_volume = 3.1416 * (line_diameter/2)**2 * line_length
        # Предполагаем плотность R404A ~1010 кг/м³
        line_mass = line_volume * 1010
        
        total_mass = base_mass.get(compressor_model, 3.0) + line_mass
        return round(total_mass, 2)

def display_compressors(compressors):
    """Отображает список компрессоров"""
    if not compressors:
        print("  Не найдено подходящих компрессоров")
        return
    
    print("\n  № | Модель         | Производитель | Тип       | Фреон  | Мощность (кВт)")
    print("----+----------------+---------------+---------------+--------+---------------")
    for i, comp in enumerate(compressors, 1):
        print(f"  {i} | {comp['model_name']:14} | {comp['manufacturer']:13} | "
              f"{comp['compressor_type']:9} | {comp['refrigerant_type']:6} | "
              f"{comp['cooling_capacity_kw']:13.1f}")

def display_refrigerants(refrigerants):
    """Отображает информацию о фреонах"""
    print("\n  Фреон | Формула       | Плотность (кг/м³) | Крит. темп. (°C)")
    print("--------+---------------+-------------------+-----------------")
    for ref in refrigerants:
        print(f"  {ref['name']:6} | {ref['chemical_formula']:13} | "
              f"{ref['density_liquid_25c']:17.0f} | {ref['critical_temperature']:15.1f}")

def get_float_input(prompt, min_value=0.1, max_value=100.0):
    """Безопасный ввод чисел с плавающей точкой"""
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Ошибка: значение должно быть от {min_value} до {max_value}")
        except ValueError:
            print("Ошибка: введите число")

def main():
    """Основная функция программы"""
    print("=" * 60)
    print("          ХОЛОДИЛЬНЫЙ КАЛЬКУЛЯТОР v1.0")
    print("=" * 60)
    
    # Инициализация БД и калькулятора
    db = DBCore()
    calculator = ColdCalculator(db)
    
    try:
        # Ввод параметров камеры
        print("\n1. ВВЕДИТЕ ПАРАМЕТРЫ ХОЛОДИЛЬНОЙ КАМЕРЫ")
        print("-" * 40)
        
        length = get_float_input("Длина камеры (м): ", 1.0, 50.0)
        width = get_float_input("Ширина камеры (м): ", 1.0, 30.0)
        height = get_float_input("Высота камеры (м): ", 2.0, 10.0)
        
        print("\nТип камеры:")
        print("1 - Среднетемпературная (-5°C ... +10°C)")
        print("2 - Низкотемпературная (-25°C ... -15°C)")
        
        chamber_choice = input("Выберите тип (1-2): ").strip()
        chamber_type = 'medium_temp' if chamber_choice == '1' else 'low_temp'
        
        ambient_temp = get_float_input("Температура окружающей среды (°C): ", -40.0, 50.0)
        
        # Расчеты
        volume = calculator.calculate_room_volume(length, width, height)
        required_power = calculator.calculate_required_power(volume, chamber_type, ambient_temp)
        
        # Вывод результатов расчета
        print("\n" + "=" * 60)
        print("          РЕЗУЛЬТАТЫ РАСЧЕТА")
        print("=" * 60)
        print(f"Объем камеры: {volume:.1f} м³")
        print(f"Тип камеры: {'Среднетемпературная' if chamber_type == 'medium_temp' else 'Низкотемпературная'}")
        print(f"Температура окружающей среды: {ambient_temp}°C")
        print(f"Расчетная холодильная мощность: {required_power:.1f} кВт")
        
        # Подбор компрессоров
        print(f"\n2. ПОДБОР КОМПРЕССОРОВ (мощность {required_power:.1f} ±30% кВт)")
        print("-" * 60)
        
        compressors = calculator.get_compressors_by_power(required_power)
        display_compressors(compressors)
        
        # Информация о фреонах
        print(f"\n3. ИНФОРМАЦИЯ О ФРЕОНАХ")
        print("-" * 40)
        
        refrigerants = calculator.get_refrigerants_info()
        display_refrigerants(refrigerants)
        
        # Расчет массы фреона (если выбран компрессор)
        if compressors:
            try:
                comp_choice = int(input("\nВыберите номер компрессора для расчета фреона (0 - пропустить): "))
                if 1 <= comp_choice <= len(compressors):
                    selected_comp = compressors[comp_choice-1]
                    line_length = get_float_input("Длина трубопроводов (м) [10]: ", 1.0, 100.0)
                    refrigerant_mass = calculator.calculate_refrigerant_mass(
                        selected_comp['model_name'], line_length
                    )
                    print(f"\n4. РАСЧЕТ МАССЫ ФРЕОНА")
                    print("-" * 40)
                    print(f"Для компрессора {selected_comp['model_name']}:")
                    print(f"Примерная масса заправки: {refrigerant_mass} кг")
            except (ValueError, IndexError):
                print("Расчет фреона пропущен")
        
        # Сохранение результатов
        save = input("\nСохранить результаты в файл? (y/n): ").lower()
        if save == 'y':
            with open('расчет_холода.txt', 'w', encoding='utf-8') as f:
                f.write("РЕЗУЛЬТАТЫ РАСЧЕТА ХОЛОДИЛЬНОЙ СИСТЕМЫ\n")
                f.write("=" * 50 + "\n")
                f.write(f"Объем камеры: {volume:.1f} м³\n")
                f.write(f"Тип камеры: {'Среднетемпературная' if chamber_type == 'medium_temp' else 'Низкотемпературная'}\n")
                f.write(f"Требуемая мощность: {required_power:.1f} кВт\n\n")
                f.write("ПОДОБРАННЫЕ КОМПРЕССОРЫ:\n")
                for comp in compressors:
                    f.write(f"- {comp['manufacturer']} {comp['model_name']}: {comp['cooling_capacity_kw']} кВт\n")
            print("Результаты сохранены в файл 'расчет_холода.txt'")
            
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
    finally:
        db.close_connection()
        print("\nРабота программы завершена. Нажмите Enter для выхода...")
        input()

if __name__ == "__main__":
    main()
