'''

1. How to use Time Module:

    for use of Time Module we need to import time
    Sysntax:
        import time

2. What is the usage of Time Module:
    The Python time module represents time-based objects in Python. Developers use time() function returns the current
    time as a UNIX timestamp.
    The ctime() function translates a UNIX timestamp into a standard year, month, day, and time format

3.WAP to display the usage of it:
'''

# Example:
import  time

'''
Python time.time():
    The time() function returns the number of seconds passed since epoch.
    
    For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
'''
seconds = time.time()
print("Seconds since epoch =", seconds)


'''
Python time.ctime():
    The time.ctime() function takes seconds passed since epoch as an argument and returns a string representing local time.
'''
# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

'''
Python time.sleep():
    The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
'''
print("Next msg will be printed next 2 sec.")
time.sleep(2)
print("This is printed after 2 seconds.")

'''
Python time.localtime():
    The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in local time.

'''
result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

'''

Ask about 9 parameters what he actually getting :IMP 

Python time.asctime():
    he asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time)
     as an argument and returns a string representing it.
'''
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)