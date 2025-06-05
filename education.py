class Student:
    def __init__(self, name, student_id):
        self.__name = name          # Приватный атрибут
        self.__student_id = student_id  # Приватный атрибут
        self.__grades = []          # Приватный атрибут
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__student_id
    
    def get_grades(self):
        return self.__grades
    
    
    def display_info(self):
        print(f"Имя: {self.__name}, ID: {self.__student_id}")
    
    def add_grade(self, grade):
        self.__grades.append(grade)
    
    def get_average(self):
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0


class Group:
    def __init__(self, student):
        self.__students = [student]  # Приватный атрибут
    
    def find_by_name(self, name):
        for student in self.__students:
            if student.get_name() == name:
                student.display_info()
                return
        print("Студент не найден")
    
    def remove_student_by_id(self, student_id):
        for i, student in enumerate(self.__students):
            if student.get_id() == student_id:
                del self.__students[i]
                print(f"Студент с ID {student_id} удалён")
                return
        print(f"Студент с ID {student_id} не найден")    
    
    def get_students(self):
        return self.__students
    
    def add_student(self, student):
        self.__students.append(student)
    
    def show_students(self):
        if not self.__students:
            print("Группа пуста")
        else:
            for student in self.__students:
                student.display_info()
