print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 6: Demonstrate the use of Class and Objects")
print("-" * 50)

class Student:
    """This class demonstrates the definition of a Class, constructor, attributes, and methods in Python."""
    
    # Class Attribute (shared by all instances)
    college = "Marwadi University"

    # Constructor (__init__ method to initialize instance attributes)
    def __init__(self, name, enrollment_no, department):
        self.name = name                      # Instance attribute
        self.enrollment_no = enrollment_no    # Instance attribute
        self.department = department          # Instance attribute

    # Instance Method
    def display_details(self):
        print(f"   Name          : {self.name}")
        print(f"   Enrollment No : {self.enrollment_no}")
        print(f"   Department    : {self.department}")
        print(f"   College       : {self.college}")

    # Another Method
    def welcome_message(self):
        print(f"   Welcome {self.name} to the {self.department} department!")


# Printing Class Docstring
print("Class Documentation (__doc__):")
print("  ", Student.__doc__)
print("-" * 50)

# Creating Objects (Instances) of the Student class
print("Creating Object 1:")
student1 = Student("Vasu Parmar", "92600565007", "MSc Cyber Security")
student1.display_details()
student1.welcome_message()

print("\nCreating Object 2:")
student2 = Student("Rahul Patel", "MU2026007", "Faculty of Computer Applications")
student2.display_details()
student2.welcome_message()
