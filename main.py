import argparse
import os
import textwrap
from employee import Employee

parser = argparse.ArgumentParser(
        description = "Returns the employee's payout",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        This program accepts two arguments that are mutually exclusive
        '-f' argument receives a file that will be read to calculate 
               the employees' payout.
        '-t' argument receives a text between double quotes to calculate
               the employee's payout.
        
        Example:
            # Reads from file
            $ python3 main.py -f 'test_cases.txt'

            # Single test case separated by comma.
            $ python3 main.py -t 'RENE=MO10:00-12:00,TU10:00-12:00'

            # Get more information
            $ python3 main.py -h
            '''))
parser.add_argument(
        '-f',
        '--file',
        help="read test cases from file with extension '.txt'"
        )

parser.add_argument(
        '-t',
        '--text',
        type=str,
        help='execute specified command'
        )


if __name__ == '__main__':
    args = parser.parse_args()
    if(args.text is None and args.file):
        # Getting the file path
        file_name = args.file   
        # Checking if it exists
        file_exists = os.path.exists(file_name)
        # checking out the extension
        if(file_name.endswith('.txt') and file_exists):
            try:
                with open(file_name) as cases:
                    for case in cases:
                        # removing the extra space and spliting by the symbol
                        # '='
                        name, days_hours = case.strip().split('=')
                        person = Employee(name, days_hours)
                        payout = person.get_payout()
                        print(f"The amount to pay {name} is: {payout} USD")
            except:
                print("Failed to read the file.")
        else:
            raise Exception("It doesn't have '.txt' extension or doesn't exist.")

    elif(args.file is None and args.text):
        # checking if it's a string
        string = args.text
        is_string = isinstance(args.text, str)
        if(is_string):
            try:
                # spliting by the symbol '='
                name, days_hours = string.split('=')
                person = Employee(name, days_hours)
                payout = person.get_payout()
                print(f"The amount to pay {name} is: {payout} USD")
            except:
                print("This string failed to get employee's payout.")
        else:
            raise Exception("The argument that you passed is not a string.")
    else:
        print("Invalid argument. Run 'python3 main.py -h' to get more info.")

