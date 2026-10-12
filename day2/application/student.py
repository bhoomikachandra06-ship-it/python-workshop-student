import requests


def get_user_details(user_id):
    """Fetch user details from the external API."""

    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}"
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        return Noneclass Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        total = self.python + self.mathematics + self.communication

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())
