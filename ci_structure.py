class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name


class Specialization:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(
        self,
        name,
        max_students,
        specialization="Not Specified"
    ):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.specialization = Specialization(specialization)

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False




class Cohort:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)




class Student(Person):
    def __init__(self, name, email, age, grade):
        super().__init__(name, email)
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


