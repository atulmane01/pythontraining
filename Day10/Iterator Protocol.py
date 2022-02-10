'''
1.Iterator Protocol:
    Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions,
    generators etc. but are hidden in plain sight.

    Iterator in Python is simply an object that can be iterated upon.
    An object which will return data, one element at a time.

    Technically speaking, a Python iterator object must implement two special methods,
    1)__iter__() and
    2)__next__(),
                collectively called the iterator protocol.


    1)iter():
            The iter() function (which in turn calls the __iter__() method) returns an iterator from them

            We use the next() function to manually iterate through all the items of an iterator.
            When we reach the end and there is no more data to be returned, it will raise the StopIteration Exception
'''
# Example:
# define a list
# my_list = [4, 7, 0, 3]
#
# # get an iterator using iter()
# my_iter = iter(my_list)
#
# # iterate through it using next()
#
# # Output: 4
# print(next(my_iter))
#
# # Output: 7
# print(next(my_iter))
#
#
# # next(obj) is same as obj.__next__()
#
# # Output: 0
# print(my_iter.__next__())
#
# # Output: 3
# print(my_iter.__next__())
#
# # This will raise error, no items left
# next(my_iter)


'''
    A more elegant way of automatically iterating is by using the for loop. Using this, 
    we can iterate over any object that can return an iterator, for example list, string, file etc.
'''

# Example:

my_list = [4, 7, 0, 3]

for element in my_list:
    print(element)
