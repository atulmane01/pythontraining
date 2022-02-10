'''
Types of Functions in Python:

1.Python Function with No argument and No Return value:
    In this type of function in Python, While defining, declaring, or calling the function, We won’t pass any arguments to the function.
    This type of Python function won’t return any value when we call the function.
'''
#
# EX:
# Python Function with No Arguments, and No Return Value
# def Adding():
#     a = 20
#     b = 30
#     Sum = a + b
#     print("After Calling the Function:", Sum)
# Adding()
'''
2.Python Function with no argument and with a Return value:
    In this type of function in Python, We won’t pass any arguments to the function while defining, declaring, or calling the function.
     When we call the Python function, this type of function returns some value.

'''
# Ex:

# Python Function with No Arguments, and with Return Value
# def Multiplication():
#     a = 10
#     b = 25
#     Multi = a * b
#     return Multi
# print("After Calling the Multiplication Function: ", Multiplication())

'''
3.Python Function with argument and No Return value:
    If you observe the above 2 types of functions, No matter how many times you executive, Python gives the same output. 
    We don’t have any control over the variable values (a, b) because they are fixed values. 
    In real-time, we mostly deal with dynamic data means we have to allow the user to enter his own values rather than fixed ones.

'''

# EX:

# Python Function with Arguments, and NO Return Value
# def Multiplications(a, b):
#     Multi = a * b
#     print("After Calling the Function:", Multi)
#
# Multiplications(10, 20)

'''
4.Python Function with argument and Return value:
    This type of python function allows us to pass the arguments to the function while calling the function. 
    This type of functions in Python returns some value when we call the function.
    
'''
# EX:
# Python Function with Arguments, and NO Return Value
# def Addition(a, b):
#     Sum = a + b
#     return Sum
# # We are calling the Function Outside the Function Definition
# print("After Calling the Function:", Addition(25, 45))
