class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    
    def display_info(self):
        print(f"Имя: {self.name}, ID: {self.student_id}")


class Group:
    def __init__(self, student):
        self.students = [student]  # Создаём список с первым студентом
    
    def add_student(self, student):
        self.students.append(student)  #  добавление нового студента
