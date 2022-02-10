'''
How to use Calendar Module:
    The calendar module allows output calendars like the program and provides additional useful
    functions related to the calendar. Functions and classes defined in the Calendar module use an
    idealized calendar, the current Gregorian calendar extended indefinitely in both directions

    Python defines an inbuilt module calendar that handles operations related to the calendar.

    for use we need to import calender module


2.What is the usage of Calendar Module:

The primary practical use of a calendar is to identify days: to be informed about
or to agree on a future event and to record an event that has happened.

3.WAP to display the usage of it:

'''
 #1: Display the Calendar of a given month.

# import module
import calendar

yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))

# 2: Display calendar of the given year.

print ("The calendar of year 2018 is : ")
print (calendar.calendar(2018))


## isleap() and leapdays()

import calendar

# using isleap() to check if year is leap or not
if (calendar.isleap(2008)):
    print("The year is leap")
else:
    print("The year is not leap")

# using leapdays() to print leap days between years
print("The leap days between 1950 and 2000 are : ", end="")
print(calendar.leapdays(1998, 2002))

