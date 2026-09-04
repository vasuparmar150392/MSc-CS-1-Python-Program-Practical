print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 19: Demonstrate various types of Methods")
print("-" * 50)

class Student:
    # Class Variable / Attribute
    university_name = "Marwadi University"
    total_students = 0

    def __init__(self, name, enrollment_no, marks):
        # Instance Variables
        self.name = name
        self.enrollment_no = enrollment_no
        self.marks = marks
        Student.total_students += 1

    # 1. Instance Method
    # Takes 'self' as the first parameter; can access and modify instance attributes
    def display_student_details(self):
        print(f"   Student Name  : {self.name}")
        print(f"   Enrollment No : {self.enrollment_no}")
        print(f"   Marks         : {self.marks}")
        print(f"   University    : {self.university_name}")

    # 2. Class Method
    # Takes 'cls' as the first parameter; decorated with @classmethod; can access/modify class variables
    @classmethod
    def get_university_info(cls):
        print(f"   [Class Method] University Name: {cls.university_name}")
        print(f"   [Class Method] Total Students Registered: {cls.total_students}")

    @classmethod
    def change_university_name(cls, new_name):
        cls.university_name = new_name
        print(f"   [Class Method] University name updated to: {cls.university_name}")

    # 3. Static Method
    # Does not take 'self' or 'cls'; decorated with @staticmethod; acts as a utility function
    @staticmethod
    def evaluate_result(marks):
        if marks >= 40:
            return "Pass"
        else:
            return "Fail"

    @staticmethod
    def is_valid_enrollment(enrollment_no):
        return len(str(enrollment_no)) > 0


# Creating Objects
student1 = Student("Vasu Parmar", "92600565007", 85)
student2 = Student("Rahul Patel", "MU2026007", 35)

print("1. Calling Instance Methods:")
print("--- Student 1 ---")
student1.display_student_details()
print("--- Student 2 ---")
student2.display_student_details()

print("\n2. Calling Class Methods:")
Student.get_university_info()

print("\n3. Calling Static Methods (Utility functions):")
print(f"   Student 1 ({student1.name}) Result: {Student.evaluate_result(student1.marks)}")
print(f"   Student 2 ({student2.name}) Result: {Student.evaluate_result(student2.marks)}")
print(f"   Is Enrollment Valid? {Student.is_valid_enrollment(student1.enrollment_no)}")
