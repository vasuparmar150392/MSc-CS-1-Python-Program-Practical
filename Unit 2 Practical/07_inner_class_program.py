print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 17: Demonstrate the concept of Inner Class")
print("-" * 50)

# Outer Class
class University:
    def __init__(self, university_name, city):
        self.university_name = university_name
        self.city = city

    def display_university_info(self):
        print(f"University Name : {self.university_name}")
        print(f"City            : {self.city}")

    # Inner Class (Class defined inside another class)
    class Student:
        def __init__(self, name, enrollment_no, department):
            self.name = name
            self.enrollment_no = enrollment_no
            self.department = department

        def display_student_info(self):
            print(f"Student Name    : {self.name}")
            print(f"Enrollment No   : {self.enrollment_no}")
            print(f"Department      : {self.department}")


# Creating an object of the Outer Class
univ = University("Marwadi University", "Rajkot")
print("--- Outer Class Details ---")
univ.display_university_info()

print("\n--- Inner Class Details (Created via Outer Class Instance) ---")
# Creating an object of the Inner Class using the Outer Class instance
student1 = univ.Student("Vasu Parmar", "92600565007", "MSc Cyber Security")
student1.display_student_info()

print("\n--- Inner Class Details (Direct Outer.Inner Instantiation) ---")
# Direct instantiation of the Inner class
student2 = University.Student("Rahul Patel", "MU2026007", "Faculty of Computer Applications")
student2.display_student_info()
