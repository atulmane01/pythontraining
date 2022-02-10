'''
1.Map() Function:
    map() function returns a map object(which is an iterator) of the results after applying the given function
    to each item of a given iterable (list, tuple etc.)

    Sysntax:
    map(fun, iter)

    Parameters:
            fun : It is a function to which map passes each element of given iterable.
            iter : It is a iterable which is to be mapped.

'''

#Programs For Map:

#1.WAP to double all the value in a list without map function and without lambda expression

# n = [3, 5, 7]
#
# def double(lst):
#
#     return [x * 2 for x in lst]
#
# print(double(n))


#2.WAP to double all the value in a list with map function and with lambda expression
#with MAp Function

# def addition(n):
#     return n + n
# # We double all numbers using map()
#
# numbers = [1, 2, 3, 4]
# result = map(addition, numbers)
# print(list(result))


#With lmbada and map Functiion

# Double all numbers using map and lambda


# numbers = [1, 9, 3, 4]
# result = map(lambda x: x + x, numbers)
# print(list(result))

