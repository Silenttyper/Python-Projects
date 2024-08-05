class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def add_course(self, course):
        self.courses.append(course)
    
    def add_grade(self, course, grade):
        self.grades[course] = grade

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"

class StudentTrackingSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
    
    def add_course(self, course):
        self.courses.append(course)

    def assign_course_to_student(self, student_id, course_code):
        student = next(s for s in self.students if s.student_id == student_id)
        course = next(c for c in self.courses if c.course_code == course_code)
        student.add_course(course)
    
    def record_grade(self, student_id, course_code, grade):
        student = next(s for s in self.students if s.student_id == student_id)
        student.add_grade(course_code, grade)
    
    def generate_report(self):
        print("Student Performance Report")
        for student in self.students:
            print(f"Student: {student.name} (ID: {student.student_id})")
            for course in student.courses:
                grade = student.grades.get(course.course_code, "N/A")
                print(f"  Course: {course}, Grade: {grade}")

# Example usage
sts = StudentTrackingSystem()

# Adding courses
course1 = Course("Mathematics", "MATH101")
course2 = Course("Science", "SCI101")

sts.add_course(course1)
sts.add_course(course2)

# Adding students
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

sts.add_student(student1)
sts.add_student(student2)

# Assigning courses and recording grades
sts.assign_course_to_student("S001", "MATH101")
sts.assign_course_to_student("S002", "SCI101")

sts.record_grade("S001", "MATH101", 90)
sts.record_grade("S002", "SCI101", 85)

# Generating report
sts.generate_report()
