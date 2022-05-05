import argparse
import os
import textwrap

from src.employee import Employee
from src.check_processing import check_extension_and_exists
from src.format import format_input_checking

parser = argparse.ArgumentParser(
        description = "Returns the employee's payout",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        This program accepts two arguments that are mutually exclusive
        '-f' argument receives a file that will be read to calculate 
               the employees' payout.
        
        Example:
            # Reads from file and it accepts the following type of inputs:
            $ python3 main.py -f 'test_cases.txt'

            $ python3 main.py -f test_cases.txt

            $ python3 main.py -f='test_cases.txt'

            # Get more information
            $ python3 main.py -h
            '''))
parser.add_argument(
        '-f',
        '--file',
        help="read test cases from file with extension '.txt'"
        )

args = parser.parse_args()

if __name__ == '__main__':
    file_exists = check_extension_and_exists(args.file)
    if(file_exists):
        with open(f'{args.file}') as file_cases:
            for case in file_cases:
                right_format = format_input_checking(case)
                if(right_format):
                    employee = Employee(case)
                    print(employee.get_payout_string())
