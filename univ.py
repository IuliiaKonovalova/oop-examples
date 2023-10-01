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

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

# adding students to the course
student_1 = Student("Jane", 19, 65)
student_2 = Student("Mike", 20, 75)
student_3 = Student("Lily", 19, 95)

# printing students
print('Student 1: ', student_1.name, student_1.age, student_1.grade)
print('Student 2: ', student_2.name, student_2.age, student_2.grade)
print('Student 3: ', student_3.name, student_3.age, student_3.grade)

# adding courses
course_1 = Course("Science", 2)
course_2 = Course("Math", 2)

# printing courses
print('Course 1: ', course_1.name, course_1.max_students)
print('Course 2: ', course_2.name, course_2.max_students)

# adding students to the course
print('Adding students to the course...')
course_1.add_student(student_1)
course_1.add_student(student_2)
print(
    'Students in course 1: ',
    course_1.students[0].name,
    course_1.students[1].name
)
print('Adding student 3 to the course...')
print(course_1.add_student(student_3))

print('Average grade in course 1: ', course_1.get_average_grade())