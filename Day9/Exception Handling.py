'''

1 .What do you mean by Exception Handling:
    Exceptions are raised when the program is syntactically correct, but the code resulted in an error.
    This error does not stop the execution of the program,
    however, it changes the normal flow of the program

    Types Of Exception:
        1.Built in Exception:
            exception which are already available in python language .the base class for all built in exception in BaseException class
            1.DivideByZero
            2.NameError

        2.UserDefined Exception :
            A programmer can create his own exception called user-defined exception

'''
# Example:
#
# # initialize the amount variable
# marks = 10000
#
# # perform division with 0
# a = marks / 0
# print(a)


'''
2. Why exception handing is important:
    Python provides a way to handle the exception so that the code can be executed without any interruption. 
    If we do not handle the exception,
    the interpreter doesn't execute all the code that exists after the exception.
    
    
    Exception handling allows you to separate error-handling code from normal code. 
    An exception is a Python object which represents an error. As with code comments, exceptions helps you to remind yourself of what the program expects.
    It clarifies the code and enhances readability
'''
# Example:
marks=1000
try:
    a = marks / 0
    print(a)

except ZeroDivisionError as est:
    print(est)