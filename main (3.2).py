def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define a Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
student1 = Student("Alice", "A101", 3.9)
student2 = Student("Bob", "B102", 3.7)
student3 = Student("Charlie", "C103", 4.0)
student4 = Student("David", "D104", 3.8)

student_list = [student1, student2, student3, student4]

sorted_students = sort_students(student_list)

for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
