from datetime import date

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
    """
    Class to represent a cohort,
    it holds name, max_students, students, and specialization
    """
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


class Mentor(Person):
    """
    Class to represent a mentor,
    it holds name, email, specializations, and students
    """
    def __init__(self, name, email):
        super().__init__(name, email)
        self.specializations = []
        self.students = []

    def add_specialization(self, spec):
        self.specializations.append(spec)

    def show_mentor_specializations(self):
        specs_names = []
        for spec in self.specializations:
            specs_names.append(spec.name)
        print('All Specs: ', specs_names)

    def add_student(self, student):
        self.students.append(student)

    def show_mentor_students(self):
        students_names = []
        for student in self.students:
            students_names.append(student.name)
        print('All students: ', students_names)


class Student(Person):
    """
    Class to represent a student,
    it holds name, email, age, grade, and projects
    """
    def __init__(self, name, email, age):
        super().__init__(name, email)
        self.age = age
        self.grade = 0
        self.projects = []

    def get_grade(self):
        return self.grade

    def update_total_score(self):
        self.grade = sum(project.grade for project in self.projects)

    def check_deadline(self):
        deadlines = []
        counter = 1
        if len(self.projects) <= 0:
            print('Deadlines: not set yet')
        else:
            for project in self.projects:
                deadlines.append(f"Project {counter}: {project.deadline}")
                counter + 1
            print('Deadlines: ', deadlines)

    def check_closest_deadline(self):
        deadlines = []
        counter = 1
        if len(self.projects) <= 0:
            print('Deadlines: not set yet')
        else:
            for project in self.projects:
                deadlines.append(project.deadline)
                counter + 1
            deadlines_objects = [
                date.fromisoformat(date_str) for date_str in deadlines
            ]
            today = date.today()
            date_differences = [abs(today - d) for d in deadlines_objects]
            closest_date_index = date_differences.index(min(date_differences))

            closest_date = deadlines[closest_date_index]
            print(
                f"""
Closest deadline is {closest_date}. It's {
    self.projects[closest_date_index].project_number
} project
                """
            )

    def find_deadline_for_project(self, num):
        if len(self.projects) <= 0:
            print('Deadlines: not set yet')
        else:
            print(
                f"""
Project {num}'s deadline is {self.projects[num - 1].deadline}
                """
            )

class Project:
    """
    Class to represent a project,
    it holds name, project_number, github_link, deadline,
    grade, deployed_link, and creator
    """
    def __init__ (
        self,
        name,
        project_number,
        github_link,
        deadline,
        grade=0,
        deployed_link="Not Deployed",
        creator=None,
    ):
        self.name = name
        self.project_number = project_number
        self.github_link = github_link
        self.deployed_link = deployed_link
        self.deadline = deadline
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
        "2023-05-23",
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
        "JD-1-project",
        1,
        "https://github.com/JD-1-project",
        "2023-05-23",
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

    project_2 = Project(
        "JD-2-project",
        2,
        "https://github.com/JD-2-project",
        "2023-07-23",
        90,
        "https://JD-2-project.com",
        student_1
    )
    print(
        'Project 2: ',
        project_2.name,
        project_2.project_number,
        project_2.github_link,
        project_2.deployed_link,
        project_2.grade,
        project_2.creator.name
    )
    print('Student 1 Projects: ', student_1.projects)

    student_1.projects.append(project_2)

    print('Student 1 Projects after appending: ', student_1.projects)
    print('Student 1 Projects after appending: ', student_1.projects[1].name)

    project_3 = Project(
        "JD-3-project",
        3,
        "https://github.com/JD-3-project",
        "2023-10-23",
        90,
        "https://JD-3-project.com",
        student_1
    )
    print(
        'Project 3: ',
        project_3.name,
        project_3.project_number,
        project_3.github_link,
        project_3.deployed_link,
        project_3.grade,
        project_3.creator.name
    )
    print('Student 1 Projects: ', student_1.projects)

    student_1.projects.append(project_3)

    print('Student 1 Projects after appending: ', student_1.projects)
    print('Student 1 Projects after appending: ', student_1.projects[1].name)


    student_1.check_deadline()
    student_2.check_deadline()
    student_1.check_closest_deadline()
    student_2.check_closest_deadline()
    student_1.find_deadline_for_project(1)
    student_1.find_deadline_for_project(2)
    student_1.find_deadline_for_project(3)


def create_mentors():
    """ Create mentors objects out of Mentor class """
    mentor_1 = Mentor('Julia Konn', 'julia@gmail.com')
    mentor_2 = Mentor('Alex Konn', 'alex@gmail.com')
    print('Mentor 1: ', mentor_1.name, mentor_1.email)
    print('Mentor 2: ', mentor_2.name, mentor_2.email)

    # create specializations
    spec_1 = Specialization("Advanced Front End")
    spec_2 = Specialization("E-commerce")
    spec_3 = Specialization("Predictive Analytics")
    print('Spec 1: ', spec_1.name)
    print('Spec 1: ', spec_2.name)
    print('Spec 1: ', spec_3.name)

    # Add specs to the mentors:
    mentor_1.add_specialization(spec_1)
    mentor_1.add_specialization(spec_2)
    mentor_2.add_specialization(spec_1)
    mentor_2.add_specialization(spec_2)
    mentor_2.add_specialization(spec_3)
    print(mentor_1.name)
    mentor_1.show_mentor_specializations()
    print(mentor_2.name)
    mentor_2.show_mentor_specializations()

    # add student to the mentor
    student_1 = Student("John Doe", "john@example.com", 19)
    print('Student 1: ', student_1.name, student_1.email, student_1.age)
    student_2 = Student("Rachel Smith", "rachel@gmail.com", 20)
    print('Student 2: ', student_2.name, student_2.email, student_2.age)

    mentor_1.add_student(student_1)
    print(mentor_1.students[0].name)
    mentor_1.show_mentor_students()
    mentor_1.add_student(student_2)
    print(mentor_1.students[1].name)
    mentor_1.show_mentor_students()



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
    create_mentors()
    print(
        f"""
        {'-'*50}
        """
    )


if __name__ == "__main__":
    main()
