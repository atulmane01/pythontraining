'''

Create a NumPy ndarray Object:
    NumPy is used to work with arrays. The array object in NumPy is called ndarray.
    We can create a NumPy ndarray object by using the array() function.


'''
import numpy as np
#
#
# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
#
# print(type(arr))


'''
Use a tuple to create a NumPy array:
'''
# import numpy as np
#
# arr = np.array((1, 2, 3, 4, 5))
#
# print(arr)


'''
Dimensions in Arrays:
    0-D Arrays:
        0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
'''
# arr = np.array(4)
#
# print(arr)


'''
1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.


'''
#Create a filter array that will return only even elements from the original array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

'''
2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.
'''
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(arr)

'''
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
# '''
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(arr)

#program to check number of dimesndhions

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)