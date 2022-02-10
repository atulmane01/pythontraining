'''
1.Uses of Generator:
    Python Generator functions allow you to declare a function that behaves likes an iterator,
    allowing programmers to make an iterator in a fast, easy, and clean way. An iterator is an
    object that can be iterated or looped upon.
    It is used to abstract a container of data to make it behave like an iterable object


    Genrators are a function that return an sequences of values we use yeid statement to return the value from function


    yield  Stattement :
        Yield statemet returns the the elements from a genrator fuction into a genrtor object

        EX :
        yield a


    next()function:
        This function is used to retrive elemnyt by elemnt from a genrator object.

'''

# def show(a,b):
#     while a<=b:
#         yield a
#         a+=1
#         except StopIteration:
#             break
# result=show(1,5)
#
#
#
# for i in result:
#     print(i)



a=[2,3,4,5]

def value(x):
    for i in x:
        yield i

def error(i):
    try:
        val=next(i)
        print(val)
    except StopIteration:
        print("Done")

b=value(a)
error(b)
error(b)
error(b)
error(b)
error(b)