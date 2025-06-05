class Group:
    def __init__(self, student):
        self.students = [student]  # Инициализация списка с одним студентом
    
    def add_student(self, student):
        self.students.append(student)  # Добавление нового студента
    
    def show_students(self):
        if not self.students:  # Проверка на пустоту списка
            print("Группа пуста")
        else:
            for student in self.students:
                student.display_info()  # Вывод информации о каждом студенте
