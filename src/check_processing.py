import os
from .format import format_time_checking

FIRST_START  = '00:01'
FIRST_END    = '09:00'
SECOND_START = '09:01'
SECOND_END   = '18:00'
THIRD_START  = '18:01'
THID_END     = '00:00'
WEEKDAYS = ["MO", "TU", "WE", "TH", "FR"]
WEEKEND = ["SA", "SU"]

def check_extension_and_exists(file_name):
    it_exists = os.path.isfile(file_name)
    file_extension = file_name.endswith(".txt")
    if(not it_exists):
        raise ValueError("The file does not exists.")
    if(not file_extension):
        raise ValueError("The file does not have 'txt' extension.")
     
    return True 

def check_working_hours(day_hours):
    day = day_hours[:2]
    hours = day_hours[2:].split('-')
    total = 0
    if(day in WEEKDAYS):
        print('Weekday', day, hours)
    elif(day in WEEKEND):
        print('Weekend', day, hours)


    return day_hours

