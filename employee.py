"""Employee

"""

class Employee:
    """
    A class that recieves a string as parameter
    """
    def __init__(self, name, days_hours):
        """Construct all the necesary attributes for the employee"""
        self.name = name
        self.days_hours = days_hours 

        self.weekdays = ["MO", "TU", "WE", "TH", "FR"]
        self.range_weekdays = [
                {'00:01-09:00': 25},
                {'09:01-18:00': 15},
                {'18:01-00:00': 20}
                ]

        self.weekend = ["SA", "SU"]
        self.range_weekend = [
                {'00:01-09:00': 30},
                {'09:01-18:00': 20},
                {'18:01-00:00': 25}
                ]

    def get_payout(self):
        """
        It returns a int number which is the employee's payout
        """
        value = 10.4
        return value

    def get_payout_string(self):
        """
        It returns a string with the following information:

        - The amount to pay [employee] is: [payout] USD
        - where: [employee] is the name of the employee taken from the input
        - where: [payout] is the output of the method 'get_payout'
        """

        return f"The amount to pay {employee} is: {payout} USD"

