from datetime import datetime
import re

re_employee_name = '[A-Za-z]+'
re_day = '(MO|TU|WE|TH|FR|SA|SU)'
re_hour = '(([0-1][0-9]|2[0-3]):[0-5][0-9])'
re_time_worked = f'{re_hour}-{re_hour}'
re_workday = f'{re_day}{re_time_worked}'
re_employee_workday = f'^{re_employee_name}={re_workday}(,{re_workday})*$'


def format_input_checking(working_days) -> bool:
    if(re.match(re_employee_workday, working_days)):
        matches = re.finditer(re_time_worked, working_days)
        for match in matches:
            start = match.group(1)
            end = '24:00' if match.group(3) == '00:00' else match.group(3)
            if(not start < end):
                raise ValueError(f"({start}) begging time cannot be equal or greater than ({end})")

    else:
        raise Exception("Invalid input format")
    
    return True

def format_time_checking(time_string) -> int:
    format_time = '%H:%M'
    zero_time = datetime.strptime('00:00', format_time)
    output = datetime.strptime(time_string, format_time) - zero_time
    hours = 0
    if(output.total_seconds() == 0.0):
        hours = 24.00
    else:
        hours = output.total_seconds() / 3600
    return hours
