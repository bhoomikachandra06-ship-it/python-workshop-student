class Student:
    """Represent a student."""

    def __init__(self, name, age, python, mathematics, communication):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        total = self.python + self.mathematics + self.communication
        percentage = total / 3
        return percentage

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Python: {self.python}")
        print(f"Mathematics: {self.mathematics}")
        print(f"Communication: {self.communication}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")class Student:"""Represent a student."""def __init__(self, name, age, python, mathematics, communication):# Store the student detailsself.name = nameself.age = ageself.python = pythonself.mathematics = mathematicsself.communication = communicationdef calculate_percentage(self):"""Calculate the student's percentage."""total = self.python + self.mathematics + self.communicationpercentage = total / 3return percentagedef display(self):"""Display the student's details."""print(f"Name: {self.name}")print(f"Age: {self.age}")print(f"Python: {self.python}")print(f"Mathematics: {self.mathematics}")print(f"Communication: {self.communication}")print(f"Percentage: {self.calculate_percentage():.2f}%")class Student:
    """Represent a student."""

    def __init__(self, name, age, python, mathematics, communication):
        # TODO: Store the student details
        pass

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        # TODO: Calculate and return the percentage
        pass

    def display(self):
        """Display the student's details."""
        # TODO: Display all student details
        pass
