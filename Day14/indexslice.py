'''
1.Indexing:
    Array indexing is the same as accessing an array element. You can access an array element by referring to
    its index number. The indexes in NumPy arrays start with 0,
     meaning that the first element has index 0, and the second has index 1
'''

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

print(arr[1])

'''
Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
'''

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

print('5th element on 2nd row: ', arr[1, 4])


'''
Access 3-D Arrays
To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.


'''

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


'''
2.Slicing:
    Slicing in python means taking elements from one given index to another given index.

    We pass slice instead of index like this: [start:end].
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[0:5])


# Example
# Slice elements from index 4 to the end of the array:

import numpy as np

arr = np.array([1,2, 3, 4, 5, 6, 7])

print(arr[1:])


#Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0, 1:4])

