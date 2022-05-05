# ioet-code-exercise

## This project is made based in the requirements of the task sent by email
### Description:

---

The company ACME offers their employees the flexibility to work the hours they 
want. They will pay for the hours worked based on the day of the week and time
 of day, according to the following table:

<strong>Monday - Friday</strong>
<p>00:01 - 09:00 25 USD</p>
<p>09:01 - 18:00 15 USD</p>
<p>18:01 - 00:00 20 USD</p>

<strong>Saturday and Sunday</strong>
<p>00:01 - 09:00 30 USD</p>
<p>09:01 - 18:00 20 USD</p>
<p>18:01 - 00:00 25 USD</p>

---

### Goal of this exercise

The goal of this exercise is to calculate the total that the company has to pay
an employee, based on the hours they worked and the times during which 
they worked. The following abbreviations will be used for entering data:

<p>MO: Monday</p>
<p>TU: Tuesday</p>
<p>WE: Wednesday</p>
<p>TH: Thursday</p>
<p>FR: Friday</p>
<p>SA: Saturday</p>
<p>SU: Sunday</p>

--- 

### Input of the program

The name of an employee and the schedule they worked, indicating the time 
and hours. This should be a .txt file with at least five sets of data. 
You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

#### Case 1:

---

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:
The amount to pay RENE is: 215 USD

#### Case 2:

---

INPUT
<p>ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00</p>

OUTPUT:
<p>The amount to pay ASTRID is: 85 USD</p>


### Requirements:
- This project is using Python 3.8.10
- Linux system(Ubuntu focal 20.04)

### Project's tree:

```
 |---ioet_excercise
 |       |---src
 |       |    |---check_processing.py
 |       |    |---employee.py
 |       |    |---example.txt
 |       |    |---format.py
 |       |
 |       |---test_ioet
 |       |    |--test_employee.py
 |       |
 |       |---main.py
 |       |---requirements.txt
 |       |---README.md
```
---

### Usage of main.py

---

`$ python3 main.py --help                 # options how to use it`

`$ python3 main.py -f ./src/employees.txt       # to read from a file`



