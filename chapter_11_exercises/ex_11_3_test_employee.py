import unittest
from ex_11_3_employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """Creating an employee and salary for the test methods"""
        self.new_employee = Employee("Dan", "Farias", 80000)

    def test_give_default_raise(self):
        """Test the default raise works properly"""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 85000)

    def test_give_different_raise(self):
        """Test the default raise works properly"""
        self.new_employee.give_raise(12000)
        self.assertEqual(self.new_employee.salary, 92000)

if __name__ == "__main__":
    unittest.main()