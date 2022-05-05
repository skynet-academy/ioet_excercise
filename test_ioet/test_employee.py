import unittest
from src.employee import Employee
from src.format import format_time_checking, format_input_checking
from src.check_processing import (
                                check_working_hours, 
                                check_extension_exists,
                                check_file_exists
                                )

CASE = "NICOLAS=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00"

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_user = Employee(case=CASE)

    def test_employee_payout_returns_a_float(self):
        """Whether payout method returns a float value"""
        total_salary = self.employee_user.get_payout_string()
        self.assertNotIsInstance(total_salary, float)

    def test_employee_payout_returns_not_int(self):
        """Whether payout method returns a not int value"""
        total_salary = self.employee_user.get_payout_string()
        self.assertNotIsInstance(total_salary, int)

    def test_employee_payout_returns_not_string(self):
        """Whether payout method returns a not a string value"""
        total_salary = self.employee_user.get_payout_string()
        self.assertIsInstance(total_salary, str)

    def test_employee_payout_in_hours_range_week_days_returns_float(self):
        """"""
        days_hours = CASE.split('=')[1].split(',')
        total_payout = self.employee_user.process_hours(days_hours)
        self.assertIsInstance(total_payout, float)

    def test_employee_payout_expected_result(self):
        expected_result ="The amount to pay NICOLAS is: 190.0 USD"
        total_payout = self.employee_user.get_payout_string()
        self.assertEqual(expected_result, total_payout)

    def test_employee_file_extension(self):
        file_test = '../src/example.txt'
        exists = check_file_exists(file_test)
        self.assertEqual(exists, True)

    def test_employee_file_exists(self):
        file_test = '../src/example.txt'
        extension = check_extension_exists(file_test)
        self.assertEqual(extension, True)






