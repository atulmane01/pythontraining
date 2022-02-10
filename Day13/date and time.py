'''

1. How to use Date and Time Module:

    The datetime module supplies classes for manipulating dates and times. While date and time arithmetic
    is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
    See also Module calendar. General calendar related functions

2. What is the usage of Date and Time Module:
    Python Datetime module supplies classes to work with date and time. These classes provide a
     number of functions to deal with dates, times and time intervals. Date and datetime are an object
      in Python, so when you manipulate them,
     you are actually manipulating objects and not string or timestamps.

     to use we need to import that module

3.WAP to display the usage of it:
    he DateTime module is categorized into 6 main classes –

date – An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. Its attributes are year, month and day.
time – An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. Its attributes are hour, minute, second, microsecond, and tzinfo.
datetime – Its a combination of date and time along with the attributes year, month, day, hour, minute, second, microsecond, and tzinfo.
timedelta – A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
tzinfo – It provides time zone information objects.
timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).

'''
#Get Current Date

from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

#Get Today’s Year, Month, and Date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Get date from Timestamp
from datetime import datetime

# Getting Datetime from timestamp
#The timestamp is the number of seconds from 1st January 1970 at UTC to a particular date.
date_time = datetime.fromtimestamp(663998)
print("Datetime from timestamp:", date_time)

#The time class creates the time object which represents local time, independent of any day.

#Get hours, minutes, seconds, and microseconds

from datetime import time

Time = time(11, 34, 56)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

# Get year, month, hour, minute, and timestamp

a = datetime(1999, 12, 12, 12, 12, 12)

print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

#current date and time

from datetime import datetime
a=datetime.now()
print(a)



