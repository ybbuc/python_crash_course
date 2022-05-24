class Employee:
    """A class to represent an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Store the name and salary for an employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount = 5_000):
        """Give an employee a raise to their annual salary."""
        self.annual_salary += amount
