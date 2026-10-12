from student import Student
from student_manager import StudentManager
from storage import load_students, save_students


manager = StudentManager()

# Load existing students
manager.students = load_students("students.json", Student)

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        python = float(input("Enter Python marks: "))
        mathematics = float(input("Enter Mathematics marks: "))
        communication = float(input("Enter Communication marks: "))

        student = Student(
            name,
            age,
            python,
            mathematics,
            communication
        )

        manager.add_student(student)
        save_students(manager.students, "students.json")
        print("Student added successfully.")

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        name = input("Enter student name: ")
        student = manager.find_student(name)

        if student:
            student.display()
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name: ")
        python = float(input("Enter new Python marks: "))
        mathematics = float(input("Enter new Mathematics marks: "))
        communication = float(input("Enter new Communication marks: "))

        if manager.update_student(
            name,
            python,
            mathematics,
            communication
        ):
            save_students(manager.students, "students.json")
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        name = input("Enter student name: ")

        if manager.delete_student(name):
            save_students(manager.students, "students.json")
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")from student import Studentfrom student_manager import StudentManagerfrom storage import load_students, save_studentsmanager = StudentManager()# Load students from students.jsonmanager.students = load_students("students.json", Student)while True:print("\n===== Student Management System =====")print("1. Add Student")print("2. View Students")print("3. Find Student")print("4. Update Student")print("5. Delete Student")print("6. Exit")choice = input("Enter your choice: ")if choice == "1":# Read student detailsname = input("Enter student name: ")age = int(input("Enter student age: "))python = float(input("Enter Python marks: "))mathematics = float(input("Enter Mathematics marks: "))communication = float(input("Enter Communication marks: "))# Create a Student objectstudent = Student(name,age,python,mathematics,communication)# Add the student to the managermanager.add_student(student)# Save studentssave_students(manager.students, "students.json")print("Student added successfully.")elif choice == "2":# View studentsmanager.view_students()elif choice == "3":# Read a namename = input("Enter student name: ")# Find the studentstudent = manager.find_student(name)# Display the student if foundif student:student.display()else:print("Student not found.")elif choice == "4":# Read the student name and new marksname = input("Enter student name: ")python = float(input("Enter new Python marks: "))mathematics = float(input("Enter new Mathematics marks: "))communication = float(input("Enter new Communication marks: "))# Update the studentif manager.update_student(name,python,mathematics,communication):# Save studentssave_students(manager.students, "students.json")print("Student updated successfully.")else:print("Student not found.")elif choice == "5":# Read the student namename = input("Enter student name: ")# Delete the studentif manager.delete_student(name):# Save studentssave_students(manager.students, "students.json")print("Student deleted successfully.")else:print("Student not found.")elif choice == "6":print("Exiting application.")breakelse:print("Invalid choice.")from student import Student
from student_manager import StudentManager
from storage import load_students, save_students


manager = StudentManager()

# TODO: Load students from students.json


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # TODO: Read student details
        # TODO: Create a Student object
        # TODO: Add the student to the manager
        # TODO: Save students
        pass

    elif choice == "2":
        # TODO: View students
        pass

    elif choice == "3":
        # TODO: Read a name
        # TODO: Find the student
        # TODO: Display the student if found
        pass

    elif choice == "4":
        # TODO: Read the student name and new marks
        # TODO: Update the student
        # TODO: Save students
        pass

    elif choice == "5":
        # TODO: Read the student name
        # TODO: Delete the student
        # TODO: Save students
        pass

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")
