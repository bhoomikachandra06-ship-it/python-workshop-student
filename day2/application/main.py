from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
from student_api import get_user_details


manager = StudentManager()

# Load students from students.json
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

            user_id = input("Enter user ID for API details: ")
            details = get_user_details(user_id)

            if details:
                print("\n--- Additional Information ---")
                print("Username:", details["username"])
                print("Phone:", details["phone"])
                print("Website:", details["website"])
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
        print("Invalid choice.")from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
from student_api import get_user_details


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
        # TODO: Add the student
        # TODO: Save students
        pass

    elif choice == "2":
        # TODO: View students
        pass

    elif choice == "3":
        # TODO: Read student name
        # TODO: Find the student

        # TODO: If the student is found:
        #       - Display the student
        #       - Call get_user_details()
        #       - Display additional API information
        pass

    elif choice == "4":
        # TODO: Read student name and new marks
        # TODO: Update the student
        # TODO: Save students
        pass

    elif choice == "5":
        # TODO: Read student name
        # TODO: Delete the student
        # TODO: Save students
        pass

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")
