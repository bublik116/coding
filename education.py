class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # Добавлен пустой список для оценок
    
    def display_info(self):
        print(f"Имя: {self.name}, ID: {self.student_id}")
    
    def add_grade(self, grade):  # Новый метод добавления оценки
        self.grades.append(grade)
    
    def get_average(self):  # Новый метод расчёта средней оценки
        return sum(self.grades) / len(self.grades) if self.grades else 0


class Group:
    def __init__(self, student):
        self.students = [student]
    
    def add_student(self, student):
        self.students.append(student)
    
    def show_students(self):
        if not self.students:
            print("Группа пуста")
        else:
            for student in self.students:
                student.display_info()
