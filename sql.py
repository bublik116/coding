import sqlite3
import random

conn = sqlite3.connect("university.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS courses")

# Создаем таблицы с полем age в students
cur.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lastname TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

cur.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL,
    course_name TEXT NOT NULL,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
""")

students = [
    ("Иванов", "Александр", 20),
    ("Петрова", "Мария", 21),
    ("Сидоров", "Дмитрий", 22),
    ("Козлова", "Анна", 19),
    ("Николаев", "Иван", 23),
    ("Волкова", "Екатерина", 20),
    ("Павлов", "Михаил", 21),
    ("Орлова", "Ольга", 24),
    ("Федоров", "Сергей", 19),
    ("Захарова", "Наталья", 22),
    ("Алексеев", "Андрей", 20),
    ("Смирнова", "Виктория", 21),
    ("Лебедев", "Артем", 23),
    ("Новикова", "Юлия", 19),
    ("Кузнецов", "Павел", 22),
    ("Васнецова", "Ирина", 20),
    ("Соколов", "Николай", 21),
    ("Морозова", "Елена", 24),
    ("Попов", "Алексей", 19),
    ("Романова", "Светлана", 22)
]

courses = [
    ("PY101", "Основы программирования на Python"),
    ("PY201", "Python для анализа данных"),
    ("PY301", "Веб-разработка на Django"),
    ("PY401", "Машинное обучение на Python"),
    ("PY501", "Автоматизация задач с помощью Python")
]

# Добавляем студентов с возрастом
cur.executemany("INSERT INTO students (name, lastname, age) VALUES (?, ?, ?)", students)

# Добавляем курсы со случайными student_id
student_ids = [i for i in range(1, len(students) + 1)]
course_data = []
for course in courses:
    course_data.append((
        course[0],  # course_code
        course[1],  # course_name
        random.choice(student_ids)  # случайный student_id
    ))

cur.executemany("INSERT INTO courses (course_code, course_name, student_id) VALUES (?, ?, ?)", course_data)

conn.commit()

# ЧТЕНИЕ ДАННЫХ ИЗ БАЗЫ
print("=== АНАЛИЗ ДАННЫХ УНИВЕРСИТЕТА ===\n")

# 1. Средний возраст студентов
cur.execute("SELECT AVG(age) FROM students")
average_age = cur.fetchone()[0]
print(f"Средний возраст студентов: {average_age:.1f} лет\n")

# 2. Количество студентов на каждом курсе
cur.execute("""
    SELECT c.course_name, COUNT(c.student_id) as student_count
    FROM courses c
    GROUP BY c.course_name
    ORDER BY student_count DESC
""")

course_stats = cur.fetchall()
print("Количество студентов по курсам:")
print("-" * 40)
for course_name, count in course_stats:
    print(f"{course_name}: {count} студент(ов)")

# 3. Дополнительная статистика
print("\n" + "=" * 40)
cur.execute("SELECT COUNT(*) FROM students")
total_students = cur.fetchone()[0]
print(f"Общее количество студентов: {total_students}")

cur.execute("SELECT MIN(age), MAX(age) FROM students")
min_age, max_age = cur.fetchone()
print(f"Возрастной диапазон: от {min_age} до {max_age} лет")

conn.close()
