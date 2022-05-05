from .check_processing import check_working_hours

class Employee:
    """
    A class that recieves a string as parameter
    """
    def __init__(self, case):
        """Construct all the necesary attributes for the employee"""
        self.case = case
        self.name = case.split('=')[0]


    def get_payout_string(self) -> str:
        """
        It returns a int number which is the employee's payout
        """
        name = self.case.split('=')[0]
        # taking away '\n', spliting by the symbol '=', and ',' 
        # to generate a list of days - hours
        days_hours = self.case.strip().split('=')[1].split(',')
        amount = self.process_hours(days_hours)
        return f'The amount to pay {name} is: {amount} USD'

    def process_hours(self, days_hours) -> float:
        """
        It process the hours and amount to pay to the employee and returns
        the total payout
        """
        # The next line returns a list with the amount per day 
        # that the employee should receive
        payout = [check_working_hours(day_hours) for day_hours in days_hours]
        # sum of the list
        total_payout = sum(payout)
        return total_payout

    def __str__(self):
        return f'Employee: {self.name}'


