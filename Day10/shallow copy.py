'''
What is the use of shallow copy:
    A shallow copy constructs a new compound object and then (to the extent possible) inserts references
    into it to the objects found in the original. A deep copy constructs a new compound object and then,
    recursively, inserts copies into it of the objects found in the original
'''
# Example:
# numbers=[1,3,5,7,80,34]
#
# new_numbers=numbers
#
# numbers[0]=100
# print(numbers)


#it can change the original object

import copy

old_list=[[0,1,2],[4,6,7],[7,2,7]]

new_list=copy.copy(old_list)

new_list[0]=['a','b','c']

print(old_list)
print(new_list)