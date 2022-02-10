'''
lambda functions:
    In Python, an anonymous function is a function that is defined without a name.
    While normal functions are defined using the def keyword in Python, anonymous
    functions are defined using the lambda keyword. Hence, anonymous functions are also called lambda functions.


1.How to create lambda function    :

    A lambda function is a small anonymous function.
    A lambda function can take any number of arguments, but can only have one expression.

    Syntax:
    lambda arguments : expression


'''

#Example
#Add 10 to argument a, and return the result:
# x = lambda a : a + 10
# print(x(5))


#PROgrams For Lambad Function:

#1.WAP to calculate the square of a number with or without lambda

# numbers=int(input("Enter The number"))
# result=numbers*numbers
# print("Spare Of ",numbers,"is =",result)


# def add(n):
#     return n * n
# print(add(5))

# With lambda Function:

# x = lambda a : a * a
# number=int(input("Enter number"))
# print(x(number))