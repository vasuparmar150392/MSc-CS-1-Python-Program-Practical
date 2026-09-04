print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 18: Demonstrate the use of Methods in a Class")
print("-" * 50)

class StudentResult:
    """Class demonstrating methods with parameters, return values, and method chaining."""

    def __init__(self, name, enrollment_no):
        self.name = name
        self.enrollment_no = enrollment_no
        self.marks = []

    # Mutator Method (Setter to input marks)
    def set_marks(self, m1, m2, m3):
        self.marks = [m1, m2, m3]

    # Method with Return Value (Calculate total marks)
    def calculate_total(self):
        return sum(self.marks)

    # Method with Return Value (Calculate percentage)
    def calculate_percentage(self):
        total = self.calculate_total()
        return total / len(self.marks) if self.marks else 0

    # Method with Return Value (Calculate grade based on percentage)
    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 80:
            return "Distinction (A+)"
        elif percentage >= 60:
            return "First Class (A)"
        elif percentage >= 40:
            return "Pass Class (B)"
        else:
            return "Fail"

    # Display Method (Calls other internal methods)
    def display_report_card(self):
        print(f"\n--- Report Card: {self.name} ---")
        print(f"Enrollment No : {self.enrollment_no}")
        print(f"Subject Marks : {self.marks}")
        print(f"Total Marks   : {self.calculate_total()} / {len(self.marks) * 100}")
        print(f"Percentage    : {self.calculate_percentage():.2f}%")
        print(f"Grade Awarded : {self.calculate_grade()}")


# Creating an object of StudentResult
student1 = StudentResult("Vasu Parmar", "92600565007")
student1.set_marks(85, 90, 88)
student1.display_report_card()

# Creating a second student object
student2 = StudentResult("Naeem Sheikh", "MU2026002")
student2.set_marks(72, 65, 78)
student2.display_report_card()
