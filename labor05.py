class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {', '.join(map(str, self.grades))}")
        print(f"Average Grade: {self.calculate_average_grade()}\n")

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def display_rating(self):
        sorted_students = sorted(self.students, key=lambda s: s.calculate_average_grade(), reverse=True)
        for student in sorted_students:
            student.display_info()

def main():
    student1 = Student(1, "Arsen", [85, 90, 92])
    student2 = Student(2, "Nazar", [78, 88, 95])
    student3 = Student(3, "Damyan", [92, 89, 94])

    group = Group()

    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    print("------------------------------")

    print("Initial Group Rating:")
    group.display_rating()

    print("------------------------------")

    group.remove_student(2)

    print("\nGroup Rating after removing a student:")
    group.display_rating()

    print("------------------------------")

if __name__ == "__main__":
    main()
