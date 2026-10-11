import jsondef save_students(students, filename):"""Save students to a JSON file."""# Convert students into dictionariesdata = []for student in students:data.append({"name": student.name,"age": student.age,"python": student.python,"mathematics": student.mathematics,"communication": student.communication})# Save the data using json.dump()with open(filename, "w") as file:json.dump(data, file, indent=4)def load_students(filename, student_class):"""Load students from a JSON file."""try:# Open and read the JSON filewith open(filename, "r") as file:data = json.load(file)# Convert dictionaries back into Student objectsstudents = []for student_data in data:student = student_class(student_data["name"],student_data["age"],student_data["python"],student_data["mathematics"],student_data["communication"])students.append(student)return studentsexcept FileNotFoundError:return []except json.JSONDecodeError:print("Error: Invalid JSON file.")return []import json


def save_students(students, filename):
    """Save students to a JSON file."""
    # TODO: Convert students into dictionaries
    # TODO: Save the data using json.dump()
    pass


def load_students(filename, student_class):
    """Load students from a JSON file."""
    # TODO: Open and read the JSON file
    # TODO: Handle FileNotFoundError
    # TODO: Handle JSONDecodeError
    # TODO: Convert dictionaries back into Student objects
    pass
