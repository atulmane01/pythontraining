'''
Python Module:
    Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program.

    1.Time:
        This module provides various time-related functions
        As the name suggests Python time module allows to work with time in Python. It allows functionality like getting the current
        time, pausing the Program from executing, etc

        The time module comes with Python’s standard utility module, so there is no need to install it externally.
        We can simply import it using the import statement.

'''

#Example

import time

print(time.ctime())


'''
2.Calender:
    Python defines an inbuilt module calendar that handles operations related to the calendar. 
    
    The calendar module allows output calendars like the program and provides additional useful functions related to the calendar
    
    
'''
# Example:

import calendar

yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))


'''
3.Date and Time:
    module named datetime can be imported to work with the date as well as time. Python Datetime module comes built into Python, 
    so there is no need to install it externally. 
    
    
'''

from datetime import date

today = date.today()

print("Today's date is", today,"with current time is :",time.ctime())