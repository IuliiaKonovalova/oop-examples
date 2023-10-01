""" Structure of the Code Institute """
class Specialization:
    """ A class to represent a specialization """
    def __init__(self, name):
        self.name = name


class Course:
    """
    A class to represent a course
    it holds name, max_students, students, and specialization
    If specialization is not specified, it defaults to "Not Specified"
    """
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
        if len(self.students) == 0:
            return 0
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


class Person:
    """A class to represent a person"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name


class Student(Person):
    def __init__(self, name, email, age):
        super().__init__(name, email)
        self.age = age
        self.grade = 0
        self.projects = []

    def get_grade(self):
        return self.grade

    def update_total_score(self):
        self.grade = sum(project.grade for project in self.projects)


class Project:
    def __init__ (
        self,
        name,
        project_number,
        github_link,
        grade=0,
        deployed_link="Not Deployed",
        creator=None
    ):
        self.name = name
        self.project_number = project_number
        self.github_link = github_link
        self.deployed_link = deployed_link
        self.grade = grade
        self.creator = creator


def creating_students():
    """ Creating students """
    student_1 = Student("John Doe", "john@example.com", 19)
    print('Student 1: ', student_1.name, student_1.email, student_1.age)

    student_2 = Student("Rachel Smith", "rachel@gmail.com", 20)
    print('Student 2: ', student_2.name, student_2.email, student_2.age)


def creating_students_with_projects():
    """ Creating students with projects """
    student_1 = Student("John Doe", "john@example.com", 19)
    print('Student 1: ', student_1.name, student_1.email, student_1.age)

    student_2 = Student("Rachel Smith", "rachel@gmail.com", 20)
    print('Student 2: ', student_2.name, student_2.email, student_2.age)

    project_1 = Project(
        "JD-1-project",1,
        "https://github.com/JD-1-project",
        90,
        "https://JD-1-project.com",
        student_1
    )
    print(
        'Project 1: ',
        project_1.name,
        project_1.project_number,
        project_1.github_link,
        project_1.deployed_link,
        project_1.grade,
        project_1.creator.name
    )
    print('Student 1 Projects: ', student_1.projects)

    student_1.projects.append(project_1)

    print('Student 1 Projects after appending: ', student_1.projects)
    print('Student 1 Projects after appending: ', student_1.projects[0].name)


def creating_students_with_projects_and_grades():
    """ Creating students with projects and grades """
    student_1 = Student("John Doe", "john@example.com", 19)
    print('Student 1: ', student_1.name, student_1.email, student_1.age)

    student_2 = Student("Rachel Smith", "rachel@gmail.com", 20)
    print('Student 2: ', student_2.name, student_2.email, student_2.age)

    project_1 = Project(
        "JD-1-project",1,
        "https://github.com/JD-1-project",
        90,
        "https://JD-1-project.com",
        student_1
    )
    print(
        'Project 1: ',
        project_1.name,
        project_1.project_number,
        project_1.github_link,
        project_1.deployed_link,
        project_1.grade,
        project_1.creator.name
    )
    print('Student 1 Projects: ', student_1.projects)

    student_1.projects.append(project_1)

    print('Student 1 Projects after appending: ', student_1.projects)
    print('Student 1 Projects after appending: ', student_1.projects[0].name)

    print('Student 1 Grade before updating: ', student_1.grade)
    student_1.update_total_score()
    print('Student 1 Grade after updating: ', student_1.grade)


def main():
    print(
        f"""
        {'-'*50}
        """
    )
    creating_students()
    print(
        f"""
        {'-'*50}
        """
    )
    creating_students_with_projects()
    print(
        f"""
        {'-'*50}
        """
    )
    creating_students_with_projects_and_grades()
    print(
        f"""
        {'-'*50}
        """
    )


if __name__ == "__main__":
    main()