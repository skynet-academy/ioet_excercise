import unittest
from employee import Employee

NAME: str = "NICOLAS"
DAYS_HOURS: str = "MO10:00-12:00,\
                   TU10:00-12:00,\
                   TH01:00-03:00,\
                   SA14:00-18:00,\
                   SU20:00-21:00"

class TestEmployee(unittest.TestCase):
    def set_up(self):
        self.employee_user = Employee(NAME, DAYS_HOURS)

    def test_employee_payout_returns_a_float(self):
        """Whether payout method returns a float value"""
        total_salary = self.employee_user.get_payout()
        self.assertNotIsInstance(total_salary, float)

    def test_employee_payout_returns_not_int(self):
        """Whether payout method returns a not int value"""
        total_salary = self.employee_user.get_payout()
        self.assertIsInstance(total_salary, int)

    def test_employee_payout_returns_not_string(self):
        """Whether payout method returns a not a string value"""
        total_salary = self.employee_user.get_payout()
        self.assertNotIsInstance(total_salary, str)

    def test_employee_payout_not_in_hours_range_week_days(self):
        """"""
        total_salary = employee_user.get_payout()
        output = employee_user.get_payout_string()

    def test_employee_payout_not_in_hours_range_weekend(self):
        pass
