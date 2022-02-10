'''
What is Constructor Overriding:

    Method overriding is an ability of any object-oriented programming language that allows a subclass
    or child class to provide a specific implementation of a
    method that is already provided by one of its super-classes or parent classes
'''

# Example:

class Father:
    def __init__(self):
        self.money=1000
        print("Father Class ")
    def show(self):
        print("Show Method")


class Son(Father):
    def __init__(self):
        self.money=1500
        self.car='BMW'
        print("son class Constructor")

    def disp(self):
        print("son class")

s=Son()
print(s.money)


