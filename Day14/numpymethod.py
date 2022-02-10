'''
Filtering Arrays:
    Getting some elements out of an existing array and creating a new array out of them is called filtering.

    In NumPy, you filter an array using a boolean index list.

    A boolean index list is a list of booleans corresponding to indexes in the array.

    If the value at an index is True that element is contained in the filtered array, if the value
    at that index is False that element is excluded from the filtered array.

'''
#1D Array
import numpy as np
#
# arr = np.array([41, 42, 43, 44])
#
# x = [True, False, True, False]
#
# newarr = arr[x]
#
# print(newarr)

#Create a filter array that will return only values higher than 42:

# arr = np.array([41, 42, 43, 44])
#
# filter_arr = arr > 42
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)

#2D-Array

# arr = np.array([[41, 42, 43, 44],[5,78,66,33]])
#
# filter_arr = arr > 42
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)

#3D array:

# arr = np.array([[41, 42, 43, 44],[5,78,66,33],[3,60,77,8]])
#
# filter_arr = arr > 42
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)

'''
2.search:
    Searching Arrays
    You can search an array for a certain value, and return the indexes that get a match.

    To search an array, use the where() method.
'''
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 4)
#
# print(x)


#even arrays

# arr = np.array([1, 2, 3, 8])
#
# x = np.where(arr%2 == 0)
#
# print(x)


'''
Search Sorted:
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

The searchsorted() method is assumed to be used on sorted arrays.
'''

arr = np.array([1,3,5,7])

x = np.searchsorted(arr,6)

print(x)


'''

3.Split():
    Splitting is reverse operation of Joining.

    Joining merges multiple arrays into one and Splitting breaks one array into multiple.
    
    We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.


'''
# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)




'''
Sorting Arrays:
    Sorting means putting elements in an ordered sequence.
    
    Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
    
    The NumPy ndarray object has a function called sort(), that will sort a specified array.
'''
#
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))
# # Sort the array alphabetically:
# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))
# #sorting 2 dimenshiona;
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print("2 Dimenshions")
# print(np.sort(arr))
# #sorting 3 Dimenshions
# arr=np.array([[[1, 5, 3], [4, 9, 6]], [[1, 10, 2], [4, 8, 6]]])
# print("3 Dimenshions")
# print(np.sort(arr))


#Add element to Numpy Array using append()
# arr = np.array([11, 2, 6, 7, 2])
# # Add / Append an element at the end of a numpy array
# new_arr = np.append(arr, 10)
# print('New Array: ', new_arr)
# print('Original Array: ', arr)


#Add element to Numpy Array using concatenate()

# arr = np.array([11, 2, 6, 7, 2])
# # Add / Append an element at the end of a numpy array
# new_arr = np.concatenate( (arr, [10] ) )
# print('New Array: ', new_arr)
# print('Original Array: ', arr)



