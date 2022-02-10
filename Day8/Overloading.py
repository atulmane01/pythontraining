'''

method overloading:
    Methods in Python can be called with zero, one, or more parameters. This process of calling the
    same method in different ways is called method overloading. ... Two methods cannot have the same name in Python;
    hence method overloading is a feature that allows the same operator to have different meanings

'''
# Example:

# Program to illustrate method overloading
class Example:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        return s

obj=Example()
print(obj.sum(10,20))
