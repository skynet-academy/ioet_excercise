from .check_processing import check_working_hours

class Employee:
    """
    A class that recieves a string as parameter
    """
    def __init__(self, case):
        """Construct all the necesary attributes for the employee"""
        self.case = case


    def get_payout_string(self):
        """
        It returns a int number which is the employee's payout
        """
        name = self.case.split('=')[0]
        # taking away '\n', spliting by the symbol '=', and ',' 
        # to generate a list of days - hours
        days_hours = self.case.strip().split('=')[1].split(',')
        payout = self.process_hours(days_hours)
        return f'The amount to pay {name} is: {payout} USD'

    def process_hours(self, days_hours):

        payout = [check_working_hours(day_hours) for day_hours in days_hours]
        #payout = sum(payout)
        return payout



