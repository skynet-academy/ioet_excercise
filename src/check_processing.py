import os
from .format import format_time_checking

MORNING   = (0.01, 9)
AFTERNOON = (9.01, 18)
NIGHT     = (18.01, 24)
WEEKDAYS = ("MO", "TU", "WE", "TH", "FR")
WEEKEND = ("SA", "SU")

def check_extension_exists(file_name) -> bool:
    file_extension = file_name.endswith(".txt")
    if(not file_extension):
        raise ValueError("The file does not have 'txt' extension.")
    return True

def check_file_exists(file_name) -> bool:
    it_exists = os.path.isfile(file_name)
    if(not it_exists):
        raise ValueError("The file does not exists.")
    return True 

def check_working_hours(day_hours) -> int:
    day = day_hours[:2]
    hours = day_hours[2:].split('-')
    total = 0
    start = format_time_checking(hours[0])
    end = format_time_checking(hours[1])
    total_hours = end - start
    if(start >= MORNING[0] and start < MORNING[1]):
        if(end >= MORNING[0] and end < MORNING[1]):
            total = total_hours * (25 if day in WEEKDAYS else 30)
        elif(end >= AFTERNOON[0] and end < AFTERNOON[1]):
            morning = (MORNING[1] - start) * (25 if day in WEEKDAYS else 30)
            afternoon = (end - AFTERNOON[0]) * (15 if day in WEEKDAYS else 20)
            total = morning + afternoon
        elif(end >= NIGHT[0] and end <= NIGHT[1]):
            morning = (MORNING[1] - start) * (25 if day in WEEKDAYS else 30)
            afternoon = (AFTERNOON[0] - MORNING[1]) * (15 if day in WEEKDAYS else 20)
            night =  (end - NIGHT[0]) * (20 if day in WEEKDAYS else 25)
            total = morning + afternoon + night

    elif(start >= AFTERNOON[0] and start <= AFTERNOON[1]):
        if(end >= AFTERNOON[0] and end <= AFTERNOON[1]):
            total = total_hours * (15 if day in WEEKDAYS else 20)
        elif(end >= NIGHT[0] and end <= NIGHT[1]):
            afternoon = (AFTERNOON[1] - MORNING[1]) * (15 if day in WEEKDAYS else 20)
            night =  (end - NIGHT[0]) * (20 if day in WEEKDAYS else 25)
            total = afternoon + night

    elif(start >= NIGHT[0] and start <= NIGHT[1]):
        if(end >= NIGHT[0] and end <= NIGHT[1]):
            total =  total_hours * (20 if day in WEEKDAYS else 25)

    return total

