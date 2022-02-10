'''
1. How to create a class:
    To create a class, use the keyword class:


    Create a class named MyClass, with a property named x:
EX
    class MyClass:
        x = 5
'''


'''
2.What are attributes and behaviour of a class:
  
    Attributes are the characteristics of the class that help to distinguish it from other classes. 
    Behaviors are the tasks that an object performs. A person's attributes, for example, include their age, name, and height, 
    while their behaviors include the fact that a person can speak, run, walk, and eat.
    
'''

'''
3.How to write a class using constructor alongwith usage of it:
    A constructor is a special type of method (function) which is used to initialize the instance members of the class.
    


'''

# Example:

class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
# accessing display() method to print employee 1 information
emp1.display()
# accessing display() method to print employee 2 information
emp2.display()
