class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Student Details:\nName: {self.name}\nRoll Number: {self.roll_no}\nMarks: {self.marks}")

if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student = Student(name, roll_no, marks)
    student.display_details()