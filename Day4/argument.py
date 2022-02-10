'''
1. Keyword arguments:
    In Python, the terms parameter and argument are used interchangeably. However, there is a slight distinction between these two terms.
    Parameters are the input variables bounded by parentheses when defining a function,
    whereas arguments are the values assigned to these parameters when passed into a function (or method) during a function call.

'''

# EX:
def fun(x,y):
    c=x+y
    print("Result is =",c)
fun(x=80,y=20)
fun(y=40,x=30)


'''
2.Default arguments in Python:
    Python allows function arguments to have default values. If the function is called without the argument, 
    the argument gets its default value.

'''
#Ex:

def add(a,b=5,c=10):
    return (a+b+c)

#Giving only the mandatory argument
print(add(3))

#Giving one of the optional arguments

print(add(3,4))

#Giving all the arguments

print(add(2,3,4))
'''
3. Variable arguments:

    In this we can pass argument in diffrent number of number of arguments in diffrent functions call.
    it will handle all the arguments using pointer (*)
    
'''

# EX:

def adn(*x):
    for i in x:
        print(i)
adn(1,2,3,4,5)
adn(4,5)
fun("vikas","Nature")

