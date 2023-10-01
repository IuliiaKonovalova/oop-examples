class Student:
    """
    Student class that holds name, age, and grade
    of a student.
    """
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    """
    Course class that holds name, max_students, and
    students of a course.
    """
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []