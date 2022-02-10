'''

1. Try Block:

    The try block lets you test a block of code for errors.
    The try block will generate an exception, because x is not defined:
    Since the try block raises an error, the except block will be executed.
    Without the try block, the program will crash and raise an error:

'''
# Example:

# try:
#   print(x)
# except:
#   print("An exception occurred")


'''
2. Try with multiple except:
    You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special 
    kind of error:
    
    
    except :
        except block is used for the to cathch an expression that is raised in the try block .
        there can be multiple except block for try block
    

'''

# Example:
# x=123
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

'''
3.Try with except and else:

Else:  this block will get excuted when no exception is raised .Else block is excuted after try block

'''
# Example:

# try:
#     print("Hello")
# except:
#     print("except")
# else:
#     print("not wrong")


'''
4 .Finally Keyword:
    The finally block, if specified, will be executed regardless if the try block raises an error or not.
    This can be useful to close objects and clean up resources
    
    This block will excuted irrespective of weather there is an exception  or not
'''
# Example

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
'''

5.raise keyword:
    The raise keyword is used to raise an exception.
    You can define what kind of error to raise, and the text to print to the user.
'''
# Example:

# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")



#Example:
a=10
b=0

try:
    d=a/b
    print(d)
    print("Inside try block")

except ZeroDivisionError:
    print("Division By zero is ot allowed")

else:
    print("Inside Else")

finally:
    print("Inside Finally")

print("Rest of code ")