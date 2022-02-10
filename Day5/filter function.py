'''
1.Filter Function:
    The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not

    syntax:

        filter(function, sequence)

        Parameters:
        function:
            function that tests if each element of a
        sequence true or not.
        sequence:
            sequence which needs to be filtered, it can
        be sets, lists, tuples, or containers of any iterators.

'''
#Example of Filter
# age=[4,3,25,35,5,69]
# def filtermethod(x):
#     if x < 18:
#         return False
#     else:
#         return True
# adult=list(filter(filtermethod,age))
#
# for i in adult:
#     print(i)


#with the help of lambda
# age=[4,3,25,35,5,69]
#
# adult=list(filter(lambda a:a>18,age))
#
# print(adult)





#1.WAP to filter even number in a list without filter and lambda expression

# numbers=[2,8,9,48,75]
# secondlst=[]
# for i in numbers:
#     if (i%2==0):
#         secondlst.append(i)
# print(secondlst)

#2.WAP to filter even number in a list with filter and lambda function

# lst = [0, 15, 25, 30, 5, 8, 13]
# result = filter(lambda x: x % 2 == 0, lst)
# print(list(result))

#
# nums = [1, 2, 3, 4, 5, 6, 7]
#
# def fun(a):
#     return a+a+a
# # result = map(lambda x: x + x + x, nums)
#
# a=list((map(fun,nums)))
# print(a)


# lis1 = [1, 2, 3, 4, 5]
#
# is_even = lambda x: x % 2 == 0
#
# is_odd=lambda x:x % 2 != 0
#
# # using filter
# lis2 = list(filter(is_even, lis1))
# list3 = list(filter(is_odd, lis1))
#
# # Printing output
# print("even Numbers " ,lis2)
# print("Odd Numbers",list3)

a=[6,2,3]
b=[1,1,6]
c=[9,5,11]
result=map(lambda p,q,r : p+q+r, a,b,c )
print(list(result))


