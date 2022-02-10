'''
    overriding:
    Overriding is the property of a class to change the implementation of a method provided by one of its base classes.
    ... In Python method overriding occurs by simply defining in the child class a method with the same name of a method
        in the parent class.
'''

# Example:

# Python program to demonstrate
# method overriding

class Example:
    def result(self,x,y):
        c=x*y
        print("Multiplication is=",c)

class Add(Example):
    def result(self,a,b):
        # super().result(10,20)
        z=a+b
        print("Addition is =",z)

obj=Add()

obj.result(10,20)