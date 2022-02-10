#What is Inheritance:

'''

Inheritance is the capability of one class to derive or inherit the properties from another class.
    The class that derives properties is called the derived class or base class and the class from which
    the properties are being derived is called the base class or parent class.

    Types:
    1.Single Inheritance
    2.Multiple Inheritance
    3.Multilevel Inheritance
    4.Hierarchical Inheritance
    5.Hybrid Inheritance

'''



'''
1. Single inheritance: 
    When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
    Inheritance is an important aspect of the object-oriented paradigm. Inheritance provides code reusability to the program 
    because we can use an existing class to create a new class instead of creating it from scratch.


'''
# Example:

# class Parent:
#     def fucn1(self):
#         print("This is parent function")
#
# class Child(Parent):
#     def funct2(self):
#         print("this is child function")
#
# obj=Child()
# obj.fucn1()
# obj.funct2()
#


'''
2. Multiple inheritance: 
    When a child class inherits from multiple parent classes, it is called multiple inheritance. 
    
'''


# Python example to show the working of multiple

# class Parent:
#     def fucn1(self):
#         print("This is parent function")
#
# class Parent1:
#     def fucn3(self):
#         print("This is function 3")
#
# class Child(Parent,Parent1):
#     def funct2(self):
#         print("this is child function")
#
# obj=Child()
# obj.fucn1()
# obj.fucn3()



#3. Multilevel inheritance: When we have a child and grandchild relationship.
'''
Multi-Level inheritance is possible in python like other object-oriented languages. 
Multi-level inheritance is archived when a derived class inherits another derived class. There is no limit on the number of 
levels up to which, the multi-level inheritance is archived in python.'''


class Parent:
    def fucn1(self):
        print("This is parent function")

class Parent1(Parent):
    def fucn3(self):
        print("This is function 3")

class Child(Parent1):
    def funct2(self):
        print("this is child function")

obj=Child()
obj.fucn1()
obj.funct2()
obj.fucn3()


'''
4.Hierarchical Inheritance:

        When two or more classes inherits a single class, it is known as hierarchical inheritance
'''
# Example:

# class Parent:
#     def fucn1(self):
#         print("This is parent function")
#
# class Parent2(Parent):
#     def fucn3(self):
#         print("This is function 3")
#
# class Child(Parent):
#     def funct2(self):
#         print("this is child function")
#
# obj=Child()
# obj1=Parent2()
# obj.fucn1()
# obj1.fucn1()


'''
5.Hybrid Inheritance:
    Hybrid inheritance is a combination of multiple inheritance and multilevel inheritance. 
    A class is derived from two classes as in multiple inheritance. However, one of the parent classes 
    is not a base class. It is a derived class.
'''
# Example:
#
class Parent:
    def fucn1(self):
        print("This is parent function")

class Parent2(Parent):
    def fucn3(self):
        print("This is function 3")

class Parent3:
    def fucn4(self):
        print("This is function 4")

class Child(Parent,Parent3):
    def funct2(self):
        print("this is child function")

obj=Child()
obj.fucn1()
obj.fucn4()

