import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Test for the class Employee"""
    def setUp(self):
        """
        Create an employee for use in all test methods.
        """
        self.jane_doe = Employee("Jane", "Doe", 90_000)

    def test_give_default_raise(self):
        """Test that giving a default raise works properly."""
        self.jane_doe.give_raise()
        self.assertEqual(self.jane_doe.annual_salary, 95_000)

    def test_give_custom_raise(self):
        """Test tht giving a custom raise works properly."""
        self.jane_doe.give_raise(3_579)
        self.assertEqual(self.jane_doe.annual_salary, 93_579)

if __name__ == '__main__':
    unittest.main()
