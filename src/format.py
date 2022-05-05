from datetime import datetime
import re

re_employee_name = '[A-Za-z]+'
re_day = '(MO|TU|WE|TH|FR|SA|SU)'
re_hour = '(([0-1][0-9]|2[0-3]):[0-5][0-9])'
re_time_worked = f'{re_hour}-{re_hour}'
re_workday = f'{re_day}{re_time_worked}'
re_employee_workday = f'^{re_employee_name}={re_workday}(,{re_workday})*$'


def format_input_checking(working_days):
    if(re.match(re_employee_workday, working_days)):
        matches = re.finditer(re_time_worked, working_days)
        for match in matches:
            if(not match.group(1) < match.group(3)):
                raise ValueError(f"({match.group(1)}) begging time cannot be equal or greater than ({match.group(3)})")

    else:
        raise Exception("Invalid input format")
    
    return True

def format_time_checking(time_string):
    format_time = '%H:%M'
    zero_time = datetime.strptime('00:00', format_time)
    output = datetime.strptime(time_string, format_time) - zero_time
    hours = output.total_seconds() // 3600.00
    return hours
